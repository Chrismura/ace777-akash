# ARCHITECTURE VIVANTE — ACE777 (2026-11-03 07:35 UTC)

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

- mission.json : 2026-11-03 07:34Z · run `MASTER_BASE_V8_6_FORTRESS_8H20` · alerte `nominal`
- PnL combiné : **0.70 $** 📈 (combo 0.7028)
- ALPHA (sniper (embuscade, ×13, revenge si claque)) : **-1.97 $** · 7 fills · 6973 skips
- BETA (éclaireur (chatouille le marché, alimente Alpha)) : **+2.67 $** · 34 fills · 604 skips
- HULK (gestionnaire de portefeuille (bag, escalier, courreur)) : **+43.13 $** · 0 fills
- Saison : CALME 🧊 · 

## Veille du jour

- [Santé]
  · hub : OK (6 providers)
  · réseau (DNS) : OK
  · sources en erreur : 0
- [Énergie du jour]
  · appels : 40 (cloud 40)
  · budget cloud : 624 max
  · par provider : gemini=19, groq=20, mistral=1
- [Nouvelles offres détectées (non intégrées)]
  · recursive/flint-v1.0:free
  · dots-studio/dots-3-note-preview:free
  · liquid/lfm-2.5-2.6b:free
  … 115 offres/pépites détectées ce matin

## Mémoire chaude (journal + résumés)

- Radar (dernières alertes) :
  · 2026-11-03T07:35:01.206295Z BTCUSDT 76856.0 0.0007 16.8 declenche=oui
  · 2026-11-03T07:35:01.209362Z ETHUSDT 2257.09 0.0002 4.6 declenche=non
  · 2026-11-03T07:35:01.209465Z ETHUSDT 2257.08 0.0002 4.6 declenche=non
  · 2026-11-03T07:35:01.209523Z ETHUSDT 2257.07 0.0002 4.7 declenche=non
- Intention en cours : BETA a sonde le marche (34 sondes, 25 long / 9 court, conf m | ALPHA attend son signal — aucun tir sur la session en cours.
- 1208 signets X résumés (quota aujourd'hui : 12/50)
- 207 fiches IA d'offres en cache (quota 8/jour)

---
Généré par archi_vivante.py — relancé à chaque validation.