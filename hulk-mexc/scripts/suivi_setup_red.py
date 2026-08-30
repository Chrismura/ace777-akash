#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""suivi_setup_red.py — Suivi quotidien du set-up RED (30/08/2026).

Consigne Christophe : « on fait son set up, on l'observe, dans quelques jours on refait
le point en relation à son comportement observé. Mesure aujourd'hui, mesure demain =
différence ou pas. »

Ce script capture à chaque run les mesures clés du set-up RED et les journalise dans
runs/SUIVI_SETUP_RED.jsonl + runs/SUIVI_SETUP_RED.md (historique visible jour par jour).
Il ne touche à RIEN dans Hulk : pure mesure d'observation.

Mesures capturées :
- prix actuel + heure UTC + fenêtre courante (creux 14-17h / nuit 21-05h / autre)
- poussière (tx fantômes), mur bid max/moy, spoof, wall_strength, régime, dd15, move6
- signal précurseur (si DIVERGENCE_ETAT.json dispo) : corr + classification
- corrélation prix RED vs BTC et RED vs ETH (fenêtre glissante 24h de points horaires)
- verdict du set-up au moment du run : fenêtre OK ? poussière <15% ? prix dans zone creux ?
"""
import json
import os
import statistics
import sys
from collections import defaultdict
from datetime import datetime, timezone

RUNS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "runs")
CROIS = os.path.join(RUNS, "croisement_contexte.jsonl")
ETAT = os.path.join(RUNS, "DIVERGENCE_ETAT.json")
JSONL = os.path.join(RUNS, "SUIVI_SETUP_RED.jsonl")
MD = os.path.join(RUNS, "SUIVI_SETUP_RED.md")

PAIRES = ("REDUSDT", "BTCUSDT", "ETHUSDT")
CREUX_H = (14, 15, 16, 17)   # fenêtre d'entrée autorisée
NUIT_H = (21, 22, 23, 0, 1, 2, 3, 4)  # fenêtre de pic
POUSSIERE_SEUIL = 15.0      # déclencheur poussière < 15%
ZONE_CREUX_BASSE = (0.107, 0.109)  # zone d'entrée idéale vue le 30/08


def load_points():
    dat = defaultdict(list)
    for line in open(CROIS, encoding="utf-8"):
        try:
            d = json.loads(line)
        except Exception:
            continue
        if d.get("pair") in PAIRES:
            dat[d["pair"]].append(d)
    for p in dat:
        dat[p].sort(key=lambda x: x["ts"])
    return dat


def corr24h(dat, a, b, now_ts):
    """Corrélation des prix horaires RED vs BTC/ETH sur les dernières 24h."""
    def hourly(pair):
        by = defaultdict(list)
        for d in dat[pair]:
            if now_ts - 24 * 3600 <= d["ts"] <= now_ts:
                by[d["utc"][:13]].append(d["price"])
        ks = sorted(by)
        return [sum(by[k]) / len(by[k]) for k in ks]
    ra, rb = hourly(a), hourly(b)
    n = min(len(ra), len(rb))
    if n < 6:
        return None
    x, y = ra[-n:], rb[-n:]
    mx, my = statistics.mean(x), statistics.mean(y)
    num = sum((xi - mx) * (yi - my) for xi, yi in zip(x, y))
    den = (sum((xi - mx) ** 2 for xi in x) * sum((yi - my) ** 2 for yi in y)) ** 0.5
    return num / den if den else None


def main():
    dat = load_points()
    if not dat.get("REDUSDT"):
        print("[ERR] pas de points RED dans", CROIS)
        sys.exit(1)
    now = dat["REDUSDT"][-1]
    now_ts = now["ts"]
    utc = now["utc"]
    h = int(utc[11:13])

    fenetre = "CREUX 14-17h" if h in CREUX_H else ("NUIT 21-05h" if h in NUIT_H else "AUTRE")
    poussiere = now.get("poussiere_taux_fantome")
    mur_max = now.get("mur_bid_max_usd")
    mur_moy = now.get("mur_bid_moy_usd")
    spoof = now.get("mur_spoof_pct")
    wall = now.get("wall_strength")
    regime = now.get("regime")
    dd15 = now.get("dd15_pct")
    m6 = now.get("m6_pct")
    prix = now["price"]

    # signal précurseur (dernier run divergence dispo)
    signal = None
    try:
        if os.path.exists(ETAT):
            etat = json.load(open(ETAT, encoding="utf-8"))
            leaders = etat.get("leaders") or []
            pompes = etat.get("pompes_pieges") or []
            stab = (etat.get("stabilite") or {}).get("REDUSDT")
            if "REDUSDT" in leaders:
                cls = "LEADER"
            elif "REDUSDT" in pompes:
                cls = "POMPE_PIEGE"
            else:
                cls = "neutre"
            signal = {"class": cls, "stabilite": stab}
    except Exception:
        pass

    # corrélations 24h
    corr_btc = corr24h(dat, "REDUSDT", "BTCUSDT", now_ts)
    corr_eth = corr24h(dat, "REDUSDT", "ETHUSDT", now_ts)

    # verdict du set-up à l'instant T
    verdict = []
    if h in CREUX_H:
        verdict.append("fenêtre OK")
    else:
        verdict.append(f"hors fenêtre ({utc[11:13]}h)")
    if poussiere is not None:
        verdict.append(f"poussière {poussiere:.1f}% {'<15 ✓' if poussiere < POUSSIERE_SEUIL else '≥15 ✗'}")
    if prix is not None:
        in_zone = ZONE_CREUX_BASSE[0] <= prix <= ZONE_CREUX_BASSE[1]
        verdict.append(f"prix {prix:.5f} {'zone creux ✓' if in_zone else 'hors zone'}")
    if mur_max is not None:
        verdict.append(f"mur {mur_max:,.0f}$")
    verdict_txt = " · ".join(verdict)

    rec = {
        "ts": utc,
        "prix": prix,
        "heure_utc": h,
        "fenetre": fenetre,
        "regime": regime,
        "poussiere": poussiere,
        "mur_bid_max_usd": mur_max,
        "mur_bid_moy_usd": mur_moy,
        "spoof_pct": spoof,
        "wall_strength": wall,
        "dd15_pct": dd15,
        "m6_pct": m6,
        "corr_btc_24h": corr_btc,
        "corr_eth_24h": corr_eth,
        "signal_divergence": signal,
        "verdict": verdict_txt,
    }

    # append JSONL
    with open(JSONL, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")

    # régénère le MD historique
    rows = [json.loads(l) for l in open(JSONL, encoding="utf-8") if l.strip()]
    lines = [
        "# 📈 SUIVI SET-UP RED — historique des mesures (démarrage 30/08/2026)",
        "",
        "Consigne Christophe : mesurer aujourd'hui, mesurer demain, voir la différence.",
        "Source : `croisement_contexte.jsonl` · ne modifie rien dans Hulk.",
        "",
        "| # | Date (UTC) | Heure | Fenêtre | Prix | Régime | Poussière % | Mur max $ | Spoof % | dd15 % | corr BTC 24h | corr ETH 24h | Signal div | Verdict |",
        "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for i, r in enumerate(rows, 1):
        sig = r.get("signal_divergence") or {}
        sig_txt = f"{sig.get('class','?')} (stab {sig.get('stabilite','?')})" if sig else "—"
        cbtc = f"{r['corr_btc_24h']:.2f}" if r.get("corr_btc_24h") is not None else "—"
        ceth = f"{r['corr_eth_24h']:.2f}" if r.get("corr_eth_24h") is not None else "—"
        lines.append(
            f"| {i} | {r['ts']} | {r.get('heure_utc','?')}h | {r.get('fenetre','?')} | "
            f"{r.get('prix','?')} | {r.get('regime','?')} | {r.get('poussiere','?')} | "
            f"{r.get('mur_bid_max_usd','?')} | {r.get('spoof_pct','?')} | {r.get('dd15_pct','?')} | "
            f"{cbtc} | {ceth} | {sig_txt} | {r.get('verdict','?')} |"
        )
    lines.append("")
    lines.append("_Règle de lecture : on compare les lignes entre elles (même heure de mesure = comparable)._")
    with open(MD, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))

    print(f"[OK] mesure {utc} -> {len(rows)} ligne(s) dans SUIVI_SETUP_RED")
    print(f"     prix={prix} fenêtre={fenetre} poussière={poussiere} corrBTC={corr_btc} corrETH={corr_eth}")
    print(f"     verdict: {verdict_txt}")


if __name__ == "__main__":
    main()