#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GARDE-FOU DE SCHEMA DU JOURNAL — classe E15 (23/09/2026)
=========================================================
POURQUOI IL EXISTE
------------------
Christophe : « vérifier les données qu'on mémorise, si il en manque si elles sont
correctement enregistrées. » Ce contrôle devait exister AVANT la faute, pas après :

  Défaut trouvé le 23/09 à 13:00 (heure locale) sur le journal EN COURS d'écriture :
      en-tête  = 11 colonnes   (recopié de l'ancien fichier par le RESUME)
      lignes   = 16 colonnes   (les 5 colonnes ajoutées le jour même)
      mesuré   : 76 163 lignes à 11 champs · 12 lignes à 16 champs · 1 en-tête à 11.

Un fichier de données ne doit pas s'écrire en DEUX largeurs : tout lecteur qui prend
l'en-tête pour la vérité (csv.DictReader) voit 5 colonnes sans nom, et 5 colonnes
nommées qui n'existent pas dans les vieilles lignes. C'est silencieux, donc c'est grave.

CE QU'IL VÉRIFIE (lecture seule, n'écrit RIEN)
----------------------------------------------
  R1  chaque journal PAPER_V1_*.csv : en-tête de largeur == schéma courant (CSV_SCHEMA)
  R2  aucune ligne PLUS LARGE que l'en-tête (ligne large = donnée orpheline)
  R3  le journal le PLUS RÉCENT (celui du moteur vivant) est valide — c'est le seul
      que les autres outils lisent en ce moment
  R4  autotest : le contrôle DOIT savoir échouer (fichiers synthétiques : bon, en-tête
      court, ligne large, ligne vide finale). Un gardien qui ne sait pas échouer n'en
      est pas un (classe E10 de la maison).
Usage : python3 verif_schema_journal.py [--json runs/VERIF_SCHEMA_JOURNAL.json]
Sortie : rc=0 si conforme (les écarts HISTORIQUES sont signalés sans casser le rc,
         comme le fait déjà la maison pour les vieux fichiers), rc=1 si le journal
         COURANT est invalide.
"""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent      # hulk-mexc/
RUNS = RACINE / "runs"

# Le schéma courant est LU à la source (paper_diprip.CSV_SCHEMA), jamais recopié ici :
# une copie divergerait le jour où l'on ajoute une colonne (c'est exactement E15).
def charger_schema() -> list[str]:
    """Lit le schéma DANS la source. Les commentaires sont retirés AVANT d'extraire les
    chaînes — sinon on ramasse le bruit des commentaires (mesuré : « asp », « profil »
    comptés comme colonnes → 18 au lieu de 16). Un contrôle qui lit mal la source se
    condamne lui-même (E10)."""
    src = (RACINE / "scripts" / "paper_diprip.py").read_text(encoding="utf-8")
    m = re.search(r"^CSV_SCHEMA\s*=\s*\[(.*?)^\]", src, flags=re.S | re.M)
    if not m:
        raise SystemExit("SCHEMA_INTROUVABLE : paper_diprip.CSV_SCHEMA introuvable")
    corps = "\n".join(l.split("#")[0] for l in m.group(1).splitlines())
    cols = re.findall(r'"([^"]+)"', corps)
    if not cols:
        raise SystemExit("SCHEMA_VIDE : aucune colonne extraite")
    return cols


def largeurs(path: Path) -> tuple[int, dict[int, int], int]:
    """(largeur en-tête, {largeur: nb lignes}, nb lignes vides finales/parasites)."""
    with path.open(newline="", encoding="utf-8", errors="replace") as f:
        lignes = list(csv.reader(f))
    if not lignes:
        return 0, {}, 0
    entete = len(lignes[0])
    corps = lignes[1:]
    vides = sum(1 for r in corps if len(r) == 0)
    dist: dict[int, int] = {}
    for r in corps:
        if len(r):
            dist[len(r)] = dist.get(len(r), 0) + 1
    return entete, dist, vides


def autotest(schema: list[str]) -> list[tuple[str, bool, str]]:
    """Le contrôle SAIT-IL échouer ? Fichiers synthétiques, aucun fichier réel touché."""
    res = []
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "T.csv"
        bon = schema
        court = schema[:11]
        large = schema + ["extra"]

        def ecrire(entete: list[str], lignes: list[list[str]]):
            with p.open("w", newline="", encoding="utf-8") as f:
                w = csv.writer(f)
                w.writerow(entete)
                for l in lignes:
                    w.writerow(l)

        ecrire(bon, [["a"] * len(bon)])
        e, dist, _ = largeurs(p)
        res.append(("fichier conforme", e == len(schema) and set(dist) == {len(schema)},
                    f"en-tête {e}, largeurs {dist}"))

        ecrire(court, [["a"] * len(court)] * 7)
        e, dist, _ = largeurs(p)
        res.append(("en-tête COURT (ancien schéma) reconnu COHÉRENT", e == 11 and max(dist) == 11,
                    f"en-tête {e}, largeurs {dist} → 11/11 cohérent, non fautif"))

        ecrire(bon, [["a"] * len(bon)] * 6 + [["a"] * len(large)])
        e, dist, _ = largeurs(p)
        res.append(("ligne LARGE (incohérence) détectée", max(dist) > e,
                    f"en-tête {e}, max ligne {max(dist)}"))

        ecrire(bon, [["a"] * len(bon)] * 4)
        with p.open("a", encoding="utf-8") as f:
            f.write("\n")
        e, dist, vides = largeurs(p)
        res.append(("ligne vide finale tolérée", e == len(schema) and vides == 1,
                    f"en-tête {e}, {vides} ligne(s) vide(s)"))
    return res


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", default=None)
    ap.add_argument("--tous", action="store_true",
                    help="examiner TOUS les journaux (défaut : les 20 plus récents)")
    args = ap.parse_args()

    schema = charger_schema()
    jsons = sorted(RUNS.glob("PAPER_V1_*.csv"), key=lambda p: p.stat().st_mtime, reverse=True)
    cibles = jsons if args.tous else jsons[:20]

    res_auto = autotest(schema)
    auto_ok = all(ok for _, ok, _ in res_auto)
    print(f"SCHEMA COURANT ({len(schema)} colonnes) : {', '.join(schema[-5:])} (+5)")

    # DEUX NOTIONS DIFFÉRENTES, et c'est la confusion des deux qui rendait le contrôle
    # inutilisable au 1er essai :
    #   (a) COHÉRENCE — l'en-tête et les lignes du fichier s'accordent (11/11 est cohérent).
    #       Un ancien journal est cohérent, il n'est pas fautif : le schéma a changé APRÈS.
    #   (b) CONFORMITÉ AU SCHÉMA COURANT — exigée du journal VIVANT (celui que le moteur
    #       écrit maintenant), qui doit naître avec l'en-tête courant.
    conformes, anciens_coherents, ecarts, detail = 0, 0, [], []
    courant_incoherent, courant_hors_schema = False, False
    # E15 — PIÈGE ÉVITÉ : signaler À VIE un fichier incoherent historique fabriquerait une
    # alarme qui ne s'éteint jamais (R14 : une alarme morte tue la confiance dans l'alarme).
    # Règle : un journal incoherent est BLOQUANT **s'il est le plus récent** (celui que le
    # moteur écrit MAINTENANT) ; sinon il est HISTORIQUE (superseded par un journal plus récent) :
    # signalé, chiffré, NON bloquant. La règle « âge < 1 h » a été essayée et REJETÉE : elle
    # affichait un rouge sur une faute déjà corrigée et déjà remplacée par le moteur — décision
    # écrite ici pour qu'elle ne soit pas redécidée par oubli.
    ecarts_bloquants, ecarts_historiques = [], []
    for i, p in enumerate(cibles):
        e, dist, vides = largeurs(p)
        coherence = (not dist) or (max(dist) <= e)          # (a)
        schema_ok = (e == len(schema))                        # (b)
        ok_global = coherence and (schema_ok or i > 0)        # historique cohérent = OK
        if schema_ok and coherence:
            conformes += 1
        elif coherence:
            anciens_coherents += 1
        else:
            _age = round((datetime.now().timestamp() - p.stat().st_mtime) / 60, 1)
            _e = {
                "fichier": p.name, "en_tete": e,
                "largeurs_lignes": {str(k): v for k, v in sorted(dist.items())},
                "n_lignes": sum(dist.values()), "age_min": _age,
            }
            if i == 0:
                _e["statut"] = "BLOQUANT (c'est le journal le plus récent = celui du moteur vivant)"
                ecarts_bloquants.append(_e)
            else:
                _e["statut"] = "HISTORIQUE — superseded, signalé, non bloquant"
                ecarts_historiques.append(_e)
            ecarts.append(_e)
        if i == 0:
            courant_incoherent = not coherence
            courant_hors_schema = not schema_ok
        detail.append({"fichier": p.name, "en_tete": e, "largeurs": dist, "vides": vides,
                       "coherent": coherence, "schema_courant": schema_ok})

    print(f"\nR1/R2 — {len(cibles)} journaux examinés : {conformes} au schéma courant, "
          f"{anciens_coherents} anciens mais COHÉRENTS (11/11 — légitimes), {len(ecarts)} INCOHÉRENTS "
          f"dont {len(ecarts_bloquants)} BLOQUANT(s) et {len(ecarts_historiques)} historique(s) superseded")
    for e in ecarts[:10]:
        print(f"   · {e['fichier']:38} en-tête {e['en_tete']:>3} · lignes {e['largeurs_lignes']} "
              f"· {e['n_lignes']} lignes · il y a {e['age_min']} min")
    if len(ecarts) > 10:
        print(f"   … et {len(ecarts) - 10} autres (historiques)")
    courante_ok = not courant_incoherent and not courant_hors_schema
    print(f"\nR3 — journal COURANT ({jsons[0].name if jsons else 'AUCUN'}) : "
          f"{'CONFORME' if courante_ok else 'INVALIDE'}"
          + (" (incohérent en-tête/lignes)" if courant_incoherent else "")
          + (" (en-tête pas au schéma courant : fichier né avant le 23/09)" if courant_hors_schema else ""))

    print("\nR4 — autotest du contrôle :")
    for nom, ok, det in res_auto:
        print(f"   [{'OK ' if ok else 'RATE'}] {nom} — {det}")
    print(f"   autotest : {'FIABLE' if auto_ok else 'NON FIABLE'}")

    rc = 0 if (auto_ok and courante_ok and not ecarts_bloquants) else 1
    print(f"\nVERDICT : {'CONFORME' if rc == 0 else 'ECART BLOQUANT DANS LE JOURNAL'} (rc={rc})")
    if ecarts_historiques:
        print(f"SIGNALÉ (non bloquant) : {len(ecarts_historiques)} journal(aux) incoherent(s) "
              f"superseded — le passé n'est pas réécrit, il est DÉCLARÉ.")
    print("Lecture seule : ce contrôle n'écrit dans aucun journal.")

    if args.json:
        Path(args.json).write_text(json.dumps({
            "instrument": "verif_schema_journal.py", "ts_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "schema": schema, "largeur_schema": len(schema),
            "journaux_examines": len(cibles), "conformes": conformes,
            "anciens_coherents": anciens_coherents, "ecarts": ecarts,
            "ecarts_bloquants": len(ecarts_bloquants),
            "ecarts_historiques": len(ecarts_historiques),
            "journal_courant": jsons[0].name if jsons else None,
            "journal_courant_conforme": bool(courante_ok), "autotest_fiable": auto_ok,
            "rc": rc, "lecture_seule": True, "ordres": 0,
        }, indent=2, ensure_ascii=False), encoding="utf-8")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
