# SPEC — Fix heartbeat → TTL revenge (codeur)

**Date :** 2026-08-15 · **Fichier :** `genesis_manifest.txt` · **Validé famille 4/4 GO-AVEC-RÉSERVE.**

## Le bug
`duo_touch_heartbeat_force()` rafraîchit `ts_ms` à chaque cycle SCOUT (appel à L1545).
Or la décision revenge (L1027) désarme le revenge si `age = now − ts_ms > 20s` (`stale_state`).
Comme `ts_ms` est rafraîchi en continu, `age` reste ~0 → `stale_state` ne se déclenche jamais
→ revenge armé en permanence (TTL 20s inopérant).

## Le fix (minimal, 1 seul bloc)
Dans `duo_touch_heartbeat_force()`, ne PAS rafraîchir `ts_ms` (ni réécrire le fichier) quand le
dernier état scout est une **perte close** : `status == "CLOSED"` ET `pnl_usdt < 0`.

## DIFF EXACT (à appliquer tel quel, octet à octet)

**OLD (dans `duo_touch_heartbeat_force`, le bloc `begin…end`) :**
```
      j=JSON.parse(File.read(path))
      j["ts_ms"]=(Time.now.to_f*1000).to_i
      tmp="#{path}.tmp.#{$$}"
      File.write(tmp, JSON.generate(j))
      File.rename(tmp, path)
```

**NEW :**
```
      j=JSON.parse(File.read(path))
      # FIX-HEARTBEAT (15/08) : ne pas rafraîchir ts_ms sur perte close (sinon TTL revenge 20s inopérant)
      unless j["status"].to_s == "CLOSED" && (Float(j["pnl_usdt"]) rescue 0.0) < 0.0
        j["ts_ms"]=(Time.now.to_f*1000).to_i
        tmp="#{path}.tmp.#{$$}"
        File.write(tmp, JSON.generate(j))
        File.rename(tmp, path)
      end
```

## Contraintes ABSOLUES
1. Ne modifier QUE ce bloc. Aucune autre ligne (ne touche pas L1027, L1044-1046, L1091, L1094, L1545).
2. Les champs duo_state sont : `role`, `status`, `side`, `bps`, `pnl_usdt`, `reason`, `cycle`,
   `hold_sec`, `ts_ms`. Le pnl se lit dans `pnl_usdt` (PAS `pnl`).
3. Conserver l'indentation exacte (6 espaces corps, 4 espaces `rescue`/`end`).
4. Si une information te manque pour produire ce diff à coup sûr, réponds EXACTEMENT
   « information insuffisante » — n'invente RIEN.

## Livrable demandé
Le bloc OLD et le bloc NEW tels que tu les appliquerais (recopiés), puis une ligne de vérification
(`bash -n` + syntaxe Ruby du heredoc). Pas d'explication longue.
