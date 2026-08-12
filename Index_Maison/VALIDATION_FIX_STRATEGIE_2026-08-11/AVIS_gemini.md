# AVIS GEMINI (via Google Gemini, task audit.protocol) — 2026-08-11T17:04:49

Membre senior ACE777. Analyse du dossier de correction. Lecture critique, sans complaisance. Nous gérons de l'argent ; un bug silencieux dans le cockpit est une faute grave.

Voici l'analyse factuelle des 4 points soulevés, suivie du verdict.

---

### 1. Le diagnostic est-il juste et complet ?
**Partiellement juste, mais superficiel sur la cause systémique.**
*   **Le fait :** Oui, `const` et `let` ont une portée de bloc (block scope). Déclarer `const BRIDGE` dans un bloc `<script>` A la rend invisible pour le bloc `<script>` B.
*   **Le piège :** Le `try/catch` silencieux (`catch (e) { /* rien */ }`) est une pratique criminelle dans un système financier. Il a transformé une erreur critique fatale (`ReferenceError`) en un état indéterminé (« chargement infini »). 
*   **Ce qui manque :** Le diagnostic ne questionne pas l'architecture. Pourquoi le code JavaScript est-il saucissonné en blocs `<script>` indépendants qui partagent l'espace global via des variables locales mal scopées ? C'est une architecture fragile, du bricolage de prototype, pas du code de production ACE777.

### 2. Le fix couvre-t-il le problème sans risque de régression ?
**Il colmate l'urgence, mais introduit du code défensif redondant.**
*   **La rustine (`const BRIDGE` + `console.error`) :** Nécessaire et immédiate. Elle résout le cas précis.
*   **Le retry conditionnel (3 essais, 2.5s) et le `no-store` :** C'est du **bricolage préventif inutile** qui masque les symptômes réseau au lieu de traiter la cause racine (qui était purement applicative/JS, puisque le bridge répondait en 2-12ms). Ajouter des retries sur une erreur de *scope* JS (ReferenceError) montre qu'on a eu peur sans comprendre exactement où était le feu. Risque de régression faible, mais complexité inutile ajoutée.

### 3. Y a-t-il d'autres variables/constantes du même type (scopes de blocs `<script>` séparés) ?
**Oui, de manière quasi certaine.**
Si le cockpit utilise plusieurs blocs `<script>` dans le même HTML sans module bundler (Webpack, Vite) ni mode strict global partagé, les risques sont systémiques. Il faut auditer immédiatement :
*   Les clés d'API, tokens de session ou identifiants de wallet (`TOKEN`, `SESSION_ID`, `WALLET_ID`).
*   Les URLs des autres services (endpoints de paiement, ledger, websocket).
*   Les fonctions utilitaires partagées (`formatMontant`, `parseDevise`) qui pourraient être redéfinies par accident (shadowing) d'un bloc à l'autre.
*   *Action requise :* Un `grep` global sur tous les scripts pour recenser toutes les constantes de configuration déclarées localement.

### 4. La leçon générale : comment éviter qu'un bug de scope soit invisible ?
La tolérance aux erreurs silencieuses doit être zéro.
1.  **Interdiction formelle des blocs `catch` vides.** Toute exception *doit* remonter ou être loguée a minima avec `console.error` et un pavé d'alerte UI (« Erreur critique du module »).
2.  **Unicité du point de configuration :** Plus de `const BRIDGE` disséminée dans les blocs HTML. Un fichier unique `config.js` chargé en premier, ou un objet global `window.ACE777_CONFIG` immuable (`Object.freeze`).
3.  **Linter / Type-checking :** Intégrer ESLint avec une règle stricte contre les variables non déclarées (`no-undef`) et les blocs catch vides (`no-empty`).
4.  **Tests de fumée (Smoke tests) automatisés :** Un script headless (comme celui qui a trouvé le bug) doit vérifier que les onglets affichent de vraies données et non des messages de chargement persistants après `N` secondes.

---

VERDICT FINAL : FIX VALIDE AVEC RESERVES
CONFIANCE : moyenne
