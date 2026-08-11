#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""propose_ameliorations.py — RITUEL AMELIORATION PROACTIVE (09/08, grave).

Reproche Christophe : « tu proposes rarement, tu executes ». Correctif structurel :
en debut de session, AVANT tout travail, je lis le backlog, je choisis TOP 3, je
soumets au juge (maker!=checker), GEMINI CONTRE-VERIFIE (famille differente —
correction famille 09/08, point 3 : le juge ne doit jamais valider seul), et je
presente a Christophe. Personne ne valide seul.

Sources du backlog :
  - Evaluations/TABLEAU_PEPITES_2026-08-08.md (43 INTEGRER / 14 VERIFIER)
  - AUTO_EVOL/IDEES.md (idees Qwen solo)
  - VEILLE_HUB_<date>.md (offres du jour)
Sortie : ~/ace777-test-day1/Index_Maison/A_Mon_Attention/PROPOSITIONS_AMELIORATIONS.md
"""
import json, os, urllib.request
from datetime import date

HOME = os.path.expanduser('~')
VAULT = os.path.join(HOME, 'Documents', 'Obsidian_ACE777')
INDEX = os.path.join(HOME, 'ace777-test-day1', 'Index_Maison')
HUB = 'http://127.0.0.1:11435/v1/chat/completions'

# Kill switch (correction famille : STOP tue tout sauf le hub)
if os.path.exists(os.path.join(INDEX, 'STOP_HUB')):
    print('[STOP] STOP_HUB present -> rituel propose ignore')
    raise SystemExit(0)


def read_head(path, n=25):
    try:
        lines = open(path, encoding='utf-8').read().splitlines()
        return '\n'.join(lines[:n])
    except Exception:
        return ''


def call_hub(task, prompt, max_tokens=900, timeout=300):
    payload = json.dumps({
        'task': task,
        'messages': [{'role': 'user', 'content': prompt}],
        'max_tokens': max_tokens, 'temperature': 0.2,
    }).encode()
    req = urllib.request.Request(HUB, data=payload, headers={'Content-Type': 'application/json'})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            d = json.loads(resp.read().decode('utf-8'))
        return d['choices'][0]['message']['content']
    except Exception as e:
        return None


def call_juge(prompt):
    out = call_hub('signets.juge', prompt)
    return out if out else 'JUGE INDISPONIBLE: (pas de reponse du hub)'


def call_gemini(prop, backlog_tete):
    """Contre-verification par GEMINI (famille differente du juge) — correction famille 09/08."""
    prompt = (
        "Tu es l'auditeur protocolaire (famille Gemini). Le JUGE (famille differente) a propose\n"
        "ce TOP 3 d'ameliorations pour le systeme ACE777. Contre-verifie-le de facon critique.\n\n"
        "TOP 3 PROPOSE PAR LE JUGE :\n%s\n\n"
        "EXTRAIT DU BACKLOG (pour recouper) :\n%s\n\n"
        "Reponds STRICTEMENT en max 8 lignes :\n"
        "VERDICT: OK ou A MODIFIER\n"
        "OBJECTIONS: <une seule objection concrete, ou 'aucune'>\n"
        "PRIORITE: <celle que TU ferais en premier et pourquoi, 1-2 phrases>"
        % (prop[:2000], backlog_tete[:1200])
    )
    # audit.protocol route vers gemini (routing.json) ; repli cortana.analyse (gemini aussi)
    for task in ('audit.protocol', 'cortana.analyse'):
        out = call_hub(task, prompt, max_tokens=500, timeout=240)
        if out:
            return out
    return 'CONTRE-VERIFICATION INDISPONIBLE (hub silencieux)'


def main():
    # 1) LIRE le backlog (3 sources)
    pepites = read_head(os.path.join(VAULT, 'Evaluations', 'TABLEAU_PEPITES_2026-08-08.md'), 60)
    idees = read_head(os.path.join(VAULT, 'AUTO_EVOL', 'IDEES.md'), 20)
    veille = read_head(os.path.join(INDEX, 'VEILLE_HUB_%s.md' % date.today().isoformat()), 25)
    if not pepites and not idees:
        print('[INFO] backlog vide — rien a proposer')
        return

    backlog = '=== PEPITES (INTEGRER/VERIFIER, extrait) ===\n%s\n\n=== IDEES QWEN ===\n%s\n\n=== VEILLE DU JOUR ===\n%s' % (pepites[:3000], idees[:1200], veille[:1500])

    # 2) juge propose le TOP 3 (maker!=checker : je ne choisis pas seul)
    prompt = """Tu es le juge independant. Voici le BACKLOG d'ameliorations du systeme ACE777
(pepites triees, idees, veille du jour).

BACKLOG :
%s

TACHE : choisis les 3 meilleures ameliorations A PROPOSER a Christophe pour cette session.
Critere : valeur pour le systeme (moins de RAM / moins de temps / plus de fiabilite) vs cout
(heures de travail). Priorite aux pEpites marquees INTEGRER non encore appliquees.

Reponds STRICTEMENT en 3 blocs (chacun max 4 lignes) :
1. <titre court>
   QUOI: <une phrase>
   PREUVE: <la source, ex. pePite #N ou veille>
   IMPACT: <ce que ca ameliore concretement>
2. ...
3. ...
Puis une ligne : RECO: <celle a faire en premier, une phrase>""" % backlog
    prop = call_juge(prompt)

    # 3) CONTRE-VERIFICATION GEMINI (famille differente du juge) — correction famille 09/08
    contre = call_gemini(prop, backlog)

    # 4) PRESENTER a Christophe (juge propose + Gemini contre-verifie -> Christophe tranche)
    out_dir = os.path.join(INDEX, 'A_Mon_Attention')
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'PROPOSITIONS_AMELIORATIONS.md')
    body = ('# 💡 PROPOSITIONS D\'AMELIORATION — %s\n\n'
            '> Genere par propose_ameliorations.py (rituel proactif 09/08).\n'
            '> Le juge PROPOSE (maker!=checker), GEMINI CONTRE-VERIFIE (famille differente),\n'
            '> Christophe TRANCHE. Personne ne valide seul (loi 1quater).\n\n'
            '## Top 3 — proposé par le juge\n\n%s\n\n'
            '## Contre-vérification — Gemini (famille différente)\n\n%s\n\n'
            '---\n'
            '_Backlog source : TABLEAU_PEPITES_2026-08-08 (43 INTEGRER / 14 VERIFIER) + IDEES + VEILLE_HUB._\n'
            % (date.today().isoformat(), prop, contre))
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(body)
    print('PROPOSITIONS_AMELIORATIONS.md ->', out_path)
    print(prop[:700])
    print('--- CONTRE-VERIF GEMINI ---')
    print(contre[:400])


if __name__ == '__main__':
    main()
