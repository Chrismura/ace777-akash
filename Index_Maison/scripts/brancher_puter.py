#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""brancher_puter.py — BRANCHE PUTER + A/B GROK RÉEL (09/08, followup Christophe).

Usage :  python3 brancher_puter.py  <PUTER_AUTH_TOKEN>
(ou export PUTER_AUTH_TOKEN=... puis python3 brancher_puter.py)

Etapes :
  1. ajoute PUTER_API_KEY=<token> dans ~/prise-ia/.env (backup, pas de doublon)
  2. ajoute le provider puter-grok dans providers.json EN OBSERVATION (enabled=false :
     le hub ne route JAMAIS un provider en observation - hub_prise_ia.py:40)
  3. A/B RÉEL : candidat grok (x-ai/grok-4.3 puis replis) vs actuel openrouter-ultra,
     VRAI JUGE (task signets.juge, famille differente) -> MIEUX/EGAL/PIRE/INACCESSIBLE
  4. rapport A_Mon_Attention/PREUVE_PUTER_GROK.md + journal

Le provider ne devient ACTIF qu'apres : A/B MIEUX + 48h observation + GO hebdomadaire
Christophe (protocole zero faute valide par les 4 familles 09/08).
"""
import json, os, sys, urllib.request, urllib.error
from datetime import datetime, date, timezone

HOME = os.path.expanduser('~')
PRISE = os.path.join(HOME, 'prise-ia')
ENV = os.path.join(PRISE, '.env')
PROVIDERS = os.path.join(PRISE, 'providers.json')
INDEX = os.path.join(HOME, 'ace777-test-day1', 'Index_Maison')
ATTENTION = os.path.join(INDEX, 'A_Mon_Attention')
JOURNAL = os.path.join(HOME, 'test-freebuff', 'journal_erreurs.md')
HUB = 'http://127.0.0.1:11435/v1/chat/completions'

PUTER_BASE = 'https://api.puter.com/puterai/openai/v1'
GROK_CANDIDATS = ['x-ai/grok-4.3', 'x-ai/grok-4.5', 'x-ai/grok-3-mini-fast']

QUESTION = ("En 3 phrases courtes : quels sont les deux risques principaux d'utiliser "
            "un modele de langage gratuit en production, et une parade pour chacun ?")


def erreur(msg):
    print('[ERREUR] ' + msg, file=sys.stderr)
    sys.exit(1)


def save_atomic(path, data):
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
    os.replace(tmp, path)


def env_key(k):
    try:
        for line in open(ENV):
            if line.startswith(k + '='):
                return line.strip().split('=', 1)[1]
    except Exception:
        pass
    return None


def set_env(k, v):
    """Ajoute ou remplace la cle dans .env (backup .env.bak)."""
    lines = open(ENV, encoding='utf-8').read().splitlines()
    bak = ENV + '.bak'
    if not os.path.exists(bak):
        open(bak, 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
    out, found = [], False
    for ln in lines:
        if ln.startswith(k + '='):
            out.append('%s=%s' % (k, v))
            found = True
        else:
            out.append(ln)
    if not found:
        out.append('%s=%s' % (k, v))
    open(ENV, 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print('[ENV] %s mise a jour (backup .env.bak)' % k)


def call_chat(base_url, model, api_key, timeout=45):
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


def hub_juge(txt_c, txt_r, model_c, model_r):
    prompt = (
        "Tu es le juge independant. Compare deux reponses a la MEME question : %r\n\n"
        "REPONSE A (candidat %s) :\n%s\n\nREPONSE B (actuel %s) :\n%s\n\n"
        "Reponds EXACTEMENT sur 1 ligne, en commencant par UN SEUL MOT : MIEUX, EGAL, PIRE, "
        "ou INACCESSIBLE. Puis apres un tiret, une phrase de preuve concrete (2-3 mots suffisent). "
        "MOT :" % (QUESTION, model_c, txt_c[:900], model_r, txt_r[:900])
    )
    payload = json.dumps({
        'task': 'signets.juge',
        'messages': [{'role': 'user', 'content': prompt}],
        'max_tokens': 80, 'temperature': 0.1,
    }).encode()
    req = urllib.request.Request(HUB, data=payload, headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=None) as resp:
            d = json.loads(resp.read().decode('utf-8'))
        out = d['choices'][0]['message']['content'].strip()
    except Exception as e:
        return 'INACCESSIBLE', 'juge indisponible: ' + str(e)[:50]
    up = out.upper()
    for v in ('MIEUX', 'EGAL', 'PIRE', 'INACCESSIBLE'):
        if up.startswith(v) or (' ' + v + ' ') in up or up == v:
            return v, out
    return 'EGAL', out[:120]


def active_reference(cfg):
    """Reference = provider actif 'gros cerveau' (openrouter-ultra en priorite)."""
    active = [p for p in cfg.get('providers', []) if p.get('enabled', False)]
    for pid in ('openrouter-ultra', 'nvidia', 'inferx', 'gemini'):
        for p in active:
            if p.get('id') == pid:
                return p
    return active[0] if active else None


def main():
    # Usage: brancher_puter.py <TOKEN> [--ref=<provider_id>]
    token, ref_override = None, None
    for a in sys.argv[1:]:
        if a.startswith('--ref='):
            ref_override = a.split('=', 1)[1]
        elif not a.startswith('-'):
            token = a
    if not token:
        token = os.environ.get('PUTER_AUTH_TOKEN')
    if not token or token.startswith('-'):
        erreur('Token manquant ou invalide. Usage: brancher_puter.py <PUTER_AUTH_TOKEN> [--ref=<provider_id>]\n'
               'Cree-le sur https://puter.com/dashboard#account -> "Create token"')

    if not os.path.exists(PROVIDERS):
        erreur('providers.json introuvable')
    cfg = json.load(open(PROVIDERS, encoding='utf-8'))

    # 1) env
    set_env('PUTER_API_KEY', token)

    # 2) provider en OBSERVATION (si absent)
    if not any(p.get('id') == 'puter-grok' for p in cfg['providers']):
        cfg['providers'].append({
            'id': 'puter-grok',
            'name': 'Puter Grok (gratuit)',
            'kind': 'cloud',
            'base_url': PUTER_BASE,
            'model': GROK_CANDIDATS[0],
            'api_key_env': 'PUTER_API_KEY',
            'enabled': False,
            'status': 'observation',
            'integrated_at': datetime.now(timezone.utc).isoformat(),
            'order': max([p.get('order', 0) for p in cfg['providers']]) + 1,
            'timeout': 90,
            'note': 'PUTER %s - en observation (A/B + GO hebdo avant activation)' % date.today().isoformat(),
        })
        save_atomic(PROVIDERS, cfg)
        print('[PROVIDER] puter-grok ajoute EN OBSERVATION (jamais route)')
    else:
        print('[PROVIDER] puter-grok deja present')

    # 3) A/B reel grok vs actuel (reference = --ref ou meilleure active)
    ref = None
    if ref_override:
        ref = next((p for p in cfg.get('providers', []) if p.get('id') == ref_override), None)
        if not ref:
            erreur('reference --ref=%s introuvable' % ref_override)
    else:
        ref = active_reference(cfg)
    if not ref:
        erreur('aucun provider actif de reference')
    ref_key = env_key(ref.get('api_key_env', '')) if ref.get('api_key_env') else None

    ok_ref, txt_ref, err_ref = call_chat(ref['base_url'], ref['model'], ref_key)
    if not ok_ref:
        erreur('actuel inaccessible: %s' % err_ref)

    verdict, preuve, model_ok = 'INACCESSIBLE', 'aucun candidat grok repond', None
    for model in GROK_CANDIDATS:
        print('[A/B] %s vs %s' % (model, ref.get('id')), flush=True)
        ok_c, txt_c, err_c = call_chat(PUTER_BASE, model, token)
        if not ok_c:
            print('[INFO] %s INACCESSIBLE: %s' % (model, err_c))
            continue
        verdict, preuve = hub_juge(txt_c, txt_ref, model, ref.get('model', '?'))
        model_ok = model
        print('[JUGE] %s — %s' % (verdict, preuve[:120]))
        break

    # 4) rapport de preuve
    os.makedirs(ATTENTION, exist_ok=True)
    rp = os.path.join(ATTENTION, 'PREUVE_PUTER_GROK.md')
    body = ('# 🥊 A/B RÉEL — Grok (via Puter) vs %s — %s\n\n'
            '| | Candidat | Actuel |\n|---|---|---|\n'
            '| Provider | Puter (gratuit) | %s |\n'
            '| Modèle | %s | %s |\n\n'
            '## Verdict du juge (famille différente)\n\n**%s** — %s\n\n'
            '> Le provider puter-grok est EN OBSERVATION : il ne devient ACTIF qu\'après\n'
            '> 48h de sondes sans faute ET ton GO hebdomadaire (protocole zéro faute).\n'
            % (ref.get('id'), date.today().isoformat(), ref.get('id'), model_ok or '-',
               ref.get('model'), verdict, preuve[:300]))
    with open(rp, 'w', encoding='utf-8') as f:
        f.write(body)
    print('PREUVE_PUTER_GROK.md ->', rp)

    with open(JOURNAL, 'a', encoding='utf-8') as f:
        f.write('\n## %s - A/B PUTER GROK : %s vs %s -> %s (%s)\n'
                % (date.today().isoformat(), model_ok or 'aucun', ref.get('id'), verdict, preuve[:100]))

    if verdict == 'MIEUX':
        print('\n>>> GROK MIEUX QUE %s (preuve jointe). En observation -> GO hebdo pour activer.' % ref.get('id'))
    elif verdict == 'EGAL':
        print('\n>>> EGAL : pas de raison de remplacer %s. Provider en observation, sera retire si pas valide.' % ref.get('id'))
    else:
        print('\n>>> %s : grok pas prouve meilleur. Provider reste dormant (observation), zero impact.' % verdict)


if __name__ == '__main__':
    main()
