# SPEC — Choix exchange + Problème partial fills (21/08 20:30)

## Contexte

Le moteur ACE777 tourne sur **Binance Futures TESTNET** depuis le 14/08.
Aujourd'hui on a découvert un problème critique :

### Le problème
1. Le CSV du moteur affiche **+18$ brut** aujourd'hui (258 fills)
2. Binance montre **-131$ realized** (1448 trades)
3. **98% des trades Binance ne sont PAS dans le CSV**

### La cause racine (prouvée)
Binance **split les ordres en 3-5 partial fills** :
```
CSV:   1 trade  qty=0.0785  (agrégé)
Binance: 3 trades qty=0.0423 + 0.015 + 0.0212  (3 commissions séparées)
```

- 251 "big phantoms" (partial fills) = **-100$** de pertes non loggées
- 1171 micro-phantoms = **-26$** supplémentaires
- Les STOP_MARKET échouent (error -1106) → le filet physique ne fonctionne pas

### Les frais
| Exchange | Maker | Taker | Partial fills |
|---|---|---|---|
| Binance | 0.02% | 0.04% | Oui (agressif) |
| MEXC | 0% | 0.02% | Moins agressif |
| Hyperliquid | 0% | 0.01% | Rare |

### Le constat
Avec 20bps de frais + partial fills qui multiplient les commissions, le bot est **structurellement perdant** sur Binance. Même un win rate de 66% ne suffit pas.

## Questions pour la famille

1. **Faut-il changer d'exchange ?** Si oui, MEXC ou Hyperliquid ? (les 2 ont des testnets)

2. **Le problème des partial fills est-il spécifique à Binance ou est-ce un problème du moteur ?** (le moteur place des ordres MARKET qui se font split par la liquidité)

3. **Le filet STOP_MARKET (error -1106) est-il réparable ?** Sans filet physique, le bot est sans protection.

4. **Le PnL brut du CSV est-il fiable ?** Si on soustrait les vrais frais Binance, le bot est-il rentable en théorie ?

5. **Recommandation exchange** pour un scalping bot qui fait 250-1400 trades/jour avec des qty de 0.005-0.13 BTC.

## Contraintes
- Christophe veut des PREUVES, pas des suppositions
- Le test doit être reproductible
- Réversible (on peut toujours revenir sur Binance)
