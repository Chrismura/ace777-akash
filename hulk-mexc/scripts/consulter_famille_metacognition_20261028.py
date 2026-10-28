#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Consultation FAMILLE + JUGE — métacognition (28/10/2026, GO Christophe).

Sujet : intégrer la métacognition dans les règles maison (+ Cortana).
Tour de table ADVISORY : on propose, Christophe dispose. Historique gardé
(AVIS_* + SYNTHESE + § registre). On pousse à fond : moelle substantielle.

Usage : python3 scripts/consulter_famille_metacognition_20261028.py [all|famille|juge|cortana] [aveugle]

Mode AVEUGLE (28/10, remarque Christophe : ne pas souffler nos solutions) : brief avec
le PROBLÈME + l'HISTORIQUE + l'état de l'art, SANS nos P1-P4. Ce sont EUX qui
proposent. Q4 devient Q1. Comparer ensuite avec le tour guidé = mesure du biais
d'amorçage maison.
"""
import json
import os
import sys
import urllib.request

HUB = "http://127.0.0.1:11435/v1/chat/completions"
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "CONSULTATION_FAMILLE_METACOGNITION_20261028")
os.makedirs(OUT, exist_ok=True)

SYSTEM = (
    "Tu es un membre de la famille ACE777 (consultation ADVISORY — tu PROPOSES, tu "
    "n'appliques JAMAIS rien). Tu connais le moteur HULK (paper dip&rip MEXC), "
    "la doctrine (brut, discipline, mesure-avant-câblage, shadow 0 ordre, réversible "
    "en 1 ligne) et l'historique ci-dessous. Avis franc, chiffré quand possible."
)

CLAUSE = (
    "CLAUSE PERMANENTE (Christophe, 16/08) : ne te contente PAS de corriger ou de "
    "valider. Si tu proposes AUTRE CHOSE (autre approche, autre architecture, autre "
    "unité) ou une AMÉLIORATION qui a du sens, dis-le explicitement. "
    "Corriger n'est pas suffisant : proposer est attendu."
)

CONTEXTE = """\
CONSULTATION FAMILLE + JUGE — métacognition dans les règles (28/10/2026, Buffy)

=== DEEP DIVE MARCHÉ (fait ce soir, 4 piliers convergents) ===
1. Nelson-Narens : étage qui FAIT vs étage qui REGARDE, séparés. Regard continu
   sans toucher ; contrôle rare et verrouillé. « Gouverneur assisté par l'IA,
   jamais souverain » — tout déléguer au même modèle casse au 1er régime inédit.
2. Reflexion (Shinn 2023) : Acteur/Évaluateur/Réflecteur SÉPARÉS (+11 pts HumanEval
   sans réentraînement). Le critique qui partage les biais du générateur ne voit rien.
3. Gençay 2026 : corrections STRUCTURELLES pas procédurales. Tout essai compte :
   un agent qui teste 100 variantes et montre la meilleure MENT par sélection.
   Déflater par le nombre d'essais (Deflated Sharpe). Hypothèse pré-enregistrée >
   trouvaille après fouille.
4. Self-critique evaluator loop : le juge = PORTAIL d'abord, jamais récompense ;
   anti-collusion (critères découplés, contre-exemples, ancre humaine) ; suivre le
   taux de désaccord juge/humain comme métrique de santé.

=== HISTORIQUE MAISON (gardé, substance) ===
- Garde-fou fidélité : le replay trailing a été refusé 4 fois avant validation
  (137/137 à 0,9 h, §29). Causes tuées : intervalle MEXC « 1h » rejeté (le bon est
  « 60m »), simu sans ARM, ancre au dernier BUY (+409 h d'écart), arms datés via git,
  pagination MEXC (endTime seul ignoré, plafond 500 → 3× les mêmes bougies).
- Trailing resserré TUÉ par la mesure (§29) : +5,36 $ max, dans le biais — pas câblé.
- Ré-entrée repart : +77,56 $ simulés mais 99 % déjà captés par le moteur (§30) —
  piste enterrée comme règle, validée comme comportement existant.
- Attribution (§31) : le moteur ne capte que 51 % (+39,61/77,56) ; 4 paires rendent
  -43,95 $ (cash_redeploy instantané → stops en cascade) ; W/RED/ZBCN BATTENT la règle.
- Variantes (§32) : 48 h > 24 h ; COOLING +50,23 $ vs IMPULSE +1,29 $ → shadow
  adaptatif câblé (48 h/14 j, COOLING seul, 3 paires, 0 ordre).
- ERREUR DÉCLARÉE (§32) : mon insertion a cassé le boot (UnboundLocalError, 2 crashs
  watchdog) — réparée, dry-run depuis. Leçon : dry-run avant tout restart.
- Acquis maison déjà métacognitifs : journal exhaustif (tous les essais, même tués),
  R8 (limites écrites), § (mémoire épisodique), resceler (constitution versionnée),
  questions fermées avant mesure (pré-enregistrement), shadow ACHAT/EXPIRE (désaccord
  à venir). Manque : déflation par essais, juge de la MÉTHODE, grille pré-câblage.

=== LES 4 PROPOSITIONS (à juger une par une) ===
P1. Règle R-méta pré-câblage : 5 questions écrites (qu'est-ce qui tuerait cette
    conclusion ? écart significatif ? données manquantes ? inverse testé ? qui
    relit ?) + barre d'acceptation écrite AVANT la mesure. Réponse manquante =
    shadow seul, pas de câblage.
P2. Déflation par essais : tout « meilleur de N variantes » doit battre le runner-up
    d'une marge > biais instrument, sinon c'est le hasard qu'on câble.
P3. Cortana-méthode : dimension qui note NOS analyses (n, biais, significativité),
    critères découplés du marché, Christophe = ancre humaine (son GO = holdout).
P4. Registre des désaccords : SHADOW_ACHAT vs EXPIRE + GO/refus de Christophe,
    relus comme les §.

=== QUESTIONS (réponds à CHACUNE, court et net) ===
Q1. Les 4 piliers marché : lequel est le plus dangereux à mal implémenter chez nous,
    et quelle garde-fous concret proposes-tu contre ce danger ?
Q2. P1..P4 : pour CHAQUE proposition, VERDICT (GO / GO-AVEC-RÉSERVES / NON) + 1 ligne
    de motif + 1 amélioration concrète si réserves.
Q3. La faille que ni les 4 piliers ni les 4 propositions ne couvrent : vois-tu un
    angle mort métacognitif restant dans la maison (pense au crash boot §32, au
    +2,45 $ câblé §33, au juge-acteur qui partagent mon cerveau) ?
Q4. UNE proposition à toi, GO-sized, que personne n'a faite (marché + maison).

FORMAT ATTENDU :
VERDICT GLOBAL : GO / GO-AVEC-RÉSERVES / NON (pour l'intégration métacognition)
CONFIANCE : XX%
Q1..Q4 : réponse courte à chaque question.
MOELLE : 5 lignes max — la substance à garder dans l'historique.
"""

CONTEXTE_AVUGLE = """\
CONSULTATION FAMILLE + JUGE — métacognition : que proposes-TU ? (28/10/2026, Buffy)

ATTENTION : on ne te donne AUCUNE solution maison. C'est TOI qui proposes.
Ne cherche pas ce qu'on attend — dis ce que TU ferais, même si ça contredit tout.

=== L'ÉTAT DE L'ART (faits, pas nos idées) ===
1. Nelson-Narens : séparer celui qui FAIT de celui qui REGARDE. Le regard ne touche
   à rien ; le contrôle est rare et verrouillé.
2. Reflexion (Shinn 2023) : Acteur/Évaluateur/Réflecteur SÉPARÉS — le juge qui
   partage les biais de l'acteur ne voit rien (+11 pts sans réentraînement).
3. Gençay 2026 : un robot qui teste 100 variantes et montre la meilleure MENT par
   sélection — déflater par le nombre d'essais ; hypothèse annoncée avant > trouvaille après.
4. TradingAgents (80 000 étoiles GitHub) : équipe d'analystes → débat haussiers VS
   baissiers → trader → équipe risque avec VETO ; backtests qui ne voient que les
   données publiées à la date d'analyse (lookahead impossible par construction) ;
   managers et analystes sur des MODÈLES DIFFÉRENTS (anti-collusion) ; chaque rapport
   enregistre ses réglages ; décisions passées soldées pour chaque ticker.
5. Self-critique evaluator : le juge = portail d'abord, jamais récompense ; critères
   découplés, contre-exemples, ancre humaine ; suivre le taux de désaccord juge/humain.

=== NOTRE HISTORIQUE (faits bruts, 28/10) ===
- Moteur paper trading crypto (HULK, MEXC). Doctrine : chiffres, mesure-avant-câblage,
  test fantôme sans ordre, tout réversible en 1 ligne.
- Garde-fou fidélité : un simulateur refusé 4 fois avant validation (137/137 à 0,9 h).
  Erreurs tuées : mauvais intervalle API, simulateur sans seuil d'armement, mauvaise
  ancre temporelle (+409 h d'écart), données paginées en triple (3× les mêmes bougies).
- Idée « sortir plus tôt » TUÉE par la mesure (+5 $ dans le biais). Idée « ré-entrée »
  à +77 $ ENTERRÉE : le moteur faisait déjà le boulot à 99 %.
- Audit : le moteur ne capte que 51 % du repart ; 4 paires perdent par rachat
  instantané (-43,95 $) ; réglage adaptatif câblé en fantôme (48 h, sorties creux
  seules, 3 paires, 0 ordre).
- Crash au redémarrage causé par ma propre modif (2 crashs, réparé) — leçon : dry-run
  avant tout restart.
- Acquis : journal exhaustif de TOUS les essais (même tués), limites écrites sur chaque
  mesure, constitution versionnée, questions fermées avant mesure, registre d'erreurs
  public (§29-§34).

=== QUESTIONS (c'est TOI qui proposes) ===
Q1. Propose TON dispositif métacognitif pour cette maison : 3 règles max, concrètes,
    branchables, chacune en 2 lignes (quoi + comment on vérifie que ça marche).
Q2. Quel point de l'état de l'art est le plus dangereux à mal implémenter chez nous,
    et quel garde-fou concret ?
Q3. Quel angle mort vois-tu que l'historique ci-dessus ne montre pas ?
Q4. UNE proposition à toi, petite et branchable, que personne n'a faite.

FORMAT ATTENDU :
VERDICT GLOBAL : GO / GO-AVEC-RÉSERVES / NON (faut-il intégrer la métacognition ?)
CONFIANCE : XX%
Q1..Q4 : réponse courte à chaque question.
MOELLE : 5 lignes max — la substance à garder.
"""


def ask(task, outname, role):
    payload = {
        "task": task,
        "messages": [
            {"role": "system", "content": SYSTEM + "\n\n" + CLAUSE + "\n\nRôle : " + role},
            {"role": "user", "content": CONTEXTE},
        ],
        "max_tokens": 2500,
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
            fh.write(f"# AVIS ({task} · {role} · provider {provider} · 2026-10-28)\n\n{content}\n")
        print(f"[OK] {outname} ({provider})")
    except Exception as e:
        print(f"[ERR] {task}: {e}")


def main():
    args = sys.argv[1:]
    aveugle = "aveugle" in args
    if aveugle:
        global CONTEXTE
        CONTEXTE = CONTEXTE_AVUGLE
    who = (args or ["all"])[0]
    suf = "_BLIND" if aveugle else ""
    if who in ("all", "famille"):
        ask("famille.analyse", f"AVIS_FAMILLE{suf}.md",
            "membre famille, relecture factuelle et rigoureuse, chiffrée.")
    if who in ("all", "juge"):
        ask("gemini.analyse", f"AVIS_JUGE{suf}.md",
            "JUGE : architecture et méthode. Tu tranches et donnes le verdict global. "
            "Sévère et juste : un GO immérité coûte du PnL.")
    if who in ("all", "cortana"):
        ask("cortana.analyse", f"AVIS_CORTANA{suf}.md",
            "Tu es CORTANA. On envisage de te faire juger la méthode : faisabilité, "
            "risques de collusion juge-acteur, ce qu'il te faudrait. Contrat ADVISORY.")
    print(f"== avis {'AVEUGLES' if aveugle else ''} dans {OUT}")


if __name__ == "__main__":
    main()
