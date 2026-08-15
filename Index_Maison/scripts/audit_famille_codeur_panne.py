#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Audit famille 6 + CODEUR — LOCALISATION DE LA PANNE ALPHA rc=1 (14/08).

Le run test (GEMINI_TEST + crash dump, 14/08 07:41Z) a REPRODUIT la mort :
ALPHA rc=1 à 07:49:10Z (~8 min après départ, juste après le fill #42).
BETA survit. Le crash dump a capturé la fenêtre de mort, mais FATAL_RC1 est
VIDE (le trap ERR n'a pas déclenché). Objectif : trouver la commande fautive
exacte + proposer un correctif borné, validé famille, avant retest.

Chaque membre : (1) verdict (GO / GO AVEC RÉSERVES / NON), (2) la commande
la plus probablement fautive (ou zone), (3) pourquoi le trap n'a pas écrit,
(4) UN correctif GO-sized borné (wrapper/lanceur, JAMAIS genesis),
(5) ce qu'il faut mesurer au prochain retest.
"""
import json
import os
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = "/Users/christophe/ace777-test-day1/Index_Maison/AUDIT_PANNE_2026-08-14"
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
LOCALISATION DE LA PANNE — ALPHA meurt en rc=1 (mort silencieuse, récurrente).

CONTEXTE HUMAIN (Christophe) : « Pas de sens de faire tourner BETA tout seul,
c'est un duo — arrête-moi ça. Trouve avec la famille et le codeur où est la
panne, et on reteste. » Le run test a été ARRÊTÉ proprement après la mort
d'ALPHA (BETA ne tourne plus). Mute Cortana/ADA activé.

================
LES FAITS (preuves réelles, pas un récit)
================
1. RUN TEST du 14/08 (GEMINI_TEST + crash dump, lancé 07:41Z, testnet) :
   - ALPHA (x13) : 3 fills gagnants (#36 +2.675, #42 +0.272, …) puis
     PROCESS_EXIT rc=1 à 07:49:10Z (~8 min après le départ).
   - BETA (x3) : survit, continue de tourner (arrêté ensuite par Christophe).
   - Pattern IDENTIQUE au 13/08 (rc=1 ~13 min après départ, après un fill).
2. CRASH DUMP capturé (runs/CRASH_DUMP_ALPHA_X13_BURST13_20260814_074910.log) :
   fenêtre de mort = 20 dernières lignes + dernier fill CSV :
   - 07:49:01 x13 #43 SKIP tension=0.00000000 momentum_too_small conf=0.2983
   - …9 secondes de SILENCE…
   - 07:49:10Z PROCESS_EXIT unit=ALPHA_X13_BURST13 how=pipe_run_unit why=rc_1 rc=1
3. FATAL_RC1 = VIDE (/tmp/ace777_fatal_rc1.log vide, aucun "FATAL_RC1" dans le
   log live). Le trap ERR posé dans genesis (ligne 90) n'a PAS écrit.
   → L'échec survient dans un SOUS-SHELL / substitution $(...) / pipeline dont
   l'échec n'est pas propagé au shell qui porte le trap (prédiction GROK
   confirmée : « pipefail seul ne suffit pas »).
4. CONTEXTE : le bot tourne sous set -euo pipefail (genesis ligne 86). Le
   lanceur fait : tail -n +85 ./genesis_manifest.txt | bash -s 2>&1 | while …
   → rc=${PIPESTATUS[1]} = rc de bash -s. Les 2 seuls exit 1 du code = checks
   de démarrage (exclus : ALPHA a tourné 8 min avant de mourir).
5. FENÊTRE SUSPECTE (ce qui se passe dans le silence de 9 s, juste après un
   SKIP radar_block / momentum_too_small, avant le cycle suivant) — candidats
   extraits du code (genesis_manifest.txt, ligne) :
   - 1599-1601 : p1_resp / depth_1 = public_get (curl_with_retry 3 tentatives
     × 5s pause = jusqu'à 15s sans sortie)
   - 1613-1615 : p2_resp / depth_2 idem
   - 1733-1745 : book_resp / klines (public_get)
   - 1385-1388 : radar_allow/direction/reason/conf = json_get "$radar_out"
   - 454 : json_get() — helper ruby ; 677-684 : num_*() — ruby -e ; un helper
     peut échouer sous set -e (sortie non-nulle) sans message si stderr avalé.
   - 1992 : llm_raw="$(curl … 2>/dev/null)" || llm_curl_ok=$? (LLM gate)
   - Substitutions SANS || true dans la boucle = mort silencieuse possible.

================
TA MISSION (5 réponses nettes)
================
1. Verdict global : GO / GO AVEC RÉSERVES / NON + raison courte.
2. LA COMMANDE (ou zone) la plus probablement fautive — justifie par le
   timing (9 s ≈ 1-2 tentatives curl_with_retry) et le code.
3. POURQUOI le trap ERR n'a pas écrit FATAL_RC1 (mécanisme bash exact).
4. UN CORRECTIF GO-sized BORNÉ (wrapper/lanceur/un helper, JAMAIS genesis ;
   bash 3.2 macOS ; zéro changement du comportement nominal).
5. CE QU'IL FAUT MESURER au prochain retest pour CONFIRMER la panne
   (1 indicateur de plus, pas plus).
Réponds en français, court et net, sans blabla.
"""


def ask(membre, system):
    payload = {
        "task": membre[1],
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": CONTEXTE},
        ],
        "max_tokens": 1300,
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
    print(f"=== AUDIT FAMILLE — PANNE ALPHA rc=1 ({cible or 'tous'}) ===", flush=True)
    for nom, task, system in membres:
        rep = ask((nom, task), system)
        print(f"\n--- {nom} ({task}) ---\n{rep}", flush=True)
        with open(os.path.join(OUT, f"AVIS_{nom}.md"), "w", encoding="utf-8") as f:
            f.write(f"# {nom} — {task}\n\n{rep}\n")
    print(f"\n[OK] {cible or 'tous'} écrit dans {OUT}", flush=True)
