# 💡 PROPOSITIONS D'AMELIORATION — 2026-08-15

> Genere par propose_ameliorations.py (rituel proactif 09/08).
> Le juge PROPOSE (maker!=checker), GEMINI CONTRE-VERIFIE (famille differente),
> Christophe TRANCHE. Personne ne valide seul (loi 1quater).

## Top 3 — proposé par le juge

1. Blame router (L1-L4)
   QUOI: Classifier les bugs selon l'étage (ask, contexte, harnais, boucle) avant d'investiguer.
   PREUVE: Pépite #1 (@starmexxx, I/I/I) — "73% des bugs = 1 étage en dessous".
   IMPACT: Évite de chercher au mauvais endroit et réduit drastiquement le temps de debug.

2. Politique d'oubli & graphs temporels
   QUOI: Marquer l'ancien contexte comme invalide sans le supprimer immédiatement.
   PREUVE: Pépite #4 et #13 (@UnTalNixon_exe, @mem0ai, I/I/I) — convergence sur les agents qui rêvent.
   IMPACT: Nettoie la mémoire chaude, réduit la confusion des agents et préserve la cohérence.

3. Budget de latence avant optimisation
   QUOI: Mesurer systématiquement le temps et les tokens consommés avant chaque refactoring lourd.
   PREUVE: Pépite #7 (@0x_Punisher, I/I/I).
   IMPACT: Empêche les optimisations prématurées et rationalise l'usage des providers du hub.

RECO: Implémenter le blame router (#1) en premier pour structurer immédiatement la résolution des bugs de cette session.

## Contre-vérification — Gemini (famille différente)

VERDICT: OK
OBJECTIONS: aucune
PRIORITE: Le #1 (Blame router) en premier, car la mission tourne en alerte amber (PnL -4.54 $) et localiser immédiatement les frictions L1-L4 évitera de gaspiller le budget cloud (déjà 191 appels).

---
_Backlog source : TABLEAU_PEPITES_2026-08-08 (43 INTEGRER / 14 VERIFIER) + IDEES + VEILLE_HUB._
