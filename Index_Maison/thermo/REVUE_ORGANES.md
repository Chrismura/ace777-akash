# 🔎 REVUE DES ORGANES
*2026-10-12 06:51:34 UTC — lecture seule sur la maison*

**101 organes** · 40 OK · 48 jugés sur leur sortie (aucun produit déclaré) · 0 assumés (zone grise/dormant) · **0 à trancher** · 13 hors délai

## 🔴 À TRANCHER (0)
- (aucun : chaque écart entre le déclaré et le prouvé est déclaré ou corrigé)

## 🔍 Candidats « produit frais, contenu peut-être figé » (1)
*Information, pas alarme : un champ « date » de jour ou un compteur donne un faux candidat. Seuls les organes dont le champ est DÉCLARÉ dans revue_declares.json (contenu_surveille) peuvent déclencher, via le chien.*
- juste-prix : `ts_iso` vieux de 1.4 h alors que le fichier a été réécrit il y a 1.4 h

## ✅ OK — produit frais ET cadence cohérente (40)
- cockpit-pont : Index_Maison/cockpit/mission.json (âge 39s / seuil 600s · KeepAlive (événementiel))
- ofi-calc : Index_Maison/data/ofi_latest.json (âge 12s / seuil 120s · StartInterval 60s)
- x402-agentic : Index_Maison/thermo/x402_agentic_etat.json (âge 5909s / seuil 7200s · StartInterval 3600s)
- watchdog : /tmp/watchdog-superviseur.out.log (âge 42s / seuil 240s · StartInterval 120s)
- carte-paires : hulk-mexc/strategie/carte_fenetres_entree.json (âge 16293s / seuil 172800s · Calendrier quotidien 04:20)
- cortana-propose-params : hulk-mexc/strategie/cortana_pilot.json (âge 80733s / seuil 172800s · Calendrier quotidien 07:45)
- paternes-btc : Index_Maison/data/paternes_btc_etat.json (âge 55136s / seuil 172800s · StartInterval 86400s)
- superviseur-process : Index_Maison/scripts/superviseur.log (âge 23s / seuil 1200s · KeepAlive (événementiel))
- rwa-yields : Index_Maison/data/rwa_yields_etat.json (âge 11467s / seuil 43200s · StartInterval 21600s)
- disjoncteur : /tmp/disjoncteur_launchd.out.log (âge 14s / seuil 120s · StartInterval 60s)
- vigie-live : Index_Maison/strategie/vigie_cooldown.json (âge 4848s / seuil 7200s · KeepAlive (événementiel))
- superviseur-auto : Index_Maison/OUTBOX_OBSIDIAN/.superviseur_state.json (âge 10s / seuil 7200s · StartInterval 3600s)
- veille-signal : /tmp/veille_signal_launchd.out.log (âge 42s / seuil 600s · StartInterval 300s)
- hub-cockpit-feed : Index_Maison/cockpit/hub.json (âge 11s / seuil 60s · StartInterval 30s)
- gitpush : .git/refs/remotes/origin/main (âge 1s / seuil 32400s · StartInterval 10800s)
- veille-hub : Index_Maison/VEILLE_HUB_2026-10-12.md (âge 6683s / seuil 86400s · Calendrier quotidien 07:00) · DÉCLARÉE (produit 43200s vs déclencheur 86400s)
- llm-gate-hub : /Users/christophe/prise-ia/heartbeat.json (âge 14s / seuil 7200s · KeepAlive (événementiel))
- troupeau-inv : Index_Maison/troupeau_inv_hist.jsonl (âge 10286s / seuil 518400s · Calendrier hebdo (3 j/sem 06:00,06:00,06:00)) · DÉCLARÉE (produit 259200s vs déclencheur 201600s)
- suivi-setup-red : hulk-mexc/runs/SUIVI_SETUP_ZBCNUSDT.jsonl (âge 58549s / seuil 172800s · Calendrier quotidien 16:35)
- superviseur-l2 : runs/L2_20261012_SNAPS.csv (âge 0s / seuil 120s · KeepAlive (événementiel))
- cortana.urgent : Index_Maison/data/cortana_analysis.json (âge 42s / seuil 7200s · StartInterval 10s) · DÉCLARÉE (produit 3600s vs déclencheur 10s)
- cycle-edel : hulk-mexc/runs/CYCLE_EDEL_SUIVI.jsonl (âge 11823s / seuil 43200s · StartInterval 21600s)
- xrpl-gouvernance : Index_Maison/thermo/xrpl_gouv_etat.json (âge 6839s / seuil 7200s · StartInterval 3600s)
- xrpl-arbitrage : Index_Maison/thermo/xrpl_arbitrage_etat.json (âge 8s / seuil 1200s · StartInterval 10s) · DÉCLARÉE (produit 600s vs déclencheur 10s)
- archi-vivante : Index_Maison/strategie/ARCHITECTURE_VIVANTE.md (âge 18s / seuil 172800s · Calendrier quotidien 07:00)
- verdicteur-micro : Index_Maison/data/cortana_micro_score.json (âge 11s / seuil 600s · StartInterval 15s) · DÉCLARÉE (produit 300s vs déclencheur 15s)
- plancher-shadow : Index_Maison/data/plancher_confirme_etat.json (âge 16s / seuil 600s · StartInterval 300s)
- veilleuse-confrontation : Index_Maison/VEILLE_CONFRONTATION_ACE_HULK.md (âge 11935s / seuil 43200s · StartInterval 21600s)
- state-generator : Index_Maison/system/state.json (âge 31s / seuil 240s · StartInterval 120s)
- cockpit-http : /tmp/cockpit_http_17800.log (âge 22s / seuil 7200s · KeepAlive (événementiel))
- superviseur : Index_Maison/OUTBOX_OBSIDIAN/.superviseur_state.json (âge 10s / seuil 7200s · StartInterval 3600s)
- nourrisseur-disjoncteur : /tmp/nourrisseur_disjoncteur.out.log (âge 29s / seuil 120s · StartInterval 60s)
- prise-ia : /Users/christophe/prise-ia/heartbeat.json (âge 14s / seuil 7200s · KeepAlive (événementiel))
- controle-config : hulk-mexc/runs/CONTROLE_CONFIG.json (âge 6280s / seuil 7200s · StartInterval 3600s)
- kronos-ombre : Index_Maison/thermo/kronos_ombre_etat.json (âge 6136s / seuil 7200s · StartInterval 3600s)
- geopol : Index_Maison/indice_app/data/scores_geopol.json (âge 52203s / seuil 172800s · StartInterval 86400s)
- veilleuse : Index_Maison/thermo/VEILLEUSE.md (âge 42s / seuil 1200s · StartInterval 600s)
- croisements-indices : Index_Maison/data/croisements_indices_etat.json (âge 9062s / seuil 43200s · StartInterval 21600s)
- cortana-feed : Index_Maison/thermo/cortana_horaire_run.log (âge 6443s / seuil 7200s · StartInterval 3600s)
- divergence : hulk-mexc/runs/DIVERGENCE_SUIVI.jsonl (âge 11697s / seuil 43200s · StartInterval 21600s)

## ⚪ Jugés sur leur sortie launchd (aucun produit déclaré) (48)
- veilleuse-chantiers, mirofish, veille-degradation, croisement-externe, analyste-cadence, couleur-regime-score, observatoire, catalogue, sniffer-ny, routeur-auto, jackson-hole-alarmes, verif-setup, sonde-volume-panier, satellite-aspiration, cortana-analyzer, presence-paires, veille-insti, obsidian-writer, fusibles-mesure, veille-yt, roulement-ia, gitpush-vault, scoreur-registre, discipline-quotidienne, veille-essaim-observation, rappels, bloc-privatise, chien-de-garde, sante-index, macro-tempete, sniffer-matin, heartbeats, journal-soir, hulk-watchdog, deriv-corr, dialogue-gemini, mirofish-front, queueoffres, superviseur-core, graph-cerveau, fees, couleur-regime, flux-nets, veilleuse-sizing-monte-carlo, autopilote, dms-veille, eval-offres, cpfp

