# SPEC — Étape 5 : actions sûres et autonomes (18/08/2026)

> Soumise au CODEUR (task `code.ia`) + FAMILLE/JUGE (tasks `audit.protocol` / `mission` / `signets.juge`) pour validation, comme demandé par Christophe (« pas plomber, fais valider »).

## Contexte (l'existant, à réutiliser — pas à recréer)

- `sante_index.py` : vérifie chaque chaîne de bout en bout (baleines, HULK, LIVE, CPFP, SÉCURITÉ, SAISON), écrit `thermo/sante_index.json` + `cockpit/sante_live.js`, **détecte les anomalies et ALERTE à la voix** (anti-empilement, auto-extinction au retour au calme). **Mais il ne RÉPARE pas.**
- `surveiller_whales.py` : détecte déjà les **GROS MOUVEMENTS** (bloc ≥1000 BTC + fragmentation ≥500 BTC) → `whales_scan_latest.json` → `live.json.onchain` → ADA + Cortana.
- `alarme.json` : alerte « prix » existante (variation, volume x3…).
- **Aucun mécanisme de RAPPEL de tâches** n'existe.

## Objectif — 3 livrables bornés

### 5a. AUTO-RÉPARATION d'un index (chaîne de monitoring)
Quand `sante_index.py` trouve une chaîne cassée, réparer de façon **sûre et bornée** :

- **Whitelist de services MONITORING uniquement** (jamais le moteur de trading ACE/HULK, jamais aucun ordre) :
  `com.ace777.whales`, `com.ace777.pont-onchain`, `com.ace777.cpfp`, `com.ace777.veilleuse`, `com.ace777.hub-cockpit-feed`, `com.ace777.cockpit-pont`, `com.ace777.saison`.
- **Action** = `launchctl kickstart -k gui/$UID/<label>` (relancer le process mort) **ou** relancer le script du feed figé.
- **Garde-fous NON négociables** :
  1. Kill-switch actif (`STOP` / `STOP_ALL`) → **jamais** réparer.
  2. Maintenance prévue (`MAINTENANCE_PREVUE` future) → **jamais** réparer.
  3. Max **3 tentatives / chaîne / 24 h** (anti-boucle) ; au-delà → alerte humaine, ne plus insister.
  4. **Chaque action tracée** (append-only) + 1 ligne mémoire collab (AGORA).
  5. Hub down → **aucune** réparation aveugle.
  6. Cooldown 10 min entre 2 réparations globales.
- Alerter l'humain (voix) **avant et après** chaque réparation.

### 5b. GROS MOUVEMENT (vérifier, PAS reconstruire)
Vérifier que `surveiller_whales.py` → `live.json.onchain` → ADA + `alarme.json` déclenchent bien **alerte vocale + affichage cockpit** quand un gros mouvement survient. Si un maillon est débranché, le **brancher** (pas réécrire la détection).

### 5c. RAPPELS de tâches
- « Cortana, rappelle-moi `<tâche>` à `<heure>` » → stocké (JSON append, TTL).
- Un vérificateur périodique (stdlib) lit les rappels échus → **alerte vocale** + affichage cockpit.
- Commandes : **ajouter / lister / supprimer**.
- Garde-fous : pas de rappel sans heure ; plafond de rappels actifs.

## Contraintes générales (non négociables)
- Python **stdlib** uniquement, bash 3.2 macOS, Mac M1 8 Go.
- Lecture seule partout, sauf l'action de réparation bornée.
- **Jamais** d'ordre de trading. **Jamais** de GO implicite.
- Écriture atomique + kill-switch respecté partout.
- Maker ≠ checker : la réparation est bornée, tracée, et le GO humain reste souverain.

## Livrables attendus du codeur
1. Patch `sante_index.py` (ou nouveau module `auto_reparer.py` appelé par lui) pour la réparation bornée.
2. Vérification 5b (le maillon gros mouvement est-il branché ?).
3. `rappels.py` (ajouter/lister/supprimer/vérifier) + hook dans le pont cockpit (commandes chat).
4. Preuve de logique + garde-fous, rien d'autre.
