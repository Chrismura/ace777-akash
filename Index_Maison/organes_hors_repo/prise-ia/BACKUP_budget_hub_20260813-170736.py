#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""budget_hub.py — budget cloud DYNAMIQUE avec réserve storm et gratuits protégés (lecture providers.json)."""

import json
import os
import shutil
import sys
import time
from typing import Any, Dict, List, Optional, Set

P = os.path.expanduser('~/prise-ia')
FACTEUR_SECURITE = 0.15
MIN_BUDGET = 40
MAX_BUDGET = 800

CAPACITES: Dict[str, int] = {
    'qwen-local': 0,
    'gemini': 1500,
    'openrouter-free': 700,
    'openrouter-ultra': 500,
    'openrouter-juge': 300,
    'nvidia': 1000,
    'inferx-coder': 400,
    'puter-grok': 800,
    'groq': 1000,
    'mistral': 0,
    'cloudflare-workers-ai': 0,
}


def providers_actifs() -> List[str]:
    """Retourne la liste des providers actifs depuis providers.json."""
    prov_path = os.path.join(P, 'providers.json')
    if not os.path.exists(prov_path):
        return []
    try:
        with open(prov_path, 'r', encoding='utf-8') as f:
            prov = json.load(f)
        actifs: List[str] = []
        for p in prov.get('providers', []):
            pid = p.get('id', '?')
            if p.get('enabled') or p.get('kind') == 'local':
                actifs.append(pid)
        return actifs
    except Exception:
        return []


def gratuits_actifs() -> List[str]:
    """Retourne la liste des providers gratuits (free: true) depuis providers.json."""
    prov_path = os.path.join(P, 'providers.json')
    if not os.path.exists(prov_path):
        return []
    try:
        with open(prov_path, 'r', encoding='utf-8') as f:
            prov = json.load(f)
        gratuits: List[str] = []
        for p in prov.get('providers', []):
            if p.get('free') is True and (p.get('enabled') or p.get('kind') == 'local'):
                gratuits.append(p.get('id'))
        return gratuits
    except Exception:
        return []


def calculer_budget_journalier(actifs: List[str]) -> Dict[str, Any]:
    """Fonction pure de calcul du budget journalier dynamique."""
    capacite_totale = sum(CAPACITES.get(pid, 0) for pid in actifs)
    total = max(MIN_BUDGET, min(MAX_BUDGET, int(capacite_totale * FACTEUR_SECURITE)))
    reserve_storm = int(total * 0.20)
    calme = total - reserve_storm
    gratuits = gratuits_actifs()
    return {
        "total": total,
        "calme": calme,
        "reserve_storm": reserve_storm,
        "gratuits": gratuits,
        "payants": [],
        "actifs": actifs,
        "ts": int(time.time())
    }


def main() -> None:
    """Point d'entrée principal."""
    try:
        actifs = providers_actifs()
        r_path = os.path.join(P, 'routing.json')
        routing: Dict[str, Any] = {}
        if os.path.exists(r_path):
            try:
                with open(r_path, 'r', encoding='utf-8') as f:
                    routing = json.load(f)
            except Exception:
                routing = {}

        referenced: Set[str] = set()
        for v in routing.get('tasks', {}).values():
            if isinstance(v, dict):
                referenced.add(v.get('provider'))
                referenced.add(v.get('fallback'))
        for pid in referenced:
            if pid and pid not in actifs:
                actifs.append(pid)

        budget = calculer_budget_journalier(actifs)
        gratuits_liste = budget.get("gratuits", [])

        print('=== BUDGET CLOUD DYNAMIQUE ===')
        print('Providers actifs (%d) : %s' % (len(actifs), ', '.join(actifs)))
        print('Capacite theorique cloud/jour : %d req' % sum(CAPACITES.get(pid, 0) for pid in actifs))
        print('Facteur securite : %d%%' % int(FACTEUR_SECURITE * 100))
        print('Budget total : %d | Calme : %d | Reserve storm : %d' % (
            budget["total"], budget["calme"], budget["reserve_storm"]))
        print('Gratuits proteges (dynamiques) : %s' % ', '.join(sorted(gratuits_liste)))
        ancien = routing.get('cloud_daily_budget', '?')
        print('Budget actuel dans routing.json : %s' % ancien)

        if '--apply' in sys.argv:
            try:
                if os.path.exists(r_path):
                    shutil.copy(r_path, r_path + '.bak-budget')
                routing['cloud_daily_budget'] = budget["calme"]
                routing['cloud_daily_reserve'] = budget["reserve_storm"]
                routing['note'] = ('cloud_daily_budget DYNAMIQUE calcule par budget_hub.py '
                                   '(%d calme + %d reserve storm). Recalcule quotidien apres rotation.' %
                                   (budget["calme"], budget["reserve_storm"]))
                with open(r_path, 'w', encoding='utf-8') as f:
                    json.dump(routing, f, indent=1, ensure_ascii=False)
                print('-> APPLIQUE : cloud_daily_budget=%d, cloud_daily_reserve=%d' % (
                    budget["calme"], budget["reserve_storm"]))
            except Exception:
                print('-> ERREUR ecriture routing.json (non fatal)')
        else:
            print('(ajouter --apply pour ecrire dans routing.json)')
    except Exception:
        print('budget_hub.py: erreur non fatale ignoree')


if __name__ == '__main__':
    main()
