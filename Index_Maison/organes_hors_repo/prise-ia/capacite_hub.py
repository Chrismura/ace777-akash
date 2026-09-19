#!/usr/bin/env python3
"""capacite_hub.py — jauge de capacité journalière du hub Prise IA.
Calcule : limites théoriques par provider + consommation réelle (usage.jsonl)
-> marge restante. Zéro dépendance (stdlib).
"""
import json
import os
from collections import defaultdict

P = os.path.expanduser('~/prise-ia')

# Capacités connues (vérifiées 08/08, sources : recherche + tests réels)
CAPACITES = {
    'qwen-local':      {'nom': 'Qwen 2.5 3B (local)', 'limite_jour': None, 'unite': 'illimite (RAM 8 Go)', 'cout': '0'},
    'gemini':          {'nom': 'Gemini Flash (Google)', 'limite_jour': 1500, 'unite': 'req/jour (free tier)', 'cout': '0'},
    'openrouter-free': {'nom': 'OpenRouter 14 modeles :free', 'limite_jour': 700, 'unite': 'req/jour (14 modeles x ~50)', 'cout': '0'},
    'nvidia':          {'nom': 'NVIDIA NIM DeepSeek V4', 'limite_jour': 1000, 'unite': 'credits initiaux + 40/min', 'cout': '0'},
    'groq':            {'nom': 'Groq (inactif)', 'limite_jour': 1000, 'unite': 'req/jour si active', 'cout': '0'},
    'mistral':         {'nom': 'Mistral (inactif)', 'limite_jour': 0, 'unite': 'desactive', 'cout': '0'},
    'cloudflare-workers-ai': {'nom': 'Cloudflare (inactif)', 'limite_jour': 0, 'unite': 'desactive', 'cout': '0'},
}

# 1. Consommation réelle
usage = os.path.join(P, 'usage.jsonl')
par_provider = defaultdict(int)
par_jour = defaultdict(int)
total = 0
if os.path.exists(usage):
    for line in open(usage):
        try:
            d = json.loads(line)
        except Exception:
            continue
        par_provider[d.get('provider', '?')] += 1
        par_jour[d.get('ts', '?')[:10]] += 1
        total += 1

# 2. Providers configurés (actif = enabled=True, local, ou utilisé récemment)
prov_path = os.path.join(P, 'providers.json')
actifs = []
if os.path.exists(prov_path):
    prov = json.load(open(prov_path))
    for p in prov.get('providers', []):
        pid = p.get('id', '?')
        if p.get('enabled') or p.get('kind') == 'local' or par_provider.get(pid, 0) > 0:
            actifs.append(pid)

# 3. Budget configuré
budget = 30
r_path = os.path.join(P, 'routing.json')
if os.path.exists(r_path):
    budget = json.load(open(r_path)).get('cloud_daily_budget', 30)

print('=' * 62)
print('JAUGE CAPACITE JOURNALIERE DU HUB PRISE IA')
print('=' * 62)
print()
print(f'Providers actifs : {", ".join(actifs)}')
print(f'Budget cloud configure : {budget} req/jour (auto-impose par nous)')
print(f'Consommation totale loguee : {total} appels')
print()
print(f'{"Provider":<20}{"Limite theorique/jour":<24}{"Conso reelle":<14}{"Marge":>8}')
print('-' * 62)
conso_totale = 0
for pid, cap in CAPACITES.items():
    conso = par_provider.get(pid, 0)
    conso_totale += conso
    if cap['limite_jour'] is None:
        marge = 'ILLIMITE'
        limite = 'illimite'
    elif cap['limite_jour'] == 0:
        marge = '-'
        limite = 'desactive'
    else:
        marge = f'{cap["limite_jour"] - conso}'
        limite = str(cap['limite_jour'])
    print(f'{pid:<20}{limite:<24}{conso:<14}{marge:>8}')
print('-' * 62)
print()
print('=== CONSOMMATION PAR JOUR ===')
for j in sorted(par_jour):
    print(f'  {j} : {par_jour[j]} appels')
print()
print('=== INTERPRETATION ===')
if total <= 50:
    print('  Vert : consommation basse, on utilise ~10-30% de la capacite cloud.')
elif total <= 150:
    print('  Orange : consommation moyenne.')
else:
    print('  Rouge : proche des limites, surveiller.')

# 4. Limites par minute (goulot reel)
print()
print('=== GOULOTS PAR MINUTE (le vrai facteur limitant) ===')
print('  OpenRouter : ~20 req/min (partage entre 14 modeles)')
print('  NVIDIA NIM : ~40 req/min')
print('  Gemini : ~15-30 req/min')
print('  -> Les jobs batch doivent etaler leurs appels dans le temps.')
