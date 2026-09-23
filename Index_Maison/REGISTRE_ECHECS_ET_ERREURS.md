# REGISTRE DES ÉCHECS ET DES ERREURS — la pièce qui manquait

> 2026-09-22 · Buffy · créé sur ordre de Christophe : « va voir ce que sont nos erreurs, enfin
> **tes** erreurs, et comment les corriger une bonne fois pour toute. »
> **Dernière mise à jour : 2026-09-23T0956Z** — c'est la borne du détecteur de récidive : toute
> ligne de mémoire **postérieure** qui retombe dans une classe connue est signalée par
> `scripts/critique_erreurs.py` (organe branché, cf. R15).
> **0 €, 0 ordre.** Ce fichier est la première version de la pièce que la recherche désigne comme
> **la seule qui manque** à une machine de trading auto-améliorante (voir §1).

---

## 1. Pourquoi ce fichier existe (et pourquoi c'est LA pièce manquante)

Source : *« The self-improving AI trading machine is mostly built. One piece left »*
(grokbot.sh, 2026 ; repris par @antpalkin). Le cycle que tourne tout desk quant a **six parties** :

| Partie | État | Ce qu'ACE777 a déjà |
|---|---|---|
| 1. **Research** | résolu | veille + sniffer + hub (10 providers gratuits) |
| 2. **Code** | résolu | Buffy/Cursor/codeur |
| 3. **Backtest** | résolu | replay, Monte-Carlo, pré-enregistrement des critères |
| 4. **Live** | résolu | Hulk paper + kill switch **dans le code** (disjoncteur, STOP_ALL) |
| 5. **Post-mortem** | résolu | MEMOIRE_COLLAB, journaux, attributions, contrôles de fidélité |
| 6. **Fine-tune** | ❌ **LA PIÈCE MANQUANTE** | **rien** |

**Ce que l'article dit exactement** : « Right now the lesson from a losing trade lands in a log file
and stays there. The next strategy the agent writes does not know about it. […] **Negative results
are the most undervalued asset in quant research, and no system currently keeps them.** »
→ Sans ce registre, **chaque cycle repart de zéro et re-teste ce qui a déjà échoué.**
C'est **littéralement** ce qui se passe ici : on redécouvre les mêmes erreurs tous les jours.

**Deux autres règles d'or que l'article valide et que la maison applique déjà (à garder)** :
- *« write down the expected outcome before the test runs, store it immutably, then compare »*
  → c'est notre **pré-enregistrement** ; il n'est pas négociable.
- *« the kill switch lives in code, never in the system prompt »* → notre disjoncteur est du code.

---

## 2. Mes erreurs récurrentes (les miennes, nommées) + la garde qui les tue

| # | Erreur (classe) | Cas réels | Garde mécanique (pas une promesse) |
|---|---|---|---|
| **E1** | **Inventer un seuil** au lieu de lire l'actif | refroidissement **6/24/48 h** posé le 22/09 ; « plafonner le compounding » sans chiffre (21/09) | **R17** : aucun seuil fixe ; chaque garde doit **afficher sa provenance mesurée** ; croisement **2 horizons** obligatoire |
| **E2** | **Conclure sans vérifier à la source** | « positions perdues » ; « veilleuse STABLE » alors que `$?` mesurait `tail` ; « 57 % des refus = volume » ; « 9 paires tier B » | **Contrôle de fidélité obligatoire** (reconstruire et comparer au journal) + lire la source canonique, jamais une copie |
| **E3** | **Instrument qui pointe la mauvaise source** | `chiffrage_gardes_refus.py` lisait des journaux **écrits en dur** → aveugle depuis 21/09 13:22Z | Tout instrument **déclare sa source et sa fraîcheur** ; interdiction des listes de fichiers en dur (le pointeur est la vérité) |
| **E4** | **Bloquer / interdire au lieu de mesurer** | `REENTRY_MAX` = paire interdite **à vie** (CCUSDT 4,5 jours) | Aucune interdiction sans **condition de sortie exprimée en grandeur mesurée** |
| **E5** | **Deux vérités pour un même fait** | compteur `reentry_count` en mémoire **non persisté** (2 comportements selon redémarrage) ; `STOP_COOLDOWN_HOURS` déclaré 2× ; double comptage du journal en `--resume` | **Une seule source persistée par fait** + le **contrôleur de config** + le **contrôle de fidélité** |
| **E6** | **Silence** : décider sans écrire | régime `WATCH` = `return` muet → CCUSDT **invisible 27 h** | **Anti-silence** (fait le 22/09) : tout refus écrit au moins 1×/h/paire |
| **E7** | **Corriger un symptôme, pas la cause** | réparer les instruments pendant que le prototype ne produit pas (20/09) | Une correction doit **nommer la classe d'erreur** (ce tableau) et **tuer la classe**, pas le cas |
| **E8** | **Cacher les limites** | mesures présentées sans leurs bornes (n faible, horizon, borne supérieure) | **Réserves écrites obligatoires** dans chaque livrable |
| **E9** | **Empiler les corrections le même jour** | 22/09 : poser un refroidissement puis le retirer 2 h plus tard | Une garde ne se pose **qu'après** un chiffrage écrit ; sinon elle attend le GO |
| **E10** | **Prendre un chiffre RECALCULÉ pour un chiffre VÉRIFIÉ** | 20-23/09 : seuil d'entrée annoncé à **5-12,75 %** pendant trois jours alors que le moteur appliquait **21,70 %** (terme manquant : `dip = max(dip_pct ; 0,50 × cadence)`, cadence ÉCRITE par le moteur colonne 9). Le chiffre faux a servi à publier « RIZE structurellement inattaquable », à chiffrer un levier d'entrée et à orienter un scan → **cause racine d'un second instrument défectueux** (`chiffrage_entree_sortie_replay.py`, 3 calculs) qui avait produit les chiffres du câblage `IMPULSE_SANS_REPLI_ON` sur EDEL | **`hulk-mexc/scripts/verif_seuil_moteur.py`** (23/09) : confronte le seuil RECALCULÉ aux chiffres que le moteur ÉCRIT (refus parlants + cadence), nomme le terme qui décide (R15), **détecte par texte** tout instrument qui recalcule un seuil sans la cadence, et **s'autoteste (7/7 erreurs discriminantes détectées sur 3 régimes)**. Branché toutes les 3 h + **affiché au cockpit** (« Garde-fou seuil moteur »). Re-vérification faite : le gain du levier EDEL était **gonflé de 25 %** (+19,68 → +14,70 $/90 j) — le câblage tient, l'annonce était fausse. |
| **E11** | **Confondre COHÉRENCE et JUSTESSE (biais de source unique)** | 23/09, nommé par la famille (Grok) : mon invariant valide la formule **du moteur** — si le moteur se trompe, mes instruments le valident et **nous nous trompons ensemble**. La classe « le chiffre est fidèle mais la règle est mauvaise » reste **ouverte** | **AUCUNE GARDE — TROU DÉCLARÉ.** Remède identifié et chiffré : **oracle indépendant** = rejouer la kline brute et comparer au signal enregistré, en court-circuitant la logique interne du moteur. **En attente de GO.** |
| **E14** | **S'auto-absoudre par la confession** — lister ses erreurs passées puis conclure **plus loin que ses chiffres**, sans garde-fou équivalent pour ses propres déductions | 23/09, nommé par la **FAMILLE** (Nemotron, consultation de l'audit MEXC×HULK) : dans le même rapport où je nommais E10/E12/E13, j'ai tiré « le stop est une vérification périodique, pas un ordre au repos » (**n=32, aucun carnet à l'instant de l'impact**), compté des coûts de frais+spread comme un fait (**ils sont ESTIMÉS**, un paper ne paie rien) et généralisé 2 cas extrêmes (−16,5 % / −39,2 %). Les 4 modèles ont répondu la même chose : **mesure solide, explications en avance sur la mesure** | **Règle d'étiquetage de provenance** : toute conclusion d'un rapport porte **MESURÉ** (lu dans une source/un instrument) · **ESTIMÉ** (modèle, borne) · **EXTRAPOLÉ** (déduction non mesurée), et une cause non mesurée est écrite « OPEN » avec **le test qui la trancherait**. Contrôle externe : le brief de consultation **doit** lister mes erreurs ET soumettre mes conclusions neuves à la même contradiction (4 modèles). *Portée déclarée : pas encore mécanique — la classe est tenue par règle écrite + revue famille, comme E11.* |
| **E13** | **Écrire une heure de MÉMOIRE au lieu de la lire** — le temps traité comme un seuil : **estimé ≠ vérifié** (même famille qu'E10, appliquée à l'horloge) | 23/09 : 4 lignes écrites **10:40Z / 10:05Z / 09:45Z / 09:15Z** alors que les **artefacts cités par ces lignes mêmes** donnent **0947Z / 0939Z / 0922Z / 0907Z** → inflation jusqu'à **+53 min**, donc des lignes **datées dans le futur** | **`Index_Maison/scripts/verif_memoire_horodatage.py`** (23/09) : **R1** aucune ligne de la date la plus récente dans le futur (> +5 min — aurait attrapé les 4) · **R2** ordre décroissant dans la date · **autotest 5/5** (dont le cas réel rejoué à **heure FIXE** : un test qui passe à 14 h et échoue à 9 h ne prouve rien). **Méthode corrigée** : l'heure d'une ligne = le **`mtime` de l'artefact qu'elle cite**, sinon `date -u` au moment d'écrire. **Limites déclarées** : une heure **sous**-estimée est indétectable ; 25 lignes anciennes hors ordre sont **signalées, jamais re-datées** (cf. §6). |
| **E21** | **Compter comme voix indépendante un avis servi par un AUTRE modèle** — et laisser un « filet » conçu pour ne jamais être à sec **réduire un jury à une seule voix sans rien casser** | 23/09 : le hub local (127.0.0.1:11435) applique un « **filet universel** » — *« plus jamais à sec tant qu'UN provider répond »*. Sur échec/lenteur il **remplace** le modèle demandé et le signale (`substitue: true`). Mesuré : au tour 2 « DeepSeek » a été répondu par **Gemini** ; au tour 3 **les trois voix** ont été répondues par **Gemini** → le jury est tombé à **UNE voix**, sans erreur, sans alarme. Pire, mesuré après correctif : **le filet masquait une voix DISPONIBLE** — sans lui, `deepseek-ai/DeepSeek-V3-0324` répond **très bien** (HuggingFace, 1,2 s) ; avec lui, il était servi par Gemini. **La plomberie fabriquait la panne qu'elle prétendait couvrir.** Aggravant : mes 3 tours de jury ont été rendus avec 1, 2 puis 3 voix **sans que je le sache avant de le mesurer** | **Le HUB est corrigé** (`~/prise-ia/hub_prise_ia.py`, backup `hub_prise_ia.py.bak-strict-jury-20260923`) : mode **`strict_model`** — la chaîne est limitée aux fournisseurs qui servent **réellement** le modèle demandé, **aucun filet**, et un modèle indisponible **échoue franchement** (« voix INDISPONIBLE, pas de substitution silencieuse »). **La session famille envoie `strict_model: true`** et vérifie **avant chaque tour** avec `--test-modeles` (qui répond, depuis quel fournisseur). Test après correctif : **Nemotron ✔ (OpenRouter), DeepSeek ✔ (HuggingFace), nex-agi ✔, Grok → échec 502 (ne vote pas)** = **3 voix indépendantes**. **Règle du milieu appliquée** (ensembles/évaluations multi-fournisseurs) : on épingle le modèle, on vérifie `response.model`, une voix substituée est un **échec d'appel**, jamais un avis. *Déclaré : le trou par redondance n'est pas refermé côté hub (le choix des experts reste manuel) ; le tour 4 n'a eu que **2 voix** (nex-agi a expiré) et c'est écrit dans le fil.* |
| **E20** | **Juger les entrées contre le PLANCHER du profil au lieu du seuil EFFECTIF du moteur** — et publier le compteur global qui en découle | 23/09 : l'instrument de la boucle des set-ups (celui qui a servi à soumettre la boucle au jury) calculait `dip_exige = calib.dip_pct` (**le plancher**) et jugeait chaque achat contre `max(0,5 ; plancher × 0,5)` ; le tableau par famille comparait à un **« 2 % » plat**. Le seuil réel du moteur est `max(plancher ; DIP_CADENCE_MULT × cadence)` puis `max(… ; IMPULSE_PULLBACK_MIN_PCT ; FRAC × m6)` → pour **EDEL le seuil est 13,20 %**, RIZE 8,44 %, CHIP 6,69 %, QAIT 5,60 %, RED 5,01 % (5 paires sur 21 où la cadence DOMINE ; ailleurs la porte pullback de 5 % gouverne). Publié : **28 % d'entrées conformes** — le chiffre vrai est **5 % (3/60)**, et la table par famille passe de « 7/26 · 7/14 · 5/7 » à « **1/26 · 1/14 · 1/7** ». C'est le **jury du tour 1 qui a validé « les défauts de conception » sur ces chiffres** | **Ce n'est PAS moi qui l'ai trouvée : le gardien l'a criée tout seul** — `hulk-mexc/scripts/verif_seuil_moteur.py` §3 « détecteur d'instruments qui recalculent un seuil SANS le terme cadence » a désigné mon fichier, puis `mesures_jury_tour2.py`. **Corrigé** : `boucle_setups_main.py` reproduit la formule du moteur **terme par terme**, publie `dip_plancher_profil_pct` / `dip_terme_cadence_pct` / `dip_effectif_pct` / `dip_requis_pct` / **`dip_terme_dominant`** (déterminance R15) et la ligne par famille porte le **seuil médian de la paire** ; `mesures_jury_tour2.py` §8 fait l'audit plancher-vs-effectif **paire par paire** (exigence 8 du jury, passée de « insuffisant » à **fait**). Gardien : **✔ CONFORME** (plus aucun instrument ne recalcule un seuil sans la cadence). **Portée déclarée** : ma « chute » est mesurée sur les bougies 1 min, le moteur écrit son propre `dd6` — les lignes `impulsion/pullback` et `re-entrée` sont **indicatives, pas une preuve d'infraction**. |
| **E19** | **Publier la médiane d'un SOUS-ENSEMBLE en la présentant comme celle du TOUT** — et laisser un mode entier sans mesure | 23/09 : au tour 2 du jury j'annonce « **9 328 lectures live, médiane 1,057 s** » pour répondre à la barre < 1 s. Faux : la colonne `delay_s` du corpus du satellite n'est écrite **que pour les lectures en mode COMPLET** (2 lectures du carnet) ; les lectures en mode LÉGER laissent la colonne **vide**. Mesure réelle : **9 496 complètes** (médiane 1,058 s) contre **1 563 lignes SANS aucun délai** → mon chiffre portait sur **86 %** des lignes. Aggravant : la latence du mode léger **n'est mesurée nulle part** (angle mort de 14 %) → la barre de la famille **ne pouvait pas être prouvée**, quoi qu'on fasse | **`hulk-mexc/scripts/verif_delai_lecture.py`** (23/09) : sépare **mesuré / aveugle**, dit OUI ou NON sur la barre, chiffre le **nombre de lectures sans délai** et mesure le **plancher physique d'un appel MEXC** (médiane 465 ms sur 10 appels réels) → si le plancher dépasse la barre, c'est un **ARBITRAGE** et c'est écrit. Autotest **3/3** · branché **3 h** · **16ᵉ gardien du cockpit** (au ROUGE, et c'est la vérité : barre NON tenue sur les lectures mesurables) |
| **E18** | **Publier la valeur de REPLI du code comme si c'était la VALEUR EFFECTIVE de la config** | 23/09 : j'ai écrit dans le brief du jury, dans la mémoire de session et dans trois documents « **stop = max(plancher ; cadence × 0,70)** » et « plancher global 8 % ». `0.70` est le **défaut écrit dans le code** (`cfg.get("STOP_CADENCE_MULT", "0.70")`) ; la config applique **0,80**, et `STOP_FLOOR_PCT` vaut **6,0** (RIZE a son propre plancher de 8,0). Je n'avais **pas ouvert `config/defaults.env`** : j'ai lu un repli et je l'ai appelé « config ». C'est E17 (un plancher pris pour un seuil) déclinée : **une valeur de repli prise pour la valeur effective**. Le jury du tour 1 avait jugé la formule sur ce chiffre | **Aucune constante recopiée** : `hulk-mexc/scripts/chiffrage_stop_serre.py` **LIT `config/defaults.env` à l'exécution** et n'écrit plus le multiplicateur en dur ; `mesures_jury_tour2.py` publie la formule, la valeur lue, la cadence observée (médiane 16,88 %, max 55,58 %) et le stop qui en découle (médiane 13,50 %, pire **44,46 %**) · **correction publiée** dans les documents concernés · **R19** : tout chiffre sur la machine passe devant le jury, et un chiffre faux est retiré avec sa classe. *Déclaré : les tour 1/tour 2 du fil gardent leurs chiffres — je ne réécris pas un fil de jury (le passé n'est pas réécrit, il est déclaré).* |
| **E17** | **Publier un PLANCHER de configuration comme le seuil réel de la machine** — et le publier TROIS FOIS (rapport, évaluation, brief du jury) au point qu'il serve à construire un verdict | 23/09 : « **2 sorties RIZE à −16,5 % et −39,2 % pour un stop annoncé de 8 %** ». Le 8 % était `universe_profils.json → RIZEUSDT.calib.stop_pct` (un **plancher**) ; le stop RÉEL est `max(plancher ; cadence × STOP_CADENCE_MULT)` = **16,51 %** puis **39,23 %** — *et le multiplicateur lui-même était faux chez moi : j'ai écrit 0,70 (défaut du code) au lieu de **0,80** (config lue). C'est la classe **E18**, découverte en produisant les mesures du tour 2. Le présent registre est corrigé ; le fil de jury garde ses chiffres et le dit (E18).*, **écrit par le moteur dans ses propres motifs** (`stop-39.23%_guard_partial_50`), et **tenu au point de base**. Le jury du matin a jugé (3 voix sur 4 « inacceptable ») **sur mon chiffre faux**, en désignant « le stop » comme priorité n°1 | **Retrait public** (bandeau de correction en tête des 3 documents concernés) · **`hulk-mexc/scripts/oracle_independant.py`** — le niveau de stop est désormais **LU dans le motif du moteur**, jamais deviné ni pris dans une config · **`hulk-mexc/scripts/chiffrage_stop_serre.py`** — publie la **formule exacte**, **LUE à l'exécution** dans `config/defaults.env` (plus aucune constante recopiée — E18), et le contre-factuel d'un plafond · **R19** (jury permanent, session ouverte avec mémoire du fil) : tout chiffre à publier sur la machine passe devant le jury, et un chiffre faux publié est **retiré publiquement** avec sa classe |
| **E15** | **Écrire un fichier de données en DEUX largeurs** (en-tête et lignes désaccordés) — un journal qui devient illisible **en silence** | 23/09, 12:52 : les 5 colonnes ajoutées au journal du moteur (GO Christophe) ne survivaient pas au **RESUME**, qui recopiait l'ANCIEN fichier (`shutil.copy2`) **par-dessus** le nouveau → **en-tête 11 colonnes, lignes à 16**. Mesuré sur le journal vivant : **76 162 lignes à 11 champs + 12 lignes à 16**. Le journal n'était pas faux : il était **ambigu** — tout lecteur qui prend l'en-tête pour la vérité voit **5 colonnes sans nom** et 5 colonnes nommées qui n'existent pas dans les vieilles lignes | **`hulk-mexc/scripts/verif_schema_journal.py`** (23/09) : lit le schéma **à la source** (`paper_diprip.CSV_SCHEMA`, jamais recopié — une copie divergerait), **R1/R2** en-tête = largeur des lignes sur 20 journaux, **R3** le journal du moteur **VIVANT** doit être au schéma courant, **R4 autotest 4/4** (conforme · en-tête court reconnu cohérent · ligne large détectée · ligne vide tolérée). **Corrigé à la racine** : schéma = source unique · le resume **réécrit l'en-tête** et jette l'ancien · garde à l'écriture (`SCHEMA_ECART` hurlé au lieu d'écrire un journal bancal). Branché toutes les **3 h** + **15ᵉ gardien du cockpit** |
| **E16** | **Publier un avis sous le nom du modèle DEMANDÉ, pas de celui qui a RÉPONDU** | 23/09 : j'ai classé un avis en `AVIS_x-ai_grok-4.3.md` alors que le hub avait **SUBSTITUÉ** le modèle (`x-ai/grok-4.3` → `gemini-flash-lite-latest`, journalisé par le hub). Je ne lisais que `provider`, jamais `model`/`model_demande`/`substitue` que la réponse contient → une consultation « 4 modèles » aurait compté **2 fois Gemini** comme 2 voix indépendantes. Même famille que **E14** (publier au-delà de ce qu'on a vérifié) | **Instrument corrigé** : l'en-tête d'un avis s'écrit « demandé X — **RÉPONDU PAR Y** » + bandeau **SUBSTITUTION** qui déclare que l'avis **ne compte pas comme une voix indépendante** + `META_*.json` (demandé/servi/substitué/attempts). *Limite (R8) : je vérifie la déclaration du hub ; je ne peux pas prouver que le fournisseur amont n'a pas menti.* |
| **E12** | **Sceller un fichier puis le modifier** (process) | 23/09 : deux modifications **légitimes** (`paper_diprip.py` refus parlant, `chiffrage_entree_sortie_replay.py` terme cadence) ont fait crier R5/R13 à juste titre ; puis **3 fichiers scellés ont été modifiés APRÈS leur scellement** → la veilleuse a signalé « INTRUSION : modification non déclarée » **3 fois** | **Règle de processus écrite** : *on scelle APRÈS la dernière modification* + `Index_Maison/scripts/declarer_rescel_20260923.py` (backup horodaté + entrée `_rescel_*` qui dit **quoi et pourquoi**). Écarts md5 = **0**, Règles d'or 7/11 → **9/11**. |

---

## 3. Résultats NÉGATIFS déjà payés (à ne jamais re-tester sans nouvelle raison)

| Date | Chose testée | Verdict mesuré | Où c'est écrit |
|---|---|---|---|
| 17-18/09 | Duo ACE sur 4H (V2) | **échec**, net −64,19 $ (6 replays, 6 échecs) | MEMOIRE_COLLAB 17/09 |
| 18/09 | Set-up V2 base (dip 5 %) sur 20 actifs | **−31,63 $** sur 61 trades | MEMOIRE_COLLAB 18/09 |
| 18/09 | V2 + filtre tendance | −1,29 $ (34 tr) — insuffisant | idem |
| 18/09 | filtre poussière / V2 | **efficacité ≈ 0** | idem |
| 21/09 | Sortie calibrée au pic (S2) | **perd 17 $** sur nos entrées réelles | `chiffrage_sortie_calibree.py` |
| 21/09 | Levier compounding | **inerte** : −0,12 $ sur 28 j (raboté avant d'agir) | R16 / `chiffrage_compounding.py` |
| 21/09 | `TIER_B_POSITION_MULT` 0,25→1,0 | +4,29 $/mois mais ratio gains/pertes **1,68:1** → refusé | MEMOIRE 12:25Z |
| 21/09 | Replay qui « ne voit pas » la porte volume | EDEL : `vol_DRY_impulse_block` | limite déclarée |
| **22/09** | **Halt piloté par l'edge récent de la paire** | **ÉCHEC : les trades pris en « edge<0 » gagnent quand même +0,29 $/trade** (n=23) → **aucune persistance de l'edge** → on ne peut pas décider sur l'historique récent de la paire | ce document, §4 |
| **22/09** | **Refroidissement en heures (6/24/48)** | **RETIRÉ le jour même** : viole R17 (seuil de temps fixe) | `_rescel_20260922c` |
| **22/09** | **Sortie à échelle SYMÉTRIQUE** (palier × cadence_paire/référence, sans plancher) | **ÉCHEC : signe INSTABLE** (+2,95 $ sur la 1re moitié, **−2,54 $** sur la 2e) → elle **abaisse** le palier des paires calmes (BTC r=0,40, ETH 0,45) alors que leur MFE médian est de 5,5 % | `chiffrage_sortie_mesuree.py` |
| **22/09** | Palier LATE élargi sans plancher (6 %/8 % → mesuré) | +13,04 $ **mais** +7,88 $ de pertes suppl. (ratio 1:1,7) — **moins bien payé** que la variante plancher (1:4,7) | idem |
| **22/09** | Élargir la sortie via la branche `A2` (+6 %/+8 % **partout**) | +8,66 $ sur l'échantillon mais c'est **un % universel de plus**, pas une mesure → ne répond pas à R17 | idem |
| **22/09** | **Relecture des seuils de RÉGIME** (`QUIET_RANGE_PCT`, `SPIKE_15D_PCT`) dans l'unité de chaque paire | **REJETÉE** : les 33 barres qu'elle bloquerait ont une **médiane de +74,5 %** de hausse en 24 h (moyenne +56,3 %) → elle bloque **juste avant les plus gros mouvements**. Les 734 barres qu'elle ouvre valent +2,55 % de médiane : ça ne paie pas | `chiffrage_regime_mesure.py` / `REGIME_MESURE_20260922.md` |

---

## 4. La mesure qui a tué mon idée (à garder, c'est une leçon)

Question : **« les chiffres de la paire disent-ils quand s'arrêter ? »**
Test (aucune horloge — la fenêtre = les 3 derniers trades **fermés de la paire**) :

| État mesuré de la paire | n | P&L moyen par trade |
|---|---|---|
| 3 derniers trades **négatifs** | 23 | **+0,2923 $** |
| 3 derniers trades positifs | 35 | +0,7188 $ |

**Verdict : l'edge récent ne prédit PAS le trade suivant** (les trades pris « après des pertes »
gagnent quand même) → **réduire la taille sur cette base couperait des trades gagnants.**
Donc **on ne câble rien** : ce n'est pas la bonne grandeur. La bonne, mesurée et déjà câblée, est le
**risque en dollars** (fusible : k × σ_mesuré × mise).

---

## 5. Ce qui a été fait pour que « ça ne se reproduise pas » — BRANCHÉ, pas écrit (22/09)

1. **LE REGISTRE EST BRANCHÉ** (fait) : il est cité par **les règles d'or (R17.5)** et par
   **`.cursorrules`** — les deux points d'entrée d'où part une proposition de garde. Contrôle
   mécanique : `scripts/critique_erreurs.py` **sort en erreur** si l'un des deux cesse de le citer
   (un registre non lu n'existe pas, R15).
2. **LE CRITIQUE TOURNE TOUT SEUL** (fait) : il est **accroché à l'organe de discipline
   quotidienne** (`discipline_quotidienne.py`, launchd 07:15) — **pas de 98ᵉ agent**. Chaque matin,
   le rapport écrit la section **ERREURS** et l'alerte crie si une classe **récidive après sa
   correction**, ou si le registre cesse d'être cité.
3. **VISIBLE DANS LA PAGE QU'ON REGARDE DÉJÀ** (fait, GO 2) : les trois verdicts (registre branché /
   récidives · seuils sans mesure R17 · sortie armée et conforme) sont affichés comme **gardiens du
   cockpit « vol »** — un verdict qu'il faut aller chercher dans un dossier n'existe pas (R15).
4. **DEUX DÉTECTEURS, parce qu'un seul laisse un trou** (fait) :
   - **prose (critique_erreurs)** → un **AVEU** est exigé (« j'ai encore… », « récidive… »). Parler
     d'une erreur n'est pas la commettre — une alarme qui sonne pour un comportement voulu tue la
     confiance dans l'alarme (R14). ⚠️ **Limite déclarée** : un aveu tu lui échappe.
   - **mécanique (inventaire_seuils_fixes)** → **toute clé de config qui décide sans être mesurée
     ni rangée est nommée**, chaque passage. Un seuil inventé **ne peut pas se cacher dans du texte**.
     Preuve immédiate : il a **crié tout seul** sur le réglage créé ce matin (`RIP_CADENCE_REF_PCT`,
     1 non classé) avant que je le range — le mécanisme marche sur un cas réel, pas en théorie.

---

## 6. Rapport d'erreur E13 — les horodatages écrits de tête (23/09/2026)

**Ce qui s'est passé** : en clôturant trois chantiers, j'ai daté 4 lignes de `MEMOIRE_COLLAB.md`
**de mémoire**. Les artefacts cités par ces lignes mêmes donnent l'heure réelle :

| ligne (chantier) | heure écrite | heure réelle (mtime de l'artefact cité) | écart |
|---|---|---|---|
| set-up paire par paire | 10:40Z | **0947Z** — `hulk-mexc/runs/SETUPS_PAIRES_20260923.{txt,json}` | **+53 min** |
| gardien au cockpit + famille | 10:05Z | **0939Z** — `…/CONSULTATION_FAMILLE_GARDE_FOU_SEUIL_20260923/SYNTHESE.md` | +26 min |
| GO 0 + GO 1/2/3 | 09:45Z | **0922Z** — `hulk-mexc/runs/SEUIL_MOTEUR.json` | +23 min |
| refus parlant + seuil réel | 09:15Z | **0907Z** — `Index_Maison/REFUS_PARLANT_ET_SEUIL_REEL_20260923.md` | +8 min |

**Ce que ça coûte** : rien au moteur (0 €, 0 ordre) — mais `MEMOIRE_COLLAB.md` est la pièce que
Cursor, Punk, Cortana et Christophe lisent pour savoir **ce qui a bougé quand**. Une heure écrite
de tête y rend l'ordre des causes invérifiable ; une ligne datée **dans le futur** est
**impossible** et détruit la confiance dans le fichier entier. C'est la classe **E10** (chiffre
recalculé pris pour vérifié) appliquée au temps.

**La garde branchée** : `Index_Maison/scripts/verif_memoire_horodatage.py` — **R1** (aucune ligne
de la date la plus récente dans le futur, +5 min de marge) · **R2** (ordre décroissant dans la date)
· **autotest 5/5**, rejoué à **heure fixe** (un test qui passe à 14 h et échoue à 9 h ne prouve
rien). Rejoué sur le fichier réel : **CONFORME** (154 lignes horodatées).

**Ce que la garde a trouvé en plus — signalé, pas corrigé** : **24 remontées de temps** dans des
dates anciennes (22/09 : 0907Z puis 0925Z · 20/09 · 18/09 · 17/09 · 14/09 · 13/09 · 11/09 · 03/09).
Elles sont **signalées** et **jamais re-datées** : je refuse d'**inventer une seconde fois** pour
corriger un chiffre inventé. Méthode à appliquer à la prochaine passe : lire le `mtime` de
l'artefact cité par la ligne.

**Limites déclarées (R8)** : la garde attrape une heure **trop grande**, jamais une heure **trop
petite** ; et elle ne juge que la date la plus récente.

**Méthode corrigée (écrite pour de bon)** : l'heure d'une ligne de mémoire =
**le `mtime` de l'artefact qu'elle cite** ; sinon `date -u` **au moment d'écrire**. Jamais de tête.

---

## 7. Rapport d'erreur E15 — le journal écrit en deux largeurs (23/09/2026)

**Ce qui s'est passé** : GO Christophe du 23/09 → ajouter au journal du moteur la provenance du
prix (quand il a été lu, son âge, le spread retenu, sa source, le coût estimé). Les colonnes ont
été ajoutées **dans le fichier naissant**, mais le **RESUME** recopiait l'ancien journal
(`shutil.copy2`) **par-dessus le nouveau** : le fichier vivant est reparti avec l'**en-tête de
l'ancien schéma** et des **lignes à 16 champs**.

**Mesuré (pas déduit)** : `PAPER_V1_20260923_105249.csv` → **en-tête 11 colonnes**, **76 162
lignes à 11** et **12 lignes à 16** ; 19 autres journaux **cohérents** (11/11 — légitimes, nés
avant le changement de schéma). Autrement dit : **un seul fichier fautif, mais c'est le seul que
les autres outils lisaient**.

**Pourquoi c'est grave et pourquoi personne ne le voyait** : c'est **silencieux**. Un fichier de
données écrit en deux largeurs ne plante rien : il rend une colonne **innommable**. C'est la même
classe que E10 (chiffre non vérifié) et E13 (heure non vérifiée) — **une donnée non VÉRIFIÉE**,
ici au niveau du **schéma**.

**Corrigé à la racine, pas au cas** :
1. `CSV_SCHEMA` = **source unique de vérité** dans `paper_diprip.py` (en-tête né et repris du même endroit) ;
2. le resume **réécrit l'en-tête courant** et **jette l'ancien** (les vieilles lignes restent, sous le schéma courant) ;
3. garde **à l'écriture** : `SCHEMA_ECART` est **hurlé** au lieu d'écrire une ligne bancale ;
4. `verif_schema_journal.py` branché (3 h + cockpit).

**Vérifié** : journal relancé (`PAPER_V1_20260923_110439.csv`) → **en-tête 16**, 76 162 lignes
historiques + lignes neuves à 16, **CONFORME rc=0**, autotest **4/4**. Moteur relancé par le
**watchdog de la maison** (`com.ace777.hulk-watchdog`, relance `--resume`), état repris
**pnl 42,1679 $ / 175 trades / 10 positions** — identique avant/après.

**Limite déclarée (R8)** : ce contrôle attrape un **désaccord de largeur**. Il ne dit **pas**
qu'une valeur dans une colonne est juste — seulement que la donnée est **lisible et nommée**.

**Ce qui n'est PAS corrigé (et qui est déclaré)** : le journal courant garde **76 162 lignes
historiques à 11 champs** sous un en-tête à 16 (choix assumé : ne pas réécrire le passé).

---

## 8. Rapport d'erreur E16 — l'avis publié sous le nom d'un autre modèle (23/09/2026)

**Ce qui s'est passé** : la consultation du jour classe ses avis par modèle demandé. Le hub a
**substitué** un modèle (`x-ai/grok-4.3` → `gemini-flash-lite-latest`) et **je ne l'ai pas vu** :
je ne lisais que `provider` dans la réponse. J'allais donc présenter **Gemini deux fois** comme
**deux voix indépendantes** dans un jury de 4 — soit un jury de **3**.

**Preuve** : le hub **journalise** la substitution (`prise-ia/hub_events.jsonl` :
« MODELE SUBSTITUE : demandé « x-ai/grok-4.3 » → servi « gemini-flash-lite-latest » ») et la
réponse expose `model` (qui a répondu), `model_demande`, `substitue`, `attempts`.

**Corrigé** : l'en-tête d'un avis porte désormais **« demandé X — RÉPONDU PAR Y »**, un bandeau
**SUBSTITUTION** déclare que cet avis **ne compte pas comme voix indépendante**, et un `META_*.json`
conserve les métadonnées. Fichier réécrit en conséquence — le texte est d'origine, **l'étiquette est
corrigée**.

**Limite déclarée (R8)** : je vérifie **la déclaration du hub**, pas la réalité du fournisseur.

**Conséquence sur le verdict du jour** : le jury n'a **pas 4 voix mais 3** — Gemini (**deux fois** :
avis direct + avis substitué), Nemotron-120b, DeepSeek-V3. Les comptes sont corrigés partout.

---

## 9. Rapport d'erreur E17 — le plancher pris pour le seuil de la machine (23/09/2026)

**Ce qui s'est passé** : j'ai publié « **2 sorties RIZE à −16,5 % et −39,2 % pour un stop annoncé
de 8 %** » — dans l'audit MEXC × HULK, dans mon auto-évaluation, et dans le **brief envoyé au
jury**. Les 3 voix sur 4 ont classé « le stop ne tient pas » en **priorité n°1**, et Christophe a
travaillé sur ce chiffre.

**Le chiffre venait d'où** : `cartographie_setups_paires.py` fait `annee = float(cal.get("stop_pct"))`
où `cal` = `profil.calib` — donc **le PLANCHER** de configuration (RIZE 8,0). Le moteur, lui,
applique `stop = max(stop_floor ; cadence × STOP_CADENCE_MULT)` : **RIZE 16,51 % puis 39,23 %**.
*Correctif du 23/09 (classe E18) : le multiplicateur lu dans `config/defaults.env` vaut **0,80** (et
`STOP_FLOOR_PCT` **6,0**) ; « 0,70 » était le **défaut du code**, recopié par erreur. La valeur
n'est plus recopiée nulle part : elle est lue à l'exécution.*
Et il **l'écrit dans ses motifs de sortie** : `stop-39.23%_guard_partial_50`. **Je n'avais pas lu la
source qui le disait** — E10/E2 une fois de plus, appliquée à un seuil.

**Mesuré après correction (oracle indépendant, bougies 1 min MEXC, 60 trades / 10 jours)** :
- **9 / 13 stops honorés** (sortie dans la minute du contact du niveau) · 4 en retard (médiane
  88 min, max 303 min) · coût du retard **+0,56 $** (positions de 3 à 43 $) ;
- 14 sorties de type stop vérifiées une par une : RED 6,0→−6,01 · XRP 6,0→−6,08 · ZBCN 6,0→−6,06
  · W 6,0→−6,08 · KITE 6,0→−6,46 · CC 6,0→−6,98 · PYTH 6,67→−6,98 · EDEL 13,8→−14,25 et
  11,95→−12,06 · RIZE 39,23→−39,23 et −39,38. **Le stop tient.**
- Ce qui reste un **vrai** défaut, mais de **NIVEAU** : RIZE se voit un stop à **39-44 %** —
  une protection nominale inexistante. Contre-factuel chiffré : plafond à 15 % → **+0,87 $ sur
  10 jours** (chiffre **OPTIMISTE**, sans ré-entrée, sortie supposée au niveau exact).

**La garde branchée** : ① l'oracle **lit** le niveau dans le motif du moteur (plus jamais de
niveau deviné) ; ② `chiffrage_stop_serre.py` publie la **formule** avec son contre-factuel ;
③ **R19** (jury permanent, session ouverte, mémoire du fil) : tout chiffre sur la machine passe
devant le jury, et un chiffre faux est retiré avec sa classe.

**Ce que je déclare ne pas avoir refermé** : je n'ai pas vérifié que les **autres** planchers de
configuration (`dip_pct`, `rip_pct`, `mise_max_pct_mur`, seuils de `defaults.env`) ne sont pas, eux
aussi, publiés quelque part comme s'ils étaient les seuils effectifs. **La question est ouverte**
(exigence posée par DeepSeek au tour 1 du jury : « audit des autres planchers config vs seuils réels »).

---

## 10. Tour 2 du jury permanent — les 8 mesures exigées, et les classes E18/E19 (23/09/2026)

**Le tour 2 a été soumis dans la session ouverte** `SUPERVISION_BUFFY_23_09` (brief archivé :
`BRIEF_T02_mesures.md`, fil complet dans `transcript.jsonl`, mémoire dans `MEMOIRE.md`).

### 10.1 Les mesures, une par une (instrument : `hulk-mexc/scripts/mesures_jury_tour2.py`)

| # | exigence du jury | chiffre produit | étiquette |
|---|---|---|---|
| 1 | [Gemini] délai de lecture **< 1 s** | médiane **1,058 s** · p90 2,020 s · **22,7 %** sous la barre | **MESURÉ — barre NON tenue** |
| 2 | [DeepSeek/Nem] fréquence de scrutation | `POLL_SEC = 20 s` · âge du prix à la décision : médiane 0,00 s, max 37,0 s · sorties via prix frais GO 2 : **0** | MESURÉ (délai de stop après GO 2 : INSUFFISANT) |
| 3 | [Nemotron] âge ↔ glissement | **0 couple exploitable** (colonne créée après les 53 stops passés) | **INSUFFISANT — non comblé par une estimation** |
| 4 | [Nemotron] espérance de `cooling` | n=12 · **+0,605 $/trade** · net +7,26 $ · gagnants **8/12 (67 %)** vs reste **48 trades à +0,536 $/trade et 79 %** | MESURÉ |
| 5 | [DeepSeek] source des bougies | API MEXC nommée · 16 caches SHA-256 · **re-téléchargement live** de 2 bougies RIZE | MESURÉ |
| 6 | [Gemini] formule exacte du stop RIZE | `max(8,0 ; cadence × 0,80)` · cadence médiane 16,88 %, max 55,58 % → stop médian **13,50 %**, pire **44,46 %** | MESURÉ (config lue) |
| 7 | [DeepSeek] plafond stop 15 % sur RIZE | creux −14,59 % et **−40,56 %** · perte au creux **−1,87 $ → −0,99 $** (**−47 %**) · 10 jours : **+0,87 $** sur +32,97 $ | MESURÉ · **portefeuille = EXTRAPOLÉ, non signé** |
| 8 | [DeepSeek] audit des autres planchers | 11 paires : `stop_pct` 6,0→10,3 · `dip_pct` 4,0→5,5 · `rip_pct` 3,0→5,2 ; le motif RIZE porte **39,23 %** quand la config porte **8,0** | MESURÉ · **audit motif par motif : INSUFFISANT (non fait, non déclaré fait)** |

### 10.2 Le verdict du tour 2, et un fait que le gardien a attrapé tout seul

**Méthode déclarée RECEVABLE (3/3 avis)** — « rigueur irréprochable », « méthode recevable ».
**Défaut n°1 confirmé : le délai de lecture du prix** (les trois avis) — c'est-à-dire la mesure que
j'avais présentée de travers (E19). **Sur le plafond de stop à 15 % : « à câbler »** (avis servi).

**Fait déclaré, pas caché** : l'avis « DeepSeek » du tour 2 a été **SUBSTITUÉ par gemini**
(en-tête du fichier : *demandé deepseek-ai/DeepSeek-V3-0324 — RÉPONDU PAR gemini-flash-lite-latest*,
bandeau SUBSTITUTION). Le jury n'a donc eu que **2 voix indépendantes** (Nemotron + Gemini) —
**et le gardien `verif_session_famille.py` l'a signalé SEUL** (`R3 dernier tour (2) : 2 voix
indépendantes < 3`, session AU ROUGE, visible au cockpit). C'est exactement le mécanisme exigé par
Christophe : la fenêtre est jugée par une règle, pas par ma parole.

### 10.3 L'arbitrage que le gardien de latence a mis au jour (classe E19)

**Plancher physique mesuré** (10 appels réels, 23/09 12:20Z) : un seul `GET /depth?limit=20` coûte
**465 ms** médian (`/ticker/price` : 317 ms). Or une lecture **complète** = **2 appels séparés de
0,5 s** — l'écart est **voulu** : c'est lui qui mesure la **vitesse de chute** du mur
(`drop_bid_pct_per_s`), le signal d'entrée du moteur. Donc une lecture complète **ne peut pas
descendre sous ~965 ms par construction**.

**Conséquence, que je refuse de maquiller** : la barre « < 1 s » du jury est **inatteignable pour les
lectures complètes** à ce plancher réseau. Ce n'est pas un retard à corriger : c'est un **arbitrage**
entre (i) mesurer la chute en 2 lectures et (ii) lire en 1 lecture pour être sous la barre.
Trois sorties possibles, **à trancher par Christophe (R19 : je ne décide plus seule)** :

1. **Mesurer la chute sur deux passes successives** (1 lecture par passe) → délai ~0,5 s, au prix
d'une finesse de mesure de la chute à la cadence des passes (~9 s) ;
2. **Garder 2 lectures** pour les paires qui ont besoin du signal de chute, **1 lecture + délai
MESURÉ** pour les autres (aujourd'hui le mode léger **ne mesure pas son délai** : angle mort) ;
3. **Bouger la barre**, en la déclarant : « < 1 s » est incompatible avec « mesurer une chute par
seconde » à 465 ms d'aller-retour. (C'est le jury qui a fixé la barre, pas la machine.)

### 10.3bis Les tours 3 et 4 — et ce que la plomberie faisait au jury (classe E21)

**Tour 3** (auto-correction E20) : le gardien a désigné mon instrument, j'ai publié les chiffres
corrigés contre moi. **Une seule voix indépendante** ce tour-là (les trois servies par Gemini).

**Tour 4** : Christophe a refusé mon « arbitrage » (« **pourquoi ne pas faire les deux ???** »).
La réponse du milieu — **écouter le carnet au lieu de le demander** — a été **mesurée** : flux
WebSocket MEXC (`wss://wbs-api.mexc.com/ws`, `…bookTicker…@10ms|100ms@<paire>`) → **âge du prix
médian 14–15 ms, p90 81 ms, 100 % sous 1 s** (456/456 puis 610/610 échantillons) contre
**1 058 ms / 22,7 %** en REST. Cadence : **11 ms (RIZE/TEL, pas de 10 ms)** et 100 ms (ZBCN/BTC).
**Donc : la fraîcheur ET la mesure de la chute, en même temps** — l'arbitrage était un **faux
dilemme né de ma méthode de lecture**. *NON fait : le câblage (snapshot REST + deltas) touche le
moteur, il attend le GO ; et la chute n'est PAS mesurée (trames protobuf non décodées) — déclaré.*

**Verdict du tour 4 (2 voix indépendantes vérifiées)** : le verdict du tour 1 **tient** (les défauts
structurels ne dépendent pas du compteur E20) · la direction **WebSocket est VALIDÉE** comme
réponse à l'exigence de latence · et **2 voix sur 2 me contredisent** sur le stop de RIZE : elles
exigent un **plafond**, même pour +0,87 $, au nom du **risque de queue**, avec un backtest 30 jours.
→ Désaccord **respecté et enregistré** : c'est le seul point où je prenais position, et le jury la
refuse. La décision reste à Christophe (moteur), avec le chiffre des deux côtés.

**Classe E21** : le « filet universel » du hub substituait les voix **en silence** (1 voix au lieu
de 3) **et masquait un fournisseur qui répondait**. Corrigé par `strict_model` (échec franc) +
`--test-modeles` avant chaque tour + comptage des **voix indépendantes** dans le fil et au cockpit.

### 10.4 Ce qui reste ouvert, nommé

- **délai de stop après GO 2** (médiane/p90) : impossible avant les premiers stops — quelques heures
  à quelques jours ; le tag `_impact_av{N}s_ap{M}s` le produira ;
- **âge × glissement** : 0 observation ;
- **audit motif par motif des planchers** : non fait (sonde à écrire) ;
- **plafond de stop par paire** : le jury dit « à câbler » (**2 voix indépendantes**), le gain mesuré
  est **+0,87 $ sur 10 jours** — **je ne câble pas sans le GO de Christophe** : c'est le moteur.

**Vérifications du jour** : gardien fenêtre famille **8/8 autotest, session OUVERTE** · gardien
latence **3/3 autotest** (rc=1 assumé) · gardiens moteur rc=0 · **0 ordre, 0 €**.
