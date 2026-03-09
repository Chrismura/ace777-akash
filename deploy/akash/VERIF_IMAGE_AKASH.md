# Vérification Image ↔ Akash YAML

## 1. Image Docker

| Élément | Statut |
|--------|--------|
| `ghcr.io/chrismura/ace777-akash:latest` | ✓ |
| `COPY . /app` → tout le repo | ✓ |
| `entrypoint.sh` → crée `~/.binance_testnet.env` | ✓ |
| Chaîne: entrypoint → fortress → v8_5_impact → duo_harmonic → ACE777_STRICT_CLONE_FUTURES_V2 | ✓ |
| RUN_DURATION 04:00:00 → 14400 sec (4h) | ✓ (corrigé) |

## 2. Variables requises (entrypoint)

| Variable | akash.yml | Obligatoire |
|----------|-----------|-------------|
| BINANCE_API_KEY | à ajouter par toi | **OUI** |
| BINANCE_API_SECRET | à ajouter par toi | **OUI** |

## 3. Variables optionnelles (entrypoint + scripts)

| Variable | akash.yml | Valeur |
|----------|-----------|--------|
| RUN_DURATION | 04:00:00 | ✓ |
| LAUNCH_SCRIPT | ./launch_test_master_base_v8_6_fortress.sh | ✓ |
| MOMENTUM_THRESHOLD | 0.95 | ✓ |
| WALL_DROP_THRESHOLD | 0.060 | ✓ |
| BUY_USDT_BETA | 150 | ✓ |
| BUY_USDT_ALPHA | 750 | ✓ |
| GLOBAL_STOP_USDT | -32.00 | ✓ |
| FLUID_EXIT_SENSITIVITY | 1.0 | ✓ |
| DYNAMIC_HOLD | TRUE | ✓ |
| BINANCE_BASE_URL_OVERRIDE | https://testnet.binancefuture.com | ✓ |

## 4. Flux des valeurs

1. **entrypoint** lit BINANCE_API_KEY/SECRET → écrit `~/.binance_testnet.env`
2. **duo_harmonic** charge les clés depuis `$HOME/.binance_testnet.env`
3. **fortress** reçoit `--duration 04:00:00` → `RUN_SEC_OVERRIDE=14400`
4. **v8_5_impact** garde `RUN_SEC_OVERRIDE` (ne l’écrase plus)
5. **duo_harmonic** utilise `RUN_SEC=14400` → run 4h

## 5. Résumé

Tout est aligné. Le YAML à envoyer est `deploy/akash/akash.yml` — ajoute BINANCE_API_KEY et BINANCE_API_SECRET avant déploiement.
