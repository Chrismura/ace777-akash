# Côtés bi-directionnels (BETA AUTO + ALPHA opposite) — couche réversible

**Date :** 2026-07-20  
**Scorecard :** axe #4 (plus-value / couverture trend) — essai A/B  
**Pourquoi :** usine = BETA SELL + ALPHA BUY figés. Marché haussier/baissier asymétrique. Même duo scout/hunter, mais BETA choisit le sens ; ALPHA revenge = côté opposé.

## Comportement

| | Usine (`NUAGE_BIDIR_SIDES=0`) | Bi-dir (`=1`) |
|---|---|---|
| BETA | `FORCE_ENTRY_SIDE=SELL` `POSITION_SIDE=SHORT` | `AUTO` / `BOTH` |
| ALPHA | `FORCE_ENTRY_SIDE=BUY` `POSITION_SIDE=LONG` | `AUTO` / `BOTH` |
| Leviers / masses | x5·200 / x13·800 | **inchangés** |
| Rôles | SCOUT / HUNTER | inchangés |
| Revenge | `DUO_FORCE_OPPOSITE` | forcé ON |

Moteur (`genesis_manifest.txt`) **intact** — patch runtime via `GO_USINE_NUAGE.sh` uniquement (comme wait-timer / duo PID).

## Usage

```bash
# usine (défaut) — ne rien changer
caffeinate -dims ./GO_USINE_NUAGE.sh

# essai bi-dir (après STOP du run en cours)
cd /Users/christophe/ace777-test-day1
NUAGE_BIDIR_SIDES=1 NUAGE_DUO_PID_WATCHDOG=0 caffeinate -dims ./GO_USINE_NUAGE.sh
```

Boot attendu : `BIDIR_SIDES=ON (AUTO/BOTH + opposite)`

## Ce que ce n’est PAS

- Pas deux setups en parallèle
- Pas hedge simultané BETA long + ALPHA short « pour annuler »
- Pas de co-entrée synchrone (INDEX SYNC reste OFF)

## Mesure A/B

1. Run 4h usine (baseline) → Engle / PnL  
2. Run 4h `NUAGE_BIDIR_SIDES=1` → Engle / PnL  
3. Comparer : fills BUY+SELL BETA, revenge ALPHA opposés, PnL total, SKIP `tactic_mismatch`
