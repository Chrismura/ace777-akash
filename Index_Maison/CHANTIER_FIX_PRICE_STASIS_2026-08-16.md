# CHANTIER — FIX-PRICE-STASIS (garde-fou « prix figé ») — 16/08/2026

**Statut :** ✅ IMPLÉMENTÉ + RE-SCELLÉ (md5 `8bce77b1…`) · **Validation :** bash -n OK, logique testée
**Verdict famille :** 4/4 GO-AVEC-RÉSERVE (`scripts/CONSULTATION_FAMILLE_PRICE_STASIS_20260816/VERDICT_FAMILLE.md`)

## Contexte

Run de test du 16/08 07:19Z (avec FIX-LAST-LOSS du matin) : **10 fills BETA dont 8 à pnl
exactement 0.00000000** (entrée = sortie au même prix, hold 7–8s). Ex. fill #100 :
tension=10.67, bid_drop=69.4%, conf=0.9993 … prix FIGÉ à 63035.10 depuis 5 min.
Le radar entre sur des signaux de carnet (murs qui fondent) alors que le prix ne bouge pas
(marché sans liquidité / testnet calme) → fausse « rupture imminente » → ordre → sortie flat
→ trades nuls + frais. Pattern déjà présent au run de nuit (69/160 fills BETA flat = 43%).
« Rupture harmonique » repérée par Christophe — confirmée par l'analyse des logs.

## Le fix (4 blocs dans `LE_VRAI_CHAMPION_CERTIFIE_37FCA367.txt`)

Principe : **ne pas entrer si le prix n'a pas bougé d'au moins 0.5 bps sur les 30 dernières secondes.**

1. **Variables** (près des `STASE_DYNAMIQUE_*`) :
   ```bash
   PRICE_STASIS_GUARD="${PRICE_STASIS_GUARD:-TRUE}"          # on/off (env)
   PRICE_STASIS_MIN_MOVE_BPS="${PRICE_STASIS_MIN_MOVE_BPS:-0.5}"   # 0.5 bps (verdict famille)
   PRICE_STASIS_WINDOW_SEC="${PRICE_STASIS_WINDOW_SEC:-30}"        # fenêtre 30s
   PRICE_STASIS_TENSION_BYPASS="${PRICE_STASIS_TENSION_BYPASS:-15}" # exception wall collapse
   ```
2. **État glissant** (avant la boucle) : `price_stasis_skips=0`, `price_stasis_ref_px=""`, `price_stasis_ref_ts=""`.
3. **Check** juste AVANT l'exécution de l'ordre (après toutes les gates radar→tactic→stase→duo→qty→llm_gate) :
   référence posée au 1er cycle ; à chaque cycle ≥ 30s, si mouvement < 0.5 bps → SKIP
   `price_stasis` (raison `price_frozen`, avec move_bps/window/ref_px/p2/tension dans le CSV)
   + compteur incrémenté. Exception : tension > 15 → bypass (wall collapse légitime).
   Le check est dans la section COMMUNE → s'applique au SCOUT (BETA) et au HUNTER (ALPHA).
4. **Rapport** : `price_stasis skips (prix figé): N` affiché en fin de run.

Le FIX-LAST-LOSS du matin n'est **pas** touché (check après le duo → revenge intact dès que
le prix bouge).

## Décisions famille intégrées (verdict 16/08)

| Question | Verdict | Décision |
|---|---|---|
| Seuils | gemini+deepseek : 0.5 bps (1.0 trop strict) | **0.5 bps / 30s** |
| Défaut | TRUE partout | **TRUE** (réversible par env) |
| Métrique | dédiée | **compteur en fin de run** |
| Exception wall collapse | 3/4 pour | **tension > 15 = bypass** |

Réserves : nvidia — filet de sécurité temporaire (cause racine = liquidité testnet, à
surveiller) ; gemini — latence ruby acceptée (< 50ms) ; deepseek — pas d'interaction
last_loss (vérifié : check après le duo).

## Validation

- [x] `bash -n` OK
- [x] Calcul move_bps testé : figé → 0.000000 (skip) · +2 bps → 1.998886 (entrée)
- [x] `num_lt` testé : 0 < 0.5 → SKIP OK
- [x] Backup avant fix : `LE_VRAI_CHAMPION_CERTIFIE_37FCA367.txt.BAK_avant_fix_price_stasis_20260816`
- [x] Re-scellé : md5 **`8bce77b17a3c2f8f40a0b6b92ce0b4bc`** (préfixe `8bce77b1`)
- [x] Réfs md5 mises à jour : GO_VORTEX_V2, GO_USINE_NUAGE, preflight, verif_pre_run_3x,
      verif_setup_champion, checkup_garage, cortana_cockpit_bridge, pulse_sous_loeil,
      superviseur_core, REGISTRE_SYNAPSES.json
- [ ] **En cours** : validation live sur un run de test

## Rollback (1 commande)

```bash
cd ~/ace777-test-day1 && cp LE_VRAI_CHAMPION_CERTIFIE_37FCA367.txt.BAK_avant_fix_price_stasis_20260816 LE_VRAI_CHAMPION_CERTIFIE_37FCA367.txt
# puis re-sceller et mettre à jour les réfs (md5 3d7605922ca0ac876c69611b45527bbd) — procédure habituelle
```

Alternative sans re-scellage (désactivation par env) :
`PRICE_STASIS_GUARD=FALSE ./GO_VORTEX_V2.sh 02:00:00` (le code reste, le check est inactif).

## Métriques de validation (après le prochain run)

1. **`price_stasis skips` > 0** sur marché calme (le run du matin aurait dû en avoir).
2. **%fills BETA flat (pnl=0) en baisse** : cible < 20% (43% au run de nuit, 80% au run du matin).
3. **0 skip sur marché vivant** : si le marché bouge (> 0.5 bps/30s), aucune entrée bloquée.
4. **Revenge intact** : %revenge ALPHA 30–60% quand le SCOUT perd (le fix last_loss tient).
5. PnL > +1 sur le run.

Si les fills flat persistent avec skips ≈ 0 → le problème n'est pas le prix figé mais
l'exécution (slippage/ordre) → investiguer (réserve nvidia).
