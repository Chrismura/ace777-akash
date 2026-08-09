#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# surveillance_quotas.py — ecrit par GEMINI (delegation Ada, loi 1quinquies)
# Etape 2 Phase 0 : remplace la jauge supprimee (surveillance minimale quotas).
#!/usr/bin/env python3
import os
import json
import sys
from datetime import datetime, timezone
from collections import defaultdict

HOME = os.path.expanduser("~")
BASE_DIR = os.path.join(HOME, "prise-ia")
USAGE_FILE = os.path.join(BASE_DIR, "usage.jsonl")
PROVIDERS_FILE = os.path.join(BASE_DIR, "providers.json")
REPORT_DIR = os.path.join(BASE_DIR, "reports")
LOG_FILE = os.path.join(REPORT_DIR, "SURVEILLANCE_QUOTAS.log")

def read_json_file(path, description):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"ERREUR: {description} introuvable: {path}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"ERREUR: {description} invalide: {path} - {e}", file=sys.stderr)
        sys.exit(1)
    except OSError as e:
        print(f"ERREUR: impossible de lire {description}: {path} - {e}", file=sys.stderr)
        sys.exit(1)

def read_usage_file():
    entries = []
    if not os.path.exists(USAGE_FILE):
        print(f"ERREUR: fichier usage.jsonl introuvable: {USAGE_FILE}", file=sys.stderr)
        sys.exit(1)
    try:
        with open(USAGE_FILE, "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    entries.append(json.loads(line))
                except json.JSONDecodeError as e:
                    print(f"ERREUR: ligne {line_num} invalide dans usage.jsonl: {e}", file=sys.stderr)
                    sys.exit(1)
    except OSError as e:
        print(f"ERREUR: impossible de lire usage.jsonl: {e}", file=sys.stderr)
        sys.exit(1)
    return entries

def main():
    providers_data = read_json_file(PROVIDERS_FILE, "providers.json")
    providers_list = providers_data.get("providers", [])
    if not isinstance(providers_list, list):
        print("ERREUR: providers.json doit contenir une liste 'providers'", file=sys.stderr)
        sys.exit(1)

    active_providers = {}
    for p in providers_list:
        if not isinstance(p, dict):
            continue
        pid = p.get("id") or p.get("name")
        if pid and p.get("enabled", True):
            active_providers[str(pid)] = True

    entries = read_usage_file()
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    today_entries = []
    for e in entries:
        ts = e.get("ts", "")
        if isinstance(ts, str) and ts.startswith(today):
            today_entries.append(e)

    provider_stats = defaultdict(lambda: {"appels": 0, "echecs": 0, "recent_errors": []})
    for e in today_entries:
        provider = e.get("provider")
        if not provider:
            continue
        provider = str(provider)
        if provider not in active_providers:
            continue
        stats = provider_stats[provider]
        stats["appels"] += 1
        status = e.get("status", "ok")
        error = e.get("error")
        if status != "ok" or error:
            stats["echecs"] += 1
            stats["recent_errors"].append(e)

    alerts = []
    for provider, stats in provider_stats.items():
        appels = stats["appels"]
        echecs = stats["echecs"]
        recent_errors = stats["recent_errors"]
        recent_count = len(recent_errors)
        last_10 = [e for e in today_entries if str(e.get("provider")) == provider][-10:]
        last_10_errors = sum(1 for e in last_10 if e.get("status", "ok") != "ok" or e.get("error"))
        rate = last_10_errors / len(last_10) if last_10 else 0

        if recent_count >= 2 or (len(last_10) >= 2 and rate > 0.5):
            alerts.append((provider, appels, echecs))

    if alerts:
        try:
            os.makedirs(REPORT_DIR, exist_ok=True)
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                for provider, appels, echecs in alerts:
                    ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
                    f.write(f"[{ts}] ALERTE provider={provider} appels={appels} echecs={echecs}\n")
        except OSError as e:
            print(f"ERREUR: impossible d'écrire le log: {e}", file=sys.stderr)
            sys.exit(1)

    print(f"SURVEILLANCE QUOTAS - {today}")
    if not active_providers:
        print("Aucun provider actif configuré")
        return

    for provider in active_providers:
        stats = provider_stats.get(provider, {"appels": 0, "echecs": 0})
        appels = stats["appels"]
        echecs = stats["echecs"]
        if echecs >= 3 or (appels > 0 and echecs / appels > 0.5):
            etat = "MORT"
        elif echecs >= 1:
            etat = "FAIBLE"
        else:
            etat = "OK"
        print(f"{provider}: {appels} appels, {echecs} echecs, {etat}")

if __name__ == "__main__":
    main()
