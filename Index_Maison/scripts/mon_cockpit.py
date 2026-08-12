#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""mon_cockpit.py — LE COCKPIT DE BUFFY (10/08).

Vue d'ensemble compacte et machine-generée de l'état ACE777, que l'IA
orchestratrice lit en UNE lecture (au lieu de 10 commandes manuelles).

Usage:
    python3 mon_cockpit.py            # vue complete
    python3 mon_cockpit.py --court    # seulement l'essentiel (debut de session)

Source : commandes réelles (launchctl, memory_pressure, hub, fichiers d'état).
Jamais de mémoire, jamais de prose. C'est le prototype de state.json.
"""
import json
import os
import subprocess
import sys
import time
from datetime import datetime, timezone

HUB = "http://127.0.0.1:11435/health"
BASE = os.path.expanduser("~/ace777-test-day1/Index_Maison")
COCKPIT = os.path.join(BASE, "cockpit")
THERMO = os.path.join(BASE, "thermo")
USAGE = os.path.expanduser("~/prise-ia/usage.jsonl")
ROUTING = os.path.expanduser("~/prise-ia/routing.json")


def run(cmd, timeout=6):
    try:
        return subprocess.check_output(cmd, shell=True, text=True,
                                       timeout=timeout).strip()
    except Exception:
        return ""


def services_etat():
    """Tous les services ace777 : vivants (PID) ou charges-planifies."""
    out = run("launchctl list | grep ace777")
    vivants, planifies = [], []
    for line in out.splitlines():
        parts = line.split()
        if len(parts) < 3:
            continue
        pid, name = parts[0], parts[2]
        (vivants if pid != "-" else planifies).append(name)
    return sorted(vivants), sorted(planifies)


def age_minutes(path):
    if not os.path.exists(path):
        return None
    return int((time.time() - os.path.getmtime(path)) / 60)


def hub_sante():
    try:
        import urllib.request
        with urllib.request.urlopen(HUB, timeout=4) as r:
            d = json.loads(r.read().decode())
        return d.get("status"), d.get("providers")
    except Exception:
        return "DOWN", None


def budget_jour():
    """Appels cloud aujourd'hui (usage.jsonl) + budget journalier."""
    try:
        today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
        n = 0
        with open(USAGE, encoding="utf-8") as f:
            for line in f:
                try:
                    if json.loads(line).get("ts", "").startswith(today):
                        n += 1
                except Exception:
                    pass
        budget = None
        try:
            budget = json.load(open(ROUTING)).get("cloud_daily_budget")
        except Exception:
            pass
        return n, budget
    except Exception:
        return "?", None


def mission_etat():
    try:
        d = json.load(open(os.path.join(COCKPIT, "mission.json")))
        return {
            "run": d.get("run"),
            "pnl": d.get("comboPnl"),
            "alert": d.get("alert"),
            "swarm": d.get("swarmCycle"),
        }
    except Exception:
        return {}


def main():
    court = "--court" in sys.argv
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"🛰️  COCKPIT BUFFY — {now}")
    print("=" * 52)

    # 1. SERVICES
    vivants, planifies = services_etat()
    print(f"\n🔧 SERVICES: {len(vivants)} vivants / {len(planifies)} planifies "
          f"(total {len(vivants)+len(planifies)})")
    if not court:
        print(f"   VIVANTS : {', '.join(vivants) if vivants else 'aucun'}")
    else:
        print(f"   {', '.join(vivants) if vivants else 'aucun vivant'}")

    # 2. HUB
    status, providers = hub_sante()
    print(f"\n🧠 HUB: {status} · {providers} providers")

    # 3. RAM
    ram = run("memory_pressure -Q | grep 'free percentage'")
    print(f"💾 RAM: {ram.strip() if ram else '?'}")

    # 4. BUDGET
    appels, budget = budget_jour()
    b = f" ({appels}/{budget})" if budget else ""
    print(f"💰 BUDGET: {appels} appels cloud aujourd'hui{b}")

    # 5. BOTS (mission.json)
    m = mission_etat()
    if m:
        print(f"\n📈 BOTS: run={m.get('run')} · PnL={m.get('pnl')} · "
              f"alerte={m.get('alert')} · swarm={m.get('swarm')}")
    if not court:
        # alpha/beta/hulk dans mission.json si presents
        try:
            d = json.load(open(os.path.join(COCKPIT, "mission.json")))
            for k in ("alpha", "beta", "hulk"):
                if isinstance(d.get(k), dict):
                    v = d[k]
                    print(f"   {k.upper()}: fills={v.get('fills', '?')} "
                          f"state={v.get('state', '?')}")
        except Exception:
            pass

    # 6. FRAICHEUR (fichiers d'etat)
    if not court:
        print("\n⏱️  FRAICHEUR (age en min):")
        for name, path in [("mission.json", os.path.join(COCKPIT, "mission.json")),
                           ("live.json", os.path.join(THERMO, "live.json")),
                           ("cortana_feed.json", os.path.join(THERMO, "cortana_feed.json"))]:
            a = age_minutes(path)
            print(f"   {name}: {'OK ('+str(a)+' min)' if a is not None and a < 60 else ('AGÉ ('+str(a)+' min)' if a is not None else 'absent')}")

    # 7. ANOMALIES simples
    print("\n⚠️  ANOMALIES:")
    anomalies = []
    if status == "DOWN":
        anomalies.append("HUB INJOIGNABLE")
    for name, path in [("mission.json", os.path.join(COCKPIT, "mission.json")),
                       ("live.json", os.path.join(THERMO, "live.json"))]:
        a = age_minutes(path)
        if a is not None and a > 120:
            anomalies.append(f"{name} fige depuis {a} min")
    # services mirofish/bots attendus arretes mais vivants ?
    for name in vivants:
        if name in ("com.ace777.mirofish", "com.ace777.mirofish-front"):
            anomalies.append(f"{name} TOURNE (était arrêté)")
    print("   " + (" | ".join(anomalies) if anomalies else "aucune détectée"))

    # 8. GIT + OUTBOX (court-circuit en mode court)
    if not court:
        dirty = run("git -C ~/ace777-test-day1 status --short | wc -l").strip()
        outbox = run(f"find {os.path.join(BASE, 'OUTBOX_OBSIDIAN')} -maxdepth 1 -type f | wc -l").strip()
        print(f"\n📦 GIT: {dirty} fichiers non commits · OUTBOX: {outbox} fichiers en attente")

    print("\n" + "=" * 52)
    return 0


if __name__ == "__main__":
    sys.exit(main())
