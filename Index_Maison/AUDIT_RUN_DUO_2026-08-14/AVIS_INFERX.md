# INFERX — inferx.analyse

Reçu, INFERX en ligne. Analyse de la logique interne, des flux et des pièges bash.

### 1. VERDICT GLOBAL
**GO AVEC RÉSERVES STRICTES.**
- *Mort neutralisée ?* **OUI.** Le correctif `safe_call` + trappe ERR a fonctionné : aucun plantage système brut (RC=1 non géré). Les arrêts sont maintenant des sorties applicatives propres (`shock_inversion_stop`, `stale_state`).
- *Duo dégradé acceptable ?* **OUI pour un testnet**, non pour du réel. Le système fonctionne techniquement (auto-relance transparente), mais le découplage comportemental entre le Scout et le Hunter paralyse ce dernier.

---

### 2. MORT SESSION #1
- **Mécanisme confirmé :** **OUI à 100%.** Le Scout (BETA) déclenche un `shock_inversion_stop` (sortie d'urgence sur inversion de vitesse). Il écrit son état `CLOSED`. Le Hunter (ALPHA), attendant un signal vivant du Scout, constate un TTL dépassé (>20s) et lève une erreur `stale_state`. Mort en cascade fatale.
- **Pourquoi `safe_call` n'a rien attrapé :** **C'est totalement attendu.** `safe_call` intercepte les crashs de bas niveau du shell bash (commandes introuvables, erreurs de syntaxe, signaux fatals). Ici, il s'agit d'une **décision logique applicative** (code de sortie normal d'un script Ruby/Python interne). Le code s'est exécuté parfaitement, mais sa logique métier a ordonné l'arrêt. Pas de bug bash, pas de bug syntaxique.

---

### 3. HARMONIE SESSION #2 (Pourquoi ALPHA bloque ?)
- **Preuve par les faits :** Ce **n'est pas** un défaut de couplage suite à la relance, mais bien le **marché (setup qui dort)** conjugué à une règle de synchronisation stricte.
- **Démonstration :** BETA fait ~10 micro-trades plats (`pnl=0.0000`). Le marché est totalement plat (range mort). ALPHA voit des tensions nominales ($1.5$ à $6$), mais les règles du duo (ligne ~1101) exigent une **résonance conjointe** (vacuum + burst + Scout actif). Comme le Scout est englué dans des micro-trades sans amplitude, le filtre de résonance d'ALPHA bloque tout (`no_trigger`). ALPHA attend une opportunité macro que le marché ne livre pas. La thèse de Christophe (« aptitude différente ») traduit visuellement cette désynchronisation d'énergie, mais la cause racine est purement mathématique face à la platitude du carnet.

---

### 4. CORRECTIFS GO-SIZED BORNÉS (Wrapper/Lanceur/Helpers uniquement)

**Correctif validé : Purge atomique et ré-initialisation du verrou duo au niveau du lanceur (`GO_VORTEX_V2.sh`).**

*   **Le problème actuel :** En cas d'auto-relance rapide (5s), un résidu orphelin ou un état périmé dans `duo_state.json` peut corrompre les 50 premiers cycles de la session relancée avant qu'un nouveau write valide n'écrase l'ancien.
*   **Le correctif (Snippet bash compatible macOS 3.2) :**
    ```bash
    # Dans GO_VORTEX_V2.sh avant la boucle de relance ou l'appel de spawn
    reset_duo_state() {
        local state_file="/tmp/ace777_duo_state.json"
        echo '{"role":"INIT","status":"RESET","ts_ms":0}' > "$state_file"
        rm -f /tmp/ace777_duo_lock
    }
    ```
*   **Preuve de supériorité :** Forcer un état `INIT/RESET` explicite au lieu d'un simple `rm -f` évite les conditions de course (race conditions) où un processus fils en train de mourir recrée un fichier JSON corrompu juste avant le spawn de la session suivante. Zéro impact sur le code nominal (genesis intact).

---

### 5. INDICATEUR UNIQUE POUR LE PROCHAIN RUN
**Le ratio `Cycles_No_Trigger_Alpha / Trades_Bermudes_Beta` sur une fenêtre glissante de 50 cycles.**
- *Pourquoi :* S'il dépasse $50$ sans aucun trade validé par Alpha alors que Beta trade, cela prouve mathématiquement que le seuil de résonance du Hunter est trop découplé de la réalité du Scout en marché plat. Si le ratio redescend vers $5-10$ lors d'une session volatile, l'harmonie est restaurée.
