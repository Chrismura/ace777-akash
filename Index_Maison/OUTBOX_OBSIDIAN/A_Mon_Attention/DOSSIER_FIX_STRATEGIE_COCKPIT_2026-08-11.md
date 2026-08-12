# DOSSIER FIX — ONGLET STRATÉGIE VIDE (11/08/2026)

## SYMPTÔME
L'onglet STRATÉGIE du cockpit affichait « Chargement des stratégies… » à vie :
les cartes (STRATÉGIES DE L'ANALYSTE, NOUVELLES OFFRES, EXPLORATION) restaient
vides, aucune requête n'arrivait au bridge :17777. Symptôme présent depuis
l'ajout de la carte STRATÉGIES (11/08).

## DIAGNOSTIC (preuve par rendu navigateur réel, Brave headless)
- Le bridge répond en 2-12 ms, CORS OK, endpoint /strategie et /offres OK.
- Un fetch standalone depuis la même origine fonctionne (OK, 4,5 Ko).
- MAIS dans la page complète : aucune requête /strategie ni /offres au bridge.
- Cause racine : `const BRIDGE='http://127.0.0.1:17777'` est déclarée dans le
  bloc <script> 4 (logique OPS) — or `const` est SCOPÉE à son bloc script.
  Le bloc 5 (cosmos + cartes STRATÉGIE/OFFRES/👁/DÉCOLLER) n'avait pas de
  BRIDGE locale → `ReferenceError: BRIDGE is not defined` à l'exécution de
  `chargerStrategie()`/`chargerOffres()` → exception avalée par try/catch →
  onglet vide, aucun fetch, « Chargement… » pour toujours. Aucune erreur visible.

## CORRECTIONS APPLIQUÉES (index.html, backup .bak-robuste-20260811-185951)
1. `const BRIDGE='http://127.0.0.1:17777'` déclarée dans le bloc 5 (après 'use strict').
2. Boot `_bootStrategie` : retry conditionnel (3 tentatives max, 2,5 s d'écart,
   uniquement si le placeholder « Chargement » est encore présent ou liste vide).
3. `fetchJson` : cache 'no-store' systématique.
4. `console.error` dans les catch (le bug était invisible car avalé en silence).

## VÉRIFICATION
Rendu Brave headless : COURT TERME affiché, « Chargement… » disparu, providers
chargés. Backups + copie trace dans ~/test-freebuff.
