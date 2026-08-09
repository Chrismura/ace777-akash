#!/usr/bin/env python3
"""veille_hub.py — CHECKUP QUOTIDIEN DU HUB (09/08/2026)
1) sante hub · 2) energie du jour (usage + budget cloud) · 3) scan catalogues
(nouvelles offres gratuites non integrees) · 4) rapport VEILLE_HUB_<date>.md

CORRECTION FAMILLE 09/08 (verdict CORRIGER, point 1 : saturation RAM 8 Go) :
ce script ne fait PLUS que le scan + rapport. Les etapes suivantes tournent en
launchd SEPARE, decalees dans le temps pour ne jamais saturer la RAM :
  09:05  veille_hub.py            (ce script : scan + rapport)
  09:30  eval_offres.py           (A/B + integration EN OBSERVATION, jamais active directe)
  10:00  catalog_providers.py     (catalogue consolide)
  10:30  propose_ameliorations.py (TOP 3 juge + contre-verif Gemini)
  11:00  observatoire.py          (sondes 48h + rollback auto >5% + validation hebdo)
Kill switch : si Index_Maison/STOP_HUB existe -> tout s'arrete SAUF le hub lui-meme.
"""
import json, os, urllib.request, datetime

HOME = os.path.expanduser('~')
PRISE = os.path.join(HOME, 'prise-ia')
HUB = 'http://127.0.0.1:11435'
OUT = os.path.join(HOME, 'ace777-test-day1', 'Index_Maison')

# Kill switch (correction famille : un fichier STOP tue tout sauf le hub)
STOP = os.path.join(OUT, 'STOP_HUB')
if os.path.exists(STOP):
    print('[STOP] STOP_HUB present -> veille ignoree (le hub, lui, continue)')
    raise SystemExit(0)


def get_json(url, headers=None, timeout=25):
    req = urllib.request.Request(url, headers=headers or {})
    return json.loads(urllib.request.urlopen(req, timeout=timeout).read())


def env_key(k):
    try:
        for line in open(os.path.join(PRISE, '.env')):
            if line.startswith(k + '='):
                return line.strip().split('=', 1)[1]
    except Exception:
        pass
    return None


# 1) sante
try:
    health = get_json(HUB + '/health', timeout=6)
    hub_ok = health.get('status') == 'ok'
    nb = health.get('providers', '?')
except Exception:
    hub_ok, nb = False, '?'

# 2) energie du jour
today = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d')
per_provider, total_today, cloud_today = {}, 0, 0
usage_path = os.path.join(PRISE, 'usage.jsonl')
if os.path.exists(usage_path):
    for line in open(usage_path):
        try:
            e = json.loads(line)
        except Exception:
            continue
        if e.get('ts', '')[:10] == today:
            total_today += 1
            p = e.get('provider', '?')
            per_provider[p] = per_provider.get(p, 0) + 1
            if e.get('kind') == 'cloud':
                cloud_today += 1
routing = {}
if os.path.exists(os.path.join(PRISE, 'routing.json')):
    routing = json.load(open(os.path.join(PRISE, 'routing.json')))
budget = routing.get('cloud_daily_budget')

# 3) scan catalogues : nouvelles offres vs modeles deja integres
providers_cfg = json.load(open(os.path.join(PRISE, 'providers.json')))
integrated = {p.get('model') for p in providers_cfg.get('providers', [])}


def scan(url, headers, name, want_free=False):
    out = []
    try:
        d = get_json(url, headers)
        for m in d.get('data', []):
            i = m.get('id')
            if not i:
                continue
            if want_free and ':free' not in i:
                continue
            if i not in integrated:
                out.append(i)
    except Exception as e:
        out.append('ERR: ' + str(e)[:60])
    return out


def scan_omniroute():
    # Catalogue free-tiers OmniRoute (43 pools gratuits documentes, MAJ bi-hebdo)
    # Source : https://raw.githubusercontent.com/diegosouzapw/OmniRoute/main/open-sse/config/freeModelCatalog.data.ts
    import re
    url = 'https://raw.githubusercontent.com/diegosouzapw/OmniRoute/main/open-sse/config/freeModelCatalog.data.ts'
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'veille_hub/1.0'})
        raw = urllib.request.urlopen(req, timeout=25).read().decode('utf-8')
    except Exception as e:
        return ['ERR: fetch (' + str(e)[:50] + ')']
    kv = re.compile(r'(\w+):\s*"((?:[^"\\]|\\.)*)"')
    out = []
    for line in raw.splitlines():
        if 'provider:' not in line:
            continue
        d = dict(kv.findall(line))
        ft = d.get('freeType', '').lower()
        tos = d.get('tos', '').lower()
        prov = d.get('provider', '')
        mid = d.get('modelId', '')
        if not prov or not mid or ft == 'discontinued' or tos == 'avoid':
            continue
        if (prov + '/' + mid) in integrated:
            continue
        mois = 'inconnu'
        if 'uncapped' in ft:
            mois = 'gratuit sans cap'
        elif ft.startswith('recurring'):
            mois = 'recurrent'
        elif ft == 'keyless':
            mois = 'sans cle'
        elif ft == 'one-time-initial':
            mois = 'credit bienvenue'
        out.append('%s/%s (%s, %s)' % (prov, mid, ft, mois))
    return out


findings = {}
or_key = env_key('OPENROUTER_API_KEY')
if or_key:
    findings['openrouter (:free)'] = scan('https://openrouter.ai/api/v1/models',
                                          {'Authorization': 'Bearer ' + or_key}, 'openrouter', want_free=True)
nkey = env_key('NVIDIA_NIM_API_KEY')
if nkey:
    findings['nvidia'] = scan('https://integrate.api.nvidia.com/v1/models',
                              {'Authorization': 'Bearer ' + nkey}, 'nvidia')
ikey = env_key('INFERX_API_KEY')
if ikey:
    findings['inferx'] = scan('https://model.inferx.net/endpoints/v1/models',
                              {'Authorization': 'Bearer ' + ikey}, 'inferx')
pkey = env_key('PUTER_API_KEY')
if pkey:
    # Puter (gratuit, token 09/08) : pas d'endpoint /models -> liste des modeles connus,
    # filtres sur ceux deja integres. L'auto-eval les re-teste chaque matin (jamais oublie).
    puter_models = ['gpt-5.4', 'claude-sonnet-4-5', 'x-ai/grok-3-mini-fast',
                    'deepseek/deepseek-v4-flash', 'gpt-4o']
    findings['puter (gratuit, token)'] = [m for m in puter_models if m not in integrated]
findings['omniroute-free-tiers (43 pools)'] = scan_omniroute()

# 4) rapport
L = ['# VEILLE HUB — ' + today, '',
     '## Santé', '- hub : ' + ('OK (' + str(nb) + ' providers)' if hub_ok else 'NOK'), '',
     '## Énergie du jour', '- appels : %d (cloud %d)' % (total_today, cloud_today),
     '- budget cloud : %s max' % (budget if budget else 'illimité'),
     '- par provider : ' + ', '.join('%s=%d' % (k, v) for k, v in sorted(per_provider.items())), '',
     '## Nouvelles offres détectées (non intégrées)', '']
for cat, items in findings.items():
    L.append('### ' + cat)
    if not items:
        L.append('- aucune nouvelle')
    else:
        for i in items[:15]:
            L.append('- ' + i)
    L.append('')
report = '\n'.join(L) + ('_généré par veille_hub.py — étapes suivantes en launchd décalé : '
                         'eval 9h30 · catalogue 10h · propositions 10h30 · observatoire 11h._')
rp = os.path.join(OUT, 'VEILLE_HUB_' + today + '.md')
open(rp, 'w', encoding='utf-8').write(report)
print(report[:1400])
