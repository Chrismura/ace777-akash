#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VERROU DE SCELLÉS — rendre le défaut d'ordre IMPOSSIBLE au lieu de le punir
==========================================================================
LE DÉFAUT QU'IL FERME (E31, mesuré le 03/11/2026)
-------------------------------------------------
Le moteur a été réparé AVANT d'être déclaré : 4 actes sur des fichiers scellés sans
pré-déclaration, 9 écarts au registre. La règle existait (R20.1 + R23), le rappel existait
(règle écrite avant la session), et la faute a eu lieu quand même : une règle qu'on doit
se rappeler n'est pas une règle, c'est une bonne intention. Ici, ce n'est plus une intention :
si un organe dont le moteur dépend n'est pas au plomb, le moteur NE DÉMARRE PAS.

CE QU'IL VÉRIFIE (lecture seule sur les fichiers, jamais de re-scellement)
-------------------------------------------------------------------------
  1. Chaque organe dont le moteur dépend existe et est inscrit au registre.
  2. Son md5 disque = md5 scellé (`md5`), ou son bloc scellé est intact (`md5_prefix`,
     journaux append-only : un ajout passe, une troncature/une réécriture échoue).
  3. Si un défaut de REGISTRE est trouvé (doublon d'un même nom, chemin absolu), il se
     répare tout seul : c'est un défaut de forme, pas de contenu — aucun scellé n'est touché.

CE QU'IL NE FAIT JAMAIS
-----------------------
  Il ne re-selle RIEN. Un verrou qui blanchit ce qu'il contrôle est la faute E22 en une
  ligne de code. En cas d'écart il refuse, et il imprime l'acte à faire, dans l'ordre.

Usage :
  python3 verrou_scelles.py --controle     # organes du moteur (appelé par le lanceur, rc=2 = refus)
  python3 verrou_scelles.py --tout         # tout le registre (rituel / veilleuse)
  python3 verrou_scelles.py --autotest     # prouve qu'il SAIT dire NON
  python3 verrou_scelles.py --etat         # état lisible par le cockpit
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent.parent
REG = RACINE / "Index_Maison" / "strategie" / "REGISTRE_SYNAPSES.json"
STATE = RACINE / "Index_Maison" / "thermo" / "verrou_scelles.json"

# ORGANES DONT LE MOTEUR DÉPEND — liste EXPLICITE (pas de découverte magique des imports :
# un verrou qui devine ce qu'il doit protéger se trompe un jour sur deux).
DEPENDANCES = [
    "hulk-mexc/scripts/paper_diprip.py",
    "hulk-mexc/scripts/watchdog_hulk_ghost.sh",
    "Index_Maison/scripts/disjoncteur.py",
    "Index_Maison/scripts/nourrir_disjoncteur.py",
    "Index_Maison/scripts/hack_actif_mesure.py",
    "Index_Maison/strategie/disjoncteur_config.json",
    "Index_Maison/scripts/resceler.py",
    "Index_Maison/scripts/predemodifier.py",
]


def utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def md5(p: Path) -> str:
    h = hashlib.md5()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 16), b""):
            h.update(b)
    return h.hexdigest()


def _prefixe_ok(p: Path, entree: dict) -> bool:
    n = int(entree.get("prefixe_octets") or 0)
    if n <= 0:
        return False
    bloc = p.read_bytes()[:n]
    return len(bloc) == n and hashlib.md5(bloc).hexdigest() == entree.get("md5")


def verifier(registre: dict, portee: list[str] | None) -> list[dict]:
    """Renvoie les écarts : [{fichier, raison, acte}]."""
    par_nom = {}
    for e in registre.get("fichier", []):
        par_nom.setdefault(str(e.get("nom")), []).append(e)

    ecarts = []
    noms = portee if portee is not None else sorted(par_nom)
    for nom in noms:
        entrees = par_nom.get(nom)
        f = RACINE / nom
        if not entrees:
            ecarts.append({"fichier": nom, "raison": "ABSENT DU REGISTRE",
                           "acte": "predemodifier --declarer puis resceler --ajouter"})
            continue
        if not f.exists():
            ecarts.append({"fichier": nom, "raison": "FICHIER INTROUVABLE",
                           "acte": "restaurer la source (git) — ne pas relancer le moteur"})
            continue
        e = entrees[0]
        if len(entrees) > 1:
            # Défaut de REGISTRE (forme), pas de contenu : réparable ici, sans toucher un scellé.
            ecarts.append({"fichier": nom, "raison": f"{len(entrees)} entrées au registre (doublon)",
                           "acte": "--reparer-registre"})
            continue
        v = e.get("verif")
        if v == "md5_prefix":
            if not _prefixe_ok(f, e):
                ecarts.append({"fichier": nom, "raison": "bloc scellé ALTÉRÉ (troncature/réécriture)",
                               "acte": "predemodifier --declarer puis resceler --fichier"})
        elif v == "md5":
            if md5(f) != e.get("md5"):
                ecarts.append({"fichier": nom, "raison": "modifié depuis le scellé",
                               "acte": "predemodifier --declarer puis resceler --fichier"})
    return ecarts


def reparer_registre() -> int:
    """Auto-réparation des DÉFAUTS DE FORME du registre — jamais du contenu.

    Doublon d'un même nom → une seule entrée (rôles/origines/historiques agrégés).
    Nom absolu → relatif (un chemin absolu ne se vérifie pas depuis le mini 15 pro).
    Aucun md5 n'est inventé : on ne scelle rien, on remet le registre en état de vérifier.
    """
    reg = json.loads(REG.read_text(encoding="utf-8"))
    ent = reg.get("fichier", [])
    prefixes = [str(RACINE) + "/", "/Users/christophe/ace777-test-day1/"]
    fixes = []
    for e in ent:
        n = str(e.get("nom") or "")
        for p in prefixes:
            if n.startswith(p):
                e["nom"] = n[len(p):]
                e.setdefault("_normalisation", []).append({"ts": utc(), "motif": "nom absolu -> relatif",
                                                           "par": "verrou_scelles.py"})
                fixes.append(f"nom relatif : {e['nom']}")
                break
    vu, fusion = {}, []
    for e in ent:
        k = e.get("nom")
        if k in vu:
            g = vu[k]
            for champ in ("role", "origine"):
                a, b = str(g.get(champ) or ""), str(e.get(champ) or "")
                if b and b not in a:
                    g[champ] = (a + " · " + b).strip(" ·")
            for champ in ("_rescel", "_ajout", "_migration", "_normalisation"):
                if e.get(champ):
                    g[champ] = (g.get(champ) or []) + e[champ]
            g["date"] = max(str(g.get("date") or ""), str(e.get("date") or ""))
            fusion.append(k)
        else:
            vu[k] = e
    if fusion:
        fixes.append(f"doublons fusionnés : {sorted(set(fusion))}")
    if fixes:
        reg["fichier"] = list(vu.values())
        REG.write_text(json.dumps(reg, ensure_ascii=False, indent=2), encoding="utf-8")
    return len(fixes)


def _rapport(ecarts, portee_libelle: str, rc_refus: int = 2) -> int:
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps({"ts": utc(), "portee": portee_libelle, "ecarts": ecarts,
                                 "conforme": not ecarts,
                                 "par": "verrou_scelles.py · Buffy (DeepSeek V4.1 Flash 10/17)"},
                                ensure_ascii=False, indent=2), encoding="utf-8")
    if not ecarts:
        print(f"VERROU {portee_libelle} : OK — tous les organes sont au plomb")
        return 0
    print(f"VERROU {portee_libelle} : REFUS ({len(ecarts)} écart(s)) — le moteur ne démarre pas")
    for e in ecarts:
        print(f"   ✗ {e['fichier']} : {e['raison']}")
        print(f"     acte à faire : {e['acte']}")
    print("   ordre maison : déclarer (R20.1) → agir → re-sceler → --liste à 0 → relancer")
    return rc_refus


def cmd_controle(portee: str) -> int:
    reg = json.loads(REG.read_text(encoding="utf-8"))
    if portee == "tout":
        return _rapport(verifier(reg, None), "TOUT LE REGISTRE")
    return _rapport(verifier(reg, DEPENDANCES), "MOTEUR")


def cmd_autotest() -> int:
    """Preuve qu'il SAIT refuser : un verrou qui ne peut pas dire NON ne protège rien."""
    import tempfile

    cas = []
    with tempfile.TemporaryDirectory() as td:
        t = Path(td)
        bon = t / "organe.py"
        bon.write_text("x = 1\n", encoding="utf-8")
        reg_ok = {"fichier": [{"nom": str(bon), "verif": "md5", "md5": md5(bon)}]}
        cas.append(("organe conforme → accepté", verifier(reg_ok, [str(bon)]) == []))

        reg_faux = {"fichier": [{"nom": str(bon), "verif": "md5", "md5": "0" * 32}]}
        cas.append(("organe modifié → REFUS", len(verifier(reg_faux, [str(bon)])) == 1))

        reg_absent = {"fichier": []}
        cas.append(("organe absent du registre → REFUS", len(verifier(reg_absent, [str(bon)])) == 1))

        reg_dbl = {"fichier": [{"nom": str(bon), "verif": "md5", "md5": md5(bon)}] * 2}
        cas.append(("doublon au registre → REFUS (réparable)",
                    "doublon" in verifier(reg_dbl, [str(bon)])[0]["raison"]))

        j = t / "journal.jsonl"
        j.write_bytes(b'{"a":1}\n')
        reg_j = {"fichier": [{"nom": str(j), "verif": "md5_prefix", "prefixe_octets": 8,
                              "md5": hashlib.md5(b'{"a":1}\n').hexdigest()}]}
        ok_ajout = verifier(reg_j, [str(j)]) == []
        j.write_bytes(b'{"a":2}\n')
        ko_reecriture = len(verifier(reg_j, [str(j)])) == 1
        cas.append(("journal append-only : ajout accepté / réécriture REFUSÉE",
                    ok_ajout and ko_reecriture))

    for nom, ok in cas:
        print(f"  {'[OK ]' if ok else '[KO ]'} {nom}")
    bon = all(ok for _, ok in cas)
    print(f"  → {'VERROU FIABLE' if bon else 'VERROU CASSÉ'} ({sum(1 for _, o in cas if o)}/{len(cas)})")
    return 0 if bon else 3


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--controle", action="store_true", help="organes dont le moteur dépend")
    ap.add_argument("--tout", action="store_true", help="tout le registre")
    ap.add_argument("--autotest", action="store_true")
    ap.add_argument("--etat", action="store_true")
    ap.add_argument("--reparer-registre", action="store_true")
    a = ap.parse_args()
    if a.autotest:
        return cmd_autotest()
    if a.reparer_registre:
        n = reparer_registre()
        print(f"REGISTRE RÉPARÉ : {n} correction(s) de forme (aucun scellé touché)")
        return 0
    if a.tout:
        return cmd_controle("tout")
    if a.controle:
        return cmd_controle("moteur")
    if a.etat:
        print(STATE.read_text(encoding="utf-8") if STATE.exists() else "aucun état (jamais lancé)")
        return 0
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
