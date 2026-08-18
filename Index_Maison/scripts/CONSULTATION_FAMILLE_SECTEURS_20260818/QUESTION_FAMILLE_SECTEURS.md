# QUESTION FAMILLE — Diagnostic par secteurs : trouver le goulot n°1 (18/08/2026)

> Objet : avant d'installer les pépites des signets, diagnostiquer le système par
> SECTEURS pour trouver le goulot d'étranglement — puis n'installer QUE la pépite
> qui débloque le goulot n°1 global (séquentiel, pas parallèle — votre réserve du 15/08).
> Christophe : « trouver le goulot d'étranglement ou autre dans tout le système, le diviser
> en plusieurs secteurs pour que ce soit plus lisible. »
> Règle d'économie : 2 membres + juge. Tout est réversible, rien ne se supprime.

---

## 1. Le système découpé en 7 secteurs

| Secteur | Contenu | Goulot suspect (à confirmer/infirmer) | Pépites candidates |
|---|---|---|---|
| **EXÉCUTION (hot)** | ACE, Hulk, moteur, fills, stops, sizing | 🔴 sizing → ruine 32,5 % (Monte Carlo 18/08) | Kelly (43+105), sorties > position |
| **DÉCISION / STRATÉGIE** | radar, indices, decision engine, modes | 🟡 filtre strict → P(fill) 6,5 % | TradingAgents (189), Alpha Orchestration |
| **MÉMOIRE / CONNAISSANCE** | Cortana, Ada, vault, justesse, leçons, agora | 🟡 Cortana stateless, justesse 44,4 %, leçons sans plist propre | 6 fichiers (192), mémoire agents (53/12), dérive mémoire (0xWast3) |
| **INFRA / HUB IA** | providers, routeur, chaîne 7h, roulement | 🟡 6 obs-* morts aux sondes (0/5), nara/nvidia lents | formats 4-bit (130), LLMRouter (6) |
| **SURVEILLANCE / SANTÉ** | veilleuses, superviseur, préflight, alertes | 🟢 bien armé (3 veilleuses) | CheckCle (111) |
| **VEILLE / INGESTION** | flotille, signets, scan GitHub, données | 🟡 signets = mine mais non ingérés automatiquement | Data Formulator, pipeline 8 étages (16) |
| **GOUVERNANCE / PROCESS** | famille, juge, codeur, Release Receipt | 🟡 Release Receipt pas standardisés partout | garde-fous (30/31) |

## 2. Contexte chiffré (18/08, preuves à la main)

- **Monte Carlo** : ruine 32,5 % même en période propre (base scellée) — chantier sizing ouvert + veilleuse 22/08
- **Cortana** : 112 notations, 44 hits (44,4 %) — elle apprend mais reste sous 50 %
- **Hub** : 6 obs-* à 0/5 aux sondes (quotas épuisés — l'observatoire tranchera dans 48h)
- **Chaîne IA** : 7 agents armés 7h00→7h15, validée par vous ce matin (GO-AVEC-RÉSERVE unanime)

## 3. Questions à la famille

1. **Le goulot n°1 GLOBAL du système** : quel secteur est le plus bloquant AUJOURD'HUI ?
   (EXÉCUTION/sizing ? MÉMOIRE/Cortana ? HUB ? Autre ?) Tranchez net.
2. **Pour votre secteur de prédilection** : quel est SON goulot n°1, et la pépite qui le
   débloque ?
3. **Le choix « UNE pépite par goulot »** : est-ce la bonne discipline, ou voyez-vous un cas
   où il faut 2 pépites ensemble pour débloquer le même goulot ?
4. **Risque d'installation** : installer une pépite maintenant (pendant le run 96h, lecture
   seule) est-il sans danger, ou vaut-il mieux TOUT attendre la fin des runtests (22/08) ?

Merci — 3 phrases max par réponse, tranchez net (GO / GO-AVEC-RÉSERVE / NON).
