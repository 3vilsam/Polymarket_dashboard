/* Build data/live.json for the Pages artifact. Read-only public GETs.
 * Does not commit. Math is edges.js; this file only fetches and trims. */
"use strict";

var fs = require("fs");
var path = require("path");
var PM = require("../edges.js");

var GAMMA = "https://gamma-api.polymarket.com/events";
var BOOKS = "https://clob.polymarket.com/books";
var MYT = "Asia/Kuala_Lumpur";
var STARTED = Date.now();
var DEADLINE_MS = 100000;
var FETCH_MS = 15000;
var PACE_MS = 200;
var LEVELS = 5;

function deadline() {
  if (Date.now() - STARTED > DEADLINE_MS) throw new Error("mirror build exceeded 100s budget");
}

function sleep(ms) {
  return new Promise(function (resolve) { setTimeout(resolve, ms); });
}

function fetchJSON(url, options) {
  deadline();
  var opts = options || {};
  opts.signal = AbortSignal.timeout(FETCH_MS);
  return fetch(url, opts).then(function (res) {
    if (!res.ok) throw new Error(url.split("?")[0] + " HTTP " + res.status);
    return res.json();
  });
}

function fetchEvents() {
  var out = [];
  var page = 0;
  function next() {
    deadline();
    var url = GAMMA + "?active=true&closed=false&limit=100&offset=" + (page * 100) + "&order=volume24hr&ascending=false";
    return fetchJSON(url).then(function (batch) {
      if (!Array.isArray(batch) || !batch.length) return out;
      out = out.concat(batch);
      page++;
      if (batch.length < 100 || page >= 3) return out;
      return sleep(PACE_MS).then(next);
    });
  }
  return next();
}

function fetchBooks(tokens) {
  var uniq = [];
  var seen = new Set();
  tokens.forEach(function (t) {
    if (t && !seen.has(t)) { seen.add(t); uniq.push(t); }
  });
  uniq = uniq.slice(0, PM.MAX_TOKENS);
  var books = {};
  var i = 0;
  function next() {
    if (i >= uniq.length) return books;
    deadline();
    var chunk = uniq.slice(i, i + 100);
    i += 100;
    return fetchJSON(BOOKS, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(chunk.map(function (t) { return { token_id: t }; }))
    }).then(function (res) {
      (res || []).forEach(function (b) {
        if (b && b.asset_id) books[String(b.asset_id)] = b;
      });
      if (i >= uniq.length) return books;
      return sleep(PACE_MS).then(next);
    });
  }
  return next();
}

function trimLevels(levels) {
  if (!Array.isArray(levels)) return [];
  var out = [];
  for (var i = 0; i < levels.length && out.length < LEVELS; i++) {
    var level = levels[i];
    if (level && typeof level === "object" && !Array.isArray(level)) out.push({ price: level.price, size: level.size });
    else if (Array.isArray(level)) out.push(level.slice(0, 2));
  }
  return out;
}

function trimBook(book) {
  return { asks: trimLevels(book && book.asks), bids: trimLevels(book && book.bids) };
}

function slimRow(r) {
  return {
    kind: r.kind,
    event_slug: r.event_slug,
    event_title: r.event_title,
    market_slug: r.market_slug,
    question: r.question,
    n_legs: r.n_legs,
    fee_rate: r.fee_rate,
    fee_rates: r.fee_rates,
    fee_rate_source: r.fee_rate_source,
    sum_ask: r.sum_ask,
    edge_bps_pre_fee: r.edge_bps_pre_fee,
    edge_bps: r.edge_bps,
    edge_bps_after_slip: r.edge_bps_after_slip,
    passes_300bps: r.passes_300bps,
    still_ge_300: r.still_ge_300,
    volume24hr: r.volume24hr,
    leg_tokens: r.leg_tokens
  };
}

function fmtMYT(d) {
  var parts = new Intl.DateTimeFormat("en-GB", {
    timeZone: MYT, year: "numeric", month: "2-digit", day: "2-digit",
    hour: "2-digit", minute: "2-digit", second: "2-digit", hour12: false
  }).formatToParts(d);
  function g(type) {
    for (var i = 0; i < parts.length; i++) if (parts[i].type === type) return parts[i].value;
    return "00";
  }
  return g("year") + "-" + g("month") + "-" + g("day") + " " + g("hour") + ":" + g("minute") + ":" + g("second") + " MYT";
}

fetchEvents().then(function (events) {
  if (!events.length) throw new Error("no events from Gamma");
  var jobs = PM.collectJobs(events);
  return fetchBooks(jobs.tokens).then(function (books) {
    var res = PM.evaluate(jobs, books);
    var summary = {};
    res.rows.forEach(function (r) {
      (r.leg_tokens || []).forEach(function (tok) {
        if (tok && books[tok] && !summary[tok]) summary[tok] = trimBook(books[tok]);
      });
    });
    var now = new Date();
    var payload = {
      generated_at_utc: now.toISOString(),
      generated_at_myt: fmtMYT(now),
      counts: {
        events: events.length,
        markets: PM.countMarkets(events),
        binary: res.rows.filter(function (r) { return r.kind === "binary_complement"; }).length,
        baskets: res.rows.filter(function (r) { return r.kind === "negrisk_basket"; }).length,
        skipped: jobs.skippedCap + res.skippedBooks,
        pass: res.nPass,
        still: res.rows.filter(function (r) { return r.passes_300bps && r.still_ge_300; }).length
      },
      edges: res.rows.map(slimRow),
      books: summary
    };
    var dir = path.join(__dirname, "..", "data");
    fs.mkdirSync(dir, { recursive: true });
    var file = path.join(dir, "live.json");
    fs.writeFileSync(file, JSON.stringify(payload));
    var bytes = fs.statSync(file).size;
    console.log("live.json events=" + payload.counts.events + " markets=" + payload.counts.markets + " edges=" + payload.edges.length + " books=" + Object.keys(summary).length + " bytes=" + bytes + " ms=" + (Date.now() - STARTED));
  });
}).catch(function (err) {
  console.error(err && err.stack ? err.stack : err);
  process.exit(1);
});
