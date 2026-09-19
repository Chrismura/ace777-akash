#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ROUTEUR AUTO (gouvernance du hub) — spec niveau 3, 13/08
=========================================================
Objectif : que le routage tourne TOUT SEUL, sans editer routing.json a la main,
et qu'il tienne pendant les tempetes.

Principes (valides avec Christophe, 13/08) :
  - AUTO avec filet de securite : backup avant ecriture + rollback auto.
  - LENT et CONSERVATEUR : le backoff progressif du hub gere l'urgence (par requete),
    le routeur gere l'optimisation tranquille (par cycle). Deux echelles de temps.
  - Fenetre de mesure glissante (12-24h), seuil de confiance, max 1 changement/cycle.
  - Ne JAMAIS reagir a une mesure isolee (pendant une tempete un bon provider peut
    etre lent 30 min — on ne le retrograde pas sur cette base).

Mesures par provider (fenetre glissante) :
  - Dispo  : succes / tentatives (usage.jsonl vs events « Bascule depuis »)
  - Vitesse: duree moyenne des reponses (duration_s, ajoute au hub le 13/08)
  - Justesse: optionnelle — si un score par (task, provider) existe, il est integre
              (ex. analyses journalisees -> score_justesse, a brancher plus tard)

Sortie : reecrit routing.json (providers reordonnes par task) avec backup + audit.
Rollback : si au cycle suivant le provider prome est moins bon que l'ancien,
           on restaure automatiquement le backup.
"""

import json
import os
import sys
from collections import defaultdict
from datetime import datetime, timedelta, timezone

ROOT = os.path.dirname(os.path.abspath(__file__))
ROUTING_PATH = os.path.join(ROOT, "routing.json")
PROVIDERS_PATH = os.path.join(ROOT, "providers.json")
USAGE_PATH = os.path.join(ROOT, "usage.jsonl")
EVENTS_PATH = os.path.join(ROOT, "hub_events.jsonl")
BACKUP_DIR = os.path.join(ROOT, "backups_routing")
AUDIT_PATH = os.path.join(ROOT, "routeur_auto_audit.jsonl")

# Fenetre de mesure glissante (heures) — assez long pour ignorer les tempetes courtes
WINDOW_H = 24
# Seuil de confiance : il faut au moins N echantillons sur cette task pour comparer
MIN_SAMPLES = 5
# Ecart de score minimal pour justifier un changement (points sur 100)
MIN_DELTA = 15
# Max 1 changement par cycle — jamais de bouleversement en une passe
MAX_CHANGES_PER_CYCLE = 1


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def load_json(path):
    try:
        with open(path) as f:
            return json.load(f)
    except Exception:
        return None


def provider_id_to_name(providers):
    """Mapping id -> nom affiche (pour croiser usage.jsonl et events)."""
    return {p.get("id"): p.get("name") for p in providers}


def read_window(path, hours):
    cutoff = datetime.now(timezone.utc) - timedelta(hours=hours)
    out = []
    if not os.path.exists(path):
        return out
    with open(path) as f:
        for line in f:
            try:
                ev = json.loads(line)
            except Exception:
                continue
            ts = ev.get("ts", "")
            try:
                t = datetime.fromisoformat(ts)
            except Exception:
                continue
            if t >= cutoff:
                out.append(ev)
    return out


def mesure(providers):
    """Retourne stats par (task, provider) et par provider (global)."""
    id2name = provider_id_to_name(providers)
    usage = read_window(USAGE_PATH, WINDOW_H)
    events = read_window(EVENTS_PATH, WINDOW_H)

    # --- succes par (task, provider) avec duree ---
    succ = defaultdict(lambda: {"n": 0, "dur": 0.0})
    succ_global = defaultdict(lambda: {"n": 0, "dur": 0.0})
    for ev in usage:
        pid = ev.get("provider")
        task = ev.get("task", "?")
        dur = ev.get("duration_s")
        if not pid:
            continue
        succ[(task, pid)]["n"] += 1
        if dur is not None:
            succ[(task, pid)]["dur"] += dur
            succ_global[pid]["n"] += 1
            succ_global[pid]["dur"] += dur

    # --- echecs : « Bascule depuis <nom> » = le provider precedent a echoue ---
    echec_global = defaultdict(int)
    echec_task = defaultdict(int)
    for ev in events:
        title = ev.get("title", "")
        if not title.startswith("Bascule depuis "):
            continue
        name = title[len("Bascule depuis "):].strip()
        # retrouver le provider id a partir du nom
        for pid, pname in id2name.items():
            if name.startswith(pname):
                echec_global[pid] += 1
                break

    stats = {}
    # global par provider
    for pid in succ_global:
        n = succ_global[pid]["n"]
        dur = succ_global[pid]["dur"]
        d_avg = dur / n if n else None
        dispo = n / (n + echec_global.get(pid, 0)) * 100 if (n + echec_global.get(pid, 0)) else None
        stats[pid] = {"samples": n, "dur_avg": d_avg, "echecs": echec_global.get(pid, 0), "dispo": dispo}
    # par task
    for (task, pid), s in succ.items():
        n = s["n"]
        d_avg = s["dur"] / n if n else None
        stats[(task, pid)] = {"samples": n, "dur_avg": d_avg, "echecs": echec_task.get(pid, 0),
                              "dispo": n / (n + echec_task.get(pid, 0)) * 100 if (n + echec_task.get(pid, 0)) else None}
    return stats


def score(st):
    """Score composite sur 100 : dispo (60) + vitesse (40)."""
    dispo = st.get("dispo") if st.get("dispo") is not None else 100.0
    dur = st.get("dur_avg")
    if dur is None:
        vit = 70.0  # pas de mesure de duree -> neutre
    else:
        # <15s = excellent, 15-60 = bon, >120 = mauvais (echelle douce)
        vit = max(0.0, 100.0 - (dur - 10) * 0.8)
        vit = min(100.0, vit)
    return 0.6 * dispo + 0.4 * vit


def decide(routing, providers, stats):
    """Compare le provider actuel de chaque task avec les alternatives mesurees.
    Retourne la liste des changements proposes (max MAX_CHANGES_PER_CYCLE)."""
    id2name = provider_id_to_name(providers)
    changes = []
    for task, rule in routing.get("tasks", {}).items():
        cur = rule.get("provider")
        if not cur:
            continue
        # candidates : tous les providers actifs ayant >= MIN_SAMPLES sur cette task
        candidates = {}
        for k, st in stats.items():
            if not isinstance(k, tuple):
                continue
            t, pid = k
            if t == task and st.get("samples", 0) >= MIN_SAMPLES and pid != cur:
                candidates[pid] = st
        if not candidates:
            continue
        cur_st = stats.get((task, cur))
        cur_score = score(cur_st) if cur_st else None
        # meilleur candidat
        best = max(candidates.items(), key=lambda kv: score(kv[1]))
        best_pid, best_st = best
        best_score = score(best_st)
        if cur_score is None:
            continue
        delta = best_score - cur_score
        if delta >= MIN_DELTA:
            changes.append({
                "task": task,
                "de": cur,
                "vers": best_pid,
                "score_actuel": round(cur_score, 1),
                "score_propose": round(best_score, 1),
                "delta": round(delta, 1),
                "echantillons": best_st.get("samples"),
            })
    # trier par delta decroissant, garder max 1
    changes.sort(key=lambda c: -c["delta"])
    return changes[:MAX_CHANGES_PER_CYCLE]


def rollback_if_degrade(routing, providers, stats):
    """Verifie si un changement recent (trace dans l'audit) s'est degrade.
    Retourne le backup a restaurer, ou None."""
    if not os.path.exists(AUDIT_PATH):
        return None
    # dernier changement applique
    last = None
    with open(AUDIT_PATH) as f:
        for line in f:
            try:
                ev = json.loads(line)
            except Exception:
                continue
            if ev.get("action") == "change" and ev.get("statut") == "applique":
                last = ev
    if not last:
        return None
    # le changement est stocke dans detail (task, de, vers, score_actuel)
    detail = last.get("detail", {})
    if not isinstance(detail, dict):
        return None
    pid = detail.get("vers")
    task = detail.get("task")
    st = stats.get((task, pid))
    if not st or st.get("samples", 0) < MIN_SAMPLES:
        return None
    new_score = score(st)
    old_score = detail.get("score_actuel", 0)
    if new_score < old_score - 10:  # degrade de plus de 10 pts -> rollback
        return detail
    return None


def audit(action, statut, detail):
    ev = {"ts": now_iso(), "action": action, "statut": statut, "detail": detail}
    try:
        with open(AUDIT_PATH, "a") as f:
            f.write(json.dumps(ev, ensure_ascii=False) + "\n")
    except Exception:
        pass


def backup_routing():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    dst = os.path.join(BACKUP_DIR, f"routing.{ts}.bak.json")
    with open(ROUTING_PATH) as f:
        data = f.read()
    with open(dst, "w") as f:
        f.write(data)
    return dst


def main():
    providers = load_json(PROVIDERS_PATH)
    routing = load_json(ROUTING_PATH)
    if not providers or not routing:
        print("ERREUR: providers.json ou routing.json illisible")
        return 1

    stats = mesure(providers.get("providers", []))

    # 1) Rollback si le dernier changement s'est degrade
    rb = rollback_if_degrade(routing, providers.get("providers", []), stats)
    if rb:
        # restaurer le provider precedent pour cette task
        task = rb.get("task")
        de = rb.get("de")
        if task in routing.get("tasks", {}):
            old = routing["tasks"][task].get("provider")
            routing["tasks"][task]["provider"] = de
            routing["tasks"][task]["note"] = f"ROLLBACK AUTO ({now_iso()[:16]}): retour {old} -> {de} (degradation mesuree)"
            audit("rollback", "applique", {"task": task, "restaure": de, "raison": "degradation"})
            print(f"ROLLBACK: task={task} restaure {de}")
            # on ecrit et on s'arrete (pas de nouveau changement ce cycle)
            backup_routing()
            with open(ROUTING_PATH, "w") as f:
                json.dump(routing, f, ensure_ascii=False, indent=2)
            return 0

    # 2) Sinon : decision conservatrice
    changes = decide(routing, providers.get("providers", []), stats)
    if not changes:
        audit("cycle", "ok", {"changements": 0, "fenetre_h": WINDOW_H})
        print(f"ROUTEUR: aucun changement (fenetre {WINDOW_H}h, 0 modif)")
        return 0

    for c in changes:
        task = c["task"]
        routing["tasks"][task]["provider"] = c["vers"]
        note = f"ROUTEUR AUTO ({now_iso()[:16]}): {c['de']} -> {c['vers']} (score {c['score_actuel']} -> {c['score_propose']}, delta {c['delta']})"
        if routing["tasks"][task].get("note"):
            routing["tasks"][task]["note"] = note + " | " + routing["tasks"][task]["note"]
        else:
            routing["tasks"][task]["note"] = note
        audit("change", "applique", c)
        print(f"CHANGEMENT: {task}: {c['de']} -> {c['vers']} (delta {c['delta']} pts, {c['echantillons']} echantillons)")

    backup_routing()
    with open(ROUTING_PATH, "w") as f:
        json.dump(routing, f, ensure_ascii=False, indent=2)
    return 0


if __name__ == "__main__":
    sys.exit(main())
