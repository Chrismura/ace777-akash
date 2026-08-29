#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""journal_divergence.py — JOURNALISATION CONTINUE du pattern DIVERGENCE (29/08).

RÉPOND AU RISQUE N°1 (Christophe, 29/08) : « journalise, mais faudra pas oublier
ensuite, c'est ça le problème, le risque. »

Ce script tourne PÉRIODIQUEMENT (plist launchd, toutes les 6h) et :
  1. Relance la machine d'analyse (analyse_divergence.py) → rapport horodaté.
  2. Écrit UN point dans runs/DIVERGENCE_SUIVI.jsonl (historique jour par jour :
     qui est LEADER / POMPE-PIÈGE à cet instant) → on voit le pattern évoluer.
  3. Met à jour runs/DIVERGENCE_ETAT.json (consommable par le cockpit) :
     - age du dernier rapport + statut FRAIS / STALE / ALERTE
     - stabilité du pattern (depuis combien de rapports CHIP est LEADER, etc.)
     - alerte si le rapport a plus de 24h = PERSONNE NE SUIT LE PATTERN.

AUCUNE décision de trading : c'est de l'observation/journalisation pure.

USAGE : python3 scripts/journal_divergence.py   (lancé par launchd)
"""
import datetime
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
RUNS = ROOT / "runs"
SUIVI = RUNS / "DIVERGENCE_SUIVI.jsonl"
ETAT = RUNS / "DIVERGENCE_ETAT.json"
STALE_H = 12      # au-delà : STALE (le pattern n'est pas re-vérifié assez souvent)
ALERTE_H = 24     # au-delà : ALERTE (personne ne suit le pattern depuis 1 jour)
NOW = datetime.datetime.now(datetime.timezone.utc)


def relance_analyse():
    """Relance la machine d'analyse → écrit runs/DIVERGENCE_<ts>.md."""
    p = subprocess.run(
        [sys.executable, str(SCRIPTS / "analyse_divergence.py")],
        capture_output=True, text=True, timeout=300,
        cwd=str(ROOT),
    )
    return p.returncode == 0, (p.stdout or "")[-600:]


def lit_signal_actuel():
    """Recalcule le signal directionnel (LEADER / POMPE-PIÈGE) par paire,
    sans réécrire : on importe la logique d'analyse_divergence."""
    sys.path.insert(0, str(SCRIPTS))
    import analyse_divergence as ad
    rows = ad.load()
    by = ad.series(rows)
    hb = ad.hourly(by)
    hours = sorted(set().union(*[set(v.keys()) for v in hb.values()]))
    pan = {h: ad.panier(hb, h) for h in hours}
    h = 3600
    fwd = ad.FWD_H
    seuil = ad.SEUIL_SIGNAL
    res = {}
    for p in sorted(hb):
        xs, ys = [], []
        for hh in hours:
            if hh not in hb[p] or pan.get(hh) is None or pan.get(hh + fwd * h) is None:
                continue
            xs.append(hb[p][hh])
            ys.append(pan[hh + fwd * h] - pan[hh])
        c = ad.corr(xs, ys)
        c = c if c is not None else 0.0
        if c >= seuil:
            sig = "LEADER"
        elif c <= -seuil:
            sig = "POMPE_PIEGE"
        else:
            sig = "neutre"
        res[p] = {"corr": round(c, 3), "signal": sig}
    return res


def main():
    ok, tail = relance_analyse()
    signaux = lit_signal_actuel()

    point = {
        "ts": NOW.isoformat(),
        "analyse_ok": ok,
        "signaux": signaux,
        "n_paires": len(signaux),
    }
    with open(SUIVI, "a", encoding="utf-8") as f:
        f.write(json.dumps(point, ensure_ascii=False) + "\n")

    # ---- stabilité (nb de rapports successifs où CHIP est LEADER, etc.) ----
    lignes = []
    if SUIVI.exists():
        for l in SUIVI.read_text(encoding="utf-8").splitlines():
            try:
                lignes.append(json.loads(l))
            except Exception:
                pass
    stables = {}
    for p in signaux:
        sig = signaux[p]["signal"]
        n = 0
        for l in reversed(lignes[:-1]):  # avant le point courant
            s = (l.get("signaux") or {}).get(p, {}).get("signal")
            if s == sig and sig != "neutre":
                n += 1
            else:
                break
        stables[p] = n + 1 if sig != "neutre" else 0

    # ---- BASCULES DE LEADERSHIP (rien n'est statique — Christophe 29/08) ----
    # On compare le rapport courant au précédent : si un signal a changé de camp
    # (LEADER→neutre, POMPE_PIEGE→neutre, neutre→LEADER, LEADER→POMPE_PIEGE...),
    # on le signale. C'est la matérialisation de « on suit tant que les chiffres
    # le montrent, on abandonne dès qu'ils changent ».
    bascules = []
    if len(lignes) >= 2:
        prec = lignes[-2].get("signaux") or {}
        for p, s in signaux.items():
            sig_new = s["signal"]
            sig_old = (prec.get(p) or {}).get("signal")
            if sig_old is None:
                continue
            if sig_new != sig_old and (sig_new != "neutre" or sig_old != "neutre"):
                bascules.append({
                    "pair": p,
                    "avant": sig_old,
                    "maintenant": sig_new,
                    "corr_avant": (prec.get(p) or {}).get("corr"),
                    "corr_maintenant": s["corr"],
                })

    # ---- état pour le cockpit + alerte oubli ----
    derniers = [l for l in lignes if l.get("analyse_ok")]
    age_h = None
    if derniers:
        age_h = (NOW - datetime.datetime.fromisoformat(derniers[-1]["ts"])).total_seconds() / 3600
    statut = "FRAIS" if (age_h is not None and age_h <= STALE_H) else (
        "STALE" if (age_h is not None and age_h <= ALERTE_H) else "ALERTE")
    etat = {
        "ts": NOW.isoformat(),
        "statut": statut,
        "age_rapport_h": round(age_h, 1) if age_h is not None else None,
        "bascules": bascules,
        "principe": "RIEN N'EST STATIQUE — signal suivi tant que les chiffres le confirment, abandonné dès inversion",
        "message": "⚠️ LE PATTERN DIVERGENCE N'EST PLUS SUIVI depuis "
                   f"{age_h:.0f}h — relancer la confrontation (voir docs/PROTOCOLE_DIVERGENCE_20260829.md)"
                   if statut == "ALERTE" else (
                   "🟡 Pattern suivi mais rapport vieux de "
                   f"{age_h:.0f}h — vérifier le moteur (croisement_contexte.jsonl)"
                   if statut == "STALE" else "🟢 Pattern divergence suivi et à jour."),
        "leaders": [p for p, s in signaux.items() if s["signal"] == "LEADER"],
        "pompes_pieges": [p for p, s in signaux.items() if s["signal"] == "POMPE_PIEGE"],
        "stabilite": stables,
        "recommande": "CONFRONTER AVEC CORTANA/FAMILLE" if statut != "FRAIS" else "OBSERVER",
    }
    ETAT.write_text(json.dumps(etat, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"[{NOW.strftime('%Y-%m-%d %H:%MZ')}] divergence journalisée ({len(signaux)} paires) "
          f"· analyse={'OK' if ok else 'ECHEC'} · statut={statut}")
    leaders = etat["leaders"]
    pieges = etat["pompes_pieges"]
    print(f"   LEADER : {', '.join(leaders) if leaders else 'aucun'}")
    print(f"   POMPE-PIÈGE : {', '.join(pieges) if pieges else 'aucun'}")
    for b in bascules:
        print(f"   🔄 BASCULE {b['pair']}: {b['avant']} → {b['maintenant']} "
              f"(corr {b['corr_avant']} → {b['corr_maintenant']}) — les chiffres ont changé, on adapte")
    if statut != "FRAIS":
        print("   " + etat["message"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
