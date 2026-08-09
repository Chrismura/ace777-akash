#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""catalog_providers.py — genere CATALOGUE_PROVIDERS.md (1 vue du hub).

Gagnant du A/B codeurs (09/08) : Qwen3-Coder (code complete par le superviseur :
chemins reels prise-ia, section preuves, roles depuis routing, ecriture atomique).
Genere chaque matin par veille_hub.py (section 5bis). 0 dependance, Python 3.9.
"""
import json
import os
import tempfile
import shutil
from datetime import date

HOME = os.path.expanduser('~')
PRISE = os.path.join(HOME, 'prise-ia')
INDEX = os.path.join(HOME, 'ace777-test-day1', 'Index_Maison')
OUT = os.path.join(INDEX, 'CATALOGUE_PROVIDERS.md')

# Kill switch (correction famille 09/08 : STOP tue tout sauf le hub)
if os.path.exists(os.path.join(INDEX, 'STOP_HUB')):
    print('[STOP] STOP_HUB present -> catalogue ignore')
    raise SystemExit(0)


def load_json(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return {}


def load_preuves(path):
    if not os.path.exists(path):
        return []
    with open(path, 'r', encoding='utf-8') as f:
        return [l.strip() for l in f if l.strip()]


def main():
    providers = load_json(os.path.join(PRISE, 'providers.json')).get('providers', [])
    routing = load_json(os.path.join(PRISE, 'routing.json')).get('tasks', {})
    preuves = load_preuves(os.path.join(INDEX, 'PREUVES_HUB.txt'))

    # roles : tache -> provider id ; on inverse pour donner les roles par provider
    def get_roles(pid):
        return sorted([t for t, c in routing.items() if c.get('provider') == pid])

    role_labels = {
        'ada.sanity': 'demarrage', 'cortana.brief': 'brief vocal',
        'audit.protocol': 'audit protocole', 'signets.synthese': 'synthese bookmarks',
        'chat.local': 'chat interactif', 'cortana.analyse': 'analyse',
        'coffre.ask': 'RAG coffre', 'qwen.elabore': 'elaboration',
        'qwen.btc': 'analyse BTC', 'signets.lot2': 'tri signets',
        'analyse.profonde': 'analyse profonde', 'signets.juge': 'JUGE',
        'mission': 'missions', 'ultra.analyse': 'analyse forte',
        'inferx.analyse': 'analyse', 'code.ia': 'CODE',
    }

    def fmt_roles(pid):
        rs = get_roles(pid)
        if not rs:
            return '-'
        return ' / '.join(role_labels.get(r, r) for r in rs)

    actifs, attente, cote, observation = [], [], [], []
    for p in providers:
        pid = p.get('id', '?')
        note = p.get('note') or ''
        model = p.get('model') or '?'
        roles = fmt_roles(pid)
        if p.get('status') == 'observation':
            observation.append((pid, model, roles, note))
        elif p.get('enabled'):
            actifs.append((pid, model, roles, note))
        elif 'payant' in note.lower() or '402' in note.lower():
            cote.append((pid, model, roles, note))
        else:
            attente.append((pid, model, roles, note))

    def section(title, items):
        L = ['## %s' % title, '',
             '| Role | Modele | Statut | Note |',
             '|------|--------|--------|------|']
        if not items:
            return '## %s\n\n*aucun*\n' % title
        for pid, model, roles, note in items:
            L.append('| %s | `%s` | %s | %s |' % (roles, model, pid, (note or '-')[:90]))
        return '\n'.join(L) + '\n'

    lines = ['# CATALOGUE DES PROVIDERS — ACE777', '',
             '*Genere le %s par catalog_providers.py (gagnant A/B codeurs 09/08). '
             'Rafraichi a chaque veille du matin.*' % date.today().isoformat(), '']
    lines.append('**Actifs : %d · En observation : %d · En attente : %d · De cote (payant) : %d**'
                 % (len(actifs), len(observation), len(attente), len(cote)))
    lines.append('')
    lines.append(section('ACTIFS', actifs))
    lines.append(section('EN OBSERVATION (48h avant activation, jamais route)', observation))
    lines.append(section('EN ATTENTE (cle manquante ou desactive)', attente))
    lines.append(section('DE COTE (payant / obsolète)', cote))

    if preuves:
        lines.append('## Preuves (A/B, benchmarks)', '')
        for pv in preuves[:12]:
            lines.append('- %s' % pv[:150])
        lines.append('')

    content = '\n'.join(lines)
    tmp_fd, tmp_path = tempfile.mkstemp(suffix='.md', dir=os.path.dirname(OUT))
    try:
        with os.fdopen(tmp_fd, 'w', encoding='utf-8') as f:
            f.write(content)
        shutil.move(tmp_path, OUT)
    except Exception:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)
        raise
    print('CATALOGUE_PROVIDERS.md ->', OUT)


if __name__ == '__main__':
    main()
