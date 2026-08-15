# RELEASE RECEIPT — Branchement onchain (15/08/2026)

## 1. Propriétaire
- **Superviseur** : Buffy · **Approuvé** : Christophe (GO) + famille (GO-AVEC-RÉSERVE,
  gemini 75% / nvidia 72%) · **Codeur** : hub (ébauche, corrigée supervision)

## 2. Frontières
- ✅ TOUCHE : `scripts/pont_onchain.py` (neuf) · `scripts/cortana_analyse.py` (2 blocs)
  · `scripts/ada_gardienne.py` (2 blocs) · `plists/com.ace777.whales.plist` (neuf)
  · `thermo/live.json` (section onchain ajoutée)
- 🚫 NE TOUCHE PAS : moteur Hulk, hub, config, autres plists — vérifié

## 3. Gaps connus
- `onchain_whaleEcartSeuil` = None quand aucun gros bloc (pas de signal à mesurer).
- Moyenne mobile 7j = approximation par jours calendaires du jsonl (pas une vraie
  fenêtre glissante 168h) — suffisant v1, à affiner si utile.
- Test A/B Cortana (avec/sans onchain, 7 jours) demandé par la famille : à mesurer via
  score_justesse.py — l'indice onchain est EN LIGNE mais la famille voulait ce test.
- Panneau cockpit whales_panel.js toujours désactivé (intégration ENSEMBLE prévue).

## 4. Révocabilité
- `launchctl unload ~/Library/LaunchAgents/com.ace777.whales.plist` + `rm` de la plist
  (le daemon /tmp lancer_whales.py peut être relancé pour revenir à l'existant).
- `rm pont_onchain.py` + suppression de la clé onchain de live.json.
- Diffs cortana_analyse/ada_gardienne : inversibles (2 blocs chacun).

## 5. Tests réels effectués
- Pont : injection + idempotence + préservation des autres clés.
- Ada : 5/5 (régression + outflow ×0.93 + inflow ×1.05 + calme + jamais 0).
- Cortana : indice reconnu + analyse réelle via hub (NEUTRE, confiance faible, disciplinée).
- Plist : lint OK, chargée, premier scan loggé, daemon /tmp arrêté, scan unique.

## 6. Rollback
```bash
launchctl unload ~/Library/LaunchAgents/com.ace777.whales.plist
rm ~/Library/LaunchAgents/com.ace777.whales.plist ~/ace777-test-day1/Index_Maison/plists/com.ace777.whales.plist
# (option) relancer l'ancien daemon :
# nohup python3 /tmp/lancer_whales.py >/dev/null 2>&1 &
# Retirer la section onchain de live.json (clé "onchain")
```
