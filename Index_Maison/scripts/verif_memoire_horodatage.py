#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verif_memoire_horodatage.py — LE GARDIEN DE LA CLASSE E13
=========================================================

POURQUOI CE FICHIER EXISTE (23/09/2026)
---------------------------------------
Christophe : « c'est pas possible de faire encore ce type d'erreurs. »
Le 23/09, j'ai écrit dans MEMOIRE_COLLAB.md **4 horodatages de tête** :
10:40Z / 10:05Z / 09:45Z / 09:15Z. Les heures RÉELLES, lues sur les artefacts
que les lignes elles-mêmes citent, étaient **0947Z / 0939Z / 0922Z / 0907Z**
(inflation jusqu'à **+53 min**, donc une ligne datée DANS LE FUTUR).

C'est **exactement la classe E10** (un chiffre recalculé pris pour un chiffre
vérifié) appliquée au temps : une heure ESTIMÉE n'est pas une heure VÉRIFIÉE.
Le registre (`REGISTRE_ECHECS_ET_ERREURS.md`) nomme donc la classe **E13** et
**ce fichier est sa garde mécanique** — pas une promesse.

CE QU'IL CONTRÔLE (et seulement ça)
-----------------------------------
  R1  INSTRUMENT : toute ligne de la date la plus récente ne peut pas être
      datée dans le FUTUR au-delà de 5 min (marge d'horloge). ← aurait attrapé
      les 4 lignes du 23/09 (10:40Z écrites alors qu'il était 09:47Z).
  R2  ORDRE : dans une même date, les lignes se lisent du plus récent au plus
      ancien → toute remontée de temps est une anomalie.
  R3  AUTOTEST : le gardien prouve qu'il SAIT échouer (ligne future injectée et
      désordre injecté → DÉTECTÉ). Un gardien qu'on n'a jamais vu échouer ne
      garde rien.

LIMITES DÉCLARÉES (R8 : on écrit les bornes)
--------------------------------------------
  * Il détecte une heure **trop grande**, jamais une heure **trop petite** :
    une ligne datée 08:30Z alors qu'il était 09:00Z passe. C'est la moitié du
    problème qu'on sait attraper mécaniquement sans lire le mtime de chaque
    artefact cité (chantier ouvert, cf. E13).
  * Il ne juge QUE la date la plus récente : les lignes anciennes (22/09,
    09:17Z / 09:07Z / 09:25Z, hors ordre et incompatibles avec les artefacts
    du jour : CHIFFRAGE_SORTIE_MESUREE_20260922_0855/0857.json → 08:55Z/08:57Z)
    sont **signalées** au rapport mais **non re-datées** : je refuse
    d'**inventer une seconde fois** pour corriger un chiffre inventé.

LECTURE SEULE : ce script n'écrit JAMAIS dans la mémoire. Il écrit son verdict
dans `runs/VERIF_MEMOIRE_HORODATAGE.json` et sort rc=0 (conforme) / rc=1 (anomalie).

CANON : `Index_Maison/REGISTRE_ECHECS_ET_ERREURS.md` §2 (classe E13) + §6.
"""

from __future__ import annotations

import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]          # ace777-test-day1/
MEMOIRE = RACINE / "Index_Maison" / "MEMOIRE_COLLAB.md"
SORTIE = RACINE / "hulk-mexc" / "runs" / "VERIF_MEMOIRE_HORODATAGE.json"
# ÉTAT lu par le cockpit (même convention que thermo/seuil_moteur.json,
# thermo/regles_or.json… : un verdict qui n'est affiché nulle part n'existe pas, R15).
ETAT = RACINE / "Index_Maison" / "thermo" / "memoire_horodatage.json"

MARGE_FUTUR_MIN = 5          # tolérance d'horloge (secondes d'écriture, fuseaux)
# Ligne de mémoire : | 2026-09-23T0947Z | Qui | ...   (formats 0947Z ET 09:47Z)
RE_LIGNE = re.compile(r"^\|\s*(\d{4})-(\d{2})-(\d{2})T(\d{2}):?(\d{2})Z\s*\|")


def _ecrire(rapport: dict) -> None:
    """Écrit le verdict (runs/ + thermo/ pour le cockpit). Lecture seule côté mémoire."""
    rapport["ts"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    rapport["conforme"] = not rapport.get("anomalies")
    for p in (SORTIE, ETAT):
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(rapport, ensure_ascii=False, indent=2), encoding="utf-8")


def lire_lignes(texte: str) -> list[tuple[int, datetime]]:
    """Toutes les lignes horodatées du tableau, dans l'ordre du fichier."""
    out: list[tuple[int, datetime]] = []
    for i, ligne in enumerate(texte.splitlines(), start=1):
        m = RE_LIGNE.match(ligne)
        if not m:
            continue
        a, mo, j, h, mi = (int(x) for x in m.groups())
        try:
            out.append((i, datetime(a, mo, j, h, mi, tzinfo=timezone.utc)))
        except ValueError:
            continue
    return out


def controler(texte: str, maintenant: datetime) -> dict:
    """R1 + R2 sur la date la plus récente. Ne modifie rien."""
    lignes = lire_lignes(texte)
    rapport: dict = {
        "n_lignes_horodatees": len(lignes),
        "maintenant_utc": maintenant.strftime("%Y-%m-%dT%H:%MZ"),
        "anomalies": [],
        "signalements": [],
    }
    if not lignes:
        rapport["anomalies"].append("aucune ligne horodatée lisible — format attendu | AAAA-MM-JJTHHMMZ |")
        return rapport

    date_recente = max(d.date() for _, d in lignes)
    recentes = [(n, d) for n, d in lignes if d.date() == date_recente]

    # --- R1 : rien dans le futur (la date la plus récente) -------------------
    plafond = maintenant + timedelta(minutes=MARGE_FUTUR_MIN)
    for n, d in recentes:
        if d > plafond:
            retard = d - (maintenant + timedelta(minutes=MARGE_FUTUR_MIN))
            rapport["anomalies"].append(
                f"R1 ligne {n} : {d.strftime('%H%MZ')} est DANS LE FUTUR "
                f"(+{int(retard.total_seconds() // 60)} min vs l'heure réelle "
                f"{maintenant.strftime('%H%MZ')}) — heure estimée, pas lue"
            )

    # --- R2 : ordre décroissant dans la date la plus récente -----------------
    for (n1, d1), (n2, d2) in zip(recentes, recentes[1:]):
        if d2 > d1:
            rapport["anomalies"].append(
                f"R2 lignes {n1}→{n2} : {d1.strftime('%H%MZ')} puis "
                f"{d2.strftime('%H%MZ')} — le tableau se lit du plus récent au "
                f"plus ancien, cette remontée de temps est une anomalie"
            )

    # --- Signalements (non bloquants) : ordre dans les dates plus anciennes --
    autres = [(n, d) for n, d in lignes if d.date() != date_recente]
    for (n1, d1), (n2, d2) in zip(autres, autres[1:]):
        if d1.date() == d2.date() and d2 > d1:
            rapport["signalements"].append(
                f"lignes {n1}→{n2} ({d1.date()}) : {d1.strftime('%H%MZ')} puis "
                f"{d2.strftime('%H%MZ')} — hors ordre, NON re-daté (on n'invente "
                f"pas une seconde fois : lire le mtime de l'artefact cité)"
            )
    return rapport


def autotest(maintenant: datetime) -> tuple[bool, list[dict]]:
    """Le gardien prouve qu'il SAIT échouer.

    ⚠️ L'autotest ne dépend PAS de l'heure d'exécution : il travaille sur une
    heure de référence FIXE (10:00Z), sinon un test qui passe à 14 h et échoue
    à 9 h ne prouve rien (leçon E10 : un contrôle dépendant de son heure n'est
    pas un contrôle).
    """
    cas = []
    ref = datetime(2026, 9, 23, 10, 0, tzinfo=timezone.utc)
    L = "| ts | Qui | Action | Où | Quoi |\n|---|---|---|---|---|\n"

    # 1) conforme : ordre décroissant, rien dans le futur
    ok = L + ("| 2026-09-23T0947Z | Buffy | ★ | doc | ligne récente |\n"
              "| 2026-09-23T0922Z | Buffy | ★ | doc | ligne plus ancienne |\n")
    r1 = controler(ok, ref)
    cas.append({"cas": "conforme", "attendu": 0, "obtenu": len(r1["anomalies"]),
                "ok": len(r1["anomalies"]) == 0})

    # 2) LE CAS RÉEL DU 23/09 : ligne datée dans le futur (10:40Z alors qu'il est 09:47Z)
    faux = L + ("| 2026-09-23T1040Z | Buffy | ★ | doc | heure écrite de tête |\n"
                "| 2026-09-23T0939Z | Buffy | ★ | doc | ligne d'avant |\n")
    r2 = controler(faux, ref)
    cas.append({"cas": "R1 ligne future (cas réel du 23/09 : 10:40Z pour 09:47Z)",
                "attendu": 1, "obtenu": len(r2["anomalies"]),
                "ok": len(r2["anomalies"]) >= 1})

    # 3) désordre dans la même date
    desordre = L + ("| 2026-09-23T0922Z | Buffy | ★ | doc | ancienne en haut |\n"
                    "| 2026-09-23T0947Z | Buffy | ★ | doc | récente en bas |\n")
    r3 = controler(desordre, ref)
    cas.append({"cas": "R2 désordre même date", "attendu": 1,
                "obtenu": len(r3["anomalies"]), "ok": len(r3["anomalies"]) >= 1})

    # 4) LIMITE DÉCLARÉE : une heure SOUS-estimée n'est pas détectable
    sous = L + "| 2026-09-23T0830Z | Buffy | ★ | doc | heure trop petite (09:00Z réelles) |\n"
    r4 = controler(sous, ref)
    cas.append({"cas": "LIMITE — heure sous-estimée non détectable (déclaré)",
                "attendu": 0, "obtenu": len(r4["anomalies"]),
                "ok": len(r4["anomalies"]) == 0})

    # 5) LE CAS RÉEL DU 22/09 : lignes hors ordre d'une date ANCIENNE
    #    → SIGNALÉES, jamais bloquantes (on ne re-date pas en inventant)
    anciennes = L + ("| 2026-09-22T09:17Z | Buffy | ★ | doc | ancienne date |\n"
                     "| 2026-09-22T09:07Z | Buffy | ★ | doc | idem |\n"
                     "| 2026-09-22T09:25Z | Buffy | ★ | doc | remontée |\n"
                     "| 2026-09-23T0947Z | Buffy | ★ | doc | la plus récente |\n")
    r5 = controler(anciennes, ref)
    cas.append({"cas": "signalement 22/09 hors ordre (non bloquant)",
                "attendu": 1, "obtenu": len(r5["signalements"]),
                "ok": len(r5["signalements"]) >= 1 and not r5["anomalies"]})
    return all(c["ok"] for c in cas), cas


def main() -> int:
    maintenant = datetime.now(timezone.utc)
    rapport: dict = {
        "instrument": "verif_memoire_horodatage.py",
        "classe": "E13",
        "source": str(MEMOIRE.relative_to(RACINE)),
        "lecture_seule": True,
    }
    print("=== GARDIEN MEMOIRE — HORODATAGE (classe E13) ===")
    print(f"source : {MEMOIRE.relative_to(RACINE)} · maintenant : {maintenant.strftime('%Y-%m-%dT%H:%MZ')}")

    fiable, cas = autotest(maintenant)
    rapport["autotest"] = {"fiable": fiable, "cas": cas}
    n_ok = sum(1 for c in cas if c["ok"])
    print(f"autotest : {'FIABLE' if fiable else 'NON FIABLE'} ({n_ok}/{len(cas)} cas)")
    for c in cas:
        print(f"  [{'ok' if c['ok'] else 'KO'}] {c['cas']} (attendu {c['attendu']}, obtenu {c['obtenu']})")
    if not fiable:
        rapport["verdict"] = "NON FIABLE — l'autotest échoue, le gardien ne garde rien"
        _ecrire(rapport)
        print("VERDICT : NON FIABLE")
        return 1

    if not MEMOIRE.exists():
        rapport["verdict"] = "SOURCE ABSENTE"
        print(f"VERDICT : source absente ({MEMOIRE})")
        _ecrire(rapport)
        return 2

    ctrl = controler(MEMOIRE.read_text(encoding="utf-8"), maintenant)
    rapport.update(ctrl)
    for a in ctrl["anomalies"]:
        print(f"  ANOMALIE {a}")
    # Un gardien qui noie son lecteur finit ignoré (R14) : on n'affiche que les
    # 3 premiers signalements, le JSON les garde tous.
    signal = ctrl["signalements"]
    for s in signal[:3]:
        print(f"  signalé  {s}")
    if len(signal) > 3:
        print(f"  … et {len(signal) - 3} autre(s) signalement(s) (voir le JSON)")
    rapport["verdict"] = (
        f"CONFORME — {ctrl['n_lignes_horodatees']} lignes horodatées, "
        f"date la plus récente sans heure future ni remontée de temps"
        if not ctrl["anomalies"] else
        f"ANOMALIE — {len(ctrl['anomalies'])} horodatage(s) incohérent(s) de la classe E13"
    )
    rapport["n_signalements"] = len(ctrl["signalements"])
    print(f"VERDICT : {rapport['verdict']}")
    _ecrire(rapport)
    return 1 if ctrl["anomalies"] else 0


if __name__ == "__main__":
    sys.exit(main())
