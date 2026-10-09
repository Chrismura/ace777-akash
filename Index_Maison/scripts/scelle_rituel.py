#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""scelle_rituel.py — LE RITUEL DE SCELLEMENT EN UN APPEL (R20.1 + re-scellement)
====================================================================================

POURQUOI CE MODULE EXISTE (mesuré le 09/10/2026, GO Christophe « go 1,2 »)
-------------------------------------------------------------------------
`MEMOIRE_COLLAB.md` est écrit AUTOMATIQUEMENT (`memoire_log.py`, `auto_reparer.py`).
Il a été inscrit au registre des scellés en mode `vivant`. Pour le durcir en `md5`,
chaque écriture doit faire le RITUEL COMPLET — et voici ce que la MESURE impose
(lu dans le code, pas supposé) :

  1. `veilleuse_synapses.py` HONORE les pré-déclarations (`_predeclare`) : une modif
     annoncée AVANT passe hors alarme → l'état reste STABLE.
  2. `drill_restauration.py` NE LES HONORE PAS : `etape_scelles()` compare le md5 SANS
     regarder les pré-déclarations. Toute écriture non re-scellée = **écart → TROU** →
     R6/R12 rouges.

DONC : pré-déclarer ne suffit pas. Il faut **pré-déclarer → écrire → re-scellér**, dans
cet ordre, à CHAQUE écriture. Ce module fait exactement ça, en un appel.

GARANTIES (ce que le module PROMET, et ce qu'il ne promet pas)
-------------------------------------------------------------
- **Idempotent** : si le fichier n'est pas scellé `md5`, aucune cérémonie — simple écriture.
- **Non bloquant** : l'écriture a TOUJOURS lieu. Une trace perdue serait pire qu'un rouge ;
  le rapport dit ce qui a échoué, il ne lève pas.
- **Sérialisé** : un verrou (`flock`) couvre pré-déclaration → écriture → re-scellement,
  car DEUX écrivains automatiques peuvent se croiser sur le même registre.
- Il ne touche PAS au moteur. Il n'écrit que `PREDECLARATIONS.jsonl` (via `predemodifier`)
  et le registre (via `resceler`) — jamais le fichier lui-même : c'est l'appelant qui écrit.

R9 respecté : ce module APPELLE les deux outils, il ne réimplémente ni le gardien
(`predemodifier.py` qui lit et crie) ni l'écrivain du registre (`resceler.py`).
"""
from __future__ import annotations

import argparse
import importlib.util
import io
import json
import sys
import time
from contextlib import redirect_stdout
from pathlib import Path

# ── Racine et chemins (surchargeables pour l'autotest hermétique) ─────────────
RACINE = Path(__file__).resolve().parent.parent.parent          # ace777-test-day1
_REG_NOM = "Index_Maison/strategie/REGISTRE_SYNAPSES.json"
_STORE_NOM = "Index_Maison/strategie/PREDECLARATIONS.jsonl"
_LOCK_SUFFIX = ".lock"

SCRIPTS = Path(__file__).resolve().parent

# Motif par défaut si l'appelant n'en donne pas (toujours : qui écrit et pourquoi c'est permis).
MOTIF_DEFAUT = ("écriture automatique d'un fichier scellé — pré-déclaration PROGRAMMÉE "
                "AVANT l'acte (rituel scelle_rituel.py)")


def _reg_path() -> Path:
    return RACINE / _REG_NOM


def _store_path() -> Path:
    return RACINE / _STORE_NOM


def _charger(nom_fichier: str, alias: str):
    """Charge un module voisin par CHEMIN et le recale sur NOTRE racine.

    Le recalage est ce qui rend l'autotest hermétique : on peut pointer une arborescence
    temporaire sans jamais toucher le vrai registre.
    """
    chemin = SCRIPTS / nom_fichier
    spec = importlib.util.spec_from_file_location(alias, chemin)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    # recale les constantes de chemin des outils (ils les calculent depuis leur __file__)
    if hasattr(module, "RACINE"):
        module.RACINE = RACINE
    if hasattr(module, "REG"):
        module.REG = _reg_path()
    if hasattr(module, "STORE"):
        module.STORE = _store_path()
    if hasattr(module, "STATE"):
        module.STATE = RACINE / "Index_Maison/thermo/predeclaration.json"
    return module


def _predemodifier():
    return _charger("predemodifier.py", "_sr_predemodifier")


def _resceler():
    return _charger("resceler.py", "_sr_resceler")


# ── Lecture du registre ──────────────────────────────────────────────────────
def entree(nom: str):
    """Retourne l'entrée de registre du fichier `nom` (chemin relatif à la racine), ou None."""
    try:
        reg = json.loads(_reg_path().read_text(encoding="utf-8"))
    except Exception:
        return None
    for e in reg.get("fichier", []):
        if str(e.get("nom")) == nom:
            return e
    return None


def scelle_md5(nom: str) -> bool:
    """Vrai si le fichier est inscrit au registre ET vérifié par md5."""
    e = entree(nom)
    return bool(e and e.get("verif") == "md5")


# ── Les deux moitiés du rituel ───────────────────────────────────────────────
def predeclarer(nom: str, motif: str, go: str = "") -> int:
    """R20.1 — annonce l'acte AVANT de le commettre. Retourne le code de sortie de l'outil."""
    try:
        m = _predemodifier()
        with redirect_stdout(io.StringIO()):
            return int(m.cmd_declarer(nom, motif, go))
    except Exception:
        return -1


def resceler(nom: str, motif: str) -> int:
    """Re-scellé — le md5 du registre SUIT le fichier. Retourne le code de sortie de l'outil."""
    try:
        m = _resceler()
        with redirect_stdout(io.StringIO()):
            return int(m.cmd_fichier(nom, motif))
    except Exception:
        return -1


# ── Le rituel complet ────────────────────────────────────────────────────────
def _verrou(chemin: Path):
    """Verrou consultatif best-effort (POSIX). Rend un descripteur, ou None si indisponible.

    On ne bloque JAMAIS une trace pour un verrou : en cas d'échec on continue sans verrou
    (le pire cas est la course préexistante entre deux appends, pas une trace perdue).
    """
    try:
        import fcntl
        fd = open(str(chemin) + _LOCK_SUFFIX, "a+")
        for _ in range(30):                     # ~3 s max
            try:
                fcntl.flock(fd.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                return fd
            except OSError:
                time.sleep(0.1)
        fd.close()
        return None
    except Exception:
        return None


def _deverrou(fd):
    try:
        if fd:
            import fcntl
            fcntl.flock(fd.fileno(), fcntl.LOCK_UN)
            fd.close()
    except Exception:
        pass


def ecrire_sous_scelle(nom: str, ecrire, motif: str = "", go: str = "") -> dict:
    """Le RITUEL : pré-déclarer → écrire → re-scellér. L'écriture a TOUJOURS lieu.

    `nom`    : chemin du fichier relatif à la racine (clé du registre)
    `ecrire` : callable sans argument qui effectivement écrit le fichier
    Retour   : rapport lisible (jamais une exception) — l'appelant peut le journaliser.
    """
    motif = motif or MOTIF_DEFAUT
    rap = {"fichier": nom, "scelle_md5": scelle_md5(nom),
           "predeclare": None, "ecrit": False, "rescel": None, "erreur": None}
    fd = _verrou(_reg_path())
    try:
        if rap["scelle_md5"]:
            rap["predeclare"] = predeclarer(nom, motif, go)
        try:
            ecrire()
            rap["ecrit"] = True
        except Exception as e:                  # l'échec d'écriture est rapporté, pas maquillé
            rap["erreur"] = repr(e)
        if rap["scelle_md5"] and rap["ecrit"]:
            rap["rescel"] = resceler(nom, motif)
    finally:
        _deverrou(fd)
    return rap


# ── CLI (état + autotest) ────────────────────────────────────────────────────
def cmd_etat(nom: str) -> int:
    e = entree(nom)
    if not e:
        print(f"{nom} : PAS AU REGISTRE")
        return 1
    print(f"{nom}")
    print(f"  verif={e.get('verif')}  md5={e.get('md5')!r}")
    print(f"  role={str(e.get('role'))[:90]}")
    return 0


def _autotest() -> int:
    """Autotest HERMÉTIQUE : tout se joue dans un répertoire temporaire, jamais le vrai
    registre, jamais la vraie mémoire."""
    import shutil
    import tempfile

    global RACINE
    ok = 0
    total = 0
    vrai_racine = RACINE
    tmp = Path(tempfile.mkdtemp(prefix="scelle_rituel_test_"))
    try:
        (tmp / "Index_Maison/strategie").mkdir(parents=True)
        (tmp / "Index_Maison/thermo").mkdir(parents=True)
        (tmp / "Index_Maison/scripts").mkdir(parents=True)
        # l'autotest a besoin des outils voisins sous la racine temporaire
        for f in ("predemodifier.py", "resceler.py"):
            shutil.copy2(SCRIPTS / f, tmp / "Index_Maison/scripts" / f)
        registre = tmp / _REG_NOM
        registre.write_text(json.dumps({"version": "test", "updated": "", "fichier": []},
                                       ensure_ascii=False), encoding="utf-8")
        cible_rel = "Index_Maison/MEM.md"
        cible = tmp / cible_rel
        cible.write_text("ligne 0\n", encoding="utf-8")

        # Les outils sont chargés depuis la racine TEMPORAIRE : on repointe SCRIPTS.
        import scelle_rituel as _self
        old_scripts = _self.SCRIPTS
        _self.SCRIPTS = tmp / "Index_Maison/scripts"
        _self.RACINE = tmp
        RACINE = tmp
        try:
            # 1) fichier non inscrit → scelle_md5 = False
            total += 1
            if _self.scelle_md5(cible_rel) is False:
                ok += 1
            print("[1] non inscrit → scelle_md5=False ................", "OK" if ok == total else "KO")

            # 2) écriture sans scellé → écrit, aucune cérémonie
            total += 1
            r = _self.ecrire_sous_scelle(cible_rel, lambda: cible.write_text(
                cible.read_text(encoding="utf-8") + "ligne 1\n", encoding="utf-8"))
            bon = (r["ecrit"] and r["predeclare"] is None and r["rescel"] is None
                   and "ligne 1" in cible.read_text(encoding="utf-8"))
            ok += 1 if bon else 0
            print("[2] non scellé → écriture nue, sans cérémonie .....", "OK" if bon else "KO")

            # on scelle le fichier (md5) pour la suite
            reg = json.loads(registre.read_text(encoding="utf-8"))
            import hashlib
            _md5 = lambda p: hashlib.md5(p.read_bytes()).hexdigest()
            reg["fichier"].append({"nom": cible_rel, "role": "test", "origine": "autotest",
                                   "verif": "md5", "auto_modifiable": False, "md5": _md5(cible)})
            registre.write_text(json.dumps(reg, ensure_ascii=False), encoding="utf-8")

            # 3) écriture SOUS scellé → rituel complet + registre à jour
            total += 1
            avant_md5 = _md5(cible)
            r = _self.ecrire_sous_scelle(cible_rel, lambda: cible.write_text(
                cible.read_text(encoding="utf-8") + "ligne 2\n", encoding="utf-8"),
                motif="autotest cas 3")
            reg2 = json.loads(registre.read_text(encoding="utf-8"))
            e2 = [x for x in reg2["fichier"] if x["nom"] == cible_rel][0]
            decl = [json.loads(l) for l in _self._store_path().read_text(encoding="utf-8").splitlines()
                    if l.strip() and not json.loads(l).get("_meta")]
            bon = (r["predeclare"] == 0 and r["rescel"] == 0
                   and e2["md5"] == _md5(cible)          # le registre SUIT le fichier
                   and any(d.get("md5_avant") == avant_md5 for d in decl))  # déclaré CONTRE le scellé
            ok += 1 if bon else 0
            print("[3] scellé → rituel complet + registre à jour .....", "OK" if bon else "KO")

            # 4) deuxième écriture → toujours cohérent (idempotence du rituel)
            total += 1
            r = _self.ecrire_sous_scelle(cible_rel, lambda: cible.write_text(
                cible.read_text(encoding="utf-8") + "ligne 3\n", encoding="utf-8"),
                motif="autotest cas 4")
            reg3 = json.loads(registre.read_text(encoding="utf-8"))
            e3 = [x for x in reg3["fichier"] if x["nom"] == cible_rel][0]
            bon = (r["predeclare"] == 0 and r["rescel"] == 0 and e3["md5"] == _md5(cible))
            ok += 1 if bon else 0
            print("[4] 2e écriture → cohérence maintenue ..............", "OK" if bon else "KO")

            # 5) écriture qui ÉCHOUE → rapportée, registre pas re-scellé à tort
            total += 1
            md5_avant_echec = _md5(cible)

            def _boom():
                raise OSError("écriture simulée en panne")

            r = _self.ecrire_sous_scelle(cible_rel, _boom, motif="autotest cas 5")
            reg4 = json.loads(registre.read_text(encoding="utf-8"))
            e4 = [x for x in reg4["fichier"] if x["nom"] == cible_rel][0]
            bon = (r["erreur"] and not r["ecrit"] and r["rescel"] is None
                   and _md5(cible) == md5_avant_echec and e4["md5"] == md5_avant_echec)
            ok += 1 if bon else 0
            print("[5] écriture en panne → rapportée, pas de faux scellé ", "OK" if bon else "KO")
        finally:
            _self.SCRIPTS = old_scripts
            _self.RACINE = vrai_racine
            RACINE = vrai_racine
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    print(f"\nAUTOTEST scelle_rituel : {ok}/{total}")
    return 0 if ok == total else 1


def main() -> int:
    ap = argparse.ArgumentParser(description="Rituel de scellement (pré-déclarer → écrire → re-scellér)")
    ap.add_argument("--etat", metavar="NOM", help="état de scellé d'un fichier du registre")
    ap.add_argument("--autotest", action="store_true")
    a = ap.parse_args()
    if a.autotest:
        return _autotest()
    if a.etat:
        return cmd_etat(a.etat)
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
