# BRIEF SPEC V2 soumis a la famille (loi 1quinquies) — 10/08

SPEC V2 — SETUP DES 3 ETAGES ACE777 (avec harmonie inter-étages)

CONTEXTE : Mac 8 Go, hub local 11435 (9 providers gratuits), 29 services launchd
(27 chargés + 2 mirofish désactivés). Objectif : passer à 13 services en 3 étages
(Infrastructure / Orchestration / Agents+Mémoire+Observabilité), superviseur
unique, mode probatoire C6 (1 action autonome/jour), 6 conditions famille C1-C6,
loi 1quinquies (la SPEC doit être validée par le JUGE avant tout code).

Les 4 décisions de la spec V2 (après audit de complétude mécanique du 10/08) :

1. CONTRAT D'HARMONIE INTER-ÉTAGES — la colonne vertébrale :
   Les 3 étages communiquent par des FEEDS JSON temps réel, schéma standard
   obligatoire : {"produit_par", "updated_at", "payload"}.
   - mission.json      (Trading->Système)  : écrit par cockpit_mission_feed.py,
     cadence 30 s, max 8 Ko, lu par mon_cockpit/cockpit-http.
   - cortana_feed.json (Vocal->Système)    : écrit par cortana_thermo.py,
     cadence événement (max 1/10 s), max 4 Ko, lu par mon_cockpit/cortana_brief.
   - live.json         (Trading->Système)  : cadence 5 s, max 12 Ko.
   - state.json        (NOUVEAU, Système)  : écrit par system_state_generator.py
     toutes les 5 min, max 3 Ko, lu OBLIGATOIREMENT par le superviseur unique
     à chaque cycle 30 min + requêtes ciblées IA (2-3 Ko).
   DÉCISION : le superviseur lit UNIQUEMENT state.json (qui agrège les 3 autres
   feeds + état des 13 services + présence des dossiers hors zone). Jamais de
   lecture directe des autres feeds par le superviseur -> pas de doublon/conflit.

2. SORT DE MIROFISH — décision actée option (c) :
   Mirofish reste DÉSACTIVÉ et sort de la liste des services surveillés.
   Règle exacte : si service_name.startswith("com.ace777.mirofish") -> skip_check
   + log "Mirofish désactivé le 10/08 – ignoré". Plists préservés dans
   DESACTIVES_2026-08-10/, code ~/mirofis/ (1 Go) en backup uniquement.
   autopilote.sh ne doit plus référencer Mirofish après mise à jour.

3. PÉRIMÈTRE VOCAL — PROTÉGÉ INTÉGRALEMENT (aucune fusion) :
   Services conservés : com.ace777.cortana.horaire + com.ace777.cortana.urgent.
   9 scripts préservés : cortana_voice, brief, analyse, thermo, horaire.sh,
   urgent_poll.sh, watch, mute, cockpit_bridge.
   Cœur Rust ~/crypto-voice-assistant-core/ (4,4 Go) = HORS périmètre du setup,
   uniquement sauvegardé. cortana_feed.json = seule interface vocal<->cockpit.

4. DOSSIERS HORS ZONE + BACKUP (intégration) :
   Backup 3 étages = 21 Go, vérifié (checksums + comptage) : systeme/ (270 Mo),
   hub/ (792 Ko), vault/ (35 Mo), launchd/ (132 Ko), hors_zones/ (4,4 Go + 14 Go
   Obsidian_BACKUPS_HORS_VAULT). Le superviseur ajoute un contrôle de PRÉSENCE
   (pas de contenu) des 5 dossiers hors zone à chaque cycle 30 min. Le cockpit
   affiche un contrôle d'intégrité backup (taille + présence) dans state.json.

CHANGEMENTS DELTA vs spec v1 : contrat d'harmonie + schéma feed, création
state.json + system_state_generator.py, 27->13 services avec règle Mirofish,
protection explicite cortana, contrôle backup, state.json = seule source de
vérité du superviseur.

3 PREMIÈRES ÉTAPES (ordre) :
  E1. Créer state.json + system_state_generator.py (agrège 3 feeds + état).
  E2. Mettre à jour superviseur unique (règle Mirofish + lecture state.json).
  E3. Intégrer contrôle backup dans cockpit (mon_cockpit.py + mission.json).


QUESTIONS À LA FAMILLE (validation de la SPEC avant exécution, loi 1quinquies) :
1. Le contrat d'harmonie inter-étages (4 feeds, schéma standard, superviseur qui
   lit UNIQUEMENT state.json agrégé) est-il sain et suffisant pour que les
   3 étages communiquent en harmonie ? Y a-t-il un risque de perte d'information
   ou de latence ?
2. La décision Mirofish (option c : désactivé, sorti de la liste surveillée,
   règle skip_check) est-elle la bonne ? Faut-il au contraire le réactiver ?
3. Le périmètre vocal (2 services + 9 scripts protégés, cœur Rust hors
   périmètre) est-il correctement protégé dans la spec ?
4. L'intégration du contrôle backup (présence 5 dossiers hors zone + taille)
   dans le superviseur et le cockpit est-elle utile ou superflue ?
5. Verdict final sur la SPEC V2 : GO / GO AVEC RESERVES / NON
   (avec 1 phrase de justification + les réserves concrètes à intégrer).
