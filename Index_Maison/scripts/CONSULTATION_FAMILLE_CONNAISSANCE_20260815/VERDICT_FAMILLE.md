# VERDICT FAMILLE — Couche de connaissance ACE777 (15/08/2026)

**Avis reçus** : gemini (85%), nvidia (78%) = 2/4 (openrouter 502 réseau, habituel).

## Verdict : GO-AVEC-RÉSERVE (convergent)

## 1. Schéma de la base — affiné
Ajouts validés par les deux :
- **`horizon_bag`** (court/moyen/long terme) — gemini + nvidia
- **`classe_hulk`** (A_core / B_bag) — sync directe avec les 2 classes Hulk — gemini + nvidia
- **`date_peremption_faits` / `expires_at`** — péremption obligatoire — gemini + nvidia
- **`score_confiance_interne`** (basé sur verdict famille) — gemini + nvidia
- **`capital_alloue_max`** (garde-fou chiffré) — nvidia
- **`statut_verification` STRUCTURÉ** : `{date, verdict, score, reserve}` (pas une chaîne
  libre — filtrage automatique possible) — nvidia

Divergence : nvidia propose de **supprimer `signets_cles`** (redondant avec
SIGNETS_RESUMES.json → garder un compteur/lien). gemini le garde.

## 2. Anti-engraissement — critères d'entrée stricts (convergent)
- **Règle 1** : un fait n'entre QUE s'il est validé par un audit formel (verdict famille)
  **OU** sourcé par un signet « garder » à forte conviction — gemini
  **OU** 2 sources indépendantes (institutionnel + on-chain, ou 2 audits distincts) — nvidia
- **Règle 2** : péremption — 90 jours (fondamentaux) / 30 jours (données marché) — nvidia ;
  tout fait non actualisé 90 j → statut `OBSOLÈTE`, exclu des injections — gemini
- **Règle 3** : fait non vérifié 7 jours → `en_attente` (hors injection) — nvidia
- **Règle 4** : quota max 50 faits/projet (au-delà → purge des plus anciens) — nvidia
- **Auto-nettoyage hebdo** : purge des périmés + archive des projets inactifs >90 j — nvidia

## 3. Injection — mode HYBRIDE (c) avec garde-fous (convergent)
- **Déclencheur** : à la demande (famille/Cortana) **+** auto si le brief contient un nom
  de projet de la base.
- **Taille max** : résumé synthétique exécutif — ≤300 mots (gemini) / ≤500 tokens (nvidia).
  Jamais la fiche complète en auto.
- **Rotation** : si >3 projets pertinents → 2 plus récents + 1 aléatoire (anti-biais de
  récence) — nvidia.
- **Exclusion** : **jamais injecter les `lecons` (sizing/stops) en mode auto** — uniquement
  sur demande explicite (ne pas polluer le contexte opérationnel) — nvidia.
- **Budget tokens strict** alloué au BRIEF — gemini.

## 4. Scoring de la base — OUI, simple (convergent)
- Fiabilité par source : institutionnel = 0.9-1.0 · audit famille = 0.7 · signet X = 0.5
- Score global d'un fait = moyenne pondérée des sources
- **Seuil d'injection ≥ 0.6** ; en dessous → `à_confirmer`, exclu de l'auto — nvidia

## Améliorations captées
1. **Lien bidirectionnel** : un audit famille généré alimente automatiquement la base
   (pas de saisie manuelle) — nvidia.
2. **Dashboard de santé** de la base (faits vérifiés vs en attente, projets couverts) — nvidia.
3. Test pilote Canton avant déploiement large — nvidia.

## Décision Buffy (supervision)
Design validé et affiné. Arbitrages retenus :
- **`signets_cles` : GARDÉ mais simplifié** (liste d'ids) — c'est la traçabilité « qui prouve
  quoi », un lien suffit.
- **Règle d'entrée nvidia (2 sources) appliquée** aux faits NON audités ; les audits famille
  restent la source première (la plus fiable).
- **Péremption 90/30 j + statut `OBSOLÈTE`** : retenus — c'est l'antidote à l'engraissement.
- **Injection hybride + exclusion des leçons en auto + rotation** : retenues telles quelles.
- **Chantier = structure de connaissance, zéro touche moteur Hulk** → réversible.
