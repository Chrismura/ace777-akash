# 🛡️ ROUND TABLE FAMILLE — FILET DE SÉCURITÉ PHYSIQUE (STOP_MARKET BINANCE) — 17/08/2026

**Contexte pour la famille :** on consulte TOUTE la famille (pas seulement corriger : AMÉLIORER si vous voyez mieux). Répondez en français, structuré, honnête. Si vous proposez autre chose que la solution présentée, dites-le clairement et expliquez pourquoi c'est mieux.

---

## 📋 LE PROBLÈME (faits vérifiés dans le code, pas des suppositions)

Le moteur ACE777 (genesis_manifest.txt) ne possède **aucune protection physique** côté Binance :

1. **Le « suffer » à -0,50 $ ne ferme PAS la position ouverte.** Il est câblé sur l'ARMEMENT de la position suivante (duo_hunter_apply_sig), pas sur la SORTIE. Il donne l'illusion d'un stop USDT qui n'existe pas.

2. **La position ouverte est fermée uniquement par la boucle logicielle** (toutes les 0,5 s) : stop_loss (bps), shockwave, fluid_exit_inversion, timeout. Aucun de ces mécanismes ne regarde la perte en USDT.

3. **Aucun ordre STOP_MARKET n'est placé sur l'exchange.** J'ai cherché STOP_MARKET/stopPrice/TAKE_PROFIT dans tout le moteur : RIEN. Si la boucle meurt ou ralentit, aucune protection physique n'existe.

4. **Cas réel #157** : position x13 coupée à -7,43 $ en 7 s par fluid_exit_inversion (chute 6,5 $/s), alors qu'un stop à -1,5 $ aurait dû couper. La boucle a vu la perte trop tard (0,5 s de tick + 889 ms de latence réseau = 1,4 s de retard → dérapage ~9 $).

## 📏 MESURES RÉELLES (testnet, 17/08)

- Spread : **1,70 $** (mainnet : 0,10 $)
- Latence réseau : 339 ms → 889 ms moy → **5 384 ms max**
- Bruit prix par tick (0,5 s) : **1,00 $ moy, 5,10 $ max**
- 1 bps ≈ **1,04 $** sur une position type (~10 400 $)
- Stop actuel : 16 bps (~16,6 $) hard / 7 bps (~7,3 $) soft / DUO_HUNTER_STOP_LOSS_BPS=0 (désactivé)

## 💡 LA SOLUTION PROPOSÉE (à challenger)

**Objectif : couper à ~5,1 bps (~5,3 $) maximum, sans latence, même si le programme meurt.**

### 1. STOP_MARKET natif côté Binance à l'entrée
- À chaque ouverture de position → placer un ordre `STOP_MARKET` avec `reduceOnly=true`
- `stopPrice` = prix d'entrée réel × (1 − stop_bps/10000) (conversion bps → prix absolu, arrondi au tickSize)
- C'est Binance qui surveille en continu (millisecondes, zéro latence de notre boucle)

### 2. Annulation systématique à chaque sortie logicielle
- Quand le moteur sort par ses propres chemins (trailing, shockwave, fluid_exit, timeout, target) → **CANCEL le STOP_MARKET d'abord**, puis sortir
- Sinon : ordre orphelin = risque de short surprise (le stop se déclenche après la fermeture et ouvre une position inverse)

### 3. Le stop logiciel reste en secours
- Si le STOP_MARKET a déjà coupé → le moteur détecte la position fermée et n'agit pas (pas de double clôture)

## ⚖️ LE COMPROMIS DÉJÀ DÉCIDÉ (à valider ou challenger)

- **`DUO_HUNTER_HARD_STOP_MULT` gardé à 2.0** : quand le scout est ouvert et en perte (duo lié), le hunter peut aller jusqu'à 2× son stop (5,1 → 10,2 bps) pour soutenir le scout. C'est VOLONTAIRE (logique duo), pas un bug. On le garde pour ne pas casser la paire scout/hunter.
- **Valeurs proposées** : `STOP_LOSS_BPS=5.1`, `SOFT_STOP_LOSS_BPS=5.1`, `DUO_HUNTER_STOP_LOSS_BPS=5.1` (les 3, car la variable hunter ne couvre pas les cycles ALPHA)

## ❓ LES 4 QUESTIONS À LA FAMILLE

1. **La solution STOP_MARKET est-elle la bonne ?** Y a-t-il un piège que nous n'avons pas vu (ordre orphelin, double clôture, slippage, testnet vs mainnet, mode hedge) ?

2. **Le seuil 5,1 bps (~5,3 $) est-il juste ?** Sachant : bruit 1 $ moy / 5,10 $ max, spread testnet 1,70 $, position ~10 400 $. Trop serré (chassé par le bruit) ou trop large (perte max trop grosse) ?

3. **Le compromis HARD_STOP_MULT=2.0 (le duo peut doubler le stop quand le scout souffre) est-il cohérent avec l'harmonie ?** Ou doit-on le serrer, et à quelle valeur ?

4. **Quelle est VOTRE amélioration ?** Pas juste corriger : si vous voyez une architecture MEILLEURE que le STOP_MARKET + annulation, dites-la. (Ex : STOP_LIMIT vs STOP_MARKET, trailing côté Binance, filet en cascade, etc.)

---

**Rappel du contexte moteur (vérifié) :**
- Le moteur a déjà `private_post()` (ligne 734) et utilise déjà `reduceOnly=true` sur ses sorties
- Il n'a AUCUNE fonction d'annulation d'ordres aujourd'hui (zéro cancel/DELETE)
- Mode hedge actif (`BINANCE_HEDGE_MODE=TRUE`, `POSITION_SIDE_STRICT=TRUE`)
- Le routage : famille/Cortana → Gemini · juge → NaraRouter · codeur → Groq · analyse profonde → NVIDIA · secours → Mistral/HuggingFace
