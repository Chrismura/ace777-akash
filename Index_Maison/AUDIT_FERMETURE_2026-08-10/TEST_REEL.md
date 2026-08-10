# TEST RÉEL — FERMETURE 3 ÉTAGES — 10/08/2026 (soir)

Correctif du codeur du hub (SPEC_fermeture_3etages.md + polish R2/R4/R5),
intégré par Ada, validé famille 4/4 (GO), testé en conditions réelles.

## Déroulé (4 étapes, tout vert)

### 1. FERMETURE — `./stop_ace777.sh`
```
=== [3ETAGES] Arret des services launchd (KeepAlive=true) ===
[3ETAGES] com.ace777.watchdog arrete
[3ETAGES] com.ace777.superviseur-core arrete
[3ETAGES] Processus superviseur_core.sh residuel detecte — kill -9   <- filet R4 a travaille
[3ETAGES] com.ace777.cockpit-pont arrete
[3ETAGES] com.ace777.cockpit-http arrete
Arrêté.
```
→ Les 4 services ont disparu de launchd. Aucun processus résiduel.

### 2. PREUVE ANTI-RELANCE (attente 130 s > intervalle watchdog 120 s)
→ **RIEN n'est revenu.** La fermeture est durable : le watchdog ne peut plus
relancer le gardien. (C'était le trou : avant, il relançait tout ~2 min après.)

### 3. REDÉMARRAGE — `launchctl bootstrap` (4 plists, ordre doc)
```
89037 com.ace777.cockpit-http
-     com.ace777.watchdog
89028 com.ace777.superviseur-core
89034 com.ace777.cockpit-pont
```
→ Les 4 services sont revenus.

### 4. TOUT RÉPOND
- Cockpit (17800) : ✅ HTML servi
- Pont (17777) : ✅ `{"muted": false, "ok": true, "bridge": "cortana+mission"}`
- Gardien : ✅ `state = running`, pid 89028, `CORE=OK`, jamais sorti
- Hub (cervelle) : ✅ `{"status": "ok", "providers": 9}` (intact pendant tout le test)

## Conclusion
La boucle complète fonctionne : **arrêt propre → rien ne revient → redémarrage
propre → tout répond.** La fermeture est à jour avec la fusion 3 étages.
