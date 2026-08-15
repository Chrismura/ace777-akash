# CHANTIER — Fix heartbeat → TTL revenge (15/08/2026)

**Statut :** ✅ appliqué + vérifié · famille 4/4 GO-AVEC-RÉSERVE · **réversible**

## Le bug
`duo_touch_heartbeat_force()` rafraîchissait `ts_ms` à chaque cycle SCOUT → `age > 20s` (L1027)
jamais vrai → `stale_state` jamais déclenché → revenge armé en permanence (TTL 20s inopérant).
Cause du %revenge ALPHA 58→89 % et du PnL erratique.

## Le fix (1 bloc)
Dans `duo_touch_heartbeat_force`, ne plus rafraîchir `ts_ms` si le dernier état scout est une
**perte close** (`status=="CLOSED" && pnl_usdt<0`) :
```
      unless j["status"].to_s == "CLOSED" && (Float(j["pnl_usdt"]) rescue 0.0) < 0.0
        j["ts_ms"]=(Time.now.to_f*1000).to_i
        ...
      end
```
Effet : `ts_ms` fige à l'instant de la perte → TTL 20s redevient opérant → revenge auto-désarmé.

## Vérifications faites
- `bash -n genesis_manifest.txt` : OK
- Syntaxe Ruby du heredoc : OK
- Test fonctionnel 3/3 : perte close → ts_ms figé ✅ · gain close → refresh ✅ · OPEN → refresh ✅
- Diff limité à la seule fonction (2 autres occurrences `ts_ms` L1168/L1217 intactes)

## Re-scellement
- md5 genesis : `fe2a7bcc…` → **`95d93d508c030c5718550096e966a929`**
- Réfs md5 mises à jour : `GO_VORTEX_V2.sh` (prefix 95d93d50), `preflight_ace777.sh`,
  `verif_pre_run_3x.sh`, `verif_setup_champion.sh`

## 🔙 RETOUR ARRIÈRE (réversible)
- **Revenir à « maintenant » (avant ce fix)** : `cp genesis_manifest.txt.BAK_avant_fix_heartbeat_20260815-152847 genesis_manifest.txt`
  puis remettre les réfs md5 sur `fe2a7bcc`.
- **Revenir à la version antérieure (avant fix CSV, 8d9ee8d6)** :
  `cp genesis_manifest.txt.BAK_avant_fix_csv_20260815-103358 genesis_manifest.txt` + réfs `8d9ee8d6`.

## ✅ Smoke test (15/08)
Run 3 min (`GO_VORTEX_V2.sh 00:03:00`) : boot OK (md5 95d93d50 passé au preflight), cycles
normaux, zéro crash, fin propre rc=0 (« Durée cible atteinte 194s »), CSV 12 colonnes intacts,
genesis inchangé. Aucun FILLED pendant le test (marché calme/férié) → le désarmement revenge
n'a pas été observé en live, mais le test fonctionnel Ruby 3/3 le prouve en isolé. **Fix validé.**
