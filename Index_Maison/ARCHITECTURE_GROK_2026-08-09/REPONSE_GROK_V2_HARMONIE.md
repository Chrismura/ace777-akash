# REPONSE GROK v2 — HARMONIE INTER-ETAGES (via Puter Grok (gratuit)) — 10/08/2026

## Brief envoye (faits mesures)

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

## Reponse Grok

**Spec V2 DELTA – ACE777 (mise à jour du 10/08)**

### 1. Contrat d’harmonie inter-étages (version finale)

Les 4 feeds constituent la colonne vertébrale. Tous respectent le même schéma minimal obligatoire :

```json
{
  "produit_par": "nom_du_script_ou_service",
  "updated_at": "2025-08-10T14:32:17Z",
  "payload": { ... }
}
```

**Règles par feed :**

- **mission.json**  
  Cadence : écriture toutes les 30 s (ou sur événement trading).  
  Taille max : 8 Ko.  
  Lecteurs autorisés : mon_cockpit.py, cockpit-http, superviseur (lecture optionnelle).  
  L’IA ne lit pas directement ce feed.

- **cortana_feed.json**  
  Cadence : écriture sur événement vocal (max 1 écriture / 10 s).  
  Taille max : 4 Ko.  
  Lecteurs autorisés : mon_cockpit.py, cortana_brief, superviseur (lecture optionnelle).

- **live.json**  
  Cadence : écriture toutes les 5 s (données trading live).  
  Taille max : 12 Ko.  
  Lecteurs autorisés : mon_cockpit.py, superviseur (lecture optionnelle).

- **state.json** (nouveau – à créer)  
  Emplacement : `Index_Maison/system/state.json`  
  Cadence : écriture toutes les 5 minutes par `system_state_generator.py` (ou sur cycle superviseur).  
  Taille max : 3 Ko (strict).  
  Lecteurs : **superviseur unique** (lecture obligatoire à chaque cycle 30 min) + IA (requêtes ciblées).  
  Rôle : mémoire mécanique agrégée des 3 autres feeds + état des 13 services + présence des dossiers hors zone.

**Décision superviseur :**  
Le superviseur lit **uniquement state.json** à chaque cycle de 30 min. Il ne lit pas directement mission.json, cortana_feed.json ni live.json. Ces trois feeds sont agrégés dans state.json par `system_state_generator.py`. Cela évite les doublons et les conflits.

### 2. Sort de Mirofish (règle définitive)

**Décision actée : option (c)**  
Mirofish reste désactivé et **sort de la liste des 13 services surveillés**.

Règle exacte à implémenter dans le superviseur :

```bash
# Règle superviseur (à ajouter dans com.ace777.superviseur-unique)
if service_name.startswith("com.ace777.mirofish"):
    skip_check = true
    log = "Mirofish désactivé le 10/08 – ignoré"
```

- Les deux plists restent dans `DESACTIVES_2026-08-10/`.  
- Le dossier `~/mirofis/` (1 Go) est conservé en backup uniquement.  
- Aucune ligne de `autopilote.sh` ne doit plus référencer Mirofish après la mise à jour de la spec.

### 3. Périmètre vocal (confirmé et protégé)

Le vocal reste **intact** et ne fait l’objet d’aucune fusion.

**Services à conserver dans les 13 :**
- `com.ace777.cortana.horaire`
- `com.ace777.cortana.urgent`

**Scripts à préserver (9) :**
- cortana_voice.py
- cortana_brief.py
- cortana_analyse.py
- cortana_thermo.py
- cortana_horaire.sh
- cortana_urgent_poll.sh
- cortana_watch.py
- cortana_mute.py
- cortana_cockpit_bridge.py

Le cœur Rust (`crypto-voice-assistant-core`) reste **hors périmètre** du setup des 3 étages. Il est uniquement sauvegardé (4,4 Go). Aucun script du setup ne doit pointer vers `launch_cortana.sh` ni `config/app.toml`.

Le feed `cortana_feed.json` reste la seule interface entre la couche vocale et le cockpit.

### 4. Dossiers hors zone et backups (intégration)

Les 21 Go de backups vérifiés (checksums + comptage) sont maintenant des références sûres. Le superviseur peut les surveiller.

**Ajouts dans la spec :**
- Le superviseur ajoute un contrôle de présence (pas de contenu) sur les 5 dossiers hors zone à chaque cycle 30 min.
- Le cockpit reçoit un nouveau contrôle d’intégrité backup (taille totale + présence des 5 dossiers) affiché dans `mission.json` et `state.json`.

Dossiers concernés :
- mirofis (1 Go)
- crypto-voice-assistant-core (4,4 Go)
- ACE777_ARCHIVES_BRUTES_DONNEES (94 Mo)
- Assistant_Vocal_HORS_VAULT (681 Mo)
- Obsidian_BACKUPS_HORS_VAULT (14 Go)

### Changements DELTA par rapport à REPONSE_GROK_3ETAGES.md

- Ajout du contrat d’harmonie + schéma feed obligatoire.
- Création de `state.json` et de `system_state_generator.py`.
- Passage de 27 → 13 services avec règle Mirofish explicite.
- Protection explicite des 2 services cortana + 9 scripts.
- Ajout du contrôle backup dans cockpit et superviseur.
- state.json devient la seule source de vérité pour le superviseur.

### 3 premières étapes concrètes (ordre d’exécution)

1. **Créer state.json et son générateur**  
   Créer le dossier `Index_Maison/system/` et le script `system_state_generator.py` (v2) qui agrège les 3 feeds + état services + présence dossiers hors zone.  
   Signature : Grok / Architecte ACE777 – 10/08

2. **Mettre à jour le superviseur unique**  
   Ajouter la règle Mirofish + lecture exclusive de `state.json` + contrôle présence des 5 dossiers hors zone.  
   Signature : Grok / Architecte ACE777 – 10/08

3. **Intégrer le contrôle backup dans le cockpit**  
   Ajouter dans `mon_cockpit.py` (et `mission.json`) un bloc qui vérifie taille + présence des dossiers hors zone et l’écrit dans `state.json`.  
   Signature : Grok / Architecte ACE777 – 10/08

Ces trois étapes doivent être réalisées avant toute réduction à 13 services. Une fois terminées, le setup V2 sera mécaniquement complet.
