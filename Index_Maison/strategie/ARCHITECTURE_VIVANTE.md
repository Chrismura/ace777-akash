# ARCHITECTURE VIVANTE — ACE777 (2026-10-26 07:16 UTC)

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

- mission.json : 2026-10-26 07:15Z · run `MASTER_BASE_V8_6_FORTRESS_8H20` · alerte `nominal`
- PnL combiné : **0.70 $** 📈 (combo 0.7028)
- ALPHA (sniper (embuscade, ×13, revenge si claque)) : **-1.97 $** · 7 fills · 6973 skips
- BETA (éclaireur (chatouille le marché, alimente Alpha)) : **+2.67 $** · 34 fills · 604 skips
- HULK (gestionnaire de portefeuille (bag, escalier, courreur)) : **+44.96 $** · 0 fills
- Saison : CALME 🧊 · 

## Veille du jour

- [Santé]
  · hub : OK (6 providers)
  · réseau (DNS) : OK
  · sources en erreur : 0
- [Énergie du jour]
  · appels : 39 (cloud 39)
  · budget cloud : 624 max
  · par provider : gemini=35, groq=2, mistral=2
- [Nouvelles offres détectées (non intégrées)]
  · recursive/flint-v1.0:free
  · nvidia/nemotron-3.5-super-vl:free
  · dots-studio/dots-3-note-preview:free
  … 119 offres/pépites détectées ce matin

## Mémoire chaude (journal + résumés)

- Radar (dernières alertes) :
  · 2026-10-26T07:15:54.740590Z BTCUSDT 80106.01 0.0000 0.2 declenche=non
  · 2026-10-26T07:15:55.210619Z ETHUSDT 2319.24 0.0003 38.0 declenche=non
  · 2026-10-26T07:15:55.884473Z BTCUSDT 80106.0 0.0000 0.2 declenche=non
  · 2026-10-26T07:15:55.939314Z BTCUSDT 80106.01 0.0000 0.2 declenche=non
- Intention en cours : BETA a sonde le marche (34 sondes, 25 long / 9 court, conf m | ALPHA attend son signal — aucun tir sur la session en cours.
- 1088 signets X résumés (quota aujourd'hui : 0/50)
- 183 fiches IA d'offres en cache (quota 8/jour)

---
Généré par archi_vivante.py — relancé à chaque validation.