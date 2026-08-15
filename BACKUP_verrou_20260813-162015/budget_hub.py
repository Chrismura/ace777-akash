#!/usr/bin/env python3
"""budget_hub.py — budget cloud DYNAMIQUE qui suit l'évolution du hub.

Principe : le budget journalier n'est plus un chiffre figé (30).
Il se recalcule depuis les providers ACTIFS : capacite_theorique * FACTEUR_SECURITE.
Si on ajoute NVIDIA NIM (+1000) ou OpenRouter (+700), le budget suit automatiquement.

Zéro dépendance (stdlib). Usage :
    python3 budget_hub.py          # affiche le calcul
    python3 budget_hub.py --apply  # écrit cloud_daily_budget dans routing.json (+ backup)
"""
import json
import os
import shutil
import sys

P = os.path.expanduser('~/prise-ia')
FACTEUR_SECURITE = 0.15          # on n'utilise que 15% de la capacité théorique par jour
MIN_BUDGET = 40                  # jamais sous 40 (on tourne déjà à ~40/jour)
MAX_BUDGET = 800                 # plafond de prudence (sécurité : ne jamais exploser)

# Capacité théorique/jour par provider (vérifiée 08/08)
CAPACITES = {
    'qwen-local': 0,             # local : illimité mais ne compte pas dans le budget cloud
    'gemini': 1500,
    'openrouter-free': 700,
    'nvidia': 1000,
    'groq': 1000,
    'mistral': 0,
    'cloudflare-workers-ai': 0,
}


def providers_actifs():
    prov_path = os.path.join(P, 'providers.json')
    if not os.path.exists(prov_path):
        return []
    prov = json.load(open(prov_path))
    actifs = []
    for p in prov.get('providers', []):
        pid = p.get('id', '?')
        if p.get('enabled') or p.get('kind') == 'local':
            actifs.append(pid)
    return actifs


def main():
    actifs = providers_actifs()
    # gemini n'a pas de champ enabled -> on l'ajoute s'il est référencé dans routing
    r_path = os.path.join(P, 'routing.json')
    routing = json.load(open(r_path)) if os.path.exists(r_path) else {}
    referenced = set()
    for v in routing.get('tasks', {}).values():
        referenced.add(v.get('provider'))
        referenced.add(v.get('fallback'))
    for pid in referenced:
        if pid not in actifs:
            actifs.append(pid)

    capacite_totale = sum(CAPACITES.get(pid, 0) for pid in actifs)
    budget_calcule = max(MIN_BUDGET, min(MAX_BUDGET, int(capacite_totale * FACTEUR_SECURITE)))

    print('=== BUDGET CLOUD DYNAMIQUE ===')
    print(f'Providers actifs ({len(actifs)}) : {", ".join(actifs)}')
    print(f'Capacite theorique cloud/jour : {capacite_totale} req')
    print(f'Facteur securite : {int(FACTEUR_SECURITE*100)}%')
    print(f'Budget calcule : {budget_calcule} req/jour')
    ancien = routing.get('cloud_daily_budget', '?')
    print(f'Budget actuel dans routing.json : {ancien}')
    print(f'Delta : {budget_calcule - (ancien if isinstance(ancien, int) else budget_calcule)}')

    if '--apply' in sys.argv:
        shutil.copy(r_path, r_path + '.bak-budget')
        routing['cloud_daily_budget'] = budget_calcule
        routing['note'] = (f'cloud_daily_budget DYNAMIQUE calcule par budget_hub.py le 08/08 '
                           f'({budget_calcule} = {capacite_totale} x {FACTEUR_SECURITE}). '
                           f'Se recalcule a chaque ajout de provider (voir budget_hub.py)')
        json.dump(routing, open(r_path, 'w'), indent=1, ensure_ascii=False)
        print(f'-> APPLIQUE : cloud_daily_budget = {budget_calcule} (backup: routing.json.bak-budget)')
    else:
        print('(ajouter --apply pour écrire dans routing.json)')


if __name__ == '__main__':
    main()
