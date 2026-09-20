# 🔬 LES PROTOCOLES EN TEST — RÉSULTATS EN PROFONDE (20/09/2026)

*Buffy, GO Christophe « me donner les résultats en profondeur des protocoles en test — verdicts, vulgariser,
et ce que ça nous apporte ». Tous les chiffres ci-dessous sont **mesurés à la source**, pas recopiés :
ils sortent de `scripts/verdicts_protocoles.py` (scellé au registre) et sont lisibles en machine dans
`thermo/PROTOCOLES_VERDICTS.json`. La page vol lit ce fichier — plus le tableau du 14/09.*

---

## 1. Le tableau de bord, en une ligne par protocole

| Protocole | Son critère (fixé AVANT les données) | Ce qu'on a mesuré | Verdict |
|---|---|---|---|
| **TROUPEAU-INV** | juger à T+72h la direction réelle du BTC · verdict le 08/11 si ≥ 55 % sur ≥ 20 cas | 11 paires · 1 seule divergente · 1 jugée : **MISS** | ⏳ **en attente** — et **inatteignable tel quel** : 1 divergence/semaine ⇒ ~8 cas au 08/11 |
| **Radar RWA (DefiLlama)** | J+8 : ≥ 3 pools du top 20 TVL bougent de ≥ 50 bps en 7 jours | 12 041 relevés · 369 pools · **0 bouge de ≥ 50 bps** (max : 35) | 🔴 **ÉCHEC** — et **critère mal ciblé** : 9 des 20 pools sont du lending Solana à ~0 % |
| **Radar XRPL gouvernance** | J+8 : ≥ 5 amendements bougent de ≥ 2 votes, OU ≥ 1 activation, OU ≥ 1 mort | 160 relevés · 112 amendements · **4 bougent de ≥ 2** · 0 activation · 0 mort | 🔴 **ÉCHEC** — le radar VOIT, c'est le seuil (8 jours) qui est hors d'échelle |
| **Arbitrage LLM-vs-règle** | justesse micro < 60 % ⇒ confiance faible · verdict annoncé le 27/09 | **0 alerte produite en 7 jours** ⇒ 0 cas à juger | ⛔ **IMPOSSIBLE** — le verdict du 27/09 ne pourra pas être rendu |
| **Geopol (réanimé)** | avis noté 2×/jour vs BTC · fenêtre 4 semaines (→ ~10/10) · critère ≥ 56 % | 17 avis : **13 NEUTRE**, 4 directionnels, **1 correct** | ⏳ **en attente** — à cette cadence le critère ne sera pas tranchable |
| **paternes-btc (Kronos)** | verdict à n ≥ 30 cycles | **9 cycles** (11 → 20/09) | ⏳ **en attente** — ~21 jours de collecte |
| **MiroFish** | simulateur multi-agents, à la demande · 08/08 jugée MISS | **2 simulations**, 1 rapport · aucun run depuis le **10/08** | ⏳ **en attente** — « réveillé le 13/09 » n'a produit aucun run |

**Ce que la machine ne dit pas d'elle-même — et qu'elle dit maintenant** : sur 7 protocoles, **2 verdicts
seulement** ont pu être rendus à la date dite. Les 5 autres n'étaient pas « en cours, tout va bien » : ils
étaient **mal câblés** (1), **mal ciblés** (1), **sans matière** (1) ou **sans échéance atteignable** (2).
Aucune page ne le disait. C'est désormais affiché par un ⚠ à côté du verdict.

---

## 2. Protocole par protocole — le fait, puis la traduction

### 2.1 TROUPEAU-INV — « le troupeau a-t-il tort quand il diverge ? »

**Le protocole (en clair).** On demande à deux « agents » de donner leur direction sur le BTC à partir de la
même graine d'actualité. Le plus souvent les deux sont d'accord. Quand ils **divergent** (l'un dit haut,
l'autre dit bas), c'est l'**intérêt du cas** : on parie que le minoritaire a raison, puis on regarde, 72 heures
plus tard, ce que le marché a réellement fait. Le verdict final est fixé d'avance : le **08/11/2026**, sur
**≥ 20 cas divergents**, avec un seuil de **55 %** de réussite — sinon le dossier est fermé définitivement.

**Les faits mesurés.**
- 11 lignes d'historique : 3 paires de **calibration** (sur la graine du 08/08) + 8 vraies paires (`paire-003` → `paire-010`).
- **Une seule divergence** : `paire-008`, graine du **14/09 04:00Z**.
- 3 paires annulées à la naissance (« miroir instable ») : le vote n'était pas exploitable.
- `paire-008` devait être jugée le **17/09 à 04:00** (T+72h). Elle ne l'avait **jamais été** : le plist ne lançait
  que `--cycle`, jamais `--juger`. **Réparé et jugée le 20/09 : MISS** — le minoritaire disait « haut », le BTC
  a fait **bas** (graine 77 520,46 $ → 76 355,06 $ à T+72h, soit −1,50 %).

**Traduction.** Le seul cas qu'on ait jamais eu à juger s'est soldé par une erreur. **1 cas ne prouve rien**
(ce n'est pas un échec du concept, c'est un échantillon de 1) — mais il dit déjà à quoi ressemble le risque :
quand le petit désaccord apparaît, ce n'est pas forcément lui qui a raison.

**Ce que ça nous apporte.**
1. Un **chiffre honnête** au lieu d'un tableau : 1 cas jugé, 0 % de réussite — à ne surtout pas lire comme un
   verdict.
2. **La découverte la plus utile est arithmétique** : avec **1 divergence par semaine**, on aura ~**8 cas** au
   08/11, pas 20. Autrement dit, le contrat du 08/11 était **impossible à honorer** et le protocole se serait
   *auto-fermé* (« dossier fermé définitivement ») sans avoir jamais été testé. Il faut soit élargir la fenêtre
   (compter en mois, pas en cas), soit augmenter la cadence (plus d'agents, plus de paires), soit abaisser le
   seuil de cas. **Décision à prendre, elle t'appartient.**
3. La réparation vaut pour tous les protocoles : **un critère sans jugement automatique est un critère mort**.

### 2.2 Radar RWA (DefiLlama) — « les rendements du crédit privé tokenisé bougent-ils ? »

**Le protocole (en clair).** On note, toutes les 6 heures, tous les rendements (« APY ») des pools de la
finance privée tokenisée. Aucune alarme, aucun ordre : on veut juste savoir si ces rendements **travaillent**
(les opportunités apparaissent et disparaissent) ou s'ils sont **plats** (rien à arbitrer). Le critère, fixé
d'avance : au **8ᵉ jour**, au moins **3 des 20 plus gros pools** doivent avoir bougé de **≥ 50 points de base**
(0,50 %) sur 7 jours.

**Les faits mesurés.** 12 041 relevés, **369 pools** suivis, dernier relevé le 20/09 16:55Z (le radar tourne
impeccablement). Sur les 20 plus gros par TVL au premier relevé du 11/09 : **0 pool** a bougé de ≥ 50 bps.
Le plus gros mouvement : **−35 bps** (les pools Centrifuge USAT/USDC). Les plus gros (« maple USDC », 2,65 Md$)
n'ont bougé que de **+1 bp**. Et surtout : **9 des 20** sont des pools de lending Solana (DSOL, JITOSOL, JLP,
ONYC…) à **~0 % de rendement** — ce ne sont pas des rendements de crédit privé, ce sont des prêteurs/« LST ».

**Traduction.** D'abord le fait : sur la semaine mesurée, **les rendements du crédit privé tokenisé étaient
quasi immobiles** (≤ 35 bps). Pour la maison, c'est une **information de marché utile** : il n'y a pas de
« chasse au rendement » à mener en ce moment sur ce segment. Ensuite le défaut : le critère a été écrit sur
« les 20 plus gros pools », mais la moitié de cette liste n'est pas de la matière à rendement — donc **le test
ne testait pas ce qu'on croyait tester**.

**Ce que ça nous apporte.**
1. Un verdict **rendu et daté** : **ÉCHEC**, avec la raison exacte (0/20 ≥ 50 bps).
2. **La conclusion de fond** : ce radar n'a pas à devenir une usine à signaux — sa valeur est d'être une
   **mesure de tendance lente**. On sait maintenant qu'un mouvement de 50 bps en 7 jours ne se produit pas
   sur ce segment : le seuil est à revoir (ou à abaisser à ~20 bps si l'intérêt est de détecter les débuts
   de tension).
3. **Décision** : reformuler le critère sur les pools **portant un vrai rendement** (filtre APY > 0,5 %), et
   décider si le radar continue en **passif assumé** (aucun signal, juste un thermomètre) — c'est mon avis :
   un thermomètre honnête vaut mieux qu'un détecteur qui ne sonne jamais.

### 2.3 Radar XRPL gouvernance — « un amendement est-il en train de passer ? »

**Le protocole (en clair).** XRPL (la blockchain du XRP) fait évoluer son code par **amendements** votés par
les validateurs. Un amendement qui franchit son seuil de votes s'**active** et change le réseau. Le radar
compte, une fois par jour, combien de votes chaque amendement a. Le critère J+8 : soit **≥ 5 amendements**
bougent de **≥ 2 votes**, soit **≥ 1 activation**, soit **≥ 1 amendement mort** — sinon c'est un échec.

**Les faits mesurés.** 160 snapshots du **13/09 au 20/09**, 112 amendements suivis. Dans la fenêtre :
- **(a) 4 amendements** ont bougé de ≥ 2 votes : `PermissionDelegationV1_1` **+8**, `DynamicMPT` +4,
  `BatchV1_1` +4, `ConfidentialTransfer` +4. Il en fallait 5.
- **(b) 0 activation** · **(c) 0 mort** · 2 amendements **nouveaux** apparus (`LendingProtocolV1_1`, `fixCleanup3_4_0`).
- Le cimetière du radar est stable (Batch → remplacé par BatchV1_1, etc. : événements **antérieurs** à la fenêtre).

**Traduction.** Le radar **voit très bien** : il a repéré que 4 amendements avancent, dont un
(`PermissionDelegationV1_1`) qui a pris **8 votes en 8 jours** — c'est un vrai mouvement de gouvernance, celui
à suivre. Mais le critère demandait « 5 » ou une activation : verdict **ÉCHEC tel qu'écrit**. Or sur XRPL un
amendement vit **des mois** ; exiger une activation en 8 jours, c'est exiger la fin d'un match 8 minutes après
le coup d'envoi.

**Ce que ça nous apporte.**
1. **Un veilleur fiable** sur un écosystème où les changements de règle précèdent les mouvements de prix
   (`PermissionDelegation`, `SingleAssetVault`, `LendingProtocol` = de la **capacité de prêt** sur XRP : si ça
   s'active, le XRP devient une plateforme de crédit on-chain — ce n'est pas un détail).
2. **La bonne mesure existe** (le compte de votes par amendement), c'est le **seuil** qui est faux. Recommandation :
   J+30 au lieu de J+8, et compter les **tendances** (votes gagnés par semaine) plutôt que des paliers.
3. **Rien à décider côté risque** : 0 activation → aucun changement de réseau à anticiper cette semaine.

### 2.4 Arbitrage LLM-vs-règle (Cortana) — « l'IA fait-elle mieux que la règle écrite ? »

**Le protocole (en clair).** La maison a une **règle mécanique** sur les signaux de microstructure (« si la
justesse descend sous 60 %, alors confiance faible »). Le protocole demande : **Cortana (l'IA) fait-elle mieux
que cette règle ?** Pour le savoir, il faut des alertes microstructure à noter : chacune est confrontée au réel
par un juge indépendant (prix public, jamais l'instrument qui a alerté). Verdict annoncé : **27/09**.

**Les faits mesurés.** `data/micro_alerts.jsonl` = **0 octet depuis le 09/09** : **aucune alerte n'a été
produite en 7 jours**. Donc : 0 alerte notée, `pct: null`. Le producteur d'alertes (module
`cortana_microstructure`) n'a rien écrit — le juge, lui, tourne toutes les 15 s pour rien.
En revanche, la mesure **utile** existe ailleurs et elle est vivante : le scoreur maison
(`scripts/justesse_v2.json`) note toutes les opinions de Cortana contre le réel → **202 avis notés**,
**87 directionnels**, **54,0 % de réussite** (43,1 % si on compte les NEUTRE), seuil maison **56 %**.

**Traduction.** Le protocole tel qu'il est écrit **ne peut pas répondre** : on ne peut pas arbitrer « IA contre
règle » sans un seul cas d'alerte. Ce n'est pas une patience, c'est un robinet fermé. Et sur la question de
fond — l'IA bat-elle la règle ? — le seul chiffre disponible dit : **54 %**, soit **2 points sous le seuil
maison**. C'est honnêtement « pas mieux que la règle », sur un échantillon encore petit.

**Ce que ça nous apporte.**
1. **Une décision à prendre** : soit le module microstructure est **mort** (et il faut le réparer ou le débrancher
   proprement), soit il n'y a simplement **rien à alerter** — mais dans ce cas, l'échéance du 27/09 doit être
   remplacée par « verdict quand ≥ 30 alertes », sinon on jugera le vide.
2. **Le bon indicateur existe déjà** : `justesse_v2` (54 % directionnel sur 87 avis) est la vraie note de
   l'IA de la maison. C'est **lui** qu'il faut surveiller — et il dit de **ne pas encore donner de poids
   directionnel aux avis de Cortana** (contexte oui, signal non).
3. Rappel de méthode : un protocole dont le matériel ne se produit pas **doit crier**, pas attendre. C'est
   maintenant le cas (⚠ dans la page vol).

### 2.5 Geopol (réanimé) — « le contexte mondial aide-t-il à prévoir le BTC ? »

**Le protocole (en clair).** Cinq capteurs (aviation militaire, activité portuaire, prix du pétrole,
sentiment des nouvelles…) fabriquent un **score géopolitique** de 0 à 1 (calme → crise). Ce score n'est pas
un signal d'achat/vente : c'est un **contexte**. Le protocole teste une question précise : **quand Cortana
donne un avis directionnel « à cause » de ce contexte, a-t-elle raison ?** Critère : sur 4 semaines
(≈ 10/10), **≥ 56 %** de justesse.

**Les faits mesurés.** Score actuel **0,3495 « calme »** (modèle ML : 54 % de probabilité « calme », 42 %
« attention »). Sur **17 avis** enregistrés : **13 NEUTRE** (« je ne me prononce pas »), **4 directionnels**,
et **1 seul correct** (25 %), avec un `t_stat` de **−2,18** (statistiquement défavorable).

**Traduction.** Le capteur vit, il est branché dans le contexte de Cortana (c'était l'objet du chantier du
12/09), et le monde est **calme** aujourd'hui. Mais **quand il ose une direction, il s'est trompé 3 fois sur 4**.
Nuance importante : 4 cas, c'est minuscule — sauf que le signal va dans le mauvais sens avec une ampleur
suffisante pour mériter attention, et que **13 NEUTRE** signifient que le capteur n'aide presque jamais à
trancher.

**Ce que ça nous apporte.**
1. **Usage à figer** : geopol = **contexte** (et c'est déjà son rôle officiel), **jamais** un déclencheur.
   Tant que la mesure reste à 1/4, lui donner un poids directionnel serait se raconter une histoire.
2. Un **critère de sortie clair** : si au ~10/10 la justesse directionnelle reste sous ~50 %, le chantier
   se conclut « contexte oui, signal non » — et on ne le rouvre plus sans une nouvelle raison mesurée.
3. Rien à faire d'urgence : le capteur est propre (5/5 modules, frais), il ne crie pas, il informe.

### 2.6 paternes-btc (Kronos) — « où en est le cycle du BTC ? »

**Le protocole (en clair).** On mesure en continu quatre repères validés par le corpus de leçons :
le croisement des moyennes **50 et 200 semaines** (régime de fond), le **RSI hebdomadaire** (chaleur du
marché), le **MACD quotidien** (filtre, jamais déclencheur) et le **contexte de cycle** (halving → sommet,
~4 ans). Ce n'est pas un signal : c'est un **tableau de bord de régime**. Verdict prévu à **≥ 30 cycles**.

**Les faits mesurés (9 cycles, 11 → 20/09).**
- Régime **HAUSSIER** constant : prix **19,8 % au-dessus** des 200 semaines (SMA200w ≈ 65 600 $).
- **RSI hebdo 67,8** : chaud, sans être en zone d'euphorie extrême.
- **MACD quotidien : histogramme −679 → −167** sur la période (il a touché −785 le 17/09) — encore **négatif**,
  mais il revient **vite** vers zéro : un croisement haussier se rapproche.
- Prix : **76 540 $ → 81 257 $ (+6,2 %)** sur les 9 jours ; chute à 75 609 $ le 17/09, puis reprise.
- Dernier croisement SMA : **05/09, baissier**, il y a 15 jours.

**Traduction.** En clair : **la tendance longue reste haussière** (prix loin au-dessus des 200 semaines),
le marché est **chaud mais pas en surchauffe** (RSI ~68), et le filtre quotidien est **en train de se
retourner** — c'est exactement la zone où l'on ne prend pas de décision brusque. La chute du 17/09 a été
absorbée en deux jours : le régime n'a pas changé.

**Ce que ça nous apporte.**
1. Un **contexte de décision** stable et vérifiable (utilisable par HULK/ACE sans interprétation
   personnelle) : haussier long, chaud court, filtre en transition.
2. **La discipline est tenue** : 9 cycles sur 9, aucun trou, aucun figement (anti-figage OK) — le protocole
   *mesure* vraiment. Il lui manque juste du temps : ~**21 jours** pour le verdict à 30 cycles.
3. Point de méthode : le MACD est noté comme **filtre**, pas déclencheur (LECON-035) — le tableau de bord
   respecte sa propre doctrine, c'est notable.

### 2.7 MiroFish — « et si on faisait parler 4 agents avant de décider ? »

**Le protocole (en clair).** Un simulateur de **marché artificiel** : 4 agents (Lucas, Sophie, Marc, Amina)
avec des profils et des positions différentes réagissent à un scénario (ex. « la Fed baisse ses taux de
75 pb »), on lit leurs ordres et l'évolution de leur sentiment. But : **préparer** une réaction, pas prédire
un prix. Fonctionnement **à la demande**. Le 08/08, une simulation a été jugée **MISS**.

**Les faits mesurés.** 2 simulations, 1 rapport complet (`report_fed_btc`), dernier run le **10/08/2026**.
Aucune nouvelle simulation depuis. Le « réveil du 13/09 » n'a produit **aucun run**.

**Traduction.** L'outil est **intact mais endormi** : rien à juger, et surtout rien à en attendre tant qu'on
ne le relance pas explicitement. C'est un outil « à la demande » : il ne se réveille pas tout seul, il
s'exécute quand on le lance.

**Ce que ça nous apporte.**
1. La fin d'une ambiguïté : **« réveillé » ≠ « utilisé »**. Aucune donnée nouvelle n'existe.
2. Un usage réaliste : un run MiroFish coûte du temps et des tokens — sa place est **avant une décision qui
   engage** (un scénario macro, une grosse liquidation), pas en routine. À garder au congélateur jusqu'à
   ce qu'un scénario le justifie.

---

## 3. Ce que cette revue nous apprend au-delà des 7 protocoles

1. **Un protocole sans verdict calculable est un protocole mort.** 4 sur 7 étaient dans ce cas (jugement
   jamais exécuté, 0 cas à juger, seuil hors d'échelle, aucun run). Aucun gardien ne le voyait : le chien
   surveille les **organes**, pas les **protocoles**. C'est désormais mesuré (`verdicts_protocoles.py` +
   ⚠ dans la page vol + cri possible).
2. **« En test » n'est pas un état permanent.** Chaque protocole a un critère **pré-enregistré** — c'est
   précisément ce qui rend le verdict honnête. Il faut donc une **date de jugement** et une **sortie** :
   succès → on industrialise ; échec → on ferme sans regret. Trois protocoles ont besoin d'une décision
   de ta part (voir §4).
3. **Les critères doivent être écrits sur la matière mesurée**, pas sur une intuition de liste :
   « top 20 TVL » (moitié de lending à 0 %), « ≥ 5 amendements en 8 jours » (une gouvernance vit des mois),
   « ≥ 20 cas au 08/11 » (1 cas/semaine mesuré). Trois critères, trois fois le même piège.
4. **Le module d'arbitrage IA-vs-règle existe déjà sous une autre forme** et fonctionne : `justesse_v2`
   (54 % directionnel sur 87 avis, seuil 56 %). C'est cette mesure qu'il faut regarder — pas un compteur
   d'alertes resté à zéro.

## 4. Les décisions qui t'attendent (aucune appliquée sans ton GO)

| Sujet | Question | Mon avis |
|---|---|---|
| **TROUPEAU-INV** | Fenêtre du verdict : garder le 08/11 (≈ 8 cas) et solder, ou passer à « ≥ 20 cas, sans date » (~5 mois), ou augmenter la cadence ? | Option 2 (le critère reste honnête, la date disparaît ; on ne juge pas 8 cas) |
| **Arbitrage LLM-vs-règle** | Le module microstructure est-il mort, ou n'y a-t-il rien à alerter ? Remplacer l'échéance du 27/09 par « ≥ 30 alertes » ? | Diagnostiquer le producteur ; remplacer la date par un compte de cas |
| **Radar RWA** | Reformuler le critère (pools à rendement réel) ou le passer en **thermomètre passif assumé** ? | Thermomètre passif : il mesure une tendance lente, ce n'est pas un détecteur |
| **Radar XRPL** | Décaler le critère à J+30 et compter les **votes gagnés/semaine** ? | Oui — le radar voit juste, c'est le seuil qui est faux |
| **48 organes jugés sur leur seule sortie launchd** | Câbler un produit pour ceux qui comptent, ou déclarer « produit à la demande » ? | Lister les 10 qui comptent vraiment et les déclarer un par un |
| **Chaque protocole** | Ajouter une **date de sortie** écrite noir sur blanc (« si pas concluant à J+X, on ferme ») ? | Oui — c'est ce qui évite les protocoles éternels |

---

*Fichiers liés : `thermo/PROTOCOLES_VERDICTS.json` (les verdicts en machine) · `thermo/REVUE_ORGANES.md`
(les 99 organes) · `INCIDENTS.md` (les 11 RCA du 20/09) · `JOURNAL_ERREURS_TEST.md` (statuts) ·
`data/lecons_analyste.jsonl` (LECON-052 → 058) · `MEMOIRE_COLLAB.md` (20/09).*
