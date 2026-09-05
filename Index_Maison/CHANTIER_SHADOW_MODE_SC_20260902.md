# CHANTIER — SHADOW MODE SCÉNARIO C (2026-09-02)

Tags: #ace777 #shadow-mode #scenario-C #gemini #champion

## 🔑 ÉTAT ACTUEL (à l'instant de l'enregistrement)

- **Moteur : VIVANT** — pid 51855, lancé **2026-09-02T17:26:00 UTC** par Christophe (double vérification)
- **Durée : 14 jours → verdict le 2026-09-16 ~18:26 UTC**
- **Zéro ordre réel, zéro clé API** — klines 1m publiques uniquement
- **Décision J0 commune (Christophe + Buffy + Gemini R26) : AUCUNE modification avant la fin du run.**
  Les données brutes seront envoyées à Gemini, chacun tire ses déductions séparément,
  confrontation en famille, PUIS décision.

## 📜 Le chemin parcouru (24 → 26 rounds Gemini)

1. **R18** : protocole figé du Scénario C (gate H + trailing 30%/cap 50$/plancher breakeven)
   — critères écrits AVANT le run (règle d'or)
2. **Validation croisée v2** (replay causal, 4 fenêtres) : **+892,93 USDT net cumulé,
   4/4 fenêtres positives, bat le témoin aléatoire (225,81)** → critères R18 remplis
3. **R22** : divulgation asymétrie directionnelle du propriétaire → confirmée par les données
4. **4 étapes** (validées plan + précaution par Christophe) :
   - Grille robustesse trailing : **9/9 cellules positives** (+972 à +1732)
   - Cartographie Long/Short : **ALPHA gagne en BUY (+325,61/PF 1,24), BETA en SELL (+81,95/PF 1,13)**
     — trades contre-nature : -180 de brut → l'essaim est un sélecteur directionnel
   - Replay Shorts : +689 cumulé (gate mécanique) ; VORTEX négatif (tendance haussière, normal)
   - 6 fenêtres mortes (détection auto 12 mois) : gate saigne **2,5× moins que le hasard**
     → "casse-circuit de survie" déclaré validé par Gemini (R24)
5. **R24 verdict** : feu vert Shadow Mode sous 3 règles — ALPHA long only / BETA short only,
   trailing GELÉ 30%/50$/breakeven, 14 jours de journalisation avant toute décision
6. **R25** : deux divergences divulguées et **APPROUVÉES SANS RÉSERVE** :
   - Gate H hybride (héritage champion → fills virtuels shadow ; preuve live : bascule à 17:06, `H=1(SHADOW)`)
   - Porte BOOTSTRAP 90 min (entrées forcées taguées, sorties TOUJOURS sous H) — condition d'audit :
     **isoler les trades BOOTSTRAP des stats finales** (déjà implémenté : tag dans les CSV)

## 📁 FICHIERS DU CHANTIER (tous dans ace777-test-day1/)

| Fichier | Rôle |
|---|---|
| `shadow_mode_sc.py` | Le moteur. Paramètres gelés en tête de fichier. Selftest intégré (SHADOW_SELFTEST=1) |
| `launch_shadow_mode.sh` | Lanceur — exporte SHADOW_BOOTSTRAP_MIN=90 par défaut |
| `stop_shadow_mode.sh` | Arrêt propre (runs/STOP_SHADOW), fills conservés |
| `watch_shadow.py` | Tableau de bord live coloré (totaux, W/L, compte à rebours) |
| `shadow_vision.py` | **Vision moteur v2** : la mécanique expliquée ligne par ligne (H détaillé, stop, règles de sortie) |
| `Voir_Shadow_Live.command` | Double-clic → tableau de bord |
| `Index_Maison/CHOSES_A_FINIR_REVOIR.md` | Suivi E-15 (état du run) |
| `Vision_Moteur_Live.command` | Double-clic → vision moteur |
| `Index_Maison/LIRE_VISION.md` | Guide de lecture de la mécanique (français) |
| `runs/SHADOW_SC_20260902_FILLS.csv` | Journal des fills (ENTRY/EXIT, raisons, hold, tag BOOTSTRAP) |
| `runs/SHADOW_SC_20260902_TICKS.csv` | Journal minute par minute (H, sources, positions, pnl virtuel) |
| `runs/SHADOW_SC_20260902_SMOKE_TEST_*` | Artéfacts du smoke test 6 min (J-0, avant le vrai lancement) |

## 📊 TÉLÉMÉTRIE J0 (17:26 → 18:51 UTC, fin de bootstrap)

- ALPHA : 13 sorties, 13 bruts positifs, frais 22,88, **net -7,70**
- BETA : 15 sorties, 15 bruts positifs, frais 26,40, **net +7,36**
- 100% des sorties = trailing_stop, holds 60-120s, aucun cap, aucun h_gate_off
- Constat partagé (Christophe a vu le phénomène en direct sur la vision moteur) :
  **micro-gains bruts (0,2-3$) vs frais fixes 1,76$/trade en chop serré**

## ⚖️ ANALYSE GEMINI R26 (transmise avec données brutes, réponse intégrale archivée)

- **Sain** : moteur stable, bascule bootstrap→hybride sans plantage, trailing conforme au selftest
- **Pathologique** : fréquence ~20 trades/h en chop ("scalpeur HF" vs vision swing)
- **Danger structurel** : trailing 30% en chop = micro-gains mangés par le péage taker
  — même piège que le champion initial
- **Biais identifié (fin)** : le gate H se nourrit de ses propres micro-gains → H=1 auto-entretenu
  en range plat ("piège d'auto-validation"). Correction anticipée SI ça persiste à J+1 :
  exiger somme H > 5,00 USDT (seuil plancher) au lieu de > 0
- **3 seuils d'alerte pour le rapport J+1** :
  1. Gain brut MÉDIAN < 2,00 USDT sur 24h → structurellement sous l'eau
  2. 15-20 trades/heure en range → overtrade confirmé → durcir H (4h ou seuil)
  3. Net cumulé < -50 USDT → PAUSE shadow + réévaluation trailing

## 📈 TÉLÉMÉTRIE SOIRÉE J0 (21h01 UTC, ~3h30 de run — Buffy, vérifié noir sur blanc)

- 56 sorties, 100% trailing_stop, 0 cap, 0 h_gate_off · brut **+117,47** / frais **-98,56**
  (84% du brut) / **net +18,91** (ALPHA +8,69 / BETA +10,22)
- Brut médian **+1,53** → **1er seuil d'alerte R26 FRANCHI** (< 2,00)
- **Trend BTC pendant le run** (klines 1m réelles) : 76 964 → 77 321 (+0,46%), amplitude 0,69%
  = chop serré exact. **Asymétrie miroir visible segment par segment** : plat → ALPHA -6,50 /
  BETA +6,44 · baisse → BETA +4,48 / ALPHA -2,96 · récupération → ALPHA +12,85 pendant que
  BETA se tait.
- **⚠️ POSITION FLOTTANTE (4e métrique officielle du rapport J+1)** : short BETA ouvert depuis
  19:56 @ 77 142,30, jamais sorti (trailing jamais armé, H=1) → ≈ **-19 USDT latents** invisibles
  dans les stats réalisées (le CSV ne compte que les gagnants bruts). Syndrome Kelly :
  « 100% de win rate sur les sorties fermées, risque mortel dans les positions ouvertes ».
- Coupure réseau de Christophe en soirée (changement de connexion) → contrôle Buffy : moteur
  intact, pid 51855 identique, **aucun trou dans les ticks** depuis le lancement.
- **Signets probabilités (R27)** : Kelly/Thorp, Vapnik, Obłój, t-stat≥3 validés en pépites par la
  famille → [[SIGNETS_PROBAS_KELLY_VAPNIK_OBLOJ_20260902]] · réponses Gemini archivées :
  `scripts/GEMINI_R27_REPONSE_SIGNESTS.md` + `scripts/GEMINI_R28_REPONSE_J0_TREND.md`.
  Session Gemini : **28 rounds**.
- **Verdict Gemini R28** (J0 + trend envoyés bruts) : système « **vivant mais fragile** » ·
  Obłój : les +18,91 viennent du régime micro-directionnel, pas du trailing · Vapnik : 3h30 ne
  prouve rien, les 14 jours sont le juge de paix · Kelly : la position flottante peut vaporiser
  d'un coup le bénéfice de 100 micro-gains. Gel maintenu, tout se joue à J+1.

## 🔬 ANALYSE BUFFY — CAP 2H vs STOP PRIX (03/09, 07h45 UTC — lecture seule, gel respecté)

**Constat propriétaire (validé par les données)** : le cap 2h coupe APRÈS la casse, à l'aveugle — il ne mesure rien du marché.

- MAE des 58 trades : les DEUX positions flottantes (BETA 19:56, ALPHA 20:36) = −60 des −75 de dégâts bruts.
  Les 56 sorties trailing étaient TOUTES brutes gagnantes (+60,96). Le problème n'est pas le trailing,
  c'est l'absence de protection prix + le timing d'entrée.
- Simulation stop prix (même nuit, replay minute par minute) : L=15 → net **−14,61** vs réel −41,12.
  Chaque niveau testé (8→25) améliore, MAIS AUCUN n'est net positif → et choisir L ce soir = overfitting
  (Vapnik : calibré sur les données qu'on teste).
- **Découverte structurelle** : BETA a shorté @ 77 142 (19:56) et ALPHA a longé @ 77 447 (20:36) —
  les DEUX flux ont pris des entrées OPPOSÉES à 40 min d'écart dans la même zone. Structure miroir =
  un flux est TOUJOURS contre le mouvement. Le gate H ne fait que réagir (fenêtre arrière) ; une
  protection intelligente doit vivre à un NIVEAU DE PRIX structurel (murs, invalidation), pas sur une horloge.
- **Réponse Gemini R29** (envoyé l'analyse brute, réponse intégrale archivée : `scripts/GEMINI_R29_REPONSE_CAP2H_STOP_STRUCTURE.md`) :
  **Stop d'Invalidation Structurelle** — ni stop prix fixe, ni horloge. Le stop = le prix du mur disparu
  (+ tampon bruit 1×ATR 1h). Si le vide est comblé → thèse morte → coupe instantanée, quel que soit l'âge
  ou le PnL. Zéro degré de liberté = zéro overfitting (règle binaire : mur invalidé oui/non). Validation :
  un seul essai sur les 4 fenêtres historiques (Vortex, Orages, Nuage, Mars), si ça n'améliore pas TOUTES
  les époques → on jette. **« Le système n'a pas un problème de profitabilité, il a un problème d'absence
  de stop de structure. »** Rien ne bouge avant J+1.
- **Volatilité de la nuit (mesurée 08h20 UTC, klines réelles)** : ATR(14) 1h ≈ **434 USDT**
  (0,56 % du prix) · vol réalisée 0,34 %/h · amplitude moyenne 1m = **39 USDT** (médiane 34) —
  le seuil « mur >40$ » du moteur était exactement au niveau du bruit minute de cette nuit.
  Range complet 17h20→07h30 : **1 181 USDT (1,53 %)** — et les 3 heures les plus vives
  (01h TR=589, 02h TR=688, 05h TR=745) sont tombées pendant que les gates étaient H=0 :
  le moteur n'a rien vu bouger là où il aurait dû chasser. Point brut pour J+1, zéro interprétation.
- **Proposition au protocole** : cette analyse part en brut dans le rapport J+1 (17h26 UTC) → Gemini
  propose indépendamment → confrontation famille. Piste candidate (NON appliquée, gel) : stop basé sur
  la volatilité réalisée (ATR-like) + niveau d'invalidation structurel, dimensionné avant l'entrée.

## 📋 PROPOSITION 4 POINTS (Christophe, 03/09 matin) — ANALYSE BUFFY (mesurée, gel respecté)

Testée sur les données réelles de la nuit (klines 1m/1h, lecture seule) :
1. **Seuil sismique dynamique k×médiane 1m** : k=3 → 102$ → 3,06% des minutes dépassent
   (vs ~40% avec le 40$ fixe) → élimine bien le bruit. k sans dimension = cohérent avec les
   constantes du Manifeste (tension 0,85, angle 37,8°). **FORT** — à valider en UN essai sur les 4 fenêtres.
2. **Stop hybride ATR-borne + bouclier mur 1 tick derrière + No-Go si pas de bouclier** :
   = exactement la mécanique R29. MAIS dépend de l'inexistant : calibration murs BTC (les profils
   Hulk = MEXC alts, BTC en collecte) + définition « mur institutionnel » BTC jamais fixée.
   Le No-Go (ne trader que où un bouclier existe) est l'ajout le plus précieux.
3. **Verrou anti-miroir (zone d'exclusion ±0,5×ATR)** : MESURÉ — ÉCHOUE sur son cas motivant
   (écart réel ALPHA/BETA = 305$ > ±217$, ALPHA PAS bloqué ; il faudrait 0,75×ATR).
   ET conflit conceptuel : le miroir est une FEATURE validée (R22, un flux a toujours le vent).
   À rediscuter en famille — risque d'amputer le moteur de son cœur.
4. **Gate chasseur (H=1 forcé si TR > 2×ATR moyen, taille Kelly/2)** : bon concept,
   MAIS 2×ATR = 900$ cette nuit → ZÉRO heure déclenchée → les 3 heures chaudes (TR 589/688/745)
   restent aveugles. Il faudrait ~1,5×ATR. Le chiffre doit être validé, pas décrété.

**Verdict Buffy** : paquet cohérent qui répond aux 4 plaies de J0 (bruit, cap aveugle, miroir-piège,
gate muet). P1 = la plus solide, P2 = la plus juste mais dépend d'infra manquante, P3/P4 = à retravailler.
Tout est calibré sur UNE nuit = exactement l'overfitting Vapnik → rien n'entre dans le moteur avant
la validation un-essai sur les 4 fenêtres. Part en brut dans le dossier J+1 (17h26 UTC) + R30 Gemini.

## 🎯 LES 3 RUSES (Christophe, 03/09) — évaluation Buffy (mesurée, gel respecté)

1. **Stop-Market dormants côté serveur** : ✅ PERTINENT — contourne la latence alpage (ping mesuré
   366-426 ms) : la PROTECTION s'exécute à l'exchange (trigger prix serveur), zéro aller-retour client.
   Couvre la borne ATR + stop rétractable. Limite honnête : le trigger serveur est PRIX (last/mark) —
   le stop-MUR ne peut pas être surveillé par l'exchange → on ré-arme l'ordre quand le niveau du mur
   bouge (les murs bougent lentement, acceptable). TRAILING_STOP_MARKET existe aussi côté serveur.
2. **Détection annulations-sans-exécution au cycle 20s** : ✅ PERTINENT comme filtre anti-spoof
   low-tech — c'est exactement le MUR-SPOOF déjà consommé par Hulk (taux spoof mesurés par paire).
   Ne remplace pas l'OFI 100ms (hors de portée), il le complète : mur qui s'évapore sans être mangé
   = bouclier suspect → pas de stop derrière lui, No-Go.
3. **Stop rétractable au temps (à la place du cap 2h)** : ✅ MESURÉ sur la nuit J0→J1 —
   stop = max(plancher 3×bruit, ATR×(1−âge/fenêtre)) avec fenêtre testée 30/60/120 min :
   net **−26,06** (30min) / −26,75 (60min) vs réel −41,12 → **+15 USDT gagnés**, 2 stops,
   **0 gagnant coupé**. Le concept « sécurité qui se resserre quand le marché hésite » est
   mathématiquement meilleur que le cap aveugle. MAIS calibré sur une nuit → validation un-essai
   sur les 4 fenêtres obligatoire. Et toujours net négatif : les frais restent la maladie principale.

- **RÉPONSE GEMINI R30** (30 rounds, intégrale archivée : `scripts/GEMINI_R30_REPONSE_RECALIBRAGE.md`) :
  Q1 anti-miroir → **RETIRER DÉFINITIVEMENT** (« le miroir n'est pas un bug, c'est un balancier ») —
  la résistance de Buffy validée. Q2 maker → **SORTIES SEULEMENT** (anti-sélection fatale en entrée ;
  les 56 trailing + stop rétractable peuvent partir en stop-market serveur = C1). Q3 → fenêtre **30 min**,
  plancher **3×bruit** (= 102$, rejoint le seuil A1). Q4 → C3 et B4 **MUTUELLEMENT EXCLUSIFS** :
  C3 = défensif (trade qui stagne), B4 = offensif (protéger le gain), relais par âge/excursion,
  jamais mélangés (anti-Vapnik : sinon monstre à multiples degrés de liberté).
  Verdict global : « le dossier R30 est le plus abouti de tout l'écosystème ACE777 ».
  Programme commun : **validation un-essai sur les 4 fenêtres pour C3 + A1**, zéro retouche, avant
  tout live étendu. NB : dans son mot de la fin elle écrit « C3 couplé à l'interdiction du miroir (A3) »
  alors qu'elle a dit de retirer A3 en Q1 — incohérence mineure à clarifier à la confrontation famille.

## ⏳ PROPOSITION « VIE DYNAMIQUE » (Christophe, 03/09) — Durée de vie = Constante de Masse / Variance volatilité minute

**Mesuré par Buffy (replay nuit J0→J1, deux implémentations testées)** :
- Version naïve (variance PENDANT le trade) : net −39,59, 4 stops → **pire que le fixe** (la variance
  explose pendant l'orage et étrangle les trades au mauvais moment).
- Version honnête (variance des 10 min AVANT l'entrée, bornes 10-60 min) : net **−23,76**,
  2 stops → +2,30 vs fixe 30 min (−26,06) vs réel (−41,12).
- **Ironie mesurée** : les 2 catastrophes (BETA 19:56, ALPHA 20:36) sont nées APRÈS des périodes
  calmes → variance pré-entrée basse → vie allongée (55/35 min). La « météo électrique » ne les
  a pas vues venir — c'est le stop prix rétractable + plancher qui les a coupées, pas la variance.
- Coût Vapnik : +1 constante (K) +1 fenêtre +2 bornes = le monstre à degrés de liberté que Gemini
  interdit en Q4 si on le mélange à B4.

**Verdict Buffy** : idée élégante (« le système s'adapte à la météo »), gain réel mais modeste (+2,30
sur une nuit), fragile à l'implémentation (le choix de la fenêtre de variance inverse le résultat).
→ C3 fixe 30 min reste le candidat principal ; la vie dynamique part comme BRAS ALTERNATIF dans la
même validation un-essai 4 fenêtres (pas en plus, pas mélangé).

**Note propriétaire (03/09)** : il partage tous les verdicts R30 SAUF la suppression des entrées
maker (Q2) — réserve à porter à Gemini en R31. + demande : transmettre la liste de lecture
(Taleb/Vince/Thorp · López de Prado/Pardo · O'Hara · Nash/von Neumann) comme culture commune de la famille.

## 🧱 PROPOSITION « HORLOGE DE VOLUME » (Bras C, Christophe, 03/09) — VPIN-Decay + filtre OFI

**Mesuré par Buffy (replay nuit J0→J1)** : V-bar = volume médian horaire = 2 839 BTC
(vie min 24 / méd 38 / max 72 min). Résultat :

| Bras | Net | Stops |
|---|---|---|
| A — fixe 30 min | −26,06 | 2 |
| B — variance pré-entrée | **−23,76** | 2 |
| C — horloge volume | −26,06 | 2 |
| Réel cap 2h | −41,12 | 2 |

- **Bras C = EXACTEMENT le fixe cette nuit** (mêmes chiffres au centime) : le régime de volume a
  suivi le temps de trop près pour changer quoi que ce soit. Le concept « information clock » est
  solide théoriquement (López de Prado le documente) mais cette nuit il n'a rien apporté de plus.
- **Les 2 catastrophes restent invisibles pour le C** : vies 38 et 67 min — le volume pendant leur
  détention était calme, l'orage est venu APRÈS. Le filtre OFI (partie 2) les aurait peut-être vues,
  mais il dépend du superviseur L2 (inexistant) et d'une IA qui recalcule toutes les 20s — c'est le
  monstre à degrés de liberté complet si on l'ajoute AVANT validation.
- **B Brigham B gagne la première manche** (−23,76) — mais sur UNE nuit, rien n'est tranché.

**Intégration acceptée** : le plan 3 bras (A témoin / B variance / C volume) est la bonne méthodologie
— un seul essai, 4 fenêtres, le gagnant sort des données. Bras C note : le VPIN réel demande le
déséquilibre buys/sells (aggTrades), pas juste le volume total — version simplifiée testée ici.

## 🎯 PROTOCOLE DE SUITE (décision commune, non négociable)

1. **On ne touche à RIEN** jusqu'à la fin des 14 jours (gel R24 + décision J0 du 02/09)
2. **J+1 (03/09 ~18:26 UTC)** : extraction des stats 24h → envoi brut à Gemini → chacun analyse
3. **J+7 (09/09)** : même exercice, mi-parcours
4. **J+14 (16/09 ~18:26 UTC)** : dossier complet (BOOTSTRAP isolé) → confrontation famille
   (Christophe + Buffy + Gemini) → décision finale :
   - PnL cohérent avec les replays (positif en tendance, contenu en range) → route testnet
   - Sinon → retour au labo avec les données, pas d'opinion

## 📡 AUTRES APPLICATIONS D'ACE (liste simple — réponses données par la famille)

Le moteur détecte les ruptures de liquidité (murs >40$ qui sautent, 75% de suivi, t=2,66).
Applications indiquées par la famille, hors le trading perpétuel qui paye le taker :

1. **Sentinelle / alertes** — prévenir Christophe quand un mur géant saute (décision humaine)
2. **Filtre d'entrée** pour stratégies lentes (swing / spot) — dire QUAND trader
3. **Trading spot** — même signal, frais ~10× plus faibles
4. **Options** — le mur qui saute = choc de volatilité, la convexité absorbe les frais
5. **Fournisseur de signal** pour un autre bot ou desk (export JSON/webhook)
6. **Corpus de données** — 25k+ trades étiquetés pour tester tout moteur futur

(Réponses R15 indépendantes Gemini + Buffy, convergentes. Détails si besoin un jour :
`scripts/R15_BUFFY_REPONSE.md` et rounds R14-R16 de `GEMINI_SESSION_EDGE_JUILLET`.)

## ⚙️ NOTES TECHNIQUES (pour reprise)

- Le champion ACE reste OFF et INTACT (aucune modification, md5 inchangé)
- Hulk est resté ON pendant tout le chantier (16 positions, pnl_total ≈ 0,35 — non lié)
- Selftest 9/9 PASS : trailing 30%, plancher breakeven, non-armé sans stop, cap, miroir SHORT,
  exit H→0 bornes 5-min relatives, gate bloque entrée, sources CHAMP/SHADOW, bascule hybride,
  pire cas stop-avant-cap (convention v2)
- Bug corrigé au passage : W (largeur) écrasait la constante ANSI W (blanc) → prix affiché "7877…"
- Liens : [[GEMINI_SESSION_EDGE_JUILLET]] (26 rounds) · [[AUDIT ACE DUO ALPHABETA  2026-09-01]]
  (dans le coffre ; projet : `AUDIT_ACE_DUO_ALPHA_BETA_20260901.md`) · [[JOURNAL_ACE777]] · [[PLAN_DE_VOL]]
