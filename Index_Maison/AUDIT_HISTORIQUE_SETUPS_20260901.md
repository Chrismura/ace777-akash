# Audit historique ACE — setups depuis le 9 juillet 2026

## Résumé exécutif

L'historique montre plusieurs périodes favorables, mais il ne permet pas de déclarer un setup rentable de façon certifiée : les anciennes sessions n'ont pas toutes un `run_id`, un sidecar et une réconciliation Binance par session.

## Références observées

| Setup | Résultats visibles | Confiance |
|---|---:|---|
| `vide_froid_vortex_v2_collab` / `2026-07-08-gemini-cursor-v2` | 4 intervalles uniques, dont `+13.1023` | moyenne-faible |
| `vide_froid_vortex_v2_collab` / `2026-07-10-v2.2.2-no-partner-halt` | nombreux intervalles, dont `+29.4095` | moyenne-faible |
| `V2.2.1_NO_SUICIDE` | plusieurs positifs, dont `+13.6019` | moyenne-faible |
| `VALIDATION_VOIE_A/pack_A` | `+19.7876` sur un intervalle | faible, échantillon unique |

Les chiffres ci-dessus sont des valeurs de rapports historiques ; ils ne doivent pas être assimilés automatiquement à un PnL net Binance.

## Différences avec les runs récents

Le setup historique de référence est documenté avec :

```text
BETA = 200 USDT
ALPHA = 800 USDT
x13 fixe dès le cycle 1
POLL_SEC = 0.064
```

Le lanceur récent force une rampe :

```text
x5 → x13 sur 180 cycles
```

Le manifeste actuel comprend également une logique de barrière duo, alors que la référence historique `+29.4095` est documentée sans cette barrière. Ces deux variantes ne sont pas équivalentes.

## Ce que l'historique permet de conclure

- Le duo Alpha/Beta a déjà connu des périodes de performance brute élevée.
- Le comportement dépend fortement du régime et du setup exact.
- Alpha a parfois fourni l'essentiel de la performance, ce qui rend les pertes de la branche Hunter particulièrement importantes.
- Les séries historiques contiennent des doublons de rapports et des changements de moteur.
- Les résultats récents V2–V4 ne peuvent pas être comparés directement aux meilleurs runs historiques.

## Ce qui manque encore

```text
run_id par session historique
commissions Binance par run_id
funding par run_id
notionnel exact par fill
preuve que le code exécuté était identique au manifeste documenté
```

## Recommandation stricte

1. Ne pas modifier `genesis_manifest.txt`.
2. Ne pas réactiver directement l'ancien setup gagnant.
3. Créer une variante isolée documentant explicitement `x13_fixed` ou `ramp_5_to_13`.
4. Tester d'abord en replay local avec frais et sorties identiques aux règles historiques.
5. Ne faire qu'un seul testnet court après validation du replay, avec compte à plat et nouveau `run_id`.
6. Juger la rentabilité uniquement sur le net réconcilié Binance.

## Verdict

```text
Historique utile pour formuler une hypothèse : oui
Setup historique certifié rentable : non
Équivalence avec le moteur actuel : non
Modification directe du champion : NO-GO
Nouveau testnet immédiat : non recommandé
LIVE : NO-GO
```
