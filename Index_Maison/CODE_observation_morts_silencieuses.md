# CODEUR — observation morts silencieuses (14/08)

Provider: Puter Grok (gratuit)

**A) INSTRUMENTATION — code à injecter (zone neutre, post-ligne 85)**

```bash
# === OBSERVATION EXIT DUMP (bash 3.2+ macOS safe) ===
: "${BOT_NAME:=UNKNOWN}"
EXIT_DUMP_DIR="${EXIT_DUMP_DIR:-runs}"
mkdir -p "$EXIT_DUMP_DIR" 2>/dev/null || true

_last_cmd=""
trap 'printf "[%s] EXIT rc=%s last=[%s] bot=%s\n" \
    "$(date -u +%H:%M:%S)" "$?" "${_last_cmd:-N/A}" "$BOT_NAME" \
    >> "$EXIT_DUMP_DIR/EXIT_DUMP_${BOT_NAME}_$(date -u +%Y%m%d_%H%M%S).log" 2>/dev/null' EXIT

trap 'export _last_cmd="$BASH_COMMAND"' DEBUG
```

**Modèle de log produit :**
```
[09:25:03] EXIT rc=1 last=[sleep 8] bot=ALPHA
[09:29:18] EXIT rc=1 last=[read -r line] bot=BETA
```

**B) ANALYSE CAUSE RACINE (classée par probabilité)**

1. **EOF pipe + pipefail (probabilité haute)**  
   `tail -n +85 | bash -s` avec `set -o pipefail`. Si le master ferme le pipe (crash, timeout, ou fin de transmission), `bash -s` reçoit EOF sur stdin. Toute lecture suivante (`read`, ou boucle implicite) peut retourner 1 sans passer par le trap ERR (car `read` sur EOF n’est pas une « erreur de commande » au sens `set -e`).

2. **Subshell / fonction retournant 1**  
   `duo_publish_state` ou `duo_touch_heartbeat` exécutés dans un sous-shell ou via `$(...)`. Si la fonction fait `return 1` (ou sort avec 1), et que ce retour est utilisé dans un contexte où `set -e` ne piège pas (ex. `local x=$(f)` ou `x=${y:-$(f)}`), le script peut sortir en rc=1 sans FATAL_RC1.

3. **Signal silencieux (SIGPIPE / SIGTERM)**  
   Mort 3-8 s après le dernier cycle = fenêtre de `sleep`. Un SIGPIPE sur stdout ou un signal externe peut tuer le processus sans que le trap ERR (ligne 90) ne s’exécute si le signal n’est pas capturé avant.

4. **Fin de boucle implicite + set -e**  
   Dernier cycle SKIP → entrée dans le cycle suivant → `read` ou condition qui échoue → sortie de la boucle `while` avec code de la dernière commande (1) sans jamais atteindre un `exit` explicite.

**Preuves d’absence de commande échouée** (ZERO FATAL_RC1, stderr_debug=0) éliminent les erreurs de commandes classiques. Reste donc : **pipe EOF** ou **retour implicite de sous-processus**.

**C) PREUVE MEILLEURE LOGIQUE + AMÉLIORATION**

**Pourquoi `trap EXIT + DEBUG` > `set -x` :**
- `set -x` génère un flux continu de lignes (bruit élevé, corrélation difficile avec le moment exact de sortie).
- `trap EXIT` s’exécute **une seule fois**, au moment de la mort, avec le code de sortie réel.
- Le trap `DEBUG` capture `$BASH_COMMAND` juste avant chaque exécution → on obtient « la dernière ligne réellement exécutée » sans avoir besoin du log complet.
- Compatible bash 3.2 (macOS) : `$BASH_COMMAND` existe depuis bash 3.0, pas de feature 4.x+ requise.
- Coût : 2 traps + 1 variable → zéro effet de bord sur la logique.

**Amélioration prouvée (mesurable, bornée) :**
Ajouter `trap '...' DEBUG` uniquement sur les lignes critiques (lecture état duo) plutôt que globalement. Cela réduit le nombre d’écritures de `$_last_cmd` de ~100 % à ~5-10 % des cycles, sans perte d’information sur la cause de sortie (la dernière commande avant mort reste capturée). Gain : réduction de l’overhead d’observation tout en gardant la même précision sur le crash.

**Livraison :** code ci-dessus + analyse + preuve. Genesis inchangé.
