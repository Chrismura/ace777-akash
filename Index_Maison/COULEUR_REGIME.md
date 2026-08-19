# COULEUR RÉGIME — portefeuille Hulk (19/08/2026)

> Un seul signal lisible pour Hulk, nettoyé du bruit. La couleur = **l'onchain
> (le brut, la vérité) filtré par le narratif (le bruit)**. Boucle auto-nourrie
> (comme El Niño / La Niña) : on note, on score vs le prix réel, on s'ajuste.
> **OBSERVATION par défaut** : on ne trade PAS, on mesure.

## La matrice

| Narratif | Onchain (brut) | Couleur | Sens |
|---|---|---|---|
| bullish | bullish | 🟢 **VERT** | aligné → favorable à l'entrée |
| bearish | bullish | 🟡 **JAUNE** | contrarian : accumulation discrète → opportunité à confirmer |
| bullish | bearish | 🔴 **ROUGE** | le piège → **NE PAS ENTRER** |
| bearish | bearish | ⚫ **NOIR** | aligné baissier → rester dehors |
| (neutre) | (neutre) | 🟠 **ORANGE** | pas assez de signal → attendre |

## La boucle auto-nourrie

```
couleur du jour (horizon 24h)
        ↓ attendre l'horizon
SCORE vs prix réel : HIT/MISS  (comme score_justesse pour Cortana)
        ↓
LEÇONS : les couleurs fiables sont gardées fortes, les autres ramollies
        ↓
la couleur s'ajuste toute seule au fil des saisons
```

## Sources
- **Onchain** (brut) : `whaleDir` (surveiller_whales) + poussière + blocs privatisés.
- **Narratif** : Fear&Greed (< 50 = peur, > 50 = greed).

## Plists
- `couleur-regime` → note la couleur à **08h05** et **15h55**.
- `couleur-regime-score` → score + leçons à **16h30**.

## Précédent de validation (à respecter)
La couleur **ne touche pas le capital** tant que la boucle justesse n'a pas
prouvé qu'elle a raison plus souvent que le hasard (min 5 échantillons/couleur).
Après validation : famille → juge → backtest → GO Christophe.
