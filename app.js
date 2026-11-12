/* Live, read-only dashboard. PAPER ONLY. GETs public Gamma events and reads
 * public CLOB order books (POST /books is Polymarket's public batch *read*;
 * no auth, no orders). Math lives in edges.js (ported from scan.py/paper.py). */
(function () {
  "use strict";
  var GAMMA = "https://gamma-api.polymarket.com/events";
  var BOOKS = "https://clob.polymarket.com/books";
  var PRICE_MS = 60000, EVENTS_MS = 300000, STATIC_MS = 600000, MAX_BACKOFF_MS = 600000;
  var MYT = "Asia/Kuala_Lumpur";
  var SVG = "http://www.w3.org/2000/svg";
  var GAUGE_C = 2 * Math.PI * 46;

  var st = { events: null, eventsAt: 0, booksAt: 0, books: null, rows: [], tab: "binary_complement",
             sortKey: "edge_bps", sortDir: -1, fails: 0, timer: null, paused: false,
             staticAt: 0, busy: false, counts: null };

  function $(id) { return document.getElementById(id); }
  function el(tag, cls, text) { var e = document.createElement(tag); if (cls) e.className = cls; if (text !== undefined) e.textContent = text; return e; }
  function fmtMYT(ms) {
    if (!ms) return "—";
    return new Intl.DateTimeFormat("en-GB", { timeZone: MYT, day: "2-digit", month: "short", hour: "2-digit", minute: "2-digit", second: "2-digit", hour12: false }).format(new Date(ms)) + " MYT";
  }
  function fmtClock(ms) {
    return new Intl.DateTimeFormat("en-GB", { timeZone: MYT, hour: "2-digit", minute: "2-digit", second: "2-digit", hour12: false }).format(new Date(ms));
  }
  function bps(v) { return v === null || v === undefined ? "—" : (v >= 0 ? "+" : "") + v.toFixed(0); }
  function cls(v) { return v === null || v === undefined ? "" : (v >= 300 ? "pos" : (v < 0 ? "neg" : "")); }
  function money(v) { if (!v) return "—"; return v >= 1e6 ? (v / 1e6).toFixed(1) + "M" : v >= 1e3 ? (v / 1e3).toFixed(0) + "k" : v.toFixed(0); }
  function qty(v) { if (v >= 1000) return (v / 1000).toFixed(1) + "k"; if (v >= 100) return v.toFixed(0); return v.toFixed(2); }
  function safeUrl(u) { return typeof u === "string" && /^https:\/\//i.test(u) ? u : null; }
  function link(href, text) { var a = el("a", null, text); a.href = href; a.target = "_blank"; a.rel = "noopener noreferrer"; return a; }
  function tone(node, v) {
    if (!node) return;
    node.classList.remove("pos", "neg", "neu");
    node.classList.add(v > 0 ? "pos" : (v < 0 ? "neg" : "neu"));
  }

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
            st.rows = res.rows; st.books = books; st.booksAt = Date.now(); st.fails = 0;
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
    if (st.paused) { b.className = "pill paused"; b.textContent = "PAUSED"; }
    else if (st.booksAt && Date.now() - st.booksAt < 150000) { b.className = "pill live"; b.textContent = "LIVE"; }
    else if (st.booksAt) { b.className = "pill stale"; b.textContent = "STALE"; }
    else { b.className = "pill wait"; b.textContent = "LOADING"; }
    $("updated").textContent = fmtMYT(st.booksAt);
    $("eventsUpdated").textContent = fmtMYT(st.eventsAt);
    $("cRefresh").textContent = st.booksAt ? fmtClock(st.booksAt) : "—";
  }
  function tickClock() {
    var now = new Date();
    var node = $("clock");
    node.textContent = fmtClock(now.getTime()) + " MYT";
    node.title = fmtMYT(now.getTime());
  }

  function bestEdge() {
    var best = null;
    (st.rows || []).forEach(function (r) {
      if (typeof r.edge_bps === "number" && (best === null || r.edge_bps > best)) best = r.edge_bps;
    });
    return best;
  }
  function topEdgeRow() {
    var best = null;
    (st.rows || []).forEach(function (r) {
      if (typeof r.edge_bps !== "number") return;
      if (!best || r.edge_bps > best.edge_bps) best = r;
    });
    return best;
  }
  function positiveMarkets() {
    var n = 0;
    (st.rows || []).forEach(function (r) {
      if (typeof r.edge_bps === "number" && r.edge_bps > 0) n += r.kind === "negrisk_basket" ? (r.n_legs || 0) : 1;
    });
    return n;
  }

  function render() {
    var c = st.counts || {};
    $("cEvents").textContent = c.events != null ? c.events : "—";
    $("cMarkets").textContent = c.markets != null ? c.markets : "—";
    $("cBinary").textContent = c.binary != null ? c.binary : "—";
    $("cBaskets").textContent = c.baskets != null ? c.baskets : "—";
    $("cSkipped").textContent = c.skipped != null ? c.skipped : "—";
    $("cPass").textContent = c.pass != null ? c.pass : "—";
    $("cStill").textContent = c.still != null ? c.still : "—";
    tone($("cPass"), c.pass || 0);
    tone($("kpiPass"), c.pass || 0);
    var best = bestEdge();
    $("cBest").textContent = best === null ? "—" : bps(best);
    tone($("cBest"), best || 0);
    tone($("kpiBest"), best || 0);
    badge();
    renderGauge();
    renderDepth();
    renderTable();
  }

  function renderGauge() {
    var arc = $("gaugeArc");
    var scanned = st.counts && st.counts.markets;
    if (!scanned) {
      $("gaugePct").textContent = "—";
      $("gaugeMeta").textContent = "Share of scanned markets whose checked book has a positive net edge.";
      arc.setAttribute("stroke-dashoffset", String(GAUGE_C));
      return;
    }
    var pos = positiveMarkets();
    var pct = pos / scanned * 100;
    var shown = Math.max(0, Math.min(100, pct));
    var rounded = Math.round(shown * 10) / 10;
    $("gaugePct").textContent = (rounded % 1 === 0 ? rounded.toFixed(0) : rounded.toFixed(1)) + "%";
    $("gaugeMeta").textContent = pos + " of " + scanned + " scanned markets have a positive net edge (baskets count each outcome).";
    arc.setAttribute("stroke-dasharray", String(GAUGE_C));
    arc.setAttribute("stroke-dashoffset", String(GAUGE_C * (1 - shown / 100)));
  }

  function prettyLabel(s) {
    return String(s).replace(/\b[a-z]/g, function (ch) { return ch.toUpperCase(); });
  }
  function categoryLabel(r) {
    var src = r.fee_rate_source || "";
    var m = /^(?:tag|category|feeType)=(.+)$/.exec(src);
    var raw;
    if (m) raw = m[1].replace(/_fees$/, "").replace(/_/g, " ");
    else if (src.indexOf("feeSchedule") === 0) raw = "fee schedule";
    else if (src.indexOf("feesEnabled") === 0) raw = "no fee";
    else if (src.indexOf("default") === 0) raw = "general";
    else if (src === "per-leg") raw = "mixed";
    else raw = src || "—";
    return prettyLabel(raw);
  }
  function kindLabel(k) {
    if (k === "negrisk_basket") return "basket";
    if (k === "binary_complement") return "binary";
    return prettyLabel(String(k || "").replace(/_/g, " "));
  }
  function catClass(label) {
    var key = String(label || "").toLowerCase();
    var known = { crypto: "c0", sports: "c1", politics: "c2", finance: "c3", geopolitics: "c4", weather: "c1", economics: "c3", culture: "c2" };
    if (known[key]) return "pill cat " + known[key];
    var h = 0, i;
    for (i = 0; i < key.length; i++) h = (h + key.charCodeAt(i)) % 5;
    return "pill cat c" + h;
  }
  function netClass(v) {
    if (v === null || v === undefined) return "pill net";
    if (v >= 300) return "pill net hot";
    if (v < 0) return "pill net neg";
    return "pill net mid";
  }

  function bookLevels(book, side) {
    var raw = book && book[side];
    if (!Array.isArray(raw)) return [];
    var out = [];
    raw.forEach(function (level) {
      var p = null, s = null;
      if (level && typeof level === "object" && !Array.isArray(level)) {
        p = Number(level.price); s = Number(level.size);
      } else if (Array.isArray(level)) {
        p = Number(level[0]); s = Number(level[1]);
      }
      if (isFinite(p) && isFinite(s) && p > 0 && s > 0) out.push({ price: p, size: s });
    });
    out.sort(function (a, b) { return side === "asks" ? a.price - b.price : b.price - a.price; });
    return out;
  }
  function bar(pct, kind) {
    var svg = document.createElementNS(SVG, "svg");
    svg.setAttribute("class", "bar");
    svg.setAttribute("viewBox", "0 0 100 8");
    svg.setAttribute("preserveAspectRatio", "none");
    var track = document.createElementNS(SVG, "rect");
    track.setAttribute("class", "bar-track");
    track.setAttribute("width", "100"); track.setAttribute("height", "8"); track.setAttribute("rx", "4");
    var fill = document.createElementNS(SVG, "rect");
    fill.setAttribute("class", kind === "bid" ? "bar-bid" : "bar-ask");
    fill.setAttribute("width", String(Math.max(1.5, Math.min(100, pct))));
    fill.setAttribute("height", "8"); fill.setAttribute("rx", "4");
    svg.appendChild(track); svg.appendChild(fill);
    return svg;
  }
  function ladder(levels, kind) {
    var box = el("div");
    box.appendChild(el("div", "side-label", kind === "bid" ? "BIDS" : "ASKS"));
    if (!levels.length) { box.appendChild(el("p", "muted small", "none")); return box; }
    var max = 0;
    levels.forEach(function (lv) { if (lv.size > max) max = lv.size; });
    var list = el("div", "ladder");
    levels.forEach(function (lv) {
      var row = el("div", "lvl " + kind);
      row.appendChild(el("span", "px", lv.price.toFixed(3)));
      row.appendChild(bar(max ? lv.size / max * 100 : 0, kind));
      row.appendChild(el("span", "sz", qty(lv.size)));
      list.appendChild(row);
    });
    box.appendChild(list);
    return box;
  }
  function renderDepth() {
    var name = $("depthName"), pills = $("depthPills"), body = $("depthBody");
    pills.textContent = ""; body.textContent = "";
    var row = topEdgeRow();
    if (!row || !st.books) {
      name.textContent = "Waiting for books";
      body.appendChild(el("p", "muted small", "Asks and bids appear after the first CLOB read. Nothing here is an order."));
      return;
    }
    name.textContent = row.question || row.event_title || "Top edge";
    pills.appendChild(el("span", netClass(row.edge_bps), bps(row.edge_bps) + " bps"));
    pills.appendChild(el("span", catClass(categoryLabel(row)), categoryLabel(row)));
    pills.appendChild(el("span", "pill side " + (row.kind === "negrisk_basket" ? "basket" : "yn"), row.kind === "negrisk_basket" ? "BASKET" : "YES+NO"));
    var tokens = row.leg_tokens || [];
    if (row.kind === "negrisk_basket" && tokens.length > 2) {
      var legs = [];
      tokens.forEach(function (tok, i) {
        var asks = bookLevels(st.books[tok], "asks");
        if (asks.length) legs.push({ i: i, best: asks[0] });
      });
      var shown = legs.slice(0, 8);
      body.appendChild(el("p", "muted small", "Best ask on each leg" + (legs.length > shown.length ? " · showing " + shown.length + " of " + legs.length : "") + "."));
      if (!shown.length) { body.appendChild(el("p", "muted small", "No ask depth on these legs.")); return; }
      var max = 0;
      shown.forEach(function (lg) { if (lg.best.size > max) max = lg.best.size; });
      var list = el("div", "ladder");
      shown.forEach(function (lg) {
        var line = el("div", "lvl ask leg");
        line.appendChild(el("span", "px", "L" + (lg.i + 1)));
        line.appendChild(bar(max ? lg.best.size / max * 100 : 0, "ask"));
        line.appendChild(el("span", "sz", lg.best.price.toFixed(3) + " · " + qty(lg.best.size)));
        list.appendChild(line);
      });
      body.appendChild(list);
      return;
    }
    var grid = el("div", "books");
    tokens.forEach(function (tok, i) {
      var book = st.books[tok];
      var card = el("div", "book");
      card.appendChild(el("h3", null, row.kind === "binary_complement" ? (i === 0 ? "Yes" : "No") : "Leg " + (i + 1)));
      if (!book) { card.appendChild(el("p", "muted small", "No book")); grid.appendChild(card); return; }
      card.appendChild(ladder(bookLevels(book, "asks").slice(0, 5), "ask"));
      card.appendChild(ladder(bookLevels(book, "bids").slice(0, 5), "bid"));
      grid.appendChild(card);
    });
    body.appendChild(grid);
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
      var pills = el("div", "pills");
      var cat = categoryLabel(r);
      pills.appendChild(el("span", catClass(cat), cat));
      pills.appendChild(el("span", "pill side " + (r.kind === "negrisk_basket" ? "basket" : "yn"), r.kind === "negrisk_basket" ? "BASKET" : "YES+NO"));
      td.appendChild(pills);
      tr.appendChild(td);
      var net = el("td", "num");
      net.appendChild(el("span", netClass(r.edge_bps), bps(r.edge_bps)));
      tr.appendChild(net);
      var rateTxt = r.kind === "negrisk_basket" ? (new Set(r.fee_rates).size === 1 ? String(r.fee_rates[0]) : "mixed") : String(r.fee_rate);
      tr.appendChild(el("td", "num", rateTxt));
      tr.appendChild(el("td", "num", r.sum_ask.toFixed(3)));
      tr.appendChild(el("td", "num " + cls(r.edge_bps_pre_fee), bps(r.edge_bps_pre_fee)));
      var slipTxt = r.edge_bps_after_slip === null ? "thin book" : bps(r.edge_bps_after_slip);
      tr.appendChild(el("td", "num " + cls(r.edge_bps_after_slip), slipTxt));
      tr.appendChild(el("td", "num", money(r.volume24hr)));
      ["", "Net edge", "Fee rate", "Cost (asks)", "Before fees", "After slippage", "24h vol"].forEach(function (label, i) {
        if (label) tr.children[i].setAttribute("data-label", label);
      });
      tb.appendChild(tr);
    });
    $("edgesNote").textContent = rows.length + " " + (st.tab === "binary_complement" ? "binary markets" : "baskets") +
      " checked; showing top 40. Green net edge = at or above 300 bps. Pink = negative. \"thin book\" = not enough depth for 10 shares.";
    document.querySelectorAll("#edges th").forEach(function (th) {
      var base = th.textContent.replace(/ [▲▼]$/, "");
      th.textContent = base + (th.getAttribute("data-k") === k ? (d < 0 ? " ▼" : " ▲") : "");
    });
  }

  function equitySeries(p) {
    var keys = ["equity", "equity_series", "pnl_series", "series"];
    for (var i = 0; i < keys.length; i++) {
      var arr = p[keys[i]];
      if (!Array.isArray(arr) || arr.length < 2) continue;
      var nums = [];
      var ok = true;
      for (var j = 0; j < arr.length; j++) {
        var v = arr[j];
        var n = typeof v === "number" ? v : (v && typeof v === "object" ? Number(v.pnl != null ? v.pnl : v.value) : Number(v));
        if (!isFinite(n)) { ok = false; break; }
        nums.push(n);
      }
      if (ok) return nums;
    }
    return null;
  }
  function drawSpark(nums) {
    var host = $("spark");
    host.textContent = "";
    var w = 320, h = 64, pad = 4;
    var min = Math.min.apply(null, nums), max = Math.max.apply(null, nums);
    if (min === max) { min -= 1; max += 1; }
    var pts = nums.map(function (v, i) {
      var x = pad + (w - pad * 2) * (i / (nums.length - 1));
      var y = pad + (h - pad * 2) * (1 - (v - min) / (max - min));
      return x.toFixed(2) + "," + y.toFixed(2);
    }).join(" ");
    var svg = document.createElementNS(SVG, "svg");
    svg.setAttribute("viewBox", "0 0 " + w + " " + h);
    svg.setAttribute("class", "spark");
    var line = document.createElementNS(SVG, "polyline");
    line.setAttribute("points", pts);
    line.setAttribute("class", nums[nums.length - 1] >= nums[0] ? "spark-up" : "spark-down");
    svg.appendChild(line);
    host.appendChild(svg);
  }

  function renderPaper(p) {
    $("paperAsOf").textContent = p.as_of_myt || "—";
    var pnl = p.summary.booked_pnl_usdc;
    $("cPnl").textContent = (pnl > 0 ? "+" : "") + Number(pnl).toFixed(2);
    tone($("cPnl"), pnl);
    tone($("kpiPnl"), pnl);
    $("cTrades").textContent = Array.isArray(p.fills) ? String(p.fills.length) : "—";
    $("cKept").textContent = "kept " + p.summary.kept + " · ledger";
    var pc = $("paperCards"); pc.textContent = "";
    [["runs", p.summary.runs, null], ["candidates", p.summary.candidates, null], ["kept after slippage", p.summary.kept, null],
     ["booked P&L (USDC)", Number(p.summary.booked_pnl_usdc).toFixed(2), Number(p.summary.booked_pnl_usdc)]].forEach(function (x) {
      var c = el("div", "card kpi neu");
      var n = el("div", "n", String(x[1]));
      if (x[2] !== null) tone(n, x[2]);
      c.appendChild(n); c.appendChild(el("div", "l", x[0])); pc.appendChild(c);
    });
    var series = equitySeries(p);
    if (series) {
      drawSpark(series);
      $("sparkNote").textContent = "Equity series from paper.json (" + series.length + " points).";
    } else {
      $("spark").textContent = "";
      $("sparkNote").textContent = "No equity series in paper.json.";
    }
    var tb = document.querySelector("#fills tbody"); tb.textContent = "";
    if (!p.fills.length) { var tr0 = el("tr"); var td0 = el("td", "muted", "No hypothetical fills yet."); td0.colSpan = 6; tr0.appendChild(td0); tb.appendChild(tr0); }
    p.fills.forEach(function (f) {
      var tr = el("tr");
      tr.appendChild(el("td", null, f.ts_myt));
      tr.appendChild(el("td", "title", f.event_title + " (" + kindLabel(f.kind) + ")"));
      tr.appendChild(el("td", "num", bps(f.edge_bps_scan)));
      tr.appendChild(el("td", "num " + cls(f.edge_bps_after_slip), bps(f.edge_bps_after_slip)));
      tr.appendChild(el("td", "num " + (f.would_be_pnl_usdc < 0 ? "neg" : "pos"), f.would_be_pnl_usdc === null ? "—" : f.would_be_pnl_usdc.toFixed(2)));
      var kept = el("td");
      kept.appendChild(el("span", f.still_ge_300 ? "pill keep" : "pill drop", f.still_ge_300 ? "yes (paper)" : "no, rejected"));
      tr.appendChild(kept);
      ["Time (MYT)", "Market", "Scan bps", "After slip bps", "Hypothetical P&L (USDC)", "Kept?"].forEach(function (label, i) {
        tr.children[i].setAttribute("data-label", label);
      });
      tb.appendChild(tr);
    });
  }

  function stageBadge(stage) {
    var s = String(stage || "");
    if (/unconfirmed/i.test(s)) return ["pill stale", "unconfirmed"];
    if (/confirmed/i.test(s)) return ["pill keep", "confirmed"];
    return ["pill wait", s || "watch"];
  }
  function renderAirdrops(a) {
    $("airAsOf").textContent = a.as_of_myt || "—";
    $("cAir").textContent = Array.isArray(a.items) ? String(a.items.length) : "—";
    var box = $("airdrops"); box.textContent = "";
    a.items.forEach(function (it) {
      var card = el("article", "air");
      var top = el("div", "top");
      top.appendChild(el("span", "name", it.name));
      var badge = stageBadge(it.stage);
      top.appendChild(el("span", badge[0], badge[1]));
      card.appendChild(top);
      if (it.category) {
        var pills = el("div", "pills");
        pills.appendChild(el("span", catClass(it.category), it.category));
        card.appendChild(pills);
      }
      card.appendChild(el("div", "meta", "Chain: " + it.chain + (it.tvl_usd ? " · TVL ~$" + money(it.tvl_usd) : "") + (it.listed_myt ? " · listed " + it.listed_myt : "")));
      card.appendChild(el("div", "meta", it.stage || ""));
      var links = el("div", "meta");
      var site = safeUrl(it.official_link), x = safeUrl(it.official_x);
      if (site) links.appendChild(link(site, "official site"));
      if (site && x) links.appendChild(document.createTextNode(" · "));
      if (x) links.appendChild(link(x, "official X"));
      if (!site && !x) links.textContent = "no official link found";
      card.appendChild(links);
      if (it.red_flags && it.red_flags.length) { var ul = el("ul"); it.red_flags.forEach(function (f) { ul.appendChild(el("li", null, f)); }); card.appendChild(ul); }
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
    tickClock();
    setInterval(tickClock, 1000);
    setInterval(badge, 10000);
    loadStatic().then(refresh);
  }
  init();
})();
