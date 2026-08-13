# ULTRA — inferx.analyse

Ici ULTRA. On regarde la prod, la vraie, celle qui prend des rafales et finit par crasher. Pas de théorie, du concret.

### 1. Verdict sur le DIAGNOSTIC
**GO AVEC RÉSERVES.**
*Raison :* Le piège `trap ERR` et le fichier `/tmp/ace777_fatal_rc1.log` sont indispensables pour capturer la ligne exacte, mais se contenter d'attendre le prochain run sans durcir l'appel API bloquant, c'est laisser une fuite ouverte. Le piège diagnostique, il ne répare pas.

---

### 2. La commande la PLUS PROBABLEMENT fautive
**Mécanisme précis :** Substitution de commande bash avec `set -euo pipefail` lors d'un appel API (Curl/Ruby/JQ) pour parser le JSON du fill cycle 81. 
Le scénario type : 
```bash
PRIX_SORTIE=$(curl -s --connect-timeout 2 "https://api..." | ruby -rjson -e 'print JSON.parse(STDIN.read)["price"]')
```
Si l'API bégaye 8 secondes (timeout réseau, surcharge du testnet ou rate limit après un fill), le helper retourne vide (`""`) ou l'évaluation Ruby crashe avec un exit code != 0. Sous `set -e`, le script meurt net. Sous `set -u`, une variable non initialisée dans un parseur génère la même fatale.

---

### 3. UNE amélioration concrète de robustesse (Anti-mort subite)
**Implémenter un wrapper de retry critique avec fallback explicite pour TOUT appel réseau/parsing dans la boucle principale.**

Ne jamais laisser une commande externe (curl, ruby, jq) s'exécuter nue sous `set -e` si elle touche au réseau ou à l'état distant. Créer une fonction robuste :

```bash
safe_api_call() {
    local retries=3
    local delay=2
    for ((i=1; i<=retries; i++)); do
        # On tente, si ça rate on capture sans tuer le script immédiatement
        if "$@"; then
            return 0
        fi
        sleep "$delay"
        delay=$((delay * 2)) # Backoff exponentiel (2s, 4s, 8s)
    >
    # Si échec total après retries, on log et on retourne une valeur par défaut ou une erreur gérée
    echo "API_RETRY_EXHAUSTED: $*" >> /tmp/ace777_fatal_rc1.log
    return 1 # À attraper explicitement avec || recovery_fallback
}
```
*Application immédiate :* Remplacer les appels bruts de récupération de prix/ordres par `safe_api_call [...] || true` ou une gestion de repli (fallback) pour que le bot rate un tick au lieu de mourir en `rc=1` et abandonner BETA. En production, un bot qui loupe un cycle a tort ; un bot qui meurt a perdu.
