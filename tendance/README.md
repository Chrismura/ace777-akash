# Tendance - Setup Sentinelle & Inversion

Ce dossier isole les tests "tendance" pour eviter de melanger avec le micro-trading.

## Setup actif

- **BETA Sentinelle (LONG)**:
  - role: `SCOUT`
  - `MOMENTUM_THRESHOLD_BETA=0.85`
  - lit la "boite" et valide le contexte
- **ALPHA Inversion (SHORT)**:
  - role: `HUNTER`
  - `SHOCK_INVERSION_ALPHA=TRUE`
  - leverage fixe `13`
- **Radar**:
  - `VACUUM_TENSION_THRESHOLD_BETA=0.618`
  - `VACUUM_TENSION_THRESHOLD_ALPHA=0.618`
- **Trailing hunter**:
  - `DUO_HUNTER_AGGR_TRAIL_ARM_BPS=12`
  - `DUO_HUNTER_AGGR_TRAIL_GIVEBACK_BPS=9`
- **Shock**:
  - `SHOCK_EXIT_10_BPS=18.0`

## Superviseur V9 (option active)

Le binome lit `runs/vortex_control.json` en temps reel (a chaque cycle):
- si `mode=CHOP` -> radar monte vers `0.85` (protection)
- si `mode=TREND` -> radar revient vers `0.618` (aspiration)
- le superviseur peut aussi ajuster `mom`

Lancer le superviseur dans un 2e terminal:

```bash
cd /Users/christophe/ace777-test-day1
./tendance/supervisor_v9.sh
```

## Lancer

```bash
cd /Users/christophe/ace777-test-day1
./tendance/launch_tendance_sentinelle_inversion_8h.sh
```

## Notes

- Le launcher reset la session (`runs/duo_session.json`) a chaque run.
- Le preflight testnet reste obligatoire.
- Le preflight LLM (Ollama) est obligatoire quand `LLM_GATE_ENABLED=TRUE`.
