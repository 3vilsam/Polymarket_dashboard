/* Live, read-only dashboard. PAPER ONLY. GETs public Gamma events and reads
 * public CLOB order books (POST /books is Polymarket's public batch *read*;
 * no auth, no orders). Math lives in edges.js (ported from scan.py/paper.py). */
(function () {
  "use strict";
  var GAMMA = "https://gamma-api.polymarket.com/events";
  var BOOKS = "https://clob.polymarket.com/books";
  var PRICE_MS = 10000, EVENTS_MS = 300000, STATIC_MS = 600000, MAX_BACKOFF_MS = 600000;
  var MIRROR_MS = 60000, DIRECT_RETRY_MS = 300000, DIRECT_TIMEOUT_MS = 6000;
  var MYT = "Asia/Kuala_Lumpur";
  var SVG = "http://www.w3.org/2000/svg";
  var GAUGE_C = 2 * Math.PI * 46;

  var st = { events: null, eventsAt: 0, booksAt: 0, books: null, rows: [], tab: "binary_complement",
             sortKey: "edge_bps", sortDir: -1, fails: 0, timer: null, paused: false,
             staticAt: 0, busy: false, counts: null, shown: {}, asks: {}, ticks: [],
             widths: {}, cycleChanges: 0, nextAt: 0, cycleMs: PRICE_MS, refreshing: false,
             builtMs: null, builtLabel: "", mode: "", mirrorAt: 0, lastDirectTry: 0, fetchedAt: 0 };

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
  function polymarketJSON(url, options) {
    var ctrl = new AbortController();
    var timer = setTimeout(function () { ctrl.abort(); }, DIRECT_TIMEOUT_MS);
    var opts = options || {};
    opts.signal = ctrl.signal;
    opts.credentials = "omit";
    opts.cache = "no-store";
    opts.referrerPolicy = "no-referrer";
    return fetch(url, opts).then(function (r) {
      clearTimeout(timer);
      if (!r.ok) throw new Error(url.split("?")[0] + " HTTP " + r.status);
      return r.json();
    }, function (e) {
      clearTimeout(timer);
      throw (e && e.name === "AbortError") ? new Error("timed out") : e;
    });
  }

  function fetchEvents() {
    var out = [], page = 0;
    function next() {
      var url = GAMMA + "?active=true&closed=false&limit=100&offset=" + page * 100 + "&order=volume24hr&ascending=false";
      return polymarketJSON(url).then(function (batch) {
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
        return polymarketJSON(BOOKS, { method: "POST", headers: { "Content-Type": "application/json" },
          body: JSON.stringify(chunk.map(function (t) { return { token_id: t }; })) })
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
      if (r[0]) {
        st.paused = !!r[0].paused;
        $("builtAt").textContent = r[0].built_at_myt || "—";
        st.builtLabel = r[0].built_at_myt || "—";
        st.builtMs = parseMYT(r[0].built_at_myt);
        renderSnaps();
      }
      if (r[1]) renderPaper(r[1]);
      if (r[2]) renderAirdrops(r[2]);
    });
  }

  function hideMirrorNote() {
    var n = $("mirrorNote");
    if (n) n.hidden = true;
  }
  function showMirrorNote(data) {
    var n = $("mirrorNote");
    if (!n) return;
    $("error").hidden = true;
    n.hidden = false;
    var when = (data && (data.generated_at_myt || data.generated_at_utc)) || "the last Actions run";
    n.textContent = "Polymarket did not answer in time. Showing the same-origin mirror from " + when + ".";
  }
  function shouldTryDirect() {
    if (st.mode !== "mirror") return true;
    return Date.now() - (st.lastDirectTry || 0) >= DIRECT_RETRY_MS;
  }
  function applyDirect(events, eventsAt, books, res, jobs) {
    st.events = events;
    st.eventsAt = eventsAt;
    st.rows = res.rows;
    st.books = books;
    st.booksAt = Date.now();
    st.fetchedAt = st.booksAt;
    st.fails = 0;
    st.mode = "direct";
    st.mirrorAt = 0;
    st.counts = { events: events.length, markets: PM.countMarkets(events),
      binary: res.rows.filter(function (r) { return r.kind === "binary_complement"; }).length,
      baskets: res.rows.filter(function (r) { return r.kind === "negrisk_basket"; }).length,
      skipped: jobs.skippedCap + res.skippedBooks, pass: res.nPass,
      still: res.rows.filter(function (r) { return r.passes_300bps && r.still_ge_300; }).length };
    $("error").hidden = true;
    hideMirrorNote();
    render();
  }
  function directScan() {
    var events = st.events, eventsAt = st.eventsAt;
    var needEvents = !events || Date.now() - eventsAt > EVENTS_MS;
    return (needEvents ? fetchEvents().then(function (ev) {
      if (ev && ev.length) { events = ev; eventsAt = Date.now(); }
    }) : Promise.resolve()).then(function () {
      if (!events) throw new Error("no events from Gamma");
      var jobs = PM.collectJobs(events);
      return fetchBooks(jobs.tokens).then(function (books) {
        return { events: events, eventsAt: eventsAt, books: books, res: PM.evaluate(jobs, books), jobs: jobs };
      });
    }).then(function (pack) {
      applyDirect(pack.events, pack.eventsAt, pack.books, pack.res, pack.jobs);
    });
  }
  function mirrorWhen(data) {
    var t = data && Date.parse(data.generated_at_utc);
    if (t && !isNaN(t)) return t;
    return parseMYT(data && data.generated_at_myt);
  }
  function applyMirror(data) {
    if (!data || !Array.isArray(data.edges)) throw new Error("mirror has no edges");
    var when = mirrorWhen(data);
    if (when == null || isNaN(when)) throw new Error("mirror has no timestamp");
    var c = data.counts || {};
    st.rows = data.edges;
    st.books = data.books && typeof data.books === "object" ? data.books : {};
    st.counts = { events: c.events, markets: c.markets, binary: c.binary, baskets: c.baskets, skipped: c.skipped, pass: c.pass, still: c.still };
    st.booksAt = when;
    st.eventsAt = when;
    st.mirrorAt = when;
    st.fetchedAt = Date.now();
    st.fails = 0;
    st.mode = "mirror";
    $("error").hidden = true;
    showMirrorNote(data);
    render();
  }
  function loadMirror() {
    return getJSON("data/live.json?t=" + Date.now()).then(applyMirror);
  }
  function refresh() {
    if (st.busy) return Promise.resolve();
    st.busy = true;
    st.refreshing = true;
    st.cycleChanges = 0;
    setWidthClass($("cycleBar"), 100, false);
    paintCountdown();
    var p = Date.now() - st.staticAt > STATIC_MS ? loadStatic() : Promise.resolve();
    return p.then(function () {
      if (st.paused) { badge(); $("cycleChanges").textContent = "changes this cycle: 0"; return; }
      if (shouldTryDirect()) {
        st.lastDirectTry = Date.now();
        return directScan().catch(function (directErr) {
          return loadMirror().catch(function () { throw directErr; });
        });
      }
      return loadMirror();
    }).catch(function (e) {
      st.fails++;
      hideMirrorNote();
      var err = $("error"); err.hidden = false;
      err.textContent = "Refresh failed (" + (e && e.message ? e.message : "network") + "). Mirror unavailable. Retrying with back-off; last good data stays on screen.";
      $("cycleChanges").textContent = "changes this cycle: 0";
    }).then(function () { st.busy = false; badge(); schedule(); });
  }

  function delay() {
    var base = st.mode === "mirror" ? MIRROR_MS : PRICE_MS;
    return st.fails ? Math.min(base * Math.pow(2, st.fails), MAX_BACKOFF_MS) : base;
  }
  function schedule() {
    clearTimeout(st.timer);
    var d = st.paused ? STATIC_MS : delay();
    st.cycleMs = d;
    st.nextAt = Date.now() + d;
    st.refreshing = false;
    setWidthClass($("cycleBar"), 0, true);
    st.timer = setTimeout(function () { if (document.hidden) { schedule(); return; } refresh(); }, d);
    paintCountdown();
  }
  function ageShort(ms) {
    var sec = Math.max(0, Math.floor((Date.now() - ms) / 1000));
    if (sec < 60) return sec + "s";
    var min = Math.floor(sec / 60);
    if (min < 60) return min + "m";
    var hr = Math.floor(min / 60);
    if (hr < 48) return hr + "h";
    return Math.floor(hr / 24) + "d";
  }
  function badge() {
    var b = $("badge");
    if (st.paused) { b.className = "pill paused"; b.textContent = "PAUSED"; }
    else if (st.mode === "mirror" && st.mirrorAt) { b.className = "pill mirror"; b.textContent = "MIRROR · data " + ageShort(st.mirrorAt) + " old"; }
    else if (st.mode === "direct" && st.booksAt && Date.now() - st.booksAt < 150000) { b.className = "pill live"; b.textContent = "LIVE"; }
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
    paintCountdown();
    renderSnaps();
    if (st.mode === "mirror") badge();
  }
  function parseMYT(s) {
    var m = /^(\d{4})-(\d{2})-(\d{2})[ T](\d{2}):(\d{2})(?::(\d{2}))?/.exec(String(s || ""));
    if (!m) return null;
    return Date.UTC(+m[1], +m[2] - 1, +m[3], +m[4] - 8, +m[5], +(m[6] || 0));
  }
  function agePhrase(ms) {
    var sec = Math.max(0, Math.floor((Date.now() - ms) / 1000));
    if (sec < 60) return sec + "s ago";
    var min = Math.floor(sec / 60);
    if (min < 60) return min + "m ago";
    var hr = Math.floor(min / 60);
    if (hr < 48) return hr + "h ago";
    return Math.floor(hr / 24) + "d ago";
  }
  function renderSnaps() {
    if (!$("paperSnap")) return;
    var label = st.builtLabel || "—";
    var age = st.builtMs != null ? " (" + agePhrase(st.builtMs) + ")" : "";
    var text = "snapshot · updated " + label + age;
    $("paperSnap").textContent = text;
    $("airSnap").textContent = text;
  }
  function setWidthClass(node, pct, instant) {
    if (!node) return;
    var n = Math.max(0, Math.min(100, Math.round(pct)));
    var prev = node.getAttribute("data-w");
    if (prev === String(n) && !instant) return;
    if (instant) node.classList.add("notrans");
    if (prev !== null) node.classList.remove("w" + prev);
    node.classList.add("w" + n);
    node.setAttribute("data-w", String(n));
    if (instant) { void node.offsetWidth; node.classList.remove("notrans"); }
  }
  function paintCountdown() {
    var node = $("countdown");
    if (!node) return;
    if (st.refreshing) { node.textContent = "updating…"; return; }
    if (!st.nextAt) { node.textContent = "next update in —s"; return; }
    var left = Math.max(0, Math.ceil((st.nextAt - Date.now()) / 1000));
    node.textContent = "next update in " + left + "s";
    var dur = st.cycleMs || PRICE_MS;
    var gone = dur - (st.nextAt - Date.now());
    setWidthClass($("cycleBar"), Math.max(0, Math.min(100, gone / dur * 100)), false);
  }
  function flash(node, dir) {
    node.classList.remove("flash-up", "flash-down");
    void node.offsetWidth;
    node.classList.add(dir > 0 ? "flash-up" : "flash-down");
  }
  function note(key, node, text, num) {
    var prev = st.shown[key];
    st.shown[key] = { text: text, num: num };
    if (node) node.textContent = text;
    if (!prev || prev.text === text) return;
    if (prev.text === "—" || text === "—") return;
    if (typeof prev.num === "number" && typeof num === "number" && isFinite(prev.num) && isFinite(num) && prev.num !== num) {
      if (node) flash(node, num > prev.num ? 1 : -1);
    }
    st.cycleChanges++;
  }
  function rowKey(r) {
    return r.kind + "|" + (r.event_slug || "") + "|" + (r.market_slug || "") + "|" + (r.question || "");
  }
  function shortName(text) {
    var s = String(text || "Market").replace(/\s+/g, " ").trim();
    return s.length > 32 ? s.slice(0, 31) + "…" : s;
  }
  function legName(r, i) {
    var base = shortName(r.kind === "negrisk_basket" ? (r.event_title || r.question) : (r.question || r.event_title));
    if (r.kind === "binary_complement") return base + (i === 0 ? " Yes" : " No");
    return base + " L" + (i + 1);
  }
  function px3(n) { return Math.round(n * 1000) / 1000; }
  function renderTicks() {
    var box = $("tickList");
    if (!box) return;
    box.textContent = "";
    if (!st.ticks.length) {
      box.appendChild(el("span", "tick muted", "No price changes yet this session."));
      return;
    }
    st.ticks.forEach(function (t) {
      var chip = el("span", "tick " + (t.newP > t.oldP ? "up" : "down"));
      chip.appendChild(el("b", null, t.name));
      chip.appendChild(document.createTextNode(" " + t.oldP.toFixed(3) + " → " + t.newP.toFixed(3) + "  " + fmtClock(t.at)));
      box.appendChild(chip);
    });
  }
  function collectTicks() {
    var fresh = [], seenTok = {};
    (st.rows || []).forEach(function (r) {
      (r.leg_tokens || []).forEach(function (tok, i) {
        if (!tok || seenTok[tok] || !st.books) return;
        seenTok[tok] = 1;
        var levels = bookLevels(st.books[tok], "asks");
        if (!levels.length) return;
        var ask = px3(levels[0].price);
        var prev = st.asks[tok];
        if (typeof prev === "number" && prev !== ask) fresh.push({ name: legName(r, i), oldP: prev, newP: ask, at: Date.now() });
        st.asks[tok] = ask;
      });
    });
    if (fresh.length) st.ticks = fresh.concat(st.ticks).slice(0, 10);
    renderTicks();
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
    note("kpiEvents", $("cEvents"), c.events != null ? String(c.events) : "—", c.events);
    note("kpiMarkets", $("cMarkets"), c.markets != null ? String(c.markets) : "—", c.markets);
    note("kpiBinary", $("cBinary"), c.binary != null ? String(c.binary) : "—", c.binary);
    note("kpiBaskets", $("cBaskets"), c.baskets != null ? String(c.baskets) : "—", c.baskets);
    note("kpiSkipped", $("cSkipped"), c.skipped != null ? String(c.skipped) : "—", c.skipped);
    note("kpiPass", $("cPass"), c.pass != null ? String(c.pass) : "—", c.pass);
    note("kpiStill", $("cStill"), c.still != null ? String(c.still) : "—", c.still);
    tone($("cPass"), c.pass || 0);
    tone($("kpiPass"), c.pass || 0);
    var best = bestEdge();
    note("kpiBest", $("cBest"), best === null ? "—" : bps(best), best);
    tone($("cBest"), best || 0);
    tone($("kpiBest"), best || 0);
    badge();
    collectTicks();
    renderGauge();
    renderDepth();
    renderTable();
    $("cycleChanges").textContent = "changes this cycle: " + st.cycleChanges;
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
    note("gauge", $("gaugePct"), (rounded % 1 === 0 ? rounded.toFixed(0) : rounded.toFixed(1)) + "%", shown);
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
  function bar(pct, kind, key) {
    var n = Math.max(0, Math.min(100, Math.round(pct)));
    var prev = st.widths[key];
    var start = prev == null ? n : prev;
    var fill = el("span", "bar-fill " + (kind === "bid" ? "bid" : "ask") + " w" + start);
    var wrap = el("div", "bar");
    wrap.appendChild(fill);
    st.widths[key] = n;
    if (prev != null && prev !== n) {
      requestAnimationFrame(function () {
        requestAnimationFrame(function () {
          fill.classList.remove("w" + start);
          fill.classList.add("w" + n);
        });
      });
    }
    return wrap;
  }
  function ladder(levels, kind, keyPrefix) {
    var box = el("div");
    box.appendChild(el("div", "side-label", kind === "bid" ? "BIDS" : "ASKS"));
    if (!levels.length) { box.appendChild(el("p", "muted small", "none")); return box; }
    var max = 0;
    levels.forEach(function (lv) { if (lv.size > max) max = lv.size; });
    var list = el("div", "ladder");
    levels.forEach(function (lv, i) {
      var row = el("div", "lvl " + kind);
      var px = el("span", "px");
      note(keyPrefix + "|" + kind + "|" + i + "|px", px, lv.price.toFixed(3), lv.price);
      row.appendChild(px);
      row.appendChild(bar(max ? lv.size / max * 100 : 0, kind, keyPrefix + "|" + kind + "|" + i));
      var sz = el("span", "sz");
      note(keyPrefix + "|" + kind + "|" + i + "|sz", sz, qty(lv.size), lv.size);
      row.appendChild(sz);
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
    var edgePill = el("span", netClass(row.edge_bps));
    note(rowKey(row) + "|depthbps", edgePill, bps(row.edge_bps) + " bps", row.edge_bps);
    pills.appendChild(edgePill);
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
        var tok = tokens[lg.i];
        var line = el("div", "lvl ask leg");
        line.appendChild(el("span", "px", "L" + (lg.i + 1)));
        line.appendChild(bar(max ? lg.best.size / max * 100 : 0, "ask", tok + "|leg"));
        var sz = el("span", "sz");
        note(tok + "|legtxt", sz, lg.best.price.toFixed(3) + " · " + qty(lg.best.size), lg.best.price);
        line.appendChild(sz);
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
      card.appendChild(ladder(bookLevels(book, "asks").slice(0, 5), "ask", tok + "|ask"));
      card.appendChild(ladder(bookLevels(book, "bids").slice(0, 5), "bid", tok + "|bid"));
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
      var netPill = el("span", netClass(r.edge_bps));
      note(rowKey(r) + "|edge", netPill, bps(r.edge_bps), r.edge_bps);
      net.appendChild(netPill);
      tr.appendChild(net);
      var rateTxt = r.kind === "negrisk_basket" ? (new Set(r.fee_rates).size === 1 ? String(r.fee_rates[0]) : "mixed") : String(r.fee_rate);
      var rateTd = el("td", "num");
      note(rowKey(r) + "|fee", rateTd, rateTxt, r.fee_rates[0]);
      tr.appendChild(rateTd);
      var costTd = el("td", "num");
      note(rowKey(r) + "|cost", costTd, r.sum_ask.toFixed(3), r.sum_ask);
      tr.appendChild(costTd);
      var preTd = el("td", "num " + cls(r.edge_bps_pre_fee));
      note(rowKey(r) + "|pre", preTd, bps(r.edge_bps_pre_fee), r.edge_bps_pre_fee);
      tr.appendChild(preTd);
      var slipTxt = r.edge_bps_after_slip === null ? "thin book" : bps(r.edge_bps_after_slip);
      var slipTd = el("td", "num " + cls(r.edge_bps_after_slip));
      note(rowKey(r) + "|slip", slipTd, slipTxt, r.edge_bps_after_slip);
      tr.appendChild(slipTd);
      var volTd = el("td", "num");
      note(rowKey(r) + "|vol", volTd, money(r.volume24hr), r.volume24hr);
      tr.appendChild(volTd);
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
      var gap = st.mode === "mirror" ? MIRROR_MS : PRICE_MS;
      if (!document.hidden && Date.now() - (st.fetchedAt || 0) > gap && !st.busy) refresh();
    });
    tickClock();
    setInterval(tickClock, 1000);
    setInterval(badge, 10000);
    loadStatic().then(refresh);
  }
  init();
})();
