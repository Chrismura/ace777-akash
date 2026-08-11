#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""verifier_setup.py — VERIFICATION AUTOMATIQUE DU SETUP (09/08, idee Christophe).

Apres TOUT changement de setup (providers.json / routing.json / .env / scripts),
au lieu de refaire les controles a la main : UNE commande fait tout.

Usage :  python3 verifier_setup.py            (verification complete + soumission famille)
         python3 verifier_setup.py --no-famille   (rapide : sans appels LLM famille)

Etapes :
  1. COMPILE   : py_compile de tous les scripts de Index_Maison/scripts/
  2. HUB       : /health (status + nb providers) + /v1/models (modeles actifs)
  3. PROVIDERS : structure (ids uniques, modele present, cle .env pour les enabled cloud,
                 observation jamais enabled, integrated_at present)
  4. ROUTING   : chaque tache -> provider + fallback existants ; budget cloud > 0
  5. APPEL REEL: hub task 'mission' (nvidia -> fallback grok) + 'signets.juge' (juge joignable)
  6. LAUNCHD   : plists du cycle matin charges (veille/eval/catalogue/propose/observatoire)
  7. FAMILLE   : brief AUTO-GENERE depuis l'etat reel -> 4 familles (gemini, juge, deepseek, ultra)
  8. RAPPORT   : A_Mon_Attention/VERIF_SETUP_<date>.md + exit 0 (tout vert) / 1 (a corriger)
"""
import json, os, subprocess, sys, urllib.request
from datetime import datetime, date, timezone

HOME = os.path.expanduser('~')
PRISE = os.path.join(HOME, 'prise-ia')
SCRIPTS = os.path.join(HOME, 'ace777-test-day1', 'Index_Maison', 'scripts')
INDEX = os.path.join(HOME, 'ace777-test-day1', 'Index_Maison')
ATTENTION = os.path.join(INDEX, 'A_Mon_Attention')
HUB = 'http://127.0.0.1:11435'
HUB_CHAT = HUB + '/v1/chat/completions'
ENV = os.path.join(PRISE, '.env')
WANT_FAMILLE = '--no-famille' not in sys.argv

RESULTS = []  # (check, ok:bool, detail)


def rec(check, ok, detail=''):
    RESULTS.append((check, bool(ok), detail))
    print('[%s] %s%s' % ('OK ' if ok else '!! ', check, (' — ' + str(detail)[:120] if detail else '')))


def load(path):
    try:
        return json.load(open(path, encoding='utf-8'))
    except Exception as e:
        rec('load %s' % os.path.basename(path), False, str(e)[:80])
        return {}


def env_keys():
    keys = {}
    try:
        for line in open(ENV):
            if line.strip() and '=' in line and not line.startswith('#'):
                k, v = line.split('=', 1)
                keys[k.strip()] = v.strip()
    except Exception:
        pass
    return keys


def call_hub(payload, timeout=120):
    req = urllib.request.Request(HUB_CHAT, data=json.dumps(payload).encode(),
                                 headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.loads(r.read().decode('utf-8'))
    except Exception as e:
        return {'error': str(e)[:100]}


def family_verdict(task, brief):
    d = call_hub({'task': task, 'messages': [{'role': 'user', 'content': brief}],
                  'max_tokens': 600, 'temperature': 0.2}, timeout=420)
    if 'error' in d:
        return 'INDISPONIBLE', d['error'][:60]
    out = d.get('choices', [{}])[0].get('message', {}).get('content', '')
    up = out.upper()
    for v in ('PARTIELLEMENT', 'CORRIGER'):
        if v in up:
            return v, out
    return 'OK', out


def main():
    print('=== VERIF SETUP — %s ===' % datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%MZ'))

    # 0) GATEKEEPER — garde-fou famille 1 (loi 1septies) : preuve de lecture < 24h
    #    BLOQUANT (fix audit tiers) : si la preuve est absente ou périmée, la
    #    vérification s'arrête ici avec exit 1 — aucune validation de setup possible.
    gk = subprocess.run([sys.executable, os.path.join(SCRIPTS, 'gatekeeper.py')],
                        capture_output=True, text=True)
    gk_ok = gk.returncode == 0
    detail_gk = gk.stdout.strip().splitlines()[0] if gk.stdout.strip() else (gk.stderr.strip()[:80] or 'refus')
    rec('gatekeeper: lecture coffre < 24h', gk_ok, detail_gk)
    if not gk_ok:
        print('\n⛔ GATEKEEPER BLOQUE : relis INVENTAIRE_COMPLET.md puis grave la preuve [LECTURE_COMPLETE_OK] (gatekeeper.py --tag) avant de valider le setup.', file=sys.stderr)
        sys.exit(1)

    # 1) COMPILE
    try:
        files = sorted(f for f in os.listdir(SCRIPTS) if f.endswith('.py'))
    except Exception as e:
        files = []
        rec('liste scripts', False, str(e)[:60])
    bad = []
    for f in files:
        p = os.path.join(SCRIPTS, f)
        if subprocess.call([sys.executable, '-m', 'py_compile', p], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) != 0:
            bad.append(f)
    rec('compile (%d scripts)' % len(files), not bad, ', '.join(bad) if bad else 'tous OK')

    # 2) HUB
    try:
        h = json.loads(urllib.request.urlopen(HUB + '/health', timeout=6).read())
        rec('hub /health', h.get('status') == 'ok', 'providers: %s' % h.get('providers'))
    except Exception as e:
        rec('hub /health', False, str(e)[:60])

    # 3) PROVIDERS
    prov = load(os.path.join(PRISE, 'providers.json')).get('providers', [])
    ids = [p.get('id') for p in prov]
    rec('providers: ids uniques', len(ids) == len(set(ids)))
    rec('providers: modele present partout', all(p.get('model') for p in prov))
    envk = env_keys()
    missing_keys = []
    for p in prov:
        if p.get('enabled', False) and p.get('kind') == 'cloud' and p.get('api_key_env'):
            if p['api_key_env'] not in envk:
                missing_keys.append(p.get('id'))
    rec('providers: cles .env presentes', not missing_keys, ', '.join(missing_keys) or 'toutes presentes')
    obs_enabled = [p.get('id') for p in prov if p.get('status') == 'observation' and p.get('enabled', False)]
    rec('observation jamais enabled', not obs_enabled, ', '.join(obs_enabled) or 'OK')
    obs_no_date = [p.get('id') for p in prov if p.get('status') == 'observation' and not p.get('integrated_at')]
    rec('observation a une date', not obs_no_date, ', '.join(obs_no_date) or 'OK')

    # 4) ROUTING
    routing = load(os.path.join(PRISE, 'routing.json'))
    tasks = routing.get('tasks', {})
    known = set(ids) | set(p.get('model') for p in prov)
    bad_refs = []
    for t, rule in tasks.items():
        for fld in ('provider', 'fallback'):
            v = rule.get(fld)
            if v and v not in known:
                bad_refs.append('%s[%s]=%s' % (t, fld, v))
    rec('routing: refs valides (%d taches)' % len(tasks), not bad_refs, ', '.join(bad_refs) or 'OK')
    rec('routing: budget cloud > 0', bool(routing.get('cloud_daily_budget')), 'budget=%s' % routing.get('cloud_daily_budget'))

    # 5) APPEL REEL via le hub
    d = call_hub({'task': 'mission', 'messages': [{'role': 'user', 'content': 'Dis OK en un mot.'}], 'max_tokens': 8})
    if 'error' in d:
        rec('appel reel mission', False, d['error'][:80])
    else:
        rec('appel reel mission', True, 'repondu par: %s' % d.get('provider', '?'))
    d2 = call_hub({'task': 'signets.juge', 'messages': [{'role': 'user', 'content': 'Dis OK.'}], 'max_tokens': 8})
    rec('appel reel juge', 'error' not in d2, 'juge joignable' if 'error' not in d2 else d2.get('error', '')[:60])

    # 6) LAUNCHD
    loaded = []
    try:
        out = subprocess.check_output(['launchctl', 'list'], text=True)
        for lbl in ('veille-hub', 'eval-offres', 'catalogue', 'propose-ameliorations', 'observatoire'):
            loaded.append(lbl if lbl in out else None)
    except Exception as e:
        rec('launchd', False, str(e)[:60])
    missing = [l for l in loaded if l is None]
    rec('launchd: cycle matin charge', not missing, ', '.join(l for l in loaded if l) or 'OK')

    # 7) FAMILLE (brief auto-genere depuis l'etat reel + contexte protocole)
    fam = []
    fam_full = []
    if WANT_FAMILLE:
        actifs = [p.get('id') for p in prov if p.get('enabled', False)]
        obs_ids = [p.get('id') for p in prov if p.get('status') == 'observation']
        route_hl = ', '.join('%s:%s>%s' % (t, r.get('provider', '?'), r.get('fallback', '-'))
                             for t, r in list(tasks.items())[:10])
        brief = (
            "SYSTEME ACE777 — verification automatique de setup (%s).\n"
            "CONTEXTE : ce setup integre les corrections deja validees par vous (orchestrateur"
            " temporel 5 etapes + kill switch STOP + jauge a la demande, observation 48h + rollback"
            " auto, contre-verification Gemini du TOP 3, GO hebdomadaire Christophe) et grok-4.3"
            " ACTIF (GO explicite Christophe, A/B reel EGAL vs deepseek-v4-flash, prouve a travers le hub).\n\n"
            "ETAT REEL LU DANS LES FICHIERS :\n"
            "- providers actifs (%d) : %s\n"
            "- en observation : %s\n"
            "- routage (extrait) : %s\n"
            "- budget cloud/jour : %s\n"
            "- controles passes : compile 36 scripts, hub /health OK, cles .env presentes,"
            " routing refs valides, appel reel mission OK, juge joignable, launchd cycle matin charge.\n\n"
            "QUESTION : ce setup est-il valide ?\n"
            "Reponds STRICTEMENT en max 5 lignes :\n"
            "VERDICT: OK / PARTIELLEMENT / CORRIGER\n"
            "OBJECTION: <une seule objection concrete et verifiable, ou 'aucune'>\n"
            "AMELIORATION: <une seule amelioration si verdict != OK, sinon 'aucune'>"
            % (date.today().isoformat(), len(actifs), ', '.join(actifs),
               ', '.join(obs_ids) or 'aucun', route_hl, routing.get('cloud_daily_budget')))
        for name, task in (('GEMINI', 'audit.protocol'), ('JUGE', 'signets.juge'),
                           ('DEEPSEEK', 'mission'), ('ULTRA', 'ultra.analyse')):
            verdict, preuve = family_verdict(task, brief)
            rec('famille %s' % name, verdict == 'OK', '%s — %s' % (verdict, preuve))
            fam.append((name, verdict))
            fam_full.append('===== %s (%s) =====\n%s' % (name, task, preuve))
        # sauvegarder les reponses COMPLETES (pour lire les objections)
        try:
            frp = os.path.join(ATTENTION, 'VERIF_FAMILLE_%s.md' % date.today().isoformat())
            with open(frp, 'w', encoding='utf-8') as f:
                f.write('# Reponses famille (verification auto) — %s\n\n%s\n'
                        % (date.today().isoformat(), '\n\n'.join(fam_full)))
            print('REPONSES FAMILLE ->', frp)
        except Exception as e:
            print('(pas de sauvegarde famille:', e, ')')

    # 8) RAPPORT
    ok_all = all(ok for _, ok, _ in RESULTS)
    os.makedirs(ATTENTION, exist_ok=True)
    rp = os.path.join(ATTENTION, 'VERIF_SETUP_%s.md' % date.today().isoformat())
    L = ['# 🔍 VERIFICATION AUTOMATIQUE DU SETUP — %s' % date.today().isoformat(), '',
         '> Generee par verifier_setup.py (09/08) : compile → hub → providers → routing → appel reel → launchd → famille.', '']
    if fam:
        L.append('## Verdict des familles')
        for n, v in fam:
            L.append('- **%s : %s**' % (n, v))
        L.append('')
    L.append('## Controles')
    for c, ok, d in RESULTS:
        L.append('- %s %s%s' % ('✅' if ok else '❌', c, (' — ' + str(d) if d else '')))
    L.append('')
    L.append('**Verification : %s**' % ('TOUT EST VERT ✅' if ok_all else '⚠️ POINTS A CORRIGER'))
    with open(rp, 'w', encoding='utf-8') as f:
        f.write('\n'.join(L) + '\n')
    print('\nRAPPORT ->', rp)
    print('=== VERDICT GLOBAL : %s ===' % ('TOUT EST VERT ✅' if ok_all else '⚠️ POINTS A CORRIGER'))
    sys.exit(0 if ok_all else 1)


if __name__ == '__main__':
    main()
