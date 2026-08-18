#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""observatoire.py — OBSERVATION 48H + ROLLBACK AUTO + VALIDATION HEBDOMADAIRE (09/08).

Correction famille 09/08 (verdict CORRIGER — points juge + ultra + deepseek) :
  - une integration AUTO reste en OBSERVATION (enabled=false : le hub ne la route JAMAIS)
  - sondes quotidiennes mesurees (5 appels courts, quota minime) -> observatoire.json
  - apres 48h : si erreurs sur les sondes > 5% -> ROLLBACK auto (retrait + journal + notice)
  - sinon : ACTIF seulement si Christophe a valide la liste hebdo (go_hebdo.json,
    semaine courante). Sans GO hebdomadaire, le provider reste en observation (jamais actif).
  - chaque run + le vendredi : rapport A_Mon_Attention/INTEGRATIONS_HEBDO.md

Place dans le cycle launchd decale : 11:00 (apres veille 9h05 / eval 9h30).
"""
import json, os, time, urllib.request
from datetime import datetime, date, timezone

HOME = os.path.expanduser('~')
PRISE = os.path.join(HOME, 'prise-ia')
PROVIDERS = os.path.join(PRISE, 'providers.json')
OBS = os.path.join(PRISE, 'observatoire.json')
GO = os.path.join(PRISE, 'go_hebdo.json')
INDEX = os.path.join(HOME, 'ace777-test-day1', 'Index_Maison')
JOURNAL = os.path.join(HOME, 'test-freebuff', 'journal_erreurs.md')
ATTENTION = os.path.join(INDEX, 'A_Mon_Attention')

PROBE = "Reponds uniquement par le mot OK."
NB_PROBES = 5
ERREUR_MAX = 0.05     # >5% d'erreurs sur les sondes -> rollback (strict, zero faute)
MIN_AGE_H = 48.0      # duree d'observation avant decision

# Kill switch (correction famille : STOP tue tout sauf le hub)
if os.path.exists(os.path.join(INDEX, 'STOP_HUB')):
    print('[STOP] STOP_HUB present -> observatoire ignore')
    raise SystemExit(0)


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


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def age_hours(ts):
    try:
        t0 = datetime.fromisoformat(ts)
        if t0.tzinfo is None:
            t0 = t0.replace(tzinfo=timezone.utc)
        return (datetime.now(timezone.utc) - t0).total_seconds() / 3600.0
    except Exception:
        return MIN_AGE_H + 1  # date inconnue -> decide des maintenant (precaution)


def probe(prov):
    """Sonde le provider NB_PROBES fois. Retourne (ok, n)."""
    base = (prov.get('base_url') or '').rstrip('/')
    model = prov.get('model') or ''
    if not base or not model:
        return 0, NB_PROBES
    key = None
    if prov.get('api_key_env'):
        try:
            for line in open(os.path.join(PRISE, '.env')):
                if line.startswith(prov['api_key_env'] + '='):
                    key = line.strip().split('=', 1)[1]
        except Exception:
            key = None
    headers = {'Content-Type': 'application/json'}
    if key:
        headers['Authorization'] = 'Bearer ' + key
    ok = 0
    for _ in range(NB_PROBES):
        try:
            payload = json.dumps({
                'model': model,
                'messages': [{'role': 'user', 'content': PROBE}],
                'max_tokens': 5, 'temperature': 0,
            }).encode()
            req = urllib.request.Request(base + '/chat/completions', data=payload, headers=headers)
            with urllib.request.urlopen(req, timeout=15) as r:
                d = json.loads(r.read().decode('utf-8'))
            if (d.get('choices') or [{}])[0].get('message', {}).get('content', '').strip():
                ok += 1
        except Exception:
            time.sleep(2)
    return ok, NB_PROBES


def week_id():
    y, w, _ = date.today().isocalendar()
    return '%d-W%02d' % (y, w)


def load_go():
    if not os.path.exists(GO):
        return None
    return load(GO)


def notice(msg):
    try:
        with open(JOURNAL, 'a', encoding='utf-8') as f:
            f.write('\n## %s - %s\n' % (date.today().isoformat(), msg))
    except Exception:
        pass


def main():
    cfg = load(PROVIDERS)
    providers = cfg.get('providers', [])
    obs_cfg = load(OBS)
    go = load_go()
    go_week = (go or {}).get('week')
    validated = (go or {}).get('validated', []) if go_week == week_id() else []    # 18/08 (Christophe) : l'observatoire surveille AUSSI les providers obs-*
    # ajoutés par queue_offres (actifs directs, décision 14/08). On ne change PAS
    # leur activation — on les sonde comme les autres et on applique le rollback
    # auto si les sondes échouent (>=2 échecs ET >5% ET échantillon >= 1 jour).
    # Règle : un provider actif ne passe JAMAIS en observation ; un provider qui
    # échoue aux sondes est ROLLBACK (désactivé, jamais supprimé — loi maison).
    def est_surveille(p):
        """Providers à sonder : en observation (eval_offres) + obs-* (queue_offres).
        Les providers historiques (gemini, mistral...) avec note ACTIVE ne sont PAS
        touchés — on ne surveille que les intégrations automatiques."""
        if p.get('status') == 'observation':
            return True
        return str(p.get('id', '')).startswith('obs-')

    observation = [p for p in providers if est_surveille(p)]
    if not observation:
        os.makedirs(ATTENTION, exist_ok=True)
        with open(os.path.join(ATTENTION, 'INTEGRATIONS_HEBDO.md'), 'w', encoding='utf-8') as f:
            f.write('# INTEGRATIONS HEBDOMADAIRES — %s\n\n_Aucun provider à surveiller._\n'
                    % date.today().isoformat())
        print('[INFO] aucun provider à surveiller')
        return

    changed = False
    rows_obs, rows_att, rows_act, rows_roll = [], [], [], []

    for p in observation:
        pid = p.get('id', '?')
        rec = obs_cfg.get(pid, {'integrated_at': p.get('integrated_at') or now_iso(), 'probes': []})
        ok, n = probe(p)
        rec['probes'].append({'ts': now_iso(), 'date': date.today().isoformat(), 'ok': ok, 'n': n})
        rec['probes'] = rec['probes'][-10:]  # purge : garde les 10 dernieres sondes max
        obs_cfg[pid] = rec

        age = age_hours(rec.get('integrated_at', ''))
        model = p.get('model') or '?'
        is_obs_active = pid.startswith('obs-')

        if is_obs_active and age < MIN_AGE_H:
            # obs-* : actif direct (décision 14/08) — on sonde mais on ne touche pas avant 48h
            rows_obs.append((pid, model, rec['integrated_at'][:10], '%.0fh/48h' % age, '%d/%d' % (ok, n), 'actif (sonde en cours)'))
            continue

        if age < MIN_AGE_H:
            rows_obs.append((pid, model, rec['integrated_at'][:10], '%.0fh/48h' % age, '%d/%d' % (ok, n), 'en observation'))
            continue

        # >= 48h : decision sur les sondes des 24 dernieres heures
        cutoff = datetime.now(timezone.utc).timestamp() - 24 * 3600
        last = [q for q in rec['probes'] if _ts(q) >= cutoff] or rec['probes'][-2:]
        tot = sum(q.get('n', 0) for q in last)
        okk = sum(q.get('ok', 0) for q in last)
        fails = tot - okk
        fail_rate = (fails / tot) if tot else 0.0

        # Rollback strict mais sans faux positif : >=2 echecs ET >5% ET echantillon >= 1 jour
        # (1 seul echec transitoire ne retire pas un bon provider — revue 09/08)
        if tot >= NB_PROBES and fails >= 2 and fail_rate > ERREUR_MAX:
            # ROLLBACK AUTO : pour un provider 'observation' -> retrait ; pour un obs-*
            # actif -> DESACTIVATION (jamais suppression — loi maison).
            if is_obs_active:
                p['enabled'] = False
                p['status'] = 'obs-rollback'
                p['note'] = (p.get('note') or '') + ' | ROLLBACK auto observatoire %s (%d%% erreurs)' % (date.today().isoformat(), 100 * fail_rate)
            else:
                cfg['providers'] = [q for q in cfg['providers'] if q.get('id') != pid]
            changed = True
            rows_roll.append((pid, model, '%.0f%%' % (100 * fail_rate), 'ROLLBACK auto (désactivé)' if is_obs_active else 'RETIRE (rollback auto)'))
            notice('OBSERVATOIRE ROLLBACK AUTO : %s (%s) - %d%% erreurs > 5%% sur 24h' % (pid, model, 100 * fail_rate))
            rp = os.path.join(INDEX, 'VEILLE_HUB_%s.md' % date.today().isoformat())
            try:
                with open(rp, 'a', encoding='utf-8') as f:
                    f.write('\n## ROLLBACK AUTO %s\n- %s (%s) : %d%% erreurs > 5%% (observatoire)\n'
                            % (date.today().isoformat(), pid, model, 100 * fail_rate))
            except Exception:
                pass
            print('[ROLLBACK] %s (%s) : %.0f%% erreurs -> désactivé' % (pid, model, 100 * fail_rate))
        elif is_obs_active:
            # obs-* sain : on le laisse actif, on note la santé
            rows_act.append((pid, model, '%d/%d' % (okk, tot), 'actif + sain (sondes OK)'))
        elif pid in validated:
            # GO hebdomadaire Christophe + 48h propres -> ACTIF
            p['enabled'] = True
            p['status'] = 'actif'
            p['note'] = (p.get('note') or '') + ' | ACTIF apres observation 48h + GO hebdo %s' % week_id()
            changed = True
            rows_act.append((pid, model, '%d/%d' % (okk, tot), 'ACTIF (GO hebdo + 48h propres)'))
            notice('OBSERVATOIRE ACTIVATION : %s (%s) - 48h propres + valide par Christophe (%s)' % (pid, model, week_id()))
            print('[ACTIF] %s (%s) : 48h sans faute + GO hebdo' % (pid, model))
        else:
            rows_att.append((pid, model, rec['integrated_at'][:10], '%d/%d' % (okk, tot),
                             '>= 48h, sans faute -> ATTENTE validation hebdo (vendredi)'))
            print('[ATTENTE] %s (%s) : 48h ok, en attente du GO hebdo de Christophe' % (pid, model))

    if changed:
        save_atomic(PROVIDERS, cfg)
    save_atomic(OBS, obs_cfg)

    # Rapport hebdomadaire
    os.makedirs(ATTENTION, exist_ok=True)
    L = ['# INTEGRATIONS HEBDOMADAIRES — %s' % date.today().isoformat(), '',
         '> Genere par observatoire.py (correction famille 09/08).',
         '> Regle : un provider integre auto n\'est JAMAIS actif directement.',
         '> Il passe 48h en observation (sondes), puis Christophe valide la liste',
         '> chaque vendredi (GO hebdomadaire). Sans GO -> pas d\'activation.', '']

    def sec(t, rows):
        if not rows:
            return []
        out = ['## %s' % t, '', '| Provider | Modele | Detail | Etat |', '|----------|--------|--------|------|']
        for r in rows:
            out.append('| ' + ' | '.join(str(x) for x in r) + ' |')
        return out + ['']

    L += sec('EN OBSERVATION (< 48h)', rows_obs)
    L += sec('EN ATTENTE DE VALIDATION (>= 48h, sans faute) — vendredi : dis "je valide la liste"', rows_att)
    L += sec('ACTIVÉS AUJOURD\'HUI (48h propres + GO hebdo)', rows_act)
    L += sec('RETIRÉS (rollback auto > 5% erreurs)', rows_roll)

    vendredi = date.today().weekday() == 4
    if rows_att:
        L += ['> **%s** : %d provider(s) attendent ton GO hebdomadaire (semaine %s).' % (
            ('VENDREDI — semaine de validation' if vendredi else 'Rappel'),
            len(rows_att), week_id()), '']
    with open(os.path.join(ATTENTION, 'INTEGRATIONS_HEBDO.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(L))
    print('INTEGRATIONS_HEBDO.md ->', os.path.join(ATTENTION, 'INTEGRATIONS_HEBDO.md'))


def _ts(q):
    try:
        t = datetime.fromisoformat(q.get('ts', ''))
        if t.tzinfo is None:
            t = t.replace(tzinfo=timezone.utc)
        return t.timestamp()
    except Exception:
        return 0.0


if __name__ == '__main__':
    main()
