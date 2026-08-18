# BILAN CYCLE IA — 18/08/2026 (vérifié par Buffy à 12h)

> Réponse aux 3 questions de Christophe : horaires, offres ramenées, intégrations.

## 1. Horaires — ajustés, prêts pour demain

| Heure | Étape | Script |
|---|---|---|
| 07:00 | Flotille part | veille_hub.py |
| 07:02 | File d'attente | queue_offres.py |
| 07:05 | Évaluation | eval_offres.py |
| 07:06 | Brief | brief_offres.py |
| 07:07 | Intégration | (via eval_offres) |
| 07:08 | Roulement | roulement_ia.py (nouveau) |
| 07:15 | Boucle apprentissage | discipline_quotidienne.py |

⚠️ Ce matin la queue a tourné à 8h15 (ancien créneau) — le cycle 7h02 complet démarre demain.

## 2. Offres ramenées ce matin — ✅ vérifié

- Flotille 7h00 a tourné : OpenRouter :free (8), NVIDIA, InferX, Puter, omniroute (43 pools)
- **35/35 candidates sont dans QUEUE_OFFRES** (dédup par hash OK)
- 0 offre inédite ce matin (mêmes modèles que les jours précédents) — normal

## 3. Intégrations dans le hub — ✅ 10 vérifiées

- diffusiongemma-26b, nemotron-3.5-lightning, nemotron-3-nano-30b, north-mini-code (Cohere) + 6 autres
- Tous `obs-*` avec `enabled:True` = ACTIF direct (décision 14/08, commentée queue_offres.py:292)
- Garde-fou : le routeur ne promeut qu'après ≥5 éch. +15 pts, rollback auto

## 4. Point à trancher (question Christophe)

- `observatoire.py` active après 48h + GO hebdo (ligne 184)
- MAIS `queue_offres.py` active déjà en direct (obs-*, décision 14/08)
- → Deux mécanismes d'activation coexistent. À trancher : garder les deux ou en retirer un.

> « On ne supprime rien, c'est la loi. » — Christophe
