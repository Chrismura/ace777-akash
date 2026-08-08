# Collab Gemini × Cursor — Vortex v2

> Implémenté le 2026-07-08 | Canonique **inchangé** (`config_active.env` Vortex OFF)

## Architecture (accord Gemini + Cursor)

```
supervisor v2 (60s)          genesis (64ms/cycle)
chop_score_v2 + klines  →  vortex_control.json  →  1× lecture  →  check_radar()
                              radar_min_*_beta/alpha
                              radar_max_spread_bps
```

## Fichiers ajoutés

| Fichier | Rôle |
|---------|------|
| `scripts/vortex_regime_compute.rb` | Macro chop_score_v2 → écrit JSON |
| `scripts/vortex_radar_read.rb` | 1 lecture/cycle → `cycle_radar_*` |
| `scripts/start_supervisor_v9_v2.sh` | Supervisor v2 (2e terminal) |
| `config_profiles/vortex_v2_collab.env` | Profil test |
| `launch_vortex_v2_collab_4h_binance.sh` | Lanceur testnet 4H A/B |
| `genesis_manifest.txt` | `VORTEX_V2_RADAR_PILOT` + `check_radar` dynamique |

## Test A/B testnet (2 terminaux)

**Référence (Vortex OFF)** — déjà validé C1 +17 :
```bash
./launch_vide_froid_4h_binance.sh --duration 04:00:00
```

**Vortex v2 ON** :
```bash
# Terminal 1
./launch_vortex_v2_collab_4h_binance.sh --duration 04:00:00

# Terminal 2 (obligatoire)
./scripts/start_supervisor_v9_v2.sh
```

Tag auto : `MASTER_VORTEX_V2_COLLAB_4H`

## Sim avant live (rejeu CSV)

```bash
ruby scripts/vortex_shadow_sim_v2.rb MASTER_HYBRID_VF_20260708 MASTER_BASE_V8_5_IMPACT_4H
```

Dernier rejeu (v2.1 min_mom TREND) :
- C1 : delta **-0.01** USDT (marginal)
- Hybrid : delta **-0.59** USDT (proxy négatif)

→ Testnet v2 = **expérimental** ; comparer PnL réel vs canonique sur même fenêtre horaire.

## JSON `vortex_control.json` (v2)

```json
{
  "mode": "TREND",
  "chop_score": 0.42,
  "radar_min_conf_beta": 0.22,
  "radar_min_conf_alpha": 0.20,
  "radar_min_mom_bps_beta": 0.004,
  "radar_min_mom_bps_alpha": 0.003,
  "radar_max_spread_bps": 14.0,
  "ts": "2026-07-08T20:00:00Z",
  "message": "v2_chop_0.42_trend"
}
```

## Garde-fous

- Bornes clamp : conf 0.15–0.45, mom 0.003–0.02, spread 4–16
- Vacuum legacy **désactivé** quand `VORTEX_V2_RADAR_PILOT=TRUE`
- `BUY_USDT_BETA=200` non modifié
- Preflight vérifie supervisor v2 si profil collab

## Rôle Gemini vs Cursor

| Gemini | Cursor |
|--------|--------|
| Vision macro, JSON, hystérésis | Implémentation ACE777, parse CSV réel |
| Profils TREND/CHOP | `radar_gate.rb` fidèle, asymétrie BETA/ALPHA |
| Plan pas à pas | Sim + feature-flag + lanceur |

Partager à Gemini : ce fichier + `runs/VORTEX_SHADOW_V2_DERNIER.md` + PnL hybrid `-5.07`.
