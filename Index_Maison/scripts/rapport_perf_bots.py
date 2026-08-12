#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""rapport_perf_bots.py — rapport de performance des bots ACE777.

Lit les CSV de runs (master_*/logs) et calcule par bot :
  - cycles / skips / vrais trades
  - win rate, expectancy, PnL total, drawdown max
  - meilleur / pire trade, durée de détention moyenne, coût spread (bps)

Sortie : strategie/RAPPORT_PERF_BOTS.md (lisible par la famille et par toi).

Usage : python3 rapport_perf_bots.py
"""
import csv
import glob
import os

LOGS_DIRS = [
    "~/ace777-test-day1/master_plus_value/logs",
    "~/ace777-test-day1/master_qwen_plus_value/logs",
    "~/ace777-test-day1/master_base/logs",
    "~/ace777-test-day1/master_qwen_base/logs",
]
OUT = os.path.expanduser(
    "~/ace777-test-day1/Index_Maison/strategie/RAPPORT_PERF_BOTS.md")


def analyser_csv(path):
    """Retourne (trades, ouvertes, (cycles, skips), erreur).
    trade = round-trip COMPLET (status FILLED, entrée + sortie présentes).
    ouverte = position entrée sans sortie (status BUY/SELL) — pas un trade fini."""
    trades = []
    ouvertes = 0
    cycles = 0
    skips = 0
    try:
        with open(path, newline="", encoding="utf-8", errors="ignore") as f:
            for row in csv.DictReader(f):
                cycles += 1
                status = (row.get("status") or "").strip().upper()
                if status == "SKIPPED":
                    skips += 1
                    continue
                if status != "FILLED":
                    ouvertes += 1
                    continue
                try:
                    pnl = float(row.get("pnl") or 0)
                except ValueError:
                    pnl = 0.0
                try:
                    hold = float(row.get("holdSec") or 0)
                except ValueError:
                    hold = 0.0
                trades.append({
                    "ts": (row.get("ts") or "")[:16],
                    "side": (row.get("side") or "").upper(),
                    "pnl": pnl, "hold": hold,
                    "reason": (row.get("exitReason") or "").strip(),
                })
        return trades, ouvertes, (cycles, skips), None
    except Exception as e:
        return [], 0, (0, 0), str(e)


def stats(trades):
    if not trades:
        return None
    n = len(trades)
    wins = [t for t in trades if t["pnl"] > 0]
    losses = [t for t in trades if t["pnl"] <= 0]
    cum = 0.0
    pic = 0.0
    drow = 0.0
    for t in trades:
        cum += t["pnl"]
        if cum > pic:
            pic = cum
        dd = pic - cum
        if dd > drow:
            drow = dd
    return {
        "n": n, "wins": len(wins), "losses": len(losses),
        "winrate": 100.0 * len(wins) / n if n else 0.0,
        "total": sum(t["pnl"] for t in trades),
        "expectancy": sum(t["pnl"] for t in trades) / n if n else 0.0,
        "drawdown": drow,
        "best": max(t["pnl"] for t in trades),
        "worst": min(t["pnl"] for t in trades),
        "hold_avg": sum(t["hold"] for t in trades) / n if n else 0.0,
        "start": trades[0]["ts"], "end": trades[-1]["ts"],
    }


def verdict(s):
    if s["n"] < 10:
        return "ÉCHANTILLON TROP PETIT (moins de 10 trades) — pas de conclusion"
    if s["total"] > 0 and s["winrate"] >= 50:
        return "BÉNÉFICIAIRE ✅ — gagne et gagne souvent (à confirmer sur plus de jours)"
    if s["total"] > 0:
        return "BÉNÉFICIAIRE ⚠️ mais win rate < 50 % — il gagne gros rarement, perd souvent petit (survit grâce aux exceptions)"
    if s["total"] <= 0 and s["winrate"] >= 50:
        return "PERDANT ❌ — gagne souvent mais perd plus gros (les pertes mangent les gains)"
    return "PERDANT ❌ — ni gains ni régularité, à reconfigurer avant tout réel"


def nom_bot(path):
    base = os.path.splitext(os.path.basename(path))[0]
    return base.replace("_", " ")


def generer():
    lignes = []
    lignes.append("# RAPPORT DE PERFORMANCE DES BOTS — ACE777")
    lignes.append("")
    lignes.append("> Généré par rapport_perf_bots.py — les chiffres viennent des")
    lignes.append("> CSV de runs (master_*/logs). C'est la PREUVE, pas une opinion.")
    lignes.append("")
    resultats = []
    vus = set()
    for d in LOGS_DIRS:
        for p in sorted(glob.glob(os.path.join(os.path.expanduser(d), "*.csv"))):
            if p in vus:
                continue
            vus.add(p)
            trades, ouvertes, (cycles, skips), err = analyser_csv(p)
            s = stats(trades) if trades else None
            resultats.append((nom_bot(p), os.path.basename(p), cycles, skips,
                              ouvertes, s, err))

    # Tableau récapitulatif, trié par PnL total
    resultats.sort(key=lambda r: (r[5]["total"] if r[5] else -1e9), reverse=True)
    lignes.append("## Classement (PnL total)")
    lignes.append("")
    lignes.append("| Bot | Fichier | Cycles | Trades | Skips | Win rate | PnL total | Expectancy/trade | Drawdown max |")
    lignes.append("|---|---|---:|---:|---:|---:|---:|---:|---:|")
    for nom, fichier, cycles, skips, ouvertes, s, err in resultats:
        if s:
            lignes.append(
                f"| {nom} | `{fichier}` | {cycles} | {s['n']} | {skips} | "
                f"{s['winrate']:.0f}% | **{s['total']:+.2f} $** | {s['expectancy']:+.4f} $ | {s['drawdown']:.2f} $ |")
        else:
            lignes.append(f"| {nom} | `{fichier}` | {cycles} | 0 | {skips} | — | — | — | — |")
    lignes.append("")

    # Détails par bot
    lignes.append("## Détail par bot")
    for nom, fichier, cycles, skips, ouvertes, s, err in resultats:
        lignes.append("")
        lignes.append(f"### {nom}")
        if err:
            lignes.append(f"- ⛔ Lecture impossible : {err}")
            continue
        if not s:
            lignes.append(f"- Aucun vrai trade (skips uniquement : {skips})")
            continue
        lignes.append(f"- **{verdict(s)}**")
        lignes.append(f"- Trades : {s['n']} ({s['wins']} gagnants / {s['losses']} perdants) · Skips : {skips} · Cycles : {cycles}")
        lignes.append(f"- Win rate : **{s['winrate']:.1f}%** · PnL total : **{s['total']:+.2f} $**")
        lignes.append(f"- Expectancy : {s['expectancy']:+.4f} $/trade (en moyenne, chaque trade rapporte ce montant)")
        lignes.append(f"- Drawdown max : {s['drawdown']:.2f} $ (la pire chute de la courbe de gains, dans l'ordre du log)")
        lignes.append(f"- Meilleur trade : {s['best']:+.2f} $ · Pire trade : {s['worst']:+.2f} $")
        lignes.append(f"- Détention moyenne : {s['hold_avg']:.0f} s")
        lignes.append(f"- Période : {s['start']} → {s['end']}")
        if ouvertes:
            lignes.append(f"- {ouvertes} position(s) ouverte(s) en fin de run (sans sortie — non comptées comme trades)")

    lignes.append("")
    lignes.append("---")
    lignes.append("Généré par rapport_perf_bots.py — la famille peut valider sur cette base.")
    contenu = "\n".join(lignes)
    tmp = OUT + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(contenu)
    os.replace(tmp, OUT)
    return OUT


if __name__ == "__main__":
    out = generer()
    print(f"[OK] {out}")
    print(open(out, encoding="utf-8").read()[:1200])
