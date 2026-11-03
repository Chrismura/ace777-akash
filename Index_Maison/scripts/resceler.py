#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RESCELER — OUTIL GÉNÉRIQUE DE RE-SCELLEMENT (remplace les outils « par vague » du 23/09)
========================================================================================
RÈGLE D'OR #5 : un scellé ne s'écrase JAMAIS en silence. Deux actes seulement, tous deux
DÉCLARÉS (backup du registre + texte de déclaration) :

  --fichier CHEMIN --motif "…"   re-déclare un fichier scellé MODIFIÉ (nouveau md5)
  --ajouter CHEMIN --role "…" --origine "…"   inscrit un instrument NEUF au registre
  --liste                        liste les écarts du registre (lecture seule, rc=1 si écart)

SE SÉPARE VOLONTAIREMENT DU GARDIEN (`predemodifier.py`) : R9 — un gardien ne modifie pas ce
qu'il surveille. Ici on ÉCRIT le registre ; là-bas on le LIT et on crie. Jamais les deux dans
le même fichier.

Pourquoi cet outil remplace `declarer_rescel_20260923.py` et `declarer_rescel_20260923b.py` :
la famille (tour 5) a jugé le processus, pas l'acte — un outil qui n'accepte QUE les fichiers
déjà connus oblige à écrire un nouvel outil à chaque vague (dette, et 3 outils pour 3 actes).
Celui-ci est générique et **append-only côté déclaration** : chaque re-scellement laisse son
motif écrit, sans jamais effacer les précédents.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import time
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent.parent
REG = RACINE / "Index_Maison" / "strategie" / "REGISTRE_SYNAPSES.json"
JOURNAL_ECRIVAINS = RACINE / "Index_Maison" / "strategie" / "JOURNAL_ECRIVAINS.jsonl"


def _ecrivain() -> dict:
    """R22 (24/10/2026, ORDRE Christophe) : QUI touche QUOI — identité de l'écrivain
    à chaque re-scellement. L'IA se déclare via $CODEBUFF_IA ou la dernière ligne de
    DECLARATIONS_IA.jsonl ; le shell donne user + pid + chaîne des parents."""
    qui = os.environ.get("CODEBUFF_IA", "").strip()
    if not qui:
        try:
            _decl = RACINE / "Index_Maison" / "strategie" / "DECLARATIONS_IA.jsonl"
            _lignes = [l for l in _decl.read_text(encoding="utf-8").splitlines() if l.strip()]
            if _lignes:
                _d = json.loads(_lignes[-1])
                qui = "%s (%s, %s)" % (_d.get("ia", "?"), _d.get("modele", "?"),
                                        _d.get("client", "?"))
        except Exception:
            pass
    if not qui:
        qui = "non-declare"
    try:
        import subprocess as _sp
        _ppid = os.getppid()
        _chaine = ["pid %s" % os.getpid()]
        for _ in range(3):
            _out = _sp.run(["ps", "-o", "comm=", "-o", "ppid=", "-p", str(_ppid)],
                           capture_output=True, text=True, timeout=5)
            _parts = _out.stdout.strip().split()
            if not _parts:
                break
            _chaine.append("%s(pid %s)" % (_parts[0], _ppid))
            _ppid = int(_parts[1])
    except Exception:
        _chaine = ["pid %s" % os.getpid()]
    return {"ts": utc(), "ia": qui, "user": os.environ.get("USER", "?"),
            "chaine": " <- ".join(_chaine)}


def utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def md5(p: Path) -> str:
    h = hashlib.md5()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 16), b""):
            h.update(b)
    return h.hexdigest()


def _charge():
    reg = json.loads(REG.read_text(encoding="utf-8"))
    bak = REG.with_name(REG.name + ".bak_resceler_%s" % time.strftime("%H%M%S"))
    shutil.copy2(REG, bak)
    return reg, bak


def _ecrit(reg) -> None:
    reg["updated"] = utc()
    tmp = REG.with_suffix(".json.tmp")
    json.dump(reg, open(tmp, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    os.replace(tmp, REG)


def cmd_liste() -> int:
    reg = json.loads(REG.read_text(encoding="utf-8"))
    ecarts, absents = [], []
    for it in reg.get("fichier", []):
        nom = str(it.get("nom"))
        p = RACINE / nom
        if not p.exists():
            absents.append(nom)
        elif it.get("verif") == "md5" and md5(p) != it.get("md5"):
            ecarts.append(nom)
        elif it.get("verif") == "md5_prefix":
            # Journal APPEND-ONLY (JOURNAL_ECRIVAINS) : chaque sceau y ajoute une ligne.
            # Le hasher en entier fabrique un ecart PERPETUEL par construction — un faux
            # rouge a vie (R14) qui apprend a ignorer l'alarme. Controle juste : le bloc
            # scelle (N premiers octets) doit etre INTACT. Un ajout passe ; une
            # troncature ou une reecriture echoue.
            _n = int(it.get("prefixe_octets") or 0)
            if _n <= 0:
                absents.append(nom + " (prefixe_octets absent)")
            else:
                import hashlib as _H
                _bloc = p.read_bytes()[: _n]
                if len(_bloc) < _n or _H.md5(_bloc).hexdigest() != it.get("md5"):
                    ecarts.append(nom)
    print(f"REGISTRE : {len(reg.get('fichier', []))} entrées")
    print(f"  écarts  : {len(ecarts)}" + (f" → {ecarts}" if ecarts else " ✔"))
    print(f"  absents : {len(absents)}" + (f" → {absents}" if absents else " ✔"))
    return 0 if not ecarts and not absents else 1


def cmd_fichier(nom: str, motif: str) -> int:
    cible = RACINE / nom
    if not cible.exists():
        print(f"REFUS : {nom} n'existe pas")
        return 2
    if not motif:
        print("REFUS : --motif obligatoire (un re-scellement sans motif est un effacement de contrôle)")
        return 2
    reg, bak = _charge()
    actuel = md5(cible)
    # R20.1-fix 03/11 (GO A Christophe) : le registre a pu accumuler PLUSIEURS entrees
    # pour un meme fichier (deux epoques, deux roles). L'ancienne boucle s'arretait a
    # la 1re : le doublon restait en ECART PERPETUEL — un faux rouge a vie (R14), qui
    # apprend a ignorer l'alarme. On realigne TOUTES les entrees portant ce nom.
    entrees = [it for it in reg.get("fichier", []) if str(it.get("nom")) == nom]
    if not entrees:
        print(f"[ABSENT DU REGISTRE] {nom} — utiliser --ajouter")
        return 3
    if entrees[0].get("verif") == "md5_prefix":
        print(f"[=] {nom} : journal append-only, sceau de prefixe — rien a re-sceler "
              f"(le sceau suit le contenu, pas la longueur)")
        return 0
    avant = entrees[0].get("md5")
    if all(it.get("md5") == actuel for it in entrees):
        print(f"[=] {nom} deja conforme" + (f" ({len(entrees)} entrees)" if len(entrees) > 1 else ""))
        return 0
    _w = _ecrivain()
    try:
        with open(JOURNAL_ECRIVAINS, "a", encoding="utf-8") as _j:
            _j.write(json.dumps({"fichier": nom, "acte": "rescel",
                                 "motif": motif, "entrees_maj": len(entrees), **_w},
                                ensure_ascii=False) + "\n")
    except Exception as _e:
        print(f"WARN journal ecrivains : {_e}")
    # R22-fix : le log ci-dessus modifie le journal lui-meme — le md5 scelle
    # est donc recalcule APRES l'ecriture, jamais avant.
    actuel = md5(cible)
    for it in entrees:
        it["md5"] = actuel
        it["date"] = utc()
        it["_rescel"] = it.get("_rescel", [])
        it["_rescel"].append({"ts": utc(), "motif": motif, "ecrivain": _w})
        it["dernier_ecrivain"] = _w
    _ecrit(reg)
    print(f"backup : {bak.name}")
    if len(entrees) > 1:
        print(f"NOTE : {len(entrees)} entrees pour {nom} — toutes realignees ; fusion a faire a la main (GO)")
    print(f"[OK] {nom}\n     {avant} -> {actuel}\n     motif : {motif}")
    return 0


def cmd_ajouter(nom: str, role: str, origine: str) -> int:
    cible = RACINE / nom
    if not cible.exists():
        print(f"REFUS : {nom} n'existe pas")
        return 2
    reg, bak = _charge()
    if any(str(i.get("nom")) == nom for i in reg.get("fichier", [])):
        print(f"[=] déjà au registre : {nom}")
        return 0
    _w = _ecrivain()
    try:
        with open(JOURNAL_ECRIVAINS, "a", encoding="utf-8") as _j:
            _j.write(json.dumps({"fichier": nom, "acte": "ajout", "role": role,
                                 "origine": origine, **_w}, ensure_ascii=False) + "\n")
    except Exception as _e:
        print(f"WARN journal écrivains : {_e}")
    reg["fichier"].append({"nom": nom, "role": role or "instrument", "origine": origine or "",
                           "verif": "md5", "auto_modifiable": False, "md5": md5(cible),
                           "date": utc(), "dernier_ecrivain": _w,
                           "_ajout": [{"ts": utc(), "motif": "inscription au registre (R15 : "
                                                              "ce qui n'est pas déclaré n'existe pas)"}]})
    _ecrit(reg)
    print(f"backup : {bak.name}")
    print(f"[+] AJOUTÉ : {nom} ({len(reg['fichier'])} entrées)")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--liste", action="store_true")
    ap.add_argument("--fichier", metavar="CHEMIN")
    ap.add_argument("--motif", default="")
    ap.add_argument("--ajouter", metavar="CHEMIN")
    ap.add_argument("--role", default="")
    ap.add_argument("--origine", default="")
    a = ap.parse_args()
    if a.liste:
        return cmd_liste()
    if a.fichier:
        return cmd_fichier(a.fichier, a.motif)
    if a.ajouter:
        return cmd_ajouter(a.ajouter, a.role, a.origine)
    ap.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
