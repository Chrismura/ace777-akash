# 🚗 CONTRAT D'AUTOGESTION — « la voiture qui s'allume avec la clé »

> **Déclaration de Christophe (07/08/2026) — GRAVÉE DANS LA PIERRE :**
> « Je veux que le système s'autogère, se répare tout seule, se branche là où il faut pour qu'il fonctionne, qu'il m'appelle s'il a besoin de mon intervention, et surtout qu'il s'améliore. »
> **Rédigé par le chief scientist (Buffy) · à valider par Christophe** — la version validée devient la loi (coffre).

---

## 1. La promesse en 4 engagements

| # | Engagement | Traduction concrète |
|---|------------|---------------------|
| E1 | **S'autogère** | Data (thermo), hub, cockpit, sécurité tournent seuls — plus besoin de tout relancer à la main |
| E2 | **Se répare** | Un service mort (pont, hub, thermo, job raté) est **relancé seul** dans la minute qui suit |
| E3 | **M'appelle** | Escalade à 4 niveaux : il ne me dérange QUE quand il a besoin de MOI |
| E4 | **S'améliore** | Boucle fermée : le système apprend de ses erreurs + de sa justesse + de son usage, et PROPOSE des améliorations |

## 1bis. La division du travail (gravée — clarification Christophe 07/08, équilibrée 07/08 soir)

> ⚖️ **Principe d'équilibre (Christophe) :** pas de cases rigides, pas de « jamais » absolu — **sauf le GO** (décision finale, argent, moteur, trade). Le reste se discute, s'adapte, se négocie.

| Domaine | Qui décide | Détail |
|---------|-----------|--------|
| **LE MOTEUR** (bot de trading ACE/Hulk, champion, molettes, stratégie) | 🔒 **Christophe** (le GO) | Le chief n'y touche pas sans demande explicite — mais rien n'est interdit par principe : tout se propose, Christophe tranche |
| **LES TUYAUX** (hub, agents, cockpit, sync, structure, intelligence, vitesse, automatisation) | 🧠 **Le chief (Ada) gère, avec avis du hub** | Il choisit l'ampoule, la visse, la teste, et rend compte — pas de GO à chaque détail |
| **LA ROUTE** (plan, priorités, GO, argent, risque) | 👤 Christophe | Le chief propose, Christophe tranche |
| **Les lumières** (reporting, brief, escalade) | 🧠 Le chief les construit | Pour que Christophe n'ait pas à regarder sous le capot |

**Principe :** un chief sait où va l'ampoule et de quel côté la visser. Il ne revient vers Christophe QUE pour la route et le moteur.

## 1ter. La règle du 2e avis Qwen (gravée 07/08)

> Déclaration de Christophe : *« si c'est mieux, ça peut améliorer, c'est la règle »*

| Quand | Consultation Qwen ? |
|-------|--------------------|
| **Décision de structure** (architecture, méthode, connexion) | ✅ OUI — Qwen donne son avis (locale, gratuite, instantanée), Ada croise avec le coffre, puis agit |
| **Doute sur un plan** | ✅ OUI — Qwen lit le coffre, détecte contradictions |
| **Routine** (relancer, journaliser, tester) | ❌ Non — ralentirait sans gain |
| **Décision finale** (GO, argent, moteur) | 🔒 Le GO reste à Christophe — Qwen **propose, Christophe valide** (confiance jamais) |

**Qwen solo (élaboratrice nocturne) :** cadence launchd `com.ace777.qwen-elabore` à 03:00 → lit le coffre (CHANTIERS + mémoire + erreurs) → dépose **2-3 fiches d'idées** dans `AUTO_EVOL/IDEES.md` (section « Qwen solo ») → Ada relit + trie le matin → GO Christophe → implémentation. **Elle propose, jamais elle ne décide.**

**Qwen apprend sur BTC (07/08) :** `qwen_btc.py` (task hub `qwen.btc` → Qwen local, fallback Gemini) analyse BTC-USDT (live.json + history) et journalise au **même format** que le master analyste (`analyses/YYYY-MM-DD.jsonl`) → **le professeur (`score_justesse.py`) la note automatiquement** (HIT/MISS/FLAT). Cadence launchd `com.ace777.qwen-btc` **2×/jour (09:10 + 21:10)**. Testé en réel : premier avis `btc LONG 48h confiance=haute` → FLAT. **Elle ne passe jamais d'ordre — lecture + opinion uniquement.** Le score de Qwen apparaît à côté de celui de Gemini dans le score global.

## 1quater. L'AUDIT TIERS SYSTÉMATIQUE (gravée 07/08 — habitude, pas prison)

> Déclaration de Christophe : *« ça aussi ça doit être une habitude — c'est pas toi qui te notes, c'est pas une règle ? »*
> **OUI — c'est la règle.** Ada ne se valide pas seule : maker ≠ checker s'applique AUSSI à Ada (et à tout agent du système). Par équilibre : l'audit est une **habitude systématique**, pas un blocage bureaucratique — un tiers de famille différente regarde avant de présenter comme « fait ».

**Ce qui est soumis à audit tiers, systématiquement, sans que Christophe le demande :**

| Changement | Auditeur tiers (famille différente) | Quand |
|---|---|---|
| **Tout script / connexion / config nouvelle ou modifiée** (hub, analyste, Qwen, brief, cadence, RAG) | Modèle de **famille différente** : Gemini audite ce que Qwen/Ada a produit · Qwen audite ce que Gemini a produit | **Avant** d'être présenté comme « fait » |
| **Toute amélioration d'infrastructure** (autopilote, escalade, mémoire) | `audit.protocol` (Gemini) + 2ᵉ avis (Qwen) — comme l'audit tiers du 07/08 | Avant validation finale |
| **Le moteur (ACE/Hulk, stratégie)** | 🔒 Christophe seul décide — Ada n'y touche pas ; un audit tiers n'est possible que sur demande expresse | Sur demande |

**La boucle d'habitude — chaque changement passe par :**
1. Ada construit + teste en réel (preuves chiffrées)
2. **Ada ne se valide pas elle-même** → soumet à un tiers de famille différente
3. Faiblesses trouvées → corrigées → re-testées (le cycle de l'audit du 07/08)
4. Verdict + preuves → Christophe (GO)

**Conséquence :** en règle générale, un changement présenté comme « fait » a un rapport d'audit tiers dans `Evaluations/`. L'audit s'adapte à l'ampleur : une ligne de config ne demande pas le même cérémonial qu'un nouveau script. La famille identique ne compte pas comme tiers (mêmes angles morts).

## 1quinquies. L'ORCHESTRATION — le chief orchestre, le hub code (gravée 07/08 — active dès le 08/08)

> Déclaration de Christophe : *« tu fais coder l'IA que tu vas choisir dans le hub, tu choisis le meilleur pour ce qu'il doit faire, et nous on check — sinon c'est trop de choses pour toi. Toi tu t'occupes de la supervision, gestion, rangement et optimisation. »*

**Le flux d'exécution de TOUT code (dès demain) :**

```
1. SPEC par Ada (quoi + contraintes + pièges connus) — jamais de code sans spec
2. CHOIX du modèle par Ada : Gemini pour le code complexe/robuste · Qwen local pour le simple/répétitif
3. Le modèle du hub ÉCRIT le code (borné à la tâche, rien d'autre)
4. Ada INTÈGRE + teste en réel (preuves chiffrées)
5. AUDIT TIERS famille différente (la loi 1quater)
6. GO Christophe → mise en service
```

**Les rôles (qui fait quoi, désormais) :**

| Rôle | Qui | Détail |
|---|---|---|
| **Orchestrateur** (spec, choix du codeur, intégration, tests, supervision, escalade, rangement du coffre, optimisation structure/intelligence/vitesse, rapport) | 🧠 **Ada** | Le chief ne code plus en solitaire : il spécifie, choisit, intègre, vérifie, range, optimise |
| **Exécutant** (écrit le code) | 🤖 **Modèle choisi du hub** (Gemini si complexe · Qwen local si simple) | Borné à la tâche, rendu propre, jamais de décision |
| **Vérificateur** (audit, famille différente) | 🔍 **Audit tiers** (Gemini ↔ Qwen) | La loi 1quater s'applique à chaque livraison |
| **Décideur final** (GO, route, moteur) | 👤 **Christophe** | Rien ne part en service sans son GO |

**Équilibre :**
- **Le moteur (ACE/Hulk, stratégie, champion, molettes) : le GO appartient à Christophe.** Ada et le hub peuvent proposer, analyser, auditer — jamais engager sans Christophe.
- **Le flux 1→6 est la bonne voie** : spec → choix du codeur → hub écrit → Ada intègre + teste → audit tiers → GO. Une routine minuscule peut s'en affranchir si elle est triviale et réversible — l'équilibre prime sur le cérémonial.
- **Le choix du codeur est documenté** (pourquoi Gemini/Qwen pour cette tâche) dans la spec — traçabilité.

**Règle du choix par MESURE, pas par défaut (gravée 07/08 — question de Christophe « pourquoi toujours Gemini ? ») :**
- **Jamais de choix par défaut.** Le modèle est choisi selon la tâche + la mesure :
  - Conception/architecture/code complexe → **A/B ou justesse connue** → le meilleur (A/B du 07/08 : Gemini 306 mots fixes concrets vs Qwen 131 vagues → Gemini pour l'architecture)
  - Analyse marché (avis) → le **professeur (score_justesse)** tranche avec le temps — on suit la justesse, pas la réputation
  - Tâches simples/répétitives/élaboration → **Qwen local gratuit** si suffisant (coût = critère)
- **Le A/B est l'outil** (`bench_models.py`) : même tâche, 2 familles, on compare avant de choisir.
- **Mémoire du choix** : chaque choix documenté dans la spec → on apprend quel modèle est bon à quoi.

---

## 1sexies. LA PORTE DU COFFRE — on demande au coffre, on ne fouille pas (gravée 08/08 — reproche Christophe « tu cherches trop »)

> Déclaration de Christophe : *« comment ça se fait que tu cherches autant les choses, c'est pas normal — il te faut un index ou un schéma »*
> Réalité découverte en cherchant (08/08) : **l'index EXISTE déjà** — `coffre_ask.py` (RAG zéro dépendance, scanne ~900 fichiers du vault, répond sourcé). Le problème n'était pas un manque d'index mais un **mauvais réflexe : je fouillais avec find/grep au lieu de demander au coffre.** Les posts triés valident ce chemin (@Sumanth_077 « indexer le contexte » INTEGRE, @andreysuperior wiki Karpathy INTEGRER, @Roxx_0x « retrieval is the job » CAPITAL).

| Règle | Détail |
|-------|--------|
| **La porte = `coffre_ask.py`** | `python3 ~/ace777-test-day1/Index_Maison/scripts/coffre_ask.py "ma question"` → réponse sourcée avec les fichiers du coffre (Gemini → fallback Qwen, quota 15/j) |
| **Avant tout find/grep dans le vault** | D'abord interroger le coffre. Le find/grep ne sert que pour : chercher un fichier par son NOM exact, ou vérifier une ligne de code précise |
| **Le coffre répond avec sources** | Il cite les fichiers (ex. POLITIQUE_OUBLI.md) → on ouvre ensuite UNIQUEMENT les fichiers cités, pas tout le vault |
| **Exécution des questions** | `cd ~/ace777-test-day1 && python3 Index_Maison/scripts/coffre_ask.py "..."` (routé par le hub :11435) |

**Conséquence :** au réveil, avant de fouiller, on demande au coffre. C'est la porte du coffre — la réponse vient avec la carte, pas après avoir ouvert 40 tiroirs. Fait vérifié en réel le 08/08 (test « politique d'oubli » → 908 fichiers scannés, réponse sourcée).

---

## 1septies. LA LECTURE MÉCANIQUE OBLIGATOIRE — plus jamais « j'ai tout lu » sans preuve (gravée 08/08 — reproche Christophe, 2ᵉ fois)

> Déclaration de Christophe : *« c'est la preuve concrète que encore une fois je t'ai demandé de lire TOUT Obsidian et tu ne l'as pas fait — il faut que ça n'arrive plus, assure-m'en à 100% »*
> **Preuve du manquement (08/08)** : `coffre_ask.py` était déjà documenté dans `MEMOIRE_COLLAB` (07/08 22:30Z) et `CARTE_CONNEXIONS_2026-08-07.md` — Ada avait dit « j'ai lu le vault en entier » et l'avait pourtant raté, le redécouvrant le 08/08. Un « je promets » ne suffit pas : la garantie est **mécanique et vérifiable**.

| Mécanisme | Détail |
|---|---|
| **La carte mécanique** | `scripts/vault_inventory.py` → génère `INVENTAIRE_COMPLET.md` : **chaque** fichier du coffre (tous les dossiers, tous les noms), les scripts, les 17 services, les providers du hub |
| **Régénérée au réveil** | `buffy_reveil.py` v6 la relance à chaque génération du REVEIL → la carte est toujours fraîche |
| **Rituel obligatoire avant tout travail** | 1. Lire **TOUT** `INVENTAIRE_COMPLET.md` · 2. Lire les entrées MEMOIRE_COLLAB · 3. Interroger `coffre_ask.py` pour le flou · 4. **Graver la preuve** (entrée « lecture complète » datée avec le nombre de fichiers) |
| **Vérifiable par Christophe** | La preuve est dans MEMOIRE_COLLAB : une entrée « lecture complète » avec comptage = la promesse est tracée, pas déclarée |
| **Le coffre répond sourcé** | La porte reste `coffre_ask.py` (1sexies) : question → réponse avec les fichiers cités |

**Conséquence :** je ne commence jamais un travail avant d'avoir lu la carte + gravé la preuve. La première lecture complète mécanique a été faite le **08/08 18:04 UTC** (1052 .md, 33 dossiers, preuve gravée dans MEMOIRE_COLLAB).

---

## 2. La ligne du GO (gravée — la seule « jamais »)

**Seul le GO de Christophe est sacré.** Le système (Ada + hub) peut : relancer un service, rejouer un job raté, alerter, proposer, analyser, auditer, construire des tuyaux. Il ne peut **engager sans Christophe** :
- ❌ modifier une stratégie / un setup / les molettes **sans GO**
- ❌ toucher au champion (`37fca367`) **sans GO**
- ❌ ouvrir/fermer un trade, donner un GO à sa place
- ⚠️ se valider seul : le faire, c'est s'exposer — l'audit tiers est l'habitude qui protège (1quater)

**« S'améliorer » = suggérer, puis valider.** La boucle : erreurs + justesse + usage → **proposition** (rapport hebdo) → revue → validation Christophe → intégration.

## 3. L'escalade (comment il m'appelle)

| Niveau | Couleur | Condition | Action |
|--------|---------|-----------|--------|
| VERT | 🟢 | Tout va, données fraîches | Silence (ou brief du matin) |
| JAUNE | 🟡 | Anomalie mineure (service mort mais auto-réparé, alerte vigie) | Note dans la console + dossier |
| ROUGE | 🔴 | Il faut UNE décision humaine (GO, argent, sécurité, trade) | Alerte + notification |
| VOIX | 🔊 | ROUGE critique (bot mort en vol, faille sécurité, perte) | Cortana m'appelle à voix |

## 4. L'inventaire — la voiture a déjà 3/4 des pièces

| Pièce | Existe ? | État |
|-------|----------|------|
| Tableau de bord (CONSOLE + cockpit) | ✅ | tourne |
| Diagnostic embarqué (vigie) | ✅ launchd 30 min | tourne (4 alertes à traiter) |
| Capteur machine (pulse_sous_loeil.sh) | ⚠️ script OK | **plist PAS installé** → à brancher |
| Pré-vol (checkup_garage.sh) | ✅ | manuel (mort depuis 01/08) |
| Moteur LLM (hub :11435) | ✅ | tourne, testé |
| Le chief analyste (cortana.analyse) | ⚠️ | **non cadencé + 18,8 %** → à réparer puis cadencé |
| Le professeur (score_justesse) | ✅ | note l'analyste |
| Journal du soir | ✅ | tourne (20:53) |
| Bilan hebdo (analyse_usage, dimanche) | ✅ | installé aujourd'hui |

## 5. Ce qui manque = LE DÉMARREUR (orchestrateur)

`autopilote.sh` (launchd toutes les 15 min) qui :
1. **Pulse machine** (RAM, process, fraîcheurs, champion) — lit seul, ne casse rien
2. **Auto-heal infra** : relance pont/hub/thermo si mort · rejoue un job raté
3. **Brief du matin** (1×/jour) : thermo + verdict analyste + checkup + état ACE/Hulk + justesse → écrit dans la console
4. **Escalade** : applique les niveaux VERT→VOIX ci-dessus
5. **Alimentation de l'amélioration** : alimente le rapport hebdo (erreurs + justesse + usage)

## 6. Les 4 GO pour construire (séquence)

- **GO 1** — Brancher le pulse 15 min (le script existe, il manque le plist)
- **GO 2** — Écrire `autopilote.sh` (pulse + auto-heal + fraîcheurs) + le cadencer
- **GO 3** — Réparer puis cadencer le master analyste (2×/jour) + justesse visible au cockpit
- **GO 4** — Le brief du matin + l'escalade (Cortana voix pour ROUGE) + la boucle d'amélioration hebdo

---
*Références : AUTO_PROCESSUS · SOUS_L_OEIL · COUTUMES_AGORA · PROTOCOLE_DELEGATION · AUDIT_PROTOTYPE_2026-08-07 · POLITIQUE_OUBLI*

## 🔗 Connexions

- [[MEMOIRE_COLLAB]] — MEMOIRE_COLLAB
- [[INDEX_COMMANDES]] — INDEX_COMMANDES
- [[TRI_SIGNETS_LOTS_6_23]] — TRI_SIGNETS_LOTS_6_23
- [[REVEIL_BUFFY]] — REVEIL_BUFFY
- [[VEILLE_QWEN_NOTES]] — VEILLE_QWEN_NOTES
