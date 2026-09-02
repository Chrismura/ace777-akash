# ARCHITECTURE VIVANTE — ACE777 (2026-09-02 19:13 UTC)

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

- mission.json : 2026-09-02 19:13Z · run `ACE_RADAR_ALIGNED_V4_60M` · alerte `red`
- PnL combiné : **-9.12 $** 📉 (combo -9.1224)
- ALPHA (sniper (embuscade, ×13, revenge si claque)) : **-3.31 $** · 5 fills · 366 skips
- BETA (éclaireur (chatouille le marché, alimente Alpha)) : **-5.81 $** · 9 fills · 339 skips
- HULK (gestionnaire de portefeuille (bag, escalier, courreur)) : **+0.44 $** · 0 fills
- Saison : ACCUMULATION 💧 · 

## Veille du jour

- [Santé]
  · hub : OK (12 providers)
- [Énergie du jour]
  · appels : 35 (cloud 35)
  · budget cloud : 624 max
  · par provider : gemini=33, openrouter-free=1, openrouter-ultra=1
- [Nouvelles offres détectées (non intégrées)]
- [INTEGRATION AUTO 2026-09-02]
  · Hub ameliore avec dots-studio/dots-3-note-preview:free (preuve A/B + juge : MIEUX - répons
  · ETAT : EN OBSERVATION 48h (jamais route) -> observatoire + GO hebdo avant activation.
- [ROLLBACK AUTO 2026-09-02]
  · obs-1786688184 (cohere/north-mini-code:free) : 100% erreurs > 5% (observatoire)
- [ROLLBACK AUTO 2026-09-02]
  · obs-1786774646 (nvidia/nemotron-3-nano-30b-a3b:free) : 100% erreurs > 5% (observatoire)
- [ROLLBACK AUTO 2026-09-02]
  · obs-1786774656 (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free) : 60% erreurs > 5% (ob
- [ROLLBACK AUTO 2026-09-02]
  · obs-1786795252 (nvidia/nemotron-3.5-content-safety:free) : 100% erreurs > 5% (observatoire
- [ROLLBACK AUTO 2026-09-02]
  · obs-1787033767 (google/diffusiongemma-26b-a4b-it) : 100% erreurs > 5% (observatoire)
- [ROLLBACK AUTO 2026-09-02]
  · obs-1787206650 (google/gemma-4-26b-a4b-it:free) : 100% erreurs > 5% (observatoire)
- [ROLLBACK AUTO 2026-09-02]
  · obs-1787248844 (nvidia/nemotron-nano-9b-v2:free) : 100% erreurs > 5% (observatoire)
- [ROLLBACK AUTO 2026-09-02]
  · dots-studio-dots-3-note-preview-free (dots-studio/dots-3-note-preview:free) : 100% erreurs
  · inclusionai/ling-3.0-flash-fin:free
  · dots-studio/dots-3-note-preview:free
  · liquid/lfm-2.5-2.6b:free
  … 110 offres/pépites détectées ce matin

## Mémoire chaude (journal + résumés)

- Radar (dernières alertes) :
  · 2026-09-02T19:13:42.701804Z ETHUSDT 2395.71 0.0003 37.9 declenche=non
  · 2026-09-02T19:13:42.701843Z ETHUSDT 2395.7 0.0003 37.9 declenche=non
  · 2026-09-02T19:13:42.905342Z ETHUSDT 2395.69 0.0003 37.9 declenche=non
  · 2026-09-02T19:13:44.432780Z BTCUSDT 77357.21 0.0002 7.3 declenche=oui
- Intention en cours : BETA a sonde le marche (9 sondes, 4 long / 5 court, conf moy | ALPHA attend son moment : 352 skips (discipline), le mur du  | ALPHA a frappe 5 fois en embuscade (13x) (dont 2 en mode rev
- 816 signets X résumés (quota aujourd'hui : 0/50)
- 79 fiches IA d'offres en cache (quota 8/jour)

---
Généré par archi_vivante.py — relancé à chaque validation.