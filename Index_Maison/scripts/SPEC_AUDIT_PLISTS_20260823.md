# SPEC AUDIT — Correctifs plists & boucles de destruction (23/08/2026)

## Contexte
Le système ACE777 tourne via 55 jobs launchd (`~/Library/LaunchAgents/com.ace777.*.plist`).
Audit du 23/08 : découverte d'une **boucle de destruction** — le plist `com.ace777.observatoire`
était structurellement cassé : `KeepAlive=true` + `RunAtLoad=true` **dupliqués** (dont un
exemplaire DANS le dict `StartCalendarInterval`). Résultat : launchd relançait le script en
**boucle infinie** (toutes les ~2 min au lieu de 1×/jour), qui réécrivait `providers.json` à
chaque cycle, **écrasant les correctifs** et **gonflant le fichier** (368 Ko → 377 Ko),
avec **987 rollbacks en cascade** dans le log.

## Correctifs appliqués

### A. 31 plists corrigés : retrait du `KeepAlive` parasite
Règle : un script **one-shot** (passe unique, cadencé par `StartInterval` ou
`StartCalendarInterval`) NE doit PAS avoir `KeepAlive` (sinon boucle infinie).
Les 31 plists suivants ont eu `KeepAlive` retiré (intervalle conservé) :
- SI (StartInterval) : autopilote(900s), backup-check(1800s), bloc-privatise(120s),
  cortana-feed(3600s), cpfp(600s), dms-veille(60s), fees(300s), gitpush-vault(10800s),
  gitpush(10800s), heartbeats(60s), hub-cockpit-feed(30s), hulk-watchdog(120s),
  macro-tempete(60s), pont-onchain(300s), rappels(60s), sante-index(300s),
  state-generator(120s), superviseur-core(900s), veille-degradation(60s),
  veilleuse-confrontation(21600s), veilleuse-sizing-monte-carlo(21600s),
  veilleuse(600s), whales(300s)
- SCI (StartCalendarInterval) : archi-vivante(7:00), catalogue(10:00),
  couleur-regime(8:05,15:55), graph-cerveau(11:30), journal-soir(20:53),
  veille-yt(9:15,18:15), veilleuse-chantiers(9:00), verif-setup(12:00)

### B. 1 plist XML cassé réparé : `com.ace777.cortana.urgent`
XML invalide (commentaire contenant `--` interdit en XML) → fichier illisible par launchd.
Réécrit proprement : `StartInterval=10s` conservé, `KeepAlive` retiré.

### C. Déjà corrigé plus tôt : `com.ace777.observatoire`
Structure cassée réparée : `KeepAlive`/`RunAtLoad` dupliqués retirés, `StartCalendarInterval
11:00` seul conservé.

### D. Modèles hub corrigés
- `openai/gpt-oss-20b:free` supprimé d'OpenRouter (404) → remplacé par `z-ai/glm-5.2:free`
- **OrcaRouter intégré** : provider `orca` (`orcarouter/free`), clé `ORCA_API_KEY` dans `.env`,
  testé via le hub (5,3 s, réponse correcte)

## Jobs conservés volontairement avec KeepAlive (daemons légitimes)
cockpit-http, cockpit-pont, llm-gate-hub, prise-ia, superviseur-process, vigie-live,
run-setupA-4h, run-vortex-96h (KeepAlive={'SuccessfulExit': False}), superviseur-core
(boucle while interne), watchdogs internes.

## Question pour la famille et le codeur
1. La règle « one-shot → pas de KeepAlive » est-elle correcte et suffisante ?
2. Y a-t-il un risque de casse (job qui ne se relance plus, cadence perdue) ?
3. Faut-il un mécanisme de détection automatique de ce pattern (KeepAlive+intervalle) dans
   `veille_degradation.py` pour que ça ne puisse plus jamais arriver en silence ?
4. Vérifier que le retrait de KeepAlive sur superviseur-core (SI=900s) ne casse pas la
   relance du superviseur (daemon while true dans superviseur_core.sh — KeepAlive retiré
   car one-shot ? À CONFIRMER : le script a une boucle `while` interne, donc KeepAlive
   était inoffensif mais SI est le vrai cadenceur. Y a-t-il un risque que le superviseur
   ne soit plus relancé après crash ?)
