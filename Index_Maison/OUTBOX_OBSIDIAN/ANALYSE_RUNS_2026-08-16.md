# ANALYSE RUNS ACE777 — 13→16/08/2026 (pourquoi le bot a changé de comportement)

**Date :** 2026-08-16 · **Auteur :** Buffy · **Sources :** `engle/journal/*.md`, `runs/*.csv`,
`runs/MASTER_VORTEX_V2_COLLAB_4H_*`, `runs/RAPPORT_PNL_AUTO_*`, `runs/DIAG_ALPHA_*`,
`LE_VRAI_CHAMPION_CERTIFIE_37FCA367.txt`, chantiers `Index_Maison/CHANTIER_FIX_*`

---

## 1. Le constat

Le dernier run (15/08 21:53 → 16/08 06:03, terminé ce matin) est **beaucoup moins actif et
rentable** que les runs précédents : le HUNTER (ALPHA) ne fait presque plus rien.

## 2. Les chiffres (cycles avec mouvements = fills)

| Run (UTC) | BETA fills/PnL | ALPHA fills/PnL | Revenge ALPHA* | PnL total |
|---|---|---|---|---|
| 13/08 08:45–12:22 | 90 / +0.51 | 0 / 0 | 0 | +0.51 |
| 13/08 12:37–15:45 | 131 / −0.10 | 0 / 0 | 0 | −0.10 |
| 13/08 16:45–17:16 | 26 / +1.64 | 14 / +1.67 | 10 | +3.30 |
| 14/08 12:51–15:57 | 155 / +0.40 | **65 / +28.26** | **52** | **+28.65** |
| 14/08 21:45→15/08 05:44 | 205 / +2.51 | **56 / +8.61** | **51** | **+11.11** |
| 15/08 10:45–12:47 | 66 / +0.52 | 41 / −0.34 | 32 | +0.18 |
| 15/08 14:05–21:50 | 229 / +1.36 | 36 / +0.81 | 24 | +2.17 |
| **15/08 21:53→16/08 06:03 (DERNIER)** | 160 / +0.36 | **12 / −0.08** | **0** | **+0.28** |

\* Revenge ALPHA = fills avec `size_note=hunter_revenge_1.5x` (taille 1.5×, qty médiane
~0.124 BTC vs 0.032 pour `strong_conf`). C'est **lui** qui générait ~90% du PnL.

## 3. La cause racine

Le champion a été **re-scellé le 15/08 à 15:30** (`95d93d50`) avec le
« FIX-HEARTBEAT → TTL revenge » (chantier `CHANTIER_FIX_HEARTBEAT_TTL_2026-08-15.md`) :

- Le SCOUT (BETA) ne rafraîchit plus `ts_ms` dans `duo_state.json` après une perte close
  → le fichier vieillit → après `DUO_EVENT_TTL_SEC` (20s) → `stale_state` → le HUNTER ne peut
  plus revenge.
- Objectif du fix : borner le revenge (il était armé en permanence avant, %revenge 58→89%).
- **Effet de bord fatal** : en marché calme (COMPRESSÉ 78%, radar ALPHA bloque 72–81% des
  cycles : `momentum_too_small`, `wall_not_collapsed`, `direction_unclear`), le HUNTER ne
  trouve presque jamais de cycle où le radar passe dans une fenêtre de 20s → **0 revenge** sur
  45 pertes SCOUT du run de nuit (log : `duo no_trigger` 112 + `duo stale_state` 25, tensions 3–8).
- Le smoke test de validation du fix n'avait eu **aucun fill** (« marché calme ») → le
  désarmement n'a pas été vu en live avant la nuit.

**Ce n'est pas (seulement) le marché** : le run 15/08 05:44 était encore plus calme
(μ=0.21 vs 0.26, CLUSTER 5.7%) et faisait 51 revenge / +8.61.

**BETA (SCOUT) n'a pas changé** : 160–229 fills, mêmes exits (`shock_inversion_stop`
dominant), winrate ~30–38%.

**Facteur aggravant** : `STORM_HUNTER` (K2v2, anti no_trigger — entrée ALPHA sans perte
SCOUT) ne s'arme plus depuis le 13/08 08:41 (0 arm dans tous les rapports après).

## 4. Les 3 setups possibles (comparaison)

| Setup | PnL attendu | Volatilité | Risque | Comment basculer |
|---|---|---|---|---|
| **A. Rollback complet** (état avant le 15/08 15:30) | +2 à +28 (comme les bons runs) | forte : runs à −6 à −12 possibles (13/08 17:46 −6.56, 13/08 18:12 −12.50, 14/08 12:17 −8.63) | revenge armé en permanence = entrées tardives sur marché retourné | `cp genesis_manifest.txt.BAK_avant_fix_heartbeat_20260815-152847 LE_VRAI_CHAMPION_CERTIFIE_37FCA367.txt` + réfs md5 `fe2a7bcc` |
| **B. Fix 15/08 conservé, TTL 20→120s** | intermédiaire | moyenne | garde le `stale_state` parasite (heartbeat figé sur perte) | `export DUO_EVENT_TTL_SEC=120` au lancement (ou défaut dans le manifest) — AUCUNE modif code |
| **C. FIX-LAST-LOSS (appliqué le 16/08) ✅** : heartbeat toujours frais + TTL revenge 120s sur `last_loss_ts` | +2 à +11, sans les gros trous | modérée | faible — garde-fou TTL intact | **actif maintenant** : champion `8bce77b1` |

**Recommandation : C** (appliqué). Il restaure la fenêtre de revenge d'avant (~75% des pertes
gardent leur fenêtre complète, gaps médians ~67s < TTL 120s) tout en gardant la protection
anti-revenge-froid du fix du 15/08. Bonus possible plus tard : réactiver `STORM_HUNTER` K2v2
pour les marchés calmes (entrée sans perte SCOUT).

## 5. Fichiers touchés le 16/08 (traçabilité)

- `LE_VRAI_CHAMPION_CERTIFIE_37FCA367.txt` (le champion actif, symlink `genesis_manifest.txt`) — FIX-LAST-LOSS (5 blocs)
- Backup : `LE_VRAI_CHAMPION_CERTIFIE_37FCA367.txt.BAK_avant_fix_last_loss_ttl_20260816`
- `GO_VORTEX_V2.sh` + `scripts/preflight_ace777.sh` + `scripts/verif_pre_run_3x.sh` + `scripts/verif_setup_champion.sh` — réfs md5 `8bce77b1`
- Docs : `CHANTIER_FIX_LAST_LOSS_TTL_2026-08-16.md` (ce chantier), `ANALYSE_RUNS_2026-08-16.md` (ce fichier), INDEX_COMMANDES §11

## 6. Comment valider le fix (run de test)

```bash
cd ~/ace777-test-day1 && ./GO_VORTEX_V2.sh 02:00:00
```

Après le run :
```bash
# PnL + fills
cat runs/RAPPORT_PNL_AUTO_$(ls -t runs/RAPPORT_PNL_AUTO_*.md | head -1 | xargs basename | sed 's/RAPPORT_PNL_AUTO_//')
# %revenge : compter les size_note=hunter_revenge dans le CSV ALPHA
grep -c "hunter_revenge" runs/MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv
# nouvelle métrique revenge_ttl_expired
grep -c "revenge_ttl_expired" runs/MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv
# stale_state doit rester ~0
grep -c "stale_state" runs/MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv
```

Critères de réussite : **%revenge entre 30 et 60%**, `revenge_ttl_expired` présent mais minoritaire,
`stale_state` ≈ 0, PnL total > +1 USDT.

---
*Analyse générée par Buffy le 16/08/2026 — données brutes dans `engle/journal/` et `runs/`.*
