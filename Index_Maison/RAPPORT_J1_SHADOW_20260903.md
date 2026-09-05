# 📊 RAPPORT J+1 — SHADOW MODE SCÉNARIO C (fenêtre 24h complète)

> **Statut au 03/09 19h25 UTC.** Fenêtre : 02/09 17:23 → 03/09 17:23 UTC (24h exactes).
> Source : `runs/SHADOW_SC_20260902_FILLS.csv` (116 fills = 58 entrées + 58 sorties) + 1 555 ticks.
> Moteur toujours vivant après la fenêtre (uptime 1j02h) — 0 nouveau fill depuis 17:23, gates H=0.
> **Conforme au protocole : les 4 métriques, BOOTSTRAP isolé, ZÉRO interprétation dans ce rapport.**

---

## LES 4 MÉTRIQUES

| # | Métrique | Valeur |
|---|----------|--------|
| 1 | **Médiane brute / trade** | **+1,50 USDT** (moyenne +1,05) |
| 2 | **Fréquence** | 58 trades / 24h = **2,4/h** |
| 3 | **NET cumulé** | **−41,12 USDT** (frais moteur estimés : 102,08 USDT) |
| 4 | **Positions flottantes** (cap 2h) | **2 / 58** sorties au cap (`hold=7200s`) |

### Détail métrique 4 — les 2 flottantes (le problème central identifié)

| Sortie | Jambe | Brut | Net | Cause |
|---|---|---|---|---|
| 02/09 21:56 | BETA SHORT | −16,37 | −18,13 | h_gate_off (cap 2h) |
| 02/09 22:36 | ALPHA LONG | −40,15 | −41,91 | h_gate_off (cap 2h) |

→ Ces deux seules sorties = **−60,04 net**, soit **146 % de la perte totale de la fenêtre**.
Les 56 autres sorties (trailing_stop) : net cumulé ≈ **+18,92**.

### Par jambe

| Jambe | Sorties | Brut | Net |
|---|---|---|---|
| ALPHA (long) | 28 | +16,07 | −33,21 |
| BETA (short) | 30 | +44,89 | −7,91 |

### Causes de sortie

- `trailing_stop` : 56
- `h_gate_off` (cap 2h aveugle) : 2 — dont les deux seules pertes > 15 USDT

---

## BOOTSTRAP (5 000 tirages avec remise, seed 42, sur les 58 nets)

| | P05 | P50 | P95 |
|---|---|---|---|
| Net moyen / trade | **−2,206** | **−0,601** | **+0,417** |

- IC 90 % du net moyen par trade : **[−2,21 ; +0,42] USDT**
- Net moyen observé : −0,709 USDT/trade
- **Zéro est DANS l'intervalle** → à J+1, l'edge net n'est ni prouvé ni réfuté.

---

## LIMITE D'ÉCHANTILLON (rappel protocole, à lire avant toute conclusion)

- 1 seule nuit, 1 seul régime de marché (BTC 76 964 → 78 145, ATR 1h ≈ 434).
- Le BOOTSTRAP mesure la variabilité d'échantillonnage, PAS le risque d'overfitting.
- La validation décisionnelle reste l'**essai 3 bras × 4 fenêtres** (C2 de la feuille de route), pas ce rapport.

---

## PROCHAINE ÉTAPE (protocole voté)

1. Ce rapport part **en brut à Gemini** (R32) — analyses séparées, puis confrontation famille.
2. Décision ce soir : lancement **essai 3 bras** (A fixe 30 min / B variance pré-entrée / C horloge volume) + **superviseur L2 passif** (si famille d'accord).

---
*Rapport généré par Buffy — lecture seule, zéro ordre, zéro contact moteur. Données : CSV shadow du 02-03/09.*
