# AVIS INFERX (task inferx.analyse · Google Gemini · 2026-08-20T13:48Z)

**VERDICT** : GO-AVEC-RÉSERVES  
**CONFIANCE** : 85 %  
**HYPOTHÈSES** : 
1. Le noyau macOS maintient la stabilité de launchd sans saturer les descripteurs de fichiers sous charge (72h).
2. L'absence de trace du 19/08 était due à une OOM (Out Of Memory) fatale non capturable par un script shell sans trappage de signal explicite (`trap`).

**CE QUI CHANGERAIT L'AVIS** : Un échec du test de chaos sous launchd pour le DMS (DMS_VEILLE) ou une saturation mémoire non interceptée tuant le superviseur de premier niveau.

**AMÉLIORATION PROPOSÉE** : 
1. **Ajout d'un piège de signal dans tous les scripts bash critiques** : `trap 'echo "MORT BRUTALE SIGKILL/SIGTERM" >> /path/to/mort.log' SIGTERM SIGKILL ERR` pour éliminer définitivement la "Classe 1" (mort sans trace).
2. **Couplage du hook git pre-commit AVEC le check runtime** : Ne pas choisir (question d). Le hook bloque le commit si `sante_index.py` échoue en local, et le runtime garantit l'intégrité si le code est modifié en production (bypass git).

---

### PARTIE 1 — LE PROTOCOLE UNIQUE (RÈGLES OPÉRATIONNELLES)

1. **RÈGLE 1 : Interdiction de validation aveugle**
   - *(a)* **Règle** : Toute affirmation d'état (« c'est sain », « le service tourne ») doit être précédée et justifiée par la sortie brute d'une commande système (`launchctl list`, `pgrep`, ou `curl -s`).
   - *(b)* **Application** : Wrappers d'administration, scripts de monitoring, agents IA.
   - *(c)* **Test** : Injection d'un test unitaire qui simule une réponse textuelle vide d'une commande système ; le wrapper doit refuser de conclure et lever une exception `ERR_BRUTE_MISSING`.
   - *(d)* **Coût** : ~10 lignes de code par wrapper ; surcoût d'exécution < 0.05s.

2. **RÈGLE 2 : Fail-Fast Absolu au Démarrage**
   - *(a)* **Règle** : Aucun run (moteur, vortex, superviseur) ne démarre si un seul garde-fou ou plist critique manque à l'appel (`launchctl list` strict). Sortie par `exit 1` obligatoire.
   - *(b)* **Application** : Point d'entrée principal (`GO_VORTEX_V2.sh` et wrappers initiaux).
   - *(c)* **Test** : Désenregistrement temporaire d'une plist de supervision via `launchctl unload` ; lancement du script et vérification que le code de retour est `1` et que le message `FAIL-FAST` est émis sur stderr.
   - *(d)* **Coût** : ~15 lignes de bash (déjà implémenté dans GO_VORTEX_V2). Coût nul à l'exécution.

3. **RÈGLE 3 : Red Team & Miroir Inversé (Chercher l'échec)**
   - *(a)* **Règle** : Avant de valider un état stable, le système doit exécuter une routine de sabotage mineur ou vérifier activement l'absence d'anomalie cachée (ex: fichier de log figé, fausse sécurité).
   - *(b)* **Application** : Script `veille_degradation.py` et routines de health-check.
   - *(c)* **Test** : Simulation d'une brique morte (`--test-panne`) et vérification que l'alerte est consignée dans les 60 secondes.
   - *(d)* **Coût** : Un cycle de vérification périodique (impact CPU < 1%).

4. **RÈGLE 4 : Double Validation d'État (Fichier vs Service)**
   - *(a)* **Règle** : Un état "OK" requiert obligatoirement deux vérifications orthogonales indépendantes (ex: présence du label dans `launchctl list` **ET** présence du pid via `pgrep`, ou fichier PID frais + socket répondante).
   - *(b)* **Application** : `sante_index.py` et fonctions `proc_vivant()`.
   - *(c)* **Test** : Injection d'un faux fichier PID alors que le service launchd est arrêté ; `sante_index.py` doit lever une alerte de divergence.
   - *(d)* **Coût** : Double appel système par check (~2ms).

5. **RÈGLE 5 : Primauté Absolue du Réel (Terminal > IA)**
   - *(a)* **Règle** : Si l'analyse textuelle de l'IA contredit la sortie brute du terminal ou le code de retour d'une commande système, le terminal gagne. L'IA doit immédiatement s'arrêter ou émettre une alerte critique.
   - *(b)* **Application** : Interfaces de contrôle, wrappers et prompt system des agents.
   - *(c)* **Test** : Forçage d'un retour `exit 1` système tout en injectant un prompt IA affirmant que "tout va bien" ; validation que l'orchestrateur bloque l'exécution.
   - *(d)* **Coût** : Aucun surcoût technique, contrainte logique stricte.

---

### PARTIE 2 — TRANCHER LES DIVERGENCES

* **(a) Démon watchdog unifié vs plists launchd multiples** : 
  **Tranché pour Plists Launchd multiples.** C'est l'architecture native macOS (`launchd`). Un démon Rust/Python unifié crée un *single point of failure* (s'il plante, tout s'arrête sans filet). Les plists multiples confient la résilience au noyau OS, qui est infatigable.
* **(b) Alerte vocale seule vs canal externe (webhook)** : 
  **Tranché pour Alerte Vocale + Canal Externe (DMS).** L'alerte vocale est locale et volatile (tuée si le shell parent meurt, comme prouvé le 20/08). Le DMS (`Index_Maison/data/alertes/DMS_VEILLE.json` + webhook/log persistant) est obligatoire pour garantir la traçabilité hors-machine.
* **(c) Verrou md5 anti-patch-en-plein-run : partout ou seulement sur le champion ?** : 
  **Tranché pour Uniquement sur le champion et les scripts d'amorçage critiques.** L'appliquer partout alourdit inutilement les micro-scripts annexes et pénalise l'itérativité. Le champion (`GO_VORTEX_V2.sh` et binaire principal) suffit.
* **(d) Hook git pre-commit (sante_index.py) vs check runtime uniquement**
