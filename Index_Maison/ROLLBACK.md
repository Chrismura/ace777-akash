# 🔄 ROLLBACK.md — Plan de retour arrière ACE777 (10/08/2026)

> Exigence famille (M5) : plan de rollback documenté AVANT toute correction.
> À lire AVANT le setup des 3 étages. Si un service ne repart pas, on ne panique pas :
> c'est exactement le but du test. On exécute ce plan.

---

## 🎯 SEUIL DE ROLLBACK (déclencheur)

**3 échecs `/health` consécutifs** (curl http://127.0.0.1:11435/health sans `"status":"ok"`)
→ rollback immédiat de l'étape en cours + arrêt + rapport à Christophe.

```bash
curl -s http://127.0.0.1:11435/health
# attendu : {"status": "ok", "providers": N}
```

---

## 💾 SOURCES DE RESTAURATION (vérifiées le 10/08 08:30)

| Source | Chemin | Contenu | Vérifié |
|---|---|---|---|
| **Backup Phase 0** | `~/Backups/ace777/phase0_20260809_185734/` | Maison complète (262 Mo, 7 404 fichiers) : scripts, plists, configs | ✅ |
| **Backup hub local** | `~/Backups/ace777/avant_3etages_20260810/prise-ia/` | Hub complet (54 fichiers, 788 Ko) : hub_prise_ia.py, .env (clés), providers, routing, usage | ✅ checksums identiques |
| **Backup hub GitHub** | `github.com/Chrismura/ace777-hub-backup` (PRIVÉ) | Identique au local (54/54 fichiers, clés incluses) | ✅ HTTP 200 |
| **Git maison** | `~/ace777-test-day1` (origin ace777-akash) | Checkpoint `e5fe1b3` v0-avant-statejson + auto-sync 3h | ✅ |
| **Plists désactivés** | `~/Library/LaunchAgents/DESACTIVES_2026-08-10/` | mirofish-front, mirofish | ✅ |
| **WORM journal** | `~/ace777-test-day1/Index_Maison/WORM_JOURNAL.log` | Trace append-only de toutes les mutations | ✅ |

---

## 🛠️ PROCÉDURE DE ROLLBACK (par scénario)

### A. Le hub ne répond plus (pire cas)
```bash
# 1. Restaurer le hub depuis le backup local (ou GitHub privé)
cp ~/Backups/ace777/avant_3etages_20260810/prise-ia/hub_prise_ia.py ~/prise-ia/hub_prise_ia.py
cp ~/Backups/ace777/avant_3etages_20260810/prise-ia/providers.json ~/prise-ia/providers.json
cp ~/Backups/ace777/avant_3etages_20260810/prise-ia/routing.json ~/prise-ia/routing.json
cp ~/Backups/ace777/avant_3etages_20260810/prise-ia/.env ~/prise-ia/.env

# 2. Redémarrer le hub
launchctl kickstart -k gui/$(id -u)/com.ace777.prise-ia
# ou : kill <PID> puis launchctl start com.ace777.prise-ia

# 3. Vérifier
curl -s http://127.0.0.1:11435/health
```

### B. Un service launchd ne repart pas (après unload/load)
```bash
# Restaurer le plist depuis le backup Phase 0
cp ~/Backups/ace777/phase0_20260809_185734/<chemin_du_plist> ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/<plist>
launchctl start <label>
# Vérifier : launchctl list | grep <label>
```

### C. Un fichier critique (444) modifié/corrompu
```bash
# Restaurer depuis le backup Phase 0
cp ~/Backups/ace777/phase0_20260809_185734/Index_Maison/scripts/<script> ~/ace777-test-day1/Index_Maison/scripts/<script>
# Le gardien refuse l'écriture directe sur 444 : passer par le mécanisme tracé (gardien + signature)
# ou, en urgence avec Christophe : chmod 644 → corriger → re-signer → chmod 444
```

### D. Rollback git (code du système)
```bash
git -C ~/ace777-test-day1 checkout e5fe1b3 -- <fichiers_concernes>
# ou revenir au checkpoint complet :
git -C ~/ace777-test-day1 reset --hard e5fe1b3   # ATTENTION : perd les commits après
```

### E. Superviseur 3 étages à désactiver (si le nouveau setup casse)
```bash
launchctl unload ~/Library/LaunchAgents/com.ace777.superviseur-unique.plist 2>/dev/null
# Les services d'origine sont toujours dans le backup Phase 0 (plists) — recharger ceux-là.
```

---

## ✅ CHECKLIST POST-ROLLBACK (dans les 15 min)

1. `curl -s http://127.0.0.1:11435/health` → `{"status":"ok",...}`
2. `launchctl list | grep ace777` → services attendus avec PID
3. `tail -20 ~/prise-ia/reports/SUPERVISEUR.log` → pas d'erreur nouvelle
4. `date` + réseau OK
5. Journaliser dans WORM_JOURNAL.log : ROLLBACK effectué, cause, heure

---

## 📌 RÈGLES

- **Backup avant chaque session** : `cp -a ~/ace777-test-day1 ~/Backups/ace777/avant_<date>/`
- **Jamais de rollback silencieux** : toujours journaliser + rapport à Christophe
- **Le rollback est une décision mécanique** (3 échecs = rollback), pas une négociation
- Sources de vérité : ce document + WORM_JOURNAL.log + MEMOIRE_COLLAB.md

*Créé : 10/08/2026 08:35 · Références : PHASE0_TERMINEE_2026-08-09.md · JUGEMENT_3ETAGES_2026-08-10/SYNTHESE.md*
