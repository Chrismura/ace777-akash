#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CARTE_PAIRES.py — la carte datée par paire que le moteur DEVRAIT lire pour l'ENTRÉE.

Génère `runs/CARTE_PAIRES_<date>.{json,md}` à partir des klines 1h en cache, des
profils moteur (`hulk-mexc/strategie/universe_profils.json`) et du dernier chiffrage
(`runs/CHIFFRAGE_SORTIE_*.json`).

Contenu par paire : fenêtre de CREUX et de PIC recalculées (7 j glissants, aucune heure
figée), amplitude médiane, spread/mur/archetype mesurés, et le verdict des entrées
réelles (dans la fenêtre de creux ou non) + le net mesuré.

0 ordre, 0 €. Recherche/lecture seule.
"""
import glob
import json
import os
from datetime import datetime, timezone
from statistics import median

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUNS = os.path.join(BASE, "runs")
CACHE = os.path.join(RUNS, "replay_cache")
PROFILS = os.path.join(BASE, "strategie", "universe_profils.json")
W_CAL_J = 7


def jour(ms):
    return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).strftime("%Y-%m-%d")


def heure(ms):
    return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).hour


def fenetres(bars, t_ref):
    cal = [b for b in bars if t_ref - W_CAL_J * 86400 * 1000 <= b["t"] < t_ref]
    if len(cal) < 24 * 3:
        return None
    par_h = {}
    for b in cal:
        par_h.setdefault(heure(b["t"]), []).append(b["c"])
    moy = {h: sum(v) / len(v) for h, v in par_h.items() if v}
    if len(moy) < 12:
        return None
    amp = median([(b["h"] - b["l"]) / b["l"] * 100 for b in cal if b["l"] > 0])
    return {"h_creux": min(moy, key=moy.get), "h_pic": max(moy, key=moy.get),
            "amp_pct": round(amp, 2)}


def main():
    profs = {}
    if os.path.exists(PROFILS):
        profs = json.load(open(PROFILS))
    ch = sorted(glob.glob(os.path.join(RUNS, "CHIFFRAGE_SORTIE_*.json")))
    chiff = json.load(open(ch[-1])) if ch else {}
    t_ref = int(datetime.now(timezone.utc).timestamp() * 1000)

    lignes = {}
    for f in sorted(glob.glob(os.path.join(CACHE, "*_1h_45j.json"))):
        pair = os.path.basename(f).split("_1h_")[0]
        try:
            bars = json.load(open(f))
        except Exception:
            continue
        w = fenetres(bars, t_ref)
        if not w:
            continue
        p = profs.get(pair) or {}
        cp = (chiff.get("par_paire") or {}).get(pair) or {}
        lignes[pair] = {
            "h_creux": w["h_creux"], "h_pic": w["h_pic"], "amp_pct": w["amp_pct"],
            "fenetre_entree_utc": [f"{(w['h_creux']-1)%24:02d}", f"{w['h_creux']:02d}", f"{(w['h_creux']+1)%24:02d}"],
            "fenetre_sortie_utc": [f"{(w['h_pic']-1)%24:02d}", f"{w['h_pic']:02d}", f"{(w['h_pic']+1)%24:02d}"],
            "archetype": p.get("archetype"),
            "spread_bps_med": p.get("spread_bps_med"),
            "mur_bid_med": p.get("mur_bid_med"),
            "drops15_pct": p.get("drops15_pct"),
            "n_entrees_reelles": cp.get("n_entrees"),
            "net_reel_2pct": cp.get("net_s1"),
            "net_creux_2pct": cp.get("net_creux_2pct"),
        }

    date = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M")
    out = {"ts": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "source": "klines 1h cache + universe_profils.json (moteur) + dernier CHIFFRAGE",
           "w_cal_j": W_CAL_J, "paires": lignes}
    jf = os.path.join(RUNS, f"CARTE_PAIRES_{date}.json")
    json.dump(out, open(jf, "w"), ensure_ascii=False, indent=1)
    # Carte CANONIQUE lue par le moteur (chemin fixe ; fail-open si périmée).
    eng = os.path.join(BASE, "strategie", "carte_fenetres_entree.json")
    json.dump(out, open(eng, "w"), ensure_ascii=False, indent=1)
    print(f"carte moteur : {eng}")

    md = [f"# Carte par paire — fenêtres recalculées ({out['ts']})", "",
          f"> creux/pic sur {W_CAL_J} j glissants · aucune heure figée · 0 ordre, 0 €", "",
          "| Paire | archétype | creux UTC | entrée | pic UTC | sortie | ampl. | spread | n entrées réelles | net réel +2% | net entrée-creux +2% |",
          "|---|---|---|---|---|---|---:|---:|---:|---:|---:|"]
    for pi in sorted(lignes, key=lambda k: -(lignes[k]["net_creux_2pct"] or -99)):
        v = lignes[pi]
        md.append(
            f"| {pi} | {v['archetype'] or '—'} | {v['h_creux']:02d}h | "
            f"{'/'.join(v['fenetre_entree_utc'])} | {v['h_pic']:02d}h | "
            f"{'/'.join(v['fenetre_sortie_utc'])} | {v['amp_pct']:.2f}% | "
            f"{v['spread_bps_med'] if v['spread_bps_med'] is not None else '—'} | "
            f"{v['n_entrees_reelles'] or 0} | "
            f"{v['net_reel_2pct'] if v['net_reel_2pct'] is not None else '—'} | "
            f"{v['net_creux_2pct'] if v['net_creux_2pct'] is not None else '—'} |")
    mf = os.path.join(RUNS, f"CARTE_PAIRES_{date}.md")
    open(mf, "w").write("\n".join(md) + "\n")
    print(f"carte : {jf}")
    print(f"carte : {mf}")
    print("\n".join(md))


if __name__ == "__main__":
    main()
