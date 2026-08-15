# Bilan 7 jours — Détection CPFP / Poussière (ACE777)
*Généré le : 2026-08-15T21:08:37.870298+00:00*

## État
- **Mode** : observation (SILENCIEUX tant que non validé)
- **Alerte émise** : JAMAIS (observation stricte)
- **Confirmation courante** : 0 / 2
- **Runs observés (7j)** : 3
- **Runs avec déclenchement global** (z-score ET CPFP) : 0

## Déclenchements par carte
- Carte 1 (z-score adaptatif ≥3.0σ + plancher 500 BTC) : 0
- Carte 2 (signature CPFP par frais ≥20× médiane) : 0
- Carte 3 (poussière <2.0 sat/vB, seuil 1000/48h) : 0

## Calibration observée
- Médiane frais 7j : 1.0 sat/vB
- Moyenne mobile 7j : 0.0 BTC
- Sigma : 0.0
- Max dust vu : 0.0 BTC

## Détail de la dernière passe
```json
{
  "carte1_zscore": {
    "declenche": false,
    "score": 0.0,
    "detail": "pas assez de données"
  },
  "carte2_cpfp": {
    "declenche": false,
    "score": 0.0,
    "detail": "pré-filtre : frais 1 sat/vB ≤ 20× médiane 7j (1) — pas de creusage"
  },
  "carte3_poussiere": {
    "declenche": false,
    "score": 0.0,
    "detail": "poussière <2.0 sat/vB : 0 vues ce run, 0 cumulées 48h (seuil 1000) — max 0.0000 BTC"
  }
}
```

---
**DÉCISION REQUISE (Christophe)** : après lecture de ce bilan, soit
`python3 detecter_cpfp.py --actif` (brancher les alertes), soit ajuster les seuils
dans la spec et recalibrer.
