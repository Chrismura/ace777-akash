# ARCHITECTURE VIVANTE — ACE777 (2026-09-29 11:32 UTC)

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

- mission.json : 2026-09-29 11:32Z · run `MASTER_BASE_V8_6_FORTRESS_8H20` · alerte `nominal`
- PnL combiné : **0.70 $** 📈 (combo 0.7028)
- ALPHA (sniper (embuscade, ×13, revenge si claque)) : **-1.97 $** · 7 fills · 6973 skips
- BETA (éclaireur (chatouille le marché, alimente Alpha)) : **+2.67 $** · 34 fills · 604 skips
- HULK (gestionnaire de portefeuille (bag, escalier, courreur)) : **+49.02 $** · 0 fills
- Saison : CALME 🧊 · 

## Veille du jour

- [Santé]
  · hub : OK (9 providers)
  · réseau (DNS) : KO — aucune source externe ne résout (hors-ligne)
  · sources en erreur : 8
- [Énergie du jour]
  · appels : 6 (cloud 6)
  · budget cloud : 624 max
  · par provider : gemini=6
- [Nouvelles offres détectées (non intégrées)]
  · ERR: <urlopen error [Errno 8] nodename nor servname provided, or
  · ERR: <urlopen error [Errno 8] nodename nor servname provided, or
  · ERR: <urlopen error [Errno 8] nodename nor servname provided, or
  … 21 offres/pépites détectées ce matin

## Mémoire chaude (journal + résumés)

- Radar (dernières alertes) :
  · 2026-09-29T11:32:47.599520Z BTCUSDT 84222.01 0.0015 26.2 declenche=oui
  · 2026-09-29T11:32:47.649499Z BTCUSDT 84222.01 0.0015 26.6 declenche=oui
  · 2026-09-29T11:32:47.650012Z BTCUSDT 84222.01 0.0015 26.7 declenche=oui
  · 2026-09-29T11:32:47.654995Z BTCUSDT 84222.01 0.0015 26.8 declenche=oui
- Intention en cours : BETA a sonde le marche (34 sondes, 25 long / 9 court, conf m | ALPHA attend son signal — aucun tir sur la session en cours.
- 1008 signets X résumés (quota aujourd'hui : 0/50)
- 143 fiches IA d'offres en cache (quota 8/jour)

---
Généré par archi_vivante.py — relancé à chaque validation.