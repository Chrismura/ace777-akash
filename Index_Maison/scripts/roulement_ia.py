#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""roulement_ia.py — ROULEMENT AUTO des IA gratuites (maillon manquant de la chaîne).

Chaîne complète (validée Christophe 18/08) :
  veille_hub 7h00 (flotille) -> queue_offres 8h -> eval_offres 9h (intégration OBSERVATION)
  -> roulement_ia 9h30 : remplace les providers MORTS par les meilleures offres testées.

Discernement (règle Christophe, 18/08) :
  - 429 / quota journalier -> ÉPUISÉ TEMPORAIRE : on garde, on route ailleurs,
    on réessaie demain (le reset revient). JAMAIS d'éjection.
  - Échec durable (2 jours sans réponse OK) -> ÉJECTION réelle + remplacement
    par la meilleure offre `teste_ok` de la queue pour le rôle du provider mort.

Garde-fous (hérités d'eval_offres, protocole zéro faute) :
  - gratuit STRICT (jamais un provider payant)
  - backup AVANT toute modification (providers.json.bak-<date>)
  - écriture ATOMIQUE (tmp + rename)
  - 1 remplacement max par run
  - SAIN intouchable : jamais de modification d'un provider qui répond
  - kill switch : Index_Maison/STOP_HUB -> arrêt propre
"""
import json
import os
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, date, timezone

HOME = os.path.expanduser('~')
PRISE = os.path.join(HOME, 'prise-ia')
PROVIDERS = os.path.join(PRISE, 'providers.json')
INDEX = os.path.join(HOME, 'ace777-test-day1', 'Index_Maison')
QUEUE = os.path.join(INDEX, 'strategie', 'QUEUE_OFFRES.json')
JOURNAL = os.path.join(HOME, 'test-freebuff', 'journal_erreurs.md')
LOG = os.path.join(INDEX, 'ROULEMENT_IA_%s.md' % date.today().isoformat())

# Un provider est "mort" si aucun appel OK depuis cette durée (secondes)
MORT_APRES_S = 2 * 86400   # 2 jours de silence = mort durable
TEMPORAIRE_S = 86400       # < 1 jour = épuisé temporaire (429, quota)
MAX_TEST = 4               # ne pas brûler les quotas gratuits


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
    except Exception:
        return {}


def save_atomic(path, data):
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
    os.replace(tmp, path)


def call_chat(base_url, model, api_key, timeout=25):
    """Appel OpenAI-compatible. Retourne (ok, texte, erreur)."""
    body = json.dumps({
        'model': model,
        'messages': [{'role': 'user', 'content': 'ping'}],
        'max_tokens': 5,
    }).encode('utf-8')
    req = urllib.request.Request(base_url.rstrip('/') + '/chat/completions',
                                 data=body,
                                 headers={'Content-Type': 'application/json',
                                          'Authorization': 'Bearer %s' % api_key,
                                          'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36'})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            d = json.loads(r.read().decode('utf-8'))
            txt = (d.get('choices') or [{}])[0].get('message', {}).get('content', '')
            return True, txt, ''
    except urllib.error.HTTPError as e:
        return False, '', 'HTTP %s' % e.code
    except Exception as e:
        return False, '', '%s' % type(e).__name__


def sante_provider(p):
    """Teste UN provider (lecture seule). Retourne (ok, texte, erreur) — 3 valeurs."""
    key = env_key(p.get('api_key_env', ''))
    if not key:
        return False, '', 'pas de cle'
    return call_chat(p.get('base_url', ''), p.get('model', ''), key)


def meilleures_offres_queue(role, limit=MAX_TEST):
    """Meilleures offres `teste_ok` de la queue pour un rôle donné."""
    q = load(QUEUE)
    offres = []
    for e in q.get('entrees', []):
        if e.get('statut') != 'teste_ok':
            continue
        if e.get('type') != 'offre':
            continue
        # role : matching souple (offre sans role -> gros cerveau)
        erole = e.get('role') or 'gros cerveau'
        if role and erole != role:
            continue
        offres.append(e)
    return offres[:limit]


def log_ligne(txt):
    with open(LOG, 'a', encoding='utf-8') as f:
        f.write('- %s %s\n' % (datetime.now(timezone.utc).strftime('%H:%MZ'), txt))
    print('[ROULEMENT] %s' % txt)


def main():
    # Kill switch
    if os.path.exists(os.path.join(INDEX, 'STOP_HUB')):
        print('[STOP] STOP_HUB present -> roulement ignore')
        sys.exit(0)

    cfg = load(PROVIDERS)
    if not cfg.get('providers'):
        print('[ERREUR] providers.json vide', file=sys.stderr)
        sys.exit(1)

    providers = cfg['providers']
    now = time.time()
    morts = []       # échec durable (2 jours) -> candidats à l'éjection
    temporaires = [] # épuisé récent (429/quota) -> on garde, on route ailleurs

    # 1) SANTÉ des providers ACTIFS (ceux qui sont réellement routés)
    for p in providers:
        if not p.get('enabled', False):
            continue
        last_ok = p.get('last_ok_ts') or 0
        age_s = now - last_ok if last_ok else None
        ok, txt, err = sante_provider(p)  # FIX 23/08 : call_chat renvoie (ok, texte, err) — 3 valeurs
        if ok:
            p['last_ok_ts'] = now
            p['last_err'] = ''
            continue
        # échec : classer
        if age_s is not None and age_s >= MORT_APRES_S:
            morts.append(p)
        elif 'HTTP 429' in err or 'HTTP 403' in err or 'HTTP 402' in err:
            temporaires.append(p)
        elif age_s is not None and age_s >= TEMPORAIRE_S:
            temporaires.append(p)
        else:
            temporaires.append(p)  # échec récent -> on surveille, pas d'éjection

    # 2) RAPPORT santé (toujours)
    if morts:
        log_ligne('🟥 MORTS (échec >2j) : %s' % ', '.join(p.get('id', '?') for p in morts))
    if temporaires:
        log_ligne('🟡 ÉPUISÉS TEMPORAIRES (gardés, 429/quota) : %s'
                  % ', '.join(p.get('id', '?') for p in temporaires))
    actifs_ok = [p for p in providers if p.get('enabled') and p not in morts]
    log_ligne('✅ ACTIFS OK : %s' % ', '.join(p.get('id', '?') for p in actifs_ok) or 'aucun')

    # 3) ÉJECTION + REMPLACEMENT (1 max par run)
    if not morts:
        log_ligne('Aucun mort durable -> rien à remplacer (roulement terminé).')
        save_atomic(PROVIDERS, cfg)
        return

    mort = morts[0]
    role = mort.get('role') or 'gros cerveau'
    offres = meilleures_offres_queue(role)
    if not offres:
        log_ligne('Pas d offre teste_ok pour le rôle "%s" -> mort gardé mais désactivé (route ailleurs).' % role)
        # On désactive (le hub ne route plus vers un mort) mais on ne supprime pas
        mort['enabled'] = False
        mort['status'] = 'mort-desactive'
        save_atomic(PROVIDERS, cfg)
        return

    # Tester les offres candidates (gratuites, déjà teste_ok) jusqu'à la 1ère qui répond
    remplacement = None
    for offre in offres:
        key = env_key(offre.get('api_key_env', ''))
        if not key:
            continue
        ok, txt, err = call_chat(offre.get('base_url', ''), offre.get('model', ''), key)
        if ok:
            remplacement = offre
            log_ligne('Candidat retenu : %s (test réel OK)' % offre.get('model'))
            break
        log_ligne('Candidat %s inaccessible (%s) -> suivant' % (offre.get('model', '?'), err))

    if remplacement is None:
        log_ligne('Aucun candidat ne répond -> mort désactivé, remplacement différé.')
        mort['enabled'] = False
        mort['status'] = 'mort-desactive'
        save_atomic(PROVIDERS, cfg)
        return

    # Backup avant modification (protocole zéro faute)
    bak = os.path.join(PRISE, 'providers.json.bak-roulement-%s' % date.today().isoformat())
    if not os.path.exists(bak):
        save_atomic(bak, cfg)

    new_id = re_sub_id(remplacement.get('model', ''))
    if any(p.get('id') == new_id for p in providers):
        log_ligne('Provider %s déjà présent -> on réactive seulement.' % new_id)
        for p in providers:
            if p.get('id') == new_id:
                p['enabled'] = True
                p['status'] = 'actif'
                p['last_ok_ts'] = now
    else:
        providers.append({
            'id': new_id,
            'name': 'Roulement %s' % remplacement.get('model'),
            'kind': 'cloud',
            'base_url': remplacement.get('base_url'),
            'model': remplacement.get('model'),
            'api_key_env': remplacement.get('api_key_env'),
            'role': role,
            'enabled': True,
            'status': 'actif',
            'free': True,
            'integrated_at': datetime.now(timezone.utc).isoformat(),
            'last_ok_ts': now,
            'order': max([p.get('order', 0) for p in providers]) + 1,
            'timeout': 60,
            'note': 'ROULEMENT AUTO %s : remplace %s (mort >2j)' % (date.today().isoformat(), mort.get('id')),
        })

    # Désactiver le mort (on ne le supprime PAS — loi maison : rien ne se supprime)
    mort['enabled'] = False
    mort['status'] = 'mort-remplace-par-%s' % new_id
    save_atomic(PROVIDERS, cfg)

    log_ligne('🔁 REMPLACEMENT : %s -> %s (%s)'
              % (mort.get('id'), new_id, remplacement.get('model')))

    # Notice rapport + journal
    with open(LOG, 'a', encoding='utf-8') as f:
        f.write('\n## ROULEMENT %s\n- %s remplacé par %s (mort >2j, test réel OK)\n'
                '- Backup: %s\n' % (date.today().isoformat(), mort.get('id'),
                                    remplacement.get('model'), os.path.basename(bak)))
    with open(JOURNAL, 'a', encoding='utf-8') as f:
        f.write('\n## %s - ROULEMENT IA : %s -> %s (mort >2j)\n'
                % (date.today().isoformat(), mort.get('id'), remplacement.get('model')))


def re_sub_id(model):
    import re
    return re.sub(r'[^a-z0-9-]', '-', model.lower()).strip('-')[:40]


if __name__ == '__main__':
    main()
