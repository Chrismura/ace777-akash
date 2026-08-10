# AVIS GEMINI (task audit.protocol)

provider: Google Gemini

En tant que GEMINI (auditeur de protocole de la famille ACE777), voici mon audit rigoureux du code soumis pour l'Étape 2 (boucle interne + watchdog).

---

### VERDICT : **GO AVEC RÉSERVES**

Le code proposé par le codeur du hub est d'excellente qualité, respecte strictement la compatibilité **bash 3.2 macOS** (pas de tableaux associatifs, pas de substitution ${var,,}), assure la non-fatalité (encapsulation des checks avec fallback `NOK`), et met en place correctement le double niveau de sécurité demandé (boucle infinie + watchdog avec fallback `kickstart`/`load`).

Cependant, **une seule réserve mineure** doit être corrigée avant l'intégration par Ada : la gestion du paramètre `--force` dans la boucle interne.

---

### RÉSERVES CONCRÈTES

#### 1. Mission 1 (`superviseur_core.sh`) — Prise en compte du `--force` dans la boucle
* **Problème :** Le codeur a correctement enrobé l'orchestration dans un `while true; do ... sleep 60; done`, mais le paramètre `--force` (souvent passé en argument au script pour déclencher un cycle immédiat hors cadence) n'est traité qu'une seule fois *avant* d'entrer dans la boucle. Si le script tourne en continu, un appel à `--force` ultérieur ne sera pas interprété, et le premier cycle après un lancement avec `--force` fera un `sleep 60` normal sans forcer les réexécutions si les timestamps ne sont pas échus.
* **Correction recommandée :** Gérer le flag `--force` au début de chaque itération ou s'assurer que le premier tour s'exécute instantanément sans bloquer. (Note : si le mécanisme `check_due` se base uniquement sur les fichiers `.last`, un `--force` doit soit supprimer les `.last`, soit être évalué par cycle).

---

### VALIDATION DES POINTS DE CONTRÔLE DE LA SPÉCIFICATION

1. **C2 (Superviseur en continu) :** ✅ Validé. L'enveloppement dans `while true` avec `sleep 60` garantit que le processus ne s'arrête jamais, permettant l'utilisation de `KeepAlive:true` dans le plist sans risque de boucle de plantage rapide (grâce au sleep et au découplage par les timers `.last`).
2. **C10 (Watchdog fiable) :** ✅ Validé. Le script `watchdog_superviseur.sh` utilise `pgrep -f 'superviseur_core.sh'`, tente un `launchctl kickstart` propre, bascule sur un `launchctl load` en fallback, et consigne le tout avec horodatage dans `~/.superviseur_core/watchdog.log`. Le contrat de sortie `WATCHDOG=OK` / `WATCHDOG=RELANCEMENT` est respecté.
3. **Non-fatalité :** ✅ Validé. L'utilisation de `|| echo "NOK"` sur chaque check empêche un échec de sous-processus de casser la boucle principale.
4. **Compatibilité Bash 3.2 macOS :** ✅ Validé. Syntaxe POSIX/Bash 3.2 respectée à la lettre.
5. **Zéro casse :** ✅ Validé. Les noms de variables, les durées des checks et les formats de sortie `CORE=...` restent strictement identiques.

---
*Fin de l'audit ACE777 — Prêt pour intégration par Ada sous réserve de la prise en compte du flag `--force`.*
