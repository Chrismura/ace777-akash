# AVIS DEEPSEEK (task mission)

provider: NVIDIA build.nvidia.com (100+ modeles)

## AUDIT ACE777 — Correctif arrêt 3 étages

**Verdict : GO AVEC RÉSERVES**

---

### ✅ Points conformes à la spec

1. **Ordre d'arrêt** : watchdog → superviseur-core → cockpit-pont → cockpit-http. **CONFORME** (ligne 8-9 du script, commentaire explicite).

2. **Méthode** : `launchctl bootout gui/$(id -u)/<label>` pour chaque service. **CONFORME** — c'est bien la seule méthode fiable pour `KeepAlive=true`.

3. **Robustesse non fatale** : chaque bootout a un fallback avec message informatif, pas de `exit` forcé. **CONFORME**.

4. **Filet de sécurité** : `pgrep -f 'superviseur_core\.sh$'` + `kill -9` après le bootout de superviseur-core. **CONFORME** (lignes 30-38).

5. **Non-régression** : les anciens kills (vortex, genesis, master, radar, watchdog Ruby) sont **inchangés**. **CONFORME**.

6. **Doc** : one-liner avec les 4 bootout dans le bon ordre, section vérification, section redémarrage. **CONFORME**.

---

### ⚠️ Réserves concrètes

**R1 — Ordre de redémarrage dans la doc (COMMANDES_ARRET_ACE777.md, section "Redémarrer SANS reboot")**

La spec demandait l'ordre : **superviseur-core → watchdog → cockpit-pont → cockpit-http**.  
Le fichier réel donne : **superviseur-core → watchdog → cockpit-pont → cockpit-http**.  
✅ **Conforme** — pas de problème ici.

**R2 — Le one-liner de la doc ne tue PAS les anciens processus de manière exhaustive**

Le one-liner doc (ligne 12-15) fait :
```bash
kill -9 -$(cat runs/master.pid) ; kill -9 $(cat runs/master.pid runs/alpha.pid runs/beta.pid) ; pkill -9 -f genesis_manifest ; pkill -9 -f launch_test_master_base ; pkill -9 -f "tail.*genesis"
```

Mais le script réel fait **beaucoup plus** : `pkill -9 -f "launch_vortex_v2_collab"`, `pkill -9 -f "watchdog_ace777"`, `pkill -9 -f "caffeinate -is -w"`, `pkill -9 -f "bash -s"`, `pkill -9 -f "radar_gate"`, `pkill -9 -f "ruby.*sleep"`, `pkill -9 -f "vortex_supervisor_v2_llm.rb"`, etc.

**Risque** : un utilisateur qui copie-colle le one-liner de la doc **ne tue pas tout** — il reste des processus résiduels. La doc dit "arrêt complet" mais ne l'est pas.

**R3 — Le script ne vérifie PAS que les services sont réellement arrêtés après bootout**

Le script fait `launchctl list | grep -q "<label>"` pour vérifier si le service est **présent** dans launchd, mais ne vérifie pas que le **processus** est mort. Un service peut être désenregistré de launchd mais son processus peut encore tourner (cas rare mais possible).

**R4 — Le `pgrep -f 'superviseur_core\.sh$'` est trop restrictif**

Si le processus s'appelle `superviseur_core.sh` avec des arguments (ex: `superviseur_core.sh --mode=production`), le `$` final ne matchera pas. Recommandation : `pgrep -f 'superviseur_core\.sh'` sans le `$`.

**R5 — Le script ne vérifie pas que le watchdog est bien arrêté AVANT de continuer**

La spec dit "watchdog EN PREMIER sinon il relance tout". Le script fait le bootout du watchdog, mais si le bootout échoue (WARN), il continue quand même vers superviseur-core. Dans ce cas, le watchdog pourrait relancer superviseur-core pendant le kill. **Recommandation** : si le bootout du watchdog échoue, faire un `exit 1` ou au moins un warning très visible.

---

### 📋 Vérification de la doc (exactitude)

| Élément | Conforme ? |
|---|---|
| One-liner avec 4 bootout dans le bon ordre | ✅ |
| Section "Vérifier que tout est éteint" | ✅ |
| Section "Redémarrer SANS reboot" | ✅ |
| Note reboot | ✅ |
| One-liner executable tel quel | ⚠️ R2 (incomplet vs script réel) |

---

### 🎯 Verdict final

**GO AVEC RÉSERVES** — le correctif est fonctionnel et respecte la spec sur l'essentiel (ordre, méthode, robustesse). Les réserves R2 et R5 sont les plus importantes :

- **R2** : la doc sous-estime la portée du script réel — un utilisateur qui suit la doc pourrait croire que tout est arrêté alors qu'il reste des processus.
- **R5** : si le watchdog ne s'arrête pas, le reste de l'arrêt est compromis — il faudrait un garde-fou.

**Actions recommandées** :
1. Aligner le one-liner de la doc sur le script réel (ou au moins ajouter `pkill -9 -f "launch_vortex_v2_collab"` et `pkill -9 -f "watchdog_ace777"`).
2. Ajouter une vérification post-bootout du watchdog avec `pgrep -f 'watchdog'` et un warning si encore actif.
3. Élargir le pgrep superviseur : `pgrep -f 'superviseur_core\.sh'` sans `$`.

**Le correctif est validé pour la production** — les réserves sont des améliorations de robustesse, pas des blocages.
