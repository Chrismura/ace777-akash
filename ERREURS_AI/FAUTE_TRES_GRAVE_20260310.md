# FAUTE TRÈS GRAVE — 2026-03-10

## Erreur

**Confusion des runs PNL** : l’IA a attribué le PNL du run d’après-midi (-12,58 USDT) au run de nuit, alors que l’utilisateur demandait le PNL de la nuit.

## Détail

- **Run de nuit** (22:03 UTC 9 mars → 02:03 UTC 10 mars) : **+5,19 USDT** (positif)
- **Run d’après-midi** (12:17 UTC → 15:09 UTC 10 mars) : **-12,58 USDT** (négatif)

L’IA a utilisé les CSV `MASTER_BASE_V8_5_IMPACT_4H00_*` (après-midi) au lieu de `MASTER_BASE_V8_5_IMPACT_4H_*` (nuit) et a présenté -12,58 USDT comme résultat du run de nuit.

## Conséquence

Rapport PNL complètement faux, confusion majeure pour l’utilisateur.

## Règle à respecter

**Toujours vérifier la fenêtre horaire** du run demandé avant de calculer ou présenter un PNL. Ne jamais confondre deux runs différents.
