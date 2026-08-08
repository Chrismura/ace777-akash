# ACE777 — Journal d’erreurs / ratés (living doc)

**But :** pour valider ACE777, les erreurs structurelles (crash nœud, mèche ratée, faux diagnostic) doivent être **tracées, classées, et idéalement éliminées** — pas rediscutées à zéro chaque run.

**Règle :** une entrée = un fait observé + cause probable + correctif (fait / prévu / refusé).  
Pas de roman Gemini. Pas de modifier le champion sans GO.

---

## Taxonomie

| Code | Famille |
|------|---------|
| E-PROC | Process mort / restart / désynchro PID |
| E-STASE | Mode Écoute / Vide Froid qui étouffe un event utile |
| E-SPREAD | `spread_too_wide` pendant tension utile (hunter) |
| E-DUO | Bus / revenge / `duo_wait` / `no_trigger` / `tension_stale` |
| E-SIDE | Mauvais sens scout (même en bi-dir) |
| E-DIAG | Fausse interprétation (outil / IA / zoom fills) |
| E-OPS | Hygiène, STERILE, RAM Mac, lancement |

---

## Journal

### 2026-07-20 — session bidir `NUAGE_PROD_4H` (~08:07Z–10:18Z)

| ID | Code | Fait | Cause | Statut |
|----|------|------|-------|--------|
| E01 | E-STASE | Mèche ~10:37 locales : Mode Écoute (volat≈18) pendant dump/rebond violent | Stase = « attendre froid » même en tempête directionnelle | **Correctif K1** `NUAGE_STORM_LATCH` prêt à tester |
| E02 | E-SPREAD | ALPHA tension 8.x → `spread_too_wide` (ex. 08:18) | Seuil radar fixe ; Vortex OFF sur usine | Prévu K2 storm hunter / Vortex plus tard |
| E03 | E-DUO | ALPHA souvent `duo no_trigger` pendant mèche si BETA gagne petit | Revenge armée surtout sur **perte** scout | **Correctif K2** `NUAGE_STORM_HUNTER` shippé |
| E04 | E-SIDE | 08:19 BETA SELL puis −1.91 sur squeeze haussier | Bi-dir ON mais signal a choisi short | Accepter risque scout ; pas « bi-dir cassé » |
| E05 | E-DIAG | Analyse initiale « mèche ~200$ » | Zoom fills 64202→64012 trop étroit | **Corrigé** — event ~700–1000$ A/R |
| E06 | E-PROC | Impression « restart BETA change la sensibilité » | Voir note ci-dessous | Documenté — pas un knobs caché |
| E07 | E-OPS | `FAIL: patch STORM non appliqué` au boot | Assert cherchait chaîne contiguë alors que log a `${C_Y}…${C_N}` au milieu | **Corrigé** 2026-07-20 |
| E08 | E-OPS | `zsh: killed` au relance (sans nettoyage) | RAM Mac / process fantômes après changement setup | Hygiène obligatoire avant chaque GO |
| E09 | E-PROC | BETA mort ~12:53Z (session −3.94) | Avant: `NET_RETRY rc=6` (DNS/host) ×2 ; puis silence ; ALPHA `tension_stale` puis relance sémantique seule ; **duo PID OFF** → pas de relaunch BETA | Documenté — trade-off `NUAGE_DUO_PID_WATCHDOG=0` |

**Bilan session :** PnL **+8.65** (BETA +0.41 · ALPHA +8.25, 4 fills) · bi-dir actif (BETA 44 BUY / 40 SELL) · Engle `WAIT_COLD` · duo PID watchdog **OFF** sur ce run.

### 2026-07-20 — session bidir soir `NUAGE_PROD_4H` (18:54Z–~20:30Z stop)

| ID | Code | Fait | Cause | Statut |
|----|------|------|-------|--------|
| E10 | E-PROC | BETA mort juste après fill #461 @20:26:37Z (FILLED OK, `shock_inversion_stop`, `mode=OFF` imprimé) ; cycle 462 jamais venu ; ALPHA `duo stale_state` | **Cause exacte INCONNUE** — écarté pour ce crash : STOP/GLOBAL_STOP (pas de log), NET_RETRY dans la fenêtre (contrairement E09), OOM Console, erreur trade CSV. Process `bash -s` mort sans message ; `run_unit` **efface** le raw.log à la sortie et **ne log pas** le exit code → preuve détruite. Hypothèse restante : exit silencieux `set -euo pipefail` en tout début de cycle suivant, ou kill externe non journalisé | Instrumentation manquante = trou #3 robustesse ; duo PID OFF a empêché le relaunch |
| E11 | E-PROC | Run 2026-07-21 ~07:57→10:34Z : **BETA mort 09:32:45Z** + **ALPHA mort 10:01:19Z** (aussi ALPHA 08:03 / 08:37) | `PROCESS_DIE last_cmd=[ "$post_delta" -le "$post_grace_i" ]` — test faux + `set -e` | **Fix shippé** runtime GO (if/fi). **Ce run n’avait PAS le fix** (pas de `STORM_HUNTER` non plus) |
| E12 | E-DUO | Après mort BETA 09:32 : ALPHA en `duo stale_state` ×20 pendant tension 2.7→12 | Scout mort + duo PID OFF → `duo_state` périmé ; hunter solo aveugle sur cluster | Relancer avec fix set -e + éventuellement `NUAGE_DUO_PID_WATCHDOG=1` |
| E13 | E-DUO | Run PM 10:40→14:40Z : **103× `duo no_trigger`** dont tension 9–13 ; **0× `STORM_HUNTER arm`** | K1 OK (latch) ; K2v1 silencieux — TTL latch mur + fallback seulement si fichier absent ; env peut ne pas suivre subshell | **K2v2 shippé** : arm live tension≥th + dir (mom/latch/radar) ; export env BETA/ALPHA ; spread floor sans exiger dir |
| E14 | E-HOLD | Run 2026-07-22 06:41–10:41Z : ALPHA **−10.56 $** (9 fills) ; hunter arm OK ; sorties surtout `shock_inversion` / `fluid_*` | K3v2 exige tension **live** ≥ th à la sortie — en fin de mèche tension retombe → hold 6–7 s | **K3v3 shippé** : `storm_hold_latched` à l’entrée ; shock/fluid bloqués tant que hold < 20 s |
| E15 | E-WATCHDOG | Run K3v3 11:44Z : ALPHA `killed_by_signal_15` puis stale 61s → relaunch #6/5 → **STOP session** ; PnL ≈ **−0.56 $** | Voir E16 | Cause racine → E16 |
| E16 | E-WATCHDOG | Preuve E15 : last CSV 14:20:52 → kill 14:21:56 (**gap 64 s**) ; `NET_RETRY rc=28` en cours ; `alpha_touch` seulement en tête de cycle → watchdog tue un ALPHA **vivant** ; puis STOP (API watchdog) → relances suicide cycle 1 | Faux positif sémantique (stale≠mort) | **Fix shippé** : skip kill si genesis/wrapper ALIVE ; pas de relance si `STOP_ALPHA` |
| E17 | E-BOOT | GO crash purge : `case *)` dans `"$(...)"` → syntax error si pgrep non vide (Ghost/Hulk match `ace777-test-day1`) | Nested `*)` ferme le `$()` | **Fix** : filtre `_filt`/`<<<` hors `$()` (GO_USINE patch E17) |

**Bilan session :** PnL ≈ **+0.99** (BETA ≈+2.10 · ALPHA ≈−1.12) · BIDIR ON · duo PID OFF · stop demandé après crash BETA.

**Correctif E10 (observabilité) :** `PROCESS_EXIT` + `PROCESS_DIE` via `GO_USINE` (toujours ON) + `scripts/patch_process_exit_log.sh` — voir `engle/PROCESS_EXIT_LOG.md`. Ne répare pas le crash ; permet de lire `last_cmd` / `rc` / signal au prochain incident.

#### Note E06 — restart et « sensibilité »

- Sur **ce** run : `NUAGE_DUO_PID_WATCHDOG=0` → **pas** de relance duo PID auto (log duo = 19 juil.).
- Ce qui a changé la « sensation » après redemande de setup : surtout **`NUAGE_BIDIR_SIDES=1`** (AUTO/BOTH), pas un mystérieux soft-knobs.
- Un restart process (manuel ou crash) **reset** quand même : compteurs cycle, soft-cooldown, fraîcheur `duo_state`, burst — effet **transitoire** (cold start), pas une nouvelle sensibilité permanente.
- Les relances duo du **19 juil.** (BETA/ALPHA morts) peuvent créer des pics `tension_stale` / `duo_wait` juste après — vrai sujet **#3 robustesse**.

---

### Template (copier pour la suite)

```
### YYYY-MM-DD — tag session
| ID | Code | Fait | Cause | Statut |
|----|------|------|-------|--------|
| Exx | E-… | … | … | ouvert / correctif / fermé |
```

---

## Lien scorecard

- Éliminer E-PROC → axe **#3**
- Éliminer E-STASE / E-SPREAD / E-DUO (mèches) → axe **#4** + `engle/PLAN_STORM_WICK.md`
- E-DIAG → discipline lecture (ce journal)
