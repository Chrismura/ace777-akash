# CHANTIER — FIX LAST-LOSS TTL revenge (16/08/2026)

**Statut :** ✅ appliqué + vérifié · re-scellage `8bce77b1` · **réversible**
**Remplace :** `CHANTIER_FIX_HEARTBEAT_TTL_2026-08-15.md` (fix du 15/08, cause de la chute du PnL)

---

## Pourquoi (résumé de l'analyse — détail : `ANALYSE_RUNS_2026-08-16.md`)

Le fix du 15/08 (FIX-HEARTBEAT : figer `ts_ms` sur perte close) a **éteint complètement** le
revenge du HUNTER (ALPHA) dans le run de nuit 15/08 21:53 → 16/08 06:03 :

| Run | Fills ALPHA | hunter_revenge_1.5x | PnL ALPHA | PnL total |
|-----|-------------|----------------------|-----------|-----------|
| 14/08 12:51–15:57 | 65 | 52 | +28.26 | +28.65 |
| 14/08 21:45→15/08 05:44 | 56 | 51 | +8.61 | +11.11 |
| 15/08 14:05–21:50 (avant fix, lancé 14:05) | 36 | 24 | +0.81 | +2.17 |
| **15/08 21:53→16/08 06:03 (DERNIER, avec fix)** | **12** | **0** | **−0.08** | **+0.28** |

Cause : avec le fix, la fenêtre de revenge après une perte SCOUT était bornée à 20s
(`DUO_EVENT_TTL_SEC`) puis `stale_state` ; en marché calme le radar ALPHA bloque 72–81% des
cycles (`momentum_too_small`) → le HUNTER ne trouvait presque jamais de fenêtre → 0 revenge.

## Le fix appliqué (FIX-LAST-LOSS)

Principe (recommandation nvidia du verdict famille du 15/08) : **ne plus figer `ts_ms`** — le
heartbeat rafraîchit toujours le fichier (plus de `stale_state` parasite) — et le **TTL revenge
se base sur un nouveau champ `last_loss_ts`** (horodatage de la perte close SCOUT).

### Modifs dans `LE_VRAI_CHAMPION_CERTIFIE_37FCA367.txt` (4 blocs + 1 variable)

1. **Variable** (près de `DUO_EVENT_TTL_SEC`) :
   ```bash
   DUO_REVENGE_TTL_SEC="${DUO_REVENGE_TTL_SEC:-120}"   # fenêtre revenge après perte SCOUT close
   ```
2. **`duo_publish_state()`** : ajoute `last_loss_ts` = now quand `CLOSED && pnl<0`, sinon `null`.
3. **`duo_touch_heartbeat_force()`** : supprime le `unless` du FIX-HEARTBEAT → refresh `ts_ms`
   **toujours** (retour au comportement d'avant le 15/08 pour le heartbeat).
4. **`duo_hunter_signal()` (Ruby)** :
   - `revenge_ttl=(Integer(ARGV[18]) rescue 120)`
   - `loss_age = last_loss_ts > 0 ? now − last_loss_ts : age` (fallback rétrocompatible)
   - `revenge = ... && loss_age <= revenge_ttl*1000`
   - si perte close mais TTL expiré → `out_reason="revenge_ttl_expired"` (**métrique de validation** : visible dans le CSV en `reason=` et dans le log `| duo revenge_ttl_expired`)
5. **Ligne des args Ruby** : `"$DUO_REVENGE_TTL_SEC"` ajouté en 19e argument.

## Vérifications faites (16/08)

- `bash -n LE_VRAI_CHAMPION_CERTIFIE_37FCA367.txt` : OK
- `ruby -c` sur le heredoc de `duo_hunter_signal` : OK
- Test fonctionnel 4/4 :
  - perte récente (5s) → `allow=true mode=revenge mult=1.5` ✅
  - perte vieille (200s > TTL 120s) → `allow=false reason=revenge_ttl_expired` ✅
  - état OPEN → `no_trigger` ✅
  - ancien duo_state sans `last_loss_ts` → fallback `age` → revenge ✅
- Diff limité aux 5 blocs du fix (vs `BAK_avant_fix_last_loss_ttl_20260816`)

## Re-scellement

- md5 genesis : `95d93d508c030c5718550096e966a929` → **`8bce77b17a3c2f8f40a0b6b92ce0b4bc`**
- Réfs md5 mises à jour : `GO_VORTEX_V2.sh` (prefix `8bce77b1`), `scripts/preflight_ace777.sh`,
  `scripts/verif_pre_run_3x.sh`, `scripts/verif_setup_champion.sh`

## 🔙 RETOUR ARRIÈRE (réversible)

- **Revenir avant CE fix (FIX-HEARTBEAT du 15/08 actif)** :
  ```bash
  cp ~/ace777-test-day1/LE_VRAI_CHAMPION_CERTIFIE_37FCA367.txt.BAK_avant_fix_last_loss_ttl_20260816 ~/ace777-test-day1/LE_VRAI_CHAMPION_CERTIFIE_37FCA367.txt
  # puis remettre les réfs md5 sur 95d93d50 (GO_VORTEX_V2.sh + scripts/preflight_ace777.sh + verif_pre_run_3x.sh + verif_setup_champion.sh)
  ```
- **Revenir avant le fix du 15/08 (comportement d'avant — revenge sans TTL)** :
  ```bash
  cp ~/ace777-test-day1/genesis_manifest.txt.BAK_avant_fix_heartbeat_20260815-152847 ~/ace777-test-day1/LE_VRAI_CHAMPION_CERTIFIE_37FCA367.txt
  # puis réfs md5 sur fe2a7bcc
  ```

## Métrique de validation (à regarder après le run de test)

- `%revenge` des fills ALPHA (size_note=`hunter_revenge_*`) : cible **30–60%** (pas 0, pas 89%)
- compteur `revenge_ttl_expired` dans les skips duo_wait (nouvelle raison)
- `stale_state` : doit rester ~0 (le heartbeat ne fige plus)

## Commande de test (datée 16/08)

```bash
cd ~/ace777-test-day1 && ./GO_VORTEX_V2.sh 02:00:00
```
→ voir INDEX_COMMANDES §11. Après le test : lire `runs/RAPPORT_PNL_AUTO_*.md` (le plus récent) + `engle/journal/ENGLE_JOURNAL_DERNIER.md`.

---
*Généré par Buffy le 16/08 — analyse complète : `ANALYSE_RUNS_2026-08-16.md`.*
