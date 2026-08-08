# Garde-fou duo PID (BETA + ALPHA) — couche réversible

**Date :** 2026-07-19  
**Pourquoi :** l’usine NUAGE ne relançait que ALPHA (heartbeat). BETA mort → duo cassé, ALPHA en `stale_state`. Un garde-fou similaire existait sur d’autres setups (v8.5 / GEMINI), pas porté sur `GO_USINE`.

## Comportement

- Toutes les ~15 s : `kill -0` sur `runs/beta_wrapper.pid` et `runs/alpha_wrapper.pid`
- Si mort et pas de `STOP_*` : `launch_beta` / `launch_alpha` (fonctions usine)
- Max relances séparées BETA/ALPHA (défaut 8) puis STOP session
- Grace ~45 s après chaque relance
- Log : `runs/DUO_PID_WATCHDOG.log`

## Activation (via GO_USINE)

| Env | Effet |
|-----|--------|
| `NUAGE_DUO_PID_WATCHDOG=1` | **défaut** — garde-fou ON |
| `NUAGE_DUO_PID_WATCHDOG=0` | OFF — usine pure (rétroactif) |

```bash
# normal (duo ON)
./GO_USINE_NUAGE.sh

# désactiver
NUAGE_DUO_PID_WATCHDOG=0 ./GO_USINE_NUAGE.sh
```

**Ne touche pas** `genesis_manifest.txt` / snapshot usine byte (patch runtime comme wait-timer).
