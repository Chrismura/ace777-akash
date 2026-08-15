# RELEASE RECEIPT — Veilleuse / Synapse (15/08/2026)

## 1. Propriétaire
- **Superviseur** : Buffy · **Approuvé** : Christophe (GO, décision boucle 24/24) + famille
  (GO-AVEC-RÉSERVE, gemini 92% / nvidia 78%) · **Codeur** : hub (ébauche, corrigée supervision)

## 2. Frontières
- ✅ TOUCHE : `strategie/REGISTRE_SYNAPSES.json` (neuf) · `scripts/veilleuse_synapses.py`
  (neuf) · `scripts/alerte_vocale.py` (neuf) · `scripts/arret_alerte.sh` (neuf) ·
  `plists/com.ace777.veilleuse.plist` (neuf) · `thermo/VEILLEUSE.md` (généré) ·
  `data/alertes/` (journal + alertes)
- 🚫 NE TOUCHE PAS : moteur Hulk, hub, config, autres plists, aucun script existant

## 3. Gaps connus (honnêteté)
- `ATTENDUS_PROCESS` vérifie via `launchctl list` : si un service attendu n'est pas chargé
  pour une raison légitime (ex. arrêt manuel voulu), la veilleuse hurlera — c'est le but,
  mais il faudra `MAINTENANCE_PREVUE` lors des arrêts planifiés.
- La limite de sécurité 24h (famille) est DÉSACTIVÉE par défaut (décision Christophe) —
  réactivable en 2 lignes si besoin.
- Le registre doit être mis à jour à chaque chantier qui touche un fichier indexé
  (obligation RELEASE_RECEIPT) — sinon fausse alerte intrusion (vérifié en test).

## 4. Révocabilité
- `launchctl unload ~/Library/LaunchAgents/com.ace777.veilleuse.plist`
- `rm` de la plist + REGISTRE_SYNAPSES.json + veilleuse_synapses.py + alerte_vocale.py
  + arret_alerte.sh + thermo/VEILLEUSE.md = retour à l'état antérieur.

## 5. Tests réels effectués
- État sain rc=0 · intrusion réelle → INTRUSION + alerte vocale · anti-empilement (1 boucle
  max, vérifié 3 runs) · extinction manuelle · auto-intégrité · py_compile OK ·
  plist lint OK + chargée (PID 43302).

## 6. Rollback
```bash
launchctl unload ~/Library/LaunchAgents/com.ace777.veilleuse.plist
rm ~/Library/LaunchAgents/com.ace777.veilleuse.plist \
   ~/ace777-test-day1/Index_Maison/plists/com.ace777.veilleuse.plist \
   ~/ace777-test-day1/Index_Maison/strategie/REGISTRE_SYNAPSES.json \
   ~/ace777-test-day1/Index_Maison/scripts/veilleuse_synapses.py \
   ~/ace777-test-day1/Index_Maison/scripts/alerte_vocale.py \
   ~/ace777-test-day1/Index_Maison/scripts/arret_alerte.sh
```
