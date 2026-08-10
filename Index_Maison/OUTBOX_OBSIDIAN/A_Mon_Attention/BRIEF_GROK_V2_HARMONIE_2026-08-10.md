# BRIEF GROK v2 — HARMONIE INTER-ETAGES (complement setup 3 etages) — 10/08/2026

> Genere mecaniquement apres audit de completude. 4 decouvertes a integrer.

## Faits mesures

  - hub : {"status": "ok", "providers": 9}
- **feeds** :
  - **mission.json** :
      - producteur : cockpit_mission_feed.py (ligne 450)
      - emplacement : Index_Maison/cockpit/mission.json
      - consommateur : mon_cockpit.py (lignes 91, 138) + cockpit-http
      - sens : Trading -> Systeme (feed cockpit)
      - note : REECRIT EN CONTINU meme bots arretes (anomalie deja signalee a Grok)
  - **cortana_feed.json** :
      - producteur : cortana_thermo.py (lance par com.ace777.cortana.urgent)
      - emplacement : Index_Maison/thermo/cortana_feed.json
      - consommateur : mon_cockpit.py (ligne 152) + cortana_brief
      - sens : Vocal -> Systeme (feed cockpit)
      - note : memmoire mecanique de la couche vocale
  - **live.json** :
      - producteur : (thermo)
      - emplacement : Index_Maison/thermo/live.json
      - consommateur : mon_cockpit.py (ligne 151)
      - sens : Trading -> Systeme
      - note : donnees live
  - **state.json (A CREER)** :
      - producteur : system_state_generator.py (concu par Grok, v2)
      - emplacement : (a definir — couche systeme)
      - consommateur : superviseur unique + IA (query ciblee 2-3 Ko)
      - sens : Systeme -> superviseur/IA
      - note : la 3e memoire mecanique, celle qui manque
- **mirofish** :
    - plists : DESACTIVES le 10/08 (dossier DESACTIVES_2026-08-10)
    - mais_autopilote_surveille_encore : autopilote.sh ligne 19 : com.ace777.mirofish + com.ace777.mirofish-front
    - code_source : ~/mirofis/ (1 Go, backend Python 35 110 fichiers + frontend) — maintenant sauvegarde
    - decision_a_acter : retirer de la liste surveillee OU reactiver — la spec doit trancher
- **vocal** :
    - services : cortana.horaire (rituel) + cortana.urgent (poll 10 s)
    - scripts_9 : cortana_voice.py, cortana_brief.py, cortana_analyse.py, cortana_thermo.py, cortana_horaire.sh, cortana_urgent_poll.sh, cortana_watch.py, cortana_mute.py, cortana_cockpit_bridge.py
    - coeur_rust : ~/crypto-voice-assistant-core/ (4,4 Go, launch_cortana.sh, config/app.toml) - PROJET PARALLELE, le vocal actif utilise edge-tts
    - feed : cortana_feed.json (voir contrat d'harmonie)
    - a_preserver : la spec 13 services ne doit pas fusionner/casser le vocal
- **hors_zone** :
    - mirofis : 1 Go - code Mirofish
    - crypto-voice-assistant-core : 4,4 Go - coeur vocal Rust
    - ACE777_ARCHIVES_BRUTES_DONNEES : 94 Mo - donnees historiques
    - Assistant_Vocal_HORS_VAULT : 681 Mo - donnees vocales
    - Obsidian_BACKUPS_HORS_VAULT : 14 Go - backups vault (ajoutes aussi)
    - total_backup_3etages : 21 Go - tout est sauvegarde et verifie (checksums + comptage)
    - consequence : le superviseur peut reference ces dossiers SANS risque de perte

## Question envoyee a Grok

Systeme ACE777 - Mac 8 Go, hub local port 11435, 9 providers gratuits, 29 services launchd (27 charges + 2 mirofish desactives), setup des 3 etages en cours de conception (tu as deja repondu REPONSE_GROK_3ETAGES.md : superviseur unique com.ace777.superviseur-unique, 27->13 services, cockpit, mode probatoire C6, loi 1quinquies).

NOUVEAU : un audit de completude mecanique (10/08) a passe en revue TOUT le systeme reel (plists, scripts, dossiers du home) et a decouvert 4 points ABSENTS de ta spec et de l'etat des lieux. Avant de valider le setup, il faut les integrer :

## 1. CONTRAT D'HARMONIE INTER-ETAGES (LE POINT CRUCIAL)
Les 3 etages communiquent deja par des FEEDS JSON temps reel. C'est la colonne vertebrale de l'harmonie. Voici les faits mesures :

- **mission.json** :
    - producteur : cockpit_mission_feed.py (ligne 450)
    - emplacement : Index_Maison/cockpit/mission.json
    - consommateur : mon_cockpit.py (lignes 91, 138) + cockpit-http
    - sens : Trading -> Systeme (feed cockpit)
    - note : REECRIT EN CONTINU meme bots arretes (anomalie deja signalee a Grok)
- **cortana_feed.json** :
    - producteur : cortana_thermo.py (lance par com.ace777.cortana.urgent)
    - emplacement : Index_Maison/thermo/cortana_feed.json
    - consommateur : mon_cockpit.py (ligne 152) + cortana_brief
    - sens : Vocal -> Systeme (feed cockpit)
    - note : memmoire mecanique de la couche vocale
- **live.json** :
    - producteur : (thermo)
    - emplacement : Index_Maison/thermo/live.json
    - consommateur : mon_cockpit.py (ligne 151)
    - sens : Trading -> Systeme
    - note : donnees live
- **state.json (A CREER)** :
    - producteur : system_state_generator.py (concu par Grok, v2)
    - emplacement : (a definir — couche systeme)
    - consommateur : superviseur unique + IA (query ciblee 2-3 Ko)
    - sens : Systeme -> superviseur/IA
    - note : la 3e memoire mecanique, celle qui manque

QUESTION : valider ce contrat comme fondation du setup. Pour chaque feed : cadence d'ecriture recommandee, taille max, qui doit le lire (superviseur, cockpit, IA), et comment state.json s'y insere sans doublon ni conflit. Le superviseur unique doit-il LIRE mission.json + cortana_feed.json + live.json a chaque cycle (30 min) ou se limiter a state.json ? Definis le schema type d'un feed (champs obligatoires : produit_par, updated_at, payload).

## 2. SORT DE MIROFISH (decision a acter dans la spec)
  - plists : DESACTIVES le 10/08 (dossier DESACTIVES_2026-08-10)
  - mais_autopilote_surveille_encore : autopilote.sh ligne 19 : com.ace777.mirofish + com.ace777.mirofish-front
  - code_source : ~/mirofis/ (1 Go, backend Python 35 110 fichiers + frontend) — maintenant sauvegarde
  - decision_a_acter : retirer de la liste surveillee OU reactiver — la spec doit trancher

QUESTION : dans ta spec 13 services, Mirofish est invisible. Or l'autopilote le surveille encore. Recommande-tu : (a) le retirer de la liste surveillee (desactive = arret assume), (b) le reactiver, (c) le garder desactive MAIS hors liste, avec une règle dans le superviseur pour eviter les fausses alertes ? Donne la regle exacte.

## 3. PERIMETRE VOCAL (a preserver tel quel)
  - services : cortana.horaire (rituel) + cortana.urgent (poll 10 s)
  - scripts_9 : cortana_voice.py, cortana_brief.py, cortana_analyse.py, cortana_thermo.py, cortana_horaire.sh, cortana_urgent_poll.sh, cortana_watch.py, cortana_mute.py, cortana_cockpit_bridge.py
  - coeur_rust : ~/crypto-voice-assistant-core/ (4,4 Go, launch_cortana.sh, config/app.toml) - PROJET PARALLELE, le vocal actif utilise edge-tts
  - feed : cortana_feed.json (voir contrat d'harmonie)
  - a_preserver : la spec 13 services ne doit pas fusionner/casser le vocal

QUESTION : le vocal = 2 services + 9 scripts + feed. Ta spec dit '4 agents metier' sans les nommer. Liste les services que le setup doit CONSERVER pour le vocal, et confirme qu'aucune fusion ne doit toucher cortana.horaire/cortana.urgent ni les scripts cortana_*. Le coeur Rust crypto-voice-assistant-core (projet parallele) doit-il rester hors perimetre (juste sauvegarde) ?

## 4. DOSSIERS HORS ZONE (maintenant sauvegardes — references sures)
  - mirofis : 1 Go - code Mirofish
  - crypto-voice-assistant-core : 4,4 Go - coeur vocal Rust
  - ACE777_ARCHIVES_BRUTES_DONNEES : 94 Mo - donnees historiques
  - Assistant_Vocal_HORS_VAULT : 681 Mo - donnees vocales
  - Obsidian_BACKUPS_HORS_VAULT : 14 Go - backups vault (ajoutes aussi)
  - total_backup_3etages : 21 Go - tout est sauvegarde et verifie (checksums + comptage)
  - consequence : le superviseur peut reference ces dossiers SANS risque de perte

QUESTION : le backup 3 etages fait 21 Go, verifie (checksums + comptage). Cela change-t-il quelque chose au setup ? (ex : le superviseur peut surveiller la presence de ces dossiers, le ROLLBACK peut les restaurer). Doit-on ajouter au cockpit un controle d'integrite du backup (taille, presence) ?

## DEMANDE FINALE
Integre ces 4 points dans ta spec des 3 etages : donne la spec V2 mise a jour (changements DELTA par rapport a REPONSE_GROK_3ETAGES.md), le contrat d'harmonie final, la regle Mirofish exacte, le perimetre vocal confirme, et les 3 premieres etapes concretes dans l'ordre avec signatures. Reponds en francais, structure, concret, actionnable.

Hub /health a l'envoi : {"status": "ok", "providers": 9}

