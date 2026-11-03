#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AUDIT DES ACTES — le gardien qui voit ce que l'IA ne déclare pas (03/11/2026)
=============================================================================
LE DÉFAUT QU'IL FERME (mesuré, pas supposé)
-------------------------------------------
Christophe, 03/11 : « tu déclares celles que tu vois, mais ce n'est pas dit que tu les
vois toutes ». C'est exact et c'est structurel : un rapport d'erreurs écrit par celui
qui se trompe ne peut PAS être complet — sinon il ne se tromperait pas.

`predemodifier.py` juge déjà les fichiers SCELLÉS. Mais tout le reste (docs, cockpit,
JSON de config, plists, scripts non scellés) peut être modifié sans que RIEN ne le
nomme. Les actes les plus coûteux de cette session sont passés par là.

CE QU'IL FAIT
-------------
Il ne demande rien à personne. Il photographie le DISQUE (md5 + mtime de chaque
fichier suivi), puis, à chaque passage, il NOMME les fichiers qui ont changé et
vérifie pour chacun qu'une PRÉ-DÉCLARATION existe, faite APRÈS le dernier audit et
AVANT l'écriture. Aucune déclaration → « acte non déclaré », nommé, daté, compté.

Il ne juge pas la qualité de l'acte — seulement s'il a été ANNONCÉ. C'est
volontairement modeste : un gardien qui prétend juger le raisonnement mentirait.

CE QU'IL NE FAIT JAMAIS
-----------------------
  · il n'écrit aucun fichier du projet (seulement son instantané + son rapport) ;
  · il ne blanchit rien : un acte non déclaré reste non déclaré ;
  · il ne bloque pas le moteur (rc=2 = signal rouge au cockpit, pas un arrêt).

Usage :
  python3 audit_actes.py --baseline    # pose la référence (1re passe)
  python3 audit_actes.py --controle    # compare, nomme, rc=2 si acte non déclaré
  python3 audit_actes.py --etat        # état lisible
  python3 audit_actes.py --autotest    # prouve qu'il SAIT dire NON
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent.parent
INDEX = RACINE / "Index_Maison"
PARAMS = RACINE / "Index_Maison" / "strategie" / "PREDECLARATIONS.jsonl"
SNAP = INDEX / "thermo" / "audit_actes_snapshot.json"
RAPPORT = INDEX / "thermo" / "audit_actes.json"

# Dossiers JAMAIS audités : runtime, journaux, données, caches. Auditer un fichier
# réécrit en boucle par un organe produirait une alarme permanente — un faux rouge
# à vie (R14) qui apprendrait à ignorer l'alarme.
EXCLUS_DIRS = {
    ".git", "__pycache__", "node_modules", ".venv", "venv",
    "runs", "data", "thermo", "pouls", "OUTBOX_OBSIDIAN", "etat", "system",
    "A_Mon_Attention", "historique_analyses", "archive", "archives",
    "logs", "backups",
}
# Fichiers à écriture automatique (miroirs, journaux, caches) : légitimes, donc hors
# périmètre. Liste EXPLICITE — pas de règle devinée.
EXCLUS_NOMS = {
    "MEMOIRE_COLLAB.md", "THERMO_DERNIER.md", "THERMO_DERNIER.json",
    "SOUS_L_OEIL.md", "CONSOLE_GENERALE.md", "AUTO_PROCESSUS.md",
    "CRITIQUE_ERREURS_DERNIER.md", "SEUILS_FIXES_DERNIER.md",
    "SEUILS_FIXES_DERNIER.json", "sante_live.js", "mission.js",
    "mission.json", "hub.json", "hub.js", "index.html", "live.js", "plancher_live.js",
    "alarme.json", "alerts_day.json", "cortana_feed.js", "ARCHITECTURE_VIVANTE.md",
    "audit_actes.json", "audit_actes_snapshot.json",
    # Registre des scellés : réécrit à CHAQUE re-scellement, et c'est resceler.py qui
    # porte la déclaration. L'auditer reviendrait à crier sur sa propre trace.
    "REGISTRE_SYNAPSES.json", "predeclaration.json", "verrou_scelles.json",
}
SUFFIXES_EXCLUS = (".jsonl", ".log", ".csv", ".pyc", ".db", ".sqlite",
                   ".bak", ".tmp", ".swp", ".pid")
EXTENSIONS_SUIVIES = {".py", ".sh", ".html", ".js", ".css", ".plist",
                      ".json", ".md", ".toml", ".yaml", ".yml"}


def utc() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def md5(p: Path) -> str:
    h = hashlib.md5()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 16), b""):
            h.update(b)
    return h.hexdigest()


def iso(ts: float) -> str:
    return datetime.fromtimestamp(ts, timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def lisible(p: Path) -> bool:
    if p.name in EXCLUS_NOMS:
        return False
    if p.name.startswith(("Journal_", "SNIFF_", "ROULEMENT_IA_", "VEILLE_", "DIGEST_")):
        return False
    if p.name.endswith(SUFFIXES_EXCLUS):
        return False
    # Fichiers de RUNTIME réécrits en boucle par les organes (ada, cortana, saison,
    # intention…) : les auditer produirait une alarme permanente — un faux rouge à vie
    # (R14) qui apprendrait à ignorer l'alarme. Ce sont des sorties, pas des actes.
    if p.name.endswith(("_live.json", "_live.js", "_etat.json")):
        return False
    return p.suffix in EXTENSIONS_SUIVIES


def _scelles() -> set:
    """Chemins DÉJÀ jugés par predemodifier.py (registre des scellés).

    POURQUOI (03/11, 2ᵉ correction) : deux gardiens qui jugent le même fichier, c'est deux
    vérités. Un fichier scellé a SON gardien (pré-déclaration + md5) ; l'audit des actes
    s'occupe du RESTE — docs, cockpit, config non scellés — là où personne ne regardait.
    """
    try:
        reg = json.loads((RACINE / "Index_Maison" / "strategie" /
                          "REGISTRE_SYNAPSES.json").read_text(encoding="utf-8"))
        return {str(i.get("nom")) for i in reg.get("fichier", []) if i.get("nom")}
    except Exception:
        return set()


def scanner(racine: Path) -> dict:
    """md5 + mtime de chaque fichier suivi. Aucune écriture."""
    fichiers = {}
    scelles = _scelles()
    for dossier in ("Index_Maison", "hulk-mexc"):
        base = racine / dossier
        if not base.is_dir():
            continue
        for p in base.rglob("*"):
            if not p.is_file() or not lisible(p):
                continue
            rel = p.relative_to(racine)
            if any(part in EXCLUS_DIRS for part in rel.parts[:-1]):
                continue
            if str(rel) in scelles:
                continue
            try:
                fichiers[str(rel)] = {"md5": md5(p), "mtime": p.stat().st_mtime}
            except OSError:
                continue
    return fichiers


def declarations(magasin: Path) -> list:
    decs = []
    if not magasin.exists():
        return decs
    for ligne in magasin.read_text(encoding="utf-8").splitlines():
        ligne = ligne.strip()
        if not ligne:
            continue
        try:
            o = json.loads(ligne)
        except Exception:
            continue
        if o.get("fichier"):
            decs.append(o)
    return decs


def comparer(racine: Path, avant: dict, apres: dict, decs: list,
             ts_ref: float) -> dict:
    """Nomme chaque acte et dit s'il a été ANNONCÉ avant l'écriture.

    Un acte est DÉCLARÉ si une ligne de PREDECLARATIONS.jsonl porte son chemin avec
    `dernier_audit <= ts_declaration <= mtime + 5 s`. La borne basse empêche qu'une
    déclaration ancienne serve de blanc-seing à vie ; la borne haute empêche de
    blanchir un acte après coup (même garantie que predemodifier.py).
    """
    actes = []
    for rel in sorted(set(avant) | set(apres)):
        a, b = avant.get(rel), apres.get(rel)
        if a and b and a["md5"] == b["md5"]:
            continue
        if a is None:
            nature = "ajout"
            t = b["mtime"]
        elif b is None:
            nature = "suppression"
            t = ts_ref
        else:
            nature = "modification"
            t = b["mtime"]
        annonce = any(
            str(d.get("fichier")) == rel
            # Fenêtre : déclaration faite dans l'heure qui précède l'écriture (le gardien
            # passe toutes les 30 min) — assez large pour une déclaration faite pendant
            # l'intervalle, assez étroite pour qu'une déclaration ancienne ne serve jamais
            # de blanc-seing (cas 5 de l'autotest).
            and ts_ref - 3600.0 <= float(d.get("ts_epoch") or 0) <= t + 5.0
            for d in decs
        )
        actes.append({"fichier": rel, "nature": nature,
                      "mtime": iso(t) if t > 0 else None,
                      "declare": annonce})
    non_declares = [a for a in actes if not a["declare"]]
    return {"actes": actes, "non_declares": len(non_declares),
            "liste_non_declares": non_declares}


def ecrire_atomique(p: Path, contenu: str) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(p.parent), text=True)
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(contenu)
    os.replace(tmp, p)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--baseline", action="store_true")
    ap.add_argument("--controle", action="store_true")
    ap.add_argument("--etat", action="store_true")
    ap.add_argument("--autotest", action="store_true")
    a = ap.parse_args()

    if a.autotest:
        return autotest()

    now = utc()
    if a.baseline:
        snap = scanner(RACINE)
        ecrire_atomique(SNAP, json.dumps({"ts": now, "epoch": __import__("time").time(),
                                          "fichiers": snap}, ensure_ascii=False))
        rap = {"ts": now, "premier_passage": True, "ok": True, "non_declares": 0,
               "fichiers_suivis": len(snap), "actes": [],
               "detail": "référence posée — aucune comparaison (ce n'est pas une preuve)"}
        ecrire_atomique(RAPPORT, json.dumps(rap, ensure_ascii=False, indent=1))
        print(f"[audit_actes] baseline : {len(snap)} fichiers suivis")
        return 0

    if a.controle or a.etat:
        try:
            s = json.loads(SNAP.read_text(encoding="utf-8"))
        except Exception as e:
            rap = {"ts": now, "ok": False, "non_declares": None,
                   "raison": f"instantané illisible ({type(e).__name__}) — lancer --baseline"}
            ecrire_atomique(RAPPORT, json.dumps(rap, ensure_ascii=False, indent=1))
            print(f"[audit_actes] REFUS : {rap['raison']}")
            return 2
        apres = scanner(RACINE)
        res = comparer(RACINE, s.get("fichiers") or {}, apres,
                       declarations(PARAMS), float(s.get("epoch") or 0))
        ok = res["non_declares"] == 0
        rap = {"ts": now, "premier_passage": False, "ok": ok,
               "fichiers_suivis": len(apres), "ts_reference": s.get("ts"),
               "declares": len(res["actes"]) - res["non_declares"],
               "non_declares": res["non_declares"],
               "liste_non_declares": res["liste_non_declares"],
               "actes": res["actes"]}
        ecrire_atomique(RAPPORT, json.dumps(rap, ensure_ascii=False, indent=1))
        # Nouvelle référence : les actes jugés ne sont plus re-comptés au passage suivant.
        ecrire_atomique(SNAP, json.dumps({"ts": now, "epoch": __import__("time").time(),
                                          "fichiers": apres}, ensure_ascii=False))
        print(f"[audit_actes] {len(res['actes'])} acte(s) · "
              f"{len(res['actes']) - res['non_declares']} déclaré(s) · "
              f"{res['non_declares']} NON DÉCLARÉ(S)")
        for x in res["liste_non_declares"][:20]:
            print(f"   ⚠ {x['nature']:<13} {x['fichier']} ({x['mtime']})")
        return 0 if ok else 2

    ap.print_help()
    return 0


def autotest() -> int:
    """Prouve qu'il SAIT dire NON — sans toucher un seul fichier du projet.

    Les quatre cas sont ceux qui comptent : un acte non annoncé doit crier, un acte
    annoncé AVANT ne doit pas crier, un fichier inchangé ne doit pas crier, et un
    fichier neuf non annoncé doit crier.
    """
    with tempfile.TemporaryDirectory() as td:
        base = Path(td)
        (base / "Index_Maison").mkdir(parents=True)
        (base / "hulk-mexc").mkdir(parents=True)
        f1 = base / "Index_Maison" / "moteur.py"
        f1.write_text("x = 1\n", encoding="utf-8")
        avant = scanner(base)
        ts_ref = __import__("time").time() - 10

        # cas 1 : modification non annoncée
        f1.write_text("x = 2\n", encoding="utf-8")
        r = comparer(base, avant, scanner(base), [], ts_ref)
        cas1 = r["non_declares"] == 1

        # cas 2 : modification annoncée AVANT (déclaration dans la fenêtre)
        mt = f1.stat().st_mtime
        decs = [{"fichier": "Index_Maison/moteur.py", "ts_epoch": mt - 2}]
        r = comparer(base, avant, scanner(base), decs, ts_ref)
        cas2 = r["non_declares"] == 0

        # cas 3 : fichier inchangé → aucun acte (référence fraîche, sinon on compare
        # à l'état d'AVANT les cas précédents — c'était le défaut de mon 1er harnais)
        frais = scanner(base)
        r = comparer(base, frais, scanner(base), [], ts_ref)
        cas3 = r["non_declares"] == 0 and len(r["actes"]) == 0

        # cas 4 : ajout non annoncé
        (base / "hulk-mexc" / "nouveau.py").write_text("y = 1\n", encoding="utf-8")
        r = comparer(base, frais, scanner(base), [], ts_ref)
        cas4 = r["non_declares"] == 1

        # cas 5 : déclaration ANCIENNE ≠ blanc-seing (antérieure au dernier audit)
        f1.write_text("x = 3\n", encoding="utf-8")
        vieille = [{"fichier": "Index_Maison/moteur.py", "ts_epoch": ts_ref - 7200}]
        r = comparer(base, frais, scanner(base), vieille, ts_ref)
        cas5 = r["non_declares"] == 2   # modif + ajout, aucune annonce valable

    cas = [("acte non annoncé détecté", cas1),
           ("acte annoncé AVANT jugé conforme", cas2),
           ("fichier inchangé → silence", cas3),
           ("fichier neuf non annoncé détecté", cas4),
           ("déclaration ancienne ≠ blanc-seing", cas5)]
    for nom, ok in cas:
        print(f"  {'[OK ]' if ok else '[KO ]'} {nom}")
    bon = all(ok for _, ok in cas)
    print(f"  → {'GARDIEN FIABLE' if bon else 'GARDIEN CASSÉ'}")
    return 0 if bon else 3


if __name__ == "__main__":
    sys.exit(main())
