# AVIS juge (provider Google Gemini)

*Rapport d'expertise et d'arbitrage — Superviseur Buffy (31/08/2026)*  
*Avis technique strict, sans concession.*

---

### A) [E] Daily notes : une note unique vs sections par agent
* **Le constat :** Une note unique où tous les agents font du `append()` en concurrence directe est une aberration architecturale. Même avec un verrou ou une queue séquentielle au niveau du pont CLI, vous allez droit vers des conflits de fusion textuelle, un historique illisible et un contexte pollué pour les LLM.
* **Mécanisme anti-collision & Recommandation :** 
  1. **Structure hybride (Fichiers séparés, vue agrégée) :** Chaque agent écrit *exclusivement* dans sa propre note journalière (ex: `Daily/2026-08-31_Agent_CortanaA.md`). 
  2. **La vue agrégée :** Obsidian gère nativement les requêtes (via Dataview ou la syntaxe native des bases). Ne faites pas fusionner les textes par les agents. Laissez Obsidian afficher dynamiquement les sections des différents agents dans une note maître du jour (`Daily/2026-08-31.md`) via des inclusions ou des blocs de requêtes.
  3. **Pour les LLM :** Le LLM lit la note maître du jour qui transclut (ou liste) les notes des sous-agents. Zéro risque de collision d'écriture, isolation parfaite des pannes d'agents.

---

### B) [F] Wikilinks : script automatique vs Day Zero
* **Le constat :** 77% de notes orphelines (1341/1733), c'est un cimetière de données, pas un second cerveau. Un script brut de recherche/remplacement textuel pour injecter des `[[wikilinks]]` sur le nom des actifs est une **catastrophe assurée** (faux positifs massifs sur les noms communs, les abréviations, etc.).
* **Recommandation :** 
  1. **Bannissez le script aveugle de rétro-injection.** Il va détruire la précision sémantique de votre base.
  2. **Approche mixte "Day Zero + NLP ciblé" :** 
    * *Day Zero strict :* Désormais, tout nouveau script ou agent *doit* générer des wikilinks validés par le Gatekeeper à la création.
    * *Pour l'existant :* Ne traitez pas les 1341 notes d'un coup. Lancez un script d'enrichissement intelligent *une seule fois* mais basé sur l'extraction d'entités (NER) ou une validation par LLM (qui vérifie le contexte avant de poser le crochet `[[ ]]`), et non sur une simple regex de dictionnaire.

---

### C) [G] Canvas : utile ou sur-ingénierie ?
* **Le constat :** Le `.canvas` piloté par JSON est un gadget pour humains, un gouffre à tokens et en maintenance pour des agents autonomes. Les LLM n'ont **rien à faire** d'une interface graphique spatiale 2D.
* **Recommandation :** 
  1. **Repoussez le Canvas à plus tard (Sur-ingénierie à ce stade).** Vos priorités sont l'intégrité des données (A', B) et la traçabilité (E). 
  2. Si vous persistez : limitez-la strictement à une carte de synthèse macro (Max **30 à 50 nœuds** : uniquement les Top Actifs et les Institutions majeures). Tout le reste doit passer par le texte structuré et les graphes de liens natifs Obsidian.

---

### D) [B]+[A'] : Migration des scripts et Frontmatter sur les synthèses
* **Le wrapper global est OBLIGATOIRE :** Réécrire 60 scripts un par un est une perte de temps absurde et une source de bugs humains. 
* **La séquence la plus sûre (Moins de casse) :**
  1. **Étape 1 (Le Wrapper Drop-in) :** Créez une bibliothèque ou un script proxy (ex: `obsidian_writer.py`) qui intercepte l'ancienne écriture dans `OUTBOX_OBSIDIAN` ou expose une fonction `write(path, content, metadata)`. Ce wrapper route *en interne* vers le Gatekeeper et `obsidian_cli_bridge.py`.
  2. **Étape 2 (Migration silencieuse) :** Modifiez la variable d'environnement ou le point de montage de `OUTBOX_OBSIDIAN` pour qu'il pointe vers ce wrapper. Les 60 scripts continueront d'écrire "comme avant" (zéro modification des 60 scripts dans un premier temps), mais l'écriture sera capturée, typée et validée.
  3. **Étape 3 (Frontmatter des synthèses) :** Intégrez l'injection automatique de ce frontmatter *directement dans le wrapper*. Si un script envoie une synthèse sans frontmatter `type: synthese_ia`, le wrapper l'ajoute à la volée selon le dossier de destination.
  4. **Étape 4 (Nettoyage progressif) :** Nettoyez les 60 scripts pour qu'ils appellent directement `write_typed()` quand vous aurez le temps, mais l'urgence opérationnelle est résolue dès l'Étape 2.

---

### E) L'AMÉLIORATION CONCRÈTE & AVIS STRICT GLOBAL

* **Ce qui est bon :** Le triptyque *CLI officielle + Gatekeeper (types stricts) + Circuit Breaker* est une excellente architecture de défense. Vous avez compris qu'écrire directement dans un vault Obsidian sans gardes-fous mène à la corruption de données.
* **Ce qui est risqué (Mon coup de gueule / Avis strict) :** 
  * Vous construisez une cathédrale d'ingénierie (skills JSON-canvas, pont CLI complexe, 4 types stricts) tout en traînant une dette technique colossale (60 scripts obsolètes dans une outbox, 77% d'orphelines). 
  * **Arrêtez de vouloir tout automatiser par la force brute.** Le risque majeur est que votre système s'effondre sous son propre poids de vérifications redondantes (fail-open disque + CLI + Gatekeeper + futurs wrappers).
* **L'amélioration concrète de mon cru :** 
  Mettez en place un **"Dead Letter Office" (DLO) Obsidian**. 
  Actuellement, si le Gatekeeper rejette une écriture ou si le pont CLI échoue (Obsidian fermé + fail-open disque raté), que se passe-t-il ? Les données s'évanouissent ou s'entassent en erreur silencieuse. 
  Créez un dossier `.agents/dalo/` où tout payload rejeté par le Gatekeeper est stocké au format JSON brut avec l'erreur explicite. Un agent "Nettoyeur" passe une fois par jour pour notifier le superviseur des scripts qui envoient de la merde. *La résilience ne vient pas seulement du fait de savoir écrire, mais de savoir tracer proprement ce qui a échoué.*
