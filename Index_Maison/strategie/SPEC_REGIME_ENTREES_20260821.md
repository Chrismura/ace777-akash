# SPEC FAMILLE — Régime d'entrées : le moteur trade dans le mauvais régime (21/08/2026)

**Demande :** Christophe — « c'est capital sinon ACE777 n'a plus de sens ».

## Problème constaté (preuve chiffrée, lecture seule)

Le moteur gagne en brut mais perd massivement en net. Sur 154 trades (20–21/08) :

| | BETA (scout) | ALPHA (hunter) | TOTAL |
|---|---|---|---|
| Trades | 89 | 65 | **154** |
| PnL brut | −1.60 | +12.17 | **+10.57** |
| Frais | −42.88 | −178.05 | **−220.93** |
| **NET** | **−44.47** | **−165.88** | **−210.36** |

### Faits accablants
1. **92–93 % des trades ont |bps| < 8** (frais aller-retour) → perte nette mathématiquement certaine.
2. **97 % des trades sortent sous le TP net requis** (`MIN_PROFIT_BPS=15`).
3. **63 % des trades sortent à 0–2 bps**, 85 % à < 5 bps. Sortie dominante : `shock_inversion_stop` (90 %).
4. Win rate **net** : 3–5 % (contre 38–56 % en brut). Le win rate brut est un mirage.
5. Notionnel ALPHA médian 2 998 USDT, max 9 707 USDT (marge 800, « x5 » affiché) → 8 bps de frais = 7.76 $/trade.

### Simulations (les 3 corrections évidentes ne suffisent PAS)
- Filtrer les entrées |bps| ≥ 8 → NET **−15.94** (seuls 7 % des trades passent, dont 3 des 5 ≥ 15 bps sont perdants).
- Plafonner le notionnel à 1 000 USDT → NET **−84.40**.
- Même avec frais = 0, le brut total n'est que +10.57 sur 154 trades (+0.07/trade) : **l'edge brut est quasi nul**.

### Cause racine identifiée : le moteur ne remplit QUE dans le régime COMPRESSÉ
Analyse IRM (proxy tension, lecture seule) :

| Régime | Temps | Fills | PnL fills |
|---|---|---|---|
| COMPRESSÉ (marché mort) | 88.5 % | **TOUS les fills** | −1.11 (BETA) |
| TRANSITOIRE (bruit retail) | 10.8 % | **0 fill** | — |
| CLUSTER (tension haute) | 0.7 % | **0 fill** | — |

Le radar détecte les régimes (vortex_control.json, IRM) mais le moteur **ignore sa propre lecture** :
- il entre sur micro-bruits de marché mort (tension ~0) → sorties à 0–2 bps,
- il skippe les régimes où il y a du vrai mouvement (TRANSITOIRE/CLUSTER).

## Questions à la famille

1. **Diagnostic** : validez-vous la cause racine « le moteur trade dans le régime COMPRESSÉ au lieu d'attendre TRANSITOIRE/CLUSTER » (preuve IRM + distribution des sorties) ?
2. **Correction prioritaire** : quelle est LA correction la plus rentable et la plus sûre :
   (a) gate d'entrée par régime (ne trader que TRANSITOIRE/CLUSTER, SKIP en COMPRESSÉ),
   (b) seuil d'élan minimum à l'entrée (refuser les micro-moments < X bps de potentiel),
   (c) sortir au TP net avec trailing au lieu du shock-exit nerveux,
   (d) autre approche (clause permanente : proposez autre chose / mieux) ?
3. **Ordre d'exécution** : quelle séquence recommandez-vous (une seule correction à la fois, testable) ?
4. **Garde-fous** : quelles conditions non négociables avant toute activation (validation sur données, testnet, rollback) ?
5. **Risque** : que risque-t-on si on ne corrige RIEN (statut quo) ?

## Contraintes

- Champion scellé `64fb153f` (verrou md5 leçon 6) — aucune modif moteur sans verdict famille + validation.
- Règle d'or : on améliore, on dégrade pas ; preuve réelle avant correction ; tout passe par famille/juge ; Buffy supervise.
- Avis seulement : rien n'est appliqué par cette consultation.
- Run testnet en cours (lecture seule OK, ne pas le perturber).
