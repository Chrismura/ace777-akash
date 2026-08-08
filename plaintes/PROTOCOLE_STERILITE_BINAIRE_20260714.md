# PROTOCOLE STÉRILITÉ BINAIRE — ACE777 / NUAGE

**Date:** 2026-07-14  
**Statut:** OBLIGATOIRE — aucun run sans PASS  
**Responsable exécution:** Christophe lance. Agent vérifie. Personne ne valide sans `STERILE=OK`.

---

## RÈGLE ZERO

```
SI verif_sterilite.sh ≠ exit 0  →  PAS DE RUN. POINT.
SI "mission terminée" SANS verif post-run  →  RUN NON CERTIFIABLE.
SI pgrep montre ≥1 process  →  DONNÉES POUBELLE.
```

Aucune exception. Aucun smoke « on verra après ». Aucun prod 4h sans smoke 15m certifié la veille du même protocole.

---

## PHASE 0 — PURGE (avant tout run)

```bash
cd /Users/christophe/ace777-test-day1
./stop_ace777_hard.sh
pkill -9 -f 'ace777_launch_v85_nuage' 2>/dev/null
pkill -9 -f 'launch_vide_froid_4h_binance_NUAGE' 2>/dev/null
pkill -9 -f 'NUAGE_PROD' 2>/dev/null
pkill -9 -f 'tail -n 0 -F runs/\.NUAGE' 2>/dev/null
pkill -9 -f 'tail -F runs/\.NUAGE' 2>/dev/null
rm -f runs/master.pid runs/*wrapper*.pid runs/*genesis*.pid
rm -f /tmp/alpha_heartbeat.txt
rm -rf /tmp/ace777_ram_exchange && mkdir -p /tmp/ace777_ram_exchange
touch STOP STOP_ALPHA STOP_BETA
chmod +x scripts/verif_sterilite.sh
./scripts/verif_sterilite.sh --pre-run
```

**PASS obligatoire:** dernière ligne = `STERILE=OK` et exit code 0.

**ÉCHEC connu:** `stop_ace777_hard.sh` ne voit PAS les process NUAGE (`ace777_launch_v85_nuage`, `tail -F runs/.NUAGE`). Ne jamais lui faire confiance seul.

---

## PHASE 1 — PRE-FLIGHT (1 minute)

| # | Check | Commande | PASS |
|---|-------|----------|------|
| 1 | Stérilité | `./scripts/verif_sterilite.sh --pre-run` | exit 0 |
| 2 | Champion intact | `md5 genesis_manifest.txt` = `37fca367` | match |
| 3 | Pas de STOP oublié d'un run mort | `ls STOP*` existe | oui |
| 4 | Tag run unique | `export TEST_TAG_OVERRIDE="NUAGE_..."` | jamais réutiliser un tag prod pollué |
| 5 | Durée explicite | `export RUN_DURATION="04:00:00"` | echo affiché au boot |

**Agent:** refuse de dire « prêt » sans avoir exécuté verif_sterilite et montré le résultat.

---

## PHASE 2 — SMOKE OBLIGATOIRE (15 min) avant tout PROD

```bash
cd /Users/christophe/ace777-test-day1
unset ALPHA_RAMP_MODE
export RUN_DURATION="00:15:00"
export TEST_TAG_OVERRIDE="NUAGE_SMOKE_$(date -u +%H%M)Z"
/tmp/launch_vide_froid_4h_binance_NUAGE.sh --duration 00:15:00
```

**Critères PASS smoke (tous requis):**

| Critère | Seuil |
|---------|-------|
| `./scripts/verif_sterilite.sh` post-run | exit 0 en ≤30s après fin |
| BETA cycles | > 50 |
| ALPHA cycles | > 30 |
| ALPHA heartbeat | `/tmp/alpha_heartbeat.txt` modifié < 60s pendant run |
| BARRIER / -2028 | 0 |
| Relances watchdog | ≤ 1 (idéal 0) |
| Doublons `tail -F` sur même raw | 0 (1 seul max par oiseau) |
| Fin run | BETA ET ALPHA arrêtés ensemble, pas de lignes après prompt |

**SI smoke FAIL → pas de PROD. Purge Phase 0. Recommencer.**

---

## PHASE 3 — PROD (seulement si smoke PASS)

```bash
cd /Users/christophe/ace777-test-day1
./scripts/verif_sterilite.sh --pre-run   # RE-vérif obligatoire
unset ALPHA_RAMP_MODE
export RUN_DURATION="04:00:00"
export TEST_TAG_OVERRIDE="NUAGE_PROD_4H_$(date -u +%Y%m%d_%H%M)Z"
/tmp/launch_vide_froid_4h_binance_NUAGE.sh --duration 04:00:00
```

**Pendant le run (toutes les 30 min — Christophe ou agent si demandé):**

```bash
./scripts/verif_sterilite.sh
pgrep -fc 'tail -n 0 -F runs/\.NUAGE'   # doit être ≤ 2 (1 BETA + 1 ALPHA)
pgrep -fc 'bash -s'                      # doit être ≤ 2
cat /tmp/alpha_heartbeat.txt && date -u
```

**ALERTE IMMÉDIATE si:**
- `tail -F` > 2 → relance watchdog sale, run **INVALIDE**
- `bash -s` > 2 → orphelins, run **INVALIDE**
- BETA cycles >> ALPHA cycles × 5 pendant >10 min sans trade ALPHA → noter, pas certifier revenge

---

## PHASE 4 — FIN DE RUN (ne jamais faire confiance au message)

Quand tu vois `NUAGE_V2.1 mission terminée` :

```bash
# IMMÉDIAT — dans les 10 secondes
./scripts/verif_sterilite.sh
```

| Résultat | Action |
|----------|--------|
| `STERILE=OK` | Run potentiellement certifiable → Phase 5 |
| `STERILE=NOK` | **Purge Phase 0** → run **GASPILLLÉ** → données **NON EXPLOITABLES** |

Puis purge complète même si OK :

```bash
./stop_ace777_hard.sh
pkill -9 -f 'ace777_launch_v85_nuage|NUAGE_PROD|tail -F runs/\.NUAGE'
./scripts/verif_sterilite.sh
```

---

## PHASE 5 — CERTIFICATION DONNÉES (avant toute analyse)

Un run est **exploitable** seulement si **TOUS** :

1. `verif_sterilite.sh` = OK à T+0, T+fin, T+30s post-fin
2. Durée réelle ≥ 95% durée demandée (vérifier `*_run_meta.json` planned_end vs last log line)
3. BETA et ALPHA CSV même tag, timestamps continus
4. 0 process orphelin post-purge
5. Rapport écrit : `runs/CERTIF_<TAG>.md` avec :
   - start/end UTC
   - cycles BETA / ALPHA
   - nb relances watchdog
   - PnL BETA + ALPHA
   - verdict PASS/FAIL

**Sans CERTIF → interdiction d'analyser PnL ou bugs algo.**

---

## RÈGLES AGENT (Cursor) — NON NÉGOCIABLES

1. **Ne jamais lancer un run** sans demande explicite de Christophe.
2. **Toujours exécuter** `verif_sterilite.sh` avant de dire « environnement propre ».
3. **Ne jamais croire** `CLEANUP_OK: 0 process` sans `pgrep` indépendant.
4. **Ne jamais certifier** un run si des lignes continuent après le prompt shell.
5. **Ne jamais analyser** PnL d'un run sans CERTIF Phase 5.
6. **Signaler immédiatement** si `tail -F` > 2 ou `bash -s` > 2 pendant run.
7. **Prochain patch code** (V2.2, hors run) : kill tree incluant `tail -F`, `ace777_launch_v85_nuage`, tracking PGID — pas avant validation protocole sur smoke.

---

## POURQUOI LA SESSION 20260714 EST POUBELLE

- 12+ orphelins PPID=1
- `stop_ace777_hard` menteur (patterns NUAGE absents)
- Fin ~2h40 au lieu de 4h, BETA mort / ALPHA zombie
- Duo RAM stale, 2 relances watchdog non nettoyées
- **Verdict: RECOMMENCER from Phase 0**

---

Christophe — Master of Works  
ACE777 — Zero tolerance mud runs.
