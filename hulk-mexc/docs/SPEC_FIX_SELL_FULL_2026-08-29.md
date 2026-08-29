# SPEC — HULK : REMPLACER LA COUPE 100% (SELL FULL) PAR DES SORTIES EN CASCADE — 29/08/2026

**Statut :** à consulter famille + Cortana · **Fichier cible :** `hulk-mexc/scripts/paper_diprip.py`
**Auteur :** Buffy (assistante) — le constat, l'audit du code et cette SPEC n'ont **modifié aucun code** (lecture seule).

---

## CONTEXTE COMPLET (fondamental — tout est vrai, rien n'est inventé)

- **Portefeuille** : paper HULK MEXC, 15 small-caps, 22/07 → 29/08/2026. Stratégie dip&rip
  (achat dip, vente rip, mise→2×→bag, DCA, compound). 786 BUY, 378 SELL_PARTIAL,
  166 SELL full, 1336 trades exécutés.
- **Signal amplitude** (move24 = range haut-bas 24h) : patron « dormance→pic », 54-78 %
  du temps sous la moyenne, pics 2-5×. **L'amplitude prédit le MOUVEMENT, pas la
  direction** : après un pic, le prix continue de monter 70-100 % du temps.
- **Croisement sorties** (données réelles) :
  - SELL_PARTIAL (délester 30-50 %) : **+83,96 $** (moy +0,22), gagnant même en
    amplitude forte (+0,19). Meilleur en IMPULSE_WAIT (252 trades).
  - SELL full (couper 100 %) : **−153,24 $** (moy −0,92), pire en amplitude forte
    (−1,57 $). Pire régimes : COOLING (61), IMPULSE (42).
  - fearGreed identique (~68) aux deux types → biais **mécanique**, pas émotionnel.
- **Convergence IA** (29/08, contexte complet injecté à chaque fois) :
  - Cortana (boucle 5 tours) : cause racine = « binarité de la sortie totale » ;
    détail : micro-lots résiduels (poussières) qui sédimentent.
  - Famille (trio + juge) : **SOUS CONDITION** — interdire SELL_full en forte amplitude,
    cascade SELL_PARTIAL par paliers (30 %) + trailing + breakeven, Dynamic Dominance
    Gate (taille ×0,5), routage post-only, 15 % des gains partiels → DCA, Dust Sweeper.

## L'AUDIT DU CODE (fait, lecture seule) — le déclencheur du SELL full

Dans `paper_diprip.py`, `sell_trade(pair, price, reason, qty=None)` :
- `qty=None` → vend **toute** la position → event = **SELL** (ligne 1672)
- **3 appels sans qty** (vente 100 %) :

| Ligne | Déclencheur | Raison |
|---|---|---|
| 1894 | `chg <= -stop%` avant 2× (trailing armé) | `stop-X%_avant_2x` |
| 1918 | `chg <= -stop%` avant 2× (sans trailing) | `stop-X%_avant_2x` |
| 1940 | pic ≥ arm puis redonne `giveback` % | `trailing_peakY%_givebackZ` |

- Le stop (lignes 407-410) : `stop = max(stop_floor 4%, cadence × 0.70)` — un % du prix,
  **sans vérifier si c'est une vraie invalidation** (VWAP rejeté, volume) ni distinguer
  le régime. Un recul de 4-6 % en COOLING/IMPULSE sur une small cap à forte amplitude =
  respiration normale (le prix remonte 70-100 % du temps) → la coupe tombe au pire moment.

## LE FIX PROPOSÉ (à valider AVANT toute modification)

### Bloc 1 — Interdire la coupe 100 % en forte amplitude
Dans les 2 branches stop (1894/1918) : si `move24` (amplitude) > seuil
(`SELL_FULL_AMPLITUDE_GUARD`, défaut 12 %) ET pas de confirmation d'invalidation,
remplacer `sell_trade(qty=None)` par une vente **partielle** (50 %) :
```python
# exemple de logique (à affiner au moment du codage)
if chg <= -stop_pct:
    if amplitude_haute and not invalidation_confirmee:
        proceeds = self.sell_trade(pair, price, "stop_partiel_amplitude_haute", qty=qty*0.5)
    else:
        proceeds = self.sell_trade(pair, price, f"stop-{stop}%_avant_2x")
```

### Bloc 2 — Filtre de confirmation d'invalidation (proposition juge)
La coupe **complète** (100 %) n'est autorisée que si le prix **rejette le VWAP 1H**
ET que le delta de volume est négatif (> 2,5σ) — sinon sortie partielle uniquement.
Config : `SELL_FULL_REQUIRE_INVALIDATION=1`.

### Bloc 3 — Cascade de sortie par paliers (proposition famille/Cortana)
Quand la position est en plus-value et se dégrade, vendre par paliers (30 % / 30 % /
reste) au lieu de tout d'un coup, avec trailing stop + déplacement du breakeven
déjà en place. Réutiliser le mécanisme existant de `rip_scaleout` (paliers 25 %).

### Bloc 4 — Traçage rétroactif
Ajouter un compteur `SELL_FULL_BY_REGIME` (COOLING/IMPULSE/IMPULSE_WAIT/WATCH) dans
le CSV pour mesurer l'effet après déploiement — et pouvoir comparer avant/après.

### Config (defaults.env, réversible)
```bash
# Garde-fou SELL full en forte amplitude (29/08)
SELL_FULL_AMPLITUDE_GUARD=12
SELL_FULL_REQUIRE_INVALIDATION=1
SELL_PARTIAL_CASCADE=1
```

## LIVRABLES (contrat de sortie)

1. Code appliqué dans `paper_diprip.py` (3 blocs + config), réversible.
2. La section PREUVE « meilleure logique » (clause permanente Christophe 14/08) :
   montrer avec les données passées combien −153 $ se seraient réduits avec la règle.
3. Une amélioration prouvée supplémentaire (UNE, bornée, sans effet de bord).
4. Rien d'autre — pas de réécriture, pas de feature.

## PRÉCAUTIONS

- Aucune modification faite à ce jour (lecture seule, 29/08).
- Circuit obligatoire : SPEC → famille + Cortana → juge → GO Christophe → test →
  déploiement réversible. Le moteur tourne en `--resume` ; tout changement devra
  être compatible et testable en paper.
