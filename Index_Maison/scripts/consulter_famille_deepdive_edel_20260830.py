#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consultation FAMILLE — DEEPDIVE EDEL (30/08/2026).

Christophe, 30/08 : « go deepdive de edel, mais tu le fais faire à la famille,
je veux pas te plomber. » → On délègue le deepdive à la famille (2 membres +
JUGE), sans révéler nos conclusions (avis indépendant), clause permanente +
PUSH EXCELLENCE. On ne leur donne pas notre set-up — ils doivent trouver le
potentiel et les risques du PROJET EDEL eux-mêmes.

Sortie : CONSULTATION_FAMILLE_DEEPDIVE_EDEL_20260830/ (avis .md + .json).
"""
import json
import os
import time
import urllib.request

ROOT = os.path.dirname(os.path.abspath(__file__))
HUB = "http://127.0.0.1:11435/v1/chat/completions"
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_DEEPDIVE_EDEL_20260830")
os.makedirs(OUT, exist_ok=True)

MEMBRES = [
    ("DEEPSEEK", "deepseek.analyse",
     "Tu es DEEPSEEK, critique factuel de la famille ACE777. Tu exiges des "
     "preuves, des sources primaires, tu refuses les conclusions non étayées, "
     "tu donnes des contre-exemples. Tu vérifies tout ce qui peut l'être."),
    ("ULTRA", "inferx.analyse",
     "Tu es ULTRA, membre de la famille ACE777. Tu regardes la robustesse à "
     "l'échelle : ce qui casse en prod, ce qui tient sur le long terme, la "
     "viabilité réelle du projet au-delà du narratif."),
    ("JUGE", "juge.tranche",
     "Tu es le JUGE de la famille ACE777. Tu tranches : GO / GO AVEC RÉSERVES / "
     "NON, avec une note sur 10 et les 3 raisons qui décident."),
]

CLAUSE = (
    "CLAUSE PERMANENTE (Christophe, 14/08 + 16/08) : Prouve la meilleure logique "
    "et applique-la dans la correction et l'amélioration si possible. Ne te "
    "contente PAS de corriger ou de valider : si tu proposes AUTRE CHOSE ou une "
    "AMÉLIORATION qui a du sens, dis-le explicitement. Corriger n'est pas "
    "suffisant : proposer est attendu. Donne ton avis strict."
)

PUSH = (
    "PUSH EXCELLENCE : Ta première réponse est le PLAFOND, pas le plancher. "
    "Va 30% plus loin. Une réponse confortable est ratée. Cherche les sources "
    "brutes, pas les synthèses. Si tu ne sais pas, dis-le — mais creuse d'abord."
)

BRIEF = """DEEPDIVE PROJET EDEL (EDELUSDT) — consultation famille (30/08/2026)

================
LE PROJET
================
EDEL est un token coté sur MEXC (paire EDELUSDT), micro-cap. Nous avons une
position paper de 10$ (seed) depuis le 24/08, jamais gérée (le moteur n'a fait
aucun trade dessus). Le prix est passé de 0.00874 à ~0.0118 (+35%) depuis le
seed, avec un aller-retour violent (creux 0.0101 → pic 0.0124 sur les 3
derniers jours).

================
CE QUE NOS DONNÉES MONTRENT (comportement, pas analyse projet)
================
- Range ~22% sur 3 jours, volatilité extrême (mouvement 6min médian 70% pendant
  les rafales vs 4% le reste du temps : il ne bouge QUE par rafales rares).
- 3 rafales en 3 jours (fin de journée UTC), après chacune le prix est en hausse
  +30min. Signal divergence maison : POMPE_PIEGE (le plus élevé du portefeuille).
- Aucune corrélation significative avec BTC, ETH ni aucune autre paire de notre
  portefeuille (~20 actifs). Il évolue en vase clos.

================
TES MISSIONS (avis INDÉPENDANT — on ne te donne PAS notre conclusion)
================
1. **LE PROJET** : qui est réellement derrière EDEL ? Société, équipe, pays ?
   Que fait le projet (cas d'usage réel) ? Cherche les sources primaires
   (site officiel, docs, annonces, listing MEXC, explorers). Le token a-t-il
   une vraie raison d'exister ou c'est du vent ?
2. **TOKENOMICS** : supply totale, % en circulation, vesting/unlocks prévus,
   risques de dilution. Un calendrier de libération de tokens à venir ?
3. **GÉOGRAPHIE DU TRADING** : qui anime le carnet ? Sessions asiatiques /
   européennes / US ? Volume réel vs artificiel (wash trading) ?
4. **RISQUES** : qu'est-ce qui peut casser le prix (delisting, unlock, scandale,
   rug, dilution) ? Notamment le risque delisting (notre leçon QAIT : un token
   retiré de MEXC du jour au lendemain).
5. **VERDICT** : ce token mérite-t-il une place dans un portefeuille, et à
   quelles conditions ? GO / GO AVEC RÉSERVES / NON, note /10, et les 3 raisons
   qui décident.

Règle d'or : distingue TOUJOURS ce que tu SAIS (source vérifiée) de ce que tu
INFÈRES (hypothèse). Si tu ne trouves pas de sources fiables, dis-le
franchement — c'est déjà une information. Ne me dis pas « c'est bien,
continuez ». Donne un avis tranché, chiffré, avec des signaux de vérification
précis.
""" + CLAUSE + "\n\n" + PUSH


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
        })
        req = urllib.request.Request(
            HUB, data=data.encode("utf-8"),
            headers={"Content-Type": "application/json"}, method="POST")
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            d = json.loads(resp.read().decode("utf-8"))
        return d["choices"][0]["message"]["content"].strip(), d.get("provider", "?")
    except Exception as e:
        return f"ERREUR: {e}", "?"


def main():
    for nom, model, system in MEMBRES:
        for attempt in (1, 2):
            print(f"[{nom}] appel {attempt}...", flush=True)
            avis, provider = appel_membre((nom, model, system), BRIEF)
            if avis.startswith("ERREUR") and attempt == 1:
                print(f"  -> retry ({avis})", flush=True)
                time.sleep(10)
                continue
            break
        with open(os.path.join(OUT, f"AVIS_{nom}.md"), "w", encoding="utf-8") as f:
            f.write(f"# AVIS {nom} — DEEPDIVE EDEL (30/08/2026)\n\n"
                    f"_provider: {provider}_\n\n{avis}\n")
        with open(os.path.join(OUT, f"AVIS_{nom}.json"), "w", encoding="utf-8") as f:
            json.dump({"membre": nom, "provider": provider, "avis": avis},
                      f, ensure_ascii=False, indent=1)
        print(f"[{nom}] OK → {OUT}/AVIS_{nom}.md", flush=True)
    print("CONSULTATION TERMINÉE")


if __name__ == "__main__":
    main()
