# 🔍 ENQUÊTE MORT RC=1 SILENCIEUSE — CAUSE RACINE PROUVÉE (14/08/2026)

## 🎯 CONCLUSION EN UNE PHRASE

**La mort rc=1 silencieuse vient d'un SI conditionnel piégé à la fin de `swarm_neighbor_load()` : quand une shockwave a été armée (après une perte) et que le cycle du bot dépasse la fenêtre + grâce, la fonction retourne 1, et `swarm_apply_coupling` l'appelle SANS protection → `set -e` tue le bash en rc=1 — sans que le trap ERR se déclenche (le genesis n'a pas `set -E`).**

---

## 1 · CE QUE TU SOUPÇONNAIS ÉTAIT EXACT : UN « SI » CONDITIONNEL

> *« si je voulais saboter je ne mettrais pas une valeur fixe mais par exemple un SI »*

**Le SI existe.** Il est à la fin de `swarm_neighbor_load()` (genesis, ~ligne 606-612) :

```bash
if [ "$swarm_shockwave_active" = "0" ] && [ "${swarm_shockwave_until_cycle:-0}" -gt 0 ]; then
    shock_until_i="$(to_int "$swarm_shockwave_until_cycle")"
    cycle_i="$(to_int "$cycle")"
    if [ "$cycle_i" -gt "$shock_until_i" ]; then
      post_delta=$((cycle_i - shock_until_i))
      post_grace_i="$(to_int "$SWARM_HUNTER_POST_SHOCKWAVE_SOLO_CYCLES")"
      [ "$post_delta" -le "$post_grace_i" ] && swarm_shockwave_post_solo=1    # ← SI PIÉGÉ
    fi
  fi
```

Quand `post_delta > post_grace` (20 cycles), la commande `[ ... ]` retourne **1** → c'est la DERNIÈRE commande de la fonction → la fonction retourne **1**.

## 2 · LA CHAÎNE COMPLÈTE DE LA MORT (chaque maillon prouvé)

| # | Maillon | Preuve |
|---|---|---|
| 1 | Un bot perd un trade ou stop_loss → `swarm_broadcast_shockwave` (ligne 2477) | Crash dump 12:14 : `shockwave alpha->beta until_cycle=49` après perte |
| 2 | La télémetrie stocke `{alpha,beta}_shockwave_until_cycle = cycle + 10` | `scripts/swarm_telemetry.rb` lignes 144/160/176 |
| 3 | Le bot voisin lit la télémetrie → `swarm_shockwave_until_cycle > 0` | `eval "$(ruby read)"` dans `swarm_neighbor_load` |
| 4 | Quand le cycle dépasse `until + grâce(20)` → le SI retourne 1 | **Preuve machine** (test harnais ci-dessous) |
| 5 | `swarm_apply_coupling` appelle `swarm_neighbor_load "$cycle"` SANS `\|\|` (ligne 621) | Lecture directe du code |
| 6 | `set -euo pipefail` SANS `set -E` → l'échec DANS une fonction ne déclenche PAS le trap ERR | **Preuve machine** : zéro FATAL_RC1, zéro stderr, rc=1 |

## 3 · PREUVE MACHINE (reproduction exacte)

Test harnais avec la structure EXACTE du genesis (`set -euo pipefail`, pas de `set -E`) :

```
--- TEST 1 : cycle 17 (post_delta=2 <= 20) -> survit
SURVIT (rc=0) - OK attendu
--- TEST 2 : cycle 100 (post_delta=85 > 20) -> MOURIR en rc=1
>>> EXIT TRAP rc=1          ← mort rc=1
(AUCUN "FATAL_RC1 TRIGGERE")  ← trap ERR MUET, exactement comme les morts réelles
RC GLOBAL DU SCRIPT = 1
```

## 4 · PREUVE CINÉTIQUE (crash dump 12:14, séquence complète)

```
12:13:14  BETA SELL tension=3.42 pnl=+0.097 (gain)
12:13:23  ALPHA broadcast shockwave alpha->beta until_cycle=49   ← après perte (fluid_exit_inversion)
12:13:31  ALPHA BUY pnl=-8.60 (GROSSE PERTE)
12:14:25  ALPHA MEURT rc=1   (~54s après sa perte : le SI armé par une shockwave antérieure de BETA)
12:17:27  BETA MEURT rc=1    (~4 min après : quand son cycle > 49 + grâce 20 ≈ 69)
```

**Timing cohérent** : ~30 cycles × ~8s ≈ 4 min entre la shockwave et la mort du voisin.

## 5 · POURQUOI LE CHAMPION (+126$) NE MOURAIT PAS

**Le SI est DANS le vrai champion scellé `37fca367`** (md5 vérifié : `37fca36712d49aa8b97890c5cad5f2e6`) — il n'a PAS été ajouté par la main extérieure. C'est un **bug latent** :

- Le SI ne se déclenche que si une shockwave est ARMÉE (perte/stop_loss → broadcast)
- Le champion GAGNAIT → pas de pertes → pas de shockwaves → le SI jamais armé → jamais déclenché
- Aujourd'hui : testnet lent/volatile → pertes → shockwaves → le SI s'arme → mort en cascade

**Ce n'est pas un sabotage. C'est un bug dormant du moteur rentable, réveillé par les pertes.**

## 6 · PREUVE PAR CONTRASTE (le run actuel)

| Session | Shockwaves broadcastées | Sortie |
|---|---|---|
| 12:06 / 12:07 / 12:14 / 12:17 | OUI (pertes → shockwaves) | 💀 rc=1 à 8-17 min |
| **Run actuel (12:17+, 18+ min)** | **0 shockwave** | ✅ **VIVANT** |

Le run actuel a largement dépassé la fenêtre des morts (8-17 min) : **sans shockwave, pas de SI armé, pas de mort.**

## 7 · CORRECTIFS POSSIBLES (à soumettre famille + juge — PAS encore appliqués)

1. **`return 0` explicite à la fin de `swarm_neighbor_load`** (le plus propre : la fonction fait du bookkeeping, elle ne doit jamais être une source d'erreur)
2. **`swarm_neighbor_load "$cycle" || true`** dans `swarm_apply_coupling` (protège l'appel, ne change pas la logique)
3. **`set -E` dans le genesis** (rend la mort LOUD — FATAL_RC1 écrit — sans la résoudre ; à combiner avec 1 ou 2)

**Règle respectée : RIEN n'a été modifié. Le genesis est intact. Le run de capture continue de tourner (18+ min, vivant).**

---

*Rapport rédigé par Buffy (superviseur) — 14/08/2026, en l'absence de Christophe, avec son autorisation de test.*
*Preuves : tests harnais /tmp/test_swarm_si2.sh, crash dumps runs/CRASH_DUMP_*, md5 scellé vérifié.*

---

## ✅ RÉSULTAT FINAL DU RUN DE 4H — 14/08 (16:00Z)

### Le fix est PROUVÉ en conditions réelles

| Métrique | Avant fix (matin) | Après fix (session 12:51→15:57Z) |
|---|---|---|
| Durée de vie des bots | 8-17 min (4 morts rc=1) | **3h06 sans une seule mort** |
| Cycle max atteint | ~134 (mort à 8-17 min) | **#1321 (ALPHA) / #1245 (BETA)** |
| Shockwaves traversées | 1 shockwave = mort assurée | **358 shockwaves à cycle > 200** (dont 25 à 900+), 0 mort |
| Fin de session | rc=1 silencieux | **rc=0 propre (durée 4h atteinte)** |

### PNL de la session fixée (testnet, 12:51→15:57Z)
- **ALPHA** : 65 trades FILLED → **+28.26 $**
- **BETA** : 155 trades FILLED → **+0.40 $**
- **Total : +28.66 $ sur 3h06** (≈ +9.3 $/h, marché calme en fin de session — beaucoup de SKIP momentum_too_small)

### Chronologie complète des morts (PRE-FIX) vs session fixée
- 12:06 / 12:07 / 12:14 / 12:17 / 12:37 / 12:40 → toutes rc=1 sur le SI piégé (après shockwave)
- 12:48 → mes kills volontaires (rc=143) pour recharger le genesis corrigé
- **12:51 → 15:57 : session fixée, 3h06, ZERO mort, rc=0**

### Conclusion
La cause racine (SI piégé dans `swarm_neighbor_load` sans `set -E`) est éliminée. Le moteur tourne en continu avec le correctif validé 3/3 GO (gemini, nvidia, puter-grok). Prochaine étape : run long de validation + retour au réel.
