# Audit Vortex — prêt pour ton retour

> Généré: `2026-07-08T19:20:00Z` | Live **non modifié** (simulation seulement)

---

## 1. Ce qui a été fait pendant ton absence

| Action | Fichier | Statut |
|--------|---------|--------|
| Sim Vortex v1 (vacuum) | `scripts/vortex_shadow_sim.rb` | ✅ Delta PnL **0** partout |
| Sim Vortex v2 (radar + hystérésis) | `scripts/vortex_shadow_sim_v2.rb` | ✅ |
| **chop_score_v2** (klines 1m + tension) | même script | ✅ **nouveau** |
| Cache klines | `runs/klines_cache/*.json` | ✅ |
| Rapport sim | `runs/VORTEX_SHADOW_V2_DERNIER.md` | ✅ |
| Patch genesis `cycle_radar_*` | `genesis_manifest.txt` | ❌ **pas fait** (volontaire) |

---

## 2. chop_score_v2 — formule macro

```
trend_chop   = 1 - min(|trend_bps_15m| / 25, 1)    # klines BTCUSDT 1m (15 min)
range_chop   = 1.0 si range < 10 bps, 0.5 si < 20
tension_chop = 1 - min(tension_ma_carnet / 1.0, 1)  # fenêtre 80 cycles CSV
vol_chop     = 0.8 si vol faible, 0.2 sinon

score = 0.30*trend + 0.25*range + 0.30*tension + 0.15*vol

Hystérésis: CHOP si score > 0.65 | TREND si score < 0.45
```

Relancer: `ruby scripts/vortex_shadow_sim_v2.rb`  
Ancien score: `CHOP_SCORE_VERSION=v1 ruby scripts/vortex_shadow_sim_v2.rb`

---

## 3. Résultats comparatifs

### chop_score v1 vs v2

| Cycle | v1 %TREND | v2 %TREND | v1 récup. | v2 récup. | v1 delta | v2 delta |
|-------|-----------|-----------|-----------|-----------|----------|----------|
| C1 `4H` | 7.5% | **45.1%** | 5 | **9** | 0.00 | -0.01 |
| Hybrid | **0%** | **27.6%** | 0 | **7** | 0.00 | **-0.59** |
| C2 | 0% | 21.7% | 0 | 10 | 0.00 | +2.52 |

### Lecture

- **chop_score_v2 fonctionne** : sort enfin du 100 % CHOP (hybrid 0 % → 27.6 % TREND).
- **Plus de lignes radar récupérées** (spread_too_wide surtout).
- **Delta PnL C1 quasi nul** (-0.01 USDT) — pas de preuve de gain.
- **Hybrid delta négatif** (-0.59) — proxy des trades récupérés = mauvais timing.
- **Moyenne +0.64** tirée par C2 (+2.52) — cycle interrompu, **ne pas sur-interpréter**.

### Verdict honnête

| Critère | Statut |
|---------|--------|
| Architecture Vortex v2 (radar) | ✅ Cohérente |
| Macro chop_score_v2 | ✅ Débloque TREND |
| Delta PnL C1 + Hybrid positif | ❌ **Non prouvé** |
| Prêt pour live | ❌ **NO-GO** |
| Prêt pour patch genesis (feature-flag OFF) | ⚠️ Discutable — tunings profils d'abord |

---

## 4. Cohérence système (checklist)

| Élément | État | Note |
|---------|------|------|
| `config_active.env` | Vortex OFF | Canonique inchangé |
| `VORTEX_CONTROL_ENABLED=FALSE` | ✅ | |
| `supervisor_v9.sh` | Ancien format JSON | Pas migré vers radar_min_* |
| `vortex_control.json` | Stale mars | Non utilisé |
| `genesis_manifest.txt` | Vortex → vacuum only | Pas radar |
| LLM gate fail-closed | ✅ | qwen 1.5b |
| `BUY_USDT_BETA=200` | ✅ | Non touché |
| Hybrid run | Terminé / arrêté | Pas de processus actifs au check 19:20Z |
| PnL session isolé | ✅ | `*_run_meta.json` |

---

## 5. Ce qui manque encore

### Avant testnet A/B

1. **Affiner profils TREND** — baisser `min_mom` (goulot = `momentum_too_small`, pas spread seul).
2. **Sim v2.1** — proxy PnL plus strict (même side + tension proche).
3. **Supervisor** — émettre JSON étendu (`radar_min_conf_beta`, etc.).
4. **Genesis** — `cycle_radar_*` une lecture/cycle + bornes clamp.
5. **Profil** `config_profiles/vortex_v2.env` + `VORTEX_CONTROL_ENABLED=FALSE` par défaut.

### Pas urgent

- Hermes / agent LLM Tier 2 (après macro rule-based stable).
- Wyckoff / IAT en gate (shadow rejetés).

---

## 6. Prochaines actions recommandées (à ton retour)

```
Option A — Tuning (recommandé)
  1. Sim avec profils TREND plus agressifs sur min_mom
  2. Rejouer C1 + Hybrid jusqu'à delta ≥ 0 sur les deux

Option B — Code (si tu veux avancer malgré delta ~0)
  1. Patch genesis cycle_radar_* derrière VORTEX_V2_ENABLED=FALSE
  2. Supervisor JSON étendu + hystérésis chop_score_v2
  3. Cycle testnet 4h A/B (OFF vs ON)

Option C — Ne rien déployer
  Si delta Hybrid reste négatif → revoir profils avant tout live
```

---

## 7. Fichiers à lire en priorité

1. `runs/VORTEX_SHADOW_V2_DERNIER.md` — résultats détaillés
2. `scripts/vortex_shadow_sim_v2.rb` — chop_score_v2 + sim radar
3. `runs/VORTEX_AUDIT_RETOUR_20260708.md` — ce document

---

## 8. Synthèse une ligne

**Le cerveau macro v2 est réparé (TREND accessible), le pipeline radar récupère des SKIP, mais le PnL proxy ne valide pas encore le déploiement — tuning profils TREND puis re-sim avant genesis.**
