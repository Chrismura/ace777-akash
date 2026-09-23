# 23/09/2026 — GO 0 À GO 3 : LE GARDE-FOU, LA SORTIE, LA CADENCE, LA TAILLE

> Demande Christophe : **« go 1,2,3. c'est pas possible de faire encore ce type d'erreurs »**.
> Réponse : l'erreur n'était pas un chiffre, c'était **une méthode** — recalculer un seuil de
> mémoire au lieu de le confronter à ce que le moteur ÉCRIT. **GO 0 construit le garde-fou qui
> rend cette classe d'erreur impossible à répéter** — et il a immédiatement trouvé **un second
> instrument défectueux, celui-là même qui a servi à câbler un flag du moteur en production.**
> **0 ordre, 0 €, aucune décision modifiée** (sauf le garde-fou, additif).

---

## GO 0 — LE GARDE-FOU (et il a déjà rapporté)

`hulk-mexc/scripts/verif_seuil_moteur.py` — lecture seule, 3 contrôles + 1 autotest :

1. **INVARIANT SUR DONNÉES RÉELLES** : chaque ligne où le moteur écrit ses propres chiffres
   (`ATTENTE:IMPULSE_WAIT dd6=… seuil=… m6=…` + sa cadence colonne 9) est **recalculée** depuis
   `config/defaults.env` et le profil de la paire, puis comparée. → **6/6 conformes**, et il
   nomme le terme qui décide (R15) :
   `RIZE cadence 51,1 % → seuil 21,70 % (décide : cadence)` · `TEL 8,2 % → 4,25 % (décide : plancher)`.
2. **DÉTECTEUR D'INSTRUMENTS** : tout script qui **recalcule un seuil d'entrée sans le terme
   cadence** est signalé (motif exact de l'erreur, cherché dans le texte, pas dans mon intuition).
3. **AUTOTEST (preuve qu'il SAIT échouer)** : seuil vrai (20,87 %) → conforme · seuil **faux**
   (4,25 % = **ma** formule tronquée) → **DÉTECTÉ en faute, écart −16,62 pt**. Un gardien qui ne
   peut pas échouer n'est pas un gardien (leçon du faux-vert du 20/09).
4. Sortie `rc=0` conforme / **`rc=3` DÉSACCORD** · état écrit dans `runs/SEUIL_MOTEUR.json` (prêt
   à être affiché au cockpit — voir §4).

### Ce qu'il a trouvé en 10 secondes

| instrument | état | conséquence |
|---|---|---|
| `chiffrage_entree_sortie_replay.py` | **DÉFECTUEUX** (3 calculs de seuil sans la cadence) | c'est **l'instrument du 21/09** qui a produit les chiffres ayant mené au câblage `IMPULSE_SANS_REPLI_ON` sur EDEL |
| `serrure_preflight.py` | faux positif (il **liste** les clés `calib` lues par le moteur) | détecteur affiné : on ne signale que les lignes de **CALCUL** — un gardien qui crie à tort est ignoré |

### Le câblage EDEL, RE-VÉRIFIÉ (le second instrument est corrigé)

Replay rejoué **hors ligne** (klines locales, 90 j × 20 paires) avec le **seuil réel** :

| | 21/09 (formule tronquée) | 23/09 (formule réelle) |
|---|---|---|
| EDEL E0 (actuel) | −1,10 $ | **+3,88 $** |
| EDEL E2 (sans repli) | +18,58 $ | **+18,58 $** |
| **gain du levier EDEL** | +19,68 $ | **+14,70 $** |
| rafales inaccessibles (portefeuille) | 25/38 = 66 % | **32/38 = 84 %** |
| E2+X2 (sans repli + trailing), test | +62,50 $ | **+59,42 $** (1re moitié +21,80 $ → ✅ cohérent) |

**⇒ le flag EDEL n'est PAS invalidé ; il est mieux fondé qu'annoncé (66 % → 84 % de rafales
inaccessibles) mais son gain chiffré était GONFLÉ de 25 %** (+19,68 → +14,70 $/90 j).

---

## GO 1 — LA SORTIE DE RIZE : ce n'est pas le va-et-vient, c'est le STOP qui ne tient pas

Instrument neuf `chiffrage_sortie_paire.py` (journal du run + chemin de prix dense) :

| histoire COMPLÈTE de RIZE | n | Σ PnL |
|---|---|---|
| **STOP / GUARD** | **8** | **−2,79 $** |
| **DUST_SWEEP** (balayé en poussière) | **5** | **−1,39 $** |
| TRAILING | 2 | +0,87 $ |
| RIP / paliers | 8 | +2,18 $ |
| **TOTAL** | 23 | **−1,12 $** |

**Les pertes de stop réalisées : 9,58 · 9,58 · 9,58 · 13,75 · 14,58 · 16,51 · 16,51 · 39,23 %**
— alors que le **stop annoncé dans le profil de RIZE est de 8 %**.

⇒ **Le stop n'est pas un stop** : il se réalise entre 1,2× et 4,9× le niveau annoncé, et **5 fois
sur 23 la sortie ne se fait même pas en marché mais en « dust sweep »**. Ce que ça coûte :
**−4,19 $ d'exits dégradés contre +3,06 $ de gains** → la paire perd. Le giveback moyen mesuré
sur ces sorties (pic atteint pendant la détention vs prix de sortie) est de **20 à 70 points**.

**Ce n'est PAS un problème d'entrée, ni de trailing, ni de ré-entrée** (mesuré : **0 BUY sur 8**
passé plus haut que la dernière vente). C'est **la sortie dans un carnet qui ne porte rien**.

---

## GO 2 — LA CADENCE PAR PAIRE : qui paie, et qui est structurellement inatteignable

`chiffrage_pump_manque.py --cadences` — cadence **écrite par le moteur** (colonne 9) :

| paire | cadence | repli **exigé** (`0,50 × cadence`) | seuil | jambes ≥ 20 % | **inaccessibles** | PnL réalisé |
|---|---|---|---|---|---|---|
| EDEL | 26,4 % | **13,20 %** | 11,22 % | 1 | 0 (0 %) | +5,78 $ |
| **RIZE** | 16,9 % | **8,44 %** | 7,17 % | 4 | **4 (100 %)** | **−1,12 $** |
| CHIP | 13,4 % | 6,69 % | 5,69 % | 2 | 0 | +9,49 $ |
| RED | 10,1 % | 5,03 % | 4,27 % | 1 | 0 | +12,30 $ |
| … 15 paires | 2,4–9,4 % | 1,19–4,70 % (plancher) | 1,01–3,99 % | 0–1 | 0 | +0,36 à +4,54 $ |
| QNT | 4,6 % | 2,29 % | 1,94 % | 1 | **1 (100 %)** | +0,37 $ |

**Le fait, en une ligne** : le seuil exigé varie de **1,70 % (BTC) à 11,22 % (EDEL)** — un facteur
**6,6** entre celui qui bouge le moins et celui qui bouge le plus. **RIZE est la seule paire dont
TOUTES les jambes de la fenêtre étaient inaccessibles — et c'est la seule perdante nette.**
La règle n'est pas cassée : elle est **proportionnelle à la violence de la paire**, donc elle
ferme **exactement** les pumps qu'on veut attraper.

---

## GO 3 — LA TAILLE MESURÉE : la profondeur est LÀ, et le « mur » est faux

Instrument neuf `sonde_profondeur_carnet.py` (carnet public MEXC, lecture seule) :

| paire | spread | absorbable < −0,5 % | **< −2 %** | plus gros niveau (« mur ») | plafond actuel = 2 % du mur | plafond / profondeur |
|---|---|---|---|---|---|---|
| CHIP | 19,7 bps | 88 059 $ | 99 775 $ | 460 968 $ | 9 219 $ | **9,2 %** |
| BIO | 13,4 bps | 13 826 $ | 15 653 $ | 131 415 $ | 2 628 $ | **16,8 %** |
| **RIZE** | 42,0 bps | **406 $** | **649 $** | **801 457 $** | 16 029 $ | **2 471 %** |
| TEL | 60,1 bps | 95 $ | 3 770 $ | 24 354 444 $ | 487 089 $ | **12 918 %** |
| ZBCN | 13,3 bps | 4 293 $ | 6 177 $ | **569 780 200 $** | 11 395 604 $ | **184 475 %** |
| RWAINC | 32,5 bps | 1 877 $ | 4 733 $ | 1 001 011 $ | 20 020 $ | 423 % |
| EDEL | 6,6 bps | 181 $ | 1 093 $ | 100 050 $ | 2 001 $ | 183 % |
| BTC | 0,0 bps | 3 601 992 $ | 7 972 222 $ | 24 $ | 0,48 $ | 0,0 % |

**Deux faits, et ils vont dans des sens opposés — c'est exactement pour ça qu'il fallait mesurer :**

1. **La profondeur est LÀ.** La mise réellement utilisée sur RIZE est de **4,88 $** = **0,75 %**
   des **649 $** absorbables sous −2 %. Sur TEL 27 $ (0,7 % de 3 770 $), sur RWAINC 27 $ (0,6 %
   de 4 733 $). **Le plafond n'est pas ce qui limite : il est ~100× plus prudent que le carnet.**
2. **Le « mur » qui le calcule est un FAUX.** `cap = 2 % × (mur live d'`aspiration_live.json`, sinon
   le mur médian du profil)`. Or le plus gros niveau mesuré vaut **801 457 $ sur RIZE** — soit
   **1 234× la profondeur réelle de son carnet** (−2 % = 649 $) — et **569 M$ sur ZBCN**. Ce sont
   des **niveaux affichés, pas exécutables** (la maison les mesure déjà : `murs_observations.json`
   → `spoof_n`, `spoof_pct`, `drop_n`). ⇒ **un plafond calculé sur ce chiffre ne veut rien dire** :
   soit il explose (16 029 $ de mise sur un carnet qui porte 649 $), soit il s'écrase sur la valeur
   figée du profil (4,88 $). Dans les deux cas **il ne mesure pas ce qu'il croit mesurer**.

**Ce que je propose (RIEN n'est câblé, GO requis)** : remplacer `2 % × mur` par une fraction
**mesurée** de la **profondeur cumulée sous un déplacement de prix plafonné** (la courbe ci-dessus).
Concrètement : la sonde tourne **en continu** et on accumule une **série** (elle est périmable :
les niveaux fantômes valent 8,8 % de la valeur affichée) ; la mise devient *« celle que le carnet
absorbe sous −0,5 % »* × une fraction prudente. **Mesuré, par paire, réversible, et ça ne touche
aucune garde.** Mais **pas avant d'avoir la série** — décider sur une photo, c'est du bricolage.

---

## 4. LIMITES DÉCLARÉES (E8) ET ÉTAT

- **GO 0** : l'invariant compare **le seuil écrit** au seuil recalculé — il ne prouve pas que la
  **formule** est la bonne stratégie, seulement qu'elle est **la même** des deux côtés. Le gardien
  doit être **branché** (cockpit/organe de discipline) pour exister tous les jours : c'est un
  **GO** à donner (il touche un générateur scellé → re-scellement requis).
- **GO 1** : les « givebacks » sont mesurés sur le chemin de prix du log (5-6 min de granularité) —
  ils sous-estiment les pics réels entre deux cycles. Le `dust_sweep` lu ici = **l'intention
  écrite par le moteur** (sa raison), pas le remplissage.
- **GO 2** : cadence = **médiane sur tout le run par paire** (une paire peut changer de régime) ;
  jambes ≥ 20 % = seuil d'**AFFICHAGE** déclaré ; 5 jours, 20 paires → **aucun verdict statistique**.
- **GO 3** : **photo instantanée** d'un carnet périsable ; **le carnet affiché n'est pas
  exécutable** ; aucune mesure d'impact réel (le moteur est en paper) — c'est le **prochain
  chantier**, et il commence par **accumuler** la sonde.

**État vérifié** : moteur **pid 97897 vivant** · **pnl 42,1679 $ / 9 pos / 175 trades** ·
veilleuse **STABLE (exit 0)** · `controle_config` **conforme (0 anomalie bloquante)** ·
**0 traceback** · **0 ordre, 0 €**.

**Livré** : `hulk-mexc/scripts/verif_seuil_moteur.py` (garde-fou + autotest) ·
`chiffrage_sortie_paire.py` (GO 1) · `chiffrage_pump_manque.py --cadences` (GO 2) ·
`sonde_profondeur_carnet.py` (GO 3) · `chiffrage_entree_sortie_replay.py` **corrigé** (le terme
cadence manquait dans 3 calculs) · `runs/{SEUIL_MOTEUR,CADENCES_PAR_PAIRE_20260923,
REPLAY_EDEL_SEUIL_REEL_20260923,PROFONDEUR_CARNET_20260923}.*`.

---

## 5. DEUXIÈME VAGUE (GO 1,2 + consultation de la FAMILLE)

### GO 1 — LE GARDIEN EST VISIBLE (et l'écart de scellés est DÉCLARÉ)

- **`git_push_auto.sh`** appelle désormais le garde-fou **toutes les 3 h** (bloc `1octies`,
  même style que les autres organes ; sortie non nulle → ligne `ALERTE` dans le journal).
- **`gen_cockpit_vol.py`** gagne le gardien **« Garde-fou seuil moteur »** : il affiche
  `6/6 refus chiffrés confrontés`, signale tout instrument qui recalcule un seuil sans la
  cadence, et **refuse d'être un feu vert si l'état est figé (>8 h)** ou si le refus parlant
  n'a pas encore 5 lignes (EN ATTENTE, normal < 1 h après une relance). **13 gardiens**
  au cockpit (12 avant).
- **L'écart de scellés, PROUVÉ ET DÉCLARÉ** : mes deux modifications légitimes
  (`paper_diprip.py` = refus parlant ; `chiffrage_entree_sortie_replay.py` = terme cadence)
  faisaient crier R5/R13 (« md5 différent »). **La maison a raison de crier** : un scellé ne
  s'écrase pas en silence. Traitement : `declarer_rescel_20260923.py` (backup horodaté +
  entrée `_rescel_20260923` qui **dit ce qui a changé et pourquoi**) → **écarts md5 = 0**,
  **5 nouveaux instruments ajoutés au registre** (123 entrées).
- **UN TROU RESTE, ET IL FAUT UN GO POUR LE FERMER** : le drill signale
  `hulk-mexc/scripts/verif_seuil_moteur.py` **non versionné (git)** — « un Mac mort le
  perdrait et la boucle ne redémarrerait pas ». Le dépôt a une règle explicite : `git_push_auto.sh`
  ne committe QUE les fichiers déjà suivis. **Il faut un `git add` + commit de mon côté
  (acte git = GO) ** — je ne le fais pas sans ton accord.

### GO 2 — LA SÉRIE DE PROFONDEUR EST OUVERTE (une photo ne suffit pas)

`sonde_profondeur_carnet.py --serie` écrit un instantané JSONL, `--serie-analyse` sort les
**médianes**. 4 passages × 8 paires = **32 lignes** (fenêtre de ~1 min) :

| paire | méd absorbable < −0,5 % | méd < −2 % | spread méd | plafond actuel méd | plafond / profondeur |
|---|---|---|---|---|---|
| **RIZE** | **458 $** | **604 $** | **64,6 bps** | 15 936 $ | **2 641 %** |
| TEL | 200 $ | 3 757 $ | 38,3 bps | 487 089 $ | 12 967 % |
| ZBCN | 1 159 $ | 2 448 $ | 16,6 bps | 11 395 604 $ | 467 342 % |
| RWAINC | 1 161 $ | 4 775 $ | 5,4 bps | 20 020 $ | 419 % |
| EDEL | 50 $ | 983 $ | 16,5 bps | 2 001 $ | 210 % |
| CHIP | 71 758 $ | 84 264 $ | 19,6 bps | 13 075 $ | **15,0 %** |
| BIO | 10 347 $ | 11 826 $ | 15,1 bps | 2 628 $ | **22,3 %** |
| BTC | 2,76 M$ | 7,80 M$ | 0,0 bps | 0,46 $ | 0 % |

**Le spread mesuré de RIZE est de 64,6 bps** — 13× le coût supposé par le moteur (5 bps),
**sur les deux côtés** : à elle seule, cette mesure explique une partie de ce que « la sortie »
coûte. Et la **stabilité à 1 min est bonne** (min-max < 100 %), mais **1 min n'est pas une
série** : la règle de taille attendra des heures de mesures, ou elle n'existera pas (R17).

### GO 3 — LA FAMILLE A JUGÉ, ET SON VERDICT EST PLUS DUR QUE LE MIEN

4 modèles consultés (`consulter_famille_garde_fou_seuil_20260923.py`), brief conçu pour la
**contradiction**, pas l'approbation. **Unanimes : « insuffisant mais utile »** (70-80 % de
confiance). Détail complet et traitement :
`Index_Maison/scripts/CONSULTATION_FAMILLE_GARDE_FOU_SEUIL_20260923/SYNTHESE.md`.

**Trois objections traitées DANS LA JOURNÉE :**
1. *« Le gardien suppose la config statique »* (Gemini, Nemotron) → **empreintes md5** de la
   config et des profils dans l'état + **cri de dérive** (avec l'avertissement qui compte :
   si le moteur n'a pas été relancé, un désaccord serait **légitime** — anciens paramètres).
2. *« Aucune preuve de son taux de faux négatifs »* (Nemotron) → autotest devenu une
   **batterie de 5 troncatures × 3 régimes** ; **7/7 erreurs discriminantes détectées (100 %)**,
   et il **refuse de compter comme échec un cas non discriminant**. Cet autotest **m'a attrapé
   moi-même** : il criait « cassé » sur des injections qui n'étaient pas des erreurs au point
   testé.
3. *« Aucun slippage : vos gains sont surévalués »* (Gemini, Grok, DeepSeek) → **mesuré** :
   `REPLAY_SLIP_BPS` de 0 à 40 bps. E0+X4 −3,93 → **−6,79 $** · E2+X2 +59,42 → **+48,86 $**
   à **45 bps/côté**, 1re moitié **+13,31 $** (positive) ⇒ **le levier tient au coût réel**,
   mais **la règle actuelle, elle, y perd** (beaucoup de petits trades).

**Deux objections NON traitées, et je les déclare en tête plutôt qu'en bas :**
- **Biais de source unique** (Grok) : mon invariant prouve la **cohérence**, pas la
  **justesse** — si le moteur applique une formule fausse, mon gardien la valide. Il faut un
  **oracle indépendant** (rejeu de la kline brute vs signal enregistré). **À GO.**
- **Aucun test en marché baissier** (les **quatre**) : 90 j de klines et 21 j de run dans **un
  seul régime haussier**. Aucun de mes chiffres ne dit ce que la règle fait quand tous les
  « dips » sont des couteaux qui tombent. **À GO.**

**Priorité : ils ne sont pas d'accord** (Gemini/DeepSeek : la taille · Nemotron : le seuil ·
Grok : le stop). Je ne tranche pas à leur place : leur désaccord **dit** que les trois ne sont
pas assez mesurées pour être priorisées objectivement — et c'est **(A), le stop**, qui
**détruit du capital** (−4,19 $ d'exits dégradés contre +3,06 $ de gains sur RIZE) alors que
(B) et (C) ne font que manquer ou sous-utiliser.
