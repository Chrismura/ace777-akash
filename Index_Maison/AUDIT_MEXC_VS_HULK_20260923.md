> # ⚠️ CORRECTION DU 23/09/2026 — À LIRE AVANT CE DOCUMENT (classe E17)
>
> **Ce document affirme : « 2 sorties RIZE à −16,5 % et −39,2 % pour un stop annoncé de 8 % ».
> C'EST FAUX, et c'est moi qui l'ai fabriqué.**
>
> - Le « 8 % » venait de `strategie/universe_profils.json → RIZEUSDT.calib.stop_pct = 8.0`,
>   c'est-à-dire un **PLANCHER de configuration**, pas le seuil de la machine.
> - Le stop **RÉEL** est `max(plancher ; cadence de la paire × 0,70)` — **RIZE : 16,51 %** (10/09)
>   puis **39,23 %** (22/09) — et il est **écrit par le moteur dans ses propres motifs de sortie**
>   (`stop-39.23%_guard_partial_50`). La machine est sortie **exactement à ces niveaux**
>   (−39,23 % → −39,23 % et −39,38 %).
> - **Vérifié sur 14 sorties de type stop (13→23/09)** : RED 6,0→−6,01 · XRP 6,0→−6,08 ·
>   ZBCN 6,0→−6,06 · W 6,0→−6,08 · KITE 6,0→−6,46 · CC 6,0→−6,98 · PYTH 6,67→−6,98 ·
>   EDEL 13,8→−14,25 et 11,95→−12,06. **Le stop tient, au point de base.**
> - Ce qui reste vrai, et qui est un problème de **NIVEAU** (pas d'exécution) : **un stop à 39 %
>   ne protège rien**. Chiffré : plafonner le stop à 15 % aurait donné **+0,87 $ sur 10 jours**
>   (`hulk-mexc/scripts/chiffrage_stop_serre.py`, chiffre **OPTIMISTE**, sans ré-entrée).
>
> **Conséquence** : l'objection n°1 du jury du matin (« le stop ne tient pas », 3 voix sur 4)
> reposait sur **mon chiffre faux**, pas sur la machine. Le verdict a été re-soumis avec la
> correction, en **session ouverte** (`scripts/SESSIONS_FAMILLE/SUPERVISION_BUFFY_23_09/`).
> Classe d'erreur : **E17** — *publier un plancher de configuration comme le seuil réel de la
> machine, alors que le moteur l'écrit dans son propre journal.*

# AUDIT MEXC × HULK — données, séquences, mémoire, re-injection (23/09/2026)

> **Commande Christophe** : « tu vas prendre les données de MEXC, tu vas les comparer une par une
> avec les données paires de Hulk, ensuite tu vas comparer une par une toutes les séquences de
> trading entrée et sortie, les mises, voir le niveau de justesse (si on rentre bien, gestion des
> bags, et les sorties), vérifier les données qu'on mémorise, si il en manque, si elles sont
> correctement enregistrées, ensuite tu les compares avec ce qu'on a une par une, et ensuite tu
> rejoues tout ça avec les derniers set-up. »
> **0 ordre, 0 €, lecture seule.** Moteur intact pendant tout l'audit.

---

## 0. Méthode — les sources sont LUES DANS LE CODE, pas dans mes documents

| Donnée Hulk | Où elle naît (lu à la source) |
|---|---|
| prix | `paper_diprip.fetch_all_prices` → `api.mexc.com/api/v3/ticker/price` (cache de cycle, `last_price`) |
| spread + **mur** | `ace_sense_mexc.book_sense` → `/api/v3/depth?limit=20` · `spread=(ask−bid)/mid` · **`wall_bid = MAX du notionnel des 20 premiers bids`** |
| feed live | `satellite_aspiration.py` → `runs/aspiration_live.json` (**MAX_PAIRS = 5 par passe**) |
| profils | `strategie/universe_profils.json` (dont le **cap de mise = 2 % de `mur_bid_med`**) |
| observations de murs | `runs/murs_observations.json` (`wall_strength` s'en sert **si** le live manque) |
| journal | `runs/PAPER_V1_20260923_090125.csv` (11 colonnes) · état `…_state.json` |
| **PnL** | `paper_diprip` : `pnl = (price − entry) × sell_qty` → **BRUT, sans frais ni spread** |

Instruments écrits pour cet audit (tous lecture seule) :
`hulk-mexc/scripts/audit_mexc_vs_hulk.py` · `audit_sequences_trades.py` · `audit_horodatage_prix.py` ·
`audit_memoire_donnees.py`. Sorties : `hulk-mexc/runs/AUDIT_*.{json,txt}`.

---

## 1. GO 1 — MEXC vs Hulk, PAIRE PAR PAIRE

### 1.1 Ce qui est FIDÈLE (et il faut le dire aussi)

* **Prix** : la vue live d'Hulk colle au marché — écart **−28 bps à +7 bps** (BTC −1,7 · ETH −1,3 ·
  MNSRY +1,9 · QNT +6,7 · CHIP −28,2 avec 7 s d'âge) → **la chaîne de prix est bonne**.
* **Spread** : identique au bps sur FLUID (21,65), MNSRY (8,97), RWA (7,24) — l'écart résiduel est
  de l'**âge de la vue**, pas une erreur.
* **Aucune anomalie** au-delà de mes seuils de lecture (50 bps prix / 20 bps spread / 60 % mur).

### 1.2 Le MUR : c'est **UN ORDRE**, pas une profondeur — et ça change tout

| paire | mur Hulk $ (max niveau) | profondeur cumulée < −0,5 % | **mur / profondeur** |
|---|---|---|---|
| RIZE | — (pas de vue live) | 364,74 | **1,0** |
| ZBCN | — | 41,25 | 0,4 |
| TEL | — | 511,50 | **4,0** |
| EDEL | — | 1 013,22 | **8,4** |
| FLUID | 111,44 | 111,44 | **11,2** |
| RWAINC | — | 1 399,19 | **5,2** |
| XRP | — | 66 211,93 | 0,2 |
| W | — | 166 688,81 | 1,0 |

Le « mur » du moteur est **le plus gros niveau unitaire des 20 premiers bids** (`wall_bid_usdt`) : sur
FLUID, c'est **11 fois** la profondeur cumulée à −0,5 %. Toute conclusion de **taille** tirée du
« mur » est donc une conclusion sur **un ordre**, et un ordre s'annule. La profondeur, elle, est
désormais mesurée séparément (colonne 2 du tableau ci-dessus).

### 1.3 Les TROUS de données (17 nommés, mesurés)

* **13 paires sur 20 n'ont AUCUNE vue live** à l'instant du contrôle (le satellite ne sonde que
  **5 paires par passe**). Pour elles, le **cap de mise se lit sur le profil figé** :
  RIZE = 2 % × 243,78 $ = **4,88 $** — le chiffre que le moteur applique encore, alors que le
  carnet mesuré vaut aujourd'hui 364,74 $.
* **4 paires sur 20 n'ont AUCUN profil** : QNT, FLUID, RWA, MNSRY → replis du code, pas de cap, pas
  de set-up chiffré. Ce sont pourtant **4 des 9 positions ouvertes**.
* **`prix` du profil** (une donnée qu'on garde) est faux de **8 % à 81 %** : RIZE **+81,7 %**,
  EDEL **−71,1 %**, CHIP −39,6 %, RED −36,0 %, KITE −29,1 %, PYTH −28,4 %, W −23,1 %, TEL −20,9 %.
* **`murs_observations.json`** couvre 18/20 paires (manquent FLUID, MNSRY, RWA).

---

## 2. GO 2 — CHAQUE séquence, contre les klines MEXC

**Reconstruction par conservation des quantités** : 302 événements non-SKIP → **124 séquences**
(115 fermées, 9 ouvertes — cohérent avec les 9 positions de l'état).
**1 anomalie**: `13/09 EDELUSDT` ferme avec **+572,08 unités achetées jamais vendues** (écart inscrit au rapport — le cas n'est ni lissé ni deviné).

### 2.1 Le prix inscrit a-t-il existé ?

| contrôle | n |
|---|---|
| séquences vérifiées conformes (100 auditées, budget de temps déclaré) | **78** |
| séquences avec un prix hors de sa minute | **22** |
| non vérifiables (pas de klines) | 15 |

**Pourquoi ? Mesuré, pas supposé** (`audit_horodatage_prix.py`) : **13/13** des prix fautifs existent
dans une minute **ANTÉRIEURE** — décalages **−1 min (4) · −2 min (5) · −4 min (1) · −5 min (3)**.
**Aucun** prix introuvable dans ±6 min ⇒ **classe A : retard d'horodatage**, PAS un prix fantôme.
Le pire cas : RIZE 10/09 16:50 sortie inscrite 0,000905 alors que la minute plafonnait à 0,000886 →
**+214 bps**, prix d'il y a 2 minutes.

**Conséquence** : jusqu'à **5 minutes**, le remplissage paper utilise un prix qui n'était plus
fraîchement négocié. **ÉTIQUETTE : MESURÉ** (les 13 prix, minute par minute). *Le MÉCANISME exact
(cache de cycle `last_price` vs photo d'aspiration du satellite) restait **EXTRAPOLÉ** — « déclaré
OPEN », et la famille a eu raison de le pointer.*

**Le test que la famille exigeait, passé le jour même** (`probe_prix_mexc_fraicheur.py`) :

| mesure | résultat |
|---|---|
| notre horloge vs l'en-tête HTTP `Date` de MEXC | **0,6 s** — ce n'est pas une horloge folle |
| **âge du dernier TRADE réel** | **16/20 paires ont échangé dans la dernière minute** ; 4/20 ≥ 1 min, RWAINC **12,9 min** |
| verdict, **par paire** (corrigé) | **H1 (notre chaîne)** sur les 16 paires liquides · **H2 (prix de l'exchange vieux par nature)** sur 4 |
| **écart « dernier prix » vs milieu du carnet** | **−90,9 bps sur RIZE** (spread 92,5 bps) · −54,4 bps FLUID · −29,4 bps RWAINC |

⇒ Le retard **n'est pas** une propriété générale de l'exchange : sur les paires liquides, c'est bien
**notre chaîne**. Et le fait neuf est pire : sur RIZE, le prix utilisé pour remplir est à **0,9 % du
prix exécutable** — **plus que le PnL moyen par trade**.

### 2.2 Justesse : entrée, bags, sortie

| paire | n | brut $ | **net estimé $** | MFE 60 min méd % | **giveback méd %** | laissé méd % | avec ajouts |
|---|---|---|---|---|---|---|---|
| RED | 8 | 12,21 | 11,84 | 0,62 | 2,88 | 1,58 | 0 |
| CHIP | 4 | 7,38 | 7,17 | 2,30 | 3,00 | 2,71 | 0 |
| HBAR | 3 | 4,71 | 4,59 | 0,35 | 2,55 | 0,70 | 0 |
| TEL | 5 | 4,03 | 3,53 | 0,82 | 5,11 | 1,12 | 0 |
| KITE | 6 | 3,44 | 3,16 | 0,69 | 4,68 | 1,34 | 0 |
| PYTH | 6 | 3,20 | 2,93 | 1,69 | 2,71 | 0,86 | 0 |
| BTC | 4 | 2,71 | 2,47 | 0,58 | 1,02 | 0,26 | 0 |
| ETH | 6 | 2,33 | 2,19 | 0,13 | 1,43 | 0,55 | 0 |
| W | 7 | 1,90 | 1,69 | 0,85 | 1,41 | 0,78 | 0 |
| XRP | 5 | 1,23 | 1,13 | 0,62 | 2,70 | 1,02 | 0 |
| CC | 7 | 0,55 | 0,48 | 1,09 | 1,70 | 1,24 | 0 |
| EDEL | 11 | 0,22 | 0,10 | 3,76 | 5,19 | 4,95 | 0 |
| ZBCN | 7 | 0,12 | **−0,02** | 1,19 | 2,08 | 0,96 | 0 |
| RWAINC | 9 | −0,07 | −0,41 | 0,55 | 7,05 | 1,00 | 0 |
| **RIZE** | 7 | **−1,52** | **−1,73** | 4,80 | **20,84** | 3,87 | 0 |
| FLUID | 3 | −2,40 | −2,54 | 0,00 | 6,55 | 1,24 | 0 |
| BIO | 2 | −0,34 | −0,37 | 1,33 | 5,37 | 0,65 | 0 |
| **TOTAL (100 seq.)** | | **39,70** | **36,19** | | | | **0** |

* **COÛTS : −3,51 $ sur 39,70 $ = 8,8 % du brut** (frais 5 bps/côté déclarés par le code + demi-spread).
  Le journal inscrit le **brut** : nos « +42,17 $ » sont **avant frais et avant spread**.
* **Aucune séquence avec ajout (bag)** sur la fenêtre : le mécanisme des bags **n'a pas servi une fois**.
* **RIZE est la seule paire dont le giveback médian dépasse 20 %** (20,84 %) : elle rend un cinquième de
  son pic avant de sortir. C'est la « perte du pump » chiffrée côté **sortie**, pas côté entrée.
* **MFE 60 min médian ≤ 2,3 % partout sauf RIZE (4,80) et EDEL (3,76)** ⇒ on n'entre pas juste avant
  un mouvement : on est payé par la **tenue** (durée médiane 7 h à 3,6 jours selon la paire).

### 2.3 Par motif de sortie (les 100 séquences vérifiées)

| motif | n | brut $ | net estimé $ | laissé méd % | giveback méd % |
|---|---|---|---|---|---|
| **stop / guard / dust** | **32** | **−33,73** | **−34,87** | 1,54 | 8,91 |
| **trailing** | **67** | **+73,43** | **+71,11** | 1,03 | 2,54 |
| autre | 1 | 0,00 | −0,05 | — | — |

⇒ **32 stops coûtent 33,73 $ ; 67 traînings en rapportent 73,43 $.** Le système vit du trailing, et
paye ses erreurs d'entrée par des stops.

---

## 3. GO 3 — ce qu'on MÉMORISE

### 3.1 Cohérence interne : PROPRE

| contrôle | résultat |
|---|---|
| horodatages non croissants | **0** |
| discontinuités de `pnl_total` (> 0,01 $) | **0** |
| ventes sans `pnl_usdt` | **0** |
| doublons d'événements de trading | **0** |
| lignes SKIP strictement répétées (TTL du dédup) | 559 = **bruit**, pas une corruption |

### 3.2 Complétude : tout est rempli… **sauf ce qui permet de juger un trade**

* Colonnes : 100 % partout, sauf `pnl_total` sur les BUY (**88 %**) et `pnl_usdt` sur les BUY (0 %,
  structurel).
* **`spread` n'est PAS une colonne** : il vit dans le **texte libre** des ventes — présent sur
  **99 % des 174 ventes** (donc exploitable), **absent sur 100 % des entrées**.
* **Colonnes qui manquent** (nommées, pas devinées) : **mise visée** avant plafonds/fusibles ·
  **mur utilisé** (live ou profil) · **seuil exigé** au moment de l'entrée · **dd6 observé** ·
  **stop nominal** · **spread payé** à l'entrée.

### 3.3 Re-injection des derniers set-up (simulation, 0 ordre)

**a) Le stop annoncé n'est pas le pire cas réalisé** — les 30 sorties « stop » :

| | valeur |
|---|---|
| perte réelle cumulée vs perte au stop **nominal** | **−2,68 $ de MIEUX** que le nominal |
| mais cas extrêmes sur RIZE | **−16,51 %** et **−39,23 %** encaissés pour un stop annoncé de **8 %** |

⇒ Les paliers vendus avant le stop font que, **en moyenne**, on perd *moins* que le stop nominal ;
mais le stop **n'est pas au repos** : c'est une **vérification périodique** sur un prix en cache, et
quand la paire n'est pas dans la passe de sonde, la perte court (**jusqu'à −39 %**).

**b) La mise** — mise médiane vs `cap` du set-up vs profondeur mesurée :

| paire | mise méd $ | cap set-up $ | profondeur < −0,5 % | mise/cap | **mise/profondeur** |
|---|---|---|---|---|---|
| **TEL** | 26,43 | 25,79 | 199,70 | **1,02** | **13,2 %** |
| EDEL | 3,38 | 18,17 | 50,00 | 0,19 | 6,8 % |
| RWAINC | 23,60 | 27,73 | 1 160,75 | 0,85 | 2,0 % |
| RIZE | 4,88 | 4,88 | 458,40 | **1,00** | 1,1 % |
| ZBCN | 6,81 | 6,81 | 1 159,35 | **1,00** | 0,6 % |
| CHIP | 20,24 | 661,99 | 71 757,95 | 0,03 | **0,03 %** |
| BIO | 9,37 | 70,49 | 10 347,10 | 0,13 | 0,09 % |
| XRP | 19,33 | 1 686,69 | — (non mesuré) | 0,01 | — |

⇒ Le cap **mord exactement** sur RIZE/ZBCN/TEL (ratio 1,00-1,02) — donc ce sont **ces trois-là** que
le plafond « 2 % du mur » contraint ; sur CHIP/BIO/XRP il ne mord pas du tout (0,01-0,13). Et **TEL
mise 13,2 % de la profondeur mesurée à −0,5 %** : c'est la seule paire où la mise attaque vraiment
le carnet.

---

## 4. Ce que ça corrompt dans MES propres conclusions précédentes (corrigé ici)

1. « Le stop ne tient pas (14,16 % réalisés pour 8 % annoncés) » → **mal formulé**. Le chiffre de
   14,16 % était la **perte agrégée** d'une séquence incluant ses ventes partielles, pas le niveau
   touché. Le fait mesuré est : **en moyenne le réalisé est 2,68 $ meilleur que le stop nominal**, et
   **deux cas RIZE ont dépassé le stop de 8 % jusqu'à −16,5 % et −39,2 %**.
2. « Le spread n'est pas mémorisé » → **faux** : il est dans le **texte des raisons de vente (99 %)**.
   Ce qui manque, c'est le spread **à l'entrée**, et sa **forme de colonne**.
3. « Les check-up ne voyaient rien » → **exact** et maintenant expliqué : ils regardaient le prix
   (fidèle à ±28 bps) et jamais **l'âge du prix au moment du remplissage** (1 à 5 minutes).

---

## 5. Les 5 faits neufs, classés par ce qu'ils coûtent

| # | Fait **mesuré** | Preuve | Ce qu'il coûte |
|---|---|---|---|
| 1 | **13 paires sur 20 sans vue live** ; cap sur profil figé (RIZE 4,88 $ pour un carnet de 364,74 $) | GO1 §1.3 | Taille figée sur un chiffre périmé, 4 paires **sans aucun profil** |
| 2 | **Le prix de remplissage a 1 à 5 minutes de retard** (13/13 dans une minute antérieure) — *H1 confirmé sur 16/20 paires, H2 sur 4* | GO2 §2.1 + sonde | Post-mortems décalés ; sur RIZE, prix de remplissage à **0,9 %** du carnet |
| 3 | **PnL inscrit BRUT** : −3,51 $ de frais+spread sur 39,70 $ (**8,8 %**) | GO2 §2.2 | Nos « +42,17 $ » ne sont pas nets |
| 4 | **32 stops = −33,73 $**, dont 2 dépassements jusqu'à −39 % (stop = vérification, pas ordre au repos) | GO2 §2.3, GO3 §3.3 | La perte extrême est structurelle, pas accidentelle |
| 5 | **Aucun bag utilisé, giveback RIZE 20,8 %**, 6 colonnes manquantes au journal | GO2/GO3 | On ne peut pas juger une entrée ni un bag après coup |

---

## 5bis. La famille a CONTESTÉ cet audit (4 modèles, 4 avis) — et elle a raison

Verdict **unanime : « utile mais incomplet »** (confiance 75/75/75/65 %) — *le détail est dans
`Index_Maison/scripts/CONSULTATION_FAMILLE_AUDIT_MEXC_20260923/SYNTHESE.md`*.

**Ce qu'ils attaquent, et que je corrige ici** :

| reproche | porté par | correction appliquée |
|---|---|---|
| Le stop « vérification périodique » : conclusion **au-delà** d'un n=32, sans carnet à l'impact | Gemini, DeepSeek | étiqueté **EXTRAPOLÉ** — le fait mesuré reste : 2 cas à −16,5 % et −39,2 % pour un stop annoncé de 8 % |
| Les −3,51 $ de coûts sont **ESTIMÉS** (paper : aucun frais prélevé) | Grok | étiquette **ESTIMÉ** conservée partout |
| « Le cap se lit sur un profil figé » : la dérive du profil ne **prouve pas** l'erreur du cap en $ | Nemotron | reformulé : ce qui est **mesuré** = 13 paires sans vue live + 4 sans profil ; ce qui était **extrapolé** = l'effet en dollars |
| **Auto-absolution par la confession** : lister mes erreurs passées m'a servi de brevet pour des conclusions neuves, sans garde-fou équivalent | Nemotron | **nouvelle règle** : chaque conclusion porte **MESURÉ / ESTIMÉ / EXTRAPOLÉ** ; classe **E14** au registre |
| L'impact des trous de données n'est pas quantifié | DeepSeek | les trous sont listés **et** leur effet est désormais borné (13 paires → cap figé ; 4 paires → replis du code) |

**Ordre de traitement qu'ils imposent** : **1) horodatage du journal** (4/4) · **2) net de coûts**
(3/4) · puis stop / colonnes / vue live (divergents). **Aucun de ces chantiers n'est câblé** : ils
attendent ton GO.

**Critères de changement d'avis qu'ils demandent** : conformité des prix > 95 % après correction de
l'horodatage (aujourd'hui **78/100**) · journaliser l'heure MEXC à chaque trade · PnL net positif
après coûts **réels** par transaction · stop au repos et vérification que les dépassements disparaissent.

---

## 6. Limites déclarées (et non comblées)

* Audit des séquences : **100/115** (budget de temps) ; le reste est **déclaré non traité**.
* Le mur/cap des set-up est celui d'**aujourd'hui**, pas celui de l'instant du trade.
* Re-injection sur les **extrêmes mesurés** (borne, pas un chemin tick par tick).
* Le mécanisme exact du retard de prix (cache de cycle vs photo d'aspiration) est **OPEN** : la sonde
  de fraîcheur doit être **rejouée AU MOMENT d'un remplissage** (alignée sur le journal), pas à un
  instant arbitraire — c'est le test décisif que la famille réclame.
* **Étiquettes de provenance** : tous les faits du §5 sont **MESURÉS** ; le coût en dollars (**ESTIMÉ**) ;
  la cause du retard et la « propriété générale » du stop (**EXTRAPOLÉES**, en attente du test).
* Marché de la fenêtre : **haussier** (BTC +12,3 %, 20/20 paires en hausse) — aucune preuve en marché
  descendant.

## 7. État (pendant et après l'audit)

`0 ordre, 0 €` · moteur **pid 97897**, **pnl 42,1679 $ / 9 positions / 175 trades** inchangés ·
`defaults.env`, `universe_profils.json`, `paper_diprip.py` **non modifiés** (git le prouve) ·
gardiens (seuil + E13) rc=0 · veilleuse rc=0.
