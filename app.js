/* Live, read-only dashboard. PAPER ONLY. GETs public Gamma events and reads
 * public CLOB order books (POST /books is Polymarket's public batch *read*;
 * no auth, no orders). Math lives in edges.js (ported from scan.py/paper.py). */
(function () {
  "use strict";
  var GAMMA = "https://gamma-api.polymarket.com/events";
  var BOOKS = "https://clob.polymarket.com/books";
  var PRICE_MS = 60000, EVENTS_MS = 300000, STATIC_MS = 600000, MAX_BACKOFF_MS = 600000;
  var MYT = "Asia/Kuala_Lumpur";

  var st = { events: null, eventsAt: 0, booksAt: 0, rows: [], tab: "binary_complement",
             sortKey: "edge_bps", sortDir: -1, fails: 0, timer: null, paused: false,
             staticAt: 0, busy: false, counts: null };

  function $(id) { return document.getElementById(id); }
  function el(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text !== undefined) e.textContent = text; return e; }
  function fmtMYT(ms) {
    if (!ms) return "—";
    return new Intl.DateTimeFormat("en-GB", { timeZone: MYT, day: "2-digit", month: "short", hour: "2-digit", minute: "2-digit", second: "2-digit", hour12: false }).format(new Date(ms)) + " MYT";
  }
  function bps(v) { return v === null || v === undefined ? "—" : (v >= 0 ? "+" : "") + v.toFixed(0); }
  function cls(v) { return v === null || v === undefined ? "" : (v >= 300 ? "pos" : (v < 0 ? "neg" : "")); }
  function money(v) { if (!v) return "—"; return v >= 1e6 ? (v / 1e6).toFixed(1) + "M" : v >= 1e3 ? (v / 1e3).toFixed(0) + "k" : v.toFixed(0); }
  function safeUrl(u) { return typeof u === "string" && /^https:\/\//i.test(u) ? u : null; }
  function link(href, text) { var a = el("a", null, text); a.href = href; a.target = "_blank"; a.rel = "noopener noreferrer"; return a; }

  function getJSON(url) {
    return fetch(url, { method: "GET", credentials: "omit", cache: "no-store", referrerPolicy: "no-referrer" })
      .then(function (r) { if (!r.ok) throw new Error(url.split("?")[0] + " HTTP " + r.status); return r.json(); });
  }

  function fetchEvents() {
    var out = [], page = 0;
    function next() {
      var url = GAMMA + "?active=true&closed=false&limit=100&offset=" + page * 100 + "&order=volume24hr&ascending=false";
      return getJSON(url).then(function (batch) {
        if (!Array.isArray(batch) || !batch.length) return out;
        out = out.concat(batch); page++;
        if (batch.length < 100 || page >= 3) return out;
        return new Promise(function (r) { setTimeout(r, 150); }).then(next);
      });
    }
    return next();
  }

  function fetchBooks(tokens) {
    var uniq = [], seen = new Set();
    tokens.forEach(function (t) { if (t && !seen.has(t)) { seen.add(t); uniq.push(t); } });
    uniq = uniq.slice(0, PM.MAX_TOKENS);
    var books = {}, chunks = [];
    for (var i = 0; i < uniq.length; i += 100) chunks.push(uniq.slice(i, i + 100));
    return chunks.reduce(function (p, chunk) {
      return p.then(function () {
        return fetch(BOOKS, { method: "POST", credentials: "omit", cache: "no-store", referrerPolicy: "no-referrer",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(chunk.map(function (t) { return { token_id: t }; })) })
          .then(function (r) { if (!r.ok) throw new Error("CLOB books HTTP " + r.status); return r.json(); })
          .then(function (res) { (res || []).forEach(function (b) { if (b && b.asset_id) books[String(b.asset_id)] = b; }); })
          .then(function () { return new Promise(function (r) { setTimeout(r, 150); }); });
      });
    }, Promise.resolve()).then(function () { return books; });
  }

  function loadStatic() {
    var v = "?t=" + Date.now();
    return Promise.all([
      getJSON("status.json" + v).catch(function () { return null; }),
      getJSON("paper.json" + v).catch(function () { return null; }),
      getJSON("airdrops.json" + v).catch(function () { return null; })
    ]).then(function (r) {
      st.staticAt = Date.now();
      if (r[0]) { st.paused = !!r[0].paused; $("builtAt").textContent = r[0].built_at_myt || "—"; }
      if (r[1]) renderPaper(r[1]);
      if (r[2]) renderAirdrops(r[2]);
    });
  }

  function refresh() {
    if (st.busy) return Promise.resolve();
    st.busy = true;
    var p = Date.now() - st.staticAt > STATIC_MS ? loadStatic() : Promise.resolve();
    return p.then(function () {
      if (st.paused) { badge(); return; }
      var needEvents = !st.events || Date.now() - st.eventsAt > EVENTS_MS;
      return (needEvents ? fetchEvents().then(function (ev) { if (ev.length) { st.events = ev; st.eventsAt = Date.now(); } }) : Promise.resolve())
        .then(function () {
          if (!st.events) throw new Error("no events from Gamma");
          var jobs = PM.collectJobs(st.events);
          return fetchBooks(jobs.tokens).then(function (books) {
            var res = PM.evaluate(jobs, books);
            st.rows = res.rows; st.booksAt = Date.now(); st.fails = 0;
            st.counts = { events: st.events.length, markets: PM.countMarkets(st.events),
              binary: res.rows.filter(function (r) { return r.kind === "binary_complement"; }).length,
              baskets: res.rows.filter(function (r) { return r.kind === "negrisk_basket"; }).length,
              skipped: jobs.skippedCap + res.skippedBooks, pass: res.nPass,
              still: res.rows.filter(function (r) { return r.passes_300bps && r.still_ge_300; }).length };
            $("error").hidden = true;
            render();
          });
        });
    }).catch(function (e) {
      st.fails++;
      var err = $("error"); err.hidden = false;
      err.textContent = "Refresh failed (" + (e && e.message ? e.message : "network") + "). Retrying with back-off; last good data stays on screen.";
    }).then(function () { st.busy = false; badge(); schedule(); });
  }

  function delay() { return st.fails ? Math.min(PRICE_MS * Math.pow(2, st.fails), MAX_BACKOFF_MS) : PRICE_MS; }
  function schedule() {
    clearTimeout(st.timer);
    var d = st.paused ? STATIC_MS : delay();
    st.timer = setTimeout(function () { if (document.hidden) { schedule(); return; } refresh(); }, d);
    $("next").textContent = (st.paused ? "checking kill switch again in " : "next refresh in ~") + Math.round(d / 1000) + " s";
  }
  function badge() {
    var b = $("badge");
    if (st.paused) { b.className = "badge paused"; b.textContent = "paused (STOP)"; return; }
    var live = st.booksAt && Date.now() - st.booksAt < 150000;
    b.className = "badge " + (live ? "live" : "stale"); b.textContent = live ? "live" : (st.booksAt ? "stale" : "loading");
    $("updated").textContent = fmtMYT(st.booksAt); $("eventsUpdated").textContent = fmtMYT(st.eventsAt);
  }

  function render() {
    var c = st.counts || {};
    $("cEvents").textContent = c.events; $("cMarkets").textContent = c.markets; $("cBinary").textContent = c.binary;
    $("cBaskets").textContent = c.baskets; $("cSkipped").textContent = c.skipped; $("cPass").textContent = c.pass; $("cStill").textContent = c.still;
    badge(); renderTable();
  }

  function renderTable() {
    var rows = st.rows.filter(function (r) { return r.kind === st.tab; }).map(function (r) {
      r.fee_rate_num = r.fee_rates[0]; return r; });
    var k = st.sortKey, d = st.sortDir;
    rows.sort(function (a, b) {
      var x = a[k], y = b[k];
      if (x === null || x === undefined) return 1; if (y === null || y === undefined) return -1;
      if (typeof x === "string") return d * x.localeCompare(y);
      return d * (x - y);
    });
    var tb = document.querySelector("#edges tbody"); tb.textContent = "";
    rows.slice(0, 40).forEach(function (r) {
      var tr = el("tr");
      var td = el("td", "title");
      var url = "https://polymarket.com/event/" + encodeURIComponent(r.event_slug);
      td.appendChild(link(url, r.kind === "negrisk_basket" ? r.event_title + " (" + r.n_legs + " outcomes)" : (r.question || r.event_title)));
      tr.appendChild(td);
      var rateTxt = r.kind === "negrisk_basket" ? (new Set(r.fee_rates).size === 1 ? String(r.fee_rates[0]) : "mixed") : String(r.fee_rate);
      tr.appendChild(el("td", "num", rateTxt));
      tr.appendChild(el("td", "num", r.sum_ask.toFixed(3)));
      tr.appendChild(el("td", "num " + cls(r.edge_bps_pre_fee), bps(r.edge_bps_pre_fee)));
      tr.appendChild(el("td", "num " + cls(r.edge_bps), bps(r.edge_bps)));
      var s = el("td", "num " + cls(r.edge_bps_after_slip), r.edge_bps_after_slip === null ? "thin book" : bps(r.edge_bps_after_slip));
      tr.appendChild(s);
      tr.appendChild(el("td", "num", money(r.volume24hr)));
      tb.appendChild(tr);
    });
    $("edgesNote").textContent = rows.length + " " + (st.tab === "binary_complement" ? "binary markets" : "baskets") +
      " checked; showing top 40. Green = at or above the 300 bps bar. \"thin book\" = not enough depth for 10 shares.";
    document.querySelectorAll("#edges th").forEach(function (th) {
      var base = th.textContent.replace(/ [▲▼]$/, "");
      th.textContent = base + (th.getAttribute("data-k") === k ? (d < 0 ? " ▼" : " ▲") : "");
    });
  }

  function renderPaper(p) {
    $("paperAsOf").textContent = p.as_of_myt || "—";
    var pc = $("paperCards"); pc.textContent = "";
    [["runs", p.summary.runs], ["candidates", p.summary.candidates], ["kept after slippage", p.summary.kept],
     ["booked P&L (USDC)", p.summary.booked_pnl_usdc.toFixed(2)]].forEach(function (x) {
      var c = el("div", "card"); c.appendChild(el("div", "n", String(x[1]))); c.appendChild(el("div", "l", x[0])); pc.appendChild(c);
    });
    var tb = document.querySelector("#fills tbody"); tb.textContent = "";
    if (!p.fills.length) { var tr0 = el("tr"); var td0 = el("td", "muted", "No hypothetical fills yet."); td0.colSpan = 6; tr0.appendChild(td0); tb.appendChild(tr0); }
    p.fills.forEach(function (f) {
      var tr = el("tr");
      tr.appendChild(el("td", null, f.ts_myt));
      tr.appendChild(el("td", "title", f.event_title + " (" + f.kind.replace("_", " ") + ")"));
      tr.appendChild(el("td", "num", bps(f.edge_bps_scan)));
      tr.appendChild(el("td", "num " + cls(f.edge_bps_after_slip), bps(f.edge_bps_after_slip)));
      tr.appendChild(el("td", "num " + (f.would_be_pnl_usdc < 0 ? "neg" : "pos"), f.would_be_pnl_usdc === null ? "—" : f.would_be_pnl_usdc.toFixed(2)));
      tr.appendChild(el("td", null, f.still_ge_300 ? "yes (paper)" : "no, rejected"));
      tb.appendChild(tr);
    });
  }

  function renderAirdrops(a) {
    $("airAsOf").textContent = a.as_of_myt || "—";
    var box = $("airdrops"); box.textContent = "";
    a.items.forEach(function (it) {
      var card = el("div", "air");
      var top = el("div", "top");
      top.appendChild(el("span", "name", it.name));
      top.appendChild(el("span", "meta", it.stage));
      card.appendChild(top);
      card.appendChild(el("div", "meta", "Chain: " + it.chain + (it.category ? " · " + it.category : "") + (it.tvl_usd ? " · TVL ~$" + money(it.tvl_usd) : "")));
      var links = el("div", "meta");
      var site = safeUrl(it.official_link), x = safeUrl(it.official_x);
      if (site) links.appendChild(link(site, "official site"));
      if (site && x) links.appendChild(document.createTextNode(" · "));
      if (x) links.appendChild(link(x, "official X"));
      if (!site && !x) links.textContent = "no official link found";
      card.appendChild(links);
      if (it.red_flags.length) { var ul = el("ul"); it.red_flags.forEach(function (f) { ul.appendChild(el("li", null, f)); }); card.appendChild(ul); }
      box.appendChild(card);
    });
  }

  function init() {
    $("tabBinary").addEventListener("click", function () { st.tab = "binary_complement"; this.classList.add("active"); $("tabBasket").classList.remove("active"); renderTable(); });
    $("tabBasket").addEventListener("click", function () { st.tab = "negrisk_basket"; this.classList.add("active"); $("tabBinary").classList.remove("active"); renderTable(); });
    document.querySelectorAll("#edges th").forEach(function (th) {
      th.addEventListener("click", function () {
        var k = th.getAttribute("data-k");
        if (st.sortKey === k) st.sortDir = -st.sortDir; else { st.sortKey = k; st.sortDir = k === "event_title" ? 1 : -1; }
        renderTable();
      });
    });
    document.addEventListener("visibilitychange", function () {
      if (!document.hidden && Date.now() - st.booksAt > PRICE_MS && !st.busy) refresh();
    });
    setInterval(badge, 10000);
    loadStatic().then(refresh);
  }
  init();
})();
