# Protocole Ghost — watchdog Hulk (paper + veille)

Garde-fou **léger** pendant que Christophe dort / s’absente.  
Ne touche **pas** ACE NUAGE / genesis.

> Nom officiel : **Ghost** (pas « fantôme » — évite la confusion avec un parasite ACE).

## Quoi

Toutes les **30 minutes** :
1. Vérifier `paper_diprip.py` (piste A)
2. Vérifier `digest_watch.py --live` (piste B / yeux Qwen)
3. Si mort **et** pas de STOP volontaire → **relance**
4. Log → `runs/WATCHDOG_GHOST.log`

Script : `scripts/watchdog_hulk_ghost.sh`  
(compat : `scripts/watchdog_hulk_nuit.sh` → même script)

## STOP volontaires (pas de relance)

| Fichier | Effet |
|---------|--------|
| `STOP_PAPER` | paper arrêté, Ghost ne relance pas |
| `STOP_DIGEST` | veille arrêtée, Ghost ne relance pas |

## Armer (session Cursor / agent)

```bash
# check immédiat
./scripts/watchdog_hulk_ghost.sh

# loop agent 30m (sentinel technique AGENT_LOOP_TICK_hulk_nuit — ID Cursor inchangé)
# — l’agent Cursor surveille le tick et relance le script
```

Ou hors agent (crontab / terminal) :

```bash
cd /Users/christophe/ace777-test-day1/hulk-mexc
while true; do
  ./scripts/watchdog_hulk_ghost.sh
  sleep 1800
done
```

## Arrêt Ghost

- Dire à l’agent : « stop loop » / « stop Ghost »
- Ou tuer le PID du `while true; sleep 1800`

Paper / veille peuvent continuer à tourner.

## Périmètre

- **IN** : Hulk paper + digest veille  
- **OUT** : ACE777, GO_USINE, genesis champion  
