#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SIMU 20 ACTIFS — banc de recherche EDGE HULK (papier, 0 ordre).
========================================================================
Outil de RECHERCHE (n'exécute rien, ne touche pas au live).

But (18/09/2026, GO Christophe) : comparer, sur les 20 paires de l'univers MEXC,
  - V0  BASELINE      : dip ADAPTATIF (σ) + FILTRE TENDANCE + mise plafonnée MUR
  - V1  Φ=0,618       : entrée sur le retracement du nombre d'or (Fibonacci)
  - V2  SCOUT/HUNTER  : 10$ au Φ0,618 puis 20$ au Φ1,00 (moyenne à la baisse)
  - V3  TRAIL SIGMA   : trailing à giveback adaptatif (σ monte/descend)

Méthodologie HONNÊTE :
  - klinières 1H MEXC (limit 500 ≈ 20 j) — fenêtre COURTE, contient des pumps → hypothèse, pas preuve.
  - SPLIT out-of-sample : 60 % in-sample / 40 % test. On juge sur le TEST.
  - ~2 % de mur gelé (universe_profils) faute de mur LIVE historique → approximation notée.
  - Entrée à l'open de la bougie SUIVANTE (pas de lookahead).

Sortie : runs/SIMU_20_ACTIFS_<ts>.json + tableau console.
"""
from __future__ import annotations

import json
import glob
import os
import statistics
import sys
import time
import urllib.request
from datetime import datetime, timezone

BASE = os.path.expanduser("~/ace777-test-day1")
HULK = os.path.join(BASE, "hulk-mexc")
RUNS = os.path.join(HULK, "runs")
PROFILS = os.path.join(HULK, "strategie", "universe_profils.json")

PAIRES = ["BTCUSDT", "ETHUSDT", "XRPUSDT", "HBARUSDT", "RIZEUSDT", "ZBCNUSDT",
          "WUSDT", "REDUSDT", "CCUSDT", "PYTHUSDT", "BIOUSDT", "KITEUSDT",
          "TELUSDT", "CHIPUSDT", "RWAINCUSDT", "EDELUSDT", "QNTUSDT",
          "FLUIDUSDT", "RWAUSDT", "MNSRYUSDT"]

# --- paramètres ---
DIP_MIN, DIP_MAX, SIGMA_K = 5.0, 12.0, 1.0
RIP_PCT, STOP_PCT = 6.0, 12.0
TRAIL_ARM_PCT, TRAIL_GB_PCT = 10.0, 4.0
MISE_CAP_USD, MISE_MUR_FRAC = 30.0, 0.02
SCOUT_USD, HUNTER_USD = 10.0, 20.0
PHI = 0.618
FRAIS_BPS_COTE = 5.0  # 0,05 %/côté
OOS_FRAC = 0.40       # 40 % final = test out-of-sample


def utc_now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H%M%SZ")


def cutoff_ms():
    """--cutoff=YYYY-MM-DD : ne garder que les bougies AVANT cette date (test hors pump)."""
    for a in sys.argv:
        if a.startswith("--cutoff="):
            y, m, d = a.split("=", 1)[1].split("-")
            return int(datetime(int(y), int(m), int(d), tzinfo=timezone.utc).timestamp() * 1000)
    return None


DAYS_HIST = 90  # historique à récupérer (paginé ; MEXC plafonne à 500/appel)


def _get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "ace777-simu"})
    return json.load(urllib.request.urlopen(req, timeout=20))


def fetch_klines(pair, days=DAYS_HIST, cache_dir=RUNS):
    """Klines 1H paginées sur `days` jours (cache 6 h)."""
    cache = os.path.join(cache_dir, f"SIMU_KL_{pair}_{days}d.json")
    if os.path.exists(cache) and (time.time() - os.path.getmtime(cache)) < 6 * 3600:
        try:
            return json.load(open(cache))
        except Exception:
            pass
    end = int(time.time() * 1000)
    cur = end - days * 86400000
    out, seen = [], set()
    while cur < end:
        u = (f"https://api.mexc.com/api/v3/klines?symbol={pair}&interval=60m"
             f"&startTime={cur}&endTime={end}&limit=500")
        d = _get(u)
        if not isinstance(d, list) or not d:
            break
        for c in d:
            if c[0] not in seen:
                out.append(c)
                seen.add(c[0])
        if len(d) < 500:
            break
        cur = int(d[-1][0]) + 3600000
    out.sort(key=lambda c: c[0])
    try:
        json.dump(out, open(cache, "w"))
    except Exception:
        pass
    return out


def sma(vals, n, i):
    if i + 1 < n:
        return None
    return sum(vals[i + 1 - n:i + 1]) / n


def sigma_pct(closes, i, n=24):
    if i + 1 < n + 1:
        return 0.0
    sub = closes[i - n + 1:i + 1]
    rets = [(sub[k] / sub[k - 1] - 1) * 100 for k in range(1, len(sub)) if sub[k - 1]]
    return statistics.pstdev(rets) if len(rets) > 1 else 0.0


def profil_mur(pair, profils):
    p = profils.get(pair) or {}
    v = p.get("mur_bid_med")
    return float(v) if v else None


def mise_usd(pair, profils):
    mur = profil_mur(pair, profils)
    if mur:
        return max(1.0, min(MISE_CAP_USD, mur * MISE_MUR_FRAC))
    return MISE_CAP_USD


def dip_adaptatif(closes, i):
    s = sigma_pct(closes, i)
    return max(DIP_MIN, min(DIP_MAX, SIGMA_K * s))


def backtest_pair(pair, kl, profils, mode, i_start, i_end):
    """Rejoue une paire entre i_start et i_end. Retourne dict stats."""
    o = [float(c[1]) for c in kl]
    h = [float(c[2]) for c in kl]
    l = [float(c[3]) for c in kl]
    c = [float(c[4]) for c in kl]
    n = len(kl)
    stake = mise_usd(pair, profils)

    trades = 0
    wins = 0
    brut = 0.0
    frais = 0.0
    i = max(i_start, 170)
    curve = [(int(kl[i][0]), 0.0)]  # courbe d'equity réalisée : (ts_ms, net cumulé $)
    while i < min(i_end, n - 2):
        # ---- signal d'entrée ----
        sma24_now, sma24_prev = sma(c, 24, i), sma(c, 24, i - 1)
        sma7d = sma(c, 168, i)
        if sma24_now is None or sma24_prev is None or sma7d is None:
            i += 1
            continue
        trend = (sma24_now > sma24_prev) and (c[i] > sma7d)
        high24 = max(h[i - 23:i + 1]) if i >= 23 else h[i]
        drop = (high24 - c[i]) / high24 * 100 if high24 else 0.0

        entrer = False
        prix_entree_ref = o[i + 1]
        # Familles : trend on/off × veto none/fixe/dyn ; phi/scout traités à part.
        use_trend = mode not in ("notrend", "notrend_veto_fixe", "notrend_veto_dyn")
        use_veto = None
        if mode in ("veto_fixe", "notrend_veto_fixe"):
            use_veto = "fixe"
        elif mode in ("veto_dyn", "notrend_veto_dyn"):
            use_veto = "dyn"
        if mode == "phi":
            h7 = max(h[i - 167:i + 1]) if i >= 167 else high24
            l7 = min(l[i - 167:i + 1]) if i >= 167 else min(l[i - 23:i + 1])
            entrer = trend and h7 > l7 and c[i] <= (h7 - PHI * (h7 - l7))
        elif mode == "scout":
            h7 = max(h[i - 167:i + 1]) if i >= 167 else high24
            l7 = min(l[i - 167:i + 1]) if i >= 167 else min(l[i - 23:i + 1])
            entrer = trend and h7 > l7 and c[i] <= (h7 - PHI * (h7 - l7))
        else:
            entrer = drop >= dip_adaptatif(c, i) and (trend or not use_trend)
            if entrer and use_veto:
                # Veto Plancher (proxy klines) : pas d'achat si chute >= seuil ET pas de
                # rebond (prix < +3% au-dessus du bas roulant ~48h).
                seuil = 25.0 if use_veto == "fixe" else max(18.0, 2.5 * sigma_pct(c, i))
                bas_roul = min(l[max(0, i - 47):i + 1])
                if drop >= seuil and not (c[i] >= bas_roul * 1.03):
                    entrer = False
        if mode in ("phi", "scout"):
            h7 = max(h[i - 167:i + 1]) if i >= 167 else high24
            l7 = min(l[i - 167:i + 1]) if i >= 167 else min(l[i - 23:i + 1])
            if h7 > l7:
                lev_phi = h7 - PHI * (h7 - l7)
                entrer = trend and c[i] <= lev_phi

        if not entrer:
            i += 1
            continue

        # ---- position ----
        base_stake = SCOUT_USD if mode == "scout" else stake
        qte_total = base_stake / prix_entree_ref
        cout = base_stake
        scout_added = False
        h7 = max(h[i - 167:i + 1]) if i >= 167 else high24
        l7 = min(l[i - 167:i + 1]) if i >= 167 else min(l[i - 23:i + 1])
        lev_full = l7  # Φ1,00 = retracement complet
        # trailing adaptatif (mode trail_sig) : arm = σ_jour, gb = σ×0,6 si σ monte sinon ×0,2
        sig_entry = sigma_pct(c, i)
        sig_prev = sigma_pct(c, i - 6)
        if mode == "trail_sig":
            arm = max(3.0, sig_entry)
            gb = max(1.0, min(6.0, sig_entry * (0.6 if sig_entry >= sig_prev else 0.2)))
        else:
            arm, gb = TRAIL_ARM_PCT, TRAIL_GB_PCT

        entree_px = prix_entree_ref
        peak = entree_px
        rip_done = False
        j = i + 1
        sortie_ok = False
        while j < min(i_end, n):
            peak = max(peak, h[j])
            chg = (c[j] / entree_px - 1) * 100
            # Scout/Hunter : rajout 20$ si le prix atteint le retracement complet
            if mode == "scout" and not scout_added and c[j] <= lev_full:
                qte_total += HUNTER_USD / c[j]  # Hunter 20$ au retracement complet
                cout += HUNTER_USD
                scout_added = True
            # rip : vendre 50 %
            if not rip_done and chg >= RIP_PCT:
                proceeds = 0.5 * qte_total * c[j]
                brut += proceeds - 0.5 * cout
                frais += (0.5 * cout + proceeds) * FRAIS_BPS_COTE / 10000.0
                qte_total *= 0.5
                cout *= 0.5
                rip_done = True
                curve.append((int(kl[j][0]), brut - frais))
            # stop (sur clôture, garde-fou simple) OU trailing
            peak_chg = (peak / entree_px - 1) * 100
            trail_hit = peak_chg >= arm and chg <= peak_chg - gb
            if chg <= -STOP_PCT or trail_hit:
                proceeds = qte_total * c[j]
                brut += proceeds - cout
                frais += (cout + proceeds) * FRAIS_BPS_COTE / 10000.0
                curve.append((int(kl[j][0]), brut - frais))
                if (proceeds - cout) > 0:
                    wins += 1
                trades += 1
                sortie_ok = True
                i = j
                break
            j += 1
        if not sortie_ok:
            break
        i += 1

    net = brut - frais
    # Drawdown max sur la courbe d'equity réalisée ($ et % depuis le pic)
    peak = 0.0
    dd_max = 0.0
    dd_pct = 0.0
    for _t, v in curve:
        if v > peak:
            peak = v
        d = peak - v
        if d > dd_max:
            dd_max = d
        if peak > 0:
            p = (peak - v) / peak * 100.0
            if p > dd_pct:
                dd_pct = p
    return {"pair": pair, "mode": mode, "trades": trades, "wins": wins,
            "brut": round(brut, 4), "frais": round(frais, 4), "net": round(net, 4),
            "dd": round(dd_max, 4), "dd_pct": round(dd_pct, 1),
            "wr": round(100.0 * wins / trades, 1) if trades else 0.0,
            "curve": curve}


def portfolio_dd(rows):
    """Drawdown max de la courbe d'equity PORTEFEUILLE (réalisée).
    On fusionne les courbes des paires sur l'axe du temps et on cumule."""
    events = []
    for idx, r in enumerate(rows):
        for t, v in r.get("curve", []):
            events.append((t, idx, v))
    if not events:
        return 0.0, 0.0, 0.0
    events.sort(key=lambda e: (e[0], e[1]))
    cur = {}
    total = 0.0
    peak = 0.0
    dd = 0.0
    dd_pct = 0.0
    for _t, idx, v in events:
        total += v - cur.get(idx, 0.0)
        cur[idx] = v
        if total > peak:
            peak = total
        d = peak - total
        if d > dd:
            dd = d
        if peak > 0:
            p = (peak - total) / peak * 100.0
            if p > dd_pct:
                dd_pct = p
    return dd, dd_pct, peak


def run():
    profils = json.load(open(PROFILS)) if os.path.exists(PROFILS) else {}
    cut = cutoff_ms()
    klines = {}
    for pa in PAIRES:
        try:
            kl = fetch_klines(pa)
            if cut:
                kl = [c for c in kl if int(c[0]) < cut]
            klines[pa] = kl
        except Exception as e:
            print(f"  [warn] {pa}: klines indisponibles ({e})", file=sys.stderr)
    if cut:
        print(f"[simu] MODE HORS-PUMP : bougies < {sys.argv} (coupure {cut})")

    modes = ["base", "notrend", "veto_fixe", "veto_dyn",
             "notrend_veto_fixe", "notrend_veto_dyn", "phi", "scout", "trail_sig"]
    res = {m: {"full": [], "oos": []} for m in modes}
    for pa, kl in klines.items():
        n = len(kl)
        cut = int(n * (1 - OOS_FRAC))
        for m in modes:
            res[m]["full"].append(backtest_pair(pa, kl, profils, m, 0, n))
            res[m]["oos"].append(backtest_pair(pa, kl, profils, m, cut, n))

    ts = utc_now()
    out = {"ts": ts, "paires": list(klines.keys()), "n_paires": len(klines),
           "oos_frac": OOS_FRAC, "caveat":
           "Fenêtre 20j (500 bougies 1H), contient des pumps -> hypothèse, pas preuve. "
           "Mur gelé (2%) faute de mur LIVE historique. Juger le TEST (OOS).",
           "resultats": {}}
    print(f"\n=== SIMU 20 ACTIFS ({ts}) — {len(klines)} paires ===\n")
    for m in modes:
        for w in ("full", "oos"):
            rows = res[m][w]
            tr = sum(r["trades"] for r in rows)
            wi = sum(r["wins"] for r in rows)
            net = sum(r["net"] for r in rows)
            dd, _dd_pct, _peak = portfolio_dd(rows)
            dd_max_paire = max((r["dd"] for r in rows), default=0.0)
            ratio = (net / dd) if dd > 0 else float("nan")
            out["resultats"].setdefault(m, {})[w] = {
                "net": round(net, 2), "trades": tr,
                "wr": round(100.0 * wi / tr, 1) if tr else 0.0,
                "dd_portefeuille": round(dd, 2),
                "dd_max_paire": round(dd_max_paire, 2),
                "net_sur_dd": round(ratio, 2) if dd > 0 else None}
            tag = "OOS(test)" if w == "oos" else "full     "
            wr = round(100.0 * wi / tr, 1) if tr else 0.0
            print(f"  {m:10} {tag}: net={net:8.2f}$  trades={tr:3d}  WR={wr:5.1f}%  "
                  f"DD={dd:7.2f}$  DD/paire<={dd_max_paire:6.2f}$  "
                  f"net/DD={(ratio if dd > 0 else float('nan')):5.2f}")
        print()
    out["detail"] = {m: [{k: v for k, v in r.items() if k != "curve"} for r in res[m]["full"]]
                     for m in modes}
    path = os.path.join(RUNS, f"SIMU_20_ACTIFS_{ts}.json")
    json.dump(out, open(path, "w"), ensure_ascii=False, indent=1)
    print(f"details -> {path}")
    return out


def walkforward(mode="base", test_days=14):
    """Robustesse : fenêtres NON chevauchantes de `test_days` (pas de recompte),
    net agrégé par fenêtre -> vérifie que l'edge n'est pas concentré sur une période."""
    profils = json.load(open(PROFILS)) if os.path.exists(PROFILS) else {}
    win = test_days * 24
    buckets = {}
    for pa in PAIRES:
        try:
            kl = fetch_klines(pa)
        except Exception:
            continue
        n = len(kl)
        start = 170
        b = 0
        while start < n:
            r = backtest_pair(pa, kl, profils, mode, start, min(start + win, n))
            d = buckets.setdefault(b, {"net": 0.0, "trades": 0, "wins": 0, "rows": []})
            d["net"] += r["net"]
            d["trades"] += r["trades"]
            d["wins"] += r["wins"]
            d["rows"].append(r)
            start += win
            b += 1
    print(f"\n=== WALK-FORWARD [{mode}] — fenêtres de {test_days}j (non chevauchantes) ===")
    tot = 0.0
    for b in sorted(buckets):
        d = buckets[b]
        wr = round(100.0 * d["wins"] / d["trades"], 1) if d["trades"] else 0.0
        dd, _dd_pct, _pk = portfolio_dd(d["rows"])
        tot += d["net"]
        d["dd"] = round(dd, 2)
        print(f"  fenêtre {b+1}: net={d['net']:8.2f}$  trades={d['trades']:3d}  WR={wr:5.1f}%  "
              f"DD={dd:7.2f}$  net/DD={(d['net'] / dd if dd > 0 else float('nan')):5.2f}")
        d.pop("rows", None)
    print(f"  TOTAL net={tot:.2f}$")
    return buckets


if __name__ == "__main__":
    if "--walkforward" in sys.argv or any(a.startswith("--walkforward=") for a in sys.argv):
        _m = next((a.split("=", 1)[1] for a in sys.argv if a.startswith("--walkforward=")), "base")
        walkforward(_m)
    else:
        run()
