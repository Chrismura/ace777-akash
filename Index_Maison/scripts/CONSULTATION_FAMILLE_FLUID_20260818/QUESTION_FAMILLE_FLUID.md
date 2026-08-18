# QUESTION À LA FAMILLE — fluid_exit_inversion : faut-il le relâcher ou le désactiver ?

**Date : 18/08/2026 · Contexte : run testnet 17/08 (V4 Algo Order API, setup D)**
**Règle d'économie respectée : 2 membres + le juge (plus jamais 6).**

---

## 1. Le contexte (ce qu'on cherche)

Le moteur a 3 détecteurs de « vitesse » qui coupent les positions en cours. On a mesuré leur performance réelle sur les logs du run (PNL à la coupe) :

| Détecteur | Rôle | ALPHA (x13) | BETA (x5) | Verdict |
|---|---|---|---|---|
| `shock_inversion_stop` | sort si vitesse quasi NULLE (bougie qui s'arrête) | +274,63 $ (845) | +45,05 $ (3173) | ✅ POSITIF |
| `fluid_exit_brake` | sort si vitesse > seuil dans les 2 sens | +9,09 $ (81) | +3,44 $ (284) | ⚠️ à peine positif |
| `fluid_exit_inversion` | sort si vitesse de chute > seuil | **−124,86 $** (153) | **−24,44 $** (630) | ❌ **NÉGATIF** |

**Détail de `fluid_exit_inversion` (le perdant) :**
- ALPHA : 30 en profit · 23 à zéro · **100 en perte** = −124,86 $
- BETA : 110 en profit · 75 à zéro · **445 en perte** = −24,44 $
- **Combiné : −149,30 $** sur le run, avec **545 coupes en perte** + **98 coupes à zéro** (frais payés pour rien) pour seulement 140 coupes en profit.

## 2. Le seuil en cause (mesuré)

- `FLUID_EXIT_SENSITIVITY=1.0` (défaut, aucune valeur explicite dans les lanceurs).
- Seuil réel : **0,02 bps/s = 0,129 $/s** sur BTC ~64 324 $.
- Concrètement : **une chute de 0,06 $ sur un seul tick (0,5 s) suffit à couper la position**.
- Le bruit normal de BTC (wicks de 0,5-2 $/s) dépasse largement ce seuil → coupes intempestives.

## 3. Le point IMPORTANT : ce qu'on NE touche PAS

**La philosophie « vide / résonance mécanique » de l'utilisateur est INCARNÉE par `shock_inversion_stop`** (sortie quand la bougie s'arrête, vitesse = 0, seuil 0,0001 bps/s). C'est LE détecteur positif (+319 $ combiné).

Le `fluid_exit_inversion` est un ajout distinct (« sorties fluides ») : il réagit à la **chute rapide**, pas à l'arrêt. Ce sont des mécanismes opposés. **La question ne touche PAS le vide.**

## 4. L'effet caché (découvert dans le code)

```bash
if num_lt "$pnl_usdt" "0" || echo "$reason" | grep -qiE 'stop_loss'; then
  swarm_broadcast_shockwave "$i" "$reason"
fi
```

**Toute coupe en perte → shockwave au voisin → le voisin se protège 10 cycles (spread plancher 4,0 bps → ultra-sélectif → SKIP en rafale).**
Les 545 coupes `fluid_exit_inversion` en perte = **545 fausses alertes de panique** envoyées au voisin pendant le run → l'autre agent a été gelé une bonne partie du temps.

## 5. La proposition à valider

**Option A — Relâcher** : `FLUID_EXIT_SENSITIVITY=0.1` → seuil = 1,29 $/s (10× plus de respiration, le bruit ne déclenche plus).

**Option B — Désactiver** : `FLUID_EXIT_ENABLED=FALSE` → le détecteur de chute rapide ne coupe plus ; on garde `fluid_exit_brake` + `shock_inversion_stop` (le vide).

**Option C — Garder tel quel** (si vous estimez que la protection chute vaut son coût).

## 6. Ce qu'on attend de vous

1. Votre avis honnête : la preuve chiffrée vous convainc-t-elle ?
2. Option A, B ou C ?
3. Un risque que nous aurions manqué ? (ex. : le fluid protège-t-il d'un vrai crash que les autres détecteurs ne couvrent pas ?)
4. Si vous proposez autre chose, dites-le — on cherche la MEILLEURE solution, pas juste une correction.

Terminez par : **VERDICT: GO / GO-AVEC-RÉSERVE / NO-GO + CONFIANCE: X%**
