# RÉPONSE CODEUR (task code.ia · Mistral La Plateforme (essai gratuit) · 10.4s) — 2026-08-18T21:18:06.991788+00:00Z

```python
# auto_reparer.py
import json
import os
import subprocess
import time
from datetime import datetime, timedelta

# Configuration
WHITELIST_SERVICES = [
    "com.ace777.whales",
    "com.ace777.pont-onchain",
    "com.ace777.cpfp",
    "com.ace777.veilleuse",
    "com.ace777.hub-cockpit-feed",
    "com.ace777.cockpit-pont",
    "com.ace777.saison"
]

MAX_ATTEMPTS = 3
COOLDOWN_MINUTES = 10
LOG_FILE = "thermo/reparations.log"
COOLDOWN_FILE = "thermo/cooldown.json"

def load_json(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_json(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

def check_kill_switch():
    kill_switch = load_json("alarme.json").get("STOP", False)
    maintenance = load_json("alarme.json").get("MAINTENANCE_PREVUE", False)
    return kill_switch or maintenance

def check_cooldown():
    cooldown_data = load_json(COOLDOWN_FILE)
    last_repair = cooldown_data.get("last_repair", 0)
    cooldown_until = last_repair + COOLDOWN_MINUTES * 60
    return time.time() < cooldown_until

def update_cooldown():
    cooldown_data = {"last_repair": time.time()}
    save_json(cooldown_data, COOLDOWN_FILE)

def log_repair(service, action, status):
    timestamp = datetime.now().isoformat()
    log_entry = {
        "timestamp": timestamp,
        "service": service,
        "action": action,
        "status": status
    }
    with open(LOG_FILE, 'a') as f:
        json.dump(log_entry, f)
        f.write('\n')

def repair_service(service):
    if service not in WHITELIST_SERVICES:
        return False

    attempts = load_json(LOG_FILE).get(service, {}).get("attempts", 0)
    if attempts >= MAX_ATTEMPTS:
        return False

    # Announce repair attempt
    subprocess.run(["say", f"Tentative de réparation pour {service}"])

    # Try to restart the service
    try:
        subprocess.run(["launchctl", "kickstart", "-k", f"gui/{os.getuid()}/{service}"], check=True)
        status = "success"
    except subprocess.CalledProcessError:
        status = "failed"

    # Log the repair attempt
    log_repair(service, "restart", status)

    # Announce repair result
    subprocess.run(["say", f"Réparation pour {service} terminée avec {status}"])

    return status == "success"

def auto_reparer():
    if check_kill_switch():
        return

    if check_cooldown():
        return

    sante_data = load_json("thermo/sante_index.json")
    for service, status in sante_data.items():
        if status == "cassé" and service in WHITELIST_SERVICES:
            if repair_service(service):
                update_cooldown()
                break

if __name__ == "__main__":
    auto_reparer()
```

```python
# verifier_whales.py
import json
import subprocess

def load_json(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def check_whales_chain():
    # Check if surveiller_whales.py is updating whales_scan_latest.json
    whales_data = load_json("whales_scan_latest.json")
    if not whales_data:
        return False

    # Check if live.json.onchain is updated
    onchain_data = load_json("live.json.onchain")
    if not onchain_data:
        return False

    # Check if alarme.json is updated
    alarme_data = load_json("alarme.json")
    if not alarme_data:
        return False

    return True

def alert_human():
    subprocess.run(["say", "Alerte : Chaîne de surveillance des baleines cassée"])
    # Update cockpit display
    with open("cockpit/sante_live.js", 'a') as f:
        f.write("alert('Alerte : Chaîne de surveillance des baleines cassée');\n")

def verifier_whales():
    if not check_whales_chain():
        alert_human()

if __name__ == "__main__":
    verifier_whales()
```

```python
# rappels.py
import json
import subprocess
from datetime import datetime, timedelta

RAPPELS_FILE = "thermo/rappels.json"

def load_json(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_json(data, file_path):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)

def ajouter_rappel(tache, heure):
    rappels = load_json(RAPPELS_FILE)
    rappel = {
        "tache": tache,
        "heure": heure,
        "timestamp": datetime.now().isoformat()
    }
    rappels.append(rappel)
    save_json(rappels, RAPPELS_FILE)

def lister_rappels():
    rappels = load_json(RAPPELS_FILE)
    for rappel in rappels:
        print(f"{rappel['tache']} à {rappel['heure']}")

def supprimer_rappel(tache, heure):
    rappels = load_json(RAPPELS_FILE)
    rappels = [r for r in rappels if not (r["tache"] == tache and r["heure"] == heure)]
    save_json(rappels, RAPPELS_FILE)

def verifier_rappels():
    rappels = load_json(RAPPELS_FILE)
    now = datetime.now()
    for rappel in rappels:
        rappel_time = datetime.strptime(rappel["heure"], "%H:%M")
        rappel_time = now.replace(hour=rappel_time.hour, minute=rappel_time.minute, second=0, microsecond=0)
        if now >= rappel_time:
            subprocess.run(["say", f"Rappel : {rappel['tache']}"])
            # Update cockpit display
            with open("cockpit/sante_live.js", 'a') as f:
                f.write(f"alert('Rappel : {rappel['tache']}');\n")
            supprimer_rappel(rappel["tache"], rappel["heure"])

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "ajouter" and len(sys.argv) > 3:
            ajouter_rappel(sys.argv[2], sys.argv[3])
        elif command == "lister":
            lister_rappels()
        elif command == "supprimer" and len(sys.argv) > 3:
            supprimer_rappel(sys.argv[2], sys.argv[3])
        elif command == "verifier":
            verifier_rappels()
```
