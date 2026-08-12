# SPEC — Audit forensique des moteurs ACE777 (substitution Cursor)

## Objectif
Produire un script Python autonome (stdlib uniquement, **lecture seule**) qui prouve, à partir des données du disque, la chaîne causale suivante :

1. **10/07** : le moteur CHAMPION `37fca367` (avec barrière duo) a produit la session de référence **+29.41 USDT** (session 204206, rapport `RAPPORT_PNL_AUTO_20260710_204206.md`).
2. **12/07** : un moteur BONNET erroné `9fe9f105` (SANS barrière duo) a été restauré/mis en place (`bonnet_forme_champion/`) → session #42 en perte / ALPHA dormante.
3. **13/07** : le log `MASTER_BASE_V8_5_IMPACT_4H00_LIVE_COLOR.log` montre **712 BARRIER_TIMEOUT**, `mode=OFF radar_adj=0`, **0 FILLED ALPHA**, désalignement de cycles — le moteur actif ce jour-là a forcé la barrière en boucle.
4. **13/07 13:27:39 UTC** : trade fatal ALPHA `hunter_revenge_1.5x` qty=0.2491 BTC → **−16.84 USDT** (CSV `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv`).
5. **14/07** : ALPHA dormante (1.7% fills, PnL −13.25) + 81 lignes `mode=OFF radar_adj=0` dans `NUAGE_PROD_4H_20260714_1829Z_LIVE_COLOR.log`.
6. **Aujourd'hui** : le moteur actif `genesis_manifest.txt` = md5 `37fca367...` (le champion, scellé par l'utilisateur).

## Fichiers sources (chemins EXACTS, à lire en mode lecture seule)
- `/Users/christophe/ace777-test-day1/29$/historique/genesis/genesis_manifest.txt_ACTIF_37fca367`
- `/Users/christophe/ace777-test-day1/29$/historique/genesis/genesis_manifest.txt_BONNET_9fe9f105`
- `/Users/christophe/ace777-test-day1/29$/historique/genesis/genesis_manifest.txt.SAUVE_avant_champion_restore`
- `/Users/christophe/ace777-test-day1/29$/historique/genesis/genesis_manifest.txt.SAUVE_20260712_avant_restore_champion204206`
- `/Users/christophe/ace777-test-day1/genesis_manifest.txt` (actif)
- `/Users/christophe/ace777-test-day1/bonnet_forme_champion/` (dossier complet : LANCER.sh, REFERENCE.txt, CHECKSUMS.txt, genesis_manifest.txt)
- `/Users/christophe/ace777-test-day1/runs/MASTER_BASE_V8_5_IMPACT_4H00_LIVE_COLOR.log` (le 13/07)
- `/Users/christophe/ace777-test-day1/runs/NUAGE_PROD_4H_20260714_1829Z_LIVE_COLOR.log` (le 14/07)
- `/Users/christophe/ace777-test-day1/runs/MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv` et `..._BETA_X5.csv`
- `/Users/christophe/ace777-test-day1/runs/RAPPORT_PNL_AUTO_20260710_204206.md` (champion +29.41)
- Dossiers de preuves : `/Users/christophe/ace777-test-day1/plaintes/` et `/Users/christophe/ace777-test-day1/ERREURS_AI/` (à citer en références, ne pas analyser en profondeur)

## Ce que le script doit faire (les 5 vérifications)
Le script doit produire un rapport markdown `AUDIT_MOTEURS_CURSOR.md` avec :

### 1. Empreintes MD5 des moteurs (preuve d'identité)
Calculer le md5 de chaque fichier moteur listé ci-dessus et vérifier :
- `37fca36712d49aa8b97890c5cad5f2e6` = ACTIF_37fca367 ET `genesis_manifest.txt` actuel (le champion scellé)
- `9fe9f105...` = BONNET (différent du champion)

### 2. Diff fonctionnel entre champion et bonnet
Faire un diff texte (`difflib`) entre ACTIF_37fca367 et BONNET_9fe9f105 et **extraire automatiquement** les fonctions ajoutées/supprimées (lignes qui commencent par `< ` / `> ` dans le diff). Attendu : la fonction `duo_hunter_phase_barrier()` + son appel sont PRÉSENTS dans le champion, ABSENTS dans le bonnet. Compter le nombre de lignes de différence et les lister.

### 3. Dater la restauration du bonnet
- Lire `bonnet_forme_champion/REFERENCE.txt` et `CHECKSUMS.txt` (contenu = référence à la session 204206 ? md5 = ?)
- Lire les dates de modification (`os.path.getmtime`) des fichiers `bonnet_forme_champion/` et des `.SAUVE_*` → identifier la date de restauration (12/07 attendu)
- Vérifier si le `genesis_manifest.txt` du dossier bonnet_forme_champion a le md5 `9fe9f105` ou `37fca367`

### 4. Signature du 13/07 (le log qui hurle)
Analyser `MASTER_BASE_V8_5_IMPACT_4H00_LIVE_COLOR.log` (nettoyer les codes ANSI avant) :
- Compter `BARRIER_TIMEOUT` (attendu ~712)
- Compter `mode=OFF radar_adj=0`
- Compter les `FILLED` ALPHA vs BETA (attendu : 0 côté ALPHA)
- Compter `no_state` / `no_trigger` / `gap_guard`
- Trouver le MIN et MAX des numéros de cycle ALPHA et BETA → calculer le désalignement max (attendu ~34 cycles d'écart)
- Extraire 3 exemples de lignes BARRIER_TIMEOUT avec leur heure

### 5. Le trade fatal + la dormance (le lien avec le PnL)
Depuis `MASTER_VORTEX_V2_COLLAB_4H_ALPHA_X13_BURST13.csv` :
- Trouver le trade du 13/07 avec le pnl le plus négatif (attendu : 13:27:39, qty=0.2491, pnl −16.84)
- Afficher sa ligne complète (ts, side, entryPrice, exitPrice, qty, pnl, exitReason, msg/size_note)
Depuis `NUAGE_PROD_4H_20260714_1829Z_LIVE_COLOR.log` :
- Compter `mode=OFF radar_adj=0` (attendu 81)

## Règles strictes
1. **stdlib uniquement** — PAS de pandas, numpy, etc. (csv, hashlib, difflib, os, re, datetime)
2. **Lecture seule** — ne modifier JAMAIS les fichiers sources. Créer seulement `AUDIT_MOTEURS_CURSOR.md`.
3. **Aucun chiffre en dur dans le verdict** — tous les nombres du rapport doivent être calculés depuis les données. Les valeurs « attendues » ci-dessus ne servent qu'à valider, pas à écrire.
4. **Robuste** : si un fichier est absent, le signaler et continuer (ne pas crasher).
5. Le script s'appelle `audit_moteurs_cursor.py`. Le rapport généré s'appelle `AUDIT_MOTEURS_CURSOR.md` (dans le même dossier).
6. Console : afficher un résumé court (md5 actif, nb BARRIER_TIMEOUT, trade fatal, verdict) + le chemin du rapport.
7. Le rapport doit avoir une section « VERDICT » finale qui réponde : le moteur actif scellé est-il bien le champion `37fca367` ? Le bonnet `9fe9f105` était-il différent (sans barrière) ? La chronologie 10/07 (+29.41) → 12/07 (bonnet) → 13/07 (712 barrier_timeout, trade −16.84) → 14/07 (dormance) est-elle cohérente avec les données ?
8. Commentaires en français dans le code.
