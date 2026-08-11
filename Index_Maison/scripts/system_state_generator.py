#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""system_state_generator.py — v2.1 (SPEC V2.1 validée famille 10/08).

Génère state.json : la mémoire mécanique de la COUCHE SYSTÈME (la 3e, après
mission.json pour le trading et cortana_feed.json pour le vocal).

LOI DU BRUT (gravé dans la spec) : la machine ECRIT le brut, l'IA LIT le brut,
PERSONNE n'interprète entre les deux.
=> state.json ne contient AUCUNE prose, AUCUN résumé, AUCUNE interprétation.
   Uniquement des mesures brutes : timestamps, compteurs, status, hashs.
   Toute transformation éventuelle ira dans une couche analysis/ séparée.

Réserve famille P1 (GEMINI + JUGE) :
  - "status" : HEALTHY | STALE | DEGRADED (seuils mesurés)
  - "feed_hash" : SHA-256 des 4 feeds agrégés (ordre fixe)
  - load_json_safe() : un feed corrompu est ignoré, jamais bloquant

Écriture ATOMIQUE : .tmp puis os.replace() — jamais de state.json corrompu.

Usage:
    python3 system_state_generator.py            # écrit state.json (cadence 2 min via plist)
    python3 system_state_generator.py --check    # lit state.json et affiche status/hash
    python3 system_state_generator.py --dry-run  # calcule sans écrire
"""
import hashlib
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone

BASE = os.path.expanduser("~/ace777-test-day1/Index_Maison")
SYSTEM_DIR = os.path.join(BASE, "system")
STATE_PATH = os.path.join(SYSTEM_DIR, "state.json")
COCKPIT = os.path.join(BASE, "cockpit")
THERMO = os.path.join(BASE, "thermo")
ROUTING = os.path.expanduser("~/prise-ia/routing.json")
HUB_HEALTH = "http://127.0.0.1:11435/health"

# Ordre FIXE des feeds pour le hash (réserve famille : "ordre fixe")
FEEDS = [
    ("mission", os.path.join(COCKPIT, "mission.json")),
    ("cortana_feed", os.path.join(THERMO, "cortana_feed.json")),
    ("live", os.path.join(THERMO, "live.json")),
    ("routing", ROUTING),
]

# Seuils de fraîcheur (réserve famille P1, validés) :
# live.json est temps réel (5 s) -> 15 s max. Les autres -> 2 min.
FRESH_SECONDS = {"live": 15, "mission": 120, "cortana_feed": 120, "routing": 120}

# Dossiers hors zone (contrôle de PRÉSENCE léger, réserve P5 — métadonnées
# uniquement, jamais de lecture récursive).
HORS_ZONE = {
    "mirofis": os.path.expanduser("~/mirofis"),
    "crypto_voice_core": os.path.expanduser("~/crypto-voice-assistant-core"),
    "archives_brutes": os.path.expanduser("~/ACE777_ARCHIVES_BRUTES_DONNEES"),
    "vocal_hors_vault": os.path.expanduser("~/Assistant_Vocal_HORS_VAULT"),
    "obsidian_backups": os.path.expanduser("~/Obsidian_BACKUPS_HORS_VAULT"),
}


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def load_json_safe(path):
    """Réserve P1-4 : un feed corrompu est ignoré, jamais bloquant."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def age_seconds(path):
    if not os.path.exists(path):
        return None
    return int(time.time() - os.path.getmtime(path))


def compute_status(feeds):
    """Réserve P1-1 : HEALTHY / STALE / DEGRADED selon la fraîcheur."""
    any_missing = False
    any_stale = False
    for name, path in FEEDS:
        present = feeds.get(name) is not None
        if not present:
            any_missing = True
            continue
        age = age_seconds(path)
        if age is None or age > FRESH_SECONDS.get(name, 120):
            any_stale = True
    if any_missing:
        return "DEGRADED"
    if any_stale:
        return "STALE"
    return "HEALTHY"


def compute_feed_hash(feeds):
    """Réserve P1-2 : SHA-256 des 4 feeds agrégés dans l'ordre fixe."""
    h = hashlib.sha256()
    for name, _path in FEEDS:
        data = feeds.get(name)
        if data is None:
            h.update(b"<absent>")
        else:
            h.update(json.dumps(data, sort_keys=True, ensure_ascii=False).encode())
    return h.hexdigest()


def run(cmd, timeout=6):
    try:
        return subprocess.check_output(cmd, shell=True, text=True,
                                       timeout=timeout).strip()
    except Exception:
        return ""


def services_etat():
    """Brut : vivants (PID) vs planifiés (-) — même logique que mon_cockpit."""
    out = run("launchctl list | grep ace777")
    vivants, planifies = [], []
    for line in out.splitlines():
        parts = line.split()
        if len(parts) < 3:
            continue
        pid, name = parts[0], parts[2]
        (vivants if pid != "-" else planifies).append(name)
    return sorted(vivants), sorted(planifies)


def hub_sante():
    """Brut : {"status": "ok", "providers": N} ou null."""
    try:
        import urllib.request
        with urllib.request.urlopen(HUB_HEALTH, timeout=4) as r:
            return json.loads(r.read().decode())
    except Exception:
        return None


def generate_state():
    """Construit le state brut. Ne lève JAMAIS (loi non-fatale)."""
    feeds = {name: load_json_safe(path) for name, path in FEEDS}
    vivants, planifies = services_etat()
    hub = hub_sante()
    ram = run("memory_pressure 2>/dev/null | head -2")

    # Présence des dossiers hors zone : métadonnées uniquement (réserve P5)
    hors_zone = {}
    for name, path in HORS_ZONE.items():
        try:
            present = os.path.isdir(path)
            hors_zone[name] = {"present": present}
        except Exception:
            hors_zone[name] = {"present": False}

    # Backup check (E2) : lit les 2 bruts produits par backup_light_check.sh
    # (presence chaque run + tailles du -sk espacees 6 h) — jamais bloquant.
    backup_presence = load_json_safe(os.path.join(SYSTEM_DIR, "backup_presence.json"))
    backup_sizes = load_json_safe(os.path.join(SYSTEM_DIR, "backup_sizes.json"))
    backup_light = {
        "presence": (backup_presence or {}).get("present", {}),
        "sizes_ko": (backup_sizes or {}).get("sizes_ko", {}),
        "presence_at": (backup_presence or {}).get("generated_at"),
        "sizes_at": (backup_sizes or {}).get("generated_at"),
    }

    state = {
        "timestamp": now_iso(),
        "generation_source": "system_state_generator.py v2.1",
        "status": compute_status(feeds),
        "feed_hash": compute_feed_hash(feeds),
        "feeds": {
            name: {
                "present": feeds.get(name) is not None,
                "age_seconds": age_seconds(path),
                "fresh_limit_s": FRESH_SECONDS.get(name, 120),
            }
            for name, path in FEEDS
        },
        "services": {
            "total": len(vivants) + len(planifies),
            "running": len(vivants),
            "planned": len(planifies),
            "running_list": vivants,
            "planned_list": planifies,
        },
        "hub": hub,
        "ram_raw": ram or None,
        "hors_zone": hors_zone,
        "backup_light": backup_light,
    }
    return state


def write_atomic(state):
    """Écriture ATOMIQUE : .tmp puis os.replace() (jamais de fichier corrompu)."""
    os.makedirs(SYSTEM_DIR, exist_ok=True)
    tmp = STATE_PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)
        f.write("\n")
    os.replace(tmp, STATE_PATH)


def verify_hash(state):
    """Réserve P1-3 : vérifie que le feed_hash du state correspond aux feeds actuels."""
    feeds = {name: load_json_safe(path) for name, path in FEEDS}
    return state.get("feed_hash") == compute_feed_hash(feeds)


def main():
    if "--check" in sys.argv:
        try:
            with open(STATE_PATH, encoding="utf-8") as f:
                s = json.load(f)
        except Exception as e:
            print("state.json illisible: %s" % e)
            return 2
        print("status: %s" % s.get("status"))
        print("timestamp: %s" % s.get("timestamp"))
        print("feed_hash: %s" % s.get("feed_hash"))
        print("hash valide maintenant: %s" % verify_hash(s))
        print("services: %d (running %d / planned %d)"
              % (s.get("services", {}).get("total", 0),
                 s.get("services", {}).get("running", 0),
                 s.get("services", {}).get("planned", 0)))
        return 0

    state = generate_state()
    if "--dry-run" in sys.argv:
        print(json.dumps(state, ensure_ascii=False, indent=2))
        return 0

    write_atomic(state)
    print("[OK] state.json ecrit (%d o) — status=%s — %s"
          % (os.path.getsize(STATE_PATH), state["status"], state["timestamp"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
