# AVIS ULTRA (task inferx.analyse · Google Gemini · 2026-08-20T13:48Z)

VERDICT : GO-AVEC-RÉSERVES
CONFIANCE : 85 %
HYPOTHÈSES : 
1. Le système sous charge lourde (>80% RAM) peut tuer des processus silencieusement (SIGKILL du kernel macOS) si les limites (ResourceLimits) ne sont pas explicitement définies dans les plists launchd.
2. Le couplage `launchctl list` + `pgrep` est robuste contre les faux positifs mais aveugle aux boucles infinies de threads bloqués (deadlock d'application sans mort de process).

CE QUI CHANGERAIT L'AVIS : Un test de chaos réussi sous charge mémoire maximale (bombage de swap) avec persistance et remontée d'alerte en < 60 secondes sans perte de données.

AMÉLIORATION PROPOSÉE : 
1. **Ajout obligatoire de limites de ressources dans launchd** : Forcer `SoftResourceLimits` et `HardResourceLimits` (notamment RSS/Memory) dans toutes les plists ACE777 pour éviter l'OOM Killer silencieux (mort sans trace du 19/08).
2. **Heartbeat d'application (Nano-PID file + Epoch)** : Ne pas se contenter de `pgrep`, chaque daemon critique doit écrire son `epoch` courant dans un fichier `/dev/shm` ou RAM disk toutes les 10s ; `sante_index` valide la fraîcheur de l'epoch (détection des zombies logiques).

SYNTHÈSE :
Le protocole unique et les réponses factuelles confirment la fermeture des brèches critiques (fail-fast, double validation). Le risque résiduel majeur est la mort par asphyxie mémoire (OOM) sans trace. L'intégration de limites de ressources matérielles dans launchd et de heartbeats temporels d'écriture garantira la robustesse en tempête et sous charge prolongée.

---

### PARTIE 1 — LE PROTOCOLE UNIQUE

**RÈGLE 1 : Interdiction absolue de validation aveugle**
- *(a) Règle :* Tout message d'état (« sain », « corrigé », « OK ») doit impérativement être préfixé ou suivi de la sortie brute d'une commande système de vérification (ex: `launchctl list | grep` ou `pgrep -fl`). Pas de sortie brute = non-événement rejeté.
- *(b) Application :* Wrappers de lancement, scripts de supervision (`sante_index.py`), rapports de fin de run.
- *(c) Test (non-régression) :* Script unitaire injectant un faux rapport textuel "OK" sans log brut associé -> le wrapper doit rejeter le rapport avec un code d'erreur 2.
- *(d) Coût :* Négligeable (< 5 ms par check, overhead textuel minime).

**RÈGLE 2 : Fail-fast absolu au démarrage (Hard Exit)**
- *(a) Règle :* Aucun moteur (genesis INTACT, C1) ne démarre si la totalité des plists de garde-fou et des MD5 des champions ne sont pas validés. `exit 1` immédiat et non négociable.
- *(b) Application :* Point d'entrée principal (`GO_VORTEX_V2.sh`).
- *(c) Test (non-régression) :* Suppression volontaire d'une plist de la liste `_PLISTS_SUPERVISION` avant le lancement -> le script doit avorter instantanément avant toute initialisation de marché.
- *(d) Coût :* ~100 ms au démarrage du système (vérification `launchctl` séquentielle).

**RÈGLE 3 : Miroir inversé / Red Team (Chasse à la panne)**
- *(a) Règle :* Avant toute validation de fin de maintenance ou de déploiement, exécution d'un scénario de chaos ciblé (simulation de brique morte, saturation I/O). Le système doit prouver qu'il détecte et alerte sur la panne, sinon le run est invalidé.
- *(b) Application :* Script de recette de déploiement (`veille_degradation.py --test-panne`).
- *(c) Test (non-régression) :* Vérification de la présence obligatoire du JSON d'alerte dans `Index_Maison/data/alertes/` consécutif au test de chaos.
- *(d) Coût :* 60 secondes par cycle de recette (exécuté hors production ou en mode sandbox).

**RÈGLE 4 : Double validation d'état orthogonale**
- *(a) Règle :* Un service n'est déclaré "actif" que si (1) `launchctl list` confirme le label ET (2) `pgrep -fl` confirme le PID actif ET (3) un indicateur métier frais (fichier de log ou métrique < seuil) est détecté.
- *(b) Application :* Superviseur core et `sante_index.py`.
- *(c) Test (non-régression) :* Simulation d'un process présent dans launchctl mais tué en arrière-plan (`kill -9`) -> détection obligatoire en < 1 cycle de supervision (60s).
- *(d) Coût :* Très faible (appels système natifs optimisés).

**RÈGLE 5 : Primauté absolue du Terminal (Le Réel gagne)**
- *(a) Règle :* En cas de divergence entre l'état théorique stocké en mémoire par l'IA/script et la réalité renvoyée par le terminal (`/dev/tty`, `launchctl`, `df`, `free`), le terminal gagne. L'IA doit immédiatement crier à l'anomalie et basculer en mode repli.
- *(b) Application :* Tous les wrappers d'exécution et interfaces de pilotage.
- *(c) Test (non-régression) :* Injection d'une variable d'état mensongère dans le contexte IA alors que le service est down -> le wrapper force la synchro sur le terminal et lève une alerte critique.
- *(d) Coût :* Aucun surcoût algorithmique (simple condition booléenne sur retour de commande).

---

### PARTIE 2 — TRANCHER LES DIVERGENCES

*(a) Un seul démon watchdog unifié (Rust/Python) vs plists launchd multiples ?*
**TRANCHÉ : Plists launchd multiples natives.**
*Justification :* Rust/Python introduit un SPOF (Single Point Of Failure) applicatif. Si le démon unifié crashe par OOM, tout tombe sans filet. `launchd` est le watchdog natif du noyau macOS, géré par le système d'exploitation lui-même. La robustesse à l'échelle repose sur l'infrastructure sous-jacente, pas sur une sur-couche logicielle supplémentaire.

*(b) L'alerte vocale seule suffit-elle, ou faut-il un canal externe (webhook) ?*
**TRANCHÉ : Canal externe asynchrone (Webhook/Fichier JSON) obligatoire en plus du vocal.**
*Justification :* L'alerte vocale (`alerte_vocale.
