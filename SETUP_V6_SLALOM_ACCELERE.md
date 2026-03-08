# SETUP V6 - SLALOM ACCELERE

Statut: prochain test valide (a lancer apres integration logique V6 dans le moteur).

## Base Duo

- BETA (Scout): x5, LONG force
- ALPHA (Hunter): x8, SHORT force opposee
- Duo TTL: 20s
- Global stop session: -5.00 USDT

## Regles V6

### 1) Sensitivity Boost (INDISPENSABLE)

Si le Scout sort en perte rapide ("fast death"), le Hunter devient plus sensible pendant une courte fenetre:

- Active: TRUE
- Fast death threshold: hold <= 30s
- Boost Hunter momentum threshold: x0.5 (divise par 2)
- Boost TTL: 40s

### 2) Stase Exit Trigger (EMA Stase)

Sortie du mode attente si le prix s'ecarte de la zone de stase du Scout:

- Active: TRUE
- Stase EMA window: 30s
- Break threshold: 3 bps

### 3) Vortex Acceleration (Burst x13)

Le burst x13 n'est autorise que sous conditions strictes:

- Active: TRUE
- Condition perte Scout: <= -15 bps
- Condition vitesse chute: >= 0.5 bps/s
- Cooldown burst: 188s (3.14 min)
- Limite: 1 coup de marteau par cooldown

## Parametres de test proposes

- TEST_TAG: TEST_DUO_V6_SLALOM_6H
- RUN_SEC: 21600
- Scout:
  - LEVERAGE=5
  - BUY_USDT=250
  - MOMENTUM_THRESHOLD=0.45
  - STOP_LOSS_BPS=12
- Hunter:
  - LEVERAGE=8
  - BUY_USDT=250
  - MOMENTUM_THRESHOLD=0.65 (base avant boost)
  - STOP_LOSS_BPS=8
  - DUO_HUNTER_STOP_LOSS_BPS=9
  - DUO_SCOUT_SUFFER_BPS=-11
  - DUO_SCOUT_SUFFER_USDT=-0.80
  - DUO_HUNTER_REQUIRE_STOP_LOSS=TRUE
  - DUO_FORCE_OPPOSITE=TRUE
  - DUO_MOMENTUM_HANDOVER=TRUE
  - RADAR_GATE=FALSE
  - TREND_FILTER=FALSE

## Flags V6 a exposer dans le moteur

Ces variables doivent etre prises en charge par le script principal pour que V6 soit effectif:

- DUO_V6_SENSITIVITY_BOOST=TRUE
- DUO_V6_FAST_DEATH_SEC=30
- DUO_V6_BOOST_MULT=0.5
- DUO_V6_BOOST_TTL_SEC=40
- DUO_V6_STASE_EXIT=TRUE
- DUO_V6_STASE_EMA_SEC=30
- DUO_V6_STASE_BREAK_BPS=3
- DUO_V6_BURST_X13=TRUE
- DUO_V6_BURST_MIN_LOSS_BPS=15
- DUO_V6_BURST_MIN_SPEED_BPS_PER_SEC=0.5
- DUO_V6_BURST_COOLDOWN_SEC=188

