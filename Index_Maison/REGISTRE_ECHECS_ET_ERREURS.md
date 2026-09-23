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
