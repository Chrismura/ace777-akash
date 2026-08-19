# 🗺️ SCHEMA ACE777 — référence rapide (mise à jour 16/08/2026)

> **But** : comprendre ACE777 en 2 minutes, sans relire tous les docs. À tenir à jour à chaque chantier.
> Jumeau de `hulk-mexc/SCHEMA_HULK.md` (même format).

## 1. En une phrase

**ACE777 = duo scalper BTC/USDT sur Binance TESTNET** (futures) : **BETA = SCOUT** (ouvre les
positions, 200 USDT) + **ALPHA = HUNTER** (amplifie après une perte scout, 800 USDT, le « revenge »).
Racine : `~/ace777-test-day1/`. Deux lanceurs : **GO_VORTEX_V2.sh** (profil radar pilot, test) et
**GO_USINE_NUAGE.sh** (usine). HULK est séparé (paper MEXC).

## 2. Les 2 rôles (le duo — LA clé de lecture)

| | BETA — SCOUT | ALPHA — HUNTER |
|---|---|---|
| Rôle | ouvre, teste le marché | amplifie x13 après perte scout |
| Masse | 200 USDT | 800 USDT (revenge ×1.5) |
| Radar | conf ≥ 0.30, mom ≥ 0.01 | conf ≥ 0.25, mom ≥ 0.008 (plus permissif) |
| Sortie | stop −16 bps, shock, fluid, inversion | suit le scout, sort sur signaux du duo |

**Le « revenge » (fixé le 16/08)** : quand le SCOUT ferme une **perte** (stop/shock/fluid/inversion),
le HUNTER ré-entre à ~1.5× pour récupérer, **dans les 120s** (`DUO_REVENGE_TTL_SEC`) après la perte
(`last_loss_ts` dans duo_state). Avant le fix : 0 revenge (fix du 15/08 trop strict) → PnL +0.28 au
lieu de +2 à +28. **Cible : %revenge ALPHA 30–60%.**

## 3. Le champion (le fichier sacré)

```
LE_VRAI_CHAMPION_CERTIFIE_37FCA367.txt   ← le code moteur (bash + ruby)
  └─ symlink : genesis_manifest.txt
md5 actuel : 8bce77b17a3c2f8f40a0b6b92ce0b4bc (préfixe 8bce77b1)
```

**Règle d'or** : on ne le modifie JAMAIS sans protocole complet :
`spec → consultation famille (4 modèles) → verdict → implémentation → tests (bash -n + ruby)
→ re-scellage (md5) → mise à jour des RÉFS md5 → note d'autorisation (A_Mon_Attention) → chantier`.

**Les réfs md5 à mettre à jour à CHAQUE re-scellage** (grep `8bce77b1` → remplacer) :
`GO_VORTEX_V2.sh` · `GO_USINE_NUAGE.sh` · `scripts/preflight_ace777.sh` · `scripts/verif_pre_run_3x.sh`
· `scripts/verif_setup_champion.sh` · `Index_Maison/scripts/checkup_garage.sh`
· `Index_Maison/scripts/cortana_cockpit_bridge.py` · `Index_Maison/scripts/pulse_sous_loeil.sh`
· `Index_Maison/scripts/superviseur_core.sh` · `Index_Maison/strategie/REGISTRE_SYNAPSES.json`
(veilleuse ! sinon elle sonne « INTRUSION »).

**Backups** (rollback) : `LE_VRAI_CHAMPION_CERTIFIE_37FCA367.txt.BAK_avant_*` (les 2 derniers :
fix_last_loss_ttl_20260816 = `3d760592…`, fix_price_stasis_20260816 = `3d760592…`).

## 4. Les 2 fixes du 16/08 (dans le champion actuel)

| Fix | Quoi | Paramètres | Raison CSV visible |
|---|---|---|---|
| **FIX-LAST-LOSS** | TTL revenge sur `last_loss_ts` (au lieu de figer ts_ms) → fenêtre 120s, heartbeat toujours frais | `DUO_REVENGE_TTL_SEC=120` | `revenge_ttl_expired`, `stale_state` ≈ 0 |
| **FIX-PRICE-STASIS** | pas d'entrée si prix figé (< 0.5 bps / 30s) — tue les fills à pnl 0.00000000 | `PRICE_STASIS_GUARD=TRUE`, `MIN_MOVE_BPS=0.5`, `WINDOW_SEC=30`, `TENSION_BYPASS=15` | `price_stasis`, `price_frozen` |

## 5. Config (source unique : `config_active.env`)

| Param | Valeur | Sens |
|---|---|---|
| `BUY_USDT_BETA` / `BUY_USDT_ALPHA` | 200 / 800 | masse duo (NE PAS toucher sans ordre) |
| `MOMENTUM_THRESHOLD` / `WALL_DROP_THRESHOLD` | 0.96 / 0.065 | radar |
| `GLOBAL_STOP_USDT` | −45 | stop global session |
| `STOP_LOSS_BPS` | 16 | stop scout |
| `LEVERAGE` | 5 | BETA x5, ALPHA x13 fixe |
| `POLL_SEC` | 0.064 | 64 ms (M1 latence) |
| `LLM_GATE_ENABLED` | TRUE (fail-closed) | gate LLM (qwen2.5-coder via ollama 11439) |
| `ENTRY_25_75_ENABLED` | TRUE | entrée 25% puis 75% après confirmation |
| `DUO_HUNTER_REQUIRE_STOP_LOSS` | FALSE | le revenge ne demande pas un stop formel |
| `RADAR_MIN_CONF_*` / `RADAR_MIN_MOM_BPS_*` | voir §2 | seuils radar BETA/ALPHA |

## 6. Le duo (mécanique interne)

```
duo_state.json (runs/) : {role: SCOUT|HUNTER, status, side, bps, pnl_usdt, reason,
                         cycle, hold_sec, ts_ms, last_loss_ts}
flux : SCOUT ferme une perte → duo_publish_state(CLOSED, pnl<0) écrit last_loss_ts
       → heartbeat (duo_touch_heartbeat_force) rafraîchit ts_ms TOUJOURS (fix 16/08)
       → HUNTER décide à chaque cycle : age(last_loss_ts) ≤ 120s → revenge OK
       → sinon reason=revenge_ttl_expired
```

## 7. Lancer / arrêter

```bash
cd ~/ace777-test-day1
# Test rapide (2h) / standard (4h)
./GO_VORTEX_V2.sh 02:00:00        # profil radar pilot (A/B vs usine)
# Arrêt propre
./stop_ace777_hard.sh             # pose STOP/STOP_ALPHA/STOP_BETA + rapport PnL + clean
# ⚠️ STOP files bloquent le champion (l.1552) : les retirer AVANT de relancer
rm -f STOP STOP_ALPHA STOP_BETA
# Preflight avant run
bash scripts/verif_setup_champion.sh
```

## 8. Lire les résultats

- **Rapport** : `runs/RAPPORT_PNL_DERNIER.md` (le plus récent `RAPPORT_PNL_AUTO_*.md`)
- **Journaux** : `engle/journal/ENGLE_JOURNAL_DERNIER.md` + CSV : `runs/MASTER_VORTEX_V2_COLLAB_4H_*.csv`
- **Fills** : lignes `FILLED` des CSV — raisons utiles : `hunter_revenge_1.5x` (le PnL), `strong_conf`,
  `entry_25_75_trap*` (petites tailles), skips : `price_stasis`, `revenge_ttl_expired`, `radar_block`
- **DIAG** : `runs/DIAG_ALPHA_*.md` (duo_wait / no_trigger / stale_state)
- **État** : `runs/STATE.md` · `runs/duo_state.json` (fichier de vérité du duo)

## 9. État au 16/08 (historique des fixes)

| Date | Chantier | md5 |
|---|---|---|
| 15/08 15:30 | FIX-HEARTBEAT (TTL 20s opérant) — ⚠️ a éteint le revenge (0 revenge, +0.28) | `95d93d50` |
| 16/08 09:13 | **FIX-LAST-LOSS** : TTL revenge 120s sur last_loss_ts — SUPERSEDE le 15/08 | `3d760592` |
| 16/08 09:56 | **FIX-PRICE-STASIS** : garde-fou prix figé 0.5bps/30s (8/10 fills flat → 0) | `8bce77b1` ✅ |

En cours : run de test GO_VORTEX_V2 02:00:00 **ACTIF** (PID 27655, relancé par Christophe après
le re-scellage price_stasis) → teste les 2 fixes (last_loss + price_stasis). Vérifier le rapport
à la fin : critères §10.

## 10. Commandes de test datées (INDEX_COMMANDES §11)

```bash
cd ~/ace777-test-day1 && ./GO_VORTEX_V2.sh 02:00:00
# Critères : %revenge 30–60% · revenge_ttl_expired présent · stale_state ≈ 0
# · price_stasis skips > 0 (marché calme) · fills flat < 20% · PnL > +1
```

## 11. Protocole famille (pour tout chantier)

1. Écrire la SPEC (`SPEC_FIX_*.md`) 2. Consulter la famille : `Index_Maison/scripts/consulter_famille_*.py`
(4 modèles : gemini, nvidia, deepseek, codestral — openrouter-juge/ultra souvent HS 502)
3. Verdict (`VERDICT_FAMILLE.md`) 4. Implémenter (ou envoyer au codeur : `envoyer_spec_codeur_*.py`)
5. Tester (`bash -n`, `ruby -c`, tests fonctionnels) 6. Re-sceller + réfs (§3) 7. Autorisation
`A_Mon_Attention/` + chantier + INDEX_COMMANDES (3 copies : workspace + OUTBOX + Obsidian).

## 12. Prochaines améliorations en attente (backlog)

- Réactiver STORM_HUNTER K2v2 (anti no_trigger, 0 arm depuis le 13/08) pour compenser les marchés calmes
- Ajuster DUO_REVENGE_TTL_SEC (120s) selon les résultats du run de test
- L'alternative nvidia (flag last_loss_ts) déjà implémentée = le FIX-LAST-LOSS actuel
