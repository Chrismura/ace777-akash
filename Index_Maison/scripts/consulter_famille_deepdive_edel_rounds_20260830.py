#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consultation FAMILLE — DEEPDIVE EDEL, 3 ROUNDS poussés (30/08/2026).

Christophe : « refaire recherche poussée 2 ou trois round, edel a du
potentiel. as tu utilise les bons prompts ? » → Non la 1ère fois (la famille
avait conclu « zéro source » SANS chercher). Correction : OBLIGATION de sources
(URLs), angle potentiel, clause permanente EN TOUTES LETTRES dans chaque prompt,
et 3 rounds jusqu'à épuisement (convention pattern institutions + push).

Round 1 : recherche libre, sources obligatoires, potentiel + risques.
Round 2 : on leur donne les sources que NOUS avons trouvées → vérifier,
corriger, approfondir, trouver ce qu'on a raté.
Round 3 : confrontation — avis des autres membres → trancher + amélioration.

Sortie : CONSULTATION_FAMILLE_DEEPDIVE_EDEL_ROUNDS_20260830/R{1,2,3}/.
"""
import json
import os
import time
import urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_DEEPDIVE_EDEL_ROUNDS_20260830")
os.makedirs(OUT, exist_ok=True)

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

SOURCES_TROUVEES = """SOURCES QUE NOUS AVONS DÉJÀ TROUVÉES (à vérifier, corriger, compléter) :
1) Edel = Edel Finance, « programmable market layer for tokenized equities »,
   prêt de titres tokenisés, marché cible $2.5T. Site : edel.finance.
   Sources : phemex.com/academy/what-is-edel-tokenized-stock-lending,
   coinmarketcap.com/currencies/edel/, rootdata.com/projects/detail/Edel Finance.
2) Équipe : James Sherbone (ex-IB Berenberg, Saxon) + Andres Soltermann
   (ex-DeFi Franc). Source : alearesearch.substack.com/p/edel-finance.
3) EXPLOIT 01/07/2026 : oracle manipulé, Google tokenisé gonflé ~7700%, ~$403K
   volés, routés via Tornado Cash, protocole de prêt MIS EN PAUSE.
   Sources : coindesk.com (01/07/2026), cryptotimes.io, cryptoslate.com.
4) LANCEMENT SNIPÉ (27/11/2025) : 30%+ du token snipé par des wallets liés au
   projet. Source : finance.yahoo.com/news/edel-finance-hot-seat-suspicious.
5) Depuis : Edel Markets (perp futures sur titres tokenisés) annoncé 09/07/2026,
   testnet, potentiel bénéficiaire adoption Coinbase. Sources : CMC, crypto.news.
6) Prix ~0.0107-0.0117, volume 24h ~$0.5-1M (MEXC, CoinGecko, CMC)."""


def brief_r1():
    return """DEEPDIVE EDEL — ROUND 1 : LE PROJET, AVEC PREUVES (30/08/2026)

EDEL (Edel Finance) est coté sur MEXC, micro-cap, prix ~0.0107, volume 24h
~$0.5-1M. Nous avons une position seed de 10$. Nous cherchons LA vérité sur ce
projet pour décider entrer / tenir / sortir.

OBLIGATION DE SOURCES : chaque affirmation sur le projet, l'équipe, la
tokenomics DOIT être accompagnée d'une URL vérifiable (site officiel, docs,
explorer, article de presse, dashboard). Si tu n'as pas de source pour un
point, écris explicitement « PAS DE SOURCE — hypothèse ».

1. LE PROJET : qui est derrière EDEL ? Équipe (noms, parcours), société,
   juridiction ? Que fait le projet exactement ? Cas d'usage réel, clients
   cibles, concurrence ? Le secteur de la tokenisation de titres est-il en
   croissance, qui sont les gros acteurs ?
2. TOKENOMICS : supply totale/circulante, répartition, vesting/unlocks (dates
   précises !), concentration des wallets.
3. LE POTENTIEL (important) : qu'est-ce qui peut faire monter le prix
   structurellement ? Catalyseurs à venir (launch, partenariats, listings,
   croissance du secteur) ? Quel serait le scénario haussier chiffré ?
4. LES RISQUES : delisting, exploit, dilution, wash trading — avec les faits.
5. VERDICT : GO / GO AVEC RÉSERVES / NON, note /10, et les 3 raisons qui
   décident.

""" + CLAUSE + "\n\n" + PUSH


def brief_r2():
    return """DEEPDIVE EDEL — ROUND 2 : VÉRIFIE NOS SOURCES, APPROFONDIS (30/08/2026)

Première passe faite. Voici les sources que NOUS avons trouvées. Ta mission :
1) VÉRIFIE chacune (les URLs sont-elles réelles ? les interprétations justes ?).
2) CORRIGE ce qui est faux ou nuancé.
3) TROUVE CE QU'ON A RATÉ : qui sont les investisseurs/backers ? y a-t-il une
   levée de fonds ? partenariats réels ? roadmap avec dates ? communauté
   (Twitter/X, Discord, Telegram) et sa taille ? quelle est la réputation du
   projet après l'exploit — s'en est-il remis ?
4) DÉVELOPPE LE POTENTIEL : le secteur tokenisé (titres tokenisés, prêt de
   titres) explose-t-il ? Edel est-il bien placé ? Quels catalyseurs précis
   dans les 3-12 prochains mois ? Scénario haussier chiffré avec probabilités.
5) RE-VERDICT : GO / GO AVEC RÉSERVES / NON, note /10, 3 raisons qui décident.

OBLIGATION DE SOURCES : URLs vérifiables pour chaque affirmation, ou
« PAS DE SOURCE — hypothèse ».

""" + SOURCES_TROUVEES + "\n\n" + CLAUSE + "\n\n" + PUSH


def brief_r3(avis):
    extrait = "\n\n".join(
        f"### AVIS {nom} (round 2)\n{texte[:1500]}" for nom, texte in avis)
    return f"""DEEPDIVE EDEL — ROUND 3 : CONFRONTATION FINALE (30/08/2026)

Voici les avis des autres membres de la famille sur EDEL (round 2). Lis-les,
puis :
1) TRANCHÉ : es-tu d'accord ou non avec chacun ? Où se trompent-ils ?
2) SYNTHÈSE : la vérité finale sur EDEL — projet, potentiel, risques.
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
    avis_round2 = []
    for round_no, brief_fn in ((1, brief_r1), (2, brief_r2)):
        rdir = os.path.join(OUT, f"R{round_no}")
        os.makedirs(rdir, exist_ok=True)
        print(f"\n=== ROUND {round_no} ===", flush=True)
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
                f.write(f"# AVIS {nom} — EDEL round {round_no} (30/08/2026)\n\n"
                        f"_provider: {provider}_\n\n{avis}\n")
            if round_no == 2:
                avis_round2.append((nom, avis))
            print(f"  [{nom}] OK ({provider})", flush=True)

    rdir3 = os.path.join(OUT, "R3")
    os.makedirs(rdir3, exist_ok=True)
    print("\n=== ROUND 3 (confrontation) ===", flush=True)
    brief3 = brief_r3(avis_round2)
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
            f.write(f"# AVIS {nom} — EDEL round 3 (30/08/2026)\n\n"
                    f"_provider: {provider}_\n\n{avis}\n")
        print(f"  [{nom}] OK ({provider})", flush=True)

    print("\nCONSULTATION 3 ROUNDS TERMINÉE")


if __name__ == "__main__":
    main()
