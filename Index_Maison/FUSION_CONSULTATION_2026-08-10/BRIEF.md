# BRIEF consultation avant fusion — 10/08

## Etat reel

CONTEXTE : Systeme ACE777 - Mac 8 Go, hub local 11435 (9 providers gratuits),
29 services launchd. Setup des 3 étages en cours, loi 1quinquies respectée.
DÉJÀ FAIT et validé par la famille (GO unanime GEMINI + JUGE) :
- SPEC V2.1 : contrat d'harmonie inter-étages (4 feeds JSON + state.json =
  seule source de vérité du superviseur), sort de Mirofish (option c, membre
  équipe en pause budgetaire), périmètre vocal protégé (2 services + 9 scripts),
  contrôle backup léger.
- E1 : system_state_generator.py v2.1 (status + feed_hash + atomic, zéro prose).
- E2 : plists chargés (state-generator 120 s + backup-check 1800 s), state.json
  en continu, backup_light_check.sh (présence 30 min + tailles du -sk 6 h).
- E3 : README_MIROFISH.md (ré-activation documentée) + _check_rust_version
  (non-fatale) dans cortana_cockpit_bridge.py — code produit par le hub.

PROCHAINE ÉTAPE : la FUSION des services 27 -> 13 (superviseur unique,
fusion/suppression des services redondants de monitoring/tri).

ÉTAT RÉEL MESURÉ (brut, à l'instant) :
- Services chargés : com.ace777.analyse-usage, com.ace777.analyste-cadence, com.ace777.autopilote, com.ace777.backup-check, com.ace777.brief-matin, com.ace777.catalogue, com.ace777.cockpit-http, com.ace777.cockpit-pont, com.ace777.cortana.horaire, com.ace777.cortana.urgent, com.ace777.eval-offres, com.ace777.gitpush, com.ace777.gitpush-vault, com.ace777.graph-cerveau, com.ace777.heartbeat, com.ace777.journal-soir, com.ace777.observatoire, com.ace777.prise-ia, com.ace777.propose-ameliorations, com.ace777.pulse-sous-loeil, com.ace777.qwen-btc, com.ace777.qwen-elabore, com.ace777.rotation-logs, com.ace777.state-generator, com.ace777.superviseur, com.ace777.surveillance-quotas, com.ace777.veille-hub, com.ace777.verif-setup, com.ace777.vigie
- Vivants : com.ace777.cockpit-http, com.ace777.cockpit-pont, com.ace777.cortana.horaire, com.ace777.prise-ia
- Hub : {"status": "ok", "providers": 9}
- state.json : STALE 29 5
- RAM : The system has 8589934592 (524288 pages with a page size of 16384).

QUESTIONS (avant d'exécuter la fusion — on veut améliorer/simplifier AVANT de casser) :
1. Y a-t-il des AMÉLIORATIONS à faire MAINTENANT (avant la fusion) qui
   simplifieraient la fusion elle-même ? (ex. : retirer un service devenu
   inutile, fusionner 2 services évidents, préparer le terrain)
2. Comment SIMPLIFIER la fusion ? (ordre des désactivations, quoi garder
   comme colonne vertébrale, quoi fusionner en premier)
3. Quels sont les 3 RISQUES principaux de la fusion (et comment les éviter) ?
4. Le superviseur unique doit remplacer/absorber quels services en priorité ?
5. Verdict : la fusion est-elle prête à être conçue, ou faut-il d'abord
   améliorer quelque chose ? (AMELIORER D'ABORD / PRET POUR CONCEPTION / AUTRE)


## Questions

CONTEXTE : Systeme ACE777 - Mac 8 Go, hub local 11435 (9 providers gratuits),
29 services launchd. Setup des 3 étages en cours, loi 1quinquies respectée.
DÉJÀ FAIT et validé par la famille (GO unanime GEMINI + JUGE) :
- SPEC V2.1 : contrat d'harmonie inter-étages (4 feeds JSON + state.json =
  seule source de vérité du superviseur), sort de Mirofish (option c, membre
  équipe en pause budgetaire), périmètre vocal protégé (2 services + 9 scripts),
  contrôle backup léger.
- E1 : system_state_generator.py v2.1 (status + feed_hash + atomic, zéro prose).
- E2 : plists chargés (state-generator 120 s + backup-check 1800 s), state.json
  en continu, backup_light_check.sh (présence 30 min + tailles du -sk 6 h).
- E3 : README_MIROFISH.md (ré-activation documentée) + _check_rust_version
  (non-fatale) dans cortana_cockpit_bridge.py — code produit par le hub.

PROCHAINE ÉTAPE : la FUSION des services 27 -> 13 (superviseur unique,
fusion/suppression des services redondants de monitoring/tri).

ÉTAT RÉEL MESURÉ (brut, à l'instant) :
- Services chargés : com.ace777.analyse-usage, com.ace777.analyste-cadence, com.ace777.autopilote, com.ace777.backup-check, com.ace777.brief-matin, com.ace777.catalogue, com.ace777.cockpit-http, com.ace777.cockpit-pont, com.ace777.cortana.horaire, com.ace777.cortana.urgent, com.ace777.eval-offres, com.ace777.gitpush, com.ace777.gitpush-vault, com.ace777.graph-cerveau, com.ace777.heartbeat, com.ace777.journal-soir, com.ace777.observatoire, com.ace777.prise-ia, com.ace777.propose-ameliorations, com.ace777.pulse-sous-loeil, com.ace777.qwen-btc, com.ace777.qwen-elabore, com.ace777.rotation-logs, com.ace777.state-generator, com.ace777.superviseur, com.ace777.surveillance-quotas, com.ace777.veille-hub, com.ace777.verif-setup, com.ace777.vigie
- Vivants : com.ace777.cockpit-http, com.ace777.cockpit-pont, com.ace777.cortana.horaire, com.ace777.prise-ia
- Hub : {"status": "ok", "providers": 9}
- state.json : STALE 29 5
- RAM : The system has 8589934592 (524288 pages with a page size of 16384).

QUESTIONS (avant d'exécuter la fusion — on veut améliorer/simplifier AVANT de casser) :
1. Y a-t-il des AMÉLIORATIONS à faire MAINTENANT (avant la fusion) qui
   simplifieraient la fusion elle-même ? (ex. : retirer un service devenu
   inutile, fusionner 2 services évidents, préparer le terrain)
2. Comment SIMPLIFIER la fusion ? (ordre des désactivations, quoi garder
   comme colonne vertébrale, quoi fusionner en premier)
3. Quels sont les 3 RISQUES principaux de la fusion (et comment les éviter) ?
4. Le superviseur unique doit remplacer/absorber quels services en priorité ?
5. Verdict : la fusion est-elle prête à être conçue, ou faut-il d'abord
   améliorer quelque chose ? (AMELIORER D'ABORD / PRET POUR CONCEPTION / AUTRE)

