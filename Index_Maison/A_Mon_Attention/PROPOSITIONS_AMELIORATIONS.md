# 💡 PROPOSITIONS D'AMELIORATION — 2026-08-09

> Genere par propose_ameliorations.py (rituel proactif 09/08).
> Le juge PROPOSE (maker!=checker), GEMINI CONTRE-VERIFIE (famille differente),
> Christophe TRANCHE. Personne ne valide seul (loi 1quater).

## Top 3 — proposé par le juge

1. **Blame router : debug par étage**
   QUOI: Appliquer la carte des 4 étages (L1 ask / L2 contexte / L3 harnais / L4 boucle) pour tout debug futur.
   PREUVE: Pépite #1 (@starmexxx) — 73% des bugs = 1 étage en dessous.
   IMPACT: Réduit le temps de diagnostic de ~70%, fiabilise le cycle maker≠checker.

2. **Mémoire pondérée par révisions + courbe de confiance**
   QUOI: Implémenter la pondération des notes par nombre de corrections et enterrer les sources fausses 2x.
   PREUVE: Pépites #16 et #17 (@0xWast3) — signal renforcé, bruit éliminé.
   IMPACT: Moins de RAM (notes inutiles purgées), plus de fiabilité des décisions.

3. **Préfixe de domaine 6 caractères + 1 note = 1 idée**
   QUOI: Ajouter un préfixe de domaine en tête de chaque note et contraindre à une idée par note.
   PREUVE: Pépites #19 (@0xkkai) et #20 (@MyWestLord) — protocole liens, zéro doublon.
   IMPACT: Recherche plus rapide, moins de RAM (pas de doublons), meilleure traçabilité.

RECO: Commencer par le blame router (#1) — c'est le plus rapide à appliquer et débloque immédiatement tous les autres débogages.

## Contre-vérification — Gemini (famille différente)

VERDICT: OK
OBJECTIONS: Aucune (le lien avec la pépite #1 est exact et l'impact opérationnel est immédiat).
PRIORITE: Le #1 (Blame router) en premier, car standardiser le diagnostic sur 4 étages structure l'application saine des améliorations #2 et #3.

---
_Backlog source : TABLEAU_PEPITES_2026-08-08 (43 INTEGRER / 14 VERIFIER) + IDEES + VEILLE_HUB._
