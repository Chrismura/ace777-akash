# ACE777 — Plan STORM / Mèche (le vrai job du duo)

**Date :** 2026-07-20  
**Contexte :** mèche ~~10:37 locales (08:37Z) — **aller-retour violent** (ordre ~700–1000$ de course, pas un micro-move de 200$). Descente depuis les highs matin (~~647xx) vers ~6385x–6394x, rebond partiel, puis stabilisation **plus bas** que le short initial. BETA en `Mode Écoute` (volat=18), micro-SELL, ALPHA `duo no_trigger` / `spread_too_wide`.  
**Note :** l’erreur d’analyse « ~200$ » venait de ne reg0n refqit arder que le fragment fills 64202→64012 — trop étroit.  
**Scorecard :** axe **#4** (plus-value) — sans casser #2 usine ni le champion.

## Le paradoxe

ACE est né pour **percuteur les anomalies de carnet**.  
Vide Froid usine fait l’inverse pendant la tempête :

```
volat haute → Mode Écoute (attente froid) → on rate la mèche
```

Ce n’est pas un bug de bus. C’est une **politique « survie chop »** qui étouffe le cas d’usage « wick ».

## Diagnostic (ce run)


| Couche        | Comportement mèche                                | Effet                                     |
| ------------- | ------------------------------------------------- | ----------------------------------------- |
| Stase         | `Mode Écoute` si soft cooldown + marché « chaud » | Scout **s’assoit** pile sur l’event       |
| BETA          | holds 6–8 s, `shock_inversion`                    | Micro-pnl, pas de ride                    |
| ALPHA revenge | armé surtout si **perte** scout                   | Si BETA gagne petit → `duo no_trigger`    |
| Spread        | `RADAR_MAX_SPREAD_BPS=8` strict                   | Tension 6–8 → SKIP pendant le bruit utile |
| Bi-dir        | déjà ON                                           | N’empêche pas un mauvais SELL ni la stase |


## Idée centrale : deux régimes, un moteur

Ne pas supprimer Vide Froid. **Bifurquer** :


| Régime    | Signature                                            | Politique                                  |
| --------- | ---------------------------------------------------- | ------------------------------------------ |
| **CHOP**  | volat haute + tension faible / `direction_unclear`   | Mode Écoute inchangé (usine)               |
| **STORM** | volat haute + **tension ≥ seuil** + direction claire | **Engager** le duo (pas attendre le froid) |


```
                    volat haute ?
                         │
            ┌────────────┴────────────┐
            │                         │
   tension faible / unclear    tension forte + dir
            │                         │
      Mode Écoute (CHOP)         STORM_LATCH
      (usine actuelle)           (nouveau knobs)
```

## Solution en 3 knobs (réversibles, hors genesis)

Tout via `GO_USINE` / env — **champion intact**. Défaut = usine (OFF).

### K1 — `NUAGE_STORM_LATCH` (cœur) — **implémenté (runtime GO)**

Quand stase voudrait `Mode Écoute` **mais** :

- `tension_score >= NUAGE_STORM_TENSION` (défaut **2.5**)
- et `mom_direction` ≠ `neutral`

→ **bypass Mode Écoute** pour ce cycle.  
Sinon → usine pure.

Implémentation : copie `/tmp/ace777_genesis_runtime.txt` + `ACE777_GENESIS_SOURCE` — **champion disque intact**.

```bash
# test recommandé (après STOP)
cd /Users/christophe/ace777-test-day1
NUAGE_BIDIR_SIDES=1 NUAGE_STORM_LATCH=1 NUAGE_DUO_PID_WATCHDOG=0 \
  caffeinate -dims ./GO_USINE_NUAGE.sh
```

Chercher dans le live : `STORM_LATCH bypass Mode Écoute`.

*C’est le fix direct de 08:36:19.*

### K3 — `NUAGE_STORM_SCOUT_HOLD` — **K3v3 entry-latch**

En régime STORM : **pas** de `shock_inversion` / `fluid_exit_*` avant `NUAGE_STORM_MIN_HOLD_SEC` (défaut **20 s**) pour **BETA et ALPHA**.

**E14 (K3v3) :** latch `storm_hold_latched=1` **à l’entrée** si tension ≥ seuil.  
K3v2 testait la tension **live** à la sortie → en fin de mèche elle retombe < 2.5 → shock à 6–7 s (run 2026-07-22 ALPHA **−10.5 $**).

Boot : `STORM_HOLD: ON (K3v3 entry-latch) min_hold=20s`  
Mesure : hold médian fills ALPHA (entrée tension≥2.5) ≥ ~20 s.

### K2 — `NUAGE_STORM_HUNTER` (ALPHA percute la mèche) — **K2v2 (runtime GO)**

**E13 fix (2026-07-21) :** plus de mur TTL. ALPHA s’arme si :

- `tension ≥ NUAGE_STORM_TENSION` (défaut 2.5)
- et direction résolue : `mom_direction` **ou** dir dans `storm_latch.ts` **ou** `radar_direction`
- spread floor `NUAGE_STORM_MAX_SPREAD_BPS` dès tension haute (sans exiger dir)
- export explicite `NUAGE_STORM_*` dans subshells BETA/ALPHA

Live : `STORM_HUNTER arm | … dir=…` · reason CSV `storm_live`

```bash
cd /Users/christophe/ace777-test-day1
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

Boot : `STORM_HUNTER: ON (K2v2 live)`  
*Répond à : duo no_trigger + spread_too_wide pendant le pic — le frein aux coups ~29 $.*

## Ce qu’on ne fait PAS

- Pas de ring buffer / C++ / OFI WS (hors sujet, 8 Go)
- Pas supprimer les filtres spread en veille
- Pas co-entrée INDEX SYNC
- Pas modifier `genesis_manifest` sans GO explicite
- Pas deux setups en parallèle

## Mesure A/B (obligatoire)

1. Baseline : run 4h actuel / usine (Engle + PnL + compteur `Mode Écoute` vs fills pendant volat>X)
2. `NUAGE_STORM_LATCH=1` seul (K1) — 4h
3. Si OK : `+ NUAGE_STORM_HUNTER=1` (K1+K2) — 4h

Critères de succès :

- moins de SKIP `Mode Écoute` quand tension ≥ seuil
- ≥1 fill ALPHA `storm` / session sur event type mèche
- drawdown session pas explosé vs baseline (garde-fou `GLOBAL_STOP`)

## Ordre vs scorecard


| Priorité       | Item                                                  |
| -------------- | ----------------------------------------------------- |
| Fait           | Bi-dir `NUAGE_BIDIR_SIDES` (sens)                     |
| Fait           | K1 `NUAGE_STORM_LATCH`                                |
| Fait           | `NUAGE_MIN_ENTRY_TENSION` (filtre)                    |
| Fait           | K3v2 hold **scout+hunter** (ALPHA ≥20 s)              |
| Fait           | K2 `NUAGE_STORM_HUNTER` — ALPHA sans revenge          |
| Fait           | Fix `set -e` post_delta (mort ALPHA)                  |
| **Maintenant** | **K3v3** latch entrée (E14) — run live hold ≥20 s     |


## Lien événements du jour


| Event                             | Cause                 | Knobs                               |
| --------------------------------- | --------------------- | ----------------------------------- |
| 08:18–19 ALPHA tension 8 + spread | barrière hunter       | K2 spread storm                     |
| 08:19 BETA SELL puis −1.91        | mauvais sens / marché | bi-dir (déjà) + signal, pas miracle |
| 08:36 Mode Écoute sur mèche       | stase anti-tempête    | **K1**                              |
| 08:38 ALPHA 7.55 duo no_trigger   | pas de perte scout    | **K2**                              |


---

**En une phrase :** ACE doit distinguer **bruit** et **tempête directionnelle** — en chop on écoute ; en storm on lâche le hunter.