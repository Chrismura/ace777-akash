# VERDICT FAMILLE — Garde-fou PRIX FIGÉ (price_stasis) — 16/08/2026

**Consultation :** 4 modèles consultés (gemini 3.9s · nvidia 118.8s · deepseek-v4 97.7s ·
codestral 2.7s). OpenRouter (juge/ultra) HS (502) → remplacés par deepseek + codestral.
**Statut :** ✅ **GO-AVEC-RÉSERVE** (4/4 GO-AVEC-RÉSERVE) — consensus très large.

## Réponses aux 4 questions

| # | Question | Consensus famille | Décision retenue |
|---|---|---|---|
| 1 | Seuils 1.0 bps / 30s ? | Nvidia : OK. Gemini + Deepseek : **0.5 bps** (1.0 risque de bloquer les entrées sur testnet calme). Codestral : OK. | **0.5 bps / 30s** (moyenne des avis, réversible par env) |
| 2 | Défaut TRUE ou FALSE ? | **TRUE partout** (3/3 explicites ; 43% de fills flat justifient une sécurité active) | **TRUE** |
| 3 | Skip classique ou métrique dédiée ? | **Métrique dédiée** (nvidia, gemini, deepseek) — un skip price_stasis n'est pas un skip classique | **Compteur `price_stasis_skips` dans le rapport** |
| 4 | Exception « wall collapse » (tension très haute) ? | Pour : gemini (seuil critique), deepseek (**tension > 15**), codestral (> 50). Contre : nvidia (un mur qui fond sans mouvement de prix = liquidité illusoire, l'exception créerait une faille) | **Exception tension > 15** (majorité 3/4, borne haute = n'ouvre que sur tension extrême) |

## Ajustements décidés (intégrés à la SPEC)

1. **Seuil mouvement** : `PRICE_STASIS_MIN_MOVE_BPS=0.5` (au lieu de 1.0).
2. **Exception wall collapse** : si `tension > 15` → pas de check price_stasis (la tension est
   déjà calculée par le radar et dispo dans le contexte).
3. **Log enrichi** : le skip `price_stasis` logge aussi `ref_px` et `p2` (debug post-run).
4. **Compteur** : `price_stasis_skips` incrémenté et rapporté en fin de run.
5. La fenêtre 30s et le défaut TRUE sont conservés tels quels.

## Réserves notées (suivi)

- **Nvidia** : le garde-fou traite le symptôme, pas la cause (liquidité testnet) — filet de
  sécurité temporaire, à surveiller sur 24h ; si les fills flat persistent malgré 0 skips →
  investiguer l'exécution (slippage/ordre) plutôt que le radar.
- **Gemini** : latence du `ruby` dans la boucle — accepté (calcul < 50ms, déjà utilisé ailleurs).
- **Deepseek** : vérifier l'interaction avec le fix last_loss_ts (le check est APRÈS le duo →
  pas d'interaction ; un revenge reste possible dès que le prix bouge).

## Ce qui changerait l'avis

- Fills flat corrélés à des mouvements de prix > 0.5 bps / 30s → le garde-fou n'aurait pas bloqué → NO-GO.
- Skip massif des entrées gagnantes sur marché vivant → seuils trop stricts → ajuster (0.3 bps ou fenêtre 15s).

## SYNTHÈSE

Diagnostic partagé : le radar entre sur des signaux de carnet non confirmés par le prix (marché
mort/testnet) → trades nuls. Action : implémenter `price_stasis` (0.5 bps / 30s, TRUE, compteur
dédié, exception tension > 15), surveiller le taux de skip sur 24h, puis traiter la cause racine
(liquidité) si besoin. Le fix last_loss_ts du matin n'est pas impacté (check après le duo).
