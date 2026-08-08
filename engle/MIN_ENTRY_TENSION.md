# Filtre entrée tension — moins de micros (frais)

**Date :** 2026-07-21  
**Scorecard :** axe #4 plus-value / frais live  
**Pourquoi :** ~45 trades/h à médiane ~0.6 bps ; frais round-trip ≈ 0.45–0.50 $ (~10 bps). Les micros sont **net négatifs** en live.

## Mécanisme (champion intact)

Usine : `VACUUM_TENSION_THRESHOLD_BETA=0.85` (déjà dans le launcher).  
Flag GO : `NUAGE_MIN_ENTRY_TENSION=2.5` → exporte `VACUUM_TENSION_THRESHOLD_BETA/ALPHA=2.5`.  
Le moteur skip déjà `cold < threshold` — **aucune modif genesis**.

## Simu (fills BETA 2026-07-20, frais 0.45 $/trade)

| Seuil tension | fills | ~/h | med bps | brut $ | frais≈ | net≈ |
|---|---:|---:|---:|---:|---:|---:|
| 0.85 (usine) | 604 | 35 | ~0 | +16 | 272 | **−256** |
| 2.0 | 368 | 21 | ~0 | +17 | 166 | −148 |
| **2.5** | **297** | **17** | ~0 | +16 | 134 | −118 |
| 5.0 | 122 | 7 | ~0.1 | +14 | 55 | −41 |

Les gros wins (≥10 bps) du jour : **22** fills / **+27 $** brut — dont **18** déjà à tension ≥2.5.

**Lecture honnête :** le filtre **coupe les frais** et garde presque tous les gros wins, mais la **médiane bps reste basse** (sortie 6–8 s). Étape suivante = hold STORM (K3), pas seulement le filtre.

## Commande test (après STOP + STERILE)

```bash
cd /Users/christophe/ace777-test-day1
NUAGE_MIN_ENTRY_TENSION=2.5 NUAGE_BIDIR_SIDES=1 NUAGE_DUO_PID_WATCHDOG=0 \
  caffeinate -dims ./GO_USINE_NUAGE.sh
```

Boot attendu : `MIN_ENTRY_TENSION: ON → VACUUM BETA/ALPHA=2.5`

Mesure 1–2 h :
- fills/heure (cible ≪ 45)
- médiane |bps|
- SKIP `cold < 2.5`
- PnL brut (frais = calcul à part)

## Ce que ce n’est PAS

- Pas un boost magique des bps sur chaque trade  
- Pas STORM hold (ça, c’est K3)  
- Pas une modif du md5 champion  
