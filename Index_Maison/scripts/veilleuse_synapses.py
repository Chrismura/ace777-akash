#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rôle (ACE777) : VEILLEUSE DES SYNAPSES — surveille l'intégrité du noyau critique.
Vérifie (cadence 10 min via launchd) :
  a) md5 des fichiers stables indexés → écart non déclaré = INTRUSION
  b) process attendus vivants (launchctl/pgrep) → panne/crash
  c) fraîcheur des fichiers données (live.json, whales) → blocage silencieux
  d) kill-switches présents (STOP / STOP_ALL) → sécurité en place
  e) auto-intégrité (md5 de soi-même) → compromission de la veilleuse
  f) pré-déclarations (R20.1) → une modification DÉCLARÉE avant l'acte n'est PAS une
     intrusion : elle sort de l'alarme et de l'alerte vocale (classe E22, cf. _predeclare)
En cas d'anomalie : rapport thermo/VEILLEUSE.md + journal + ALERTE_[ts].json +
lancement d'alerte_vocale.py en détaché (boucle stricte 24h/24, volonté Christophe).
MAINTENANCE_PREVUE (date ISO de fin) → suspend les alertes.
Stdlib uniquement, écriture atomique, kill-switch respecté, zéro touche moteur Hulk.
"""

import os
import sys
import json
import time
import hashlib
import tempfile
import subprocess
from pathlib import Path
from datetime import datetime, timezone

# RACINE = repo racine (~/ace777-test-day1) — le registre utilise des chemins relatifs au repo
RACINE = Path(__file__).resolve().parent.parent.parent
IM = RACINE / "Index_Maison"
REGISTRE_PATH = IM / "strategie" / "REGISTRE_SYNAPSES.json"
THERMO_VEILLEUSE = IM / "thermo" / "VEILLEUSE.md"
ALERTES_DIR = IM / "data" / "alertes"
JOURNAL_PATH = ALERTES_DIR / "veilleuse.log"
MAINTENANCE_PATH = IM / "strategie" / "MAINTENANCE_PREVUE"
ALERTE_VOCALE = IM / "scripts" / "alerte_vocale.py"
PREDECL_PATH = IM / "strategie" / "PREDECLARATIONS.jsonl"

KILL_SWITCHES = [
    IM / "strategie" / "STOP",
    Path.home() / "ace777-test-day1" / "Index_Maison" / "STOP_ALL",
]

# Process attendus vivants (labels launchd / noms) — PAS les services calendrier
# (discipline-quotidienne = 1×/jour, pas permanent)
ATTENDUS_PROCESS = [
    "com.ace777.hub-cockpit-feed",
    "com.ace777.cockpit-http",
    "com.ace777.cockpit-pont",
    "com.ace777.whales",
    "com.ace777.veilleuse",
]


def journaliser(message: str):
    try:
        ALERTES_DIR.mkdir(parents=True, exist_ok=True)
        ts = datetime.now(timezone.utc).isoformat()
        with open(JOURNAL_PATH, "a", encoding="utf-8") as f:
            f.write(f"[{ts}] {message}\n")
    except Exception:
        pass


def ecriture_atomique(chemin: Path, contenu: str):
    chemin.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_path = tempfile.mkstemp(dir=str(chemin.parent), text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(contenu)
        os.replace(tmp_path, chemin)
    except Exception:
        if os.path.exists(tmp_path):
            try:
                os.remove(tmp_path)
            except Exception:
                pass
        raise


def calculer_md5(chemin: Path) -> str:
    try:
        h = hashlib.md5()
        with open(chemin, "rb") as f:
            while chunk := f.read(8192):
                h.update(chunk)
        return h.hexdigest()
    except Exception:
        return ""


def _predeclare(fichier: str, md5_scelle: str = "") -> bool:
    """Vrai si une PRÉ-DÉCLARATION (R20.1) couvre cette modification : une déclaration du
    MÊME fichier dont le `md5_avant` est le md5 SCELLÉ au registre — donc déclarée CONTRE la
    version encore scellée, avant l'acte.

    POURQUOI CE LECTEUR EXISTE (classe E22, récidive 28-29/09/2026) : SANS lui, la veilleuse
    ne lisait pas le registre des pré-déclarations. Le rituel CORRECT (pré-déclarer →
    modifier → re-sceler) faisait donc crier « INTRUSION — modification non déclarée » puis
    déclenchait l'alerte VOCALE pendant toute la fenêtre déclaré→re-scellé (jusqu'à 10 min,
    cadence de la veilleuse) : une fausse alarme (R14) qui rendait le rituel inutilisable —
    plus personne ne déclare un acte qui fait sonner la sirène. Preuve par le CODE : dans la
    version antérieure, ce fichier ne lisait jamais PREDECLARATIONS.jsonl (git diff du
    29/09). Preuve par le HARNAIS : `veilleuse_synapses.py --autotest` (4 cas).

    ⚠️ MESURE INVENTÉE, CORRIGÉE LE 29/09 (classe E10) : une version antérieure de ce
    commentaire affirmait que la veilleuse avait accusé `preuve_lecture.py` le 29/09 à
    09:11:27Z « alors que la modification avait été annoncée ». C'était FAUX : ce fichier n'a
    JAMAIS été pré-déclaré (il fait partie des 16 actes constatés, radiés de l'alarme). Les
    deux seules alarmes réelles du journal — 09:01:27Z sur `verdicts_protocoles.py`,
    09:11:27Z sur `preuve_lecture.py` — étaient donc JUSTES : la veilleuse n'a pas menti ce
    jour-là, elle a crié sur deux actes réellement non déclarés. Le trou A reste réel, mais
    il est LATENT : il se prouve par le code et le harnais, jamais par une alarme inventée.
    Un gardien doit crier sur un acte ANNONCÉ ; on ne l'accuse pas d'un cri qu'il n'a pas
    poussé (R14 dans les deux sens).

    Une déclaration ne peut pas être fabriquée pour éteindre un rouge : elle doit porter le
    md5 de la version ENCORE SCELLÉE, sinon elle ne couvre rien.
    """
    if not PREDECL_PATH.exists():
        return False
    try:
        for ligne in PREDECL_PATH.read_text(encoding="utf-8").splitlines():
            ligne = ligne.strip()
            if not ligne:
                continue
            try:
                o = json.loads(ligne)
            except Exception:
                continue
            if o.get("fichier") != fichier:
                continue
            if md5_scelle and o.get("md5_avant") != md5_scelle:
                continue
            return True
    except Exception:
        return False
    return False


def autotest() -> int:
    """Preuve que `_predeclare` SAIT dire NON (un gardien qui ne peut pas refuser ne garde rien).

    Travaille sur un registre SYNTHÉTIQUE (jamais le vrai) : le vrai registre est sauvegardé
    puis restauré, quoi qu'il arrive.
    """
    global PREDECL_PATH
    vrai = PREDECL_PATH
    tmp = Path(tempfile.mkdtemp()) / "PREDECLARATIONS.jsonl"
    tmp.write_text(
        json.dumps({"ts": "2026-09-29T09:22:41Z", "fichier": "X/scelle.py",
                    "md5_avant": "aaa"}) + "\n"
        + json.dumps({"ts": "2026-09-29T09:22:41Z", "fichier": "Y/autre.py",
                      "md5_avant": "bbb"}) + "\n",
        encoding="utf-8")
    PREDECL_PATH = tmp
    try:
        cas = [
            ("acte DÉCLARÉ (md5_avant == md5 scellé) → couvert",
             _predeclare("X/scelle.py", "aaa") is True),
            ("acte NON déclaré → refusé", _predeclare("Z/inconnu.py", "ccc") is False),
            ("déclaration d'un AUTRE fichier → refusée", _predeclare("Y/autre.py", "aaa") is False),
            ("mauvais md5_avant (déclaration fabriquée) → refusée",
             _predeclare("X/scelle.py", "zzz") is False),
        ]
    finally:
        PREDECL_PATH = vrai
    for nom, ok in cas:
        print(f"  [{'OK ' if ok else 'KO '}] {nom}")
    bon = all(ok for _, ok in cas)
    print(f"  → {'GARDIEN FIABLE' if bon else 'GARDIEN CASSÉ'} ({sum(1 for _, ok in cas if ok)}/{len(cas)} cas)")
    return 0 if bon else 3


def alerte_vocale_active() -> bool:
    """Vrai si une boucle d'alerte vocale tourne déjà (anti-empilement).
    Sinon, la veilleuse toutes les 10 min empilerait des boucles infinies."""
    try:
        out = subprocess.check_output(["pgrep", "-f", "alerte_vocale.py"],
                                      text=True, stderr=subprocess.DEVNULL)
        return bool(out.strip())
    except Exception:
        return False


def verifier_maintenance() -> bool:
    """True si MAINTENANCE_PREVUE existe avec une date de fin future."""
    if not MAINTENANCE_PATH.exists():
        return False
    try:
        fin = datetime.fromisoformat(MAINTENANCE_PATH.read_text(encoding="utf-8").strip())
        if datetime.now(timezone.utc) < fin:
            return True
    except Exception:
        pass
    return False


def declencher_alerte(type_alerte: str, description: str):
    """Écrit ALERTE_[ts].json + lance alerte_vocale.py en détaché (boucle stricte)."""
    ts = int(time.time())
    alerte_data = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "id": f"ALERTE_VEILLEUSE_{ts}",
        "type": type_alerte,
        "description": description,
    }
    try:
        ALERTES_DIR.mkdir(parents=True, exist_ok=True)
        ecriture_atomique(ALERTES_DIR / f"ALERTE_{ts}.json",
                          json.dumps(alerte_data, ensure_ascii=False, indent=2))
    except Exception as e:
        journaliser(f"Erreur écriture ALERTE json : {e}")

    msg = f"Alerte ACE777. {type_alerte}. {description}"
    try:
        subprocess.Popen(
            ["python3", str(ALERTE_VOCALE), "--message", msg, "--id", str(ts)],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            start_new_session=True,
        )
        journaliser(f"ALERTE [{type_alerte}] : {description} — alerte vocale lancée (id {ts})")
    except Exception as e:
        journaliser(f"Erreur lancement alerte_vocale : {e}")


def verifier_process(attendu: str) -> bool:
    """Vérifie qu'un label launchd / process est vivant."""
    try:
        out = subprocess.check_output(["launchctl", "list"], text=True,
                                      stderr=subprocess.DEVNULL)
        if attendu in out:
            return True
    except Exception:
        pass
    try:
        out = subprocess.check_output(["pgrep", "-fl", attendu], text=True,
                                      stderr=subprocess.DEVNULL)
        return attendu in out
    except Exception:
        return False


def main():
    journaliser("Veilleuse démarrée.")

    # d) Kill-switches présents (sécurité en place — on note, on ne bloque pas)
    kill_actifs = [str(ks) for ks in KILL_SWITCHES if ks.exists()]

    if not REGISTRE_PATH.exists():
        journaliser("ERREUR : registre introuvable — pas de veille possible.")
        sys.exit(1)
    try:
        reg_data = json.loads(REGISTRE_PATH.read_text(encoding="utf-8"))
    except Exception as e:
        journaliser(f"ERREUR : registre illisible : {e}")
        sys.exit(1)

    anomalies = []
    declarees = []      # modifications ANNONCÉES (R20.1) en attente de re-scellement : pas une intrusion
    lignes = [f"# Rapport Veilleuse — {datetime.now(timezone.utc).isoformat()}", ""]

    # e) Auto-intégrité de la veilleuse (comparée au registre)
    mon_chemin = Path(__file__).resolve()
    mon_md5 = calculer_md5(mon_chemin)
    for item in reg_data.get("fichier", []):
        if str(item.get("nom", "")).endswith("veilleuse_synapses.py") and item.get("verif") == "md5":
            attendu = item.get("md5", "")
            if attendu and attendu != mon_md5:
                if _predeclare(str(item.get("nom", "")), attendu):
                    declarees.append(f"Auto-intégrité : `{mon_chemin.name}` DÉCLARÉ (R20.1), re-scellement en attente")
                else:
                    anomalies.append(("INTRUSION",
                                      f"Auto-intégrité violée : {mon_chemin.name} modifié sans déclaration"))
            break

    # a) + c) Fichiers du registre
    for item in reg_data.get("fichier", []):
        # Robustesse : une entrée de registre malformée ne doit pas tuer la veilleuse
        # (crash observé le 14/09 : KeyError 'nom'). On la signale et on continue.
        nom = item.get("nom")
        verif = item.get("verif")
        if not nom:
            anomalies.append(("REGISTRE", "Entrée sans clé 'nom' — ignorée (registre à corriger)"))
            continue
        cible = RACINE / nom
        if not cible.exists():
            anomalies.append(("PANNE", f"Fichier manquant : {nom}"))
            continue
        if verif == "md5":
            attendu = item.get("md5", "")
            if attendu:
                actuel = calculer_md5(cible)
                if actuel != attendu:
                    if _predeclare(nom, attendu):
                        declarees.append(f"Modification DÉCLARÉE (R20.1) en attente de re-scellement : `{nom}`")
                    else:
                        anomalies.append(("INTRUSION",
                                          f"Modification non déclarée : {nom} (md5 diffère du registre)"))
        elif verif == "fraicheur":
            try:
                max_min = item.get("fraicheur_max_min", 60)
                age_min = (time.time() - cible.stat().st_mtime) / 60.0
                if age_min > max_min:
                    anomalies.append(("PANNE",
                                      f"Données figées : {nom} (âge {age_min:.0f} min > {max_min} min)"))
            except Exception:
                anomalies.append(("PANNE", f"Fraîcheur impossible à vérifier : {nom}"))

    # b) Process attendus vivants
    for proc in ATTENDUS_PROCESS:
        if not verifier_process(proc):
            anomalies.append(("PANNE", f"Process attendu absent : {proc}"))

    # Rapport
    if anomalies:
        lignes.append("## État : ⚠️ ANOMALIES DÉTECTÉES")
        for t, desc in anomalies:
            lignes.append(f"- **{t}** : {desc}")
    else:
        lignes.append("## État : ✅ STABLE — tout est en ordre")
    if declarees:
        lignes.append("")
        lignes.append("## Modifications DÉCLARÉES (R20.1) — annoncées AVANT l'acte, pas des intrusions")
        for d in dict.fromkeys(declarees):        # l'auto-intégrité et la boucle du registre peuvent viser le même fichier
            lignes.append(f"- {d}")
        lignes.append("")
        lignes.append("*(Une modification déclarée passe hors alarme et hors alerte vocale ; "
                      "elle doit être re-scellée par `resceler.py`.)*")
    if kill_actifs:
        lignes.append("")
        lignes.append(f"Kill-switches présents (sécurité) : {', '.join(kill_actifs)}")
    ecriture_atomique(THERMO_VEILLEUSE, "\n".join(lignes) + "\n")

    # Alerte
    if anomalies:
        if verifier_maintenance():
            journaliser("Anomalies ignorées (MAINTENANCE_PREVUE active).")
            sys.exit(0)
        t, desc = anomalies[0]
        if alerte_vocale_active():
            journaliser(f"Anomalie [{t}] : {desc} — alerte vocale DÉJÀ active, pas de nouvel empilement.")
        else:
            journaliser(f"ALERTE [{t}] : {desc}")
            declencher_alerte(t, desc)
        sys.exit(1)

    journaliser("Vérification OK — aucune anomalie.")
    sys.exit(0)


if __name__ == "__main__":
    if "--autotest" in sys.argv:
        sys.exit(autotest())
    main()
