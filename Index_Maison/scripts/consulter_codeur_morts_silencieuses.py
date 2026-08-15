#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CODEUR — constatation morts silencieuses 14/08 (preuves a l'appui).

Demande au codeur : (1) produire l'instrumentation d'observation minimale
pour CAPTURER la cause (trap EXIT + derniere commande), (2) analyser la
cause racine, (3) prouver la meilleure logique (clause permanente).
"""
import json, os, urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = "/Users/christophe/ace777-test-day1/Index_Maison/CODE_observation_morts_silencieuses.md"

PROMPT = """\
Tu es le CODEUR de la famille ACE777 (task code.ia). Ecris le code demande,
borne a la tache, rien d'autre. Aucune reecriture, aucune feature hors cadre.

CLAUDE PERMANENTE (Christophe, 14/08 — a respecter a CHAQUE intervention) :
« Prouve la meilleure logique et applique-la dans la correction et
l'amelioration si possible. »
-> Tu dois (1) PROUVER que ta correction/instrumentation est la meilleure
logique (pas une rustine), et (2) proposer UNE amelioration si elle est
PROUVEE (mesurable, bornee, sans effet de bord).

================ PREUVES (verifiees superviseur, dossier AUDIT_MORT_SILENCIEUSE_2026-08-14) ================

LE RUN 4H DU 14/08 a fait 3 sessions ; les 2 premieres sont mortes EN ENTIER :

Session #1 (08:31:37Z) : BETA mort 08:49:29Z rc=1 | ALPHA mort 08:52:26Z rc=1
Session #2 (08:52:33Z) : ALPHA mort 09:25:05Z rc=1 | BETA mort 09:29:20Z rc=1
Session #3 : fin propre rc=0 a 09:31Z (duree atteinte)

LES 4 MORTS — MEME SIGNATURE (extraits des crash dumps) :
1) BETA #1 : dernier cycle logge 08:49:26 #92 SKIP -> mort 08:49:29 (3 s)
2) ALPHA #1 : dernier cycle logge 08:52:18 #108 SKIP | duo stale_state -> mort 08:52:26 (8 s)
3) ALPHA #2 : dernier cycle logge 09:24:57 #203 SKIP -> mort 09:25:05 (8 s)
4) BETA #2 : dernier cycle logge 09:29:13 #214 SKIP Mode Ecoute -> mort 09:29:20 (7 s)
=> Chaque mort survient PENDANT le cycle suivant (jamais logge), 3-8 s apres le
dernier cycle logge. PROCESS_EXIT.log : how=pipe_run_unit why=rc_1 rc=1.

PREUVES D'ABSENCE :
- ZERO FATAL_RC1 : le trap ERR (ligne 90 du champion, active dans la partie
  executee tail -n +85) n'a JAMAIS tire -> AUCUNE commande n'a echoue sous set -e.
- ZERO WARN safe_call du run (les 3 warnings = tests superviseur). stderr_debug = 0 octet.
- Les seuls exit 1 du code execute (lignes 367 BASE_URL, 1492 leverage) sont au
  DEMARRAGE, pas dans la boucle.
- Master : tail -n +85 genesis | bash -s (pipefail actif) -> le bash -s sort rc=1 sans message.

CONTEXTE TECHNIQUE :
- Le champion execute (genesis_manifest.txt) : ~2500 lignes, boucle principale
  while avec cycles SKIP/BUY/SELL, sleep ~8-10 s par cycle, duo_publish_state
  (SCOUT) / duo state lecture (HUNTER), trap ERR ligne 90 -> FATAL_RC1.
- Le master (launch_test_master_base_v8_5_impact.sh) lance : tail -n +85
  ./genesis_manifest.txt | bash -s, avec pipefail.
- Fonctions cles : safe_call (wrappeur), duo_publish_state, duo_touch_heartbeat.

================ TA MISSION ================

A) INSTRUMENTATION D'OBSERVATION (livrable principal) : code bash/zone a
   injecter, MINIMAL et borne (aucune logique metier changee), pour CAPTURER
   la cause d'une sortie rc=1 silencieuse pendant un cycle. Propose :
   1. trap EXIT qui loggue : rc de sortie + derniere ligne executee (via
      DEBUG/PS4) + timestamp + nom du bot. Compatible bash 3.2 macOS.
   2. modele de log lisible dans runs/ (ex. EXIT_DUMP_<bot>_<ts>.log).
   3. AUCUNE modification de la logique du champion (interdit).
B) ANALYSE CAUSE RACINE : avec les preuves ci-dessus, quelles sont les causes
   possibles d'un rc=1 sans FATAL_RC1 ni exit 1 du code ? (ex. EOF du pipe
   bash -s, read sur stdin vide, signal, fin de boucle implicite, retour de
   sous-shell, etc.) Classe par probabilite.
C) CLAUSE PERMANENTE : prouve la meilleure logique pour l'instrumentation
   (pourquoi trap EXIT + PS4 plutot que set -x plein) + UNE amelioration
   prouvee si possible.

Perimetre impose : genesis INTACT en logique. Aucun patch metier. Uniquement
observation.

RENDS : code + preuve, en francais, concis.
"""

def main():
    payload = {
        "task": "code.ia",
        "messages": [{"role": "user", "content": PROMPT}],
        "max_tokens": 2200,
        "temperature": 0.2,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=None) as resp:
        d = json.loads(resp.read().decode())
    content = d["choices"][0]["message"]["content"]
    provider = d.get("provider", "?")
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(f"# CODEUR — observation morts silencieuses (14/08)\n\nProvider: {provider}\n\n{content}\n")
    print(f"CODEUR ({provider}) -> {len(content)} chars -> {OUT}")

if __name__ == "__main__":
    main()
