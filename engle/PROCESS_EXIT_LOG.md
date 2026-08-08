# PROCESS_EXIT / PROCESS_DIE — raison de mort BETA/ALPHA

**Date :** 2026-07-20  
**Scorecard :** axe #3 robustesse (E10)  
**Pourquoi :** crash scout sans message → impossible de savoir *pourquoi*. Le `wait || true` masquait même le code de sortie (toujours 0).

## Ce qui est ajouté (champion disque intact)

Via `GO_USINE_NUAGE.sh` (toujours ON, pas de flag) :

| Ligne | Où | Contenu |
|-------|-----|---------|
| `PROCESS_DIE \| … last_cmd=… ec=…` | trap ERR/EXIT dans preamble `bash -s` | **Dernière commande** qui a tué le process (`set -e`) |
| `PROCESS_EXIT unit=… how=… why=… rc=…` | fin de `run_unit` | Code / signal après `wait` (rc réel, plus masqué) |

Fichiers :
- `runs/PROCESS_EXIT.log` (append)
- `runs/<TAG>_LIVE_COLOR.log`
- si rc≠0 : copie `runs/.<TAG>_<UNIT>.raw.EXIT.rcN.log`

## Comment lire

```bash
# Après un STOP / incident (recommandé — hygiène)
./scripts/hygiene_apres_arret.sh
# → imprime WHY_ARRET=… (obligatoire)
# → runs/LAST_STOP_REASON.txt
# → runs/RAPPORT_ERREURS_DERNIER.md
# → engle/journal/ERR_SESSION_DERNIER.md

# Ou rapport seul :
./scripts/rapport_erreurs_session.sh
```

**E18 (2026-07-23) :** chaque pose de STOP doit laisser une trace :
- timer → `runs/STOP_REASON.txt` `reason=timer_nominal`
- duo max relaunch → `reason=duo_max_relaunch_*`
- sinon le rapport déduit `stop_files_early_writer_unknown`

Fichiers :
- `runs/PROCESS_EXIT.log` (append)
- `runs/STOP_REASON.txt` / `runs/LAST_STOP_REASON.txt`
- `runs/<TAG>_LIVE_COLOR.log`
- si rc≠0 : copie `runs/.<TAG>_<UNIT>.raw.EXIT.rcN.log`
