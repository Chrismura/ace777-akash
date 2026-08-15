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
    lignes = [f"# Rapport Veilleuse — {datetime.now(timezone.utc).isoformat()}", ""]

    # e) Auto-intégrité de la veilleuse (comparée au registre)
    mon_chemin = Path(__file__).resolve()
    mon_md5 = calculer_md5(mon_chemin)
    for item in reg_data.get("fichier", []):
        if item["nom"].endswith("veilleuse_synapses.py") and item.get("verif") == "md5":
            attendu = item.get("md5", "")
            if attendu and attendu != mon_md5:
                anomalies.append(("INTRUSION",
                                  f"Auto-intégrité violée : {mon_chemin.name} modifié sans déclaration"))
            break

    # a) + c) Fichiers du registre
    for item in reg_data.get("fichier", []):
        nom = item["nom"]
        verif = item.get("verif")
        cible = RACINE / nom
        if not cible.exists():
            anomalies.append(("PANNE", f"Fichier manquant : {nom}"))
            continue
        if verif == "md5":
            attendu = item.get("md5", "")
            if attendu:
                actuel = calculer_md5(cible)
                if actuel != attendu:
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
    main()
