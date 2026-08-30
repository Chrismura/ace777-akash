#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consultation FAMILLE — DEEPDIVE ACTIF, 3 ROUNDS POUSSÉS (générique).

Protocole gravé 30/08 (Christophe) : TOUS les actifs du portefeuille sont
traités avec le MÊME système — set-up dans FICHE_IA, recherche (deepdive)
dans la fiche projet de l'actif, 3 rounds minimum, obligation de sources
(URLs ou « PAS DE SOURCE »), clause permanente EN TOUTES LETTRES dans
chaque prompt.

Usage : python3 consulter_famille_deepdive_actif_3rounds.py <PAIRE> ["Description du projet"]
Ex. :  python3 consulter_famille_deepdive_actif_3rounds.py CHIPUSDT

Round 1 : recherche libre, sources obligatoires, potentiel + risques.
Round 2 : on leur donne les sources trouvées par nous → vérifier, corriger,
approfondir, trouver ce qu'on a raté.
Round 3 : confrontation — avis des autres membres → trancher + amélioration.

Sortie : CONSULTATION_FAMILLE_DEEPDIVE_<PAIRE>_ROUNDS_<DATE>/R{1,2,3}/.
"""
import json
import os
import sys
import time
import urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"

MEMBRES = [
    ("DEEPSEEK", "deepseek.analyse",
     "Tu es DEEPSEEK, critique factuel de la famille ACE777. Tu exiges des "
     "preuves, des URLs vérifiables, tu refuses les conclusions non étayées. "
     "Si un autre membre avance un chiffre, tu le vérifies."),
    ("ULTRA", "inferx.analyse",
     "Tu es ULTRA, membre de la famille ACE777. Tu regardes la robustesse à "
     "l'échelle : viabilité réelle, croissance, ce qui tient sur le long terme. "
     "Tu cherches le POTENTIEL autant que les risques."),
    ("JUGE", "juge.tranche",
     "Tu es le JUGE de la famille ACE777. Tu tranches : GO / GO AVEC RÉSERVES / "
     "NON, note sur 10, et les 3 raisons qui décident. Tu entends tous les "
     "arguments avant de juger."),
]

CLAUSE = (
    "CLAUSE PERMANENTE (Christophe, 14/08 + 16/08) : Prouve la meilleure logique "
    "et applique-la dans la correction et l'amélioration si possible. Ne te "
    "contente PAS de corriger ou de valider : si tu proposes AUTRE CHOSE "
    "(approche différente, autre architecture, autre unité) ou une AMÉLIORATION "
    "qui a du sens, dis-le explicitement. Corriger n'est pas suffisant : "
    "proposer est attendu. Donne ton avis strict."
)

PUSH = (
    "PUSH EXCELLENCE : Ta première réponse est le PLAFOND, pas le plancher. "
    "Va 30% plus loin. Une réponse confortable est ratée. Cherche les sources "
    "brutes, pas les synthèses. Si tu ne sais pas, dis-le — mais creuse d'abord."
)


def date_stamp():
    return time.strftime("%Y%m%d", time.gmtime())


def brief_r1(pair, desc):
    return f"""DEEPDIVE {pair} — ROUND 1 : LE PROJET, AVEC PREUVES (30/08/2026)

{desc}

Nous avons une position (paper) sur cet actif et cherchons LA vérité sur le
projet pour décider entrer / tenir / sortir.

OBLIGATION DE SOURCES : chaque affirmation sur le projet, l'équipe, la
tokenomics DOIT être accompagnée d'une URL vérifiable (site officiel, docs,
explorer, article de presse, dashboard). Si tu n'as pas de source pour un
point, écris explicitement « PAS DE SOURCE — hypothèse ».

1. LE PROJET : qui est derrière ? Équipe (noms, parcours), société,
   juridiction ? Que fait le projet exactement ? Cas d'usage réel, clients
   cibles, concurrence ? Le secteur est-il en croissance, qui sont les gros
   acteurs ?
2. TOKENOMICS : supply totale/circulante, répartition, vesting/unlocks (dates
   précises !), concentration des wallets.
3. LE POTENTIEL (important) : qu'est-ce qui peut faire monter le prix
   structurellement ? Catalyseurs à venir (launch, partenariats, listings,
   croissance du secteur) ? Quel serait le scénario haussier chiffré ?
4. LES RISQUES : delisting, exploit, dilution, wash trading — avec les faits.
5. VERDICT : GO / GO AVEC RÉSERVES / NON, note /10, et les 3 raisons qui
   décident.

""" + CLAUSE + "\n\n" + PUSH


def brief_r2(pair, sources):
    return f"""DEEPDIVE {pair} — ROUND 2 : VÉRIFIE NOS SOURCES, APPROFONDIS (30/08/2026)

Première passe faite. Voici les sources que NOUS avons trouvées. Ta mission :
1) VÉRIFIE chacune (les URLs sont-elles réelles ? les interprétations justes ?).
2) CORRIGE ce qui est faux ou nuancé.
3) TROUVE CE QU'ON A RATÉ : qui sont les investisseurs/backers ? y a-t-il une
   levée de fonds ? partenariats réels ? roadmap avec dates ? communauté
   (Twitter/X, Discord, Telegram) et sa taille ? quelle est la réputation du
   projet ?
4) DÉVELOPPE LE POTENTIEL : le secteur explose-t-il ? Cet actif est-il bien
   placé ? Quels catalyseurs précis dans les 3-12 prochains mois ? Scénario
   haussier chiffré avec probabilités.
5) RE-VERDICT : GO / GO AVEC RÉSERVES / NON, note /10, 3 raisons qui décident.

OBLIGATION DE SOURCES : URLs vérifiables pour chaque affirmation, ou
« PAS DE SOURCE — hypothèse ».

""" + sources + "\n\n" + CLAUSE + "\n\n" + PUSH


def brief_r3(pair, avis):
    extrait = "\n\n".join(
        f"### AVIS {nom} (round 2)\n{texte[:1500]}" for nom, texte in avis)
    return f"""DEEPDIVE {pair} — ROUND 3 : CONFRONTATION FINALE (30/08/2026)

Voici les avis des autres membres de la famille sur {pair} (round 2). Lis-les,
puis :
1) TRANCHÉ : es-tu d'accord ou non avec chacun ? Où se trompent-ils ?
2) SYNTHÈSE : la vérité finale sur {pair} — projet, potentiel, risques.
3) AMÉLIORATION (clause permanente) : que propose-tu de DIFFÉRENT qui ferait
   mieux que ce qui a été dit ? Une approche, une métrique, un set-up ?
4) VERDICT FINAL : GO / GO AVEC RÉSERVES / NON, note /10, 3 raisons qui
   décident.

OBLIGATION DE SOURCES : URLs vérifiables, ou « PAS DE SOURCE — hypothèse ».

=== AVIS DES AUTRES MEMBRES ===
{extrait}

{CLAUSE}

{PUSH}"""


def appel_membre(membre, brief, timeout=300):
    nom, model, system = membre
    try:
        data = json.dumps({
            "model": model,
            "messages": [
                {"role": "system", "content": system + "\n\n" + CLAUSE + "\n\n" + PUSH},
                {"role": "user", "content": brief},
            ],
            "temperature": 0.7,
            "max_tokens": 4000,
        }).encode("utf-8")
        req = urllib.request.Request(
            HUB, data=data,
            headers={"Content-Type": "application/json"}, method="POST")
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            d = json.loads(resp.read().decode("utf-8"))
        return d["choices"][0]["message"]["content"].strip(), d.get("provider", "?")
    except Exception as e:
        return f"ERREUR: {e}", "?"


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 consulter_famille_deepdive_actif_3rounds.py <PAIRE> [description]")
        sys.exit(1)
    pair = sys.argv[1].upper()
    if not pair.endswith("USDT"):
        pair += "USDT"
    desc = sys.argv[2] if len(sys.argv) > 2 else f"{pair} est un actif de notre portefeuille (MEXC, micro-cap)."
    ds = date_stamp()
    OUT = os.path.join(ROOT, f"CONSULTATION_FAMILLE_DEEPDIVE_{pair}_ROUNDS_{ds}")
    os.makedirs(OUT, exist_ok=True)

    # Sources réelles : fichier texte optionnel sources_<PAIRE>.txt à côté du script.
    # Sinon fallback : on pointe les fiches projet existantes (DEEPDIVE_GLOBAL etc.).
    src_txt = os.path.join(ROOT, f"sources_{pair}.txt")
    if os.path.exists(src_txt):
        with open(src_txt, encoding="utf-8") as f:
            sources = "SOURCES QUE NOUS AVONS DÉJÀ TROUVÉES (à vérifier, corriger, compléter) :\n" + f.read()
    else:
        sources = (f"SOURCES QUE NOUS AVONS DÉJÀ TROUVÉES : nos fiches projet contiennent un premier deepdive "
                   f"(Index_Maison/OUTBOX_OBSIDIAN/Crypto_Projet/DEEPDIVE_GLOBAL_20260829.md + FICHE_SETUP_{pair}_20260830.md). "
                   f"Notre profil comportemental mesuré : runs/profils_actifs/PROFIL_{pair}.md. "
                   f"Vérifie ces faits, corrige, et trouve ce qu'on a raté.")

    avis_round2 = []
    start_round = 2 if "--r2" in sys.argv else 1
    rounds = [(1, lambda: brief_r1(pair, desc)), (2, lambda: brief_r2(pair, sources))]
    for round_no, brief_fn in rounds:
        if round_no < start_round:
            continue
        rdir = os.path.join(OUT, f"R{round_no}")
        os.makedirs(rdir, exist_ok=True)
        print(f"\n=== ROUND {round_no} — {pair} ===", flush=True)
        for nom, model, system in MEMBRES:
            for attempt in (1, 2):
                print(f"  [{nom}] appel {attempt}...", flush=True)
                avis, provider = appel_membre((nom, model, system), brief_fn())
                if avis.startswith("ERREUR") and attempt == 1:
                    print(f"    retry ({avis})", flush=True)
                    time.sleep(10)
                    continue
                break
            with open(os.path.join(rdir, f"AVIS_{nom}.md"), "w", encoding="utf-8") as f:
                f.write(f"# AVIS {nom} — {pair} round {round_no} (30/08/2026)\n\n"
                        f"_provider: {provider}_\n\n{avis}\n")
            if round_no == 2:
                avis_round2.append((nom, avis))
            print(f"  [{nom}] OK ({provider})", flush=True)

    rdir3 = os.path.join(OUT, "R3")
    os.makedirs(rdir3, exist_ok=True)
    print(f"\n=== ROUND 3 (confrontation) — {pair} ===", flush=True)
    brief3 = brief_r3(pair, avis_round2)
    for nom, model, system in MEMBRES:
        for attempt in (1, 2):
            print(f"  [{nom}] appel {attempt}...", flush=True)
            avis, provider = appel_membre((nom, model, system), brief3)
            if avis.startswith("ERREUR") and attempt == 1:
                print(f"    retry ({avis})", flush=True)
                time.sleep(10)
                continue
            break
        with open(os.path.join(rdir3, f"AVIS_{nom}.md"), "w", encoding="utf-8") as f:
            f.write(f"# AVIS {nom} — {pair} round 3 (30/08/2026)\n\n"
                    f"_provider: {provider}_\n\n{avis}\n")
        print(f"  [{nom}] OK ({provider})", flush=True)

    print(f"\nCONSULTATION 3 ROUNDS TERMINÉE — {OUT}")


if __name__ == "__main__":
    main()
