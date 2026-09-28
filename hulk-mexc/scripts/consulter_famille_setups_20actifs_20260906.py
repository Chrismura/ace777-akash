#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""consulter_famille_setups_20actifs_20260906.py — Consultation FAMILLE + CORTANA.

Sujet : système de set-ups 20 actifs (grille 20×20, lead-lag, décorrélation,
poussière individuelle, fiches SETUP+PROJET v3). 2 membres famille + Cortana.
ADVISORY : ils proposent, rien n'est appliqué sans validation Christophe.

Usage : python3 scripts/consulter_famille_setups_20actifs_20260906.py [deepseek|gemini|cortana|all]
"""
import json
import os
import sys
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_SETUPS_20ACTIFS_20260906")
os.makedirs(OUT, exist_ok=True)

SYSTEM = (
    "Tu es un membre de la famille ACE777 (consultation ADVISORY — tu PROPOSES, tu "
    "n'appliques JAMAIS rien). Tu connais le moteur HULK (paper dip&rip MEXC small caps), "
    "la doctrine « même système, pas même set-up » et le protocole de croisement externe. "
    "Avis franc, chiffré, GO-sized."
)

CLAUSE = (
    "CLAUSE PERMANENTE (Christophe, 16/08 — applicable à TOUS les prompts) : "
    "Ne te contente PAS de corriger ou de valider. Si tu proposes AUTRE CHOSE (approche "
    "différente, autre architecture, autre unité) ou une AMÉLIORATION qui a du sens, "
    "dis-le explicitement. Corriger n'est pas suffisant : proposer est attendu."
)

CONTEXTE = """\
CONSULTATION FAMILLE + CORTANA — Système de set-ups 20 actifs (06/09/2026, Buffy)

=== CE QUI A ÉTÉ FAIT (audit + extensions du jour) ===
1. AUDIT complet du système de set-ups (20 actifs CORE : BTC ETH XRP HBAR RIZE ZBCN W RED CC
   PYTH BIO KITE TEL CHIP RWAINC EDEL QNT FLUID RWA MNSRY) :
   - Profils rechargés sur 9 jours (27/08→05/09, ~22k points/paire, archive .gz + live, filtre bad ticks).
   - Suivi quotidien réparé : 4 paires (BTC RIZE CHIP FLUID) étaient mortes car le script
     dérivait sa liste du state paper → liste CORE-20 explicite désormais.
   - Défauts corrigés : poussière = indicateur PANIER (pas individuel) étiquetée comme telle ;
     mur max = max du run (gelé) → mur moy/max séparés ; date fiches dynamique + versionnées.
2. NOUVEAU — GRILLE 20×20 (analyse_grille_correlation.py, 9 jours, rendements horaires) :
   - Lead-lag vs panier : AUCUN leader net sur 9 jours — tout le groupe bouge en lag 0
     (synchronisé). RWAINC lag -3h mais corr 0.125 (bruit). BIO lag -3h corr +0.31 (piste faible).
   - Décorrélation (moyenne |corr| aux 19 autres) : RIZE 0.061, RWAINC 0.073, RED 0.093,
     EDEL 0.127, RWA 0.134, CHIP 0.142 = bloc ENDOGÈNE. BTC/ETH 0.411 = les baromètres.
   - Relations binômes : une seule dépasse le seuil (BIO précède le panier de 3h, corr 0.31).
   - Signal directionnel 9j (m6→delta panier +4h) : RWAINC seul ≥ +0.15 (leader haussier).
     Les majors (BTC -0.32, ETH -0.26, XRP -0.29) ressortent POMPE-PIÈGE (corrélés au panier
     qui monte avant de retomber). EDEL -0.43 le pire.
3. NOUVEAU — POUSSIÈRE INDIVIDUELLE (poussiere_paire.py, carnet MEXC ±2%, 2 snapshots à 75s) :
   - Carnets sains : BTC 0.5%, ETH 0.2%, XRP 0.3%, HBAR 0.2%, CC 1.7%, PYTH 1.5%, RED 4.2%.
   - Carnets fragiles : MNSRY 100%, FLUID 60.6%, RWA 62%, ZBCN 58.9%, QNT 46.2%, RWAINC 43.1%.
   - Évanescence (fantômes) : CHIP 50.7%, KITE 46.8%, RIZE 44.8%, TEL 32.6%, EDEL 29.1%,
     PYTH 23.9% des petits bids disparaissent en 75s.
4. FICHES v3 : DEUX fiches par actif (40 au total) :
   - FICHE_SETUP (technique) : statut famille + garde-fou NON famille + rôle dans le groupe
     (lead-lag, décorrélation, copains) + profil 9j + set-up individuel + poussière individuelle.
   - FICHE_PROJET (étude projet) : catégorie, thèse enregistrée (CC la seule complète),
     verdict deepdive, TVL DefiLlama + mcap CoinGecko live, sources de vérité, check-up 2-4 sem.

=== LES QUESTIONS (réponds à CHACUNE, court et net) ===
Q1. La grille 9 jours dit : pas de leader, groupe synchronisé lag 0. Acceptes-tu ce verdict
    (donc : PAS de trigger « premier qui donne le mouvement » à câbler) ou faut-il tester
    autre chose (autre fenêtre, autre métrique que le rendement horaire, intraday 15min) ?
Q2. Le bloc endogène (RIZE RWAINC RED EDEL RWA CHIP) : pour chaque actif, ses signaux doivent
    être lus comme indépendants du panier. Vois-tu un risque ou une opportunité à câbler les
    entrées de ce bloc SANS filtre macro (contrairement au reste) ?
Q3. La poussière individuelle (±2%, seuil 200$, évanescence 75s) remplace l'indicateur panier.
    Les seuils te semblent-ils bons pour des small caps MEXC, et quelle règle d'entrée/skip
    proposes-tu à partir de (poussière bid %, évanescence %) ?
Q4. Les fiches doubles (SETUP technique + PROJET étude) : structure suffisante pour qu'une IA
    (Hulk, Cortana, analyste) prenne une décision éclairée par actif, ou manque-t-il une
    section (ex. historique des décisions, score de conviction, backend de cliché carnet) ?
Q5. UNE amélioration GO-sized pour le système entier (pas cosmétique).

FORMAT ATTENDU :
VERDICT GLOBAL : GO / GO-AVEC-RÉSERVES / NON
CONFIANCE : XX%
Q1..Q5 : réponse courte à chaque question.
SYNTHÈSE : 5 lignes max.
"""


def ask(task, outname, system_extra=""):
    payload = {
        "task": task,
        "messages": [
            {"role": "system", "content": SYSTEM + "\n\n" + CLAUSE + ("\n\n" + system_extra if system_extra else "")},
            {"role": "user", "content": CONTEXTE},
        ],
        "max_tokens": 2000,
        "temperature": 0.3,
    }
    req = urllib.request.Request(
        HUB, data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=420) as resp:
            d = json.loads(resp.read().decode("utf-8"))
        content = d["choices"][0]["message"]["content"].strip()
        provider = d.get("provider", "?")
        fn = os.path.join(OUT, outname)
        with open(fn, "w", encoding="utf-8") as fh:
            fh.write(f"# AVIS ({task} · provider {provider} · 2026-09-06)\n\n{content}\n")
        print(f"[OK] {outname} ({provider})")
    except Exception as e:
        print(f"[ERR] {task}: {e}")


def main():
    who = (sys.argv[1:] or ["all"])[0]
    if who in ("all", "deepseek"):
        ask("famille.analyse", "AVIS_DEEPSEEK.md",
            "Rôle : membre famille, relecture factuelle et rigoureuse, chiffrée.")
    if who in ("all", "gemini"):
        ask("gemini.analyse", "AVIS_GEMINI.md",
            "Rôle : membre famille, regard architecture et méthode de mesure.")
    if who in ("all", "cortana"):
        ask("cortana.analyse", "AVIS_CORTANA.md",
            "Tu es CORTANA, analyste-maîtresse (contrat ADVISORY : tu proposes, tu n'appliques rien). "
            "Tu connais l'aspiration, les murs de paille et le vortex.")
    print(f"== avis dans {OUT}")


if __name__ == "__main__":
    main()
