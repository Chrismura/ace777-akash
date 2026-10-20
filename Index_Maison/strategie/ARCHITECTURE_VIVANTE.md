# ARCHITECTURE VIVANTE — ACE777 (2026-10-20 11:07 UTC)

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

- mission.json : 2026-10-20 11:07Z · run `MASTER_BASE_V8_6_FORTRESS_8H20` · alerte `nominal`
- PnL combiné : **0.70 $** 📈 (combo 0.7028)
- ALPHA (sniper (embuscade, ×13, revenge si claque)) : **-1.97 $** · 7 fills · 6973 skips
- BETA (éclaireur (chatouille le marché, alimente Alpha)) : **+2.67 $** · 34 fills · 604 skips
- HULK (gestionnaire de portefeuille (bag, escalier, courreur)) : **+46.32 $** · 0 fills
- Saison : CALME 🧊 · 

## Veille du jour

- [Santé]
  · hub : OK (7 providers)
  · réseau (DNS) : OK
  · sources en erreur : 0
- [Énergie du jour]
  · appels : 14 (cloud 14)
  · budget cloud : 624 max
  · par provider : gemini=11, groq=2, mistral=1
- [Nouvelles offres détectées (non intégrées)]
  · minimax/minimax-m3.1-flash:free
  · nvidia/nemotron-3.5-super-vl:free
  · dots-studio/dots-3-note-preview:free
  … 110 offres/pépites détectées ce matin

## Mémoire chaude (journal + résumés)

- Radar (dernières alertes) :
  · 2026-10-20T11:07:23.369422Z BTCUSDT 81520.0 0.0004 9.7 declenche=oui
  · 2026-10-20T11:07:23.404095Z BTCUSDT 81520.0 0.0004 9.7 declenche=oui
  · 2026-10-20T11:07:23.416578Z BTCUSDT 81520.0 0.0004 10.0 declenche=oui
  · 2026-10-20T11:07:23.546782Z ETHUSDT 2386.43 0.0002 34.0 declenche=non
- Intention en cours : BETA a sonde le marche (34 sondes, 25 long / 9 court, conf m | ALPHA attend son signal — aucun tir sur la session en cours.
- 1057 signets X résumés (quota aujourd'hui : 0/50)
- 167 fiches IA d'offres en cache (quota 8/jour)

---
Généré par archi_vivante.py — relancé à chaque validation.