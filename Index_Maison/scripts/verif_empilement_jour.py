#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EMPILEMENT DU JOUR — GARDE MÉCANIQUE DE LA CLASSE E9
====================================================
CLASSE E9 (registre) : « Empiler les corrections le même jour » — 22/09 : poser un
refroidissement puis le RETIRER 2 h plus tard. Remède écrit : « une garde ne se pose
**qu'après** un chiffrage écrit ; sinon elle attend le GO. »

CE QUI ÉTAIT FAIT AVANT : E9 restait une **promesse déclarée à dessein**. La raison
écrite était juste : un compteur « même fichier, même jour » crierait sur du travail
LÉGITIME (mesuré : `paper_diprip.py` a **5 actes le 22/09**, tous légitimes) et se
confondrait avec R17/`inventaire_seuils_fixes.py` (garde de E1).

POURQUOI CE N'EST PLUS UNE PROMESSE : la règle E9 n'interdit pas de toucher un fichier
deux fois le même jour — elle interdit de **POSER puis RENONCER le même jour sans ordre
écrit**. C'est la signature exacte du cas fondateur (22/09 : refroidissement posé puis
retiré, seul). Le discriminant n'est donc pas le NOMBRE d'actes mais :

  deux actes le même jour  ET  l'un des motifs RENONCE (RETIR/SUPPRIM/ANNUL/DÉSACTIV…)
  ET  aucun ordre écrit (« ORDRE » / « GO ») dans les motifs du jour ni dans une
      PRÉ-DÉCLARATION `predemodifier.py` du même jour portant un `go`.

Ce discriminant rend le gardien :
  - SILENCIEUX sur le travail légitime empilé (additif, sans renoncement) — le cas des
    5 actes du 22/09 ne crie plus ;
  - SILENCIEUX sur un renoncement ORDONNÉ (mesuré : `_rescel_20260922c` = « R17 APPLIQUÉE
    (22/09, ORDRE Christophe …). RETIRÉ : … » → l'ordre est écrit, c'est conforme) ;
  - BRUYANT uniquement sur le geste que E9 nomme : renier le même jour, seul.

PORTÉE (R14 : une règle nouvelle ne juge pas le passé) : la garde est ACTIVE À PARTIR DE
`ACTIF_DEPUIS`. Les actes antérieurs sont constatés (comptés, jamais reprochés).

Lecture seule. N'écrit que son rapport `thermo/empilement_jour.json`.
  python3 verif_empilement_jour.py            # rapport + rc 0 (conforme) / 3 (violation)
  python3 verif_empilement_jour.py --json F   # état machine
  python3 verif_empilement_jour.py --autotest # prouve que le gardien SAIT dire NON
"""
from __future__ import annotations

import argparse
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path

IM = Path(__file__).resolve().parent.parent                # Index_Maison
RACINE = IM.parent                                         # ace777-test-day1
REGISTRE = IM / "strategie" / "REGISTRE_SYNAPSES.json"
PREDEC = IM / "strategie" / "PREDECLARATIONS.jsonl"
OUT = IM / "thermo" / "empilement_jour.json"

# La règle juge ce qui vient : les actes antérieurs restent constatés, jamais reprochés (R14).
ACTIF_DEPUIS = "2026-10-09"

# Verbes de RENONCEMENT (la « pose » n'a pas besoin d'être détectée : c'est le retrait qui signe E9).
RE_RENONCE = re.compile(r"RETIR|SUPPRIM|ANNUL|D[EÉ]SACTIV|ABANDONN|REMIS|ENLEV|REVERT|REVIENT", re.I)
# Un ordre écrit rend le renoncement légitime (« sinon elle attend le GO »).
RE_ORDRE = re.compile(r"\bORDRE\b|\bGO\b", re.I)


def utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _jour_cle(k: str) -> str | None:
    m = re.search(r"_(\d{8})", k)
    if not m:
        return None
    s = m.group(1)
    return f"{s[:4]}-{s[4:6]}-{s[6:]}"


def _acts(it: dict) -> list[tuple[str, str]]:
    """Extrait (jour, motif) de chaque acte d'une entrée du registre des scellés.

    Deux formes coexistent : les clés DATÉES `_rescel_YYYYMMDD*` / `_ajout_YYYYMMDD*`
    (valeur = motif) et les listes append-only `_rescel` / `_ajout` (dicts {ts, motif})."""
    out: list[tuple[str, str]] = []
    for k, v in it.items():
        if not isinstance(k, str):
            continue
        if k.startswith("_rescel_") or k.startswith("_ajout_"):
            day = _jour_cle(k)
            if day:
                out.append((day, v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)))
        elif k in ("_rescel", "_ajout") and isinstance(v, list):
            for e in v:
                if isinstance(e, dict) and e.get("ts"):
                    out.append((str(e["ts"])[:10], str(e.get("motif") or "")))
    return out


def controler(fichiers: list, decs: list, actif_depuis: str = ACTIF_DEPUIS) -> dict:
    """Logique PURE (injectable) : renvoie {violations, observations, constates}.

    - violations  : renoncement le même jour, sans ordre écrit, DANS la fenêtre active.
    - constates   : actes antérieurs à l'activation (jamais reprochés — R14).
    - observations: renoncements le même jour AVEC ordre écrit (conformes, tracés)."""
    jours_go: dict[tuple[str, str], bool] = {}
    for d in decs or []:
        f, go, ts = d.get("fichier"), d.get("go"), (d.get("ts") or "")
        if f and go and ts:
            jours_go[(str(f), str(ts)[:10])] = True

    viol, obs, constat = [], [], 0
    for it in fichiers or []:
        nom = str(it.get("nom"))
        par_jour: dict[str, list[str]] = {}
        for day, motif in _acts(it):
            if not day:
                continue
            if day < actif_depuis:
                constat += 1
                continue
            par_jour.setdefault(day, []).append(motif)
        for day, motifs in sorted(par_jour.items()):
            if len(motifs) < 2:
                continue                       # un seul acte : rien n'est « empilé »
            if not any(RE_RENONCE.search(m or "") for m in motifs):
                continue                       # empilement ADDITIF : c'est du travail, pas un reniement
            ordre = (any(RE_ORDRE.search(m or "") for m in motifs)
                     or jours_go.get((nom, day), False))
            if ordre:
                obs.append(f"{nom} · {day} : renoncement le même jour AVEC ordre écrit (conforme)")
            else:
                viol.append({"fichier": nom, "jour": day,
                             "raison": "≥ 2 actes le même jour dont un RENONCEMENT, SANS ordre écrit "
                                       "(E9 : poser puis renier le même jour, seul)"})
    return {"violations": viol, "observations": obs, "constates": constat}


def _lire():
    fichiers = json.loads(REGISTRE.read_text(encoding="utf-8")).get("fichier", [])
    decs = []
    if PREDEC.exists():
        for l in PREDEC.read_text(encoding="utf-8").splitlines():
            l = l.strip()
            if not l:
                continue
            try:
                o = json.loads(l)
            except Exception:
                continue
            if o.get("fichier"):
                decs.append(o)
    return fichiers, decs


def rapport(fichiers, decs) -> dict:
    res = controler(fichiers, decs, ACTIF_DEPUIS)
    propre = not res["violations"]
    j = {"ts": utc(), "actif_depuis": ACTIF_DEPUIS, "verdict": "PROPRE" if propre else "VIOLATION",
         "n_violations": len(res["violations"]), "violations": res["violations"],
         "observations": res["observations"], "actes_avant_activation_constates": res["constates"],
         "n_fichiers_registre": len(fichiers)}
    return j


def autotest() -> int:
    """Prouve que le gardien SAIT dire NON — et qu'il ne crie PAS à tort (famille E23/R14)."""
    J = "2026-10-09"
    # 1) le cas fondateur : pose puis RENONCEMENT le même jour, SANS ordre → DOIT crier
    f_renonce = [{"nom": "x.py", "_rescel_20261009": "refroidissement posé",
                  "_rescel_20261009b": "RETIRÉ : refroidissement supprimé"}]
    r1 = controler(f_renonce, [], J)
    # 2) empilement ADDITIF le même jour (pas de renoncement) → SILENCIEUX (le cas « 5 actes du 22/09 »)
    f_additif = [{"nom": "y.py", "_rescel_20261009_a": "ajout 1",
                  "_rescel_20261009_b": "ajout 2", "_rescel_20261009_c": "ajout 3"}]
    r2 = controler(f_additif, [], J)
    # 3) renoncement le même jour AVEC ordre écrit dans le motif → SILENCIEUX (cas `_rescel_20260922c`)
    f_ordre = [{"nom": "z.py", "_rescel_20261009": "pose",
                "_rescel_20261009b": "RETIRÉ : (ORDRE Christophe « on regarde les chiffres »)"}]
    r3 = controler(f_ordre, [], J)
    # 4) renoncement à un JOUR DIFFÉRENT (pas le même jour) → SILENCIEUX
    f_autre_jour = [{"nom": "w.py", "_rescel_20261009": "pose",
                     "_rescel_20261010": "RETIRÉ : retiré le lendemain"}]
    r4 = controler(f_autre_jour, [], J)
    # 5) renoncement le même jour justifié par une PRÉ-DÉCLARATION avec `go` → SILENCIEUX
    r5 = controler([{"nom": "v.py", "_rescel_20261009": "pose",
                     "_rescel_20261009b": "RETIRÉ"}],
                   [{"fichier": "v.py", "ts": "2026-10-09T08:00:00Z", "go": "GO Christophe"}], J)
    # 6) rien dans la fenêtre (actes antérieurs) → SILENCIEUX et CONSTATÉ (R14)
    r6 = controler([{"nom": "u.py", "_rescel_20260922": "pose",
                     "_rescel_20260922c": "RETIRÉ : R17"}], [], J)
    cas = [
        ("renoncement le même jour SANS ordre → CITÉ", len(r1["violations"]) == 1),
        ("empilement additif le même jour → SILENCIEUX (pas de faux positif)", not r2["violations"]),
        ("renoncement le même jour AVEC ordre écrit → SILENCIEUX", not r3["violations"]),
        ("renoncement à un jour DIFFÉRENT → SILENCIEUX", not r4["violations"]),
        ("renoncement justifié par une pré-déclaration GO → SILENCIEUX", not r5["violations"]),
        ("actes AVANT activation : constatés, jamais reprochés (R14)",
         not r6["violations"] and r6["constates"] == 2),
    ]
    for nom, ok in cas:
        print(f"  {'[OK ]' if ok else '[KO ]'} {nom}")
    bon = all(ok for _, ok in cas)
    print(f"  → {'GARDIEN FIABLE' if bon else 'GARDIEN CASSÉ'}")
    return 0 if bon else 3


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", metavar="FICHIER")
    ap.add_argument("--autotest", action="store_true")
    a = ap.parse_args()
    if a.autotest:
        return autotest()
    fichiers, decs = _lire()
    j = rapport(fichiers, decs)
    dest = Path(a.json) if a.json else OUT
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(j, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"EMPILEMENT DU JOUR (E9) — actif depuis {j['actif_depuis']} · "
          f"{j['n_fichiers_registre']} scellés · {j['actes_avant_activation_constates']} acte(s) "
          f"antérieur(s) constaté(s)")
    if j["violations"]:
        print(f"  ❌ {j['n_violations']} VIOLATION(S) — renoncement le même jour sans ordre écrit :")
        for v in j["violations"]:
            print(f"     {v['fichier']} · {v['jour']} : {v['raison']}")
    else:
        print("  ✔ aucun renoncement le même jour sans ordre écrit dans la fenêtre active")
    for o in j["observations"]:
        print(f"  · {o}")
    print(f"  (état écrit : {dest})")
    return 3 if j["violations"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
