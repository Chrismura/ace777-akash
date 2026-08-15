# CHANTIER — Dérive mémoire (4 indicateurs @0xWast3) — 15/08/2026

**Statut : APPLIQUÉ + TESTÉ** · lecture seule · réversible.

## Décision famille (gemini 85% / nvidia 72%)
Consensus sur cette piste (rang 1 gemini, rang 2 nvidia, indépendamment). Origine : signet N°1 @0xWast3 — un système de mémoire qui surveille SA PROPRE santé (4 indicateurs) pour détecter le savoir obsolète avant qu'il ne pollue les décisions.

## Livré
- `Index_Maison/scripts/derive_memoire.py` : module autonome stdlib, 4 indicateurs par indice :
  - **I1 Fréquence de référence** : FROID (≥7j sans analyse) / SOUS-UTILISÉ (≤2 analyses/14j)
  - **I2 Taux de contradiction** : flip-flop LONG↔SHORT > 50% → INSTABLE
  - **I3 Vitesse de décroissance** : PÉRIMÉ (>7j) / CRITIQUE (>14j)
  - **I4 Dispersion de confiance** : calibration vs pile-ou-face (justesse ≤40% → CRITIQUE)
  - Statut = le pire des 4 · exit 0/1/2.
- Rapport `thermo/DERIVE_MEMOIRE.md` + JSON `strategie/derive_memoire.json`.
- Branchement dans `discipline_quotidienne.py` : appel fail-open après la re-note Cortana + alerte `DÉRIVE MÉMOIRE` si rc≥1 + section « MÉMOIRE (dérive) » au rapport. Launchd 07h15 déjà en place → **se nourrit tout seul chaque jour**.

## Vérifications (vertes)
- `py_compile` OK · run réel : 12 indices, **3 instables / 7 critiques** — cohérent avec la réalité (funding 35%, fearGreed 33%, btc 37.5% → CRITIQUE · radar 50% / verre 67% → STABLE · bassine 100% mais 9j sans analyse → PÉRIMÉ). La mémoire dit la vérité sur Cortana.
- Discipline + dérive testées ensemble : alerte `DÉRIVE MÉMOIRE : au moins 1 indice CRITIQUE` déclenchée, rapport mis à jour, exit=3 (alertes présentes).

## Note honnête
- Le codeur (gemini) a été coupé à 4000 tokens (fin d'`ecrire_json` + diff discipline manquants) et contenait une coquille (`lignes_ md`). J'ai complété la fin selon la spec, corrigé la coquille, et rédigé le branchement discipline moi-même. Le cœur (chargement, 4 indicateurs, extraction avis) est du codeur et a été vérifié ligne à ligne.
- I4 utilise la justesse par indice (justesse_v2.json) — les données par confiance (haute/faible) ne sont pas encore stockées séparément ; c'est le prochain raffinement possible.

## Retour arrière (réversible)
- `rm Index_Maison/scripts/derive_memoire.py` + revert du branchement dans discipline_quotidienne.py (git checkout si commité).
