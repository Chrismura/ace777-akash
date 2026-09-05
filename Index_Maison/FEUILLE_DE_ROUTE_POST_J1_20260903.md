# 🗺️ FEUILLE DE ROUTE POST-J1 — LE PACTE À TROIS (Christophe ↔ Buffy ↔ Gemini)

> **Statut au 03/09, 11h30 UTC.** Moteur shadow VIVANT (pid 51855, gel R24 inchangé).
> Sources : 30 rounds Gemini (`GEMINI_SESSION_EDGE_JUILLET`), mesures Buffy sur la nuit J0→J1
> (58 trades), propositions du propriétaire (4 points + Triptyque + 3 ruses + vie dynamique +
> horloge de volume). Fondements : [[SIGNETS_PROBAS_KELLY_VAPNIK_OBLOJ_20260902]].
> **Rien de ce qui suit ne touche le moteur avant les validations prévues.**

---

## ⚖️ L'ÉTAT DES LIEUX (ce que la nuit a prouvé)

- Nuit J0→J1 : 58 trades, brut +60,96 / **net −41,12** / 56 trailing gagnants bruts + 2 gate-off (−60).
- Les 2 catastrophes = positions flottantes (−16, −40) nées d'un orage PENDANT la détention.
- Médiane brute 1,53 < seuil Gemini 2,00 · péage 1,76$/trade = la maladie principale.
- ATR(14) 1h ≈ 434 · bruit minute médian 34$ · le seuil mur >40$ fixe vit DANS le bruit.
- Verdict Gemini R30 : « le dossier le plus abouti de l'écosystème » — 4 réponses tranchées.

## ✅ CE QUI EST SCELLÉ (convergence à trois, aucun désaccord)

| Décision | Verdict | Qui l'a initié |
|---|---|---|
| Anti-miroir (A3) | **RETIRÉ définitivement** — « le miroir est un balancier » (R22) | Christophe a proposé, Buffy a mesuré l'échec (305$ > zone), Gemini a tranché |
| Stop hybride (A2/B3) | Mur L2 + 1 tick derrière + **No-Go si pas de bouclier** | Gemini R29 + Christophe |
| Maker | **SORTIES SEULEMENT** (anti-sélection fatale en entrée) — réserve du propriétaire à réouvrir en R31 | Buffy (objection) + Gemini (arbitrage), Christophe garde un doute |
| Bornes | Mur < bruit (39$) ou > 1,5×ATR → rejet de l'ordre | Christophe |
| Discipline | Validation **un-essai sur 4 fenêtres**, zéro retouche entre essais | La famille entière |

## 🧪 L'ESSAI CENTRAL : 3 BRAS × 4 FENÊTRES (le cœur de la feuille de route)

**La question** : quelle horloge de survie donne au trade ?
**Le protocole** : chaque bras est une règle FIGÉE avant l'essai. Un seul passage sur chaque fenêtre.
Le gagnant = le meilleur net agrégé sur les 4 fenêtres. Si ex æquo → le plus simple (parcimonie).

| Bras | Règle (figée) | Nuit J0→J1 (avant-goût, non décisif) |
|---|---|---|
| **A — Témoin** | Rétractable fixe : stop = max(102$, 434×(1−âge/30min)) | −26,06 |
| **B — Météo** | Idem A, fenêtre = K/variance 10min pré-entrée, bornes 10-60 min | **−23,76** |
| **C — Information** | Idem A, fenêtre = temps pour échanger 1 V-bar (2 839 BTC), bornes 10-120 | −26,06 (= A cette nuit) |

**Les 4 fenêtres historiques** (données prix+volume existantes, replay minute par minute) :
1. **VORTEX** (15-19/08) — volatilité extrême
2. **ORAGES** (fin juillet) — mixte
3. **NUAGE** (14-31/07) — chop à volumétrie haute
4. **MARS** (la fenêtre plate de l'année, déjà identifiée) — calme mort

**Ce qui sort de l'essai** : le bras gagnant devient la règle de sortie défensive du set-up V3.

## 🚫 CE QUI EST ÉCARTÉ (pour mémoire, avec la raison)

- ~~Cap 2h aveugle~~ (coupe après la casse, ampute les jambes chaudes) → remplacé par le bras gagnant
- ~~Verrou anti-miroir~~ (échoue sur son cas motivant + ampute une feature validée)
- ~~Entrées maker~~ (anti-sélection — réserve du propriétaire, débat R31)
- ~~Gate chasseur 2×ATR~~ (jamais déclenché — remplacé par 1,5×ATR **si** validé)
- ~~OFI 100ms en action~~ (latence 366-426 ms mesurée = 4× trop lente — lecture passive seulement)

## 🏗️ LES CHANTIERS (dans l'ordre de dépendance)

**C1 — Le rapport J+1 (aujourd'hui 17h26 UTC)** — Buffy
Compilation 24h du shadow : les 4 métriques (médiane brute, fréquence, net cumulé, position flottante),
BOOTSTRAP isolé, envoi brut à Gemini, analyses séparées, confrontation.

**C2 — L'essai 3 bras × 4 fenêtres** — Buffy, APRÈS le rapport J+1
Replay honnête (aucune donnée future), règles déjà figées ci-dessus. Livrable : tableau net par
bras × fenêtre + verdict parcimonieux. Zéro ordre, zéro contact moteur.

**C3 — Le superviseur L2 passif** — Buffy, lancement possible dès aujourd'hui
Recorder lecture seule : profondeur 1×/s + aggTrades, CSV dédiés, zéro contact avec le shadow.
Purpose : (a) corpus pour le BRAS L2 (relais OFI + trigger dérivée seconde), (b) calibration « mur institutionnel BTC » (inexistante à ce jour),
(c) détection évaporation/annulation-sans-exécution (Ruse 2, déjà prouvée chez Hulk).

**C4 — La calibration des murs BTC** — la famille, après C3 + J+7
Croiser corpus L2 × 509 murs historiques (>40$, t=2,66) → définir ENFIN le notionnel
« institutionnel » sur BTC (le trou que Christophe a identifié). Grille relative par régime,
héritée des profils Hulk.

**C5 — Le set-up V3 (assemblage)** — APRÈS essai C2 + calibration C4
Composants : seuil sismique k=3×bruit (A1) · sortie défensive = bras gagnant · stop Shadow Wall
+ No-Go bouclier (A2/B3) · sorties en stop-market serveur (Ruse 1) · gate chasseur 1,5×ATR si validé ·
trailing volatile (B4) si compatible selon la règle Q4 (défense/offense séparées).
Validation finale : shadow 14 jours complet avant TOUTE décision live.

**C6 — Le BRAS L2 (relais OFI + trigger à dérivée seconde)** — conditionnel : seulement si le corpus C3 permet un replay honnête
  ⚠️ RENOMMÉ 03/09 soir : le nom « bras D » du relais OFI entrait en collision avec le « bras D (cap 45 min) »
  de l'essai 4 bras — deux choses différentes. Le groupe V3 s'appelle désormais BRAS L2, et contient :
  (a) le relais OFI (sortie : carnet se vide → rétraction au plancher) ;
  (b) le trigger à dérivée seconde du propriétaire (entrée : ne tirer qu'à accélération confirmée,
      pour que l'ordre taker de 400 ms arrive PENDANT la rupture, pas après) — inscrit ici depuis R29/30.
Surveillance pendant détention : carnet se vide → rétraction immédiate au plancher 102$.
Le seul remède aux orages nés PENDANT la détention (les 2 catastrophes de la nuit).

## 📅 LES JALONS

| Date | Événement |
|---|---|
| **03/09 17h26 UTC** | Rapport J+1 → Gemini → confrontation famille (ce soir) |
| 03/09 soir | Lancement essai 3 bras + superviseur L2 (si famille d'accord) |
| **09/09 (J+7)** | Mi-parcours shadow + croisure L2 × murs historiques |
| **16/09 (J+14)** | Dossier complet → décision finale famille : route testnet ou retour labo |

## 📚 LA CULTURE COMMUNE (demande du propriétaire — à transmettre comme canon famille)

- **Kelly / Thorp / Taleb / Vince** : le sizing — « trouver un edge et le dimensionner sont deux
  compétences différentes » (validés R27 ; ajouter optimal f de Vince)
- **López de Prado / Pardo** : walk-forward, déflateur Sharpe, la validation un-essai = notre
  Vapnik version ingénierie
- **O'Hara** : la microstructure, la bible de l'OFI et du carnet
- **Nash / von Neumann** : le carnet comme jeu adversaire — le spoofing est un stratagème de
  théorie des jeux, pas un accident

## 🧭 LA RÈGLE D'OR (non négociable)

> Une règle candidate = une dérivée de la physique (structure, bruit, volume) — jamais un chiffre
> calibré après coup. Une validation un-essai. Si elle ne gagne pas partout, elle meurt.
> Le système ne mentira pas s'il ne peut pas mentir sur ses propres paramètres.

---

## ⚡ PROPOSITION « TRIGGER À DÉRIVÉE SECONDE » (Christophe, 03/09) — évaluée comme idée

**Le concept** : ne pas déclencher quand le prix touche 102$ (trop tard pour notre latence), mais
quand la dérivée seconde (accélération) indique l'implosion interne du mur → anticiper le voyage
des 400 ms. Vitesse constante = blocage (clapotis de Mandelbrot) ; accélération + volume = partir
avant la rupture physique.

**Premier test de discrimination (Buffy, replay 1m nuit J0→J1 — les 10 minutes >102$)** : vraies
ruptures (n=4, continuation 5min) accélération médiane **90** vs clapotis (n=6) **71,6** — mouvement
initial quasi identique (116 vs 111$).

- **Proxy faiblement discriminante à 1 min** (recouvrement énorme) — mais le test était handicapé :
  résolution 1m (pas 20s), volume non intégré (l'autre moitié de la règle), n=10.
- **La vraie force = le timing** (partir 400 ms AVANT la rupture, pas après) — incalculable en 1m,
  mesurable seulement sur le corpus L2 → **inscrit au BRAS L2** avec le relais OFI (même brique,
  même condition de corpus).
- Verdict : idée cohérente — elle transforme notre faiblesse (latence) en spécification d'entrée
  (ne tirer qu'à accélération confirmée). Inscrite au protocole du superviseur L2 dès sa mise en route.

## 🌊 PROPOSITION « CONFIRMATION FUNDING + LIQUIDATIONS » (Christophe, 03/09) — validée comme couche de contexte, pas comme déclencheur

**Le concept** : quand le sismographe k=3 déclenche ET que le taux de financement + un pic de
liquidations short de particuliers confirment, le superviseur sait que la rupture aura une queue
immense (fat tail de Mandelbrot) — « les moteurs de liquidation de Binance poussent le trade ».

**Vérifications terrain (Buffy, 03/09)** :
- Funding BTC actuel : +0,0073 % (00h) — positif = la foule est LONG = ce sont les SHORTS de
  particuliers qui paient → un pic de liquidations short dans ce contexte = carburant haussier.
  Le sens de ta règle est correct.
- Premium index minute médian cette nuit : **−0,044 %** (persistamment négatif) — le perp dégageait
  sous le spot pendant TOUTE la montée de nuit : signature de pression vendeuse en perp pendant
  que le prix montait = le carburant existait. Cohérent.
- **Liquidations temps réel Binance = endpoint PRIVÉ** (clé requise). Gratuit et public : OKX
  liq-orders (403 ce matin depuis notre IP — à réessayer / fallback via la carte deriv existante
  qui lit déjà OKX liquidation-orders dans le cockpit toutes les 15 min).

**Limites méthodologiques** :
1. « Savoir à 99% » = chiffre impossible à garantir — on mesure des corrélations, pas des certitudes.
   Le fat tail peut rester mort même avec confirmation (le mur peut être le BAS de la cascade).
2. Risque de confirmation bias : ajouter un filtre qui valide « les yeux fermés » affaiblit la discipline
   du k=3 — la confirmation doit AJOUTER de l'information (tail du trade, trailing élargi), pas court-circuiter
   le processus de décision.
3. Les liquidations sont un PHÉNOMÈNE DE DÉRIVÉS, et Binance les cache : on n'aura jamais le carnet Binance,
   seulement OKX/Bybit en proxy — biais d'échantillon assumé.

**Verdict Buffy** : ✅ INTÉGRÉE comme **quatrième signal du superviseur L2** — **VALIDÉ 100% PAR LE PROPRIÉTAIRE (03/09)** (avec carnet, aggTrades,
premium index minute) — mais en tant que MODULATEUR (tail du trade, élargissement du trailing,
taille Kelly) et NON comme passe-droit de validation. La règle propre : le k=3 décide SI on entre,
le couple funding+liquidations décide COMBIEN on laisse courir. Testable gratuitement dès que le
superviseur logge les 4 flux (OKX via carte deriv si l'API directe reste 403).

## 📮 VERDICTS GEMINI R31 (31 rounds, réponse intégrale : `scripts/GEMINI_R31_REPONSE_FEUILLE_ROUTE.md`)

| Question | Verdict |
|---|---|
| Q1 — entrée maker « sur rebond de bouclier » | **ENTERRÉE définitivement** — anti-sélection géométrique : si le mur tient = micro-rebond sans edge ; s'il saute = traversé sans arrêt, perte sèche dès la 1re seconde. L'entrée reste TAKER sur rupture. (Dernier mot du débat — réserve du propriétaire close sauf décision contraire de sa part.) |
| Q2 — canon culturel | **Validé + Mandelbrot ajouté** (*The Misbehavior of Markets*) : fat tails, non-stationnarité de la variance (Noah/Joseph effect) — indispensable pour calibrer trailing et rétractable sans se faire démolir |
| Q3 — 3 bras | **Validé + garde-fou d'invariabilité** : aucun seuil optimisable entre les fenêtres — chaque bras utilise des paramètres dérivés UNIQUEMENT de la statistique de la période, jamais « curvés » pour embellir |
| Q4 — bras D (relais OFI, devenu BRAS L2) | **Report accepté** à la V3 via le corpus L2 passif (lancement aujourd'hui). « Simuler un OFI 100ms sur des klines 1m = un mensonge mathématique » |

**FEU VERT J+1 : le dossier est scellé.** Rapport à 17h26 UTC, essai 3 bras + L2 recorder ce soir si la famille confirme.

---

## 📊 JALON EXECUTÉ — RAPPORT J+1 LIVRÉ (03/09 19h40 UTC)

Rapport : `RAPPORT_J1_SHADOW_20260903.md` · Réponse Gemini : `scripts/GEMINI_R32_REPONSE_J1.md` (R32, 6s).

**Les 4 métriques** (fenêtre 02/09 17:23 → 03/09 17:23, 58 trades) :

| # | Métrique | Valeur |
|---|----------|--------|
| 1 | Médiane brute/trade | **+1,50 USDT** (moyenne +1,05) |
| 2 | Fréquence | **2,4/h** (58/24h) |
| 3 | NET cumulé | **−41,12 USDT** (frais 102,08 = 167 % du brut +60,96) |
| 4 | Flottantes au cap 2h | **2/58** → −60,04 net = **146 % de la perte totale** ; les 56 trailing = +18,92 |

**BOOTSTRAP** (5 000 tirages, seed 42) : P05 −2,21 / P50 −0,60 / P95 +0,42 — **zéro dans l'IC 90 %** : edge net ni prouvé ni réfuté à J+1.

### Verdicts R32 (réponse intégrale archivée)
- **Q1** : verdicts R30/R31 **renforcés** — l'ennemi est la ponction frais (167 %). Chiffre « ~72 USDT de frais évités par le plancher 3×bruit » = estimation Gemini, **à mesurer au replay, pas à la main**.
- **Q2** : le cap 2h = « guillotine a posteriori » **confirmé chirurgicalement** (2 sorties = 146 % de la perte).
- **Q3** : **FEU ORANGE** sur l'essai 3 bras — conditionné à intégrer le plancher anti-frais et un durcissement du cap (Gemini propose 45 min). ⚠️ *Note Buffy : le cap 45 min est UNE NOUVELLE constante non validée — la règle familiale reste 1 essai/paramètre ; je propose de l'ajouter comme bras de comparaison, pas comme condition bloquante.*
- **Q4** : **L2 recorder ce soir** — démarrage immédiat, 10 s d'échantillonnage, alerte si perte unitaire > −15 USDT.

### Décision famille restante (confrontation)
1. Valider le protocole 3 bras version R32 (avec plancher anti-frais intégré) — oui/non
2. Le cap 45 min : condition bloquante (Gemini) ou bras supplémentaire (Buffy) — arbitrage
3. GO/NO-GO lancement L2 recorder 10s ce soir

---

## 🧪 JALON EXECUTÉ — ESSAI 3 BRAS + CAP45 × 4 FENÊTRES (03/09 soir, GO propriétaire sur contre-point Buffy)

Le propriétaire a validé le contre-point : le cap 45 min devient **bras D comparatif** (pas condition bloquante).
Script : `Index_Maison/scripts/essai_3bras_4fenetres.py` — replay HONNÊTE (aucune donnée future),
klines 1m en cache, frais 8 bps AR, notionnel 200 USDT, trailing 30 %, cap gain +50 $,
plancher anti-frais k=3 × médiane 1m borné [60 ; 300] (statistique de la fenêtre elle-même — invariant, garde-fou R31).

**TABLEAU NET (USDT) — bras × fenêtre :**

| fenêtre | A témoin (cap 2h) | B variance | C volume | D cap45 |
|---------|------------------:|-----------:|---------:|--------:|
| VORTEX (120h) | −3,30 | −3,30 | −7,51 | −3,63 |
| NUAGE (432h) | −4,56 | −4,56 | −32,68 | −3,84 |
| ORAGES (96h) | −2,85 | −2,85 | −12,29 | −3,17 |
| MARS (144h) | −0,86 | −0,86 | −10,55 | −1,97 |
| **TOTAL** | **−11,56** | **−11,56** | **−63,03** | **−12,62** |

**Lecture parcimonieuse (rapportée, pas interprétée)** :
- B = A au centime sur chaque fenêtre : le plancher anti-frais n'a JAMAIS été atteint dans les 4 fenêtres
  (les bornes 60-300 $ dépassent tous les MAE des trades simulés) — il protège contre les catastrophes type
  nuit J+1 (−40 $), pas contre le bruit quotidien.
- C (volume) est le PIRE partout : l'horloge volume prolonge les trades perdants sans améliorer les gagnants.
- D (cap 45 min) ≈ A (±1 USDT) : couper plus tôt ne change presque rien ici — les petites pertes se font
  vite ou pas du tout. Aucun bras ne sort du rouge : **la maladie reste les frais sur la fréquence**, pas la sortie.

**Verdict d'essai (1 seul, sans retouche)** : AUCUN bras ne bat le témoin de façon décisive →
le levier prioritaire reste la réduction de fréquence (k=3 en entrée) et l'économie de frais (sorties maker
côté serveur, votée R30), pas la mécanique de sortie.

⚠️ **INCIDENT CANAL (rectifié)** : les R32/R33 ont d'abord été envoyés par API directe `gemini-flash-lite-latest`
SANS historique (réponse hors canal, archivée `.API-DIRECTE-HORS-CANAL.bak`). Détecté par le propriétaire,
**renvoyé sur le BON canal** (`gemini_chat.py --session EDGE_JUILLET`, hub local, identité canonique famille.json,
historique complet) → **ROUND 32, provider Google Gemini**, archivé dans `GEMINI_SESSION_EDGE_JUILLET.{json,md}`
et extrait dans `GEMINI_R33_REPONSE_ESSAI.md`. Verdicts du bon canal :
- Q1 : verdicts R30-R32 **tiennent** — le plancher k=3 jamais déclenché sur ces fenêtres ≠ mauvaise idée, calibration à revoir.
- Q2 : **bascule officielle du diagnostic** — le problème est l'ENTRÉE (fréquence) + les FRAIS, plus la sortie.
- Q3 : le shadow live souffre d'un **biais d'auto-validation du gate H en zone de bruit** (H s'auto-alimente de micro-gains → overtrading). Constat R26 confirmé.
- Q4 : 4 métriques L2 J+7 : Time-to-Heal du mur, OFI 5 s avant/après évaporation, taux de spoofing, profil de volatilité micro-structurelle.
- **Clause permanente** : proposition V3 = **Filtre de Persistance du Carnet** (aspiration maintenue 3 snapshots consécutifs avant entrée — tue le spoofing) + étude d'une **bascule ALPHA sur SPOT** (frais/funding étouffent l'edge brut < 10 bps sur futures).

---

## 🥚 JALON R34 (round 33, Google Gemini) — LA V3 PREND FORM, ON MARCHE SUR DES ŒUFS

Le propriétaire a posé la règle du soir : **attention, on arrive au but** — chaque pas est mesuré avant d'être posé.

### Mesures Buffy (corpus L2 premier échantillon, 13 min, lecture seule)
- 558 murs appariés APPARU→EVAPORE : **vie médiane 2 secondes**, **76 % morts en ≤3 s**
- => le FPC à 3 s filtrerait 76 % du flux de murs : le spoofing est le bruit dominant, mesuré.

### Confrontation Buffy ↔ Gemini (clause permanente dans les DEUX sens)
1. **SPOT : enterré par Gemini elle-même.** Son arithmétique était fausse (spot 20 bps AR vs futures 8-10 ; le funding ne frappe pas des cycles de minutes). Elle retire la proposition — « gel définitif ». On reste sur Futures BTCUSDT.
2. **FPC : validé à l'unanimité** comme LA brique V3, avec deux prérequis non négociables : corpus L2 multi-régimes (13 min ne suffisent pas — overfitting instantané) + seuil de persistance VALIDÉ au replay (balayage 2/3/5 s sur corpus J+7, un seul essai, paramètres invariants). Forma retenue par Gemini : **Score de Persistance continu → seuil binaire dynamique** (âge × masse absorbée, adapté au régime du carnet).
3. **Entrée anticipative RÉHABILITÉE sous condition** (couplage R14 × FPC) : poser un ordre post-only DANS un mur persistant = entrer maker au moment de l'évaporation, capter le saut au lieu du résidu. Gemini : « le FPC transforme l'ordre anticipatif d'un pari aveugle en calcul de microstructure » — validée pour test en SANDBOX uniquement.
4. **Protocole L2 J+7 figé** : Time-to-Heal · OFI 5 s pré/post évaporation · taux de spoofing · profil micro-structurel du trailing. Zéro modification.

### Le chemin vers le but (état au 03/09 soir)
| Brique | Statut |
|---|---|
| Shadow scénario C (gel R24) | 🟢 tourne (1 j 02 h) — J+1 livré |
| Essai 4 bras × 4 fenêtres | ✅ exécuté — verdict : sortie exsangue, priorité = entrée + frais |
| Superviseur L2 | 🟢 prêt + smoke test OK — **lancement durable : 1 commande du propriétaire** |
| FPC (V3) | 📐 défini, testé sur 13 min — **attend son corpus J+7** |
| Entrée anticipative post-only | 📐 réhabilitée SOUS CONDITION FPC — sandbox après J+7 |
| Spot | ⚰️ enterré (R34, par Gemini elle-même) |

**Règle du propriétaire gravée : on ne code AUCUNE brique V3 avant le corpus J+7. Mesurer, contester, sceller.**

---

## 🧬 JALON R35 (03/09 soir, après le GO propriétaire) — LE FPC HÉRITE DE LA MÉTHODE HULK

Le propriétaire a fait le lien de mémoire : **« on a une chose semblable sur Hulk, la collecte des murs »**. Vérifié en lisant le code, noir sur blanc :

### Ce que Hulk a déjà (MEXC, altcoins) — et qui tourne EN CE MOMENT
- **Sonde aspiration** (`ace_sense_mexc.py` dans `paper_diprip.py`, actif 2 j 12 h en `--resume`) : double lecture du carnet à 0,5 s → évolution des murs (même philosophie que le L2 1/s).
- **Détecteur de spoofing** (`observer_murs.py`, launchd `com.ace777.observer-murs`) : « mur qui fond ≥15 %/s puis se reconstruit » — le FPC de Gemini est la réinvention d'une brique que Hulk porte depuis le 16/08.
- **Observatoire agrégé** : **74 425 mesures, 27 paires** (`MURS_RAPPORT.md` / `murs_observations.json`, mis à jour 20h18 ce soir) :
  - SOL : mur bid moyen 501 793 $, spoof 0 %
  - BTC-MEXC : mur bid max 1 924 444 $, spoof 3,31 %
  - XRP : spoof 4,3 % (376 événements) — la paire la plus manipulée du panel
  - Total : 1 845 spoofs (2,5 %), 3 871 chutes ≥15 %/s (le signal ACE)
- **Thèse Christophe déjà validée sur ce corpus** (12 j de données) : descente ≥ 2 % + prise de mur → +24 h WR 58 %, R:R 3,7 (`detecter_accumulation`, mode OBSERVATION, suivi +6h/+24h).

### Action exécutée ce soir : la méthode Hulk est PORTÉE sur le L2 BTC
`superviseur_l2.py` v2 : flag **SPOOF** ajouté (éaporation puis réapparition au même niveau ≤ 120 s → `event=SPOOF` dans le CSV murs). Testé en 60 s : **3 SPOOF détectés** (ASK 81388 / 55 k$, 81418 / 55 k$, 81443 / 50 k$) — le détecteur de mensonges de Hulk fonctionne sur Binance dès sa première minute.

### Conséquence pour le FPC (V3)
- Le protocole J+7 ne part pas de zéro : **l'étalonnage spoof/murs existe déjà** (74 k mesures Hulk + corpus BTC en cours).
- La grille de calibration reste RELATIVE par marché (médiane glissante) — leçon commune des deux moteurs.
- Le seuil SPOOF_WINDOW (120 s) est un paramètre candidat : balayage 60/120/300 s au replay J+7, un seul essai (règle anti-overfitting inchangée).

**La mémoire du propriétaire a évité de réinventer une roue que Hulk roule depuis le 16/08.**

---

## 🛰️ JALON — SUPERVISEUR L2 PASSIF : PRÊT (lancement par le propriétaire)

Script : `Index_Maison/scripts/superviseur_l2.py` + lanceur `launch_l2_superviseur.sh`.
**Testé OK** (45 s de smoke test : 18 snapshots, 139 événements murs, plus gros mur BID 1 982 546 USDT @ 81 445)
puis ~109 snapshots sur la soirée avant arrêt.
- 1 snapshot/s REST `/fapi/v1/depth?limit=50` (poids ~5, limite 2400/min → marge large)
- CSV dédiés : `runs/L2_YYYYMMDD_SNAPS.csv` (1 ligne/s) + `runs/L2_YYYYMMDD_MURS.csv` (APPARU/EVAPORE/FRANCHI)
- Seuil mur RELATIF : 8× médiane notionnelle glissante (10 min), borné [50k ; 2M] — leçon Hulk, aucun absolu figé
- Zéro ordre, zéro clé, zéro contact shadow/champion · stop : `touch runs/STOP_L2`
- **Contrainte terrain constatée** : les process lancés depuis la session Buffy meurent à la fin de la commande
  (le shadow survit car lancé depuis le terminal de Christophe) → **le lancement durable se fait par Christophe** :

```
cd ~/ace777-test-day1 && ./launch_l2_superviseur.sh
```

Arbitrage de fréquence : le protocole R32 disait 10 s ; le script sonde 1×/s (meilleure résolution,
poids REST toujours négligeable). Ajustable via SNAP_EVERY.

---
*Buffy, 03/09 11h30 UTC — document vivant, mis à jour après chaque jalon.*
