#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""repare_ids.py — CHIRURGIEN DES IDS (logique cycle de vie, GO Christophe 17/10/2026).

Constat pratique (Christophe) : les offres ne MEURENT pas, elles CHANGENT —
renommage, upgrade, retrait (groq/compound évaporé, glm-5.2:free devenu payant,
deepseek-v4-flash -> v4.1-flash). Le roulement ne sait que remplacer un provider
ENTIER ; personne ne réparait un champ `model` mort (les deux ci-dessus sont
restés morts des semaines). Ce job comble ce trou :

  pour chaque provider avec clé : catalogue LIVE du fournisseur -> le `model`
  configuré y est-il ? sinon (404/410 au test) : successeur testé OK -> on répare.

Frontières STRICTES (zéro conflit avec les autres maillons) :
  - ne touche JAMAIS à `enabled` (territoire du roulement) ni aux providers SAINs
    (test OK -> intouché, pas même une note) ;
  - 429 quota -> on passe (temporaire, JAMAIS d'éjection) ;
  - 402 paywall -> note seulement, le discernement reste au roulement ;
  - écriture : backup 1x/run AVANT + atomique (tmp + os.replace) ;
  - kill switch : Index_Maison/STOP_HUB -> arrêt propre ;
  - gratuit STRICT : successeurs pris dans les catalogues free/listes live ;
  - MAX 3 réparations/run ; --dry-run pour répéter sans écrire.

Usage :
  python3 repare_ids.py            # répare (launchd 7h04)
  python3 repare_ids.py --dry-run  # annonce sans écrire
"""
import json
import os
import sys
import urllib.request
import urllib.error
from datetime import date

HOME = os.path.expanduser('~')
PRISE = os.path.join(HOME, 'prise-ia')
PROVIDERS = os.path.join(PRISE, 'providers.json')
INDEX = os.path.join(HOME, 'ace777-test-day1', 'Index_Maison')
BAK = os.path.join(PRISE, 'providers.json.bak-repare-%s' % date.today().isoformat())

MAX_REPARES = 3
TIMEOUT = 20  # un micro-test doit répondre vite ; cold-start -> INDECIS, retenté demain

# Ordre de préférence des successeurs quand la famille a disparu du catalogue.
# On intersecte avec le catalogue LIVE : jamais d'ID inventé.
SUCCESSEURS_PREFERES = {
    'groq': ['qwen/qwen3.8-27b', 'openai/gpt-oss-20b', 'openai/gpt-oss-120b'],
    'openrouter-free': ['google/gemma-4-31b-it:free',
                        'cohere/north-mini-code:free',
                        'nvidia/nemotron-3.5-lightning:free',
                        'nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free'],
    'nvidia': ['deepseek-ai/deepseek-v4.1-flash',
               'moonshotai/kimi-k3',
               'nvidia/nemotron-3-ultra-550b-a55b'],
    'nvidia-coder': ['deepseek-ai/deepseek-coder-6.7b-instruct',
                     'bigcode/starcoder2-15b',
                     'mistralai/codestral-22b-instruct-v0.1'],
    'mistral': ['codestral-latest', 'codestral-2508'],
}

# base_url -> listeur de catalogue (None = pas de catalogue, test direct seul).
# Le listeur renvoie la liste des IDs live (ou None si illisible).
def _get(url, key=None, timeout=25):
    try:
        headers = {}
        if key:
            headers['Authorization'] = 'Bearer ' + key
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode('utf-8'))
    except Exception:
        return None


def catalogue_openrouter():
    d = _get('https://openrouter.ai/api/v1/models')
    if not d:
        return None
    return [m.get('id') for m in d.get('data', []) if m.get('id')]


def catalogue_groq(key):
    d = _get('https://api.groq.com/openai/v1/models', key)
    if not d:
        return None
    return [m.get('id') for m in d.get('data', []) if m.get('id')]


def catalogue_nim(key):
    d = _get('https://integrate.api.nvidia.com/v1/models', key)
    if not d:
        return None
    return [m.get('id') for m in d.get('data', []) if m.get('id')]


def catalogue_mistral(key):
    d = _get('https://api.mistral.ai/v1/models', key)
    if not d:
        return None
    data = d.get('data', [])
    return [m.get('id') for m in data if m.get('id')]


def env_key(k):
    try:
        for line in open(os.path.join(PRISE, '.env')):
            if line.startswith(k + '='):
                return line.strip().split('=', 1)[1]
    except Exception:
        pass
    return None


def test_model(base_url, model, key, timeout=TIMEOUT):
    """Teste un modèle. Retourne ('ok', texte) | ('http404',..) | ('http410',..)
    | ('http402',..) | ('http429',..) | ('autre', ..) | ('timeout', ..).
    Accepte les réponses reasoning-only (content null) : c'est vivant aussi
    (même fix que eval_offres 17/10 : le .strip() sur None tuait les candidats)."""
    try:
        body = json.dumps({
            'model': model,
            'messages': [{'role': 'user', 'content': 'Dis juste: ok'}],
            'max_tokens': 20,
        }).encode()
        headers = {'Content-Type': 'application/json'}
        if key:
            headers['Authorization'] = 'Bearer ' + key
        req = urllib.request.Request(base_url.rstrip('/') + '/chat/completions',
                                     data=body, headers=headers)
        with urllib.request.urlopen(req, timeout=timeout) as r:
            d = json.loads(r.read().decode('utf-8'))
        msg = (d.get('choices') or [{}])[0].get('message', {}) or {}
        texte = msg.get('content') or msg.get('reasoning') or ''
        if isinstance(texte, str):
            texte = texte.strip()
        if not texte:
            return 'vide', ''
        return 'ok', texte[:80]
    except urllib.error.HTTPError as e:
        return 'http%d' % e.code, ''
    except TimeoutError:
        return 'timeout', ''
    except Exception as e:
        if 'timed out' in str(e):
            return 'timeout', ''
        return 'autre', str(e)[:60]


def famille_tokens(model_id):
    """Tokens de famille pour apparier un successeur (glm, deepseek, qwen...)."""
    toks = []
    for t in model_id.lower().replace('/', ' ').replace('-', ' ').replace('_', ' ').split():
        if t not in ('free', 'it', 'instruct', 'latest', 'flash', 'pro', 'max', 'fp8'):
            toks.append(t)
    return toks


def vendeur(model_id):
    """Vendeur = préfixe avant '/' (nex-agi, xingchen-agi, google...)."""
    return (model_id.split('/')[0] if '/' in model_id else model_id.split('-')[0]).lower()


GENERIOUES = {'agi', 'ai', 'free', 'chat', 'instruct', 'it', 'latest', 'flash',
              'pro', 'max', 'fp8', 'model', 'preview', 'turbo', 'mini', 'small'}


def successeurs(provider_id, model_mort, live_ids):
    """Candidats successeurs : préférés explicites (si live) puis même VENDEUR.
    FIX 17/10 (dry-run) : l'appariement par tokens libres mariait nex-agi avec
    xingchen-agi sur le seul token 'agi' — un faux successeur. Désormais le
    vendeur doit correspondre (ou le candidat vient de la table explicite)."""
    cands = []
    for pref in SUCCESSEURS_PREFERES.get(provider_id, []):
        if pref in (live_ids or []) and pref != model_mort:
            cands.append(pref)
    if live_ids:
        vendu = vendeur(model_mort)
        toks = set(famille_tokens(model_mort)) - GENERIOUES
        for lid in live_ids:
            if lid == model_mort or lid in cands:
                continue
            if vendeur(lid) != vendu:
                continue
            if toks & (set(famille_tokens(lid)) - GENERIOUES):
                cands.append(lid)
    return cands


def main():
    dry = '--dry-run' in sys.argv
    if os.path.exists(os.path.join(INDEX, 'STOP_HUB')):
        print('[STOP] STOP_HUB present -> repare_ids ignore')
        return 0
    try:
        cfg = json.load(open(PROVIDERS, encoding='utf-8'))
    except Exception as e:
        print('[ERREUR] providers.json illisible: %s' % e)
        return 1

    repares = 0
    backup_fait = os.path.exists(BAK)
    for p in cfg.get('providers', []):
        if repares >= MAX_REPARES:
            print('[INFO] plafond %d reparations atteint, suite demain' % MAX_REPARES)
            break
        pid = p.get('id', '?')
        if pid.startswith('obs-'):
            continue  # registre de l'observatoire : intouchable
        key_env = p.get('api_key_env')
        key = env_key(key_env) if key_env else None
        if p.get('kind') == 'local':
            continue  # Ollama local : pas de catalogue distant
        if not key:
            continue  # sans clé on ne peut ni lister ni tester
        base = p.get('base_url', '')
        model = p.get('model', '')

        etat, _ = test_model(base, model, key)
        if etat == 'ok':
            continue  # SAIN intouchable
        if etat == 'http429':
            continue  # quota temporaire : JAMAIS d'éjection ni de note
        if etat == 'timeout':
            print('[INDECIS] %s (%s) : timeout (cold-start ?) -> on retentera demain' % (pid, model))
            continue
        if etat == 'http402':
            print('[PAYWALL] %s (%s) : 402, discernement au roulement' % (pid, model))
            continue
        if etat not in ('http404', 'http410'):
            print('[AUTRE] %s (%s) : %s -> au roulement' % (pid, model, etat))
            continue

        # ID mort (404/410) : chercher le successeur dans le catalogue live.
        live = None
        if 'openrouter.ai' in base:
            live = catalogue_openrouter()
        elif 'api.groq.com' in base:
            live = catalogue_groq(key)
        elif 'nvidia.com' in base:
            live = catalogue_nim(key)
        elif 'api.mistral.ai' in base:
            live = catalogue_mistral(key)
        if live is not None and model in live:
            print('[BIZARRE] %s (%s) : 404/410 mais listé -> quota déguisé ? on ne touche pas' % (pid, model))
            continue
        cands = successeurs(pid, model, live)
        if live is None:
            print('[SANS-CATALOGUE] %s (%s) : ID mort, pas de catalogue (%s) -> au roulement'
                  % (pid, model, base))
            continue
        if not cands:
            print('[SANS-SUCCESSEUR] %s (%s) : ID mort, aucun successeur live -> au roulement' % (pid, model))
            continue
        applique = None
        for cand in cands:
            et2, txt2 = test_model(base, cand, key)
            if et2 == 'ok':
                applique = (cand, txt2)
                break
            print('[SUCC %s] %s -> %s' % (et2, cand, pid))
        if not applique:
            print('[ECHEC] %s : successeurs testés, aucun OK -> au roulement' % pid)
            continue
        cand, preuve = applique
        if dry:
            print('[DRY-RUN] %s : %s -> %s (preuve: %r)' % (pid, model, cand, preuve))
            continue
        if not backup_fait:
            tmp_b = BAK + '.tmp'
            with open(tmp_b, 'w', encoding='utf-8') as f:
                json.dump(json.load(open(PROVIDERS, encoding='utf-8')), f, indent=1, ensure_ascii=False)
            os.replace(tmp_b, BAK)
            backup_fait = True
        vieux = p['model']
        p['model'] = cand
        p['note'] = (p.get('note') or '') + \
            ' | 17/10+ REPARE-ID auto : %s mort (%s) -> %s testé OK (%r). enabled inchangé.' \
            % (vieux, etat, cand, preuve)
        repares += 1
        print('[REPARE] %s : %s -> %s (preuve: %r)' % (pid, vieux, cand, preuve))

    if repares and not dry:
        tmp = PROVIDERS + '.tmp'
        with open(tmp, 'w', encoding='utf-8') as f:
            json.dump(cfg, f, indent=1, ensure_ascii=False)
        os.replace(tmp, PROVIDERS)
        print('[OK] %d reparation(s) ecrites (atomique, backup %s)' % (repares, BAK))
    elif not repares:
        print('[OK] rien à réparer (tous les IDs testés sont vivants ou temporaires)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
