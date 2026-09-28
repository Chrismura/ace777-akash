#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SUIVI_SORTIE_MESUREE.py — GO 3 : « suivre en vol les prochaines sorties par paliers et vérifier
que le palier MESURÉ apparaît bien dans le journal ».

Ce que cet organe vérifie, mécaniquement, sur le journal EN VOL :
  1. LA RÈGLE EST-ELLE ARMÉE ? (`RIP_CADENCE_MESURE_ON=1` dans la config ET lue par le code).
     Sans cette ligne, « aucune sortie » serait indiscernable d'une règle éteinte — c'est
     exactement le silence qu'on a supprimé (règle #6).
  2. LE PALIER EFFECTIF EST-IL CELUI DE LA MESURE ? chaque sortie par palier porte désormais
     `rip_5.6pct_palier1_niv5.5pct_cad20.0rel2.74_sell_25pct`. On recalcule, depuis la config,
     ce que la règle DOIT donner — `niv = palier_fixe × max(1 ; cadence / référence)` — et on
     compare. Un écart = la règle n'est pas celle qu'on croit (on crie).
  3. L'HISTORIQUE : les sorties d'AVANT le câblage (ancien format, sans `niv`) sont comptées
     séparément — elles ne sont pas des anomalies, c'est l'histoire.

Source unique : le pointeur `.hulk_resume_pointer` → le state du run vivant → son CSV.
Lecture seule. 0 €, aucun ordre.
Produit : `Index_Maison/thermo/sortie_mesuree.json` + `.md` (affiché par le cockpit vol).
"""
import csv
import glob
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

MAISON = Path.home() / "ace777-test-day1"
IM = MAISON / "Index_Maison"
HULK = MAISON / "hulk-mexc"
RUNS = HULK / "runs"
DEFAUTS = HULK / "config" / "defaults.env"
SORTIE_JSON = IM / "thermo" / "sortie_mesuree.json"
SORTIE_MD = IM / "thermo" / "sortie_mesuree.md"

# rip_5.6pct_palier1_niv5.5pct_cad20.0rel2.74_sell_25pct   (format MESURÉ, 22/09)
RE_MESURE = re.compile(
    r"^rip_(?P<chg>[\d.]+)pct_palier(?P<palier>\d)_niv(?P<niv>[\d.]+)pct"
    r"_cad(?P<cad>[\d.]+)rel(?P<rel>[\d.]+)_sell_(?P<frac>\d+)pct")
# rip_6.1pct_palier1_sell_25pct                            (ancien format, AVANT la mesure)
RE_ANCIEN = re.compile(r"^rip_(?P<chg>[\d.]+)pct_palier(?P<palier>\d)_sell_(?P<frac>\d+)pct")


def lire_cfg():
    cfg = {}
    try:
        for l in DEFAUTS.read_text(encoding="utf-8", errors="ignore").splitlines():
            l = l.strip()
            if l and not l.startswith("#") and "=" in l:
                k, v = l.split("=", 1)
                cfg[k.strip()] = v.strip()
    except OSError:
        pass
    return cfg


def journal_vivant():
    """Le journal EN VOL, lu à la SOURCE : pointeur → state → CSV (une seule vérité)."""
    src = None
    try:
        ptr = (RUNS / ".hulk_resume_pointer").read_text(encoding="utf-8").strip()
        if ptr:
            csv_p = RUNS / ptr.replace("_state.json", ".csv")
            if csv_p.exists():
                src = ("pointeur", csv_p)
    except OSError:
        pass
    if src is None:
        fs = sorted(glob.glob(str(RUNS / "PAPER_V1_*.csv")), key=os.path.getmtime)
        if fs:
            src = ("mtime (repli)", Path(fs[-1]))
    return src


def main():
    cfg = lire_cfg()
    on = int(cfg.get("RIP_CADENCE_MESURE_ON", "0") or 0) == 1
    ref = float(cfg.get("RIP_CADENCE_REF_PCT", "7.30") or 7.30)
    p1e = float(cfg.get("RIP_EARLY_P1_PCT", "2.0"))
    p2e = float(cfg.get("RIP_EARLY_P2_PCT", "6.0"))
    p1l = float(cfg.get("RIP_LATE_P1_PCT", "6.0"))
    p2l = float(cfg.get("RIP_LATE_P2_PCT", "8.0"))
    early_pairs = {p.strip().upper() for p in
                   (cfg.get("RIP_EARLY_PAIRS") or "XRPUSDT,HBARUSDT").split(",") if p.strip()}

    src = journal_vivant()
    if not src:
        print("SUIVI SORTIE MESURÉE — aucun journal PAPER_V1 (rien à suivre)")
        return 1
    origine, chemin = src

    mesure, ancien, anomalies, derniers = [], 0, [], []
    with open(chemin, newline="") as f:
        for r in csv.DictReader(f):
            raison = (r.get("reason") or "").strip()
            if not raison.startswith("rip_"):
                continue
            m = RE_MESURE.match(raison)
            if m:
                pair = (r.get("pair") or "").strip()
                d = m.groupdict()
                fixe = (p1e if d["palier"] == "1" else p2e) if pair in early_pairs \
                    else (p1l if d["palier"] == "1" else p2l)
                attendu = fixe * max(1.0, float(d["cad"]) / ref) if (on and ref > 0) else fixe
                ecart = abs(float(d["niv"]) - attendu)
                mesure.append({"ts": r.get("ts"), "pair": pair, "palier": int(d["palier"]),
                               "niv": float(d["niv"]), "attendu": round(attendu, 4),
                               "cad": float(d["cad"]), "rel": float(d["rel"]),
                               "ecart": round(ecart, 4)})
                if ecart > 0.05:      # 0,05 pt = borne d'affichage (le journal arrondit au 0,1)
                    anomalies.append(mesure[-1])
            elif RE_ANCIEN.match(raison):
                ancien += 1

    derniers = mesure[-5:]
    # Réserves écrites (E8) : une borne d'affichage n'est pas une tolérance de règle.
    verdict = ("EN ATTENTE — la règle est armée, aucune sortie par palier depuis le câblage"
               if not mesure and on else
               f"{len(mesure)} sortie(s) par palier depuis le câblage — toutes conformes"
               if mesure and not anomalies else
               f"⚠ {len(anomalies)} sortie(s) NON conforme(s) à la règle mesurée"
               if anomalies else
               "RÈGLE ÉTEINTE (RIP_CADENCE_MESURE_ON=0) — les paliers sont restés fixes")

    print("SUIVI SORTIE MESURÉE (R17) — lecture du journal en vol")
    print(f"  journal      : {chemin.name} (source : {origine})")
    print(f"  règle armée  : {'OUI' if on else 'NON'} "
          f"(RIP_CADENCE_MESURE_ON={cfg.get('RIP_CADENCE_MESURE_ON')}, référence "
          f"{ref:.2f} %/jour)")
    print(f"  sorties MESURÉES (format `niv…cad…rel…`) : {len(mesure)}")
    print(f"  sorties d'AVANT le câblage (ancien format) : {ancien}  (histoire, pas anomalie)")
    for d in derniers:
        print(f"    {d['ts']} {d['pair']:11s} palier{d['palier']} niv {d['niv']:.1f} % "
              f"(attendu {d['attendu']:.1f} · cad {d['cad']:.1f} · rel {d['rel']:.2f})")
    print(f"  VERDICT : {verdict}")

    maintenant = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    etat = {"ts": maintenant, "journal": chemin.name, "source": origine, "regle_armee": on,
            "reference_pct": ref, "n_mesurees": len(mesure), "n_anciennes": ancien,
            "n_conformes": len(mesure) - len(anomalies), "n_anomalies": len(anomalies),
            "verdict": verdict, "dernieres": derniers, "anomalies": anomalies[:10]}
    SORTIE_JSON.parent.mkdir(parents=True, exist_ok=True)
    SORTIE_JSON.write_text(json.dumps(etat, ensure_ascii=False, indent=1), encoding="utf-8")
    SORTIE_MD.write_text(
        f"# Suivi de la sortie mesurée — {maintenant}\n\n"
        f"- Règle armée : **{'OUI' if on else 'NON'}** (référence {ref:.2f} %/jour)\n"
        f"- Sorties par palier **au format mesuré** : **{len(mesure)}** "
        f"(conformes {len(mesure) - len(anomalies)} · anomalies {len(anomalies)})\n"
        f"- Sorties d'avant le câblage (ancien format) : {ancien}\n"
        f"- **Verdict : {verdict}**\n\n"
        "Chaque sortie porte le palier EFFECTIF et la mesure qui l'a produit :\n"
        "`rip_5.6pct_palier1_niv5.5pct_cad20.0rel2.74_sell_25pct` → palier mesuré 5,5 % "
        "(il aurait été 2,0 % avant), cadence mesurée 20,0 %/jour, rapport 2,74.\n",
        encoding="utf-8")
    return 0 if not anomalies else 3


if __name__ == "__main__":
    raise SystemExit(main())
