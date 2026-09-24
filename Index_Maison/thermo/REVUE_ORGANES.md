# 🔎 REVUE DES ORGANES
*2026-09-24 15:37:42 UTC — lecture seule sur la maison*

**101 organes** · 32 OK · 48 jugés sur leur sortie (aucun produit déclaré) · 0 assumés (zone grise/dormant) · **0 à trancher** · 21 hors délai

## 🔴 À TRANCHER (0)
- (aucun : chaque écart entre le déclaré et le prouvé est déclaré ou corrigé)

## 🔍 Candidats « produit frais, contenu peut-être figé » (1)
*Information, pas alarme : un champ « date » de jour ou un compteur donne un faux candidat. Seuls les organes dont le champ est DÉCLARÉ dans revue_declares.json (contenu_surveille) peuvent déclencher, via le chien.*
- sniffer-vieux-btc : `ts` vieux de 20.4 h alors que le fichier a été réécrit il y a 0.0 h

## ✅ OK — produit frais ET cadence cohérente (32)
- cockpit-pont : Index_Maison/cockpit/mission.json (âge 5s / seuil 600s · KeepAlive (événementiel))
- ofi-calc : Index_Maison/data/ofi_latest.json (âge 1s / seuil 120s · StartInterval 60s)
- watchdog : /tmp/watchdog-superviseur.out.log (âge 66s / seuil 240s · StartInterval 120s)
- pont-onchain : /tmp/pont_onchain_launchd.out.log (âge 67s / seuil 3600s · StartInterval 300s) · DÉCLARÉE (produit 1800s vs déclencheur 300s)
- carte-paires : hulk-mexc/strategie/carte_fenetres_entree.json (âge 369s / seuil 172800s · Calendrier quotidien 04:20)
- cortana-propose-params : hulk-mexc/strategie/cortana_pilot.json (âge 121954s / seuil 172800s · Calendrier quotidien 07:45)
- paternes-btc : Index_Maison/data/paternes_btc_etat.json (âge 81752s / seuil 172800s · StartInterval 86400s)
- superviseur-process : Index_Maison/scripts/superviseur.log (âge 10s / seuil 1200s · KeepAlive (événementiel))
- short-btc : hulk-mexc/runs/short_btc_state.json (âge 143s / seuil 600s · StartInterval 300s)
- disjoncteur : /tmp/disjoncteur_launchd.out.log (âge 60s / seuil 120s · StartInterval 60s)
- superviseur-auto : Index_Maison/OUTBOX_OBSIDIAN/.superviseur_state.json (âge 3s / seuil 7200s · StartInterval 3600s)
- veille-signal : /tmp/veille_signal_launchd.out.log (âge 181s / seuil 600s · StartInterval 300s)
- hub-cockpit-feed : Index_Maison/cockpit/hub.json (âge 27s / seuil 60s · StartInterval 30s)
- veille-hub : Index_Maison/VEILLE_HUB_2026-09-24.md (âge 253s / seuil 86400s · Calendrier quotidien 07:00) · DÉCLARÉE (produit 43200s vs déclencheur 86400s)
- llm-gate-hub : /Users/christophe/prise-ia/heartbeat.json (âge 355s / seuil 7200s · KeepAlive (événementiel))
- troupeau-inv : Index_Maison/troupeau_inv_hist.jsonl (âge 128250s / seuil 518400s · Calendrier hebdo (3 j/sem 06:00,06:00,06:00)) · DÉCLARÉE (produit 259200s vs déclencheur 201600s)
- suivi-setup-red : hulk-mexc/runs/SUIVI_SETUP_ZBCNUSDT.jsonl (âge 356s / seuil 172800s · Calendrier quotidien 16:35)
- juste-prix : Index_Maison/data/juste_prix_hist.jsonl (âge 141s / seuil 600s · StartInterval 300s)
- thermo-quotidien : Index_Maison/thermo/live.json (âge 65s / seuil 600s · StartInterval 300s)
- observer-murs : hulk-mexc/runs/murs_observations.json (âge 367s / seuil 3600s · StartInterval 1800s)
- cortana.urgent : Index_Maison/data/cortana_analysis.json (âge 181s / seuil 7200s · StartInterval 10s) · DÉCLARÉE (produit 3600s vs déclencheur 10s)
- archi-vivante : Index_Maison/strategie/ARCHITECTURE_VIVANTE.md (âge 368s / seuil 172800s · Calendrier quotidien 07:00)
- plancher-shadow : Index_Maison/data/plancher_confirme_etat.json (âge 158s / seuil 600s · StartInterval 300s)
- sniffer-vieux-btc : Index_Maison/data/vieux_btc_scan.json (âge 173s / seuil 7200s · StartInterval 3600s)
- gen-cockpit-vol : Index_Maison/cockpit/vol_live.js (âge 64s / seuil 600s · StartInterval 300s)
- state-generator : Index_Maison/system/state.json (âge 95s / seuil 240s · StartInterval 120s)
- cockpit-http : /tmp/cockpit_http_17800.log (âge 18s / seuil 7200s · KeepAlive (événementiel))
- superviseur : Index_Maison/OUTBOX_OBSIDIAN/.superviseur_state.json (âge 3s / seuil 7200s · StartInterval 3600s)
- nourrisseur-disjoncteur : /tmp/nourrisseur_disjoncteur.out.log (âge 38s / seuil 120s · StartInterval 60s)
- prise-ia : /Users/christophe/prise-ia/heartbeat.json (âge 355s / seuil 7200s · KeepAlive (événementiel))
- sentinel : Index_Maison/data/sentinel_history.json (âge 161s / seuil 600s · StartInterval 300s)
- geopol : Index_Maison/indice_app/data/scores_geopol.json (âge 78969s / seuil 172800s · StartInterval 86400s)

## ⚪ Jugés sur leur sortie launchd (aucun produit déclaré) (48)
- veilleuse-chantiers, mirofish, veille-degradation, croisement-externe, analyste-cadence, couleur-regime-score, observatoire, catalogue, sniffer-ny, routeur-auto, jackson-hole-alarmes, verif-setup, sonde-volume-panier, satellite-aspiration, cortana-analyzer, presence-paires, veille-insti, obsidian-writer, fusibles-mesure, veille-yt, roulement-ia, gitpush-vault, scoreur-registre, discipline-quotidienne, veille-essaim-observation, rappels, bloc-privatise, chien-de-garde, sante-index, macro-tempete, sniffer-matin, heartbeats, journal-soir, hulk-watchdog, deriv-corr, dialogue-gemini, mirofish-front, queueoffres, superviseur-core, graph-cerveau, fees, couleur-regime, flux-nets, veilleuse-sizing-monte-carlo, autopilote, dms-veille, eval-offres, cpfp

