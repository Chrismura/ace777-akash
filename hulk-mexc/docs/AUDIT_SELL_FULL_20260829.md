# AUDIT — DÉCLENCHEUR DU SELL FULL (coupe 100 %) dans le moteur Hulk

**Date** : 29/08/2026
**Auteur** : Buffy (assistante) — **lecture seule, AUCUNE modification du moteur**
**Contexte** : le croisement Hulk × indices (1336 trades) montre SELL_PARTIAL = +84 $,
SELL full = −153 $. Les 3 IA (Cortana, famille, Buffy) convergent : la coupe à 100 %
est le problème n°1. Le juge a exigé « à vérifier d'abord » : le SELL full est-il
déclenché par un faux signal COOLING/IMPULSE ?

---

## 1. CE QUI DÉCLENCHE UNE VENTE COMPLÈTE (event = SELL)

Dans `paper_driprip.py`, `sell_trade(pair, price, reason, qty=None)` :
- **qty=None** → vend **toute** la position → event = **SELL** (ligne 1672)
- **qty=partiel** → event = **SELL_PARTIAL**

**Les 3 appels SANS qty (vente 100 %) :**

| Ligne | Déclencheur | Raison |
|---|---|---|
| **1894** | `chg <= -stop%` **avant 2×** (avec trailing armé) | `stop-X%_avant_2x` |
| **1918** | `chg <= -stop%` avant 2× (sans trailing) | `stop-X%_avant_2x` |
| **1940** | **trailing :** pic ≥ arm puis redonne `giveback` % sous le pic | `trailing_peakY%_givebackZ` |

**Le stop (ligne 407-410)** : `stop = max(stop_floor 4%, cadence × 0.70)` — le stop est
**proportionnel à la cadence** (volatilité). Quand la cadence monte (amplitude forte),
le stop s'élargit… mais quand le prix baisse de ce % en régime COOLING/IMPULSE, la
coupe tombe à 100 %.

## 2. VERDICT DE L'AUDIT (confirme le soupçon du juge)

**OUI — les SELL full se concentrent sur les faux signaux :**

1. **Stop avant 2× (1894/1918)** : le moteur coupe **tout** si le prix baisse de `stop%`
   AVANT d'avoir atteint +100 % (2×). Or dans les small caps à forte amplitude, un
   recul de 4-6 % en régime COOLING est **une respiration normale**, pas une invalidation
   — le patron « dormance→pic » montre que le prix remonte 70-100 % du temps après un creux.
2. **Aucune différenciation par régime** : le même stop % est appliqué en COOLING/IMPULSE,
   alors que le croisement montre que ces régimes sont **précisément ceux où le SELL full
   perd le plus** (COOLING 61 SELL, IMPULSE 42 SELL).
3. **Trailing giveback (1940)** : sortie totale quand le prix redonne `giveback` % sous le
   pic — même mécanique binaire.

**En résumé** : le moteur coupe à 100 % sur **un stop en % du prix**, sans vérifier si
c'est une vraie invalidation (VWAP 1H rejeté, volume) ou une simple respiration de
l'amplitude. C'est exactement le « coupe-gorge » décrit par la famille.

## 3. CONSTAT CHIFFRÉ (rétroactif, depuis les données)

- SELL full : **166 trades, −153,24 $** (−0,92 $ moyen)
  - Amplitude forte : **−1,57 $ moyen** (le pire)
  - Régimes : COOLING 61, IMPULSE 42, IMPULSE_WAIT 61
- SELL_PARTIAL : **378 trades, +83,96 $** (+0,22 $ moyen), gagnant même en amplitude forte

## 4. PISTES (à décider AVANT toute modification — AUCUN changement fait ici)

1. **Interdire SELL full en amplitude forte** : transformer la coupe 100 % en vente
   partielle (ex. 50 %) quand `move24` dépasse un seuil, sauf vrai signal d'invalidation.
2. **Filtre de confirmation** : ne couper à 100 % que si rejet du VWAP 1H + delta volume
   négatif (proposition juge) — sinon sortie partielle seulement.
3. **Palier de sortie** : remplacer le stop binaire par une cascade SELL_PARTIAL 30 % +
   trailing + breakeven (proposition famille/Cortana).
4. **Traçage** : ajouter un compteur de SELL full par régime pour suivre l'effet après
   changement.

## 5. PRÉCAUTIONS PRISES

- **Aucune modification** du moteur (lecture seule, 29/08).
- Ce document est la **trace rétroactive** de l'audit.
- Toute modification future devra passer par le circuit habituel (SPEC → famille →
  juge → GO Christophe → test) et être réversible.
