# Session AMÉLIORATION GROK — brief de démarrage

**Ouverture :** 2026-07-21  
**But unique :** retrouver des fills **≥ ~29 USDT** (comme déjà vu), pas optimiser des micros à 0.02 $.

---

## Preuve que c’est possible (CSV NUAGE)

| Quand | Agent | PnL | bps | tension |
|-------|--------|-----|-----|---------|
| 2026-07-14 | **ALPHA** | **+32.07** | 12.7 | ~7.9 |
| 2026-07-15 | **ALPHA** | **+29.60** | 28.5 | ~1.5 |
| 2026-07-20 | ALPHA | +8.53 | 5.5 | ~3.6 |
| 2026-07-20 | BETA max | +2.42 | 24 | ~7.4 |

→ Les **29 $+** sont des coups **ALPHA (hunter ×13 · 800 USDT)**, pas BETA.  
BETA maxe ~2–2.5 $ même à 30 bps (masse trop petite).

**Implication :** améliorer = faire **rire ALPHA sur les vrais moves**, pas faire trader BETA 45×/h.

---

## Stack shipé (2026-07-21) — prêt run

| Flag | Rôle | Statut |
|------|------|--------|
| `NUAGE_BIDIR_SIDES=1` | sens AUTO | prêt |
| `NUAGE_MIN_ENTRY_TENSION=2.5` | moins de micros entrée | prêt |
| `NUAGE_STORM_LATCH=1` | bypass Mode Écoute + écrit `storm_latch.ts` | K1 |
| `NUAGE_STORM_SCOUT_HOLD=1` | hold ≥20 s si tension haute | K3 |
| `NUAGE_STORM_HUNTER=1` | ALPHA sans perte scout (anti `no_trigger`) | **K2v2 SHIPPÉ** (live + export env) |
| Fix `set -e` post_delta | mort ALPHA | **toujours ON** via runtime |
| `NUAGE_DUO_PID_WATCHDOG` | relaunch process | OFF en test |
| `PROCESS_EXIT` / `PROCESS_DIE` | raison de mort | toujours ON via GO |

Champion `genesis_manifest` md5 `37fca367…` — **intouchable**.

---

## Cible run (KPI)

1. **≥ 1 fill ALPHA ≥ 20 $** sur un run 4 h (stretch : ≥ 29 $)  
2. Live : lignes `STORM_HUNTER arm` + fills hors `duo no_trigger`  
3. Hold scout tension≥2.5 : médiane ≫ 8 s (preuve K3)  
4. Champion disque md5 inchangé

---

## Commande — lance dans TON terminal (STOP + hygiène d’abord)

```bash
cd /Users/christophe/ace777-test-day1
# ./stop_ace777_hard.sh   # si session précédente
# scripts/hygiene_mac_ram.sh   # si RAM TIGHT

NUAGE_MIN_ENTRY_TENSION=2.5 \
NUAGE_BIDIR_SIDES=1 \
NUAGE_STORM_LATCH=1 \
NUAGE_STORM_SCOUT_HOLD=1 \
NUAGE_STORM_HUNTER=1 \
NUAGE_STORM_MIN_HOLD_SEC=20 \
NUAGE_STORM_TTL_SEC=20 \
NUAGE_STORM_MAX_SPREAD_BPS=14 \
NUAGE_DUO_PID_WATCHDOG=0 \
caffeinate -dims ./GO_USINE_NUAGE.sh
```

**Boot attendu :**
- `STORM_LATCH: ON`
- `STORM_SCOUT_HOLD: ON min_hold=20s`
- `STORM_HUNTER: ON ttl=20s spread_max=14`
- `GENESIS_RUNTIME: … disk md5=37fca367… — intact`

Docs : `engle/PLAN_STORM_WICK.md` · `engle/PISTES_OSCI_HALO.md` (tiroirs séparés)

---

## Phrase d’ouverture (si nouveau chat)

> Session **amélioration GROK**. Brief : `engle/SESSION_AMELIORATION_GROK.md`.  
> Stack K1+K2+K3+MIN_ENTRY shippé. Objectif : fills ALPHA **+29 $**. Champion intact.
