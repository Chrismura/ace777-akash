# 🔎 REVUE DES ORGANES
*2026-10-21 16:21:23 UTC — lecture seule sur la maison*

**101 organes** · 42 OK · 48 jugés sur leur sortie (aucun produit déclaré) · 0 assumés (zone grise/dormant) · **0 à trancher** · 11 hors délai

## 🔴 À TRANCHER (0)
- (aucun : chaque écart entre le déclaré et le prouvé est déclaré ou corrigé)

## 🔍 Candidats « produit frais, contenu peut-être figé » (2)
*Information, pas alarme : un champ « date » de jour ou un compteur donne un faux candidat. Seuls les organes dont le champ est DÉCLARÉ dans revue_declares.json (contenu_surveille) peuvent déclencher, via le chien.*
- juste-prix : `ts_iso` vieux de 0.2 h alors que le fichier a été réécrit il y a 0.2 h
- thermo-quotidien : `ts` vieux de 0.5 h alors que le fichier a été réécrit il y a 0.0 h

## ✅ OK — produit frais ET cadence cohérente (42)
- cockpit-pont : Index_Maison/cockpit/mission.json (âge 67s / seuil 600s · KeepAlive (événementiel))
- ofi-calc : Index_Maison/data/ofi_latest.json (âge 15s / seuil 120s · StartInterval 60s)
- x402-agentic : Index_Maison/thermo/x402_agentic_etat.json (âge 1667s / seuil 7200s · StartInterval 3600s)
- watchdog : /tmp/watchdog-superviseur.out.log (âge 83s / seuil 240s · StartInterval 120s)
- pont-onchain : /tmp/pont_onchain_launchd.out.log (âge 63s / seuil 3600s · StartInterval 300s) · DÉCLARÉE (produit 1800s vs déclencheur 300s)
- carte-paires : hulk-mexc/strategie/carte_fenetres_entree.json (âge 50484s / seuil 172800s · Calendrier quotidien 04:20)
- xrpl-onchain : Index_Maison/thermo/xrpl_onchain_etat.json (âge 1753s / seuil 7200s · StartInterval 3600s)
- cortana-propose-params : hulk-mexc/strategie/cortana_pilot.json (âge 38181s / seuil 172800s · Calendrier quotidien 07:45)
- paternes-btc : Index_Maison/data/paternes_btc_etat.json (âge 92317s / seuil 172800s · StartInterval 86400s)
- superviseur-process : Index_Maison/scripts/superviseur.log (âge 49s / seuil 1200s · KeepAlive (événementiel))
- short-btc : hulk-mexc/runs/short_btc_state.json (âge 0s / seuil 600s · StartInterval 300s)
- sentinelle-independante : Index_Maison/thermo/sentinelle_independante_etat.json (âge 2283s / seuil 5400s · StartInterval 3600s)
- backup-check : Index_Maison/system/backup_presence.json (âge 373s / seuil 3600s · StartInterval 1800s)
- disjoncteur : /tmp/disjoncteur_launchd.out.log (âge 56s / seuil 120s · StartInterval 60s)
- superviseur-auto : Index_Maison/OUTBOX_OBSIDIAN/.superviseur_state.json (âge 3091s / seuil 7200s · StartInterval 3600s)
- veille-signal : /tmp/veille_signal_launchd.out.log (âge 121s / seuil 600s · StartInterval 300s)
- hub-cockpit-feed : Index_Maison/cockpit/hub.json (âge 4s / seuil 60s · StartInterval 30s)
- veille-hub : Index_Maison/VEILLE_HUB_2026-10-21.md (âge 24145s / seuil 86400s · Calendrier quotidien 07:00) · DÉCLARÉE (produit 43200s vs déclencheur 86400s)
- llm-gate-hub : /Users/christophe/prise-ia/heartbeat.json (âge 3483s / seuil 7200s · KeepAlive (événementiel))
- troupeau-inv : Index_Maison/troupeau_inv_hist.jsonl (âge 44475s / seuil 518400s · Calendrier hebdo (3 j/sem 06:00,06:00,06:00)) · DÉCLARÉE (produit 259200s vs déclencheur 201600s)
- suivi-setup-red : hulk-mexc/runs/SUIVI_SETUP_ZBCNUSDT.jsonl (âge 4366s / seuil 172800s · Calendrier quotidien 16:35)
- thermo-quotidien : Index_Maison/thermo/live.json (âge 63s / seuil 600s · StartInterval 300s)
- observer-murs : hulk-mexc/runs/murs_observations.json (âge 1977s / seuil 3600s · StartInterval 1800s)
- cortana.urgent : Index_Maison/data/cortana_analysis.json (âge 131s / seuil 7200s · StartInterval 10s) · DÉCLARÉE (produit 3600s vs déclencheur 10s)
- cycle-edel : hulk-mexc/runs/CYCLE_EDEL_SUIVI.jsonl (âge 2284s / seuil 43200s · StartInterval 21600s)
- archi-vivante : Index_Maison/strategie/ARCHITECTURE_VIVANTE.md (âge 31860s / seuil 172800s · Calendrier quotidien 07:00)
- plancher-shadow : Index_Maison/data/plancher_confirme_etat.json (âge 78s / seuil 600s · StartInterval 300s)
- signal3-livre-ecorche : Index_Maison/data/heartbeat_signal3.json (âge 217s / seuil 3600s · StartInterval 1800s)
- veilleuse-confrontation : Index_Maison/VEILLE_CONFRONTATION_ACE_HULK.md (âge 2268s / seuil 43200s · StartInterval 21600s)
- gen-cockpit-vol : Index_Maison/cockpit/vol_live.js (âge 39s / seuil 600s · StartInterval 300s)
- state-generator : Index_Maison/system/state.json (âge 71s / seuil 240s · StartInterval 120s)
- cockpit-http : /tmp/cockpit_http_17800.log (âge 7s / seuil 7200s · KeepAlive (événementiel))
- superviseur : Index_Maison/OUTBOX_OBSIDIAN/.superviseur_state.json (âge 3091s / seuil 7200s · StartInterval 3600s)
- nourrisseur-disjoncteur : /tmp/nourrisseur_disjoncteur.out.log (âge 20s / seuil 120s · StartInterval 60s)
- prise-ia : /Users/christophe/prise-ia/heartbeat.json (âge 3483s / seuil 7200s · KeepAlive (événementiel))
- controle-config : hulk-mexc/runs/CONTROLE_CONFIG.json (âge 2063s / seuil 7200s · StartInterval 3600s)
- sentinel : Index_Maison/data/sentinel_history.json (âge 373s / seuil 600s · StartInterval 300s)
- geopol : Index_Maison/indice_app/data/scores_geopol.json (âge 1437s / seuil 172800s · StartInterval 86400s)
- veilleuse : Index_Maison/thermo/VEILLEUSE.md (âge 401s / seuil 1200s · StartInterval 600s)
- croisements-indices : Index_Maison/data/croisements_indices_etat.json (âge 2320s / seuil 43200s · StartInterval 21600s)
- cortana-feed : Index_Maison/thermo/cortana_horaire_run.log (âge 198s / seuil 7200s · StartInterval 3600s)
- divergence : hulk-mexc/runs/DIVERGENCE_SUIVI.jsonl (âge 2256s / seuil 43200s · StartInterval 21600s)

## ⚪ Jugés sur leur sortie launchd (aucun produit déclaré) (48)
- veilleuse-chantiers, mirofish, veille-degradation, croisement-externe, analyste-cadence, couleur-regime-score, observatoire, catalogue, sniffer-ny, routeur-auto, jackson-hole-alarmes, verif-setup, sonde-volume-panier, satellite-aspiration, cortana-analyzer, presence-paires, veille-insti, obsidian-writer, fusibles-mesure, veille-yt, roulement-ia, gitpush-vault, scoreur-registre, discipline-quotidienne, veille-essaim-observation, rappels, bloc-privatise, chien-de-garde, sante-index, macro-tempete, sniffer-matin, heartbeats, journal-soir, hulk-watchdog, deriv-corr, dialogue-gemini, mirofish-front, queueoffres, superviseur-core, graph-cerveau, fees, couleur-regime, flux-nets, veilleuse-sizing-monte-carlo, autopilote, dms-veille, eval-offres, cpfp

