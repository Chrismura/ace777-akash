# SPEC — cycles_terminal.py : les cycles d'ACE777 sur le terminal (jumeau cockpit)

**Date** : 2026-08-12 (tard) · **Auteur** : Buffy (superviseur) · **Codeur** : hub `code.ia`

## Objectif

Christophe observe l'état des bots **par la forme et les couleurs** des cycles qui défilent
(cockpit), pas par les chiffres. Il veut **la même vision dans le terminal** : le flux de
cycles ALPHA/BETA en continu, avec **les mêmes couleurs que le cockpit**, pour pouvoir
observer l'harmonie α/β même sans navigateur — et pouvoir rejouer un run passé pour l'audit.

Ce script est un **instrument de lecture** (comme le cockpit) : il ne décide rien,
il ne modifie rien. Lecture seule.

## Source de données

Le moteur écrit pendant chaque run :
- `~/ace777-test-day1/runs/<PREFIX>_LIVE_COLOR.log` — le flux de cycles en continu
  (déjà coloré ANSI par le moteur, mais avec une palette générique cyan/jaune/vert
  qui **ne distingue pas** alpha de beta)
- `~/ace777-test-day1/runs/<PREFIX>_ALPHA_X13_BURST13.csv` et `<PREFIX>_BETA_X5.csv`

Le script lit **le `*_LIVE_COLOR.log` le plus récent** par défaut (comme
`cockpit_mission_feed.py::find_ace_pair` : préfixe du log le plus récent, ou le plus
récent du dossier). Option `--replay <fichier>` pour rejouer un log passé.

## Couleurs EXACTES (les mêmes que le cockpit — index.html)

| Élément | Couleur | ANSI truecolor |
|---|---|---|
| Préfixe `[ALPHA_X13_BURST13]` | ambre `#f0a020` | `\x1b[38;2;240;160;32m` |
| Préfixe `[BETA_X5]` | cyan `#5ee7ff` | `\x1b[38;2;94;231;255m` |
| Lignes de cycle ALPHA (corps) | ambre atténué `#f0a020` | `38;2;240;160;32` |
| Lignes de cycle BETA (corps) | cyan `#5ee7ff` | `38;2;94;231;255` |
| `SKIP` / `SKIPPED` | gris `#8a7a55` | `38;2;138;122;85` |
| `FILLED` / `entry=` / `SELL`/`BUY` exécutés | vert acide `#7CFF6B` | `38;2;124;255;107` |
| PnL **positif** | vert acide `#7CFF6B` | `38;2;124;255;107` |
| PnL **négatif** | rouge `#ff4d4d` | `38;2;255;77;77` |
| `conf=` faible (< 0.1) | rouge `#ff4d4d` (alerte) | `38;2;255;77;77` |
| Horodatages / `#cycle` | cyan clair `#9dff7a` | `38;2;157;255;122` |
| En-têtes de run (config) | vert `#7CFF6B` | `38;2;124;255;107` |
| Reset | `\x1b[0m` | |

**Règle d'or** : les codes ANSI du log source sont **retirés puis remplacés** par cette
palette (le script re-peint, il n'hérite pas des couleurs du moteur).

## Comportement

### Mode live (défaut)
```
python3 cycles_terminal.py
```
1. Trouve le `*_LIVE_COLOR.log` le plus récent de `~/ace777-test-day1/runs/`
2. Affiche un en-tête (fichier, taille, dernière ligne lue) en vert
3. `tail -f` le fichier : chaque nouvelle ligne est **re-peinte** avec la palette :
   - Préfixe `[BETA_X5]` → cyan ; `[ALPHA_X13_BURST13]` → ambre
   - Le reste de la ligne coloré selon la règle (SKIP gris, FILLED vert, pnl +/- , conf faible rouge)
4. Toutes les **50 lignes**, une ligne de **pouls** (résumé) au format :
   ```
   ▸ α #42 · β #47 | FILLS α=2 β=3 | SKIP α=38 β=41 | PnL α=+0.19 β=+2.24 | voilure=...
   ```
   avec α en ambre, β en cyan, pnl vert/rouge selon le signe.
5. `Ctrl+C` → affiche le **bilan de session** (totaux depuis le début de la lecture) puis quitte proprement.

### Mode replay
```
python3 cycles_terminal.py --replay ~/ace777-test-day1/runs/MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log
```
- Rejoue le fichier **sans vitesse réelle** : affiche les lignes immédiatement (flux brut
  défilé), ou avec `--vitesse 0.05` (pause 50 ms par ligne) pour un défilement lisible.
- Même palette, mêmes lignes de pouls, même bilan `Ctrl+C`.

### Options
```
--replay <fichier>   rejouer un log passé
--vitesse <secondes> pause par ligne en replay (défaut 0)
--tail <n>           ne lire que les n dernières lignes en live au démarrage
--no-pulse           désactiver les lignes de pouls
--json               sortie JSON d'une ligne par cycle (pour empreinte / audit)
```

## Sortie JSON (option --json)

Une ligne JSON par cycle (le script n'écrit **jamais** dans les fichiers du moteur) :
```json
{"ts":"20:50:35","bot":"BETA_X5","cycle":1,"type":"SKIP","reason":"momentum_too_small","conf":0.3354,"tension":0.0}
{"ts":"20:51:01","bot":"BETA_X5","cycle":3,"type":"FILL","side":"SELL","pnl":0.0,"bps":0.0,"conf":0.9582}
```

## Contraintes (règles de la maison)

1. **100% stdlib Python 3** (re, sys, os, glob, json, time, datetime). Aucune
   dépendance externe. Pas de curses compliqué — flux de lignes ANSI simple.
2. **Lecture seule** : ne touche jamais aux CSV/logs du moteur, n'écrit qu'en stdout.
3. Résiste aux fichiers en cours d'écriture (lignes partielles : on attend `\n`,
   pas d'exception si le fichier n'existe pas — message clair + exit 1).
4. `python3 -m py_compile` doit passer. Pas de `|` dans les annotations de type
   (Python 3.9 du système) — utiliser `Optional[str]` à la place.
5. Fichier unique autonome `cycles_terminal.py`, ~250-350 lignes max, commentaires
   en français, en-tête docstring avec usage.
6. Le terminal doit rester **lisible à 80 colonnes** : pas de ligne plus longue que
   ~110 caractères avant couleurs (le corps `msg` des FILLED peut être long : tronquer
   le `msg` à 60 caractères avec `…`).

## Pièges connus

- Les lignes du log contiennent **déjà** des codes ANSI (`\x1b[...m`) : les retirer
  avec une regex `\x1b\[[0-9;]*m` **avant** de re-peindre, sinon couleurs imbriquées cassées.
- `conf=` peut être `conf=0.0` → à colorer en rouge (alerte). `conf=0.9582` → vert.
- Les lignes `[BETA_X5] --- ACE777 STRICT CLONE...` (en-têtes de config) → vert, pas gris.
- Les lignes `entry=` sont les FILLED : la partie `pnl=` après `|` peut être négative
  (ex. `pnl=-0.00000000`) → rouge si < 0, vert sinon. Attention `-0.0` → considérer ≥ 0.
- Le fichier peut faire plusieurs Mo : en live, ne **jamais** relire tout le fichier,
  seulement les nouvelles lignes (se souvenir de la position `f.seek(0, 2)` au départ).
