#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit famille 6 — VALIDATION DU LANCEMENT DU RUN TEST MOTEUR (14/08).

Contexte : chantier E-08 (cause racine ALPHA rc=1, mort silencieuse ~13 min
après le départ, juste après un fill). Le JUGE a déjà exigé un crash dump
(13/08, GO AVEC RÉSERVES) — il est appliqué au lanceur v8_5. Avant de lancer
le run test, la famille + le juge tranchent 3 points bornés :

Q1. PROTOCLE DE RUN TEST — quel lanceur ?
    - v8_5 (launch_test_master_base_v8_5_impact.sh) : crash dump ACTIF,
      défaut de fortress, mais sans les corrections GEMINI_TEST (SIGPIPE,
      rampe levier model).
    - GEMINI_TEST (launch_test_master_base_v8_5_impact_GEMINI_TEST.sh) :
      identique au run crashé du 13/08 (reproduction fidèle), mais SANS
      crash dump (FATAL_RC1 via le trap reste actif dans genesis).
    - Ajouter le crash dump à GEMINI_TEST aussi (petite modif lanceur,
      passe par ce circuit).
Q2. CHAMPION — genesis md5 = af307996 (98c80b5c + trap ERR diagnostic
    ajouté le 14/08 00:46, backup /tmp/genesis_manifest.txt.bak-errtrap-*).
    Le préflight bloque (attendu 98c80b5c). Options :
    - Re-sceller af307996 (le trap est un ajout diagnostic légitime, exigé
      par la famille ; le champion = 98c80b5c + trap, vérifié par diff).
    - Restaurer 98c80b5c (trap déplacé ailleurs — contredit « ne pas toucher
      aux corrections » de Christophe).
Q3. PLAN DE RETOUR — valider les points de rollback avant exécution :
    - genesis pré-trap : /tmp/genesis_manifest.txt.bak-errtrap-20260814-004638
      (= md5 98c80b5c… vérifié).
    - lanceur v8_5 pré-crash-dump : launch_test_master_base_v8_5_impact.SAUVE_V2.sh.
    - lanceur GEMINI_TEST intact (md5 b36b4998…).
    - compte : 0 position ouverte · testnet (aucun argent réel).

Chaque membre : (1) verdict global (GO / GO AVEC RÉSERVES / NON + raison
courte), (2) réponse nette à Q1 (le lanceur choisi), (3) réponse nette à Q2
(re-sceller ou restaurer), (4) Q3 : valide ou réserve, (5) UNE amélioration
GO-sized si réserves.
"""
import json
import os
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = "/Users/christophe/ace777-test-day1/Index_Maison/AUDIT_LANCEMENT_TEST_2026-08-14"
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
VALIDATION FAMILLE + JUGE — LANCEMENT DU RUN TEST MOTEUR (14/08, avant toute exécution).

CONTEXTE HUMAIN (Christophe) : « Alpha se tue, et voilà — je veux la cause racine,
pas un pansement. » « Ne touche pas aux corrections, peut-être qu'elles sont
légitimes. On passe par la famille et le juge, Buffy supervise. » Le moteur a été
récupéré après un sabotage Cursor (audit forensique, confession noir sur blanc —
l'audit est peut-être à revoir, on verra plus tard). Christophe ordonne :
« on finit la logique de ce matin, on fait valider tout ça, on lance, on teste le
moteur et le cockpit, et on voit ».

LES FAITS VÉRIFIÉS (14/08 matin, lecture seule) :
- Run MASTER_VORTEX_V2_COLLAB_4H (testnet, 13/08) : ALPHA meurt en PROCESS_EXIT
  rc=1 à 18:25:42Z, 13 min après le départ, juste après le fill cycle 81. BETA
  survit (rc=0 à 20:37). Récurrent (16:39, 17:11, 17:30, 17:42, 18:08, 18:25).
- Cause probable : set -euo pipefail + stderr avalé → mort rc=1 silencieuse.
- Trap ERR posé dans genesis (ligne 90) : au prochain rc=1, écrit
  FATAL_RC1 ligne=N cmd=[...] dans le log du run ET /tmp/ace777_fatal_rc1.log.
  Testé en réel (false → ligne exacte). Zéro changement de comportement.
- Crash dump appliqué au lanceur v8_5 (launch_test_master_base_v8_5_impact.sh,
  14/08 08:33) : au premier rc!=0, capture 20 dernières lignes + FATAL_RC1 +
  dernier fill CSV, dans runs/CRASH_DUMP_<unit>_<ts>.log. Backup SAUVE_V2.
- PRÉFLIGHT réel du lanceur (preflight_ace777.sh) : TOUT VERT sauf 1 point :
  genesis md5 = af307996… attendu 98c80b5c… (le trap a modifié genesis).
  Compte à plat = 0 position ouverte (C8 OK) · clés testnet OK · ping OK.
- Chaîne de lancement : GO_VORTEX_V2 (obsolète : attend encore 37fca367, il
  refuserait même 98c80b5c) → launch_vortex_v2_collab_4h_binance.sh →
  launch_test_master_base_v8_6_fortress.sh → LAUNCH_V85_SCRIPT (défaut v8_5).
  Le run crashé du 13/08 tournait avec GEMINI_TEST (via LAUNCH_V85_SCRIPT),
  qui n'a PAS le crash dump.
- Points de retour vérifiés : genesis pré-trap /tmp/genesis_manifest.txt.bak-
  errtrap-20260814-004638 (= 98c80b5c…) · lanceur v8_5 pré-crash-dump SAUVE_V2 ·
  GEMINI_TEST intact (b36b4998…) · 0 position · testnet (aucun argent réel).

LES 3 QUESTIONS (réponds net, 1 réponse chacune) :
Q1. PROTOCLE DU RUN TEST — quel lanceur ?
    a) v8_5 (crash dump actif, comportement proche du run crashé)
    b) GEMINI_TEST (identique au run crashé, reproduction fidèle, SANS crash
       dump — mais FATAL_RC1 reste actif via le trap dans genesis)
    c) Ajouter d'abord le crash dump à GEMINI_TEST, puis lancer avec GEMINI_TEST
Q2. CHAMPION — genesis = af307996 (98c80b5c + trap ERR diagnostic).
    a) RE-SCELLER af307996 (le trap est légitime, exigé par la famille ; le
       champion reste 98c80b5c sémantiquement, vérifié par diff)
    b) RESTAURER 98c80b5c (trap déplacé hors genesis — contredit « ne pas
       toucher aux corrections » de Christophe)
Q3. PLAN DE RETOUR — valides-tu les points de rollback ci-dessus comme
    condition préalable au lancement (oui / non + réserve éventuelle) ?

TA MISSION :
1. Verdict global : GO / GO AVEC RÉSERVES / NON + raison courte et nette.
2. Q1 : a, b ou c + une phrase de justification.
3. Q2 : a ou b + une phrase de justification.
4. Q3 : oui / non / réserve.
5. UNE amélioration concrète GO-sized (pas cosmétique) si tu as des réserves.
Réponds en français, format court et net, sans blabla.
"""


def ask(membre, system):
    payload = {
        "task": membre[1],
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": CONTEXTE},
        ],
        "max_tokens": 1000,
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
    print(f"=== AUDIT FAMILLE — LANCEMENT RUN TEST ({cible or 'tous'}) ===", flush=True)
    for nom, task, system in membres:
        rep = ask((nom, task), system)
        print(f"\n--- {nom} ({task}) ---\n{rep}", flush=True)
        with open(os.path.join(OUT, f"AVIS_{nom}.md"), "w", encoding="utf-8") as f:
            f.write(f"# {nom} — {task}\n\n{rep}\n")
    print(f"\n[OK] {cible or 'tous'} écrit dans {OUT}", flush=True)
