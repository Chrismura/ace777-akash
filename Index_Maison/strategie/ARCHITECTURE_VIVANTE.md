# ARCHITECTURE VIVANTE — ACE777 (2026-09-18 16:55 UTC)

> Document GÉNÉRÉ AUTOMATIQUEMENT à l'instant. La famille valide
> en s'appuyant sur CE contexte, pas sur des documents figés.

## Qui tourne en ce moment
- ✅ hub
- ✅ pont cockpit
- ✅ radar
- ⛔ lecteur signets
- ⛔ générateur fiches
- ✅ feed mission
- ⛔ serveur cockpit

## Routage des tâches de décision

- `analyste.strategie` → gemini (repli groq)
- `audit.protocol` → gemini (repli groq)
- `signets.juge` → nara (repli groq)
- `signets.lot2` → gemini (repli nara)
- `signets.synthese` → gemini (repli nara)

## État de la mission (bots + PnL)

- mission.json : 2026-09-18 13:48Z · run `MASTER_BASE_V8_6_FORTRESS_8H20` · alerte `nominal`
- PnL combiné : **0.70 $** 📈 (combo 0.7028)
- ALPHA (sniper (embuscade, ×13, revenge si claque)) : **-1.97 $** · 7 fills · 6973 skips
- BETA (éclaireur (chatouille le marché, alimente Alpha)) : **+2.67 $** · 34 fills · 604 skips
- HULK (gestionnaire de portefeuille (bag, escalier, courreur)) : **+6.75 $** · 0 fills
- Saison : CALME 🧊 · 

## Veille du jour

- [Santé]
  · hub : OK (10 providers)
- [Énergie du jour]
  · appels : 27 (cloud 27)
  · budget cloud : 624 max
  · par provider : gemini=20, huggingface=1, openrouter-juge=2, orca=4
- [Nouvelles offres détectées (non intégrées)]
- [ROLLBACK AUTO 2026-09-18]
  · obs-1786688184 (cohere/north-mini-code:free) : 100% erreurs > 5% (observatoire)
- [ROLLBACK AUTO 2026-09-18]
  · obs-1786774646 (nvidia/nemotron-3-nano-30b-a3b:free) : 100% erreurs > 5% (observatoire)
- [ROLLBACK AUTO 2026-09-18]
  · obs-1786774656 (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free) : 60% erreurs > 5% (ob
- [ROLLBACK AUTO 2026-09-18]
  · obs-1786774667 (nvidia/nemotron-3.5-lightning:free) : 100% erreurs > 5% (observatoire)
- [ROLLBACK AUTO 2026-09-18]
  · obs-1786795252 (nvidia/nemotron-3.5-content-safety:free) : 100% erreurs > 5% (observatoire
- [ROLLBACK AUTO 2026-09-18]
  · obs-1787033767 (google/diffusiongemma-26b-a4b-it) : 100% erreurs > 5% (observatoire)
- [ROLLBACK AUTO 2026-09-18]
  · obs-1787206650 (google/gemma-4-26b-a4b-it:free) : 100% erreurs > 5% (observatoire)
- [ROLLBACK AUTO 2026-09-18]
  · obs-1787248844 (nvidia/nemotron-nano-9b-v2:free) : 100% erreurs > 5% (observatoire)
- [ROLLBACK AUTO 2026-09-18]
  · obs-1787724924 (minimax/minimax-m3:free) : 100% erreurs > 5% (observatoire)
- [ROLLBACK AUTO 2026-09-18]
  · obs-1788416175 (deepseek-ai/deepseek-v4-pro-0813) : 100% erreurs > 5% (observatoire)
  · ERR: <urlopen error [Errno 8] nodename nor servname provided, or
  · ERR: <urlopen error [Errno 8] nodename nor servname provided, or
  · ERR: <urlopen error [Errno 8] nodename nor servname provided, or
  … 21 offres/pépites détectées ce matin

## Mémoire chaude (journal + résumés)

- Radar (dernières alertes) :
  · 2026-09-18T13:49:51.562139Z BTCUSDT 79963.99 0.0016 32.1 declenche=non
  · 2026-09-18T13:49:51.562326Z ETHUSDT 2557.03 0.0029 1364.3 declenche=non
  · 2026-09-18T13:49:51.730581Z BTCUSDT 79963.99 0.0016 32.1 declenche=non
  · 2026-09-18T13:49:51.872872Z BTCUSDT 79963.99 0.0016 32.1 declenche=non
- Intention en cours : BETA a sonde le marche (34 sondes, 25 long / 9 court, conf m | ALPHA attend son signal — aucun tir sur la session en cours.
- 934 signets X résumés (quota aujourd'hui : 15/50)
- 119 fiches IA d'offres en cache (quota 8/jour)

---
Généré par archi_vivante.py — relancé à chaque validation.