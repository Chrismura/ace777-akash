# AVIS gemini (provider Google Gemini)

Reçu, superviseur Buffy. Voici un audit sans langue de bois et des décisions tranchées pour finaliser ces chantiers d’ici au 31/08/2026. 

---

### A) [E] Daily notes : une note unique vs sections par agent ?
*   **Mon avis strict :** Une note unique appendée simultanément par des agents asynchrones est **une aberration technique** qui garantit des conflits de fusion, des écritures entrelacées illisibles pour un LLM et l'explosion de votre circuit breaker. Les LLM n’ont pas besoin d’un "journal fourre-tout" chronologique brut ; ils ont besoin d’un **état de situation structuré**.
*   **Mécanisme anti-collision & Recommandation :** 
    1. *Abandonnez l'append brut sur une note unique.*
    2. Créez un dossier `/Agents_Logs/YYYY-MM-DD/` où **chaque agent écrit sa propre note** (`[nom_agent].md`) via le pont.
    3. Utilisez une note journal *centrale* (ou une vue Dataview) qui fait simplement des inclusions (`![[...]`) ou liste les liens vers les notes des agents du jour. Le LLM lit ce dossier en un bloc via une requête contextuelle propre, sans risque de corruption.

### B) [F] Wikilinks : script automatique vs Day Zero ?
*   **Mon avis strict :** Un script de type *Regex-matching* qui balance des `[[wikilinks]]` à travers 1733 notes existantes à l’aveugle est **une bombe à retardement**. Il va créer des centaines de faux positifs (ex: nom d'un actif qui est un mot commun en français, ou homonymes), polluer votre graphe et ruiner la confiance dans vos métadonnées.
*   **Recommandation :** **Approche Hybride ciblée + Day Zero.**
    *   *Pour l'existant (77% orphelines) :* Ne touchez pas au corps des textes avec des scripts naïfs. Utilisez plutôt une **requête Dataview globale** basée sur le frontmatter (ex: lier les fiches qui partagent le même `tag` ou la même `famille`) pour simuler du lien sans modifier les fichiers.
    *   *Pour le futur (Day Zero) :* Règle absolue : tout nouveau script de génération (via le Gatekeeper) **doit** injecter explicitement les wikilinks dans le corps, validés par le type strict.

### C) [G] Canvas : utile ou sur-ingénierie ?
*   **Mon avis strict :** À ce stade, avec 77% de notes orphelines et des scripts en cours de migration, **le Canvas est de la sur-ingénierie cosmétique**. Vos agents pilotent des données textuelles/structurées (JSON/Markdown), pas des interfaces graphiques. Un fichier `.canvas` généré par LLM finit invariablement en pelote de nœuds indéchiffrable.
*   **Recommandation :** **À repousser à l’après-migration.** Si vous y tenez absolument pour l'humain (dashboard visuel), limitez-le strictement à **1 seul Canvas de synthèse haut niveau** (ex: Top 10 Actifs ↔ Institutions clés), plafonné à 30 nœuds max, généré en lecture seule une fois par jour. Pas d'écriture dynamique par les agents.

### D) [B]+[A'] : Migration des scripts et Frontmatter sur les synthèses
*   **Ordre de migration & Wrapper :** 
    1. Réécrire 60 scripts un par un est suicidaire (perte de temps, bugs de régression). **Il FAUT un wrapper global.**
    2. **La séquence la plus sûre :** Ne touchez pas aux 60 scripts dans un premier temps. Modifiez l'implémentation de la fonction de sortie de `OUTBOX_OBSIDIAN` : au lieu de faire un simple `cp` vers le disque, interceptez les flux pour les faire passer de force par la fonction `write_typed` du pont CLI. Le wrapper agit comme un proxy transparent.
    3. *Frontmatter sur les synthèses [B] :* Traitez-le par vagues de familles de scripts. Le Gatekeeper doit rejeter toute synthèse n'ayant pas le type `synthese_ia` dès le passage du wrapper.

### E) Amélioration critique & Avis global strict

*   **Ce qui est bon :** L’architecture défensive mise en place (Gatekeeper, types stricts, read-back hash, fail-open disque, circuit breaker) est d’un excellent niveau de robustesse industrielle. Vous avez pensé à la résilience.
*   **Ce qui est risqué :** Vous sous-estimez la **dette technique du Legacy** (~60 scripts + 1341 notes orphelines). Vouloir tout nettoyer (graphe, vieux scripts, logs unifiés) en même temps que vous déployez le pont va bloquer le système sous les exceptions.
*   **Mon amélioration critique (de mon cru) :** 
    Instaurez un **mécanisme de "Dry-Run" obligatoire pour le Pont CLI** pendant 48h. Avant que le wrapper ne force l'écriture réelle via le pont, logguez toutes les tentatives des 60 scripts dans une table de validation. Si le Gatekeeper lève une exception de type ou de frontmatter, le script legacy est bloqué *avant* de corrompre Obsidian, et une alerte est remontée. 
    *En clair : forcez la conformité par la périphérie (le pont/wrapper) sans modifier le cœur des scripts existants.*
