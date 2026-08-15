# ULTRA — inferx.analyse

Ici ULTRA (famille ACE777). Je regarde la structure sous la tempête, la charge et le long terme. Pas de place pour l'illusion.

Voici mon verdict et mes tranchages :

1. **VERDICT :** GO. La mort silencieuse sous `set -e` dans des sous-shells non protégés est une aberration de robustesse inacceptable en prod.

2. **CIBLE :** **Option A (Ajout minimal dans genesis + Re-scellement)**. 
   *Justification ACE777 :* Le lanceur n'est qu'un bootstrap. Mettre de la logique de résilience dans le lanceur pour corriger le moteur, c'est de la dette technique. Le précédent est là (af307996). On touche genesis, on protège les points de fragilité, on re-scelle. Propre, auditable, immutable.

3. **MÉCANISME RÉEL :** **Confirmé**. Les `public_get` ont leurs filets (`|| true`), mais les appels de helpers Ruby imbriqués (`json_get`, `as_num`, etc.) à l'intérieur de substitutions de variables (`$(...)`) lèvent un `rc!=0` en cas de JSON corrompu ou vide. Sous `set -e`, cela assassine le sous-shell instantanément et silencieusement (le trap global rate le coche dans le pipe).

4. **LISTE EXACTE DES ZONES À PROTÉGER (Bash 3.2 macOS safe) :**
   Il faut enrober les substitutions critiques d'une valeur par défaut ou d'un fallback `|| echo "0"` / `|| echo ""` selon le type (numérique ou string), ou créer une fonction helper `safe_eval()` locale.
   *   **Zones critiques ciblées (lignes 1600, 1614, 1734-1735, 2057, 2061, 2071, 2109, 2142, 2431 et autour) :**
       Remplacer les appels bruts du type :
       `p1="$(as_num "$(json_get "$p1_resp" "price")")"`
       Par une structure sécurisée :
       `p1="$(as_num "$(json_get "$p1_resp" "price" || echo "0")" || echo "0")"`
       *Idem pour les helpers de trend et de calcul (`trend_bps_from_klines`, `num_*`) :* toujours attacher un fallback `|| echo "0"` à l'intérieur des `$(...)` pour empêcher le `set -e` de déclencher la guillotine.

5. **INDICATEUR DE PREUVE AU RETEST :**
   L'apparition explicite d'un log de fallback ou de récupération dans la sortie standard (ex: `[WARN] ruby helper recovery triggered on line XXX`) au lieu d'un arrêt net à `rc=1` sans trace. Si le process dépasse 15 minutes sans mourir après le fill #42, la correction est validée.
