/* Polymarket paper-monitor math, ported 1:1 from fees.py, edges.py,
 * scan.py (collect_jobs / evaluate) and paper.py (simulate).
 * PAPER ONLY. Pure functions, no network, no keys, no orders.
 * Fee (https://docs.polymarket.com/trading/fees): fee = C x feeRate x p x (1 - p)
 */
(function (root, factory) {
  if (typeof module === "object" && module.exports) module.exports = factory();
  else root.PM = factory();
})(typeof self !== "undefined" ? self : this, function () {
  "use strict";

  var MIN_EDGE_BPS = 300, MIN_BASKET_LEGS = 3, MAX_TOKENS = 500;
  var PAPER_SHARES = 10.0, PESSIMISTIC_SLIP_BPS = 50;
  var FEE_DECIMALS = 5, MIN_FEE = 1e-5, DEFAULT_FEE_RATE = 0.05;

  var CATEGORY_RATES = {
    "crypto": 0.07, "sports": 0.05, "finance": 0.04, "politics": 0.04,
    "economics": 0.05, "culture": 0.05, "weather": 0.05, "other": 0.05,
    "general": 0.05, "other / general": 0.05, "mentions": 0.04, "tech": 0.04,
    "geopolitics": 0.0, "combos": 0.05
  };
  // Insertion order matches fees.py FEE_TYPE_RATES (prefix match relies on it).
  var FEE_TYPE_RATES = [
    ["crypto_fees", 0.07], ["sports_fees", 0.05], ["sports_fees_v3", 0.05],
    ["finance_fees", 0.04], ["politics_fees", 0.04], ["economics_fees", 0.05],
    ["culture_fees", 0.05], ["weather_fees", 0.05], ["mentions_fees", 0.04],
    ["tech_fees", 0.04], ["geopolitics_fees", 0.0], ["combos_fees", 0.05],
    ["general_fees", 0.05], ["other_fees", 0.05]
  ];

  function isObj(v) { return v !== null && typeof v === "object" && !Array.isArray(v); }
  function pyTruthy(v) {
    if (v === null || v === undefined || v === false || v === 0 || v === "") return false;
    if (Array.isArray(v)) return v.length > 0;
    if (isObj(v)) return Object.keys(v).length > 0;
    return true;
  }
  // Python float(): null on failure.
  function toFloat(v) {
    if (v === null || v === undefined) return null;
    if (typeof v === "boolean") return v ? 1 : 0;
    if (typeof v === "number") return v;
    if (typeof v === "string") {
      var s = v.trim();
      if (s === "") return null;
      var n = Number(s);
      return isNaN(n) ? null : n;
    }
    return null;
  }
  // Python round(x, 5): both use the exact binary value; exact ties are negligible here.
  function round5(x) { return parseFloat(x.toFixed(FEE_DECIMALS)); }

  // ---- fees.py ----
  function takerFeeUsdc(shares, price, feeRate) {
    if (shares <= 0 || feeRate <= 0) return 0.0;
    var raw = shares * feeRate * price * (1.0 - price);
    if (raw <= 0) return 0.0;
    var r = round5(raw);
    if (r < MIN_FEE) return 0.0;
    return r;
  }
  function rateForCategory(name) {
    if (!pyTruthy(name)) return null;
    var key = String(name).trim().toLowerCase();
    return Object.prototype.hasOwnProperty.call(CATEGORY_RATES, key) ? CATEGORY_RATES[key] : null;
  }
  function rateForFeeType(ft) {
    if (!pyTruthy(ft)) return null;
    var key = String(ft).trim().toLowerCase(), i;
    for (i = 0; i < FEE_TYPE_RATES.length; i++) if (FEE_TYPE_RATES[i][0] === key) return FEE_TYPE_RATES[i][1];
    for (i = 0; i < FEE_TYPE_RATES.length; i++) if (key.indexOf(FEE_TYPE_RATES[i][0]) === 0) return FEE_TYPE_RATES[i][1];
    return null;
  }
  function tagsFrom(tags) {
    var out = [];
    if (!pyTruthy(tags) || !Array.isArray(tags)) return out;
    tags.forEach(function (t) {
      if (typeof t === "string") out.push(t);
      else if (isObj(t)) ["label", "slug", "name"].forEach(function (f) { if (pyTruthy(t[f])) out.push(String(t[f])); });
    });
    return out;
  }
  function resolveFeeRate(market, tags) {
    market = market || {};
    if (market.feesEnabled === false) return [0.0, "feesEnabled=false"];
    var sch = market.feeSchedule;
    if (isObj(sch) && Object.prototype.hasOwnProperty.call(sch, "rate")) {
      var r = toFloat(sch.rate);
      if (r !== null) return [r, "feeSchedule.rate"];
    }
    var typed = rateForFeeType(market.feeType);
    if (typed !== null) return [typed, "feeType=" + market.feeType];
    var labels = tagsFrom(tags);
    for (var i = 0; i < labels.length; i++) {
      var m = rateForCategory(labels[i]);
      if (m !== null) return [m, "tag=" + labels[i]];
    }
    var cat = pyTruthy(market.category) ? market.category : market.groupItemTitle;
    var mapped = rateForCategory(typeof cat === "string" ? cat : null);
    if (mapped !== null) return [mapped, "category=" + cat];
    return [DEFAULT_FEE_RATE, "default:Other/General"];
  }

  // ---- edges.py ----
  function levelPrice(l) {
    if (isObj(l)) return toFloat(l.price);
    if (Array.isArray(l) && l.length) return toFloat(l[0]);
    return null;
  }
  function bestLevel(levels, which) {
    var prices = [];
    (levels || []).forEach(function (l) {
      var p = levelPrice(l);
      if (p !== null && p > 0 && p < 1) prices.push(p);
    });
    if (!prices.length) return null;
    return which === "min" ? Math.min.apply(null, prices) : Math.max.apply(null, prices);
  }
  function bestAsk(book) { return pyTruthy(book) ? bestLevel(book.asks, "min") : null; }
  function walkBuyVwap(book, shares) {
    if (!pyTruthy(book) || shares <= 0) return null;
    var levels = [];
    (book.asks || []).forEach(function (l) {
      var p = null, s = null;
      if (isObj(l)) { p = toFloat(l.price); s = toFloat(l.size); }
      else if (Array.isArray(l) && l.length >= 2) { p = toFloat(l[0]); s = toFloat(l[1]); }
      if (p === null || s === null) return;
      if (p > 0 && p < 1 && s > 0) levels.push([p, s]);
    });
    levels.sort(function (a, b) { return a[0] - b[0]; });
    var remaining = shares, cost = 0, filled = 0;
    for (var i = 0; i < levels.length; i++) {
      var take = Math.min(remaining, levels[i][1]);
      cost += take * levels[i][0]; filled += take; remaining -= take;
      if (remaining <= 1e-12) break;
    }
    if (filled + 1e-9 < shares) return null;
    return cost / filled;
  }
  function applyPessimisticSlip(price, slipBps, cap) {
    if (cap === undefined) cap = 0.999;
    var s = price + slipBps / 10000.0;
    if (s <= 0) return 0.0;
    return Math.min(cap, s);
  }
  function isValidAsk(a) { return a !== null && a !== undefined && a > 0 && a < 1; }
  function binaryCostAfterFees(y, n, yr, nr, shares) {
    if (shares === undefined) shares = 1.0;
    if (shares <= 0 || !isValidAsk(y) || !isValidAsk(n)) return null;
    var fees = takerFeeUsdc(shares, y, yr) + takerFeeUsdc(shares, n, nr);
    return round5(shares * y + shares * n + fees);
  }
  function edgeBpsFromCost(cost, shares) {
    if (shares === undefined) shares = 1.0;
    if (cost === null || shares <= 0) return null;
    return (shares - cost) / shares * 10000.0;
  }
  function binaryEdgeBps(y, n, yr, nr, shares) {
    if (!isValidAsk(y) || !isValidAsk(n)) return null;
    return edgeBpsFromCost(binaryCostAfterFees(y, n, yr, nr, shares), shares);
  }
  function basketLegsComplete(legs, minLegs) {
    if (minLegs === undefined) minLegs = MIN_BASKET_LEGS;
    if (!legs || legs.length < minLegs) return false;
    for (var i = 0; i < legs.length; i++) if (!isObj(legs[i]) || !isValidAsk(legs[i].ask)) return false;
    return true;
  }
  function basketCostAfterFees(legs, shares) {
    if (shares === undefined) shares = 1.0;
    if (shares <= 0 || !basketLegsComplete(legs)) return null;
    var cost = 0;
    legs.forEach(function (l) { cost += shares * l.ask + takerFeeUsdc(shares, l.ask, l.fee_rate || 0); });
    return round5(cost);
  }
  function basketEdgeBps(legs, shares) {
    if (!basketLegsComplete(legs)) return null;
    return edgeBpsFromCost(basketCostAfterFees(legs, shares), shares);
  }
  function passesMinEdge(e) { return e !== null && e >= MIN_EDGE_BPS; }

  // ---- scan.py helpers ----
  function asList(v) {
    if (v === null || v === undefined) return [];
    if (Array.isArray(v)) return v;
    if (typeof v === "string") { try { var p = JSON.parse(v); return Array.isArray(p) ? p : []; } catch (e) { return []; } }
    return [];
  }
  function activeMarkets(ev) {
    return (ev.markets || []).filter(function (m) {
      return isObj(m) && m.active !== false && m.closed !== true && m.enableOrderBook !== false;
    });
  }
  function yesNoTokens(m) {
    var tokens = asList(m.clobTokenIds).filter(pyTruthy).map(String);
    var outcomes = asList(m.outcomes).map(String);
    if (tokens.length < 2) return [null, null];
    var lower = outcomes.map(function (o) { return o.trim().toLowerCase(); });
    var yi = lower.indexOf("yes") >= 0 ? lower.indexOf("yes") : 0;
    var ni = lower.indexOf("no") >= 0 ? lower.indexOf("no") : 1;
    if (yi >= tokens.length || ni >= tokens.length || yi === ni) return [tokens[0], tokens[1]];
    return [tokens[yi], tokens[ni]];
  }
  function yesToken(m) {
    var y = yesNoTokens(m)[0];
    if (y) return y;
    var tokens = asList(m.clobTokenIds).filter(pyTruthy).map(String);
    return tokens.length ? tokens[0] : null;
  }
  function volume(ev, m) {
    var srcs = [m, ev];
    for (var i = 0; i < srcs.length; i++) {
      var s = srcs[i];
      if (!pyTruthy(s)) continue;
      var keys = ["volume24hr", "volume24hrClob", "volume"];
      for (var k = 0; k < keys.length; k++) {
        if (s[keys[k]] !== null && s[keys[k]] !== undefined) {
          var f = toFloat(s[keys[k]]);
          if (f !== null) return f;
        }
      }
    }
    return 0.0;
  }
  function collectJobs(events) {
    var binaries = [], baskets = [], tokens = [], seen = new Set(), skippedCap = 0;
    function accept(tids) {
      // Mirrors scan.py accept(): duplicates inside `new` count toward the cap.
      var newList = tids.filter(function (t) { return t && !seen.has(t); });
      if (seen.size + newList.length > MAX_TOKENS) return false;
      newList.forEach(function (t) { if (!seen.has(t)) { seen.add(t); } tokens.push(t); });
      return true;
    }
    events.forEach(function (ev) {
      var markets = activeMarkets(ev);
      var tags = ev.tags || [];
      var title = ev.title || ev.slug || "";
      if (pyTruthy(ev.negRisk) && markets.length >= MIN_BASKET_LEGS) {
        var legs = [], tids = [], ok = true;
        for (var i = 0; i < markets.length; i++) {
          var tid = yesToken(markets[i]);
          if (!tid) { ok = false; break; }
          var fr = resolveFeeRate(markets[i], tags);
          legs.push({ market_slug: markets[i].slug || "", question: markets[i].question || "",
                      token_id: tid, fee_rate: fr[0], fee_rate_source: fr[1] });
          tids.push(tid);
        }
        if (!ok) skippedCap += 1;
        else if (!accept(tids)) skippedCap += 1;
        else baskets.push({ event_slug: ev.slug || "", event_title: title, volume24hr: volume(ev), legs: legs });
        return;
      }
      markets.forEach(function (m) {
        var yn = yesNoTokens(m);
        if (!yn[0] || !yn[1]) return;
        if (!accept([yn[0], yn[1]])) return;
        var fr = resolveFeeRate(m, tags);
        binaries.push({ event_slug: ev.slug || "", event_title: title, market_slug: m.slug || "",
                        question: m.question || "", yes_token: yn[0], no_token: yn[1],
                        fee_rate: fr[0], fee_rate_source: fr[1], fee_type: m.feeType || "",
                        volume24hr: volume(ev, m) });
      });
    });
    return { binaries: binaries, baskets: baskets, tokens: tokens, skippedCap: skippedCap };
  }

  // ---- paper.py simulate (hypothetical fill, 10 shares, +50 bps per leg) ----
  function simulate(kind, legTokens, rates, books, shares, slipBps) {
    if (shares === undefined) shares = PAPER_SHARES;
    if (slipBps === undefined) slipBps = PESSIMISTIC_SLIP_BPS;
    if (!legTokens.length) return { slipped_cost: null, edge_bps_after_slip: null, still_ge_300: 0, notes: "no token ids" };
    var slipped = [];
    for (var i = 0; i < legTokens.length; i++) {
      var v = walkBuyVwap(books[legTokens[i]], shares);
      if (v === null) return { slipped_cost: null, edge_bps_after_slip: null, still_ge_300: 0, notes: "insufficient depth or missing book" };
      slipped.push(applyPessimisticSlip(v, slipBps));
    }
    var edge, unit;
    if (kind === "negrisk_basket") {
      var legs = slipped.map(function (p, j) { return { ask: p, fee_rate: rates[j] }; });
      edge = basketEdgeBps(legs, 1.0);
      unit = basketCostAfterFees(legs, 1.0);
    } else {
      if (slipped.length < 2) return { slipped_cost: null, edge_bps_after_slip: null, still_ge_300: 0, notes: "binary row missing a leg token" };
      edge = binaryEdgeBps(slipped[0], slipped[1], rates[0], rates[1], 1.0);
      unit = binaryCostAfterFees(slipped[0], slipped[1], rates[0], rates[1], 1.0);
    }
    return { slipped_cost: unit === null ? null : unit * shares, edge_bps_after_slip: edge,
             still_ge_300: (edge !== null && edge >= MIN_EDGE_BPS) ? 1 : 0,
             notes: "pessimistic slip +" + slipBps + " bps per leg on VWAP of " + shares + " shares" };
  }

  // ---- scan.py evaluate, plus pre-fee edge and paper re-check ----
  function evaluate(jobs, books) {
    var rows = [], skippedBooks = 0;
    jobs.binaries.forEach(function (j) {
      var y = bestAsk(books[j.yes_token]), n = bestAsk(books[j.no_token]);
      var edge = binaryEdgeBps(y, n, j.fee_rate, j.fee_rate);
      if (edge === null) { skippedBooks += 1; return; }
      var fees = takerFeeUsdc(1.0, y, j.fee_rate) + takerFeeUsdc(1.0, n, j.fee_rate);
      rows.push({ kind: "binary_complement", event_slug: j.event_slug, event_title: j.event_title,
        market_slug: j.market_slug, question: j.question, n_legs: 2, fee_rate: j.fee_rate,
        fee_rates: [j.fee_rate, j.fee_rate], fee_rate_source: j.fee_rate_source, yes_ask: y, no_or_sum_ask: n,
        sum_ask: y + n, edge_bps_pre_fee: (1 - (y + n)) * 10000, cost_after_fees: y + n + fees,
        edge_bps: edge, passes_300bps: passesMinEdge(edge) ? 1 : 0, volume24hr: j.volume24hr,
        leg_tokens: [j.yes_token, j.no_token] });
    });
    jobs.baskets.forEach(function (j) {
      var legs = [];
      for (var i = 0; i < j.legs.length; i++) {
        var a = bestAsk(books[j.legs[i].token_id]);
        if (a === null) { skippedBooks += 1; return; }
        legs.push(Object.assign({}, j.legs[i], { ask: a }));
      }
      var edge = basketEdgeBps(legs);
      if (edge === null) { skippedBooks += 1; return; }
      var cost = 0, sum = 0;
      legs.forEach(function (l) { sum += l.ask; cost += l.ask + takerFeeUsdc(1.0, l.ask, l.fee_rate); });
      rows.push({ kind: "negrisk_basket", event_slug: j.event_slug, event_title: j.event_title,
        market_slug: "", question: j.event_title, n_legs: legs.length,
        fee_rate: legs.map(function (l) { return l.fee_rate; }).join(";"),
        fee_rates: legs.map(function (l) { return l.fee_rate; }), fee_rate_source: "per-leg",
        yes_ask: "", no_or_sum_ask: sum, sum_ask: sum, edge_bps_pre_fee: (1 - sum) * 10000,
        cost_after_fees: cost, edge_bps: edge, passes_300bps: passesMinEdge(edge) ? 1 : 0,
        volume24hr: j.volume24hr, leg_tokens: legs.map(function (l) { return l.token_id; }) });
    });
    rows.sort(function (a, b) { return b.edge_bps - a.edge_bps; });
    rows.forEach(function (r) {
      var s = simulate(r.kind, r.leg_tokens, r.fee_rates, books);
      r.edge_bps_after_slip = s.edge_bps_after_slip;
      r.slipped_cost = s.slipped_cost;
      r.still_ge_300 = s.still_ge_300;
      r.sim_notes = s.notes;
    });
    var nPass = rows.filter(function (r) { return r.passes_300bps; }).length;
    return { rows: rows, nPass: nPass, skippedBooks: skippedBooks };
  }

  function countMarkets(events) {
    return events.reduce(function (a, e) { return a + activeMarkets(e).length; }, 0);
  }

  return {
    MIN_EDGE_BPS: MIN_EDGE_BPS, MAX_TOKENS: MAX_TOKENS, PAPER_SHARES: PAPER_SHARES,
    PESSIMISTIC_SLIP_BPS: PESSIMISTIC_SLIP_BPS, CATEGORY_RATES: CATEGORY_RATES,
    takerFeeUsdc: takerFeeUsdc, resolveFeeRate: resolveFeeRate, bestAsk: bestAsk,
    walkBuyVwap: walkBuyVwap, applyPessimisticSlip: applyPessimisticSlip,
    binaryEdgeBps: binaryEdgeBps, basketEdgeBps: basketEdgeBps, basketCostAfterFees: basketCostAfterFees,
    binaryCostAfterFees: binaryCostAfterFees, collectJobs: collectJobs, evaluate: evaluate,
    simulate: simulate, countMarkets: countMarkets, activeMarkets: activeMarkets
  };
});
