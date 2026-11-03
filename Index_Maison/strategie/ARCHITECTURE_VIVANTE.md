# ARCHITECTURE VIVANTE — ACE777 (2026-11-03 11:19 UTC)

> Document GÉNÉRÉ AUTOMATIQUEMENT à l'instant. La famille valide
> en s'appuyant sur CE contexte, pas sur des documents figés.

## Ce qui produit en ce moment (donnée datée)
- ✅ hub LLM · `heartbeat.json` 55 min · daemon (tolérance 60 min)
- ✅ pont cockpit · `mission.json` 1 min · daemon (tolérance 60 min)
- ✅ radar · `journal_radar.log` 0 min · daemon (tolérance 60 min)
- ✅ feed mission · `hub.json` 0 min · toutes les 30 s (tolérance ×3 = 5 min)
- ⚪ lecteur signets · `SIGNETS_RESUMES.json` 34 min · pas de cadence déclarée (organe non planifié)
- ✅ générateur fiches · `FICHES_OFFRES.json` 2.2 h · calendaire (tolérance 26 h)
- ✅ serveur cockpit · port 17800 répond · daemon (tolérance 60 min)
- **6 frais · 0 lents · 0 muets** — critère = la donnée produite, jamais le nom du processus

## Routage des tâches de décision

- `analyste.strategie` → gemini (repli groq)
- `audit.protocol` → gemini (repli groq)
- `signets.juge` → nara (repli groq)
- `signets.lot2` → gemini (repli nara)
- `signets.synthese` → gemini (repli nara)

## État de la mission (bots + PnL)

- mission.json : 2026-11-03 11:18Z · run `MASTER_BASE_V8_6_FORTRESS_8H20` · alerte `nominal`
- PnL combiné : **0.70 $** 📈 (combo 0.7028)
- ALPHA (sniper (embuscade, ×13, revenge si claque)) : **-1.97 $** · 7 fills · 6973 skips
- BETA (éclaireur (chatouille le marché, alimente Alpha)) : **+2.67 $** · 34 fills · 604 skips
- HULK (gestionnaire de portefeuille (bag, escalier, courreur)) : **+38.58 $** · 0 fills
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
  · 2026-11-03T11:19:22.405037Z ETHUSDT 2269.88 0.0001 18.1 declenche=non
  · 2026-11-03T11:19:22.405195Z ETHUSDT 2269.9 0.0001 18.1 declenche=non
  · 2026-11-03T11:19:22.405319Z ETHUSDT 2269.91 0.0001 18.2 declenche=non
  · 2026-11-03T11:19:22.812654Z BTCUSDT 77202.82 0.0004 4.5 declenche=non
- Intention en cours : BETA a sonde le marche (34 sondes, 25 long / 9 court, conf m | ALPHA attend son signal — aucun tir sur la session en cours.
- 1211 signets X résumés (quota aujourd'hui : 15/50)
- 215 fiches IA d'offres en cache (quota 8/jour)

---
Généré par archi_vivante.py — relancé à chaque validation.