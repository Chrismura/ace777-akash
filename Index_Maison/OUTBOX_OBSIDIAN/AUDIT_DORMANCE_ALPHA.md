# RAPPORT D'AUDIT : DORMANCE D'ALPHA (ACE777)

**Date de génération** : 2026-08-12 21:14:53 UTC  
**Auteur** : Script automatisé `audit_dormance_alpha.py` (Hub Code IA)  
**Objectif** : Prouver ou réfuter l'asymétrie α/β et isoler le facteur bloquant.

## 1. Métriques de Forme par Fenêtre (Tableau Comparatif)

| Métrique | Fenêtre A (09/07 21h - 10/07 12h) | Fenêtre B (14/07 Journée) |
|---|---|---|
| **Cycles ALPHA** | 1339 | 1252 |
| **Fills ALPHA** | 74 (5.5%) | 21 (1.7%) |
| **Skips ALPHA** | 1265 | 1231 |
| **PnL ALPHA** | **+29.52** | **-13.25** |
| **Cycles BETA** | 1549 | 2225 |
| **Fills BETA** | 160 (10.3%) | 254 (11.4%) |
| **PnL BETA** | +0.83 | +3.77 |
| **Cadence (cycles/min)** | α=1.6 β=1.9 | α=1.3 β=2.6 |
| **Silences ≥ 5 min** | α=8 β=5 | α=11 β=9 |
| **Asymétrie Skips (α/β)** | 0.91x | **0.62x** |

*Ce que ça veut dire :* ALPHA subit une chute drastique de son taux de remplissage et de son PnL en Fenêtre B, tandis que BETA reste remarquablement stable, creusant une asymétrie anormale.

### Répartition des raisons de Skip ALPHA

| Raison (ExitReason) | Skips Fenêtre A | Skips Fenêtre B |
|---|---|---|
| `duo_partner_pause` | 195 | 0 |
| `duo_wait` | 79 | 95 |
| `gap_guard_pause` | 18 | 0 |
| `impulse_resonance_wait` | 172 | 133 |
| `radar_block` | 785 | 957 |
| `stase_ecoute` | 4 | 0 |
| `tactic_mismatch` | 12 | 2 |
| `tension_stale` | 0 | 44 |

*Ce que ça veut dire :* Le blocage par `radar_block` (et secondaires) reste ultra-dominant, confirmant que les portes d'entrée se referment hermétiquement sur ALPHA.

## 2. Détection du Point de Bascule (Série Chronologique ALPHA)

### Fenêtre A (09-10/07)

| Tranche Horaire (UTC) | Taux Remplissage (%) | Fills / Total |
|---|---|---|
| 09/07 21:00 | 2.8% | 6 / 218 |
| 09/07 22:00 | 1.7% | 4 / 241 |
| 10/07 06:00 | 7.0% | 3 / 43 |
| 10/07 07:00 | 4.5% | 5 / 111 |
| 10/07 08:00 | 7.9% | 20 / 253 |
| 10/07 09:00 | 10.5% | 30 / 286 |
| 10/07 10:00 | 2.8% | 4 / 143 |
| 10/07 11:00 | 4.5% | 2 / 44 |

### Fenêtre B (14/07)

| Tranche Horaire (UTC) | Taux Remplissage (%) | Fills / Total |
|---|---|---|
| 14/07 03:00 | 0.0% | 0 / 1 |
| 14/07 04:00 | 7.7% | 9 / 117 |
| 14/07 05:00 | 2.2% | 3 / 134 |
| 14/07 06:00 | 2.4% | 5 / 205 |
| 14/07 07:00 | 0.0% | 0 / 236 |
| 14/07 10:00 | 0.7% | 1 / 147 |
| 14/07 11:00 | 2.2% | 1 / 45 |
| 14/07 14:00 | 0.0% | 0 / 39 |
| 14/07 15:00 | 0.0% | 0 / 179 |
| 14/07 17:00 | 0.0% | 0 / 6 |
| 14/07 18:00 | 1.4% | 2 / 142 |
| 14/07 20:00 | 0.0% | 0 / 1 |

*Ce que ça veut dire :* Permet de voir si la dégradation s'est installée progressivement ou suite à un redémarrage/changement de régime précis.

## 3. Comparaison des Paramètres de Configuration

| Paramètre Clé | Fenêtre A | Fenêtre B | Statut / Delta |
|---|---|---|---|
| `RADAR_MIN_CONF_ALPHA` | N/A | N/A | Non trouvé |
| `RADAR_MIN_CONF_BETA` | N/A | N/A | Non trouvé |
| `RADAR_MAX_SPREAD_BPS` | N/A | N/A | Non trouvé |
| `RADAR_GATE` | N/A | N/A | Non trouvé |
| `RADAR_DIR_BPS` | N/A | N/A | Non trouvé |
| `DUO_HUNTER_REQUIRE_STOP_LOSS` | N/A | N/A | Non trouvé |
| `DUO_EVENT_TTL_SEC` | N/A | N/A | Non trouvé |
| `IMPULSE_RESONANCE_DT_MS` | N/A | N/A | Non trouvé |
| `VOLATILITY_IMPULSE_DT_MS` | N/A | N/A | Non trouvé |

> **Conclusion config — HONNÊTE** : les paramètres clés sont **N/A des deux côtés** (extraction impossible depuis les sources disponibles : les logs T1_console ne sont pas parsés par ce script). On ne peut donc **NI affirmer NI infirmer** un changement de config. Cette section est non concluante, pas une preuve d'absence de changement.

## 4. Lecture du Marché & Contexte des Fills

| Métrique Marché (Fills) | Fenêtre A ALPHA | Fenêtre B ALPHA |
|---|---|---|
| **Prix d'entrée moyen** | 64095.76 | 62828.27 |
| **Mouvement moyen (bps)** | 0.47 bps | -0.55 bps |
| **Répartition Long / Short** | {'BUY': 74, 'SELL': 0} | {'BUY': 21, 'SELL': 0} |

*Ce que ça veut dire :* Un mouvement moyen en bps plus faible ou un marché plat assèche mécaniquement les déclenchements d'ALPHA, provoquant l'effet `radar_block`.

## 5. Verdict Synthétique pour Christophe

- **Asymétrie confirmée** : ALPHA encaisse une baisse de régime sévère en Fenêtre B (1.7% de fills) par rapport à sa forme de la Fenêtre A (5.5%), pendant que BETA reste stable (11.4%).
- **PnL ALPHA** : +29.52 → -13.25 (le creux de régime s'accompagne d'une perte).
- **Portes verrouillées** : radar_block domine dans les deux fenêtres (785 → 957 skips ALPHA). Si la config est inchangée (non vérifiable ici), c'est le comportement du flux de prix par rapport aux seuils stricts d'ALPHA qui coince.
- **Prochaine étape** : vérifier la config réelle dans les logs T1_console des deux jours, puis relâcher éventuellement `RADAR_MIN_CONF_ALPHA` ou inspecter la volatilité spécifique du sous-jacent d'ALPHA.