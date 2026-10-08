#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VERIF SOURCES INSTRUMENTS — garde mécanique de la classe E3 (câblée le 08/10/2026)
=================================================================================
CLASSE E3 = « instrument qui pointe la mauvaise source ». Le cas réel : un chiffrage lisait un
journal ÉCRIT EN DUR → il est resté aveugle dès que le journal vivant a changé (mesuré 21/09).
Règle de la maison : **le POINTEUR est la vérité** (on prend le journal le plus récent), jamais
une liste de fichiers en dur.

CE QUE LA GARDE MESURE (déterministe, pas de prose) : dans les scripts d'instruments, une
**référence datée `PAPER_V1_<date>`** écrite dans une LIGNE DE CODE (affectation), au lieu d'un
motif (`PAPER_V1_*.csv`). Une telle référence gèle l'instrument sur un journal mort.

SEVERITE (mesurée le 08/10 : 5 scripts, AUCUN invoqué) :
  - instrument INVOQUÉ par la boucle (plist / git_push_auto / analyste_cadence) + source en dur
    → **TROU** (l'instrument en service regarde un journal mort) ;
  - instrument NON invoqué (analyse ponctuelle) → **DETTE DÉCLARÉE** : nommé, compté, PAS fatal
    (R14 : on ne rougit pas à vie sur des outils d'archive ; on les DIT).

LECTURE SEULE · 0 ordre · 0 € · stdlib. Branché par `git_push_auto.sh` (3 h). `--autotest`.
"""
from __future__ import annotations

import glob
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent.parent
IM = RACINE / "Index_Maison"
SCRIPTS_HULK = RACINE / "hulk-mexc" / "scripts"
OUT_JSON = IM / "thermo" / "sources_instruments.json"

# Une référence datée à un journal (PAPER_V1_ + 6 à 8 chiffres), hors motif `PAPER_V1_*`.
RE_SOURCE_DATEE = re.compile(r"""["'][^"']*PAPER_V1_\d{6,8}[^"']*["']""")
ZONES_INVOCATION = ["Index_Maison/plists", "~/Library/LaunchAgents",
                    "Index_Maison/scripts/git_push_auto.sh",
                    "Index_Maison/scripts/analyste_cadence.sh"]


def utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")


def est_invoque(fichier: Path) -> bool:
    """Le script est-il appelé par un agent launchd ou par la boucle ? (mesuré, pas supposé)"""
    noms = [str(fichier)]
    try:
        if fichier.is_relative_to(RACINE):
            noms.append(str(fichier.relative_to(RACINE)))
    except Exception:
        pass
    for zone in ZONES_INVOCATION:
        base = Path(zone).expanduser() if zone.startswith(("~", "/")) else RACINE / zone
        cibles = sorted(base.rglob("*")) if base.is_dir() else [base]
        for c in cibles:
            if not c.is_file():
                continue
            try:
                txt = c.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue
            if any(n in txt for n in noms):
                return True
    return False


def ligne_est_code(ligne: str) -> bool:
    """Une ligne de code qui ASSIGNE une source — pas un commentaire, pas une docstring/print."""
    s = ligne.strip()
    if s.startswith("#") or not s:
        return False
    if "=" not in s and "[" not in s:
        return False                       # JOURNAUX = [...] contient [ mais pas forcément =
    return True


def scanner(scripts_dir: Path = SCRIPTS_HULK) -> dict:
    atteints, dettes = [], []
    if not scripts_dir.is_dir():
        return {"invoques_en_dur": atteints, "dettes": dettes, "n_scripts": 0}
    for f in sorted(scripts_dir.glob("*.py")):
        try:
            lignes = f.read_text(encoding="utf-8", errors="ignore").splitlines()
        except Exception:
            continue
        trouvees = []
        for i, ligne in enumerate(lignes, 1):
            if ligne_est_code(ligne) and RE_SOURCE_DATEE.search(ligne):
                trouvees.append({"ligne": i, "extrait": ligne.strip()[:110]})
        if not trouvees:
            continue
        item = {"fichier": f.name, "occurrences": trouvees, "invoque": est_invoque(f)}
        (atteints if item["invoque"] else dettes).append(item)
    return {"invoques_en_dur": atteints, "dettes": dettes,
            "n_scripts": len(list(scripts_dir.glob("*.py")))}


def main() -> int:
    if "--autotest" in sys.argv:
        return autotest()
    r = scanner()
    ok = not r["invoques_en_dur"]
    out = {"ts": utc(), "ok": ok, "n_scripts": r["n_scripts"],
           "n_invoques_en_dur": len(r["invoques_en_dur"]),
           "n_dettes": len(r["dettes"]), **r,
           "lecture_seule": True, "ordres": 0}
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[sources_instruments] {'OK' if ok else 'TROU'} — "
          f"{r['n_scripts']} scripts · {len(r['invoques_en_dur'])} source(s) datée(s) dans un "
          f"instrument INVOQUÉ · {len(r['dettes'])} dette(s) déclarée(s)")
    for d in r["dettes"]:
        print(f"  · dette déclarée : {d['fichier']} (non invoqué)")
    for t in r["invoques_en_dur"]:
        print(f"  🔴 {t['fichier']} : {t['occurrences'][0]['extrait']}")
    return 0 if ok else 1


def autotest() -> int:
    import tempfile
    cas = []
    with tempfile.TemporaryDirectory() as td:
        d = Path(td)
        (d / "bon.py").write_text('CSV = sorted(glob.glob("runs/PAPER_V1_*.csv"))[-1]\n', encoding="utf-8")
        (d / "dur.py").write_text('CSV = os.path.join(RUNS, "PAPER_V1_20260922_090430.csv")\n', encoding="utf-8")
        (d / "dur_liste.py").write_text('JOURNAUX = ["runs/PAPER_V1_20260918_165523.csv"]\n', encoding="utf-8")
        (d / "commentaire.py").write_text('# on lit PAPER_V1_20260918_165523.csv autrefois\nprint("ok")\n',
                                          encoding="utf-8")
        r = scanner(d)
        noms = {x["fichier"] for x in r["dettes"]} | {x["fichier"] for x in r["invoques_en_dur"]}
        cas.append(("motif (pointeur) → aucune détection", "bon.py" not in noms))
        cas.append(("source datée en dur → détectée", "dur.py" in noms))
        cas.append(("liste de journaux en dur → détectée", "dur_liste.py" in noms))
        cas.append(("référence datée en COMMENTAIRE → ignorée", "commentaire.py" not in noms))
        cas.append(("non invoqué → classé DETTE (pas trou)", any(x["fichier"] == "dur.py" for x in r["dettes"])))
    for nom, ok in cas:
        print(f"  {'[OK ]' if ok else '[KO ]'} {nom}")
    bon = all(ok for _, ok in cas)
    print(f"  -> {'GARDIEN FIABLE' if bon else 'GARDIEN CASSÉ'} ({sum(1 for _, o in cas if o)}/{len(cas)})")
    return 0 if bon else 3


if __name__ == "__main__":
    sys.exit(main())
