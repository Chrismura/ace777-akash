# FAUTES TRÈS GRAVES — Masse et Insubordination (2026-02-27)

## 1. MODIFICATION DE MASSE SANS ORDRE

**Erreur :** L'IA a modifié `BUY_USDT_BETA` de 200 à 250 sans que l'utilisateur le demande.

**Ordre de l'utilisateur :** Masse BETA = 200.

**Action de l'IA :** A mis 250 "pour marge" — INSUBORDINATION.

**Règle :** Ne jamais modifier les valeurs de masse sans ordre explicite.

---

## 2. ERREUR -4164 (Notional < 100)

**Cause :** INITIAL_FRACTION=0.25 ou 0.50 avec BUY_USDT_BETA=200 → après réductions (SOFT_MASS_FACTOR, dynamic_sizing), l'ordre initial tombait sous 100 USDT.

**Solution correcte (injonction utilisateur) :** INITIAL_FRACTION=0.70 pour BETA (70% de 150 = 105 USDT). Pas toucher à la masse.

**Erreur de l'IA :** A augmenté la masse au lieu de corriger la fraction.

---

## 3. INCOMPRÉHENSION DE LA CHAÎNE DE MODULES

**Erreur :** L'IA a présenté deux modules modifiés sans expliquer clairement que l'utilisateur ne lance qu'un seul fichier (`launch_vide_froid_4h_binance.sh`).

---

## RÈGLES À RESPECTER

1. **Masse :** Ne jamais modifier BUY_USDT_BETA/ALPHA sans ordre explicite.
2. **Fraction :** Pour éviter -4164, ajuster INITIAL_FRACTION (0.70 pour BETA) — pas la masse.
3. **Clarté :** Expliquer quel fichier lancer, pas multiplier les modules sans contexte.
