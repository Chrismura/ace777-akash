# Erreur Binance -2028 : Leverage insufficient margin

## Message
```
Abort leverage error: code=-2028 msg=Leverage is smaller than permitted: insufficient margin balance
```

## Signification
Erreur Binance Futures : **solde de marge insuffisant** pour le levier demandé.

Quand le script essaie de définir le levier (ex: 3 pour BETA), Binance vérifie que le compte a assez de marge. Si le solde testnet est trop bas, la requête échoue.

## Solutions

1. **Recharger le testnet** : Binance Futures Testnet permet d'obtenir des USDT gratuits :
   - https://testnet.binancefuture.com
   - Section "Get testnet funds" ou similaire

2. **Réduire le levier BETA** : Dans `launch_test_master_base_v8_5_impact.sh`, changer :
   ```bash
   export LEVERAGE="3"   # pour BETA
   ```
   en `LEVERAGE="1"` ou `LEVERAGE="5"` (parfois 5 demande moins de marge qu'un levier intermédiaire selon le symbole)

3. **Réduire BUY_USDT** : Diminuer `BUY_USDT_BETA` (200) et `BUY_USDT_ALPHA` (800) pour des positions plus petites.
