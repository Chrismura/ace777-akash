# AVIS openrouter-ultra (provider OpenRouter Nemotron 3 Ultra 550B (free) - analyse forte, 126.1s)

### F1 — Réparer la justesse (score_justesse.py)

*   **Technique** : Faisable (stdlib Python, CSV). Risque faible de casser un consommateur : le script est en lecture seule, sortie JSON/CSV. Attention à la migration de l'historique (93 analyses) : prévoir un recalcul *ex post* sur la nouvelle logique pour ne pas perdre la série temporelle.
*   **Impact** : Passe d'une métrique "bruit" (corrélation forcée BTC) à une métrique "signal" (performance intrinsèque par indice). Permet d'identifier quels indices sont prédictifs *vraiment*. NEUTRE noté = fin de l'échappatoire statistique.
*   **Risque/Sécurité** : Respecte C2/C3 (lecture seule), Champion intouchable, GO humain (1 chantier = refactor script + backfill).
*   **Ordre de priorité** : **#1 (Urgent)**. C'est la boussole. Sans justesse fiable, Ada et Cortana naviguent à l'aveugle.

**VERDICT : GO**
**CONFIANCE : 95 %**
**HYPOTHÈSES** : 1) Les données historiques brutes (OHLCV funding, fear/greed) sont archivées en CSV pour recalculer. 2) Le seuil 0,3 % est calibré sur la volatilité réelle des indices (pas du BTC).
**CE QUI CHANGERAIT L'AVIS** : Absence des données sources brutes pour le backfill (perte historique) ou découverte d'un consommateur aval (ex: dashboard) qui parse le format de sortie *actuel* sans versioning.
**AMÉLIORATION PROPOSÉE** : 1) Versionner le format de sortie (`justesse_v2.json`). 2) Ajouter une colonne "régime de marché" (trend/range) pour segmenter la justesse future. 3) Automatiser le recalcul quotidien via cron/hub.

---

### F2 — Carte d'identité ACE777 + Prompts canon au boot

*   **Technique** : Trivial (fichiers `.md`/`.txt` + injection dans `app.toml` ou `system_prompt` au démarrage Rust/Python). 0 Go RAM. Risque nul de casse.
*   **Impact** : Ancre l'alignement global. Évite la dérive "persona" (Cortana qui croit trader). Donne à Qwen/Ada un contrat explicite. Base pour audit futur.
*   **Risque/Sécurité** : Neutre (documentation). Respecte toutes contraintes. GO humain = rédaction (1h).
*   **Ordre de priorité** : **#2 (Immédiat post-F1)**. Prérequis pour F5 (prompt voix) et F3 (rôle dashboard).

**VERDICT : GO**
**CONFIANCE : 100 %**
**HYPOTHÈSES** : 1) Le hub/launcher lit un champ `system_prompt_path` ou `identity_config` au boot. 2) Les 3 acteurs (Ada, Cortana, Qwen) acceptent une injection de prompt externe.
**CE QUI CHANGERAIT L'AVIS** : Si l'architecture impose un prompt *hardcodé* dans les binaires Rust/Python (rebuild nécessaire à chaque modif).
**AMÉLIORATION PROPOSÉE** : 1) Stocker dans `config/identity/ace777_core.md` + `prompts/{ada,cortana,qwen}.md`. 2) Ajouter un hash SHA256 dans les logs de démarrage pour tracer quelle version de l'identité tourne. 3) Prévoir un champ `version_strategie` pour la bascule saison (Ada).

---

### F3 — Cortana = Dashboard unifié (Fills ACE + Hulk + Indices)

*   **Technique** : Lecture CSV (runs ACE) + lecture DB/CSV (paper Hulk) + agrégation Pandas/Polars. ~50-100 Mo RAM pic. Faisable. Risque : complexité de jointure temporelle (fills vs bougies). Un seul script `cortana_analyse.py` = point de défaillance unique (SPOF) pour la vue.
*   **Impact** : **Cœur de valeur**. Cortana devient la "vue unique de vérité" (Single Pane of Glass). Permet corrélation fills/stratégie vs indices vs paper. Base pour décisions humain (GO).
*   **Risque/Sécurité** : Lecture seule (C2/C3 OK). Champion intouchable. GO humain = 1 chantier (extension script).
*   **Ordre de priorité** : **#3 (Après F1/F2)**. Dépend de F1 (justesse indices) et F2 (rôle défini).

**VERDICT : GO**
**CONFIANCE : 90 %**
**HYPOTHÈSES** : 1) Les fills ACE (CSV) et Hulk (paper) ont des timestamps UTC alignés et une clé de jointure commune (symbol, ts). 2) Le volume de données Hulk paper tient en RAM (8 Go) ou est streamable.
**CE QUI CHANGERAIT L'AVIS** : Si Hulk paper n'est pas accessible en lecture locale (ex: API distante lente, pas de dump CSV/Parquet).
**AMÉLIORATION PROPOSÉE** : 1) Sortie standardisée `cortana_snapshot_{ts}.json` (schéma figé) consommable par hub/voix. 2) Métrique "PnL attributé par régime" (lien F1). 3) Alerte silencieuse si divergence fills vs signal > seuil.

---

### F4 — Un seul aiguilleur (Hub exclusif, nettoyage brain.rs)

*   **Technique** : Refactor Rust (`brain.rs`) : suppression code mort (Gemini/Ollama direct), appel unique `hub.route(prompt)`. `app.toml` aligné. Rotation modèles déjà dans `routing.json`. Risque : régression routing (fallback offline). Tests unitaires obligatoires.
*   **Impact** : Simplifie drastiquement la chaîne de commande. Élimine l'incohérence "3 cerveaux". Garantit que la rotation/coût/latence est gérée *uniquement* par le hub.
*   **Risque/Sécurité** : Critique. Touche au chemin de décision (C2/C3 : le hub ne doit *jamais* appeler C2/C3). Le repli hors-ligne (Ollama local) doit être garanti par le hub, pas `brain.rs`. GO humain = 1 chantier Rust (compilation, test).
*   **Ordre de priorité** : **#4 (Parallèle à F3 ou après)**. Nettoyage architecture, pas urgence métier mais urgence technique (dette).

**VERDICT : GO-AVEC-RÉSERVE**
**CONFIANCE : 80 %**
**RÉSERVE** : Valider que le hub gère *exhaustivement* le fallback offline (timeout, modèle local dispo, queue) avant de supprimer la logique locale de `brain.rs`.
**HYPOTHÈSES** : 1) `prise-ia` (hub) expose une API synchrone simple (`route(req) -> res`). 2) `routing.json` couvre tous les cas d'usage actuels (analyse, voix, résumé).
**CE QUI CHANGERAIT L'AVIS** : Si le hub n'a pas de timeout configurables ou de health-check modèles locaux (risque blocage `brain.rs`).
**AMÉLIORATION PROPOSÉE** : 1) Intégration test : `cargo test -- --nocapture` simulant panne hub/réseau. 2) Métrique `hub_latency_ms` / `hub_fallback_count` loggée dans `brain.rs`. 3) Supprimer `puter-grok` (402) du code et de `routing.json`.

---

### F5 — Nettoyer prompt voix (Cortana) + greffe identité

*   **Technique** : Modification `persona.rs` / prompt système. Injection `identity.md` (F2). Suppression littérale "exécute des ordres". Zéro code logique. Risque nul.
*   **Impact** : Aligne l'interface humaine (voix) sur la réalité contractuelle (dashboard seule). Prépare C7 (autonomie future) sans casser l'existant.
*   **Risque/Sécurité** : Renforce C2/C3 (interdit explicite dans le prompt). GO humain = 15 min édition.
*   **Ordre de priorité** : **#5 (Dernier, dépend F2)**. Cosmétique mais contractuel.

**VERDICT : GO**
**CONFIANCE : 100 %**
**HYPOTHÈSES** : 1) Le prompt voix est assemblé dynamiquement (template + injection identité) et non hardcodé en dur dans le binaire. 2) Le TTS/STT ne parse pas le prompt pour en déduire des permissions (seul le code Rust le fait).
**CE QUI CHANGERAIT L'AVIS** : Si le prompt voix est compilé dans le binaire (rebuild requis) ou si une couche intermédiaire (ex: function calling ouvert) utilise le texte du prompt pour autoriser des tools.
**AMÉLIORATION PROPOSÉE** : 1) Ajouter clause explicite : « Je suis un observateur en lecture seule. Toute action nécessite validation humaine explicite via l'interface CLI/GUI. » 2) Versionner le prompt vocal (`voice_prompt_v3.md`).

---

### SYNTHÈSE

1.  **F1 (Justesse)** → 2. **F2 (Identité)** → 3. **F3 (Dashboard Cortana)** → 4. **F4 (Hub unique)** → 5. **F5 (Prompt voix)**.
**Risque n°1** : **F4 (Hub unique)** — Supprimer le fallback local dans `brain.rs` *avant* que le hub ne prouve sa robustesse offline (timeout, santé Ollama) = cockpit muet en cas de coupure réseau.
