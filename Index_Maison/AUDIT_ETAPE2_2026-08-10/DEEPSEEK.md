# AVIS DEEPSEEK (task mission)

provider: NVIDIA build.nvidia.com (100+ modeles)

## AUDIT ÉTAPE 2 — Verdict : **GO AVEC RÉSERVES**

---

### MISSION 1 — Boucle interne (C2)

**Points conformes :**
- ✅ Boucle `while true` correctement implémentée
- ✅ `sleep 60` respecte la fenêtre 60-120s
- ✅ Contrat CORE=OK|WARN|NOK écrit à chaque cycle
- ✅ Compatible bash 3.2 (pas de tableaux associatifs, pas de `${var,,}`)
- ✅ Checks protégés par `|| echo "NOK"` (non-fatalité)

**Réserves :**

1. **Ligne ~15 (bloc APRÈS)** : `while true` sans condition de sortie — si le script est lancé en mode debug ou test, il sera impossible de l'arrêter proprement. Ajouter une gestion de signal :
   ```bash
   trap 'echo "CORE=STOP"; exit 0' INT TERM
   ```

2. **Ligne ~30 (bloc APRÈS)** : `sleep 60` non protégé — si le système est en veille ou si un signal arrive pendant le sleep, la boucle peut se comporter de manière inattendue. Utiliser `sleep 60 || true` pour garantir la continuité.

3. **Manque de gestion du mode `--force`** : La spec demande explicitement "si FORCE=1, faire un cycle complet immédiat puis continuer la boucle". Le code actuel ne gère pas cette variable — vérifier que `FORCE` est bien initialisée avant la boucle et que le premier cycle est forcé si nécessaire.

---

### MISSION 2 — Watchdog (C10)

**Points conformes :**
- ✅ `pgrep -f 'superviseur_core.sh'` correct
- ✅ Kickstart avec `-k` (kill + restart) bien implémenté
- ✅ Fallback `launchctl load` présent
- ✅ Journalisation horodatée dans `~/.superviseur_core/watchdog.log`
- ✅ Contrat WATCHDOG=OK|RELANCEMENT respecté
- ✅ Script léger (~30 lignes), stdlib only

**Réserves critiques :**

1. **Ligne 20** : `pgrep -f 'superviseur_core.sh'` — risque de faux positif si un autre processus contient cette chaîne dans sa ligne de commande (ex: un éditeur ouvert sur ce fichier). Plus robuste :
   ```bash
   pgrep -f '^/bin/bash .*superviseur_core\.sh' || pgrep -f 'superviseur_core\.sh$'
   ```

2. **Ligne 24-25** : `launchctl kickstart -k` — si le service n'est pas chargé, cette commande échoue silencieusement (stderr redirigé). Le fallback `load` est bien prévu, mais il faut vérifier que le plist existe avant :
   ```bash
   if [ ! -f "$HOME/Library/LaunchAgents/$PLIST_LABEL.plist" ]; then
       watchdog_log "ERREUR: plist manquant"
       echo "WATCHDOG=RELANCEMENT"
       exit 1
   fi
   ```

3. **Ligne 30** : `launchctl load` — sur macOS moderne, `load` est déprécié au profit de `bootstrap`. Pour bash 3.2, `load` reste acceptable mais devrait être suivi d'un `launchctl start` pour garantir le démarrage immédiat.

4. **Manque de vérification post-relance** : Après kickstart ou load, le watchdog devrait vérifier que le processus est effectivement relancé (attendre 2-3 secondes puis re-vérifier avec pgrep). Actuellement, il assume que la commande a réussi.

---

### Non-fatalité globale

- ✅ Les checks individuels sont protégés
- ⚠️ La boucle `while true` n'a pas de protection contre les erreurs fatales du script lui-même (ex: si `check_due` plante, la boucle continue mais avec des variables potentiellement vides)

---

### Recommandations finales

1. **Ajouter le trap de signal** dans superviseur_core.sh
2. **Protéger le sleep** avec `|| true`
3. **Vérifier la gestion de FORCE** (initialisation avant boucle)
4. **Améliorer le pgrep** du watchdog pour éviter les faux positifs
5. **Ajouter une vérification post-relance** dans le watchdog (sleep 3 + re-pgrep)

**Verdict : GO AVEC RÉSERVES** — le code fonctionne mais nécessite ces 5 corrections mineures pour une robustesse optimale en production.
