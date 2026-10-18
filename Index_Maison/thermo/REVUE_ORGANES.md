# 🔎 REVUE DES ORGANES
*2026-10-18 10:01:15 UTC — lecture seule sur la maison*

**101 organes** · 40 OK · 48 jugés sur leur sortie (aucun produit déclaré) · 0 assumés (zone grise/dormant) · **2 à trancher** · 11 hors délai

## 🔴 À TRANCHER (2)
- **watchdog** — produit déclaré non résolu : /tmp/watchdog-superviseur.out.log → introuvable (StartInterval 120s)
  - à faire : corriger le chemin au registre, ou déclarer la ligne dans revue_declares.json → produits_non_resolus
- **veille-signal** — produit déclaré non résolu : /tmp/veille_signal_launchd.out.log → introuvable (StartInterval 300s)
  - à faire : corriger le chemin au registre, ou déclarer la ligne dans revue_declares.json → produits_non_resolus

## 🔍 Candidats « produit frais, contenu peut-être figé » (1)
*Information, pas alarme : un champ « date » de jour ou un compteur donne un faux candidat. Seuls les organes dont le champ est DÉCLARÉ dans revue_declares.json (contenu_surveille) peuvent déclencher, via le chien.*
- thermo-quotidien : `ts` vieux de 1.9 h alors que le fichier a été réécrit il y a 0.0 h

## ✅ OK — produit frais ET cadence cohérente (40)
- cockpit-pont : Index_Maison/cockpit/mission.json (âge 12s / seuil 600s · KeepAlive (événementiel))
- ofi-calc : Index_Maison/data/ofi_latest.json (âge 33s / seuil 120s · StartInterval 60s)
- pont-onchain : /tmp/pont_onchain_launchd.out.log (âge 30s / seuil 3600s · StartInterval 300s) · DÉCLARÉE (produit 1800s vs déclencheur 300s)
- carte-paires : hulk-mexc/strategie/carte_fenetres_entree.json (âge 32s / seuil 172800s · Calendrier quotidien 04:20)
- xrpl-onchain : Index_Maison/thermo/xrpl_onchain_etat.json (âge 29s / seuil 7200s · StartInterval 3600s)
- cortana-propose-params : hulk-mexc/strategie/cortana_pilot.json (âge 15368s / seuil 172800s · Calendrier quotidien 07:45)
- paternes-btc : Index_Maison/data/paternes_btc_etat.json (âge 31s / seuil 172800s · StartInterval 86400s)
- superviseur-process : Index_Maison/scripts/superviseur.log (âge 33s / seuil 1200s · KeepAlive (événementiel))
- short-btc : hulk-mexc/runs/short_btc_state.json (âge 14s / seuil 600s · StartInterval 300s)
- sentinelle-independante : Index_Maison/thermo/sentinelle_independante_etat.json (âge 31s / seuil 5400s · StartInterval 3600s)
- rwa-yields : Index_Maison/data/rwa_yields_etat.json (âge 26s / seuil 43200s · StartInterval 21600s)
- disjoncteur : /tmp/disjoncteur_launchd.out.log (âge 34s / seuil 120s · StartInterval 60s)
- vigie-live : Index_Maison/strategie/vigie_cooldown.json (âge 7115s / seuil 7200s · KeepAlive (événementiel))
- superviseur-auto : Index_Maison/OUTBOX_OBSIDIAN/.superviseur_state.json (âge 24s / seuil 7200s · StartInterval 3600s)
- gitpush : .git/refs/remotes/origin/main (âge 9086s / seuil 32400s · StartInterval 10800s)
- veille-hub : Index_Maison/VEILLE_HUB_2026-10-18.md (âge 18059s / seuil 86400s · Calendrier quotidien 07:00) · DÉCLARÉE (produit 43200s vs déclencheur 86400s)
- troupeau-inv : Index_Maison/troupeau_inv_hist.jsonl (âge 194471s / seuil 518400s · Calendrier hebdo (3 j/sem 06:00,06:00,06:00)) · DÉCLARÉE (produit 259200s vs déclencheur 201600s)
- suivi-setup-red : hulk-mexc/runs/SUIVI_SETUP_ZBCNUSDT.jsonl (âge 69923s / seuil 172800s · Calendrier quotidien 16:35)
- superviseur-l2 : runs/L2_20261018_SNAPS.csv (âge 1s / seuil 120s · KeepAlive (événementiel))
- juste-prix : Index_Maison/data/juste_prix_hist.jsonl (âge 9s / seuil 600s · StartInterval 300s)
- thermo-quotidien : Index_Maison/thermo/live.json (âge 31s / seuil 600s · StartInterval 300s)
- cortana.urgent : Index_Maison/data/cortana_analysis.json (âge 6456s / seuil 7200s · StartInterval 10s) · DÉCLARÉE (produit 3600s vs déclencheur 10s)
- cycle-edel : hulk-mexc/runs/CYCLE_EDEL_SUIVI.jsonl (âge 16s / seuil 43200s · StartInterval 21600s)
- xrpl-gouvernance : Index_Maison/thermo/xrpl_gouv_etat.json (âge 32s / seuil 7200s · StartInterval 3600s)
- xrpl-arbitrage : Index_Maison/thermo/xrpl_arbitrage_etat.json (âge 11s / seuil 1200s · StartInterval 10s) · DÉCLARÉE (produit 600s vs déclencheur 10s)
- archi-vivante : Index_Maison/strategie/ARCHITECTURE_VIVANTE.md (âge 25s / seuil 172800s · Calendrier quotidien 07:00)
- verdicteur-micro : Index_Maison/data/cortana_micro_score.json (âge 15s / seuil 600s · StartInterval 15s) · DÉCLARÉE (produit 300s vs déclencheur 15s)
- plancher-shadow : Index_Maison/data/plancher_confirme_etat.json (âge 28s / seuil 600s · StartInterval 300s)
- signal3-livre-ecorche : Index_Maison/data/heartbeat_signal3.json (âge 13s / seuil 3600s · StartInterval 1800s)
- veilleuse-confrontation : Index_Maison/VEILLE_CONFRONTATION_ACE_HULK.md (âge 15084s / seuil 43200s · StartInterval 21600s)
- gen-cockpit-vol : Index_Maison/cockpit/vol_live.js (âge 31s / seuil 600s · StartInterval 300s)
- cockpit-http : /tmp/cockpit_http_17800.log (âge 33s / seuil 7200s · KeepAlive (événementiel))
- superviseur : Index_Maison/OUTBOX_OBSIDIAN/.superviseur_state.json (âge 24s / seuil 7200s · StartInterval 3600s)
- nourrisseur-disjoncteur : /tmp/nourrisseur_disjoncteur.out.log (âge 12s / seuil 120s · StartInterval 60s)
- controle-config : hulk-mexc/runs/CONTROLE_CONFIG.json (âge 11s / seuil 7200s · StartInterval 3600s)
- kronos-ombre : Index_Maison/thermo/kronos_ombre_etat.json (âge 4s / seuil 7200s · StartInterval 3600s)
- geopol : Index_Maison/indice_app/data/scores_geopol.json (âge 12014s / seuil 172800s · StartInterval 86400s)
- veilleuse : Index_Maison/thermo/VEILLEUSE.md (âge 31s / seuil 1200s · StartInterval 600s)
- croisements-indices : Index_Maison/data/croisements_indices_etat.json (âge 34s / seuil 43200s · StartInterval 21600s)
- divergence : hulk-mexc/runs/DIVERGENCE_SUIVI.jsonl (âge 10s / seuil 43200s · StartInterval 21600s)

## ⚪ Jugés sur leur sortie launchd (aucun produit déclaré) (48)
- veilleuse-chantiers, mirofish, veille-degradation, croisement-externe, analyste-cadence, couleur-regime-score, observatoire, catalogue, sniffer-ny, routeur-auto, jackson-hole-alarmes, verif-setup, sonde-volume-panier, satellite-aspiration, cortana-analyzer, presence-paires, veille-insti, obsidian-writer, fusibles-mesure, veille-yt, roulement-ia, gitpush-vault, scoreur-registre, discipline-quotidienne, veille-essaim-observation, rappels, bloc-privatise, chien-de-garde, sante-index, macro-tempete, sniffer-matin, heartbeats, journal-soir, hulk-watchdog, deriv-corr, dialogue-gemini, mirofish-front, queueoffres, superviseur-core, graph-cerveau, fees, couleur-regime, flux-nets, veilleuse-sizing-monte-carlo, autopilote, dms-veille, eval-offres, cpfp

