# SPEC — audit_dormance_alpha.py : pourquoi ALPHA se bloque (9-10/07 vs 14/07)

**Date** : 2026-08-12 (tard) · **Auteur** : Buffy (superviseur) · **Codeur** : hub `code.ia`

## Contexte (résultats de l'audit préliminaire déjà fait)

Christophe ressentait une dégradation du bot (la « forme » des cycles devenait moche)
sans changement de code. L'audit préliminaire a confirmé une **asymétrie α/β** :

| Métrique | Fenêtre A : 09/07 21h → 10/07 12h | Fenêtre B : 14/07 (journée) |
|---|---|---|
| Cycles ALPHA | 1 339 | 1 252 |
| Fills ALPHA | 74 (5.5%) | **21 (1.7%)** ← 3× moins |
| PnL ALPHA | **+29.52** | **−13.25** |
| Cycles BETA | 1 549 | 2 225 |
| Fills BETA | 160 (10%) | 254 (11%) |
| PnL BETA | +0.83 | +3.77 |
| Skip dominant ALPHA | radar_block (785) | radar_block (957) |

**Hypothèse** : ALPHA devient de plus en plus bloqué par ses propres portes
(radar_block, duo_wait, impulse_resonance_wait, duo_partner_pause). BETA reste sain.
La mission du script : **prouver ou réfuter** cette hypothèse et **identifier CE qui
a changé** entre les deux fenêtres (paramètres ? données ? marché ?).

## Sources de données (chemins exacts)

### Fenêtre A (9-10/07) — run MASTER_VORTEX_V2_COLLAB_4H
- `~/ace777-test-day1/runs/MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`
- `~/ace777-test-day1/runs/MASTER_VORTEX_V2_COLLAB_4H_BETA_X5.csv`
  - Colonnes : `ts,cycle,side,status,entryPrice,exitPrice,qty,bps,pnl,exitReason,holdSec,msg`
  - SKIP : `status=SKIPPED` ou `side=SKIP` ; la raison est dans la colonne `exitReason`
    (ex. `radar_block`, `duo_wait`, `impulse_resonance_wait`, `duo_partner_pause`)
  - FILLED : les autres lignes ; `pnl` = PnL du trade
- Logs de config au démarrage : `~/ace777-test-day1/runs/T1_console_2026071*.log`
  (lignes `=== V8.6 FORTRESS ===`, `=== DUO ===`, `=== RADAR ===`, `=== LLM GATE ===`,
  `CONFIG name=vide_froid_vortex_v2_collab v=...`)
- Diagnostics : `~/ace777-test-day1/runs/DIAG_ALPHA_20260709_*.md` et `20260710_*.md`
- Rapports : `~/ace777-test-day1/runs/RAPPORT_PNL_AUTO_20260709_*.md` et `20260710_*.md`

### Fenêtre B (14/07) — runs NUAGE du jour
- CSV : tous les `~/ace777-test-day1/runs/*.csv` **modifiés le 14/07** (repérer via
  `os.path.getmtime` dans la journée du 14/07), notamment :
  - `NUAGE_PROD_4H_20260714_1829Z_ALPHA_X13_BURST13.csv` / `_BETA_X5.csv` (le run 4h principal)
  - `NUAGE_BOOTTEST_1747Z/1749Z/2006Z_*`, `NUAGE_SMOKE_1447Z/1503Z/1526Z/1807Z_*`,
    `NUAGE_4H00_*`, `MASTER_BASE_V8_5_IMPACT_4H00_*`, `NUAGE_V2/V2.1_SMOKE_15M_*`
- Logs de config : `~/ace777-test-day1/runs/NUAGE_PROD_4H_20260714_1829Z_LIVE_COLOR.log`
  (début du fichier = lignes d'en-tête config), idem pour les autres `*_LIVE_COLOR.log` du 14/07

### Configs (pour comparer les paramètres)
- `~/ace777-test-day1/config_active.env` (config actuelle, version `2026-07-08-setup-ready`)
  — clés RADAR (`RADAR_MIN_CONF_BETA`, `RADAR_MIN_CONF_ALPHA`, `RADAR_MIN_MOM_BPS_*`,
  `RADAR_MAX_SPREAD_BPS`, `RADAR_GATE`, `RADAR_DIR_BPS`), DUO (`DUO_HUNTER_REQUIRE_STOP_LOSS`,
  `DUO_EVENT_TTL_SEC`), IMPULSE (`IMPULSE_RESONANCE_DT_MS`, `VOLATILITY_IMPULSE_DT_MS`)
- `~/ace777-test-day1/config_profiles/vortex_v2_collab.env` (profil de référence)
- `~/ace777-test-day1/genesis_manifest.txt.SAUVE_*` (sauvegardes des 11-12/07)
- `~/ace777-test-day1/launch_vortex_v2_collab_4h_binance.sh` (+ `.SAUVE_*`)
  — valeurs passées au moteur au démarrage

## Ce que le script doit produire

Un script unique `audit_dormance_alpha.py` (lecture seule, stdlib) qui génère un
rapport `AUDIT_DORMANCE_ALPHA.md` dans le dossier courant avec :

### 1. Métriques de forme par fenêtre (tableau comparatif)
Pour ALPHA et BETA de chaque fenêtre :
- cycles, fills, skips, taux de remplissage (fills/cycles %), PnL total
- **répartition des skips par raison** (comptage par `exitReason`) avec %
- cadence : cycles par minute + nombre de plages de silence (≥ 5 min sans aucun cycle)
- **taux de skips ALPHA/BETA** (asymétrie : ratio skips_alpha / skips_beta)

### 2. Détection du point de bascule (le plus important)
Dans la fenêtre A, calculer le taux de remplissage ALPHA **par tranche de 1 h** et
afficher la série chronologique (ex. `21h: 4.2% | 22h: 3.1% | ...`). Repérer si la
baisse se fait progressivement ou brutalement, et à quelle heure elle commence.
Faire de même pour la fenêtre B (par tranche de 1 h).

### 3. Comparaison des paramètres (config)
Extraire de chaque source de config les valeurs RADAR/DUO/IMPULSE/RESONANCE et
afficher un tableau **paramètre → valeur fenêtre A → valeur fenêtre B → delta**.
Si une valeur diffère : c'est un suspect majeur (mettre `<<< CHANGEMENT` en face).
Si toutes les valeurs sont identiques : le script doit le dire explicitement
(« aucun paramètre n'a changé entre A et B » → le coupable n'est pas la config).

### 4. Lecture du marché (contexte)
Pour chaque fenêtre, depuis les lignes FILLED des CSV : prix moyens d'entrée/sortie
(BTC), nombre de fills longs vs courts (`side` BUY/SELL), et la taille moyenne des
mouvements (bps moyens). Objectif : voir si le marché était plus calme/plus violent
dans une fenêtre (un marché trop calme = radar_block systématique).

## Contraintes (règles de la maison)

1. **100% stdlib Python 3** (csv, glob, os, re, datetime, collections). Pas de dépendance.
2. **Lecture seule absolue** : ne modifie JAMAIS les CSV/logs du moteur. Écrit
   uniquement `AUDIT_DORMANCE_ALPHA.md` (avec `atomic write` : tmp + rename).
3. `python3 -m py_compile` doit passer. Pas de `|` dans les annotations de type
   (Python 3.9) — `Optional[str]` à la place.
4. Fichier unique autonome, ~250-350 lignes, commentaires en français, docstring d'usage.
5. Robuste aux fichiers manquants : si une source n'existe pas, le script le signale
   dans le rapport et continue avec ce qui existe (jamais de crash).
6. Les timestamps CSV sont ISO UTC (`2026-07-08T20:50:35Z`) — parser proprement.
7. Rapports lisibles en markdown avec tableaux, pour Christophe (non-expert) :
   vulgariser les sections (« ce que ça veut dire » en 1 ligne sous chaque tableau).

## Pièges connus

- Les CSV du 14/07 sont **multiples** (boottests + smokes + prod) : il faut TOUS les
  agréger pour la fenêtre B, mais uniquement les lignes avec `ts` dans le 14/07 UTC
  (certains CSV contiennent des lignes d'autres jours).
- `exitReason` peut être vide ou `?` sur certaines lignes : compter dans une
  catégorie `inconnu` au lieu de crasher.
- Le `pnl` des SKIP est vide/0 : ne compter le PnL que sur les FILLED.
- Les logs `T1_console_*` et `*_LIVE_COLOR.log` contiennent des codes ANSI :
  les retirer avant de parser la config.
- La fenêtre A commence le 09/07 21:00 UTC et finit le 10/07 12:00 UTC (15 h).
  La fenêtre B = tout le 14/07 UTC (0h00 → 23h59).
- Les fichiers de config `.SAUVE_*` peuvent avoir des valeurs différentes : prendre
  la plus proche de chaque date (pour A : manifest du 11-12/07 ou config_active ;
  pour B : les en-têtes des logs LIVE_COLOR du 14/07 qui montrent la config RÉELLE
  utilisée ce jour-là — c'est la source la plus fiable).
