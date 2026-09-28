#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
v2_replay_hunter.py — V2-REPLAY (GO Christophe 12/09/2026)
Replay 90 jours du profil HUNTER à l'échelle, critères pré-enregistrés, ZÉRO ordre.

DISCIPLINE ANTI-DATA-SNOOPING (gravée avant tout run) :
  - LA SPÉCIFICATION EST FIGÉE ICI, AVANT D'AVOIR VU LES DONNÉES DE SIMULATION.
  - Paramètres tirés des valeurs DÉJÀ DOCUMENTÉES de la maison (manifest champion,
    CSV HUNTER, protocole audit R4) — JAMAIS des données testées.
  - UN SEUL ESSAI : aucune variante autorisée sans nouveau GO.
  - Verdict rendu PAR LES CRITÈRES FIGÉS (check_edge_criteria), pas par l'envie.

SPÉCIFICATION FIGÉE (profil HUNTER à l'échelle — FAITS_RETABLIS §3) :
  Entrée (à 00:00 UTC, au calme — « on est censé être déjà dedans ») :
    - SHORT si le prix a baissé hier ; LONG sinon (les 2 côtés — le trou des runs HUNTER).
    - Refus si ATR14_j ≥ 2,5 × médiane des 30 derniers ATR (orage — LECON pires trades).
    - Refus si volume hier < 0,8 × médiane 30 j (marché mort).
  Position : notionnel fixe 1 000 $ (à l'échelle ; le champion était ~600-1 500 $).
  Sorties (l'ordre du champion, conforme au manifest et aux runs HUNTER) :
    1. STOP de structure : −2,5 × ATR_j (large, laisse respirer — l'assurance de queue)
    2. TRAILING : suit le meilleur prix, rend 3 × ATR_j depuis le pic (sortie dominante §2)
    3. TIMEOUT : 48 h max (2 × le hold cible de l'audit)
  Coûts (modèle famille, cf. audit 21/08) : 4 bps/côté taker + slippage 0,5 $/côté.
  Frais = (prix_entrée+sortie)×qty×4bps + 1,0 $ slippage total.

CRITÈRES DE VERDICT (figés, tirés de check_edge_criteria.py + Meta-Testeur R4) :
  C1. n ≥ 30 trades fermés
  C2. net moyen/trade > frais moyen/trade  (l'edge paie le péage)
  C3. winrate net > 50 %
  C4. aucune raison de sortie > 40 % des pertes nettes totales
  C5. (Meta-Testeur R4) brut moyen/trade ≥ 3 × frais moyens/trade
  → VERDICT "EDGE_CONFIRME" si les 5 · "ECHEC" sinon. Il n'y a pas de 3e verdict.

Sorties : Index_Maison/thermo/v2_replay_resultat.json + rapport MD à côté.
Lecture seule sur la maison. Zéro clé API, zéro ordre.
"""
import json
import statistics
import sys
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

# ---------- SPÉCIFICATION FIGÉE (ne pas modifier sans nouveau GO) ----------
KLINE_URL = "https://api.binance.com/api/v3/klines"
SYMBOL = "BTCUSDT"
INTERVAL = "5m"
JOURS = 90
NOTIONNEL = 1000.0
STOP_ATR_MULT = 2.5        # stop de structure large
TRAIL_GIVEBACK_ATR = 3.0   # rend 3 ATR depuis le pic
TIMEOUT_H = 48
FEE_BPS_SIDE = 4.0         # bps par côté, taker (modèle famille 21/08)
SLIPPAGE_PER_SIDE = 0.5    # $ par côté
MIN_VOL_RATIO = 0.8        # volume hier ≥ 0,8× médiane 30 j
MAX_ATR_RATIO = 2.5        # ATR_j < 2,5× médiane 30 j (anti-orage)
VERDICT_CRITERES = ["C1_n>=30", "C2_net>frais", "C3_WR>50%", "C4_pertes<=40%", "C5_brut>=3x_frais"]


def http_json(url: str):
    # NOTE (12/09) : urllib timeoutait sur api.binance.com depuis cette machine
    # (curl passait — chemin réseau différent). Couche ACQUISITION uniquement,
    # la spécification de stratégie reste figée. curl + repli fapi + cache disque.
    import subprocess, hashlib
    h = hashlib.md5(url.encode()).hexdigest()[:16]
    cache = Path("/tmp") / f"v2replay_klines_{h}.json"
    if cache.exists():
        return json.loads(cache.read_text())
    last_err = None
    for attempt in range(3):
        try:
            r = subprocess.run(["curl", "-s", "-m", "20", url], capture_output=True, text=True, timeout=25)
            if r.returncode == 0 and r.stdout.strip().startswith("["):
                data = json.loads(r.stdout)
                cache.write_text(json.dumps(data))
                return data
            last_err = RuntimeError(f"curl rc={r.returncode} out={r.stdout[:120]!r}")
        except Exception as e:
            last_err = e
    raise last_err


def fetch_klines_5m(days: int):
    """Récupère `days` jours de klines 5m (fenêtres de 1000, marche arrière)."""
    end = int(datetime.now(timezone.utc).timestamp() * 1000)
    start = end - days * 24 * 3600 * 1000
    out = []
    cursor = start
    while cursor < end:
        url = f"{KLINE_URL}?symbol={SYMBOL}&interval={INTERVAL}&startTime={cursor}&limit=1000"
        batch = http_json(url)
        if not batch:
            break
        out.extend(batch)
        cursor = batch[-1][6] + 1  # close_time + 1 ms
        if len(batch) < 1000:
            break
        if len(out) % 5000 < 1000:
            print(f"[V2-REPLAY]   ... {len(out)} bougies")
    # dédoublonnage par open_time
    seen = {}
    for k in out:
        seen[k[0]] = k
    rows = [seen[k] for k in sorted(seen)]
    # colonne : 0 open_time, 1 open, 2 high, 3 low, 4 close, 5 volume, 6 close_time
    return [
        {
            "t": k[0] / 1000,
            "o": float(k[1]), "h": float(k[2]), "l": float(k[3]),
            "c": float(k[4]), "v": float(k[5]),
        }
        for k in rows
    ]


def daily_bars(kl):
    """Agrège les 5m en jours : O/H/L/C/volume/ATR14_journalier."""
    days = {}
    for k in kl:
        d = datetime.fromtimestamp(k["t"], tz=timezone.utc).date()
        b = days.setdefault(d, {"o": k["o"], "h": k["h"], "l": k["l"], "c": k["c"], "v": 0.0})
        b["h"] = max(b["h"], k["h"]); b["l"] = min(b["l"], k["l"]); b["c"] = k["c"]; b["v"] += k["v"]
    ds = sorted(days)
    bars = [dict(date=d, **days[d]) for d in ds]
    # ATR14 journalier (Wilder simplifié : moyenne arithmétique des TR)
    trs = []
    for i, b in enumerate(bars):
        if i == 0:
            tr = b["h"] - b["l"]
        else:
            pc = bars[i - 1]["c"]
            tr = max(b["h"] - b["l"], abs(b["h"] - pc), abs(b["l"] - pc))
        trs.append(tr)
        b["atr14"] = sum(trs[-14:]) / len(trs[-14:])
        b["tr"] = tr
    return bars


def run():
    print(f"[V2-REPLAY] récupération {JOURS} jours de {INTERVAL} {SYMBOL}...")
    kl = fetch_klines_5m(JOURS)
    print(f"[V2-REPLAY] {len(kl)} bougies 5m reçues")
    bars = daily_bars(kl)
    print(f"[V2-REPLAY] {len(bars)} jours agrégés")
    print("[V2-REPLAY] simulation (spécification figée v1 — un seul essai)...")
    # ---- simulation 5m ----
    trades = []
    refus = {"orage": 0, "volume_mort": 0, "deja_en_position": 0}
    pos = None  # {side, entry, qty, atr, best, t_entry, stop, j0_index}
    med_atr_all = statistics.median(b["atr14"] for b in bars[30:])
    # index des bougies 5m par jour
    from collections import defaultdict
    kl_by_day = defaultdict(list)
    for k in kl:
        kl_by_day[datetime.fromtimestamp(k["t"], tz=timezone.utc).date()].append(k)
    day_index = {b["date"]: i for i, b in enumerate(bars)}
    dates = [b["date"] for b in bars]

    for di in range(31, len(bars)):
        b = bars[di]
        yest = bars[di - 1]
        med30_atr = statistics.median(x["atr14"] for x in bars[max(0, di - 30):di])
        med30_vol = statistics.median(x["v"] for x in bars[max(0, di - 30):di])

        # 1) position ouverte -> la gérer sur les 5m du jour
        # FIX CAUSALITÉ (run 1 INVALIDÉ — voir rapport) : mémorise l'état au début
        # du jour pour interdire toute ré-entrée sur un prix du passé après une
        # sortie intra-jour.
        pos_au_debut = pos is not None
        if pos is not None:
            for k in kl_by_day.get(b["date"], []):
                if pos["side"] == "SHORT":
                    pos["best"] = min(pos["best"], k["l"])
                    trail = pos["best"] + TRAIL_GIVEBACK_ATR * pos["atr"]
                    stop = pos["stop"]
                    if k["h"] >= stop:   # stop de structure touché d'abord (conservateur)
                        exit_px = min(stop, k["h"])
                        close_trade(trades, pos, exit_px, k, "stop_structure")
                        pos = None; break
                    if k["h"] >= trail:
                        exit_px = min(trail, k["h"])
                        close_trade(trades, pos, exit_px, k, "trailing")
                        pos = None; break
                else:
                    pos["best"] = max(pos["best"], k["h"])
                    trail = pos["best"] - TRAIL_GIVEBACK_ATR * pos["atr"]
                    stop = pos["stop"]
                    if k["l"] <= stop:
                        exit_px = max(stop, k["l"])
                        close_trade(trades, pos, exit_px, k, "stop_structure")
                        pos = None; break
                    if k["l"] <= trail:
                        exit_px = max(trail, k["l"])
                        close_trade(trades, pos, exit_px, k, "trailing")
                        pos = None; break
                # timeout
                if (k["t"] - pos["t_entry"]) > TIMEOUT_H * 3600:
                    close_trade(trades, pos, k["c"], k, "timeout")
                    pos = None; break

        # 2) entrée à 00:00 UTC si pas de position
        sortie_ce_jour = pos_au_debut and pos is None
        if pos is not None:
            refus["deja_en_position"] += 1
        elif not sortie_ce_jour and b["date"] in kl_by_day:
            if yest["atr14"] >= MAX_ATR_RATIO * med30_atr:
                refus["orage"] += 1
            elif yest["v"] < MIN_VOL_RATIO * med30_vol:
                refus["volume_mort"] += 1
            else:
                # FIX CAUSALITÉ (run 1 INVALIDÉ) : la direction se décide sur la
                # bougie d'HIER (complète) — la version d'avant lisait le close du
                # JOUR (= le futur à 00:00) : fuite de donnée, run annulé.
                side = "SHORT" if yest["c"] < yest["o"] else "LONG"
                # entrée au 1er close 5m du jour (00:00-00:05)
                k0 = kl_by_day[b["date"]][0]
                atr = yest["atr14"]
                qty = NOTIONNEL / k0["c"]
                if side == "SHORT":
                    stop = k0["c"] + STOP_ATR_MULT * atr
                    best = k0["c"]
                else:
                    stop = k0["c"] - STOP_ATR_MULT * atr
                    best = k0["c"]
                pos = {"side": side, "entry": k0["c"], "qty": qty, "atr": atr,
                       "best": best, "stop": stop, "t_entry": k0["t"], "j0": di}
    # position résiduelle : clôturée au dernier close (comptée, horizon 90 j)
    if pos is not None:
        klast = kl[-1]
        close_trade(trades, pos, klast["c"], klast, "fin_periode")
        pos = None

    # ---- verdict selon critères figés ----
    n = len(trades)
    if n == 0:
        print("[V2-REPLAY] 0 trade simulé — spécification trop restrictive ou données insuffisantes")
        return
    frais = [t["fees"] for t in trades]
    nets = [t["net"] for t in trades]
    bruts = [t["brut"] for t in trades]
    wins = [t for t in trades if t["net"] > 0]
    wr = 100 * len(wins) / n
    avg_net = sum(nets) / n
    avg_fee = sum(frais) / n
    avg_brut = sum(bruts) / n
    losses_by_exit = {}
    for t in trades:
        if t["net"] < 0:
            losses_by_exit[t["exit"]] = losses_by_exit.get(t["exit"], 0.0) + (-t["net"])
    tot_losses = sum(losses_by_exit.values())
    worst_share = max(losses_by_exit.values()) / tot_losses * 100 if tot_losses > 0 else 0.0
    crit = {
        "C1_n>=30": n >= 30,
        "C2_net>frais": avg_net > avg_fee,
        "C3_WR>50%": wr > 50.0,
        "C4_pertes<=40%": worst_share <= 40.0,
        "C5_brut>=3x_frais": avg_brut >= 3 * avg_fee,
    }
    verdict = "EDGE_CONFIRME" if all(crit.values()) else "ECHEC"

    res = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "spec": "v1 figée avant run (voir docstring)",
        "periode": f"{dates[31]} -> {dates[-1]}",
        "jours": JOURS,
        "trades": n,
        "refus": refus,
        "wr_net_pct": round(wr, 1),
        "brut_total": round(sum(bruts), 2),
        "frais_total": round(sum(frais), 2),
        "net_total": round(sum(nets), 2),
        "avg_brut": round(avg_brut, 3),
        "avg_fee": round(avg_fee, 3),
        "avg_net": round(avg_net, 3),
        "perte_max_part_pct": round(worst_share, 1),
        "exit_counts": _exit_counts(trades),
        "criteres": crit,
        "verdict": verdict,
        "seuil_verdict": "les 5 critères — pas de 3e verdict",
    }
    out = Path.home() / "ace777-test-day1/Index_Maison/thermo/v2_replay_resultat.json"
    out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(res, ensure_ascii=False, indent=1))
    return res


def close_trade(trades, pos, exit_px, k, reason):
    qty = pos["qty"]
    direction = -1 if pos["side"] == "SHORT" else 1
    brut = (exit_px - pos["entry"]) * qty * direction
    fees = (pos["entry"] + exit_px) * qty * FEE_BPS_SIDE / 10000 + 2 * SLIPPAGE_PER_SIDE
    trades.append({"ts_in": pos["t_entry"], "ts_out": k["t"], "side": pos["side"],
                   "entry": pos["entry"], "exit": exit_px, "exit_reason": reason,
                   "brut": brut, "fees": fees, "net": brut - fees,
                   "hold_h": (k["t"] - pos["t_entry"]) / 3600})


def _exit_counts(trades):
    from collections import Counter
    return dict(Counter(t["exit_reason"] for t in trades))


if __name__ == "__main__":
    run()
