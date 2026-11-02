# ARCHITECTURE VIVANTE — ACE777 (2026-11-02 15:03 UTC)

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

- mission.json : 2026-11-02 15:02Z · run `MASTER_BASE_V8_6_FORTRESS_8H20` · alerte `nominal`
- PnL combiné : **0.70 $** 📈 (combo 0.7028)
- ALPHA (sniper (embuscade, ×13, revenge si claque)) : **-1.97 $** · 7 fills · 6973 skips
- BETA (éclaireur (chatouille le marché, alimente Alpha)) : **+2.67 $** · 34 fills · 604 skips
- HULK (gestionnaire de portefeuille (bag, escalier, courreur)) : **+43.31 $** · 0 fills
- Saison : CHAUFFE 🌡️ · 

## Veille du jour

- [Santé]
  · hub : OK (6 providers)
  · réseau (DNS) : OK
  · sources en erreur : 0
- [Énergie du jour]
  · appels : 46 (cloud 46)
  · budget cloud : 624 max
  · par provider : gemini=17, groq=26, mistral=3
- [Nouvelles offres détectées (non intégrées)]
  · recursive/flint-v1.0:free
  · dots-studio/dots-3-note-preview:free
  · liquid/lfm-2.5-2.6b:free
  … 115 offres/pépites détectées ce matin

## Mémoire chaude (journal + résumés)

- Radar (dernières alertes) :
  · 2026-11-02T15:03:08.580157Z BTCUSDT 77876.01 0.0004 3.2 declenche=non
  · 2026-11-02T15:03:08.635374Z BTCUSDT 77876.0 0.0004 3.2 declenche=non
  · 2026-11-02T15:03:08.858680Z ETHUSDT 2288.36 0.0005 58.9 declenche=non
  · 2026-11-02T15:03:08.870939Z ETHUSDT 2288.34 0.0005 58.9 declenche=non
- Intention en cours : BETA a sonde le marche (34 sondes, 25 long / 9 court, conf m | ALPHA attend son signal — aucun tir sur la session en cours.
- 1196 signets X résumés (quota aujourd'hui : 50/50)
- 207 fiches IA d'offres en cache (quota 8/jour)

---
Généré par archi_vivante.py — relancé à chaque validation.