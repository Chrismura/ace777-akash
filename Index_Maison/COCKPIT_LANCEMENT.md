# Cockpit — commande de lancement

**Validé 31 juil. 2026** · stack : LaunchAgents + pywebview 1ˢ · Brave `--app` filet.

## Lancer (depuis n’importe où)

```bash
bash ~/ace777-test-day1/Index_Maison/scripts/cockpit_up.sh
```

⚠️ Pas depuis `~` avec un chemin relatif (`Index_Maison/...`) → `No such file`.  
Toujours le chemin **absolu** ci-dessus, ou :

```bash
cd ~/ace777-test-day1 && bash Index_Maison/scripts/cockpit_up.sh
```

## Variantes

```bash
# Daemons seulement (pont :17777 + HTTP :17800)
bash ~/ace777-test-day1/Index_Maison/scripts/cockpit_up.sh --daemons

# Fenêtre seule (si PONT/HTTP déjà ON)
bash ~/ace777-test-day1/Index_Maison/scripts/open_cockpit_app.sh

# Réparer / installer LaunchAgents
bash ~/ace777-test-day1/Index_Maison/scripts/install_cockpit_daemons.sh
```

## Rappels

| | |
|--|--|
| Recharger page | **⌘R** (F5 = dictation micro) |
| Fenêtre | pywebview native · sinon Brave `--app` |
| Jamais | Safari · `file://` |
| Si `ERR_CONNECTION_REFUSED` | relancer `cockpit_up.sh` |

## Onglets cockpit

OPS · THERMO · BOARD · **GRAPH** (synapses connexions) · VOL

Canon : [[INDEX_COMMANDES]] §5b · [[JOURNAL_COCKPIT]] · [[PLAN_DE_VOL]]
