# SPEC — CORRECTIF VIGIE / SUPERVISEUR — 2026-08-16

> **Symptôme** : 13 instances de `vigie_live.py` accumulées en 7 h → `analyste.strategie`
> martelé sur nvidia (50-400 s/appel) → 429 partout → hub saturé.
> **Cause racine** (diagnostic Buffy, preuves ps/log) : `ws_recv()` bloque sans timeout
> sur décrochage WebSocket silencieux → heartbeat mort → `superviseur.sh` relance
> SANS tuer l'ancienne vigie → accumulation. Chaque vigie a son cooldown en mémoire → 13× l'analyste.
> **Doctrine** : stdlib uniquement, kill-switch, écriture atomique, idempotent, réversible.

---

## Livrables (codeur)

### 1. `Index_Maison/scripts/vigie_live.py` — MODIF CRITIQUE (WebSocket timeout)

- **Problème** : `ws_recv(ws)` bloque indéfiniment sur une connexion half-open (TCP mort
  sans FIN). Aucune exception → le `try/except` de reconnexion ne se déclenche jamais.
- **Correctif** : mettre un **timeout de lecture** sur le socket WebSocket (ex.
  `ws.settimeout(30)` avant la boucle, ou un timeout équivalent sur `ws_recv`). En cas de
  timeout/décrochage → lever une exception → la reconnexion EXISTANTE (try/except,
  `sleep 5`) s'occupe du reste. **Ne pas réécrire la logique de reconnexion, elle est déjà bonne.**
- **Heartbeat de vie** : en plus des trades, écrire/mettre à jour `strategie/journal_radar.log`
  (ou un `touch` léger) à intervalle régulier (ex. toutes les 30-60 s) même sans trade,
  pour que le superviseur voie la vigie vivante en marché calme.

### 2. `Index_Maison/scripts/superviseur.sh` — MODIF (kill avant relance)

- **Problème** : `restart_process` fait `nohup python3 ... &` sans tuer l'ancien process.
- **Correctif** : dans `restart_process`, AVANT le `nohup`, tuer l'ancien process :
  - `vigie` → `pkill -f "vigie_live.py"` puis `sleep 1`
  - `hub` → `pkill -f "hub_prise_ia.py"` puis `sleep 1`
  - `cockpit` → `pkill -f "cockpit_http_server.py"` puis `sleep 1`
- **Garantie** : `pkill` ne doit JAMAIS matcher `superviseur.sh` lui-même (patterns ciblés
  sur les noms de scripts Python uniquement).

### 3. `Index_Maison/scripts/vigie_live.py` — MODIF (cooldown analyste partagé)

- **Problème** : `data.cooldown_until` est en mémoire (`SymbolData`). 13 instances = 13
  cooldowns indépendants = 13× l'analyste sur la même alerte.
- **Correctif (défense en profondeur)** : persister le cooldown dans un fichier partagé,
  ex. `strategie/vigie_cooldown.json` (`{symbole: cooldown_until}`), lu/écrit en écriture
  atomique. Même si une 2e vigie tournait, elle verrait le cooldown de la 1ʳᵉ.

### 4. (OPTIONNEL) `strategie/journal_radar.log` — rotation

- Le fichier fait **161 Mo** et grossit (1 ligne par trade, même bruit). Ajouter une
  rotation/troncature simple (ex. garder les N dernières lignes, ou purger si > 20 Mo).

---

## NE PAS toucher
- `analyste.py` (le cooldown se règle côté vigie, pas côté analyste).
- Le hub `prise-ia` (hors périmètre — chantier hub à part).
- `paper_diprip.py` (moteur Hulk), les runs ACE.

---

## Format de réponse exigé
- Pour chaque fichier : bloc ```python ou ```bash complet (ou ```diff EXACT avant→après pour les MODIFS).
- Une section « NOTES » finale : choix faits, valeur du timeout retenue, comportement du heartbeat.
- Réponds en français, factuel.
