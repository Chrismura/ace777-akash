# Tests V6 Hashrate

Ce dossier contient la bascule de test V6 "Slalom Accelere" + module Hashrate BTC.

## Fichier principal

- `launch_test_duo_v6_hashrate_6h.sh`

## Objectif

- Reprendre la base 5/8/13
- Ajouter les modules V6:
  - Sensitivity Boost
  - Stase Exit (EMA)
  - Burst x13 sous cooldown 3.14 min
- Ajouter le module Hashrate BTC (gate + modulation du seuil momentum)

## Lancement

```bash
cd /app
./tests_v6_hashrate/launch_test_duo_v6_hashrate_6h.sh
```

