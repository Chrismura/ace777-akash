# Vortex SHADOW — simulation timing & intelligence

> Mode **lecture seule** — replay CSV, pas de modification live
> Généré: `2026-07-08T17:46:06Z`

## Méthode

1. **Régime** recalculé toutes les N secondes (5 / 15 / 60) ou statique.
2. **PnL rule** : derniers FILLED → TREND si net > 0, sinon CHOP (comme supervisor V9).
3. **Features** : tension moyenne + taux SKIP + dérivée tension → `radar_target` continu 0.55–0.90.
4. **Impact vacuum** : lignes `vacuum_filter` qui passeraient le nouveau seuil.
5. **Proxy PnL** : pour entrées supplémentaires, PnL du prochain FILLED dans les 90s (oracle optimiste/pessimiste selon corrélation).
6. **Contrefactuel FILLED** : trades réels bloqués si tension < seuil vortex à ce moment.

_Limite : le radar domine souvent avant vacuum — impact vortex peut être faible sur vide froid actuel._

## `MASTER_BASE_V8_5_IMPACT_4H`

- Durée replay: **13.33 h** | Lignes: 5906 | FILLED: 201 | PnL réel: **4.5053 USDT**
- SKIP radar_block: 2167 | SKIP vacuum_filter: 0

### Comparatif politiques

| Politique | Flips régime | %CHOP | %TREND | Extra vacuum pass | Proxy PnL extra | Shadow FILLED | Delta vs réel |
|-----------|--------------|-------|--------|-------------------|-----------------|---------------|---------------|
| Sans Vortex (0.85 fixe) | — | — | — | 0 (0 proxy) | +0.0000 | 4.5053 | **+0.0000** |
| Radar fixe 0.618 (TREND permanent) | — | — | — | 0 (0 proxy) | +0.0000 | 4.5053 | **+0.0000** |
| Radar fixe 0.85 (CHOP permanent) | — | — | — | 0 (0 proxy) | +0.0000 | 4.5053 | **+0.0000** |
| Vortex 60s — PnL rule | 4 | 74.9% | 25.1% | 0 (0 proxy) | +0.0000 | 4.5053 | **+0.0000** |
| Vortex 15s — PnL rule | 4 | 75.0% | 25.0% | 0 (0 proxy) | +0.0000 | 4.5053 | **+0.0000** |
| Vortex 5s — PnL rule | 4 | 75.0% | 25.0% | 0 (0 proxy) | +0.0000 | 4.5053 | **+0.0000** |
| Vortex 5s — features marché | 0 | 100.0% | 0.0% | 0 (0 proxy) | +0.0000 | 4.5053 | **+0.0000** |
| Vortex 15s — features marché | 0 | 100.0% | 0.0% | 0 (0 proxy) | +0.0000 | 4.5053 | **+0.0000** |

### Stabilité régime (5s vs 60s)

- **Vortex 5s — PnL rule** : 4 bascules / 9600 slots (~0.3 /h)
- **Vortex 15s — PnL rule** : 4 bascules / 3200 slots (~0.3 /h)
- **Vortex 60s — PnL rule** : 4 bascules / 800 slots (~0.3 /h)
- **Vortex 5s — features marché** : 0 bascules / 9600 slots (~0.0 /h)

### Lecture rapide

- **Peu ou pas de `vacuum_filter`** sur ce cycle → le Vortex n'aurait presque pas changé les SKIP (radar en amont).
- Meilleur scénario shadow: **Sans Vortex (0.85 fixe)** (+0.0000 USDT vs réel).
- Pire scénario shadow: **Sans Vortex (0.85 fixe)** (+0.0000 USDT vs réel).

## `MASTER_BASE_V8_5_IMPACT_C2`

- Durée replay: **6.48 h** | Lignes: 1971 | FILLED: 44 | PnL réel: **-0.1669 USDT**
- SKIP radar_block: 1472 | SKIP vacuum_filter: 0

### Comparatif politiques

| Politique | Flips régime | %CHOP | %TREND | Extra vacuum pass | Proxy PnL extra | Shadow FILLED | Delta vs réel |
|-----------|--------------|-------|--------|-------------------|-----------------|---------------|---------------|
| Sans Vortex (0.85 fixe) | — | — | — | 0 (0 proxy) | +0.0000 | -0.1669 | **-0.0000** |
| Radar fixe 0.618 (TREND permanent) | — | — | — | 0 (0 proxy) | +0.0000 | -0.1669 | **-0.0000** |
| Radar fixe 0.85 (CHOP permanent) | — | — | — | 0 (0 proxy) | +0.0000 | -0.1669 | **-0.0000** |
| Vortex 60s — PnL rule | 2 | 97.7% | 2.3% | 0 (0 proxy) | +0.0000 | -0.1669 | **-0.0000** |
| Vortex 15s — PnL rule | 2 | 97.7% | 2.3% | 0 (0 proxy) | +0.0000 | -0.1669 | **-0.0000** |
| Vortex 5s — PnL rule | 2 | 97.7% | 2.3% | 0 (0 proxy) | +0.0000 | -0.1669 | **-0.0000** |
| Vortex 5s — features marché | 0 | 100.0% | 0.0% | 0 (0 proxy) | +0.0000 | -0.1669 | **-0.0000** |
| Vortex 15s — features marché | 0 | 100.0% | 0.0% | 0 (0 proxy) | +0.0000 | -0.1669 | **-0.0000** |

### Stabilité régime (5s vs 60s)

- **Vortex 5s — PnL rule** : 2 bascules / 4667 slots (~0.3 /h)
- **Vortex 15s — PnL rule** : 2 bascules / 1556 slots (~0.3 /h)
- **Vortex 60s — PnL rule** : 2 bascules / 389 slots (~0.3 /h)
- **Vortex 5s — features marché** : 0 bascules / 4667 slots (~0.0 /h)

### Lecture rapide

- **Peu ou pas de `vacuum_filter`** sur ce cycle → le Vortex n'aurait presque pas changé les SKIP (radar en amont).
- Meilleur scénario shadow: **Sans Vortex (0.85 fixe)** (-0.0000 USDT vs réel).
- Pire scénario shadow: **Sans Vortex (0.85 fixe)** (-0.0000 USDT vs réel).

## `MASTER_HYBRID_VF_20260708`

- Durée replay: **1.33 h** | Lignes: 1214 | FILLED: 35 | PnL réel: **8.0607 USDT**
- SKIP radar_block: 893 | SKIP vacuum_filter: 0

### Comparatif politiques

| Politique | Flips régime | %CHOP | %TREND | Extra vacuum pass | Proxy PnL extra | Shadow FILLED | Delta vs réel |
|-----------|--------------|-------|--------|-------------------|-----------------|---------------|---------------|
| Sans Vortex (0.85 fixe) | — | — | — | 0 (0 proxy) | +0.0000 | 8.0607 | **+0.0000** |
| Radar fixe 0.618 (TREND permanent) | — | — | — | 0 (0 proxy) | +0.0000 | 8.0607 | **+0.0000** |
| Radar fixe 0.85 (CHOP permanent) | — | — | — | 0 (0 proxy) | +0.0000 | 8.0607 | **+0.0000** |
| Vortex 60s — PnL rule | 3 | 23.5% | 76.5% | 0 (0 proxy) | +0.0000 | 8.0607 | **+0.0000** |
| Vortex 15s — PnL rule | 3 | 23.1% | 76.9% | 0 (0 proxy) | +0.0000 | 8.0607 | **+0.0000** |
| Vortex 5s — PnL rule | 3 | 22.9% | 77.1% | 0 (0 proxy) | +0.0000 | 8.0607 | **+0.0000** |
| Vortex 5s — features marché | 0 | 100.0% | 0.0% | 0 (0 proxy) | +0.0000 | 8.0607 | **+0.0000** |
| Vortex 15s — features marché | 0 | 100.0% | 0.0% | 0 (0 proxy) | +0.0000 | 8.0607 | **+0.0000** |

### Stabilité régime (5s vs 60s)

- **Vortex 5s — PnL rule** : 3 bascules / 961 slots (~2.3 /h)
- **Vortex 15s — PnL rule** : 3 bascules / 321 slots (~2.3 /h)
- **Vortex 60s — PnL rule** : 3 bascules / 81 slots (~2.3 /h)
- **Vortex 5s — features marché** : 0 bascules / 961 slots (~0.0 /h)

### Lecture rapide

- **Peu ou pas de `vacuum_filter`** sur ce cycle → le Vortex n'aurait presque pas changé les SKIP (radar en amont).
- Meilleur scénario shadow: **Sans Vortex (0.85 fixe)** (+0.0000 USDT vs réel).
- Pire scénario shadow: **Sans Vortex (0.85 fixe)** (+0.0000 USDT vs réel).

## `MASTER_TENDANCE_SENTINELLE_INVERSION_8H00`

- Durée replay: **11.61 h** | Lignes: 6954 | FILLED: 251 | PnL réel: **-22.9837 USDT**
- SKIP radar_block: 5259 | SKIP vacuum_filter: 0

### Comparatif politiques

| Politique | Flips régime | %CHOP | %TREND | Extra vacuum pass | Proxy PnL extra | Shadow FILLED | Delta vs réel |
|-----------|--------------|-------|--------|-------------------|-----------------|---------------|---------------|
| Sans Vortex (0.85 fixe) | — | — | — | 0 (0 proxy) | +0.0000 | -22.9837 | **+0.0000** |
| Radar fixe 0.618 (TREND permanent) | — | — | — | 0 (0 proxy) | +0.0000 | -22.9837 | **+0.0000** |
| Radar fixe 0.85 (CHOP permanent) | — | — | — | 0 (0 proxy) | +0.0000 | -22.9837 | **+0.0000** |
| Vortex 60s — PnL rule | 16 | 79.9% | 20.1% | 0 (0 proxy) | +0.0000 | -22.9837 | **+0.0000** |
| Vortex 15s — PnL rule | 16 | 79.9% | 20.1% | 0 (0 proxy) | +0.0000 | -22.9837 | **+0.0000** |
| Vortex 5s — PnL rule | 16 | 79.8% | 20.2% | 0 (0 proxy) | +0.0000 | -22.9837 | **+0.0000** |
| Vortex 5s — features marché | 0 | 100.0% | 0.0% | 0 (0 proxy) | +0.0000 | -22.9837 | **+0.0000** |
| Vortex 15s — features marché | 0 | 100.0% | 0.0% | 0 (0 proxy) | +0.0000 | -22.9837 | **+0.0000** |

### Stabilité régime (5s vs 60s)

- **Vortex 5s — PnL rule** : 16 bascules / 8358 slots (~1.4 /h)
- **Vortex 15s — PnL rule** : 16 bascules / 2786 slots (~1.4 /h)
- **Vortex 60s — PnL rule** : 16 bascules / 697 slots (~1.4 /h)
- **Vortex 5s — features marché** : 0 bascules / 8358 slots (~0.0 /h)

### Lecture rapide

- **Peu ou pas de `vacuum_filter`** sur ce cycle → le Vortex n'aurait presque pas changé les SKIP (radar en amont).
- Meilleur scénario shadow: **Sans Vortex (0.85 fixe)** (+0.0000 USDT vs réel).
- Pire scénario shadow: **Sans Vortex (0.85 fixe)** (+0.0000 USDT vs réel).

## Synthèse globale

| Politique | Delta PnL moyen (vs réel) | Flips/h moyen |
|-----------|---------------------------|---------------|
| Sans Vortex (0.85 fixe) | **+0.0000** USDT | — |
| Radar fixe 0.618 (TREND permanent) | **+0.0000** USDT | — |
| Radar fixe 0.85 (CHOP permanent) | **+0.0000** USDT | — |
| Vortex 60s — PnL rule | **+0.0000** USDT | 1.1 |
| Vortex 15s — PnL rule | **+0.0000** USDT | 1.1 |
| Vortex 5s — PnL rule | **+0.0000** USDT | 1.1 |
| Vortex 5s — features marché | **+0.0000** USDT | 0.0 |
| Vortex 15s — features marché | **+0.0000** USDT | 0.0 |

## Recommandation simulation

- **TREND permanent** : impact marginal en moyenne — le goulot n'est pas le seuil vacuum seul.
- **Features 5s vs PnL 60s** : différence faible — valider sur cycle dédié avant choix.
- **Prochaine étape suggérée** : cycle testnet A/B `VORTEX_CONTROL_ENABLED=TRUE` avec supervisor **15s features + hystérésis**, pas 5s PnL seul.
