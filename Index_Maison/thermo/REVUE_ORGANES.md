# 🔎 REVUE DES ORGANES
*2026-09-30 19:49:31 UTC — lecture seule sur la maison*

**101 organes** · 46 OK · 48 jugés sur leur sortie (aucun produit déclaré) · 0 assumés (zone grise/dormant) · **1 à trancher** · 6 hors délai

## 🔴 À TRANCHER (1)
- **gitpush** — produit déclaré non résolu : .git/refs/remotes/origin/main → introuvable (StartInterval 10800s)
  - à faire : corriger le chemin au registre, ou déclarer la ligne dans revue_declares.json → produits_non_resolus

## 🔍 Candidats « produit frais, contenu peut-être figé » (0)
*Information, pas alarme : un champ « date » de jour ou un compteur donne un faux candidat. Seuls les organes dont le champ est DÉCLARÉ dans revue_declares.json (contenu_surveille) peuvent déclencher, via le chien.*
- (aucun)

## ✅ OK — produit frais ET cadence cohérente (46)
- cockpit-pont : Index_Maison/cockpit/mission.json (âge 11s / seuil 600s · KeepAlive (événementiel))
- ofi-calc : Index_Maison/data/ofi_latest.json (âge 14s / seuil 120s · StartInterval 60s)
- x402-agentic : Index_Maison/thermo/x402_agentic_etat.json (âge 527s / seuil 7200s · StartInterval 3600s)
- watchdog : /tmp/watchdog-superviseur.out.log (âge 63s / seuil 240s · StartInterval 120s)
- pont-onchain : /tmp/pont_onchain_launchd.out.log (âge 123s / seuil 3600s · StartInterval 300s) · DÉCLARÉE (produit 1800s vs déclencheur 300s)
- carte-paires : hulk-mexc/strategie/carte_fenetres_entree.json (âge 62608s / seuil 172800s · Calendrier quotidien 04:20)
- xrpl-onchain : Index_Maison/thermo/xrpl_onchain_etat.json (âge 2556s / seuil 7200s · StartInterval 3600s)
- cortana-propose-params : hulk-mexc/strategie/cortana_pilot.json (âge 126895s / seuil 172800s · Calendrier quotidien 07:45)
- paternes-btc : Index_Maison/data/paternes_btc_etat.json (âge 128553s / seuil 172800s · StartInterval 86400s)
- superviseur-process : Index_Maison/scripts/superviseur.log (âge 59s / seuil 1200s · KeepAlive (événementiel))
- short-btc : hulk-mexc/runs/short_btc_state.json (âge 107s / seuil 600s · StartInterval 300s)
- sentinelle-independante : Index_Maison/thermo/sentinelle_independante_etat.json (âge 2676s / seuil 5400s · StartInterval 3600s)
- backup-check : Index_Maison/system/backup_presence.json (âge 1570s / seuil 3600s · StartInterval 1800s)
- disjoncteur : /tmp/disjoncteur_launchd.out.log (âge 43s / seuil 120s · StartInterval 60s)
- vigie-live : Index_Maison/strategie/vigie_cooldown.json (âge 82s / seuil 7200s · KeepAlive (événementiel))
- superviseur-auto : Index_Maison/OUTBOX_OBSIDIAN/.superviseur_state.json (âge 3235s / seuil 7200s · StartInterval 3600s)
- veille-signal : /tmp/veille_signal_launchd.out.log (âge 55s / seuil 600s · StartInterval 300s)
- hub-cockpit-feed : Index_Maison/cockpit/hub.json (âge 28s / seuil 60s · StartInterval 30s)
- veille-hub : Index_Maison/VEILLE_HUB_2026-09-30.md (âge 53348s / seuil 86400s · Calendrier quotidien 07:00) · DÉCLARÉE (produit 43200s vs déclencheur 86400s)
- llm-gate-hub : /Users/christophe/prise-ia/heartbeat.json (âge 2214s / seuil 7200s · KeepAlive (événementiel))
- troupeau-inv : Index_Maison/troupeau_inv_hist.jsonl (âge 229763s / seuil 518400s · Calendrier hebdo (3 j/sem 06:00,06:00,06:00)) · DÉCLARÉE (produit 259200s vs déclencheur 201600s)
- suivi-setup-red : hulk-mexc/runs/SUIVI_SETUP_ZBCNUSDT.jsonl (âge 13106s / seuil 172800s · Calendrier quotidien 16:35)
- superviseur-l2 : runs/L2_20260930_SNAPS.csv (âge 0s / seuil 120s · KeepAlive (événementiel))
- juste-prix : Index_Maison/data/juste_prix_hist.jsonl (âge 219s / seuil 600s · StartInterval 300s)
- thermo-quotidien : Index_Maison/thermo/live.json (âge 123s / seuil 600s · StartInterval 300s)
- observer-murs : hulk-mexc/runs/murs_observations.json (âge 217s / seuil 3600s · StartInterval 1800s)
- cortana.urgent : Index_Maison/data/cortana_analysis.json (âge 55s / seuil 7200s · StartInterval 10s) · DÉCLARÉE (produit 3600s vs déclencheur 10s)
- whales : Index_Maison/data/whales_mouvements.jsonl (âge 192s / seuil 1200s · StartInterval 300s) · DÉCLARÉE (produit 600s vs déclencheur 300s)
- xrpl-gouvernance : Index_Maison/thermo/xrpl_gouv_etat.json (âge 3051s / seuil 7200s · StartInterval 3600s)
- xrpl-arbitrage : Index_Maison/thermo/xrpl_arbitrage_etat.json (âge 3s / seuil 1200s · StartInterval 10s) · DÉCLARÉE (produit 600s vs déclencheur 10s)
- archi-vivante : Index_Maison/strategie/ARCHITECTURE_VIVANTE.md (âge 187s / seuil 172800s · Calendrier quotidien 07:00)
- verdicteur-micro : Index_Maison/data/cortana_micro_score.json (âge 13s / seuil 600s · StartInterval 15s) · DÉCLARÉE (produit 300s vs déclencheur 15s)
- plancher-shadow : Index_Maison/data/plancher_confirme_etat.json (âge 19s / seuil 600s · StartInterval 300s)
- sniffer-vieux-btc : Index_Maison/data/vieux_btc_scan.json (âge 1092s / seuil 7200s · StartInterval 3600s)
- signal3-livre-ecorche : Index_Maison/data/heartbeat_signal3.json (âge 1471s / seuil 3600s · StartInterval 1800s)
- gen-cockpit-vol : Index_Maison/cockpit/vol_live.js (âge 95s / seuil 600s · StartInterval 300s)
- state-generator : Index_Maison/system/state.json (âge 64s / seuil 240s · StartInterval 120s)
- cockpit-http : /tmp/cockpit_http_17800.log (âge 23s / seuil 7200s · KeepAlive (événementiel))
- superviseur : Index_Maison/OUTBOX_OBSIDIAN/.superviseur_state.json (âge 3235s / seuil 7200s · StartInterval 3600s)
- nourrisseur-disjoncteur : /tmp/nourrisseur_disjoncteur.out.log (âge 29s / seuil 120s · StartInterval 60s)
- prise-ia : /Users/christophe/prise-ia/heartbeat.json (âge 2214s / seuil 7200s · KeepAlive (événementiel))
- controle-config : hulk-mexc/runs/CONTROLE_CONFIG.json (âge 2456s / seuil 7200s · StartInterval 3600s)
- sentinel : Index_Maison/data/sentinel_history.json (âge 267s / seuil 600s · StartInterval 300s)
- geopol : Index_Maison/indice_app/data/scores_geopol.json (âge 125731s / seuil 172800s · StartInterval 86400s)
- veilleuse : Index_Maison/thermo/VEILLEUSE.md (âge 82s / seuil 1200s · StartInterval 600s)
- cortana-feed : Index_Maison/thermo/cortana_horaire_run.log (âge 2641s / seuil 7200s · StartInterval 3600s)

## ⚪ Jugés sur leur sortie launchd (aucun produit déclaré) (48)
- veilleuse-chantiers, mirofish, veille-degradation, croisement-externe, analyste-cadence, couleur-regime-score, observatoire, catalogue, sniffer-ny, routeur-auto, jackson-hole-alarmes, verif-setup, sonde-volume-panier, satellite-aspiration, cortana-analyzer, presence-paires, veille-insti, obsidian-writer, fusibles-mesure, veille-yt, roulement-ia, gitpush-vault, scoreur-registre, discipline-quotidienne, veille-essaim-observation, rappels, bloc-privatise, chien-de-garde, sante-index, macro-tempete, sniffer-matin, heartbeats, journal-soir, hulk-watchdog, deriv-corr, dialogue-gemini, mirofish-front, queueoffres, superviseur-core, graph-cerveau, fees, couleur-regime, flux-nets, veilleuse-sizing-monte-carlo, autopilote, dms-veille, eval-offres, cpfp

