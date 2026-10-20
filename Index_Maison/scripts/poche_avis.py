#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""poche_avis.py — AVIS DÉTERMINISTE PAR POCHE (chantier 20/10, GO Christophe).

Pourquoi : Cortana juge le marché BTC ; Hulk trade des alts. Le dry-run du
20/10 a prouvé que juger les avis BTC sur les alts tombe à ~40 % — il faut
des avis PAR ACTIF, dans l'unité de l'actif (leçon 22/09).

Doctrine (même que verdict_marche_maths.py, par actif) :
  chg24 <= q20(chg24 histo de LA PAIRE) → LONG (contrarian)
  chg24 >= q80                           → SHORT
  sinon                                  → NEUTRE
Seuils = quantiles mesurés, jamais choisis. Sans LLM (0 appel, R10-friendly).
Faits joints : régime + murs + spread du satellite, position Hulk.

Usage :
  python3 poche_avis.py                        # émet l'avis du jour (ETH+XRP)
  python3 poche_avis.py --calibrer             # quantiles par paire (klines 200j)
  python3 poche_avis.py --backtest --jours 30  # rejoue la règle sur klines
IA=Buffy (Muse Spark 1.3, Freebuff).
"""
from __future__ import annotations
import argparse, json, statistics, sys, urllib.request
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
THERMO = RACINE / "Index_Maison" / "thermo"
POCHES = ["ETHUSDT", "XRPUSDT"]
OUT_DIR = THERMO / "analyses_poche"
SEUIL_MOVE_BASE = 0.3  # % (même que score_justesse, scalé par cadence)


def klines(sym: str, limit: int = 200) -> list:
    url = f"https://api.mexc.com/api/v3/klines?symbol={sym}&interval=1d&limit={limit}"
    req = urllib.request.Request(url, headers={"User-Agent": "poche-avis/1.0"})
    with urllib.request.urlopen(req, timeout=20) as r:
        return json.loads(r.read())


def closes(sym: str, limit: int = 200) -> list[tuple[str, float]]:
    out = []
    for k in klines(sym, limit):
        dt = datetime.fromtimestamp(k[0] / 1000, tz=timezone.utc).strftime("%Y-%m-%d")
        out.append((dt, float(k[4])))
    return out


def calibrer(sym: str) -> dict:
    cl = closes(sym)
    chg = [(cl[i + 1][1] / cl[i][1] - 1) * 100 for i in range(len(cl) - 1)]
    chg_s = sorted(chg)
    q20 = chg_s[int(0.2 * len(chg_s))]
    q80 = chg_s[int(0.8 * len(chg_s))]
    cad = statistics.median(abs(c) for c in chg)
    seuil = SEUIL_MOVE_BASE * cad / 0.936
    # GO A (20/10) — PROBAS EMPIRIQUES PAR ZONE (Brier-ready, ForecastBench) :
    # P(succès | zone) mesurée sur la fenêtre : pas de proba inventée, la proba
    # = fréquence historique du succès dans la zone. Événement LONG : lendemain
    # >= +seuil ; SHORT : <= -seuil ; NEUTRE : |move| < seuil (le calme annoncé).
    def freq(zone, succes):
        ok = n = 0
        for i in range(len(chg) - 1):
            if zone(chg[i]):
                n += 1
                if succes(chg[i + 1]):
                    ok += 1
        return round(ok / n, 3) if n else 0.5, n
    p_long, n_long = freq(lambda c: c <= q20, lambda mv: mv >= seuil)
    p_short, n_short = freq(lambda c: c >= q80, lambda mv: mv <= -seuil)
    p_calm, n_calm = freq(lambda c: q20 < c < q80, lambda mv: abs(mv) < seuil)
    return {"q20": round(q20, 3), "q80": round(q80, 3),
            "cadence_med": round(cad, 3),
            "seuil_move": round(seuil, 3),
            "p_long": p_long, "n_long": n_long,
            "p_short": p_short, "n_short": n_short,
            "p_calm": p_calm, "n_calm": n_calm,
            "n_jours": len(chg), "calibre_le": datetime.now(timezone.utc).strftime("%Y-%m-%d")}


EVENEMENTS = {"LONG": "lendemain >= +seuil (rebond contrarian)",
              "SHORT": "lendemain <= -seuil (retombée contrarian)",
              "NEUTRE": "|lendemain| < seuil (calme annoncé)"}


def avis(chg24: float | None, cal: dict) -> dict:
    if chg24 is None:
        return {"avis": "NEUTRE", "motif": "chg24 absent", "proba": 0.5,
                "evenement": EVENEMENTS["NEUTRE"]}
    if chg24 <= cal["q20"]:
        return {"avis": "LONG", "motif": f"chg24 {chg24:.2f} <= q20 {cal['q20']}",
                "proba": cal["p_long"], "evenement": EVENEMENTS["LONG"]}
    if chg24 >= cal["q80"]:
        return {"avis": "SHORT", "motif": f"chg24 {chg24:.2f} >= q80 {cal['q80']}",
                "proba": cal["p_short"], "evenement": EVENEMENTS["SHORT"]}
    return {"avis": "NEUTRE", "motif": f"chg24 {chg24:.2f} dans [{cal['q20']}, {cal['q80']}] ",
            "proba": cal["p_calm"], "evenement": EVENEMENTS["NEUTRE"]}


def faits_live(sym: str) -> dict:
    f = {"prix": None, "regime": "?", "wall_bid": None, "wall_ask": None,
         "spread_bps": None, "chg24": None}
    try:
        sat = json.loads((RACINE / "hulk-mexc" / "runs" / "aspiration_live.json").read_text())
        p = (sat.get("paires") or {}).get(sym) or {}
        f.update({"prix": p.get("prix"), "regime": p.get("regime", "?"),
                  "wall_bid": p.get("wall_bid_usdt"), "wall_ask": p.get("wall_ask_usdt"),
                  "spread_bps": p.get("spread_bps")})
    except Exception:
        pass
    try:
        url = f"https://api.mexc.com/api/v3/ticker/24hr?symbol={sym}"
        req = urllib.request.Request(url, headers={"User-Agent": "poche-avis/1.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            t = json.loads(r.read())
        f["chg24"] = float(t.get("priceChangePercent") or 0.0)
        if f["prix"] is None:
            f["prix"] = float(t.get("lastPrice") or 0.0)
    except Exception:
        pass
    return f


def emettre() -> list[dict]:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    jour = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    lignes = []
    for sym in POCHES:
        cal = calibrer(sym)
        f = faits_live(sym)
        a = avis(f["chg24"], cal)
        lignes.append({"ts": datetime.now(timezone.utc).isoformat(), "pair": sym,
                       "horizon": "24h", **a, "seuil_long": cal["q20"],
                       "seuil_short": cal["q80"], "seuil_move": cal["seuil_move"],
                       "faits": f})
    with (OUT_DIR / f"{jour}.jsonl").open("a", encoding="utf-8") as fh:
        for l in lignes:
            fh.write(json.dumps(l, ensure_ascii=False) + "\n")
    # TABLEAU (20/10) : dernier avis par paire, lu par la carte POCHES
    # (indices.html via :17800/thermo/poche_latest.json). Écrasé, jamais appendé.
    (THERMO / "poche_latest.json").write_text(
        json.dumps({"ts": datetime.now(timezone.utc).isoformat(), "avis": lignes},
                   ensure_ascii=False, indent=1), encoding="utf-8")
    return lignes


def backtest(jours: int = 30) -> dict:
    res = {}
    for sym in POCHES:
        cl = closes(sym, 200)
        chg = [(cl[i + 1][1] / cl[i][1] - 1) * 100 for i in range(len(cl) - 1)]
        cal_chg = chg[: len(chg) - jours]
        s = sorted(cal_chg)
        cal = {"q20": s[int(0.2 * len(s))], "q80": s[int(0.8 * len(s))]}
        cad = statistics.median(abs(c) for c in cal_chg)
        seuil = SEUIL_MOVE_BASE * cad / 0.936
        hit = n = 0
        for i in range(len(chg) - jours, len(chg) - 1):
            a = avis(chg[i], cal)["avis"]
            if a == "NEUTRE":
                continue
            mv = chg[i + 1]
            n += 1
            bon = (mv > 0 and a == "LONG") or (mv < 0 and a == "SHORT")
            if bon and abs(mv) >= seuil:
                hit += 1
        res[sym] = {"n": n, "hit": hit, "pct": round(100 * hit / n, 1) if n else 0.0,
                    "q20": round(cal["q20"], 3), "q80": round(cal["q80"], 3),
                    "seuil_move": round(seuil, 3)}
    return res


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--calibrer", action="store_true")
    ap.add_argument("--backtest", action="store_true")
    ap.add_argument("--jours", type=int, default=30)
    ap.add_argument("--emettre", action="store_true")
    args = ap.parse_args()
    if args.backtest:
        print(json.dumps(backtest(args.jours), ensure_ascii=False, indent=1))
    elif args.calibrer:
        print(json.dumps({s: calibrer(s) for s in POCHES}, ensure_ascii=False, indent=1))
    else:
        for l in emettre():
            print(l["pair"], l["avis"], "-", l["motif"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
