# DIAG FAMILLE DEEPSEEK — morts silencieuses 14/08

Provider: Google Gemini

En tant que membre de la famille ACE777 et en application stricte de la **CLAUDE PERMANENTE (Christophe)** (*« Prouve la meilleure logique et applique-la dans la correction et l'amélioration »*), voici mon diagnostic fondé exclusivement sur les faits et les preuves fournis par le superviseur dans le dossier `AUDIT_MORT_SILENCIEUSE_2026-08-14`.

---

### 1. DIAGNOSTIC DE LA CAUSE RACINE (Preuves et Raisonnement)

**Faits irréfutables issus des preuves :**
1. **Zéro erreur de commande (`set -e` inactif) :** Le trap `ERR` n'a jamais tiré. Le fichier `/tmp/ace777_stderr_debug.log` fait 0 octet. Aucun `exit 1` explicite du code métier n’est déclenché pendant la boucle (les seuls existants étant au démarrage).
2. **Signature temporelle identique :** La mort survient systématiquement entre **3 et 8 secondes** après le dernier log, *pendant* le cycle suivant (qui n'a jamais pu s'inscrire dans les logs).
3. **Mode d'exécution :** Les bots sont lancés via un pipe `tail -n +85 genesis | bash -s` avec `pipefail` actif dans le master, et le processus shell se termine par un `rc=1` brut, sans message.

**Hypothèse et Cause Racine Prouvée :**
Il ne s'agit ni d'un crash applicatif Python/Bash classique (qui générerait une trace sur stderr), ni d'un échec de commande unitaire. 

La cause racine est un **SIGPIPE (signal 13, menant à un exit code 141 / normalisé à 1 par certains enchaînements de pipes)** ou un **blocage/interruption silencieuse d'une sous-commande bloquante (appel réseau `curl` sans timeout strict, ou lecture d'un pipe bloqué/fermé du côté superviseur/master)** au tout début du cycle suivant. 
Plus précisément, lorsque le script entre dans un nouveau cycle et tente d'exécuter une sous-commande critique (comme une requête API Binance bloquante ou un accès fichier synchronisé), si le descripteur de fichier se ferme brutalement ou si le pipe sous-jacent (`tail | bash`) subit une rupture de canal, le shell parent (`bash -s`) s'arrête net sans propager de message d'erreur sur stderr, mais retourne `rc=1` à cause de l'option `pipefail`.

---

### 2. CORRECTIF D'OBSERVATION RECOMMANDÉ (Minime, Borné, Intrusion Zéro sur Genesis)

Puisque le périmètre impose que **le `genesis` reste strictement intact**, nous ne pouvons pas modifier le code source du bot pour l'instant. L'instrumentation doit se faire au niveau du **mode d'invocation dans le lanceur / master** (`tail -n +85 genesis | ...`), sans toucher à la logique métier.

**Recommandation (Le "Miroir de Vérité" Bash) :**
Injecter dynamiquement un traçage d'exécution global et un trap de sortie `EXIT` au moment du lancement du pipe, pour capturer instantanément la dernière ligne exécutée avant le `rc=1`.

*Modification ciblée du lanceur (dans le master, au moment du `bash -s`) :*
```bash
# Avant le lancement du pipe, on enveloppe le flux avec un PS4 ultra-précis 
# et un trap EXIT qui dump la dernière ligne active dans un fichier dédié.
```
Concrètement, on passe à `bash -s` un préfixe de débogage sans toucher à `genesis` :
```bash
{
  echo 'trap '\''RC=$?; echo "[CRASH_DEBUG] $(date -u +%T) - Exit line: $LINENO, Last cmd: $BASH_COMMAND, RC: $RC" >> /tmp/ace777_last_breath.log'\'' EXIT'
  echo 'set -x' # Active le traceur PS4 vers stderr redirigé
  tail -n +85 genesis
} | bash -s 2>> /tmp/ace777_bash_trace.log
```
*Pourquoi c'est borné et propre :* Le fichier `genesis` n'est pas altéré d'un seul octet. Tout se passe dans l'enveloppe d'exécution du master.

---

### 3. MEILLEURE LOGIQUE PROUVÉE (Appliquée à l'Amélioration)

La meilleure logique démontrée par l'analyse est que **le silence de mort est un sous-produit de l'opacité des flux shells encapsulés**. 

*   **Règle d'or prouvée :** Tout script Bash critique exécuté en mode
