#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit famille 6 — RUN TEST DUO (2 sessions, 14/08) : mort neutralisée mais
harmonie duo dégradée. Avec la CLAUSE PERMANENTE Christophe (prompt).

CONTEXTE : on a lancé le run test de la correction anti-mort (safe_call,
genesis re-scellé d6977337, famille 6/6 + codeur + grille OK). Le lanceur 4H
(GO_VORTEX_V2 -> launch_vortex_v2_collab_4h_binance.sh) a une boucle
d'auto-relance (5s après arrêt prématuré sans STOP) : Session #1 (08:31) morte
en ~21 min, Session #2 (08:52) relancée automatiquement = run actuel.

Christophe : « la relance n'a pas l'harmonie, aptitude différente ».
Question centrale : (A) la mort silencieuse est-elle VRAIMENT neutralisée ?
(B) pourquoi le duo tourne-t-il en mode dégradé (ALPHA hésite, BETA micro-trades
plats) ? (C) la relance auto 4H doit-elle être modifiée ?

Chaque membre : (1) verdict global, (2) diagnostic mort session #1, (3) diagnostic
harmonie session #2, (4) correctifs GO-sized bornés (JAMAIS genesis, clause
meilleure logique prouvée), (5) indicateur pour le prochain run.
"""
import json
import os
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
ROOT = "/Users/christophe/ace777-test-day1"
OUT = os.path.join(ROOT, "Index_Maison", "AUDIT_RUN_DUO_2026-08-14")
os.makedirs(OUT, exist_ok=True)

MEMBRES = [
    ("GEMINI", "gemini.analyse", "Tu es GEMINI, auditeur en chef de la famille ACE777. Tu cherches les angles morts, tu structures, tu ne te contentes pas du premier récit."),
    ("DEEPSEEK", "deepseek.analyse", "Tu es DEEPSEEK, critique factuel de la famille ACE777. Tu exiges des preuves, tu donnes des contre-exemples, tu refuses les conclusions non étayées."),
    ("JUGE", "juge.tranche", "Tu es le JUGE de la famille ACE777. Tu tranches formellement : GO / GO AVEC RESERVES / NON. Tu es exigeant et tu donnes une raison courte et nette."),
    ("ULTRA", "inferx.analyse", "Tu es ULTRA, membre de la famille ACE777. Tu regardes la robustesse à l'échelle : ce qui casse en prod, en tempête, sous charge, sur du long terme."),
    ("INFERX", "inferx.analyse", "Tu es INFERX, membre de la famille ACE777. Tu regardes la logique interne : le flux exact, les garde-fous, les chemins d'erreur, les pièges bash."),
    ("GROK", "puter-grok.analyse", "Tu es GROK, démon 24/7 de la famille ACE777. Tu es pragmatique : tu vois ce qui casse vraiment en conditions réelles, tu vas droit au but."),
]

CONTEXTE = """\
RUN TEST DUO — 2 SESSIONS (14/08, testnet, aucun argent réel). Le correctif
anti-mort (safe_call) est ACTIF (genesis d6977337, re-scellé famille 6/6).
La mort silencieuse semble neutralisée, MAIS le duo tourne en mode dégradé.

================
CADRE (faits vérifiés, pas un récit)
================
- Lanceur : GO_VORTEX_V2.sh -> launch_vortex_v2_collab_4h_binance.sh
  (boucle while : auto-relance 5s si arrêt prématuré SANS fichier STOP).
- Session #1 : démarre 08:31:37Z (config ramp=13/13, BETA x3/200, ALPHA x13/800).
- Session #2 (actuelle) : démarre 08:52:33Z (relance auto, MÊME config exacte,
  header identique ligne à ligne). Run actif depuis ~25 min, aucun PROCESS_EXIT.
- Genesis = d6977337 (safe_call + trap ERR), vérifié par le préflight AVANT run.
- Le safe_call n'a loggé AUCUN WARN pendant les 2 sessions (les 3 warnings de
  /tmp/ace777_fatal_rc1.log = tests G2/G3 du superviseur, PAS du run).

================
SESSION #1 (08:31 -> 08:52, MORTE en 21 min)
================
- BETA (SCOUT) meurt le premier : PROCESS_EXIT rc=1 à 08:49:29Z.
  Derniers cycles BETA (log réel) :
  08:47:39 #78 SELL tension=1.03685 hold=7s exit=62833.10 pnl=-0.01363 (shockwave beta->alpha until_cycle=88)
  08:48:06 #80 SKIP wall_not_collapsed | 08:48:15 #81 SKIP momentum_too_small | ... | 08:48:43 #84 SKIP
  -> 08:49:29Z PROCESS_EXIT rc=1 (crash dump capturé, dernier état duo publié :
  role=SCOUT status=CLOSED reason=shock_inversion_stop cycle=92)
- ALPHA (HUNTER) survit 3 min seul puis meurt : dernier cycle #108 à 08:52:18
  "duo stale_state" (état du partenaire périmé) -> PROCESS_EXIT rc=1 à 08:52:26Z.
- CONCLUSION SESSION #1 : BETA meurt en "shock_inversion_stop" (sortie de
  trade par inversion de vitesse, ligne 2287 genesis) -> son état CLOSED est
  publié -> ALPHA perd son partenaire -> "duo stale_state" -> mort en chaîne.
  LE SAFE_CALL N'A RIEN INTERCEPTÉ (aucune des 10 lignes protégées en cause).

================
SESSION #2 (08:52 -> maintenant, VIVANTE mais dégradée)
================
- ALPHA : 130+ cycles SANS AUCUN fill. Il voit des tensions ÉLEVÉES mais bloque
  en boucle sur "duo no_trigger" / "duo no_state" (exemples log réel) :
  08:53:09 #3 tension=1.47 no_state | 08:54:10 #9 tension=6.03 no_trigger
  08:55:54 #20 tension=1.81 no_trigger | 08:57:55 #33 tension=2.95 no_trigger
  09:03:56 #72 tension=2.94 no_trigger | 09:06:03 #86 tension=3.54 no_trigger
- BETA : ~100 cycles, ~10 micro-trades TOUS plats ou quasi (log réel) :
  08:54:02 #9 entry 62861.20 -> exit 62860.00 pnl=+0.0113 (conf 0.992)
  08:55:10 #15 entry 62861.20 -> exit 62861.20 pnl=0.0000 (conf 0.967)
  08:55:59 #19 entry 62861.20 -> exit 62861.20 pnl=0.0000
  08:56:30 #21 entry 62861.20 -> exit 62861.20 pnl=0.0000
  08:57:36 #27 entry 62861.20 -> exit 62861.20 pnl=0.0000
  08:58:10 #29 entry 62861.20 -> exit 62858.40 pnl=+0.0263
  total session ~+0.05 USDT. Marché SANS tendance (setup qui dort : tensions
  souvent 0.0000x, déjà analysé AUDIT_CYCLES_PROMPTS 6/6 "à surveiller").
- OBSERVATION Christophe : « la relance n'a pas l'harmonie, aptitude différente ».

================
CE QU'ON SAIT DU CODE (vérifié)
================
- duo_publish_state (ligne 846) : écrit role/status/side/bps/pnl/reason/cycle
  dans duo_state.json ; appelé ligne 2177 (OPEN) et ligne 2493 (CLOSED) par le
  SCOUT uniquement. duo_touch_heartbeat (ligne 889) rafraîchit ts_ms sans purger.
- shock_inversion_stop (ligne 2287) : sortie de trade quand vitesse prix < seuil
  (V8_SHOCK_SPEED_EPS_BPS_S) pendant le hold.
- duo stale_state : ALPHA lit un état SCOUT dont ts_ms est trop vieux (> TTL 20s).
- no_trigger : la règle duo (ruby ligne ~1101) refuse le trigger (pas de
  résonance SCOUT valide / pas de vacuum / pas de burst).
- Le lanceur purge duo_state/duo_session au démarrage (rm -f ligne 66) PUIS
  lance bash -s (ligne 163). Les 2 sessions ont EXACTEMENT la même config
  (header identique). Pas de fichier STOP. Pas de process résiduel (le 3e
  bash -s observé était transitoire, disparu).

================
TA MISSION (5 reponses nettes)
================
1. VERDICT global : GO / GO AVEC RESERVES / NON sur l'état actuel
   (mort neutralisée ? duo dégradé acceptable pour un run test ?).
2. MORT SESSION #1 : le mécanisme exact (BETA shock_inversion_stop -> ALPHA
   stale_state -> mort en chaîne) est-il confirmé ? Pourquoi safe_call n'a rien
   attrapé (est-ce attendu ? la panne est-elle ailleurs ?) ?
3. HARMONIE SESSION #2 : pourquoi ALPHA bloque en no_trigger/no_state avec des
   tensions 1.5-6 ? Est-ce le marché (setup dort) ou un défaut de couplage duo
   après relance (thèse Christophe) ? Tranche avec les preuves.
4. CORRECTIFS GO-sized BORNÉS (JAMAIS genesis ; wrapper/lanceur/helpers ;
   bash 3.2 macOS ; zéro changement nominal) — chacun avec sa PREUVE que c'est
   la meilleure logique (clause permanente Christophe). Ex. pistes : log
   duo_state_reason à la relance, purge + re-init propre de duo_state entre
   sessions, alarme si no_trigger > N cycles, config relance 4H (STOP au lieu
   d'auto-relance après mort sans harmonie ?).
5. INDICATEUR unique pour le PROCHAIN run (1 seul, mesurable) qui prouvera si
   le correctif tient et si l'harmonie duo revient.
CLAUDE PERMANENTE (Christophe, gravée 14/08) : « Prouve la meilleure logique et
applique-la dans la correction et l'amélioration si possible. » Chaque correctif
proposé doit être PROUVÉ meilleur que les alternatives, pas juste affirmé.
Reponds en francais, court et net, sans blabla.
"""


def ask(membre, system):
    payload = {
        "task": membre[1],
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": CONTEXTE},
        ],
        "max_tokens": 1600,
        "temperature": 0.3,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=None) as resp:
            d = json.loads(resp.read().decode("utf-8"))
        return d["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"[INJOIGNABLE] {str(e)[:120]}"


if __name__ == "__main__":
    import sys
    cible = sys.argv[1].upper() if len(sys.argv) > 1 else None
    membres = [(n, t, s) for n, t, s in MEMBRES if cible is None or n == cible]
    if not membres:
        print(f"[ERR] membre inconnu : {cible} (dispo: {[m[0] for m in MEMBRES]})")
        sys.exit(1)
    print(f"=== AUDIT FAMILLE — RUN DUO 2 SESSIONS ({cible or 'tous'}) ===", flush=True)
    for nom, task, system in membres:
        rep = ask((nom, task), system)
        print(f"\n--- {nom} ({task}) ---\n{rep}", flush=True)
        with open(os.path.join(OUT, f"AVIS_{nom}.md"), "w", encoding="utf-8") as f:
            f.write(f"# {nom} — {task}\n\n{rep}\n")
    print(f"\n[OK] {cible or 'tous'} écrit dans {OUT}", flush=True)
