#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Analyse usage du hub Prise IA — rapport de sante + suggestions.

Lit usage.jsonl + hub_events.jsonl + routing.json (~/prise-ia) et produit :
  1. Vue d'ensemble : appels totaux, split local/cloud, par jour
  2. Par tache : appels, local vs cloud, quota configure, taux cloud
  3. Routage par complexite : distribution des longueurs SIMPLE/COMPLEXE -> suggestion de seuil
  4. Fiabilite : failovers, erreurs, quotas atteints
  5. Suggestions (a appliquer apres GO humain — loi 3)

Zero dependance (stdlib uniquement), comme le hub.

Usage :
    python3 analyse_usage.py                  # 7 derniers jours, rapport console
    python3 analyse_usage.py --days 1         # aujourd'hui seulement
    python3 analyse_usage.py --days 14 --write   # + ecrit un rapport .md dans le vault

Pour tester sans toucher aux donnees reelles, passer des chemins en arguments
positionnels (usage.jsonl, hub_events.jsonl, routing.json).
"""
import argparse
import json
import os
import re
import sys
from datetime import datetime, timedelta, timezone
from statistics import median

ROOT = os.path.expanduser("~/prise-ia")
USAGE_PATH = os.path.join(ROOT, "usage.jsonl")
EVENTS_PATH = os.path.join(ROOT, "hub_events.jsonl")
ROUTING_PATH = os.path.join(ROOT, "routing.json")
VAULT = os.path.expanduser("~/Documents/Obsidian_ACE777")
REPORT_DIR = os.path.join(VAULT, "AUTO_EVOL")

ROUTING_RE = re.compile(
    r"Complexite:\s*(SIMPLE|COMPLEXE)\s*\((\d+)\s*car\.\)\s*(?:mais budget cloud atteint\s*)?->\s*(local|cloud)"
)


def load_jsonl(path):
    """Charge un fichier JSONL en tolerant les lignes invalides."""
    rows = []
    if not os.path.exists(path):
        return rows
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except Exception:
                continue
    return rows


def parse_ts(ts):
    try:
        dt = datetime.fromisoformat(ts)
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt
    except Exception:
        return None


def build_report(usage_path, events_path, routing_path, days):
    now = datetime.now(timezone.utc)
    since = now - timedelta(days=days)

    usage = [e for e in load_jsonl(usage_path) if (t := parse_ts(e.get("ts", ""))) and t >= since]
    events = [e for e in load_jsonl(events_path) if (t := parse_ts(e.get("ts", ""))) and t >= since]

    routing = {}
    if os.path.exists(routing_path):
        try:
            with open(routing_path) as f:
                routing = json.load(f)
        except Exception:
            routing = {}
    tasks_cfg = routing.get("tasks", {})

    lines = []
    add = lines.append

    # ---------- 1. Vue d'ensemble ----------
    add("=" * 62)
    add("ANALYSE USAGE — hub Prise IA")
    add(f"Periode : {since:%Y-%m-%d %H:%M} -> {now:%Y-%m-%d %H:%M} UTC ({days} j)")
    add("=" * 62)

    total = len(usage)
    n_local = sum(1 for e in usage if e.get("kind") == "local")
    n_cloud = sum(1 for e in usage if e.get("kind") == "cloud")
    add(f"\nAppels totaux : {total}  (local {n_local} · cloud {n_cloud})")
    if total:
        add(f"Taux cloud    : {100.0 * n_cloud / total:.0f}%")

    # par jour
    per_day = {}
    for e in usage:
        day = e.get("ts", "")[:10]
        per_day.setdefault(day, {"local": 0, "cloud": 0})
        per_day[day][e.get("kind", "?")] = per_day[day].get(e.get("kind", "?"), 0) + 1
    if per_day:
        add("\nPar jour :")
        for day in sorted(per_day):
            d = per_day[day]
            add(f"  {day}  local {d.get('local', 0):>3} · cloud {d.get('cloud', 0):>3}")

    # ---------- 2. Par tache ----------
    per_task = {}
    for e in usage:
        t = e.get("task") or "auto"
        per_task.setdefault(t, {"local": 0, "cloud": 0})
        per_task[t][e.get("kind", "?")] = per_task[t].get(e.get("kind", "?"), 0) + 1

    if per_task:
        add("\nPar tache :")
        add(f"  {'Tache':<22} {'Total':>5} {'Local':>6} {'Cloud':>6} {'Quota':>6}  Remarque")
        for t in sorted(per_task, key=lambda k: -sum(per_task[k].values())):
            s = per_task[t]
            tot = s["local"] + s["cloud"]
            cfg = tasks_cfg.get(t, {})
            quota = cfg.get("cloud_quota", "-")
            remark = ""
            if not cfg and tot and s["cloud"]:
                remark = "appel sans tache (model force ?)"
            elif cfg.get("provider", "").startswith("gemini") and tot and s["cloud"] == 0:
                remark = "config cloud mais 0 appel cloud ?"
            add(f"  {t:<22} {tot:>5} {s['local']:>6} {s['cloud']:>6} {str(quota):>6}  {remark}")
    else:
        add("\nPar tache : (aucune donnee sur la periode)")

    # ---------- 3. Routage par complexite ----------
    add("\nRoutage par complexite (evenements routing) :")
    routing_stats = {}
    for ev in events:
        if ev.get("kind") != "routing":
            continue
        m = ROUTING_RE.search(ev.get("title", ""))
        if not m:
            continue
        kind_r, length = m.group(1), int(m.group(2))
        task = ev.get("detail") or "?"
        routing_stats.setdefault(task, {"simple": [], "complex": []})
        bucket = "simple" if kind_r == "SIMPLE" else "complex"
        routing_stats[task][bucket].append(length)

    if not routing_stats:
        add("  (aucun evenement routing sur la periode)")
    for task in sorted(routing_stats):
        st = routing_stats[task]
        cfg = tasks_cfg.get(task, {})
        th = cfg.get("complexity_threshold", 600)
        s_list, c_list = st["simple"], st["complex"]
        s_min = min(s_list) if s_list else "-"
        s_max = max(s_list) if s_list else "-"
        c_min = min(c_list) if c_list else "-"
        c_max = max(c_list) if c_list else "-"
        add(f"  {task} (seuil {th}): "
            f"SIMPLE n={len(s_list)} [{s_min}-{s_max}] · COMPLEXE n={len(c_list)} [{c_min}-{c_max}]")
        if len(c_list) >= 3 and len(s_list) >= 3:
            med_c = median(c_list)
            margin = max(10, int(th * 0.1))
            if c_min - th <= margin:
                add(f"    💡 suggestion : seuil {th} -> ~{med_c} (des complexes collent au seuil, debut a {c_min})")
            elif th - s_max <= margin:
                add(f"    ℹ️  a surveiller : des simples montent jusqu a {s_max}, proche du seuil {th}")
            else:
                add(f"    ✅ seuil bien calibre : simples <= {s_max} < seuil {th} <= complexes")

    # ---------- 4. Fiabilite ----------
    kinds = {}
    for ev in events:
        k = ev.get("kind", "?")
        kinds[k] = kinds.get(k, 0) + 1
    add("\nEvenements (par type) :")
    if kinds:
        for k in sorted(kinds, key=lambda x: -kinds[x]):
            add(f"  {k:<10} {kinds[k]}")
    else:
        add("  (aucun)")
    n_fail = kinds.get("failover", 0) + kinds.get("error", 0)
    n_quota = kinds.get("quota", 0)
    if n_fail:
        add(f"\n⚠️  {n_fail} bascule(s)/erreur(s) sur la periode — verifier la fiabilite des fournisseurs.")
    if n_quota:
        add(f"⚠️  {n_quota} repli(s) budget cloud atteint.")

    # ---------- 5. Suggestions ----------
    add("\n" + "=" * 62)
    add("SUGGESTIONS (a appliquer apres GO humain — loi 3)")
    add("=" * 62)
    any_sugg = False
    if n_quota:
        add(f"  · Budget cloud atteint {n_quota}x — envisager d'augmenter cloud_daily_budget ou de baisser le seuil de complexite.")
        any_sugg = True
    if not total:
        add("  · Aucun appel sur la periode — le hub est-il sollicite ?")
        any_sugg = True
    elif n_cloud == 0 and any(tasks_cfg.get(t, {}).get("provider", "").startswith("gemini") for t in per_task):
        add("  · Aucun appel cloud alors que des taches sont configurees Gemini — verifier les cles/failover.")
        any_sugg = True
    if not any_sugg:
        add("  · Aucune suggestion automatique — la config semble saine. A revoir a la prochaine periode.")
    add("")
    add("Note : usage.jsonl loggue des compteurs d'appels, pas les tokens/couts reels.")
    add("Pour un vrai pilotage par cout, enrichir log_usage() avec les metadonnees de usage des fournisseurs (piste).")

    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description="Analyse usage du hub Prise IA")
    ap.add_argument("--days", type=int, default=7, help="nombre de jours a analyser (defaut 7)")
    ap.add_argument("--write", action="store_true", help="ecrit le rapport dans le vault (AUTO_EVOL)")
    ap.add_argument("paths", nargs="*", help="optionnel : usage.jsonl hub_events.jsonl routing.json (tests)")
    args = ap.parse_args()

    usage_path = args.paths[0] if len(args.paths) > 0 else USAGE_PATH
    events_path = args.paths[1] if len(args.paths) > 1 else EVENTS_PATH
    routing_path = args.paths[2] if len(args.paths) > 2 else ROUTING_PATH

    report = build_report(usage_path, events_path, routing_path, args.days)
    print(report)

    if args.write:
        # TCC macOS protege ~/Documents (le vault) : si launchd ne peut pas y ecrire,
        # on bascule sur ~/prise-ia/reports/ (non protege) — rapport toujours genere.
        fname = None
        for dest in (REPORT_DIR, os.path.join(ROOT, "reports")):
            try:
                os.makedirs(dest, exist_ok=True)
                fname = os.path.join(dest, f"ANALYSE_USAGE_{datetime.now(timezone.utc):%Y-%m-%d}.md")
                with open(fname, "w") as f:
                    f.write("# Analyse usage hub Prise IA\n\n```text\n" + report + "\n```\n")
                break
            except Exception as e:
                print(f"\n(echec ecriture {dest}: {e})")
                fname = None
        if fname:
            print(f"\nRapport ecrit : {fname}")
        else:
            print("\n⚠️  Rapport non ecrit (aucun emplacement accessible).")


if __name__ == "__main__":
    main()
