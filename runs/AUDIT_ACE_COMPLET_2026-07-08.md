# AUDIT ACE COMPLET — 2026-07-08

> Audit poussé : Explore + Security Review + synthèse manuelle  
> Périmètre : `ace777-test-day1` + bridge `crypto-voice-assistant-core`  
> Bugbot : indisponible (connexion interrompue) — complété manuellement sur ops layer

---

## Verdict exécutif

| Dimension | Score | Commentaire |
|-----------|-------|-------------|
| **Desk testnet reproductible** | **~70 %** | Cycle #1 validé (+17 USDT, ALPHA 57 trades) |
| **Desk pro intégré (vocal + shadow + promo)** | **~40 %** | Cortana partiel, pas de SKILL/hooks, IAT/Wyckoff shadow only |
| **Sécurité opérationnelle** | **Moyen+** | Fail-closed OK, 2 P1 sécu à corriger avant live |
| **Complétude instruments** | **Partielle** | BTC testnet solide ; live préparé ; Vortex/tendance morts |

**Décision :** setup **GO testnet** sur `vide_froid_binance` · **NO-GO live mainnet** tant que P1 sécu non corrigés · **NO-GO promo plus_value** avant 2ᵉ cycle propre.

---

## 1. Inventaire & matrice (Explore)

### Cœur actif ✅

- `genesis_manifest.txt` — radar, duo, LLM gate, V8 tension/résonance
- `config_active.env` — source unique `vide_froid_binance`
- `launch_vide_froid_4h_binance.sh` → `v8_6_fortress` → `v8_5_impact`
- Scripts ops : preflight, watchdog, STATE, PnL, DIAG, post-run
- Bridge Cortana : `ace777.rs`, `detect.rs`, `iat.rs`, `quantum/malanga`

### Lanceurs (18)

| Type | Fichiers |
|------|----------|
| **Canoniques** | `launch_vide_froid_4h/8h_binance.sh`, `launch_vide_froid_hybrid_4h_binance.sh` |
| **Live** | `launch_vide_froid_hybrid_4h_live.sh` (nécessite `~/.binance_live.env`) |
| **Legacy** | `launch_vide_froid_8h_alpha_plus14*`, `launch_250_4h.sh`, tendance… |

### Masters archivés

| Dossier | Meilleur PnL connu | Verdict |
|---------|-------------------|---------|
| `master_plus_value` | +17.62 USDT (BETA seul, mars) | Archive référence |
| `config_active` (C1 08/07) | **+17.11** (BETA+ALPHA) | **Meilleur duo** |
| `master_qwen_*` | -24 USDT | ❌ Abandonner |
| `tendance/` | -23 USDT | ❌ Orphelin |

### Mort / orphelin ☠️

| Composant | Statut |
|-----------|--------|
| Vortex + `vortex_control.json` | OFF canonique, JSON stale `invalid_v9_json` |
| `conseil_phase_ace777.py` | REPL standalone, non branché |
| `tendance/supervisor_v9.sh` | Réparé mais inutilisé |
| Docker / Akash deploy | Supprimé du working tree |
| `master_base/tools/` | Absent (promis par README) |

### Matrice instruments

| Instrument | État |
|------------|------|
| Testnet Futures | ✅ Présent |
| Live mainnet | ⚠️ Partiel (lanceur sans run validé) |
| Duo SCOUT/HUNTER | ✅ Fixes P0–P2 appliqués |
| LLM gate fail-closed | ✅ (grep bash, pas JSON #6) |
| IAT Malanga | ⚠️ Cortana live + shadow replay ; pas dans ACE777 |
| Wyckoff | ⚠️ Shadow seulement (rejeté en gate — delta -15 USDT sur C1) |
| Watchdog réseau | ✅ 120s |
| Caffeinate | ✅ Lanceurs 4H |
| PnL session isolé | ✅ `*_run_meta.json` |
| Cortana vocal ACE777 | ✅ Lecture ; stop = conseil manuel |
| Tests auto ACE777 | ❌ Quasi absents |
| Cursor SKILL / hooks | ❌ Plan #7 #8 non fait |

---

## 2. Sécurité (Security Review)

### P0 — Aucun critique validé

- Clés via env / `~/.binance_*.env` — pas dans logs CSV
- Mainnet exige `BINANCE_ALLOW_MAINNET=TRUE` + `fapi.binance.com`
- LLM fail-closed par défaut

### P1 — À corriger avant live

| # | Risque | Fichier | Action |
|---|--------|---------|--------|
| S1 | `BASE_URL` validé par sous-chaîne → exfil clés possible | `genesis_manifest.txt` | Allowlist hôte stricte |
| S2 | LLM gate `grep trade\|yes\|go\|ok` trop permissif | `genesis_manifest.txt` | JSON structuré TRADE/SKIP only |
| S3 | Live mainnet : friction faible | `launch_*_live.sh` | `I_UNDERSTAND_LIVE_MAINNET=YES` obligatoire |

### P2

| # | Risque | Action |
|---|--------|--------|
| S4 | `stop_ace777.sh` pkill trop large | Limiter aux PID `runs/*.pid` |
| S5 | `vortex_control.json` non signé | Permissions 600 + schéma |
| S6 | Divergence VALIDATION vs genesis live | Documenter ou aligner |

---

## 3. Bugs & ops (synthèse manuelle — Bugbot KO)

| # | Sév. | Problème | Statut |
|---|------|----------|--------|
| B1 | P0 | Timer 3h30 non déclenché (batterie) → run 6h+ | Mitigé : caffeinate + watchdog |
| B2 | P0 | Processus zombies après coupure | `./stop_ace777.sh` (pkill large) |
| B3 | P1 | STATE `RUNNING` + phase `ended` | ✅ Corrigé (priorité phase) |
| B4 | P1 | PnL pollué multi-sessions CSV | ✅ Meta session + archive |
| B5 | P1 | DIAG_ALPHA wording faux si `REQUIRE_STOP_LOSS=FALSE` | ✅ Corrigé |
| B6 | P1 | `--duration` cassait `load_config` | ✅ Corrigé lanceur 4H |
| B7 | P2 | `RUN_STATE` checkpoint ALPHA reprend tier x13 ancien | À vérifier en nouveau tag |
| B8 | P2 | Logs colorés absents si `tail -f` CSV | `tail_csv_color.sh` ajouté |

---

## 4. Simulations shadow (données runs)

| Indicateur | Cycle C1 | Verdict intégration live |
|------------|----------|--------------------------|
| **Wyckoff** (IAT≥80) | -15.86 USDT vs réel | ❌ Ne pas intégrer en gate |
| **IAT Malanga** (≥80) | 0 filtré (max ~49) | ⚠️ Advisory Cortana seulement |
| **Hybrid en cours** | 5+ trades, ~+3 USDT | 🔄 Fin ~22h25 Paris |

---

## 5. Top 10 oublis pour « ACE complet »

1. **2 cycles propres** par setup avant promo `master_plus_value`
2. **`llm_gate_verify.py`** JSON (#6 plan) — P1 sécu + fiabilité
3. **Allowlist BASE_URL** stricte — P1 sécu live
4. **Cursor SKILL + hooks** pre/post-run (#7 #8)
5. **IAT bridge** : alerte vocale OK, pas de gate ACE777 (validé par sim)
6. **Wyckoff** : shadow only, rejeté pour gate
7. **Nettoyage Vortex** : supprimer résidus ou documenter OFF
8. **`conseil_phase`** → advisory read-only (#10)
9. **`master_base/tools/`** : scripts promo/diff config
10. **Tests** : radar, duo, vault, E2E un cycle

---

## 6. Roadmap priorisée

### P0 — Cette semaine

- [ ] Fin cycle hybrid → analyse `RAPPORT_PNL` + comparaison vs canonique
- [ ] `./stop_ace777.sh` après chaque run (Mac branché)
- [ ] 1 cycle canonique 4H reproductif (confirmer C1)
- [ ] Corriger S1 + S2 **avant** tout test `launch_*_live.sh`

### P1 — Semaines 2–3

- [ ] `llm_gate_verify.py` + fail-closed JSON
- [ ] `.cursor/skills/ace777-trading/SKILL.md` + hooks
- [ ] `stop_ace777.sh` ciblé (S4)
- [ ] A/B hybrid vs canonique (2 cycles complets)
- [ ] Mettre à jour `EXPORT_SETUP_IA.md` (bridge ACE777)
- [ ] `master_base/tools/` minimal

### P2 — Mois 2–3

- [ ] Cortana : métriques latence, journal ordres, stop vocal sécurisé
- [ ] Modules testables genesis (radar, duo)
- [ ] Promo `vide_froid_binance` → `master_plus_value` si 2 cycles OK
- [ ] Abandon formel : tendance, qwen seul, conseil_phase orphelin

---

## 7. Agents utilisés

| Agent | Résultat |
|-------|----------|
| **Explore** | ✅ Inventaire exhaustif |
| **Security Review** | ✅ 3 P1, 3 P2 |
| **Bugbot** | ❌ Échec connexion (×2) — complété manuellement |

---

## 8. Fichiers de référence

- `runs/AUDIT_2026-07-08.md` — cycles 08/07
- `PLAN_AMELIORATIONS_PRO.md` — plan phases 1–4
- `runs/IAT_SHADOW_DERNIER.md` — sim IAT
- `runs/WYCKOFF_SHADOW_DERNIER.md` — sim Wyckoff
- `RUN_INDEX.md` — historique runs

---

*Généré : 2026-07-08 · Prochaine revue : après fin cycle `MASTER_HYBRID_VF_20260708`*
