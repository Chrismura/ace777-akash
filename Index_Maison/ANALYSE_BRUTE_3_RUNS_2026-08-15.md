# 🔬 Analyse brute des 3 runs (14-15/08) — refaite par Buffy, jusqu'au CSV

**Date :** 2026-08-15 · Sources : CSV scellés `runs/SCELLE/` (4 fichiers) + EXIT_DUMP + configs + genesis.
**Méthode :** re-vérification intégrité → parsing brut → sessions → stats → diffs de vocabulaire.

---

## 1. Intégrité & même moteur ✅ (confirmé, preuve indépendante)

| Contrôle | Résultat |
|---|---|
| sha256 des 4 CSV scellés | **OK** (match signatures) |
| Préfixe identique (fichier 14 vs 15) | **octet-pour-octet** (ALPHA 3 454 288 o, BETA 5 429 893 o) |
| genesis_md5 | `8d9ee8d6…` identique sur les 4 signatures |
| Config (config_active.env + vortex_v2_collab.env) | mtime 12/08 18:28 → **inchangée** pendant les 3 runs |

→ **Même moteur, même config sur les 3 runs. Aucun changement de setup** (seule la durée 4h/8h et le nombre de relances changent).

---

## 2. ⚠️ TTL réel = 60 s, PAS 20 s (anomalie majeure de l'analyse)

Toute l'analyse famille + mémoire utilisait **TTL = 20 s** (valeur par défaut du genesis). **Faux.**

- `config_active.env` : `export DUO_EVENT_TTL_SEC=60` (commentaire « P1 : TTL état scout élargi (réduit stale_state) »)
- `config_profiles/vortex_v2_collab.env` : `export DUO_EVENT_TTL_SEC=60`
- `genesis_manifest.txt` L297 : `DUO_EVENT_TTL_SEC="${DUO_EVENT_TTL_SEC:-20}"` → **lit l'env = 60**, le 20 n'est qu'un fallback jamais utilisé ici.
- Utilisé L1104 (duo_hunter_decide) et L2332 (partner guard).

**Conséquence :** la famille a validé « heartbeat neutralise le TTL 20s » sur une prémisse fausse. La conclusion reste vraie (le heartbeat rafraîchit ts_ms toutes les ~8 s, donc reste < 60 s), mais le « 20 s » des rapports est à corriger partout.

---

## 3. ⚠️ CSV : header 12 colonnes, données 11 colonnes (durée absente du scellé)

- Header : `ts,cycle,side,status,entryPrice,exitPrice,qty,bps,pnl,exitReason,holdSec,msg` (12)
- **Chaque ligne de données : 11 champs.** La colonne `msg` n'existe **pas du tout** (même pas vide).
- Le champ détaillé (`radar=… size_note=… tension=…`) est écrit **dans `holdSec`** (11e). La durée de détention `$hold_done` n'est **PAS écrite dans le CSV**.
- **MAIS la durée EST calculée et affichée au terminal** (log live, non scellé) : `hold=7s sec=7` (genesis L2516, cohérent avec entry→exit). Elle vit donc dans `runs/CMD_TRACE_*.log`, **pas dans le fichier scellé**.
- **Preuve code** : L2507 (écriture CSV FILLED) met le message dans le slot `holdSec` et n'écrit **ni la durée ni `msg`** ; L2516 (echo terminal) affiche `hold=$hold_done s sec=$hold_done`.
- **Impact** : le fichier de vérité scellé/signé est **aveugle à la durée de détention** (valeur pourtant clé pour analyser trades rapides/longs, capital immobilisé, corrélation durée↔pnl). À réparer : écrire la durée dans `holdSec` et le message dans `msg` (12 colonnes comme promis). 0 ligne sur 20 961 (ALPHA) / 29 157 (BETA) n'a de msg.

---

## 4. Timeline réelle (confirmée par EXIT_DUMP.log)

| Session | Début → fin | Cycles | Sortie |
|---|---|---|---|
| Run 4h #1 | 12:51:16 → 15:57:00 | 1→1320 | **rc=0** propre |
| mini-session (non documentée) | 16:22:37 → 16:24:31 | 1→4 | sans EXIT_DUMP |
| V2 #1 | 16:24:31 → 19:35:46 | 1→1371 | rc=0 |
| V2 #2 | 19:36:23 → 19:53:47 | 1→111 | rc=0 |
| V2 #3 | 19:54:36 → 20:24:32 | 1→177 | rc=0 |
| Nuit | 21:45:03 → 05:44:43 | 1→3629 | rc=0 |

- **Zéro mort rc=1 après 12:48** (les 6 morts du matin : 12:06/12:07/12:14/12:17/12:37/12:40, dernière commande tracée `vortex_micro_circuit_breaker "$spread_bps"`).
- Les « 3 sessions » de V2 sont des **relances auto par design** (le fortress sort « Done » quand son compteur CYCLES est atteint, le launcher relance jusqu'aux 4h murales) — **pas des crashes**.
- **Anomalie mineure :** mini-session de 2 min (16:22→16:24, 4 cycles) entre Run 4h#1 et V2, non documentée, sans trace EXIT_DUMP.

---

## 5. Stats recalculées (brut, par fenêtre)

### ALPHA (x13)
| Run | filled | PNL | W/L/F | flat% | revenge (trades) |
|---|---|---|---|---|---|
| 4h #1 | 65 | **+28.2571** | 30/19/16 | 24.6% | 52 (80.0%) |
| V2 | 37 | **+16.6131** | 21/4/12 | 32.4% | 25 (67.6%) |
| Nuit | 56 | **+8.6069** | 24/10/22 | 39.3% | 51 (91.1%) |

### BETA (x5)
| Run | filled | PNL | W/L/F | flat% | revenge |
|---|---|---|---|---|---|
| 4h #1 | 155 | **+0.3956** | 57/65/33 | 21.3% | 0 |
| V2 | 157 | **+1.969** | 61/36/60 | 38.2% | 0 |
| Nuit | 205 | **+2.5071** | 73/57/75 | 36.6% | 0 |

> Écart de ±1 trade vs tableau précédent (BETA V2 157 vs 156, BETA Nuit 205 vs 204) = **comptage à la frontière de fenêtre** (off-by-one).

---

## 6. Diffs de « vocabulaire » entre les 3 runs (≠ changement de setup)

Ces différences sont **dynamiques** (décisions du moteur selon le marché), pas des changements de config :

| Champ | Run 4h #1 uniquement | V2/Nuit uniquement |
|---|---|---|
| size_note ALPHA | `hunter_burst_1.625x`, `…trap` (sans `_no_add`) | `…trap_no_add` |
| size_note BETA | `strong_conf_full+entry_25_75_trap` | — |
| exitReason BETA | `shock_exit_10bps` (1×) | `kill_switch` (1×, V2) |

---

## 7. Autres anomalies notées

1. **Signature scellée : champ `config=` vide** → on ne peut pas prouver a posteriori QUELLE config tournait (gouvernance à renforcer).
2. **Queue de session figée** : Run 4h #1 — dernier trade 15:56:09 (cyc 1314), puis 6 cycles SKIP `radar_block` et 26 min de silence avant la relance. Bénin (marché calme), à surveiller.
3. **EXIT_DUMP des morts rc=1** : dernière commande tracée = `vortex_micro_circuit_breaker`, alors que l'enquête du 14/08 pointe le SI de `swarm_neighbor_load`. Non contradictoire (le trap DEBUG trace tout), mais à garder en tête.

---

## Conclusion

Les 3 runs sont le **même moteur avec la même config** — aucune virgule n'a changé dans le setup. Les vraies anomalies sont :
- **TTL 60s ≠ 20s** (prémisse fausse dans toute l'analyse famille).
- **CSV header/données 12 vs 11 colonnes** (msg jamais écrit ; la durée `hold_done` est affichée au terminal mais **absente du CSV scellé** → à écrire dans `holdSec` pour les prochains scellements).
- **Signature `config=` vide** (traçabilité config absente).

Le bug heartbeat (revenge quasi-permanent) reste confirmé, mais à re-formuler avec TTL=60s.
