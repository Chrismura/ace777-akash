---
ts: 2026-07-27T19:54:27Z
agent: score_hulk_veille
mode: P0_read_only
paper: PAPER_V1_20260726_174926.csv
window_min: 30
stale_hours: 6
n_buys: 7
n_hints_flat: 479
---

# Score Hulk ↔ Veille — `PAPER_V1_20260726_174926.csv`

Généré : `2026-07-27T19:54:27Z` · **0 API** · lecture seule.

## Légende

- 🔴 **RED** — hint négatif (`WATCH_PULLBACK` / `IMPULSE_WAIT`…) dans les **30 min** avant le BUY
- 🟠 **AMBER** — pas de hint 30m, mais caution dans les **6 h** (stale)
- 🟡 **YELLOW** — blind spot : la veille n’a jamais parlé de cette paire avant le trade
- 🟢 **GREEN** — pas de frein veille dans 30m (et la paire était déjà connue)

> Correction vs pitch externe : RWAINC/QAIT early = **YELLOW** (veille après le buy), pas RED. KITE GREEN ≠ « la veille confirme un long » : ça veut dire *pas de frein récent* (les vieux WATCH_PULLBACK hors fenêtre ne comptent plus).

## Synthèse

| Score | n |
|-------|---|
| 🔴 RED | 1 |
| 🟠 AMBER | 2 |
| 🟡 YELLOW | 2 |
| 🟢 GREEN | 2 |

- BUY scorés : **7**
- Hints plats veille : **479**
- RED puis stop négatif (preuve confrontation) : **1**
- Somme PnL des sells liés (1er sell après buy) : **-1.22 USDT** (incomplet si positions encore ouvertes)

## Tableau

| Paire | Heure BUY (UTC) | Score | Résultat sell | Détail |
|-------|-----------------|-------|---------------|--------|
| QAITUSDT | 2026-07-26 18:03 | 🔴 RED | -1.22$ | Veille WATCH_PULLBACK 13 min avant (×1 dans 30m) |
| RIZEUSDT | 2026-07-26 20:42 | 🟢 GREEN | ouvert / pas de sell après | Pas d'alerte négative dans 30m (veille a déjà parlé de la paire avant, sans frein récent) |
| RWAINCUSDT | 2026-07-27 07:31 | 🟠 AMBER | ouvert / pas de sell après | Pas de hint dans 30m, mais caution stale (IMPULSE_WAIT il y a 0.5h, ×4/6h) |
| REDUSDT | 2026-07-27 12:34 | 🟡 YELLOW | ouvert / pas de sell après | Blind spot veille — aucune alerte sur cette paire avant le trade |
| ZBCNUSDT | 2026-07-27 16:29 | 🟡 YELLOW | ouvert / pas de sell après | Blind spot veille — aucune alerte sur cette paire avant le trade |
| TELUSDT | 2026-07-27 16:55 | 🟢 GREEN | ouvert / pas de sell après | Pas d'alerte négative dans 30m (veille a déjà parlé de la paire avant, sans frein récent) |
| CHIPUSDT | 2026-07-27 17:25 | 🟠 AMBER | ouvert / pas de sell après | Pas de hint dans 30m, mais caution stale (WATCH_PULLBACK il y a 2.8h, ×1/6h) |

## Lecture

1. **RED + stop** = Hulk a ignoré un frein veille récent → filtre soft utile.
2. **YELLOW** = veille trop lente / filtre trop étroit (début de session ou paire hors radar).
3. **AMBER** = bruit ou caution trop vieille — ne suffit pas seul à bloquer, à croiser avec prix.
4. Ne pas juger la campagne sur le seul réalisé tant que des positions restent ouvertes.

## Fichiers source

- Paper : `/Users/christophe/ace777-test-day1/hulk-mexc/runs/PAPER_V1_20260726_174926.csv`
- Veille : `/Users/christophe/ace777-test-day1/hulk-mexc/runs/VEILLE_CALLS.jsonl`
