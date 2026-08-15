# CHANTIER — ONCHAIN v2 : Détection CPFP / Poussière / Z-score (15/08/2026)

**Statut :** ✅ LIVRÉ + TESTÉ (mode observation 7 jours)
**Pépite :** la découverte UTXO/CPFP de Christophe (camouflage de baleines)

---

## Pourquoi

Le scan actuel (≥1000 BTC) est **aveugle** au camouflage UTXO+CPFP : une baleine peut
déplacer des milliers de BTC en éclatant son UTXO en un arbre de poussière à frais
quasi nuls, puis en déclenchant le tout par une transaction enfant à frais
astronomiques (CPFP) qui force le mineur à valider l'arbre entier.

**Principe :** les baleines connaissent les seuils publics → un seuil plus bas fixe
serait contourné aussi. La réponse = **seuils statistiques adaptatifs** (la ligne
bouge chaque jour) + **signatures inaltérables** (le frais astronomique EST le
mécanisme).

## Décisions validées

| Décision | Détail |
|---|---|
| Portée option 1 | Nouveau module v2 SANS toucher au scan actuel |
| **Silencieux 7 jours** | Observation + calibration, AUCUNE alerte avant validation |
| Alerte finale | Vocale en boucle (veilleuse) + cockpit + Cortana/Ada |
| Seuils | z≥3σ adaptatif + plancher 500 BTC + double condition (z ET CPFP) + 2 confirmations |
| Pré-filtre API | Ne creuser QUE si frais >20× médiane + backoff + cache (free tier) |
| Pondération | Signal ×0.5 tant que non validé en réel |

## Ce qui a été livré

1. **`detecter_cpfp.py`** (NOUVEAU) — 3 cartes :
   - Carte 1 : z-score adaptatif (normale = jours précédents, anomalie = aujourd'hui)
   - Carte 2 : signature CPFP par frais (pré-filtre + backoff + creusage parents)
   - Carte 3 : poussière <2 sat/vB (anticipation, agrégée 48h)
   - Mode observation par défaut, `--bilan` pour la décision des 7 jours, `--actif`
2. **`pont_onchain.py`** (MODIF) — enrichit la section onchain SI mode actif ET
   confirmation ≥2 ET double condition : cpfpSignal + cpfpScore (×0.5)
3. **`ada_gardienne.py`** (MODIF) — modulateur CPFP −7% de voilure si EXÉCUTION CPFP
4. **Cortana** — AUCUNE modif nécessaire (déjà branchée sur la synthèse onchain ;
   reçoit la phrase pré-mâchée automatiquement)
5. **`com.ace777.cpfp.plist`** (NOUVEAU) — cadence 10 min launchd, chargée
6. **Registre veilleuse** mis à jour (v1.1.0, 19 items)

## Bugs trouvés en supervision (codeur)

| Bug codeur | Correction |
|---|---|
| Signature `calculer_voilure(capital_actuel, vol_actuelle)` inventée | Réutilisé la vraie signature `(p, thermo=None)` |
| Clés `montant`/`frais_sat_vb`/`dernier_scan` inventées | Utilisé la vraie structure (`btc`, `ts`, `type`) |
| Carte 2 CPFP non implémentée (regardait tx_count d'un bloc) | Implémenté : pré-filtre frais + parents/enfants |
| Double condition OR au lieu de AND (D5) | Corrigé : `z AND CPFP` |
| **Bug de conception découvert en test** : moyenne mobile incluant le pic → signal dilué (z=2.65 pour un pic 8×) | Corrigé : normale = jours précédents, anomalie = aujourd'hui (z=410 pour 800 BTC vs normale 98±1.7) |

## Tests réels effectués

| Test | Résultat |
|---|---|
| Mode observation : silencieux, aucun effet live.json | ✅ |
| Pré-filtre API respecté (frais 1 sat/vB → pas de creusage) | ✅ |
| z-score : pic 800 BTC vs normale → z=410, déclenche | ✅ |
| Pont : signal NON injecté en observation | ✅ |
| Pont : signal injecté si actif + confirmation 2 (score ×0.5) | ✅ |
| Ada : voilure −7% avec signal CPFP (borne ±10%), tests existants TOUS VERTS | ✅ |
| Cortana (hub réel) : intègre le signal — « préparation imminente d'un déplacement de liquidité massive », NEUTRE, confiance haute | ✅ |
| Veilleuse : rc=0 état sain après mise à jour du registre | ✅ |
| Plist : chargée, premier run launchd OK | ✅ |

## Prochaine étape (dans 7 jours)

`python3 Index_Maison/scripts/detecter_cpfp.py --bilan` → lire
`Index_Maison/data/CPFP_BILAN_7JOURS.md` → décision Christophe :
- `--actif` pour brancher les alertes, OU
- ajuster les seuils dans la spec et recalibrer.

Références de calibration de Cortana : 4000 tx poussière/2h · 10000 sorties <0.01 BTC/6
blocs · enfant >500 sat/vB (à comparer à nos seuils arbitrés : 1000/48h · 20× médiane).
