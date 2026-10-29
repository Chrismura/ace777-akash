# ARCHITECTURE VIVANTE — ACE777 (2026-10-29 22:49 UTC)

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

- mission.json : 2026-10-29 22:49Z · run `MASTER_BASE_V8_6_FORTRESS_8H20` · alerte `nominal`
- PnL combiné : **0.70 $** 📈 (combo 0.7028)
- ALPHA (sniper (embuscade, ×13, revenge si claque)) : **-1.97 $** · 7 fills · 6973 skips
- BETA (éclaireur (chatouille le marché, alimente Alpha)) : **+2.67 $** · 34 fills · 604 skips
- HULK (gestionnaire de portefeuille (bag, escalier, courreur)) : **+43.78 $** · 0 fills
- Saison : CALME 🧊 · 

## Veille du jour

- [Santé]
  · hub : OK (6 providers)
  · réseau (DNS) : KO — aucune source externe ne résout (hors-ligne)
  · sources en erreur : 8
- [Énergie du jour]
  · appels : 16 (cloud 16)
  · budget cloud : 624 max
  · par provider : gemini=14, groq=2
- [Nouvelles offres détectées (non intégrées)]
  · ERR: <urlopen error [Errno 8] nodename nor servname provided, or
  · ERR: <urlopen error [Errno 8] nodename nor servname provided, or
  · ERR: <urlopen error [Errno 8] nodename nor servname provided, or
  … 21 offres/pépites détectées ce matin

## Mémoire chaude (journal + résumés)

- Radar (dernières alertes) :
  · 2026-10-29T22:49:50.040062Z ETHUSDT 2275.96 0.0008 237.9 declenche=non
  · 2026-10-29T22:49:50.087712Z ETHUSDT 2275.96 0.0008 237.9 declenche=non
  · 2026-10-29T22:49:50.091429Z BTCUSDT 79007.81 0.0007 0.4 declenche=non
  · 2026-10-29T22:49:50.109360Z BTCUSDT 79007.82 0.0007 0.4 declenche=non
- Intention en cours : BETA a sonde le marche (34 sondes, 25 long / 9 court, conf m | ALPHA attend son signal — aucun tir sur la session en cours.
- 1146 signets X résumés (quota aujourd'hui : 6/50)
- 183 fiches IA d'offres en cache (quota 8/jour)

---
Généré par archi_vivante.py — relancé à chaque validation.