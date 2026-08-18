# QUESTION FAMILLE — Vérification de la logique des chaînes + modifications du jour (18/08/2026)

> Objet : la chaîne IA automatique + les modifications qui tournent aujourd'hui.
> Christophe demande : « vérification de la logique des chaînes, et check par la famille des dernières modifications qui tournent ».
> Règle d'économie : 2 membres + juge (plus jamais 6). Tout est réversible, rien ne se supprime.

---

## 1. La chaîne IA du matin (nouveaux horaires, tout avant la session)

| Heure | Étape | Script | Lit → Écrit |
|---|---|---|---|
| 07:00 | Flotille | veille_hub.py | → VEILLE_HUB_<date>.md |
| 07:02 | File d'attente | queue_offres.py | lit VEILLE_HUB → QUEUE_OFFRES.json + **intègre ACTIF (obs-\*)** |
| 07:05 | Évaluation | eval_offres.py | lit VEILLE_HUB → **intègre OBSERVATION (enabled:false)** |
| 07:06 | Brief | brief_offres.py | rapport |
| 07:07 | Intégration | (via eval_offres) | backup avant + 1 intégration max |
| 07:08 | Roulement | roulement_ia.py | lit QUEUE + providers → **remplace les morts** |
| 07:15 | Apprentissage | discipline_quotidienne.py | re-note Cortana + Ada |
| 11:00 | Observation | observatoire.py | sonde 48h → rollback auto >5% erreurs |

## 2. Les modifications d'aujourd'hui (qui tournent déjà)

1. **Cortana voit les bots** (cortana_analyse.py) : injecte l'état ACE (PnL, trades, sorties) + HULK (paper, positions, sonde) dans son contexte d'analyse — lecture seule
2. **Ada voit les bots** (ada_gardienne.py) : lit mission.json (alpha/beta/hulk) dans son coup d'œil — lecture seule
3. **roulement_ia.py (NOUVEAU)** : discerne épuisé temporaire (429/quota → GARDÉ) vs mort durable (>2j → ÉJECTÉ + remplacé par la meilleure offre teste_ok de la queue). Backup avant, atomique, 1 remplacement max, kill switch STOP_HUB.
4. **observatoire.py étendu** : sonde maintenant les obs-* (queue_offres) en plus des observation (eval_offres). Rollback obs-* = DÉSACTIVATION (jamais suppression). + fix robustesse : timeout 15s (était None = blocage infini).
5. **Horaires** : tout resserré avant 7h30 (fin du 9h30).

## 3. LE POINT À TRANCHER (le seul vrai questionnement)

**Deux mécanismes d'intégration coexistent dans la même chaîne :**
- **queue_offres (7h02)** : intègre les offres testées OK en **ACTIF direct** (`obs-*`, enabled:True — décision 14/08)
- **eval_offres (7h05)** : intègre en **OBSERVATION** (enabled:false — correction famille 09/08, jamais routé avant 48h + GO)

**C'est cohérent ou c'est une contradiction ?**
- Les obs-* sont actifs mais désormais **sondés par l'observatoire** (rollback auto si échec) — est-ce que ça suffit comme garde-fou pour justifier l'actif direct ?
- Ou faut-il unifier (tout en observation) ?

## 4. Questions à la famille

1. **La chaîne du matin est-elle logique et sans conflit ?** (dépendances, ordre, horaires)
2. **Le double mécanisme d'intégration (obs-* actif direct vs eval en observation) est-il acceptable** maintenant que l'observatoire sonde les obs-* ?
3. **Le roulement (mort >2j → remplacé) est-il bien calibré ?** (2 jours = trop long, trop court, ou juste ?)
4. **Risques manquants ?** (un maillon qui peut casser la chaîne)

Merci — 3 phrases max par réponse, tranchez net (GO / GO-AVEC-RÉSERVE / NON).
