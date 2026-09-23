# 🥇 RÈGLE D'OR — la constitution opérationnelle d'ACE777

> **Statut : v2 — RECENSEMENT + PROPOSITIONS SOURCÉES, à finaliser avec Christophe.**
> Ajout du **19/09** (soir) : consultation de la **famille du hub** (4 angles, dont **CONTESTE**) +
> **recherche externe** (SRE, GitOps, chaos engineering, Release It!, FDIR spatial, two-person rule,
> défense en profondeur). Les **5 règles candidates (R10–R14)** sont proposées en bas — elles ne sont
> **pas encore ratifiées**. Synthèse complète : `CONSULTATION_FAMILLE_REGLES_OR_20260919/SYNTHESE.md`.
> Établi le **2026-09-19** par Buffy, sur demande : « tout faire pour améliorer RÈGLE D'OR…
> établir une seule liste ». Les règles ci-dessous sont **recopiées de leurs sources réelles**
> (chacune est citée) : rien n'est inventé. Les points marqués ❓ attendent ta décision.
>
> Pourquoi une note unique : les règles d'or existent aujourd'hui **éparpillées** dans au moins
> 6 documents (Constitution, POLITIQUE_OUBLI, PREFS_STACK, INDEX_COMMANDES, la mémoire, les
> scripts). Résultat : on les oublie ou on les applique à moitié. **Une seule liste = une seule
> loi.** C'est le principe qui a réparé la mémoire ce jour-là : *une seule vérité, des miroirs
> explicites.*

---

## ✍️ 1. PARLER SIMPLE (l'art de la vulgarisation)
> Source : `PREFS_STACK.md` — « Règle d'or — parler simple (31 juil.) » · règle Cursor
> `.cursor/rules/vulgariser-par-defaut.mdc`

Expliquer **comme à un enfant intelligent** : court, clair, **une idée à la fois**. Le jargon
et le code profond **seulement si Christophe le demande** (ou colle une erreur à réparer).
**Si Christophe ne comprend pas → c'est nous qui avons mal expliqué** : on recommence plus simple.

**Statut** : ✅ appliquée. *Mesuré* : elle est vérifiée à chaque réponse par le vérificateur (`verifier_regles_or.py`).

## 🧠 2. CORPS LOCAL / CERVEAU CLOUD (la règle d'or fondatrice)
> Source : `ACE777-Constitution.md` §2 — Principe fondateur

**« La RAM sert à *raisonner*, jamais à *stocker*. Le lourd part dans le cloud. »**
Corollaire : les organes locaux restent **lisibles hors-ligne en mode dégradé** (dernier état connu).
8 Go de RAM unifiée n'est pas une limite, c'est **l'architecture** (pattern Karpathy / LLM-Wiki).

**Statut** : ✅ appliquée. *Mesuré le 19/09* : mémoire 62 % libre (`memory_pressure`) · **0 IA locale
chargée** (Ollama au repos, 15 Mo) · le raisonnement passe par le **hub** (10 providers cloud gratuits) ·
tout le prototype tient en **~190 Mo** (contre 1 442 Mo pour Brave — qui n'est PAS du prototype).

## 🛑 3. GO HUMAIN — on ne lance RIEN sans le dire
> Source : `INDEX_COMMANDES.md` — « Règle d'or : ne lance **jamais** ACE ni Hulk sans avoir dit
> **GO** et sans Mac froid » · doctrine maison « **1 GO = 1 chose** »

- Aucun **ordre de marché**, jamais, sans GO explicite (**0 ordre**).
- Aucun run ACE/Hulk sans **GO** + **Mac froid** + **portes de stérilité** (`verif_sterilite.sh --pre-run`).
- **1 GO = 1 chose** : un mandat = un périmètre ; le reste attend.

**Statut** : ✅ appliquée. *Mesuré le 19/09* : ACE duo **OFF**, HULK paper **ON** (+18,12 $) — conforme
au GO documenté ; aucune écriture moteur aujourd'hui.

## 🔍 4. SURFACER LES CONTRADICTIONS (jamais les masquer)
> Source : `POLITIQUE_OUBLI.md` — étage **Reconcile** : « contradictions **surfacées** → Christophe
> décide (**règle d'or n°1**) »

Toute incohérence (chiffre qui ne colle pas, deux sources qui se contredisent, un organe qui dit
vivant alors qu'il est mort) doit être **remontée**, jamais lissée. On ne devine pas la décision :
**on la donne à Christophe.**

**Statut** : ✅ appliquée le 19/09 (cf. § Contradictions surfacées du diagnostic) : le chiffre RAM
trompeur a été corrigé publiquement, le vrai bug de backup débusqué, 2 faux positifs de gardiennage retirés.

## 🔒 5. UN SCELLÉ NE S'ÉCRASE JAMAIS EN SILENCE
> Source : mémoire maison, gravée le **19/09** après un vrai dérapage (la v1 de `sync_plists.sh`
> a clobberé 4 fichiers scellés → la veilleuse a crié 4 intrusions, à raison)

Sur un fichier **scellé** (registre md5) : on **DÉCLARE**, on n'écrase pas. Règle dérivée :
**on travaille sur des copies**, jamais sur le scellé ; chaque modification = **1 ligne en mémoire**
+ **backup `/tmp/*.bak-avant-*`**.

**Statut** : ✅ appliquée. *Mesuré* : **83 scellés, 0 écart** ; veilleuse **STABLE**.

## 🪞 6. UNE SEULE VÉRITÉ, DES MIROIRS EXPLICITES, RIEN DE SILENCIEUX
> Source : doctrine née des 2 fissures du 05–19/09 (boucle mémoire, `POINT_REPRISE_DERNIER`)

- **Une** source de vérité (ex. `Index_Maison/MEMOIRE_COLLAB.md`) ; les copies sont **déclarées**.
- Ce qui **diverge doit être VISIBLE** (jamais un écart muet). *Leçon* : une **liste blanche** qui
  perd une entrée casse une boucle **sans bruit** — donc **découvrir** au lieu de **lister**.
- Ce qui est **installé** doit être **versionné** (0 hors repo), et ce qui vit **hors git** doit avoir
  une source de restauration (**miroir** ou **git amont**).

**Statut** : ✅ appliquée. *Mesuré le 19/09* : 97 agents, **0 hors repo**, drill **READY**, mémoire
232 Ko identiques canon↔coffre.

## 🆓 7. ZÉRO EURO
> Source : contrainte maison répétée (hub = providers gratuits)

**0 €** : on n'utilise que les **providers gratuits** du hub. Brancher une **API payante** = **GO humain**.

**Statut** : ✅ appliquée. *Mesuré* : le hub tourne sur `providers.json` — **100 % `free: true`**.

## 📏 8. PREUVE DATÉE, OU RIEN
> Source : contrainte maison « une affirmation sans preuve datée ne compte pas » · leçon 19/09
> « une limite non mesurée est une bombe, pas un garde-fou »

- Toute affirmation = **preuve datée** (fichier, md5, mesure).
- **Un gardien ne s'ajoute pas** : il s'**accroche** à un organe qui vit déjà (sinon c'est un 98ᵉ agent).
- Une **limite non mesurée** est une bombe : on **mesure** avant d'en poser une.
- Un **drill**, ça se **répète** : une sauvegarde jamais testée est une hypothèse, pas une sauvegarde.

**Statut** : ✅ appliquée. *Mesuré* : drill branché sur `git_push_auto` (3 h) ; gardiens dans la page vol.

## 👁️ 9. LIRE, NE PAS ÉCRIRE (un gardien ne modifie pas ce qu'il surveille)
> Source : `superviseur_core.sh` — « Règle d'or : LIT state.json, ne l'écrit JAMAIS »

Tout organe de **surveillance** est **lecture seule**. Il observe, il crie, il n'agit pas sur l'état
qu'il juge (sinon il fausse sa propre mesure).

**Statut** : ✅ appliquée. *Mesuré* : `veilleuse_synapses` · `chien_de_garde` · `drill_restauration`
· `derive_memoire` — tous read-only.

---

## 🧭 LES 3 PILIERS (organisation proposée — option, pas remplacement)
> Source : angle **SIMPLE** de la consultation famille + **GitOps** / **SRE**.

Les 9 règles se regroupent en **3 piliers** lisibles : **1. ÉTAT DÉCLARÉ** (ce qui est vivant est dans le
repo ; ce qui diverge est visible → #5, #6, #9) · **2. ACTION MAÎTRISÉE** (rien sans GO ; 1 GO = 1 chose ;
0 € → #1, #3, #7) · **3. VÉRITÉ MESURÉE** (preuve datée ; contradictions surfacées → #2, #4, #8).
**Décision ❓** : garde-t-on 9 règles + 3 piliers, ou seulement les 3 piliers avec les 9 en annexe ?

---

## ✅ R10 à R15 — APPLIQUÉES ET MESURÉES (19/09, GO Christophe « applique au mieux » / « go 1,2,3 »)

> Issues de la famille (4 angles, dont CONTESTE) + recherche externe. Toutes respectent les
> contraintes : **0 €**, **aucune régression**, **aucun 98ᵉ agent**, et **mesurables** (PASS/FAIL).
> Elles sont **toutes mesurées** par `scripts/verifier_regles_or.py` et **visibles** dans la page vol
> (gardien « Règles d'or ») : le 19/09 à 13:21Z → **11/11 tenues**.

### R7 — DÉROGATION DÉCLARÉE POUR `inferx` (décision Christophe 19/09)
> Le provider **`inferx`** est marqué payant mais utilisé **sans facturation** (clé gratuite).
> Christophe : « mettre de côté inferx, peut-être qu'il sera de nouveau disponible gratuitement ».
> Ce n'est **pas** une violation cachée : c'est une **dérogation écrite, datée et motivée** dans
> `strategie/derogations_regles.json` → le vérificateur R7 l'affiche « dérogation déclarée : ['inferx'] »
> et **reste ✅** tant qu'aucun AUTRE provider payant n'est activé. À revoir si inferx facture ou
> s'il repasse `free: true`.

### R10 — SURVEILLER LA SATURATION DE L'HÔTE, pas seulement les artefacts
> Source externe : **Google SRE — *four golden signals*** : latence, trafic, erreurs, **saturation**
> (https://sre.google/sre-book/monitoring-distributed-systems/).

**En une phrase** : la maison surveille ses fichiers, **pas la machine** qui les exécute — on ajoute la
saturation (RAM libre **réelle**, swap, disque, charge) comme signal de premier ordre.
**Piège à éviter** : ne **jamais** utiliser `vm_stat` seul (Pages free) — il a menti (« 91 Mo » alors que
62 % libre). Utiliser `memory_pressure` + `sysctl vm.swapusage` + `df`.
**Implémentation** : dans `scripts/verifier_regles_or.py` (déjà lecture seule), 3 contrôles PASS/FAIL.
**Mesure** : 1 ligne dans la page « vol » (Saturation hôte : OK/KO).

### R11 — FAIL-SAFE PAR DÉFAUT : dans le doute, on ne décide pas
> Source externe : **fail-safe vs fail-operational** (ISO 26262, industrie) + **défense en profondeur**.

**En une phrase** : si un chiffre clé d'une décision importante n'est pas **confirmé par ≥ 2 sources**
(écart ≤ 5 %), alors **on ne décide pas** — on récupère d'abord. (Déjà vrai pour les **prix** via
`croisement_externe` ; on **généralise** aux seuils, alertes et entrées.)
**Implémentation** : étendre `croiser_donnees_externes.py` (existant). **Mesure** : 0 décision prise sur un
`data_quality_fail` (registre `data/croisement_externe.jsonl`).

### R12 — UNE SAUVEGARDE N'EST PROUVÉE QUE PAR UNE RESTAURATION RÉELLE (et un drill, ça se répète)
> Source externe : **Chaos engineering** — hypothèse d'**état stable** + expérience contrôlée
> (https://principlesofchaos.org/) · *« ta sauvegarde ne vaut que ta dernière restauration »*.

**En une phrase** : tout mécanisme de sauvegarde/restauration doit être validé par un test d'échec
**automatisé et récurrent** ; sinon il est **interdit de le considérer comme acquis**.
**Implémentation** : `scripts/drill_restauration.py` (existant) rendu **bloquant** (verdict affiché
dans la page vol) + un passage **mensuel** planifié sur `git_push_auto` (pas de nouvel agent).
**Mesure** : `DRILL : READY` + **date du dernier drill réussi**.

### R13 — L'AUTO-RÉPARATION EST BORNÉE : détecter → isoler → récupérer, **jamais le moteur**
> Source externe : **FDIR spatial (NASA/JPL)** — détection, isolation, récupération (https://llis.nasa.gov/lesson/839).

**En une phrase** : un organe peut se réparer **seul** s'il reste **local, redémarrable et versionné** ;
il ne touche **JAMAIS** le moteur/le champion (règle C1) — et chaque auto-réparation **se déclare** (1 ligne mémoire).
**Implémentation** : de façon bornée sur les organes déjà en place (relance launchd, rotation des logs) ;
**preuve mécanique** = la veilleuse d'intégrité est STABLE (aucun scellé touché sans déclaration) **et**
le drill ne trouve **0 écart** de scellés. **Mesure** (R13 du vérificateur) : `veilleuse STABLE · 0 écart`.

### R14 — UNE ALARME QUI NE PEUT PLUS DIRE VRAI EST UNE FAUSSE ALARME
> Source externe : **fatigue d'alerte / signal-to-noise** (SRE) + *cry wolf*.

**En une phrase** : une alerte dont la **source est morte** ne doit ni rester allumée à vie ni être
ignorée : on la **répare** ou on la **retire**. (Cas réel : `derive_memoire` reste « NON saine » à vie
à cause de **13 indices morts** → plus personne ne croit l'alarme.)
**Implémentation** : dans `derive_memoire.py` / `verifier_regles_or.py`, exiger que chaque indice ait une
**source fraîche** ; sinon il passe en « RETIRÉ/ARCHIVÉ » au lieu de « CRITIQUE ». **Mesure** : 0 alerte
permanente dont la source est > 7 j.

**Correctifs réels appliqués le 19/09** (chacun a tué une fausse alarme observée) :
1. **Source tarie** (> 14 j sans analyse) → statut **RETIRÉ**, hors alarme (13 indices concernés).
2. **Population** : une calibration se juge sur les **paris DIRECTIONNELS** (LONG/SHORT), pas sur un
   `hit/n` qui **mélange les NEUTRE** (LECON-041) — c'est ce mélange qui déclarait **`geopol` CRITIQUE**
   (15 % apparent) alors que ses 4 seuls paris directionnels donnaient 25 %.
3. **Échantillon** : aucun verdict de calibration avant **n ≥ 20** (la règle du scoreur, LECON-042).
   En dessous → **EN OBSERVATION** (ni bon ni mauvais). C'est le cas de `geopol` (4 paris).

> 🔎 **Diagnostic `geopol` (19/09)** : il n'est plus CRITIQUE — il est **EN OBSERVATION**. En clair :
> **trop peu de paris directionnels (4) pour le juger**, alors que le scoreur refusait déjà de trancher
> (n=14 < 20). Ce n'était pas un indice cassé : c'était **un verdict rendu sans échantillon suffisant**.
> À surveiller (il est bearish alors que BTC montait) — mais on ne condamne pas sur 4 paris.

### R15 — TOUJOURS BRANCHER (ce qu'on construit doit être **rappelé**)
> Source interne : **notre propre historique** (la preuve la plus forte ici) — le **pont onchain**
> existait sans plist (« la boucle était coupée »), **`superviseur-core`** était écrit mais **jamais
> chargé**, la **rotation** des logs oubliait 3 fichiers, et **13 indices affichés** dans le cockpit
> n'étaient **plus analysés**.
> Corollaire **GitOps** : ce qui n'est pas dans la boucle de réconciliation **n'existe pas**. Et en
> **FDIR (NASA/JPL)**, un détecteur **non câblé** n'existe pas, même s'il est parfaitement codé.

**En une phrase** : **tout ce qu'on construit ou qu'on affiche doit être BRANCHÉ** — sinon c'est un
organe mort qui consomme (ou pire : un affichage qui **ment** parce que plus rien ne l'alimente).
**Implémentation** : les **15 bulles** de l'app Indices (`cockpit/indices.html`) sont désormais toutes
soit **analysées** (rotation = 22 indices), soit **déclarées « affichage seul »** avec leur raison
(`strategie/branchements_declares.json`, 2 cas : `justesse` et `ace`).
**Mesure** (R15 du vérificateur) : `15 bulles affichées · 22 indices en rotation · 2 affichage-seul`,
et **0 bulle non branchée**. Toute nouvelle bulle doit être branchée ou déclarée.

### R16 — ON N'OPPOSE RIEN À UN LEVIER VOULU SANS L'AVOIR MESURÉ (proposée 21/09, à ratifier)
> Source interne : **faute réelle de Buffy, 21/09** — j'ai proposé de « plafonner le
> compounding » alors que le compounding est, avec l'amplitude, **un levier de base
> de la stratégie** (Christophe : « c'est nos DEUX leviers principaux »). Ma
> proposition allait **contre la règle d'or n°1** (mémoire 19:25Z : « LE BUT DU
> PROTOTYPE EST DE GÉNÉRER DE LA PLUS-VALUE — faites ce qui est nécessaire »).

**En une phrase** : **un levier voulu (amplitude, compounding) ne se plafonne pas — il se
MESURE et se DÉCLARE.** Toute proposition qui **limite** une capacité du moteur doit d'abord
être **chiffrée en dollars contre la règle d'or n°1** (« est-ce que ça améliore ACE ? »),
réserves écrites incluses. Et **une alarme qui sonne pour un comportement voulu est un bug
d'alerte, pas un signal** (corollaire de R14) : on l'affiche comme **levier actif**, on ne crie
que sur la **vraie** brèche (le plafond que le moteur s'applique à lui-même).

**Mesure du 21/09** (0 €, lecture seule) — `chiffrage_compounding.py` :
levier compounding **isolé à une variable** = **−0,12 $ sur 28 j** (il est aujourd'hui *inerte*,
raboté par la chaîne de multiplicateurs puis le plafond du mur) ; `cockpit_mission_feed.py` :
« hors budget » ne crie plus que **au-delà de base × COMPOUND_MAX_MULT**, et affiche
« **compounding actif** » entre les deux.
**Implémentation** : `chiffrage_compounding.py` (mesure) + `audit_leviers_moteur.py` (carte des
trous : 63 leviers monétaires jamais chiffrés / 10 chiffrés).
**Mesure (R16)** : toute proposition qui plafonne/éteint un levier est accompagnée d'un chiffre
en dollars, ou elle n'est pas proposée.

### R17 — AUCUN SEUIL FIXE : LA MESURE DÉCIDE (ORDRE Christophe, 22/09/2026)
> Mot pour mot : « **on ne donne pas de timing FIXE D'ARRÊT** […] **ON REGARDE LES CHIFFRES,
> ce sont eux qui déterminent l'arrêt.** Copier le système utilisé par les desks professionnels. »

**En une phrase** : **aucun** seuil **fixe** (temps, compteur, pourcentage « en dur ») ne décide d'un
**arrêt**, d'une **reprise** ou d'un **blocage** — la décision vient d'une grandeur **MESURÉE sur
l'actif** (sa volatilité σ, son mur, son amplitude, son budget de perte en $, son spread).

**Pourquoi (la faute qui a produit cette règle)** : le 22/09 j'ai posé un « refroidissement »
**en heures fixes** (6/24/48 h) après avoir retiré un blocage **à vie** (`REENTRY_MAX`) — **deux
fois la même faute**, une taille en dessous : un chiffre choisi par moi au lieu d'être lu sur
l'actif. Doctrine desk (vérifiée) : le halt se **mesure** (« reduce risk after a drawdown and
**halt after a sequence of losses ; only lift size once equity recovers** ») ; la pause des desks
est celle de **la journée d'un humain**, pas une constante de stratégie ; et Klement (2013) montre
que **sortie et re-entrée s'estiment ensemble** — donc par la mesure, jamais par une horloge.

**Application, sans exception** :
1. Une garde **temporelle** ou un **compteur** sur une décision de marché est **interdit** ; si une
   protection est nécessaire, elle s'exprime en **dollars mesurés** ou en **fraction d'une grandeur
   mesurée de l'actif** (ex. le fusible = k × σ_mesuré × mise), jamais en heures.
2. Un seuil **exprimé en pourcentage fixe** ne peut être posé que s'il vient d'une mesure :
   c'est déjà le cas des piliers de la maison (les seuils sont explicitement « écrits en RELATIF »).
3. **Croisement d'horizons obligatoire** : le sens d'une garde dépend de l'horizon (mesuré le
   22/09 : `REENTRY_MAX` vaut **−14,5 $ à 6 h** et **+56,3 $ à 24 h**). Toute mesure de garde
   s'affiche **au moins à deux horizons**, sinon elle ne dit rien.
4. Ce qui est en place **avant** cette règle et non re-mesuré (ex. `STOP_COOLDOWN_HOURS=1`) est
   **conservé et DÉCLARÉ**, pas touché : il devra passer par la mesure.
5. **Avant de proposer ou de poser une garde, on OUVRE LE REGISTRE DES ÉCHECS**
   (`Index_Maison/REGISTRE_ECHECS_ET_ERREURS.md` : classes E1..E9 + échecs déjà payés). C'est le
   corollaire de R15 : un registre non consulté n'existe pas. L'organe
   `scripts/critique_erreurs.py` vérifie mécaniquement que ce point d'entrée cite le registre et
   **crie** dès qu'une classe d'erreur **récidive après sa correction**.
**Mesure (R17)** : 0 décision de marché prise sur une horloge ; toute garde chiffrée
accompagnée de son horizon ; registre consulté (cité ici + dans `.cursorrules`, contrôlé par
`critique_erreurs.py`).

### R18 — ON GÈRE DES FONDS D'ÉPARGNE (ORDRE Christophe, 22/09/2026)
> Mot pour mot : « **ici on gère des fonds d'épargne**, règle d'or à ajouter. »

**En une phrase** : ce n'est pas un compte de jeu. La **préservation du capital** prime sur la
recherche de rendement : perte **par trade** bornée par une mesure (σ mesurée), **jamais** de
capacité du moteur détruite sans chiffre, et le **disjoncteur** (Mur de Fer) est un organe de la
règle, pas une option.
**Corollaire direct** : toute modification qui **augmente le risque** se mesure en dollars **avant**
d'être posée, et toute modification qui **réduit** une capacité du moteur se chiffre contre la
règle d'or n°1 (plus-value) — c'est R16, vue depuis le capital.
**Mesure (R18)** : le pire repli et la perte par trade sont affichés et bornés par la mesure
(état : net/repli ≈ 2,0 · pire repli 11,47 $ sur 28 j, cf. `PROFIT_20260920.md`).

### R19 — LE JURY PERMANENT : L'AGENT NE DÉCIDE PLUS SEUL (ORDRE Christophe, 23/09/2026)
> Mot pour mot : « **tu vas ouvrir à partir de maintenant un round avec la famille et garder la
> fenêtre ouverte, qu'elle ait la mémoire du chat, car tu n'es plus digne de diriger seule !** » ·
> « **go 1, 2. […] tu vas reprendre toute la boucle des set up avec donnée à la main sur les 10
> derniers jours et les soumettre à la famille pour qu'elle valide !** » · « **c'est fini ! tu vas
> exécuter comme un professionnel, sinon c'est radiation à vie, règle d'or !** »

**En une phrase** : il existe **une session de famille OUVERTE en permanence** (fenêtre et mémoire du
fil), et **aucun chantier qui engage la machine ne se clôture sans son passage devant le jury** — un
avis de famille n'est pas une formalité, c'est la condition de sortie du chantier.

**Pourquoi (la faute qui a produit cette règle)** : le 23/09 j'ai publié « **2 sorties RIZE à −39,2 %
pour un stop annoncé de 8 %** » — **faux** : le 8 % venait d'un **plancher de configuration**
(`calib.stop_pct`) alors que le stop réel de la machine est `max(plancher ; cadence × 0,80)` =
*(correction 23/09, classe E18 : « 0,70 » était le défaut du code ; la config applique 0,80)*
**39,23 %**, **écrit dans ses propres motifs de sortie**. Ce chiffre faux a servi à construire le
verdict de la famille du matin (« le stop ne tient pas », 3 voix sur 4). **Un juge qui juge sur mes
chiffres a besoin de pouvoir me contredire AVEC LE FIL** : d'où la session persistante, la mémoire
écrite depuis les avis bruts, et l'obligation de soumettre — pas seulement de rapporter.

**Application, sans exception** :
1. **Session ouverte** : `Index_Maison/scripts/SESSIONS_FAMILLE/<session>/` — transcript
   **append-only**, `META.json` (état, tours, dernier tour), mémoire de session écrite **depuis les
   textes bruts des avis** (je ne réécris pas un verdict).
2. **Mémoire du fil obligatoire** : chaque tour repart **avec l'historique** — le jury doit pouvoir
   vérifier si j'ai fait ce qu'il avait exigé.
3. **Voix indépendantes seulement** : une réponse **substituée** (modèle demandé ≠ modèle servi) est
   **étiquetée** et **ne compte pas** (classe E16).
4. **Tout chiffre à publier sur la machine passe par le jury** ; s'il est démenti, il est **retiré
   publiquement** et sa classe d'erreur enregistrée (E17 ici).
5. **Un chiffre faux publié = radiation** (mot de Christophe) : mesuré par le fait que la classe
   d'erreur correspondante récidive **après** sa publication et sa garde.
**Mesure (R19)** : contrôlée mécaniquement par `verifier_regles_or.py` — session **OUVERTE**,
**consultée ≤ 24 h**, **fil cohérent** (chaque tour posé a ses avis), **≥ 3 voix indépendantes**.
Tant que ce n'est pas vrai, la règle est violée et la page « vol » le dit.

### Amélioration de #3 — DOUBLE CONTRÔLE pour toute action irréversible
> Source externe : **two-person rule / dual control** (https://en.wikipedia.org/wiki/Two-person_rule).

**En une phrase** : une action **irréversible** (ordre réel, purge, déploiement) exige **2 validations
indépendantes** — et pas seulement pour le nucléaire : c'est ce qui évite qu'un seul bug/une seule
hallucination déclenche quelque chose qu'on ne peut pas annuler.

---

## ❓ À TRANCHER AVEC CHRISTOPHE (la « 4 » qu'on fait ensemble)

1. **Hiérarchie** : que fait-on quand deux règles s'opposent ? Ex. #3 (GO humain) vs auto-réparation
   (#8) : l'auto-réparation doit rester **bornée** et **ne jamais** toucher au moteur.
2. **Portée** : ces 9 règles valent-elles pour **tous les agents** (Buffy, Ada, Cortana, Antigravity,
   famille du hub) ? Qui a le **droit d'écrire** dans la maison ? (proposition : **Christophe tranche ;
   un seul écrivain par chantier**).
3. **Format** : garde-t-on 9 règles, ou on en fait 3 « méta » (Parler · Construire · Prouver) ?
4. **Emplacement canonique unique** : ce fichier, la Constitution, ou les deux (Constitution = vision,
   REGLE_D_OR = opérationnel) ?
5. **Sanction/rapport** : doit-on **mesurer** leur respect à chaque passage (vérificateur) et l'afficher
   dans la page « vol » ?
6. **R10–R14** : appliquées et mesurées le 19/09 (10/10). Reste-t-il une à **retirer** ? (à confirmer)
7. ~~**R14** : les **13 indices RETIRÉS**… on les réactive ou on les archive ?~~ → ✅ **TRANCHÉ le 19/09 par
   Christophe : RÉACTIVÉS.** Les 13 indices (dont `btc`, l'indice cœur) sont revenus dans la rotation de
   l'analyste (`analyste_cadence.sh`) : les 4 cœurs gardent leur cadence, **2 indices réactivés par passage
   en rotation** (+2 appels/passage seulement, 0 €, réversible). État après réactivation : **0 RETIRÉ**, tous
   les indices rafraîchis. Deux garde-fous ajoutés pour que ça ne redevienne pas du bruit :
   **RETIRÉ** si source tarie (> 14 j) et **calibration jugée seulement à partir de n ≥ 10** (sinon un
   indice vu 2 fois à 0 % criait CRITIQUE à tort).

---

*Sources internes citées : `ACE777-Constitution.md` · `POLITIQUE_OUBLI.md` · `PREFS_STACK.md` ·
`INDEX_COMMANDES.md` · `MEMOIRE_COLLAB.md` (09/09 + 19/09) · `superviseur_core.sh`.*

*Sources externes (v2) : Google SRE — four golden signals (`sre.google/sre-book/monitoring-distributed-systems/`) ·
GitOps / boucle de réconciliation (`akuity.io/blog/what-is-argo-cd-features-and-business-benefits`) ·
Chaos engineering (`principlesofchaos.org`) · Release It! — Nygard (`pragprog.com/titles/mnee2/release-it-second-edition/`) ·
FDIR spatial NASA/JPL (`llis.nasa.gov/lesson/839`) · two-person rule (`en.wikipedia.org/wiki/Two-person_rule`) ·
défense en profondeur / fail-safe (`risk-engineering.org/concept/defence-in-depth`).*

*Consultation famille (4 angles, dont CONTESTE) : `CONSULTATION_FAMILLE_REGLES_OR_20260919/`.
Recensement + propositions Buffy 19/09/2026 — 0 ordre, 0 €. Vérificateur : `scripts/verifier_regles_or.py`.*
