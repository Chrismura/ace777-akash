#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rôle : Génère et met à jour Index_Maison/strategie/REGISTRE_ORGANES.json en scannant
       les plists et en fusionnant non-destructivement avec criticite_organes.json.
"""

import os
import json
import hashlib
import subprocess
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
INDEX_MAISON = BASE_DIR / "Index_Maison"
PLISTS_DIRS = [
    Path.home() / "Library" / "LaunchAgents",
    INDEX_MAISON / "plists"
]
CRITICITE_PATH = INDEX_MAISON / "strategie" / "criticite_organes.json"
REGISTRE_PATH = INDEX_MAISON / "strategie" / "REGISTRE_ORGANES.json"

def ecriture_atomique(chemin: Path, data_str: str) -> None:
    chemin.parent.mkdir(parents=True, exist_ok=True)
    if chemin.exists():
        try:
            backup_path = chemin.with_suffix(chemin.suffix + ".bak")
            backup_path.write_bytes(chemin.read_bytes())
        except Exception:
            pass
    import tempfile
    fd, tmp_path = tempfile.mkstemp(dir=str(chemin.parent), text=True)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as f:
            f.write(data_str)
        os.replace(tmp_path, str(chemin))
    except Exception as e:
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
        raise e

def calculer_md5(fichier: Path) -> str:
    hasher = hashlib.md5()
    try:
        with open(fichier, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception:
        return ""

# ── CADENCE RÉELLE DU DÉCLENCHEUR (réparé 20/09/2026, GO « incassable ») ─────
# AVANT : `freq = 300` par défaut dès qu'il n'y avait pas de StartInterval → 22
# organes à déclencheur CALENDAIRE (quotidien : journal-soir, veille-yt, verif-setup,
# suivi-setup-red…) portaient une cadence FAUSSE de 300 s. Inerte tant qu'ils n'ont
# pas de produit (le chien les juge alors sur leur sortie launchd), mais le jour où
# l'un reçoit un produit, le seuil tombait à 600 s → faux positif PERMANENT (R14 :
# une alarme qui ment est pire que pas d'alarme, elle apprend à ignorer les autres).
# Désormais on lit le VRAI déclencheur et on en déduit la VRAIE période. La vérité
# humaine (frequence_attendue_sec_critique de criticite_organes.json) reste
# PRIORITAIRE : elle déclare la cadence du PRODUIT, qui peut être plus lente que le
# déclencheur (cortana.urgent tourne toutes les 10 s mais n'écrit que sur alerte).
def cadence_du_plist(plist_file: Path):
    """-> (periode_sec_ou_300_defaut, declencheur, cadence_plist_sec_ou_None)

    cadence_plist_sec = fait mesuré (période du déclencheur), None si événementiel
    (KeepAlive / WatchPaths / RunAtLoad) : on ne devine pas une période qui n'existe pas.
    """
    try:
        import plistlib
        d = plistlib.load(open(plist_file, "rb"))
    except Exception:
        return 300, "illisible", None

    si = d.get("StartInterval")
    if si:
        return int(si), "StartInterval %ss" % int(si), int(si)

    sci = d.get("StartCalendarInterval")
    if sci:
        entrees = sci if isinstance(sci, list) else [sci]
        jours = [e for e in entrees if isinstance(e, dict) and "Weekday" in e]
        if jours:
            # Entrées hebdomadaires (TROUPEAU-INV lun/mer/ven) : période moyenne.
            periode = int(7 * 86400 / max(1, len(jours)))
            quand = "%d j/sem %s" % (len(jours), ",".join(
                "%02d:%02d" % (int(e.get("Hour", 0)), int(e.get("Minute", 0))) for e in jours))
            return periode, "Calendrier hebdo (%s)" % quand, periode
        if len(entrees) > 1:
            periode = int(86400 / len(entrees))
            return periode, "Calendrier %d passages/jour" % len(entrees), periode
        e = entrees[0] if isinstance(entrees[0], dict) else {}
        if "Day" in e or "Month" in e:
            return 2592000, "Calendrier mensuel", 2592000
        return 86400, "Calendrier quotidien %02d:%02d" % (int(e.get("Hour", 0)),
                                                          int(e.get("Minute", 0))), 86400

    if d.get("KeepAlive"):
        return 300, "KeepAlive (événementiel)", None
    if d.get("WatchPaths"):
        return 300, "WatchPaths (événementiel)", None
    if d.get("RunAtLoad"):
        return 300, "RunAtLoad (événementiel)", None
    return 300, "aucun déclencheur déclaré", None


def launchd_charges():
    """Retourne l'ensemble des labels com.ace777.* réellement chargés dans launchd."""
    charges = set()
    try:
        out = subprocess.run(["launchctl", "list"], capture_output=True, text=True, timeout=15).stdout
        # Format launchctl list : "PID\tStatut\tLabel" — le label est la DERNIÈRE colonne,
        # jamais en début de ligne (bug historique : charges() renvoyait toujours un set vide).
        for ligne in out.splitlines():
            parties = ligne.strip().split("\t")
            if len(parties) >= 3:
                label = parties[-1].strip()
                if label.startswith("com.ace777."):
                    charges.add(label)
    except Exception:
        pass  # fail-open : si launchctl indisponible, on considère tout chargé pour ne pas crier en masse
    return charges


def main():
    charges = launchd_charges()
    criticites_data = {}
    if CRITICITE_PATH.exists():
        try:
            with open(CRITICITE_PATH, "r", encoding="utf-8") as f:
                raw = json.load(f)
                for item in raw.get("organes", []):
                    criticites_data[item["organe"]] = item
        except Exception:
            pass

    organes_trouves = {}
    md5_plists = {}

    for pdir in PLISTS_DIRS:
        if not pdir.exists():
            continue
        for plist_file in pdir.glob("com.ace777.*.plist"):
            nom_organe = plist_file.stem.replace("com.ace777.", "")
            md5_val = calculer_md5(plist_file)
            md5_plists[plist_file.name] = md5_val

            # Cadence réelle déduite du déclencheur (voir cadence_du_plist).
            freq, declencheur, cadence_plist = cadence_du_plist(plist_file)

            organe_info = criticites_data.get(nom_organe, {
                "organe": nom_organe,
                "criticite": "MINEUR",
                "tolerance_mult": 2.0,
                "mode": "produit",
                "commentaire": "Découvert par scan automatique"
            })
            # VÉRITÉ HUMAINE (criticite_organes.json) : sa fréquence explicite PRIME sur le plist.
            # Cas légitimes : daemon KeepAlive sans StartInterval (llm-gate-hub), produit
            # daté/calendrier (veille-hub 07h00), cadence d'écriture variable (vigie-live).
            freq_humaine = organe_info.get("frequence_attendue_sec_critique")
            if freq_humaine:
                freq = int(freq_humaine)
            organe_info["frequence_attendue_sec"] = freq
            organe_info["plist"] = str(plist_file.name)
            # FAITS de la revue des organes (20/09) : la cadence DÉCLARÉE (seuil du
            # chien) et la cadence RÉELLE du déclencheur coexistent sans se mentir.
            # Une divergence n'est pas une panne — c'est une déclaration à faire.
            organe_info["declencheur"] = declencheur
            organe_info["cadence_plist_sec"] = cadence_plist
            # VÉRITÉ MACHINE : chargé dans launchd (launchctl list), pas l'emplacement du fichier
            organe_info["zone_grise"] = (plist_file.stem not in charges) if charges else False

            organes_trouves[nom_organe] = organe_info

    # Fusion non destructive avec les éléments critiques déclarés non présents en plist physique
    for nom, obj in criticites_data.items():
        if nom not in organes_trouves:
            obj["zone_grise"] = True
            organes_trouves[nom] = obj

    registre_final = {
        "generated_at": datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
        "md5_plists": md5_plists,
        "organes": list(organes_trouves.values())
    }

    ecriture_atomique(REGISTRE_PATH, json.dumps(registre_final, indent=2))
    print(f"Registre généré avec succès : {REGISTRE_PATH}")

if __name__ == "__main__":
    main()
