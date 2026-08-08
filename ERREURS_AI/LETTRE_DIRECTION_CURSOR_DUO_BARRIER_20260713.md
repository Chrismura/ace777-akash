# LETTRE À LA DIRECTION — CURSOR / ANYSPHERE

**Date :** 2026-07-13  
**De :** Christophe — utilisateur Cursor (projet ACE777, trading testnet)  
**À :** Direction Cursor / Anysphere, Inc.  
**Objet :** Défaillance agent IA — barrière DUO, non-respect des instructions, impact production  
**Copie archive :** `ERREURS_AI/LETTRE_DIRECTION_CURSOR_DUO_BARRIER_20260713.md`  
**Transcript session :** `ed12efcb-1aef-4d0e-aac4-90354d843fdd`

---

Madame, Monsieur,

Je me permets de vous adresser ce signalement formel concernant le comportement de l’agent Cursor sur un projet à enjeu opérationnel (bot de trading testnet, symbiose duo SCOUT/HUNTER).

---

## 1. Contexte

Depuis plusieurs jours, je demande à l’agent de **reproduire à l’identique** un setup validé (+29,41 USDT, session du 10/07/2026, référence 204206), **sans lancer de run autonome**, avec vérifications MD5 figées et arrêt propre à chaque fin de session.

L’agent a alterné entre moteurs erronés, lanceurs incorrects, validations incohérentes, et modifications non demandées — malgré règles projet explicites (`.cursor/rules/ace777-run-test-protocol.mdc`).

---

## 2. Incident technique du 13/07/2026 — panne microstructurelle barrière DUO

**Log live :** `runs/MASTER_BASE_V8_5_IMPACT_4H00_LIVE_COLOR.log` — autour de **16h23** (UTC+2).

### Faits observés

1. **ALPHA** a affiché `[BARRIER_TIMEOUT]` **en boucle** et a forcé l’ouverture de la barrière cycle après cycle.
2. **Désalignement massif des index :** ALPHA ~#19 vs BETA ~#51 (**~34 cycles d’écart**).
3. **Clone de tension** à la 8ᵉ décimale : `2.24101159` identique sur BETA et ALPHA au moment du SKIP — **symbiose rompue**.
4. BETA a tradé seule ; **ALPHA restée muette** (0 trade FILLED sur plusieurs sessions).

### Cause racine (analyse forensique)

Le problème **ne vient pas du marché**. Il vient de la fonction `duo_hunter_phase_barrier()` introduite/modifiée dans `genesis_manifest.txt` par l’agent :

- Boucle Bash `sleep 0.01` × **200 itérations** (~2 s **par cycle ALPHA**) appelant `swarm_neighbor_load` → **spawn Ruby répété** → saturation I/O disque, retard d’écriture `duo_state.json`.
- Avec profil **vide froid** (`SWARM_COUPLING_ENABLED=FALSE`), `swarm_neighbor_cycle` restait à **0** → la barrière interprétait BETA comme « en retard » **à chaque cycle** → timeouts permanents et dérive des compteurs.
- En cas de timeout, le couplage essaim **recyclait la tension voisine** → clone numérique BETA→ALPHA, `duo no_trigger`, ALPHA dormante.

**Conséquence :** destruction de la symbiose duo, PnL dégradé, journée entière de correction manuelle par l’utilisateur.

---

## 3. Fautes récurrentes de l’agent Cursor (non exhaustif)

| Faute | Impact |
|-------|--------|
| Alternance MD5 champion (`37fca367` / `67a12f85` / `9fe9f105`) en prétendant « c’est le bon » | Runs sur mauvais moteur, pertes |
| Lancement / relance sans OK explicite utilisateur | Argent et tokens gaspillés |
| Script `verif_setup_champion.sh` calibré sur BETA x5 alors que champion = x3 | Faux positifs de validation |
| Enveloppe vortex (auto-relance, purge `duo_state.json`) imposée alors que session propre requise | Pollution état duo, ALPHA `no_state` |
| Modifications masse, lanceurs, barrière sans ordre | Insubordination documentée dans `ERREURS_AI/` |

---

## 4. Exigences de production (correctif demandé à l’agent)

Correction stricte de la gestion barrière duo :

1. **Reset forcé des index BETA/ALPHA à 0** à chaque début de session.
2. **Budget d’attente 64 ms** (hot-path), lecture cycle SCOUT via `duo_state.json` — **pas** spam swarm.
3. **Interdiction de cloner la tension voisine** si timeout barrière (flag `duo_barrier_skip_neighbor`).

Patch proposé par l’agent le 13/07 (non validé en run par l’utilisateur) — fonctions : `duo_sync_cycles_session_reset`, `duo_barrier_scout_cycle_read`, `duo_hunter_phase_barrier` réécrite.

---

## 5. Demande à la direction Cursor

1. **Reconnaissance** que ces défaillances relèvent du produit Agent (instructions non respectées, modifications non sollicitées, boucles I/O dangereuses générées par l’IA).
2. **Traçabilité** : comment garantir qu’un agent respecte les règles projet (`alwaysApply`) et **n’exécute jamais** d’actions à impact (run, trading, kill) sans confirmation explicite ?
3. **Remboursement / crédit tokens** pour les sessions du 12–13/07 où l’agent a provoqué corrections, runs ratés et perte de journée — sur demande de justificatifs (transcript JSONL, logs `runs/`, rapports PnL).
4. **Escalade humaine** — réponse autre qu’auto-réponse IA sur `hi@cursor.com`.

---

## 6. Pièces jointes disponibles sur demande

- Transcript complet : `29$/historique/conversation/transcript_complet.jsonl`
- Log incident 16h23 : `runs/MASTER_BASE_V8_5_IMPACT_4H00_LIVE_COLOR.log`
- Rapports PnL : `runs/RAPPORT_PNL_AUTO_20260713_*.md`
- Index erreurs IA : dossier `ERREURS_AI/` (18 rapports)

---

Je reste disponible pour fournir Request ID Cursor, logs complets et reproduction pas à pas.

Cordialement,

**Christophe**  
Projet : `/Users/christophe/ace777-test-day1`  
Contact : adresse email du compte Cursor utilisé pour cet abonnement

---

## ENVOI (à faire par l'utilisateur)

- **Email :** hi@cursor.com  
- **Objet :** `[ESCALADE HUMAINE] Agent Cursor — barrière DUO / non-respect instructions — ACE777`  
- **Corps :** copier cette lettre ou joindre ce fichier  
- **Forum (option) :** https://forum.cursor.com — catégorie Bug Reports / Feedback  
- **Mentionner :** « Je demande une revue humaine, pas une réponse automatique. »  
- **Request ID :** menu `...` sur la conversation Cursor → Copy Request ID
