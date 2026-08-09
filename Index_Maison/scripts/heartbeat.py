#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Généré par Google Gemini via hub (loi 1quinquies : Ada spécifie, le hub écrit) — 09/08
# Fichier : heartbeat.py
import os
import sys
import json
import re
import subprocess
from datetime import datetime, timezone, timedelta
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

HOME = Path("/Users/christophe")
VAULT = HOME / "Documents" / "Obsidian_ACE777"
MAISON = HOME / "ace777-test-day1"
OUTBOX = MAISON / "Index_Maison" / "OUTBOX_OBSIDIAN"
PRISE_IA = HOME / "prise-ia"
REPORTS = PRISE_IA / "reports"
HEARTBEAT_JSON = PRISE_IA / "heartbeat.json"
GRAPH_FILE = MAISON / "Index_Maison" / "graph_cerveau" / "data.js"
QWEN_IDEES = OUTBOX / "AUTO_EVOL" / "IDEES.md"
QWEN_LOG = REPORTS / "QWEN_ELABORE.log"
PAUSE_FILE = MAISON / "Index_Maison" / "PAUSE_ORCHESTRATRICE"
ALERT_FILE = OUTBOX / "A_Mon_Attention" / "HEARTBEAT_ALERT.md"
HUB_HEALTH_URL = "http://127.0.0.1:11435/health"

def obtenir_temps_actuel():
    return datetime.now(timezone.utc)

def fichier_age_heures(chemin):
    if not chemin.exists():
        return 9999.0
    mtime = chemin.stat().st_mtime
    dt_mtime = datetime.fromtimestamp(mtime, timezone.utc)
    delta = obtenir_temps_actuel() - dt_mtime
    return delta.total_seconds() / 3600.0

courant_epoch = lambda: obtenir_temps_actuel().strftime("%Y-%m-%dT%H:%M:%SZ")

def verifier_hub():
    req = Request(HUB_HEALTH_URL, method="GET")
    try:
        with urlopen(req, timeout=6) as response:
            return response.status == 200
    except (URLError, HTTPError, TimeoutError, Exception):
        return False

def mesurer_ram():
    try:
        res = subprocess.run(["memory_pressure", "-Q"], capture_output=True, text=True, timeout=5)
        sortie = res.stdout
        match = re.search(r"System-wide memory free percentage:\s*(\d+)%", sortie)
        if match:
            return int(match.group(1))
    except Exception:
        pass
    return 100

def verifier_git():
    if not (MAISON / ".git").exists():
        return 9999.0
    try:
        res = subprocess.run(
            ["git", "-C", str(MAISON), "log", "-1", "--format=%ct"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if res.returncode == 0 and res.stdout.strip():
            epoch_commit = float(res.stdout.strip())
            dt_commit = datetime.fromtimestamp(epoch_commit, timezone.utc)
            delta = obtenir_temps_actuel() - dt_commit
            return delta.total_seconds() / 3600.0
    except Exception:
        pass
    return 9999.0

def charger_dernier_heartbeat():
    if HEARTBEAT_JSON.exists():
        try:
            with open(HEARTBEAT_JSON, "r", encoding="utf-8", errors="replace") as f:
                return json.load(f)
        except Exception:
            pass
    return None

def ecrire_alerte_et_pause(alertes, pause_active):
    ALERT_FILE.parent.mkdir(parents=True, exist_ok=True)
    horodatage = obtenir_temps_actuel().strftime("%Y-%m-%d %H:%M:%S UTC")
    
    texte_alerte = f"# Alerte Heartbeat - {horodatage}\n\n"
    for alerte in alertes:
        texte_alerte += f"- {alerte}\n"
    texte_alerte += f"\nStatut pause orchestratrice: {'ACTIVÉE' if pause_active else 'LEVÉE'}\n"
    
    with open(ALERT_FILE, "w", encoding="utf-8") as f:
        f.write(texte_alerte)
        
    if pause_active:
        PAUSE_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(PAUSE_FILE, "w", encoding="utf-8") as f:
            f.write(f"Pause déclenchée le {horodatage}\n")
    else:
        if PAUSE_FILE.exists():
            try:
                PAUSE_FILE.unlink()
            except Exception:
                pass

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--status":
        dernier = charger_dernier_heartbeat()
        if not dernier:
            print("Aucun historique de heartbeat trouvé.")
        else:
            print(f"Dernier pouls : {dernier.get('ts', 'Inconnu')}")
            print(f"Graph age : {dernier.get('graph_h', -1)} h")
            print(f"Git age : {dernier.get('git_h', -1)} h")
            print(f"Hub status : {'OK' if dernier.get('hub') else 'KO'}")
            print(f"Qwen age : {dernier.get('qwen_h', -1)} h")
            print(f"RAM libre : {dernier.get('ram_pct', -1)} %")
            print(f"Pause active : {dernier.get('pause', False)}")
            print("Alertes :")
            for a in dernier.get('alerts', []):
                print(f"  - {a}")
        sys.exit(0)

    graph_h = fichier_age_heures(GRAPH_FILE)
    git_h = verifier_git()
    hub_ok = verifier_hub()
    qwen_h = fichier_age_heures(QWEN_IDEES)
    qwen_log_h = fichier_age_heures(QWEN_LOG)
    ram_pct = mesurer_ram()

    alertes = []
    
    if graph_h > 30.0:
        alertes.append(f"GRAPH stagne depuis {graph_h:.1f} heures.")
        
    if git_h > 4.0:
        alertes.append(f"GIT stagne depuis {git_h:.1f} heures.")
        
    if not hub_ok:
        alertes.append("HUB inaccessible (health check échoué).")
        
    qwen_stagne = (qwen_h > 72.0) and (qwen_log_h > 72.0)
    if qwen_stagne:
        alertes.append(f"QWEN STAGNE (IDEES.md age: {qwen_h:.1f}h, log age: {qwen_log_h:.1f}h).")
        
    if ram_pct < 15:
        alertes.append(f"RAM critique: {ram_pct}% libre.")

    # Fix audit tiers (famille differente) : seuil RAM relevé à 60 % (l'auditeur
    # jugeait 15 % trop laxiste — le Mac Air 8 Go vit déjà serré, alerter plus tôt).
    if 15 <= ram_pct < 60:
        alertes.append(f"RAM tendue: {ram_pct}% libre (< 60%).")
    ancien_hb = charger_dernier_heartbeat()
    runs_consecutifs_critiques = 0
    
    hub_actuel_ok = hub_ok
    qwen_actuel_stagne = qwen_stagne
    
    if ancien_hb:
        ancien_hub = ancien_hb.get("hub", True)
        ancien_qwen_stagne = ancien_hb.get("qwen_stagne", False)
        if (not ancien_hub or ancien_qwen_stagne) and (not hub_actuel_ok or qwen_actuel_stagne):
            runs_consecutifs_critiques = 2
        elif not hub_actuel_ok or qwen_actuel_stagne:
            runs_consecutifs_critiques = 1

    pause_necessaire = runs_consecutifs_critiques >= 2

    if alertes or pause_necessaire:
        ecrire_alerte_et_pause(alertes, pause_necessaire)
    else:
        ecrire_alerte_et_pause([], False)

    donnees_heartbeat = {
        "ts": courant_epoch(),
        "graph_h": round(graph_h, 2),
        "git_h": round(git_h, 2),
        "hub": hub_ok,
        "qwen_h": round(qwen_h, 2),
        "qwen_stagne": qwen_stagne,
        "ram_pct": ram_pct,
        "pause": pause_necessaire,
        "alerts": alertes
    }

    PRISE_IA.mkdir(parents=True, exist_ok=True)
    try:
        with open(HEARTBEAT_JSON, "w", encoding="utf-8") as f:
            json.dump(donnees_heartbeat, f, ensure_ascii=False, indent=2)
    except Exception:
        pass

    sys.exit(0)

if __name__ == "__main__":
    main()

