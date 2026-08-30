# MÉTHODE — CONFRONTATION GEMINI (validée Christophe, 24/08/2026)

> **Quand l'utiliser** : pour toute décision IMPORTANTE ou tout indicateur à mettre
> « au top et incassable » (conception, recalibrage, garde-fous, choix de seuils).
> **Pourquoi** : l'erreur du 23/08 (consultation « audit général » en 4 tours fixes,
> ~5 h, hors-sujet) a montré qu'un dialogue non dirigé part dans tous les sens.
> Cette méthode transforme Gemini en **second avis d'experte indépendant**, puis en
> **partenaire de compromis** — le but est le MEILLEUR SETUP, pas d'avoir raison.
> **Résultat de référence** : `COMPROMIS_POUSSIERE_GEMINI_20260824.md` (6 tours,
> ~22 s d'API, indicateur poussière au top).

---

## Principe central

**Ne JAMAIS donner nos valeurs au départ.** Si on donne notre setup, Gemini se
contente de valider ou d'ajuster à la marge → on reste piégé dans nos propres
choix. On décrit le SYSTÈME (but, architecture, contraintes, leçons) sans chiffres,
et c'est ELLE qui conçoit avec SES valeurs → on obtient un vrai second avis
indépendant. Puis on confronte.

---

## La boucle de direction (rôle du superviseur = Buffy)

```
TOUR 1 — CONTEXTE GÉNÉRALISTE (zéro valeur de notre part)
        → but, architecture, contraintes, leçons passées.
        Elle propose un design complet avec SES valeurs chiffrées.

JE LIS SA RÉPONSE → ANALYSE : a-t-elle compris le CONCEPT ?
   (le concept = le mécanisme central du sujet, pas la surface)

   ┌─ NON → je lui donne des INDICES ciblés → elle répond à nouveau
   │        (boucle jusqu'à compréhension)
   └─ OUI → je la REDIRIGE vers l'amélioration / la mise en place

J'ATTENDS ses VALEURS chiffrées (chaque paramètre demandé)

JE VÉRIFIE ses valeurs contre CE QUE JE SAIS (données réelles,
documents d'enquête, contraintes terrain — PAS contre nos valeurs)

   ┌─ FAUSSES / INCOHÉRENTES → indices jusqu'à correction
   │        (vérifier la COHÉRENCE INTERNE : ses seuils se contredisent-ils ?
   │         sont-ils possibles sur un cas réel ? respectent-ils les contraintes ?)
   └─ CORRECTES → je POUSSE l'amélioration jusqu'au plafond :
        « as-tu atteint le maximum exigeable ? » → elle doit conclure
        ON NE PEUT PLUS FAIRE MIEUX (sinon elle continue)

CONFRONTATION — je lui révèle notre setup réel, point par point.
   Pour CHAQUE désaccord : on tranche (sa valeur / notre valeur / compromis)
   avec une justification. Le but : le meilleur setup, pas avoir raison.
```

---

## Les 5 règles d'or (tirées du cas poussière 24/08)

1. **Ne jamais donner nos valeurs au TOUR 1.** Décrire le système sans chiffres.
   (Elle a proposé 15 s puis corrigé à 120 s seule — la bonne valeur.)

2. **Diriger tour par tour, lire chaque réponse, analyser la compréhension.**
   Pas de script à tours fixes. On décide le message suivant selon SA réponse.
   (Le 23/08 : 4 tours fixes sans lecture → hors-sujet.)

3. **Vérifier ses valeurs contre la TERRAIN, pas contre nos valeurs.**
   - Cohérence interne : ses seuils se croisent-ils sur un cas réel ?
     (Elle a posé « taux ≥ 15 % ET volume ≥ 1,5 Mo » → impossible sur un bloc de
     4200 tx ; on l'a fait corriger.)
   - Contraintes réelles : API gratuite sans clé, anti-ban, M1 8 Go, stdlib.
   - **Tester les hypothèses d'API en direct avant d'appliquer.**
     (Elle a promis « volume exact via le résumé du bloc » → testé en direct :
     `/api/block/{hash}` = header SANS txs → correction rejetée, adaptée.
     C'est LE point qui a évité une régression.)

4. **Pousser jusqu'au plafond.** Dernier tour : « pousse jusqu'au plafond, cherche
   les angles morts de CETTE chaîne, conclus par ON NE PEUT PLUS FAIRE MIEUX ou
   ENCORE UNE AMÉLIORATION ». Exiger la phrase exacte pour forcer la décision.

5. **Confrontation explicite.** Tableau point par point (sa valeur / notre valeur /
   retenu), chaque désaccord tranché avec justification. Documenter le compromis
   final + ce qui ne change pas. **Si une correction n'est pas validée à 100 %,
   ne pas l'appliquer : la re-confronter ou l'adapter, jamais aveuglément.**

---

## Format de sortie

- **Dialogue complet** : `scripts/CONSULTATION_GEMINI_<SUJET>_<DATE>/TOURn.md` + `etat.json`
  (script réutilisable : `scripts/dialogue_gemini_<sujet>.py` — un tour à la fois,
  état conservé, direct API, gestion 429).
- **Compromis final** : `COMPROMIS_<SUJET>_GEMINI_<DATE>.md` — tableau des valeurs
  retenues + origine (elle / nous / compromis) + justification + preuves.
- **Mémoire** : ligne datée dans `MEMOIRE_COLLAB.md`.

— Méthode validée par Christophe le 24/08/2026 (« je veux qu'on trouve le meilleur
compromis ») après le cas poussière conclu en 6 tours.