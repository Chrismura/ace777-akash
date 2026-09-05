# RECOMMANDATION Beta — 2026-09-01

> Destiné à la famille. Pas de modification du champion.
> Données : V2, V3, V4 — 9 trades Beta — lecture seule.

---

## Constat principal

**5 trades sur 9 Beta étaient dans le mauvais sens.**

Le lanceur fixe `FORCE_ENTRY_SIDE=SELL` pour Beta (le scout).
Mais le radar indique parfois `long`.
Résultat : Beta entre SELL quand il faudrait acheter, et subit un stop_loss.

## Preuve par replay local

| | Réel | Si radar-aligned |
|---|---:|---:|
| Brut | -8,98 | **-0,51** |
| Frais | +5,03 | +5,03 |
| Net | -14,00 | **-5,54** |
| Delta | — | **+8,47** |

Sur les 4 stop_loss inversés :
- 3 seraient devenus des **gains** (même petits)
- 1 serait resté une perte

## Autres constats

1. **Confiance inversée** : les trades les plus confiants (0,999) sont les plus perdants.
2. **Trailing_stop** : positif en brut mais les frais mangent tout (+5,33 → +0,15 net).
3. **Alpha** : la seule unité capable de générer un net positif sur V2 (+0,12).

## Ce qu'il ne faut PAS faire

- ❌ Modifier les seuils `COMPRESSE` ou `spread_too_wide`
- ❌ Relancer ACE en testnet sans changement
- ❌ Toucher au champion
- ❌ Activer le LIVE

## Ce qu'il FAUT faire

### Étape 1 — Replay local avec radar-aligned (sans Binance)

Recalculer les trades Beta en supposant que l'entrée suit le signal radar.
Vérifier si le net cumulé reste négatif après frais.

### Étape 2 — Testnet court avec radar-aligned

Créer un lanceur variant qui n'utilise pas `FORCE_ENTRY_SIDE=SELL` pour Beta.
Le scout décide seul : BUY si radar=long, SELL si radar=short.
Testnet 15 minutes, même setup.

### Étape 3 — Valider le modèle de confiance

Vérifier si `conf` prédit réellement la direction ou juste la volatilité.
Si c'est la volatilité, ne pas l'utiliser comme gate d'entrée.

---

## Verdict

```text
Cause principale de perte Beta : FORCE_ENTRY_SIDE=SELL
Correction la plus sûre : supprimer FORCE_ENTRY_SIDE
Résultat attendu : réduction de ~8,5 USDT de pertes sur 45 min
Preuve : replay local, pas encore testnet
ACE LIVE : toujours interdit
```

---

*Recommandation Buffy — 2026-09-01*
