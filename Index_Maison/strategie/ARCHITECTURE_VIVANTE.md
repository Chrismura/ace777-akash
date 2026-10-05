# ARCHITECTURE VIVANTE — ACE777 (2026-10-05 13:30 UTC)

> Document GÉNÉRÉ AUTOMATIQUEMENT à l'instant. La famille valide
> en s'appuyant sur CE contexte, pas sur des documents figés.

## Qui tourne en ce moment
- ⛔ hub
- ✅ pont cockpit
- ✅ radar
- ⛔ lecteur signets
- ⛔ générateur fiches
- ⛔ feed mission
- ✅ serveur cockpit

## Routage des tâches de décision

- `analyste.strategie` → gemini (repli groq)
- `audit.protocol` → gemini (repli groq)
- `signets.juge` → nara (repli groq)
- `signets.lot2` → gemini (repli nara)
- `signets.synthese` → gemini (repli nara)

## État de la mission (bots + PnL)

- mission.json : 2026-10-05 13:30Z · run `MASTER_BASE_V8_6_FORTRESS_8H20` · alerte `nominal`
- PnL combiné : **0.70 $** 📈 (combo 0.7028)
- ALPHA (sniper (embuscade, ×13, revenge si claque)) : **-1.97 $** · 7 fills · 6973 skips
- BETA (éclaireur (chatouille le marché, alimente Alpha)) : **+2.67 $** · 34 fills · 604 skips
- HULK (gestionnaire de portefeuille (bag, escalier, courreur)) : **+44.54 $** · 0 fills
- Saison : CALME 🧊 · 

## Veille du jour

- [Santé]
  · hub : OK (7 providers)
  · réseau (DNS) : OK
  · sources en erreur : 0
- [Énergie du jour]
  · appels : 59 (cloud 59)
  · budget cloud : 624 max
  · par provider : gemini=56, orca=3
- [Nouvelles offres détectées (non intégrées)]
  · apodex/apodex-1.1-mini:free
  · inclusionai/ling-3.0-flash-sante:free
  · qwen/qwen3.8-27b:free
  … 114 offres/pépites détectées ce matin

## Mémoire chaude (journal + résumés)

- Radar (dernières alertes) :
  · 2026-10-05T13:30:39.734166Z BTCUSDT 85952.28 0.0017 23.4 declenche=oui
  · 2026-10-05T13:30:39.734235Z BTCUSDT 85952.27 0.0017 23.4 declenche=oui
  · 2026-10-05T13:30:39.734311Z ETHUSDT 2716.27 0.0011 97.3 declenche=non
  · 2026-10-05T13:30:39.734430Z ETHUSDT 2716.26 0.0011 97.3 declenche=non
- Intention en cours : BETA a sonde le marche (34 sondes, 25 long / 9 court, conf m | ALPHA attend son signal — aucun tir sur la session en cours.
- 1015 signets X résumés (quota aujourd'hui : 0/50)
- 151 fiches IA d'offres en cache (quota 8/jour)

---
Généré par archi_vivante.py — relancé à chaque validation.