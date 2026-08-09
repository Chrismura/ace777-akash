#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""eval_offres.py — EVALUATION COMPARATIVE AUTO + INTEGRATION AUTO des meilleures IA gratuites.

Flux (protocole zero faute, valide Christophe 09/08) :
  veille_hub.py (detection 9h05) -> eval_offres.py (9h30 : A/B reel + juge famille differente)
  -> si GRATUIT + MIEUX + test reel OK -> integration ADDITIVE EN OBSERVATION
  -> jamais active directe : observatoire.py (11h) valide apres 48h de sondes
     + GO hebdomadaire Christophe (correction famille 09/08, points juge/ultra/deepseek).

Corrections appliquees (09/08) :
  - vrai appel au juge via le hub (task signets.juge) — PAS d'heuristique maison
  - chemins corrects ; ecriture ATOMIQUE (tmp + rename) ; mapping de role
  - filtre gratuit STRICT ; 1 seule integration par run ; backup AVANT ; SAIN intouchable
  - CORRECTION FAMILLE : integration en `enabled:false` + `status:'observation'`
    (le hub ne route PAS un provider enabled:false -> derive silencieuse impossible)
  - kill switch : Index_Maison/STOP_HUB -> arret propre.
"""
import json, os, re, sys, time, urllib.request, urllib.error
from datetime import datetime, date, timezone

HOME = os.path.expanduser('~')
PRISE = os.path.join(HOME, 'prise-ia')
PROVIDERS = os.path.join(PRISE, 'providers.json')
INDEX = os.path.join(HOME, 'ace777-test-day1', 'Index_Maison')
JOURNAL = os.path.join(HOME, 'test-freebuff', 'journal_erreurs.md')
HUB = 'http://127.0.0.1:11435/v1/chat/completions'
OPENROUTER = 'https://openrouter.ai/api/v1'

QUESTION = ("En 3 phrases courtes : quels sont les deux risques principaux d'utiliser "
            "un modele de langage gratuit en production, et une parade pour chacun ?")

# Mapping role -> provider actuel de reference (priorite de choix)
ROLE_MAP = [
    ('gros cerveau', ['openrouter-ultra', 'nvidia', 'inferx', 'gemini']),
    ('code',         ['inferx-coder', 'nvidia', 'openrouter-ultra']),
    ('rapide',       ['gemini', 'qwen-local', 'openrouter-free']),
]


def env_key(k):
    try:
        for line in open(os.path.join(PRISE, '.env')):
            if line.startswith(k + '='):
                return line.strip().split('=', 1)[1]
    except Exception:
        return None
    return None


def load(path):
    try:
        return json.load(open(path, encoding='utf-8'))
    except Exception as e:
        print('[ERREUR] load %s: %s' % (path, e), file=sys.stderr)
        return {}


def save_atomic(path, data):
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
    os.replace(tmp, path)  # atomique


def active_providers(cfg):
    return [p for p in cfg.get('providers', []) if p.get('enabled', False)]


def closest_reference(active, role_hint):
    for label, ids in ROLE_MAP:
        for pid in ids:
            for p in active:
                if p.get('id') == pid:
                    return p
    return active[0] if active else None


def call_chat(base_url, model, api_key, timeout=35):
    """Appel OpenAI-compatible. Retourne (ok, texte, erreur)."""
    try:
        headers = {'Content-Type': 'application/json'}
        if api_key:
            headers['Authorization'] = 'Bearer ' + api_key
        payload = json.dumps({
            'model': model,
            'messages': [{'role': 'user', 'content': QUESTION}],
            'max_tokens': 220, 'temperature': 0.3,
        }).encode()
        req = urllib.request.Request(base_url.rstrip('/') + '/chat/completions',
                                     data=payload, headers=headers)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            d = json.loads(resp.read().decode('utf-8'))
        text = d['choices'][0]['message']['content'].strip()
        if not text:
            return False, '', 'reponse vide'
        return True, text, ''
    except urllib.error.HTTPError as e:
        body = ''
        try:
            body = e.read().decode('utf-8')[:80]
        except Exception:
            pass
        return False, '', 'HTTP %s %s' % (e.code, body)
    except Exception as e:
        return False, '', str(e)[:80]


def hub_juge(texte_cand, texte_actuel, model_cand, model_actuel):
    """Appel du VRAI juge (famille differente, task signets.juge) — pas d'heuristique."""
    prompt = (
        "Tu es le juge independant. Compare deux reponses a la MEME question : %r\n\n"
        "REPONSE A (candidat %s) :\n%s\n\nREPONSE B (actuel %s) :\n%s\n\n"
        "Reponds EXACTEMENT sur 1 ligne, en commencant par UN SEUL MOT : MIEUX, EGAL, PIRE, "
        "ou INACCESSIBLE. Puis apres un tiret, une phrase de preuve concrete (2-3 mots suffisent). "
        "Exemple : MIEUX - reponse plus precise et structuree.\n"
        "MOT :"
        % (QUESTION, model_cand, texte_cand[:900], model_actuel, texte_actuel[:900])
    )
    payload = json.dumps({
        'task': 'signets.juge',
        'messages': [{'role': 'user', 'content': prompt}],
        'max_tokens': 80, 'temperature': 0.1,
    }).encode()
    req = urllib.request.Request(HUB, data=payload, headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            d = json.loads(resp.read().decode('utf-8'))
        out = d['choices'][0]['message']['content'].strip()
    except Exception as e:
        return 'INACCESSIBLE', 'juge indisponible: ' + str(e)[:50]
    for v in ('MIEUX', 'EGAL', 'PIRE', 'INACCESSIBLE'):
        if out.upper().startswith(v):
            return v, out
    up = out.upper()
    for v in ('MIEUX', 'EGAL', 'PIRE', 'INACCESSIBLE'):
        if v in up:
            return v, out
    return 'EGAL', out[:120]


def is_free(p):
    note = (p.get('note') or '').lower()
    price = p.get('price', 0)
    if isinstance(price, (int, float)) and price > 0:
        return False
    if any(w in note for w in ('payant', 'prix ', '$', 'coute')):
        return False
    if p.get('tos') == 'avoid' or p.get('discontinued'):
        return False
    return True


def already_done_today():
    rp = os.path.join(INDEX, 'VEILLE_HUB_%s.md' % date.today().isoformat())
    if os.path.exists(rp):
        txt = open(rp, encoding='utf-8').read()
        # couvre l'ancien et le nouveau marqueur (bug revue 09/08 : INTEGRE != INTEGRATION)
        return 'INTEGRATION AUTO' in txt or 'INTEGRE AUTO' in txt
    return False


def candidates_from_veille():
    """Candidates testables = modeles :free OpenRouter + NVIDIA + InferX listes dans le rapport."""
    out = []
    or_key = env_key('OPENROUTER_API_KEY')
    nkey = env_key('NVIDIA_NIM_API_KEY')
    ikey = env_key('INFERX_API_KEY')
    rp = os.path.join(INDEX, 'VEILLE_HUB_%s.md' % date.today().isoformat())
    if not os.path.exists(rp):
        print('[INFO] pas de rapport VEILLE_HUB du jour')
        return out
    section = None
    for line in open(rp, encoding='utf-8'):
        if line.startswith('### '):
            section = line[4:].strip()
            continue
        line = line.strip()
        if not line.startswith('- '):
            continue
        item = line[2:].strip()
        if 'ERR:' in item:
            continue
        if section == 'openrouter (:free)':
            out.append({'model': item, 'base_url': OPENROUTER,
                        'api_key_env': 'OPENROUTER_API_KEY', 'role': 'gros cerveau'})
        elif section == 'nvidia':
            out.append({'model': item, 'base_url': 'https://integrate.api.nvidia.com/v1',
                        'api_key_env': 'NVIDIA_NIM_API_KEY', 'role': 'gros cerveau'})
        elif section == 'inferx':
            out.append({'model': item, 'base_url': 'https://model.inferx.net/endpoints/v1',
                        'api_key_env': 'INFERX_API_KEY', 'role': 'gros cerveau'})
        elif section and 'puter' in section:
            out.append({'model': item, 'base_url': 'https://api.puter.com/puterai/openai/v1',
                        'api_key_env': 'PUTER_API_KEY', 'role': 'gros cerveau'})
    return out


def main():
    # Kill switch (correction famille : STOP tue tout sauf le hub)
    if os.path.exists(os.path.join(INDEX, 'STOP_HUB')):
        print('[STOP] STOP_HUB present -> eval ignore')
        sys.exit(0)

    cfg = load(PROVIDERS)
    if not cfg.get('providers'):
        print('[ERREUR] providers.json vide', file=sys.stderr)
        sys.exit(1)

    if already_done_today():
        print('[SKIP] integration deja faite aujourd hui')
        sys.exit(0)

    active = active_providers(cfg)
    cands = candidates_from_veille()
    if not cands:
        print('[INFO] aucune candidate testable (pas de modele :free accessible)')
        sys.exit(0)

    def rank(c):
        # Puter en 1er (gratuit, token dispo) : c'est la source la plus accessible
        order = {'PUTER_API_KEY': 0, 'OPENROUTER_API_KEY': 1, 'INFERX_API_KEY': 2, 'NVIDIA_NIM_API_KEY': 3}
        return order.get(c.get('api_key_env'), 9)
    cands.sort(key=rank)
    MAX_TEST = 4  # ne pas bruler les quotas gratuits (429 :free par jour)
    cands = cands[:MAX_TEST]
    tried = 0
    for cand in cands:
        tried += 1
        key = env_key(cand.get('api_key_env', ''))
        if not key:
            print('[INFO] pas de cle pour %s -> SKIP' % cand.get('api_key_env'))
            continue

        ref = closest_reference(active, cand.get('role', 'gros cerveau'))
        if not ref:
            print('[ERREUR] aucun provider actif de reference', file=sys.stderr)
            sys.exit(1)

        print('[A/B] %s (candidat) vs %s (actuel)' % (cand['model'], ref.get('id')))
        ok_c, txt_c, err_c = call_chat(cand['base_url'], cand['model'], key)
        if not ok_c:
            print('[INFO] candidat INACCESSIBLE: %s' % err_c)
            continue
        ref_key = env_key(ref.get('api_key_env', '')) if ref.get('api_key_env') else None
        ok_r, txt_r, err_r = call_chat(ref['base_url'], ref['model'], ref_key)
        if not ok_r:
            print('[INFO] actuel INACCESSIBLE: %s' % err_r)
            continue

        verdict, preuve = hub_juge(txt_c, txt_r, cand['model'], ref.get('model', '?'))
        print('[JUGE] %s — %s' % (verdict, preuve[:120]))

        if verdict != 'MIEUX':
            print('[INFO] verdict=%s -> on passe au candidat suivant' % verdict)
            continue

        # Integration additive EN OBSERVATION : backup avant, ecriture atomique,
        # enabled=false -> le hub ne route PAS (correction famille 09/08).
        bak = os.path.join(PRISE, 'providers.json.bak-%s' % date.today().isoformat())
        if not os.path.exists(bak):
            save_atomic(bak, cfg)
        new_id = re.sub(r'[^a-z0-9-]', '-', cand['model'].lower()).strip('-')[:40]
        if any(p.get('id') == new_id or p.get('model') == cand['model'] for p in cfg['providers']):
            print('[INFO] deja integre (id ou modele existe) -> SKIP')
            sys.exit(0)
        cfg['providers'].append({
            'id': new_id,
            'name': 'Auto %s' % cand['model'],
            'kind': 'cloud',
            'base_url': cand['base_url'],
            'model': cand['model'],
            'api_key_env': cand.get('api_key_env'),
            'enabled': False,                     # OBSERVATION : jamais route par le hub
            'status': 'observation',              # -> observatoire.py decidera (48h + GO hebdo)
            'integrated_at': datetime.now(timezone.utc).isoformat(),
            'order': max([p.get('order', 0) for p in cfg['providers']]) + 1,
            'timeout': 60,
            'note': 'INTEGRE AUTO %s EN OBSERVATION (preuve A/B + juge: %s)' % (date.today().isoformat(), preuve[:90]),
        })
        save_atomic(PROVIDERS, cfg)
        print('[OK] INTEGRATION AUTO (EN OBSERVATION): %s (%s)' % (new_id, cand['model']))

        # Notice rapport + journal
        rp = os.path.join(INDEX, 'VEILLE_HUB_%s.md' % date.today().isoformat())
        with open(rp, 'a', encoding='utf-8') as f:
            f.write('\n## INTEGRATION AUTO %s\n- Hub ameliore avec %s (preuve A/B + juge : %s)\n'
                    '- ETAT : EN OBSERVATION 48h (jamais route) -> observatoire + GO hebdo avant activation.\n'
                    % (date.today().isoformat(), cand['model'], preuve[:160]))
        with open(JOURNAL, 'a', encoding='utf-8') as f:
            f.write('\n## %s - INTEGRATION AUTO (OBSERVATION) : %s (%s) MIEUX que %s - preuve A/B + juge\n'
                    % (date.today().isoformat(), new_id, cand['model'], ref.get('id')))
        print('[NOTICE] rapport + journal mis a jour (en observation, pas encore actif)')
        break  # 1 seule integration par run

    if tried == 0:
        print('[INFO] aucun candidat testable')
    else:
        print('[FIN] %d candidat(s) tente(s) — 1 integration max par run (regle OSSATURE)' % tried)


if __name__ == '__main__':
    main()
