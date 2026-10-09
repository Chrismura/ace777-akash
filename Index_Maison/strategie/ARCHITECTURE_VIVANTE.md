# ARCHITECTURE VIVANTE — ACE777 (2026-10-09 19:22 UTC)

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

- mission.json : 2026-10-09 19:22Z · run `MASTER_BASE_V8_6_FORTRESS_8H20` · alerte `nominal`
- PnL combiné : **0.70 $** 📈 (combo 0.7028)
- ALPHA (sniper (embuscade, ×13, revenge si claque)) : **-1.97 $** · 7 fills · 6973 skips
- BETA (éclaireur (chatouille le marché, alimente Alpha)) : **+2.67 $** · 34 fills · 604 skips
- HULK (gestionnaire de portefeuille (bag, escalier, courreur)) : **+45.41 $** · 0 fills
- Saison : CALME 🧊 · 

## Veille du jour

- [Santé]
  · hub : OK (7 providers)
  · réseau (DNS) : KO — aucune source externe ne résout (hors-ligne)
  · sources en erreur : 8
- [Énergie du jour]
  · appels : 13 (cloud 13)
  · budget cloud : 624 max
  · par provider : gemini=11, orca=2
- [Nouvelles offres détectées (non intégrées)]
  · ERR: <urlopen error [Errno 8] nodename nor servname provided, or
  · ERR: <urlopen error [Errno 8] nodename nor servname provided, or
  · ERR: <urlopen error [Errno 8] nodename nor servname provided, or
  … 21 offres/pépites détectées ce matin

## Mémoire chaude (journal + résumés)

- Radar (dernières alertes) :
  · 2026-10-09T19:22:17.291008Z ETHUSDT 2485.92 0.0002 75.0 declenche=oui
  · 2026-10-09T19:22:17.291097Z ETHUSDT 2485.97 0.0001 75.0 declenche=oui
  · 2026-10-09T19:22:17.291163Z ETHUSDT 2486.04 0.0001 75.2 declenche=oui
  · 2026-10-09T19:22:17.404933Z BTCUSDT 82508.01 0.0000 0.8 declenche=non
- Intention en cours : BETA a sonde le marche (34 sondes, 25 long / 9 court, conf m | ALPHA attend son signal — aucun tir sur la session en cours.
- 1024 signets X résumés (quota aujourd'hui : 9/50)
- 151 fiches IA d'offres en cache (quota 8/jour)

---
Généré par archi_vivante.py — relancé à chaque validation.