#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
COSMOS HUB FEED - Génère hub.json et hub.js pour le cockpit ACE777
Usage: python3 hub_cockpit_feed.py
"""

import json
import os
import sys
import urllib.request
from datetime import datetime, timedelta, timezone
from collections import Counter

# Configuration
BASE_DIR = os.path.expanduser("~/prise-ia")
COCKPIT_DIR = os.path.expanduser("~/ace777-test-day1/Index_Maison/cockpit")
HEALTH_URL = "http://127.0.0.1:11435/health"


def safe_read_json(filepath):
    """Lit un fichier JSON en toute sécurité"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return None


def safe_read_jsonl(filepath):
    """Lit un fichier JSONL en toute sécurité"""
    data = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    data.append(json.loads(line.strip()))
                except Exception:
                    continue
    except Exception:
        pass
    return data


def get_health():
    """Récupère la santé du hub"""
    try:
        with urllib.request.urlopen(HEALTH_URL, timeout=2) as response:
            return json.loads(response.read().decode())
    except Exception:
        return None


def main():
    try:
        # Lire les fichiers source
        providers = safe_read_json(os.path.join(BASE_DIR, "providers.json")) or {}
        providers = providers.get("providers", providers) if isinstance(providers, dict) else providers
        usage = safe_read_jsonl(os.path.join(BASE_DIR, "usage.jsonl"))
        routing = safe_read_json(os.path.join(BASE_DIR, "routing.json")) or {}
        events = safe_read_jsonl(os.path.join(BASE_DIR, "hub_events.jsonl"))

        # Calculer les compteurs par provider (24h)
        now = datetime.now(timezone.utc)
        cutoff = now - timedelta(hours=24)
        provider_counts = Counter()
        today_counts = Counter()
        today_str = now.strftime("%Y-%m-%d")

        for call in usage:
            try:
                ts = call.get("ts", "")
                provider = call.get("provider", "")
                kind = call.get("kind", "")

                # Compter les appels 24h
                if ts:
                    try:
                        ts_dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
                        if ts_dt > cutoff:
                            provider_counts[provider] += 1
                    except Exception:
                        pass

                # Compter les appels du jour pour le budget cloud
                if today_str in ts and kind == "cloud":
                    today_counts[provider] += 1
            except Exception:
                continue

        # Budget cloud
        cloud_budget = routing.get("cloud_daily_budget", 480)
        cloud_consumed = sum(today_counts.values())
        cloud_remaining = max(0, cloud_budget - cloud_consumed)

        # File d'attente live (15 derniers appels)
        recent_calls = sorted(usage, key=lambda x: x.get("ts", ""), reverse=True)[:15]

        # Événements récents (10 derniers)
        recent_events = sorted(events, key=lambda x: x.get("ts", ""), reverse=True)[:10]

        # Quotas par tâche
        tasks_quotas = routing.get("tasks", {})

        # Santé du hub
        health = get_health()

        # Préparer les données providers
        providers_data = []
        if isinstance(providers, list):
            for p in providers:
                if not isinstance(p, dict):
                    continue
                pid = p.get("id", "")
                providers_data.append({
                    "id": pid,
                    "name": p.get("name", pid),
                    "kind": p.get("kind", "local"),
                    "model": p.get("model", ""),
                    "enabled": p.get("enabled", True),
                    "timeout": p.get("timeout", 30),
                    "calls_24h": provider_counts.get(pid, 0)
                })

        # Construire le hub data
        hub_data = {
            "generated_at": now.isoformat(),
            "providers": providers_data,
            "budget": {
                "daily": cloud_budget,
                "consumed": cloud_consumed,
                "remaining": cloud_remaining
            },
            "queue": recent_calls,
            "events": recent_events,
            "tasks_quotas": tasks_quotas,
            "health": health
        }

        # Écriture atomique de hub.json
        json_path = os.path.join(COCKPIT_DIR, "hub.json")
        tmp_json = json_path + ".tmp"
        with open(tmp_json, 'w', encoding='utf-8') as f:
            json.dump(hub_data, f, indent=2, ensure_ascii=False)
        os.replace(tmp_json, json_path)

        # Écriture atomique de hub.js
        js_path = os.path.join(COCKPIT_DIR, "hub.js")
        tmp_js = js_path + ".tmp"
        js_content = "window.__HUB__ = " + json.dumps(hub_data, ensure_ascii=False) + ";"
        with open(tmp_js, 'w', encoding='utf-8') as f:
            f.write(js_content)
        os.replace(tmp_js, js_path)

        print(f"OK COSMOS HUB feed généré à {now.isoformat()}")
        print(f"   Providers: {len(providers_data)}, Appels 24h: {sum(provider_counts.values())}")
        print(f"   Budget cloud: {cloud_consumed}/{cloud_budget} consommé")

    except Exception as e:
        print(f"WARN Erreur non fatale: {e}")

    sys.exit(0)


if __name__ == "__main__":
    main()
