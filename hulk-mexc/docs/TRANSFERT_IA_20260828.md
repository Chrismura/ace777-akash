# TRANSFERT IA — Session du 28/08/2026 (audit trend + liquidité + accumulation)

> **À LIRE EN PREMIER PAR TOUTE IA QUI REPREND CE PROJET.**
> Ce document est auto-suffisant : il contient tout le contexte nécessaire pour
> comprendre l'état du système, les découvertes, les décisions et la suite.
> Écrit par Buffy (Freebuff) le 28/08/2026, pour Christophe et toute IA future.

---

## 0. TL;DR (30 secondes)

Le 28/08, on a audité **comment détecter le trend de marché** (méthodes des fonds
institutionnels confrontées à nos données réelles), découvert que **le momentum
multi-horizon (TSMOM) est le détecteur le plus réactif** mais que **personne ne bat
le hasard sur 7 jours** (le court terme = bruit), validé la **structure de liquidité
du BTC** (ancrage 64k$, mur 82k$, sol 61,5k$), et prouvé sur 12 jours de données
que **"descente ≥ 2% + prise du mur au sud" = signal d'accumulation +24h** (58% win,
R:R 3,7 — mais à confirmer hors jours haussiers).

**Implémenté (actif en paper)** : mode **trailing** sur 6 paires liquides (laisser
courir les gagnants), **détecteur d'accumulation 24h en OBSERVATION** (journalise,
ne trade pas), **profil de liquidité** (niveaux clés BTC).

**En attente** : 2-3 semaines de collecte pour valider/invalider l'edge d'accumulation.

---

## 1. Contexte du projet (pour toute IA nouvelle)

- **HULK** = bot de **paper trading** (jamais d'argent réel) sur MEXC spot, small caps.
  Moteur : `hulk-mexc/scripts/paper_diprip.py` (tourne 24/7 via launchd + watchdog).
- **ACE777 / Index_Maison** = l'écosystème autour : indices, régime de marché,
  ADA GARDIENNE (sentinelle de risque), cockpit, veille, sniffer.
- **Christophe** = le chef de projet. Règles d'or gravées :
  1. On ne code pas une stratégie sans **preuve réelle** (backtest sur données).
  2. Le **narratif/opinion ne vaut rien** face au prix (les faits).
  3. On **mesure d'abord, on observe ensuite, on trade enfin** — jamais l'inverse.
  4. Tout doit être **réversible** et **documenté**.
- Données disponibles : klines Binance (publiques, gratuites), klines MEXC,
  CSVs de sonde aspiration (`ASPIRATION_CALIB_*.csv` + `OBSERVATION_MURS_*.csv`).

---

## 2. L'AUDIT TREND (la demande de Christophe)

### 2.1 La question
*"Audite le meilleur setup pour détecter le trend. Comment les gros fonds s'y
prennent ? Confronte et valide. Puis couple avec nos indices et notre IA."*

### 2.2 Méthodes institutionnelles (recherche faite)
| Méthode | Qui l'utilise | Principe |
|---|---|---|
| TSMOM / momentum multi-horizon (1-12 mois) | Man Group, Winton, AQR, Moskowitz et al. 2012 | Le signe du rendement passé donne la direction |
| MA200 / golden cross (MA50/200) | Fonds actions, ETFs trend | Bull si prix > MA200 ; croisement 50/200 |
| Décomposition bull/bear/sideways (rendement 60j) | Papers académiques (AdaptiveTrend 2026, arxiv 2602.11708) | Sert à **valider** les résultats, pas prédire |
| Régime de volatilité (GARCH, ciblage vol) | Citadel, managed futures | La vol se prédit (~70%), la direction = bruit → dimensionner par la vol |
| HMM 3 états | LSEG, quant shops | Classé "plus tard" par notre éval #7 (lent, à valider OOS) |

### 2.3 Les résultats (300 jours de klines 1j BTC, Binance — réelles)

**Marché testé** : contenait les 3 régimes — bull (mars-mai, jusqu'à 82k$), **bear
réel (juin-juillet, creux 58 625$ le 30/06)**, retournement (août, +35% depuis le creux).

**Réactivité au retournement du 30/06** (le point critique) :
| Méthode | Repasse HAUSSIER | Lag après creux |
|---|---|---|
| **TSMOM 30j** | **05/07** | **5 jours** ← le plus réactif |
| MA200 | 19/08 | 50 jours |
| MA50/200 (golden cross) | **jamais** | ∞ — INAPPLICABLE au crypto |

**Qualité de séparation** (le signal sépare-t-il les bons des mauvais jours ?) :
- TSMOM 30j : séparation +0,795%/jour, Sharpe 2,50
- MA200 : séparation +2,277%/jour (le plus fort) mais ne parle que 3 jours en 300

**Justesse à 7 jours** (la question piège) :
| Méthode | HIT 7j | Verdict |
|---|---|---|
| TSMOM 30j seul | 48,6% | ≈ hasard (base 47,5%) |
| Multi-horizon 30/60/90/120 | 45,5% | ≈ hasard |
| Multi-horizon + MA200 | 100% (3/3) | parfait mais ultra-rare |

### 2.4 LES DEUX LEÇONS FONDAMENTALES (à retenir pour toujours)

1. **Le golden cross MA50/200 est INAPPLICABLE au crypto** : il n'a jamais repassé
   haussier alors que BTC avait déjà rebondi de +35%. Trop lent pour des marchés qui
   changent de régime en semaines.
2. **AUCUN signal de trend ne bat le hasard sur 7 jours** : 7j est trop court pour un
   signal de climat. **Les signaux de trend servent à router la stratégie (bull→hold,
   bear→défensif), PAS à acheter/vendre maintenant.** C'est la distinction fonds :
   climat vs météo du jour.

### 2.5 Le constat sur notre système (important)
Le 28/08, notre `couleur_regime.py` disait **ORANGE** ("pas assez de signal", avis IA
3 LONG / 4 SHORT) alors que la méthode validée disait **HAUSSIER clair** (r30 +24%,
r60 +32%, 4/4 horizons). **Le moteur était en retard sur le retournement depuis juillet.**
Leçon : **le prix (fait) doit primer sur l'avis IA (opinion)** — l'IA ne bloque pas un
trend validé. (Non implémenté — décision en attente.)

---

## 3. LA STRUCTURE DE LIQUIDITÉ DU BTC (la lecture de Christophe, validée)

### 3.1 Le contexte
Christophe avait vu une vidéo : "gros mur au-dessus de 80k$, beaucoup de liquidité
au sud entre 50-62k$". Il pensait que le marché allait redescendre. (Au départ il a
dit "murs au nord" puis corrigé : "je voulais dire murs au sud" = les murs d'achat
en dessous.)

### 3.2 Validation par le profil de volume (300j de klines)
Module : `hulk-mexc/scripts/profil_liquidite.py` → `runs/liquidite_profil.json`.
Résultat (28/08) :
```
ANCRAGE (POC)      : 64,000$   ← le prix le plus échangé (le "centre de gravité")
Zone de valeur 70% : [62,000$ — 91,500$]
Support épais (sol) : 61,500$   ← ta zone sud
Mur haut (résist.) : 82,000$    ← le vide de volume au-dessus du prix (ton mur 80k)
Étage suivant      : 86,500$    ← la liquidité qui remonte (le toit épais)
```
**La lecture de Christophe (vidéo, sans indicateurs) est CONFIRMÉE par les données.**
Interprétation : le prix à 79,5k$ est SOUS le mur 82k$, avec un vide 82-86k$ au-dessus
et un toit épais 88-91k$. **Breakout = traverser le vide d'un coup ; échec au mur →
gravité vers l'ancrage 64k$ (volume 4× plus dense).** Le mur dit OÙ, le TSMOM dit QUAND.

---

## 4. LA DÉCOUVERTE : PRISE DE LIQUIDITÉ = SIGNAL D'ACCUMULATION (le gros morceau)

### 4.1 La thèse de Christophe
*"Un trend peut se déclencher sur la prise de liquidité. Le prix est attiré vers le
bas pour prendre la liquidité d'achat (les gros murs bid en dessous), et ça peut
déclencher un mouvement."*

### 4.2 Le chemin de la validation (avec les pièges évités)
1. **Premier test (1 jour de données)** : prise du mur ask (nord) → baisse 78% du
   temps. Mais c'était le MAUVAIS côté (Christophe voulait le sud) et 1 jour = trop peu.
2. **Test corrigé (1 jour)** : prise du mur bid (sud) → hausse 22% seulement. Toujours
   trop peu, marché baissier ce jour-là.
3. **Vérification demandée par Christophe** ("normalement il y a déjà des sondes") :
   ✅ il avait raison — `probe_aspiration()` dans le moteur collecte déjà drop_bid/ask
   %/s depuis le 16/08 = **~60 000 lignes** dans ASPIRATION_CALIB_*.csv. Mon process
   séparé (journal_prises_liquidite.py) était un DOUBLON → **supprimé**.
4. **Analyse sur les 12 jours de données existantes** (~60k lignes) :
   - 2 908 prises au sud (murs ≥ 2 000$) : prise seule → REBOND 50% = **pile ou face**
   - MAIS descente ≥ 2% avant la prise → REBOND **63%**
   - Prise sèche (≥15%/s) vs lente : aucun effet (49% vs 46%)
5. **Mesure de l'ESPÉRANCE (le piège évité)** : win rate 63% ≠ profit. Sur 83 signaux :
   - **+1h : 46% win, moyenne −0,01% = ZÉRO edge** (le rebond existe mais trop tardif)
   - **+6h : 55% win, moyenne +1,48%, R:R 1,66**
   - **+24h : 58% win, moyenne +4,09%, R:R 3,72** ← LE SIGNAL
6. **Test de robustesse (l'honnêteté)** : 60% des signaux concentrés sur 2 jours
   haussiers (18/08, 20/08) et 2 paires (XRP 25, RED 21) → **l'edge est probablement
   sur-estimé par le contexte**. Les pires cas (RED −8,7% le 21/08) montrent qu'en
   contexte baissier le signal ne protège pas.

### 4.3 LA FORMULE (validée, à confirmer)
```
SIGNAL ACCUMULATION = descente ≥ 2% (30 min) + prise du mur SUD (drop_bid ≥ 5%/s,
mur ≥ 2 000$, pas de spoof) → acheter pour TENIR 24h+ (pas scalper)
```
**La lecture** : la descente prépare (purge les vendeurs faibles), la prise du mur
confirme (plus personne pour vendre → rebond). **La liquidité est le CONFIRMATEUR du
retournement, pas le déclencheur.** Et le rebond est à MOYEN terme (24h), pas à 1h.

### 4.4 Décision Christophe : OBSERVATION (pas de trade)
Implémenté dans `paper_diprip.py` : `detecter_accumulation()` — journalise chaque
candidat avec suivi +6h/+24h dans `runs/accumulation_signal.jsonl`. **ZÉRO effet moteur.**

---

## 5. CE QUI A ÉTÉ IMPLÉMENTÉ (état au 28/08 soir)

### 5.1 Mode TRAILING actif (laisser courir les gagnants)
- **Quoi** : sur les paires avec `trail_arm_pct`/`trail_giveback_pct` dans leur profil,
  le moteur ne vend plus au rip fixe — il laisse courir et sort si le prix redonne X%
  sous son pic. Le stop fixe reste en backstop.
- **Où** : `strategie/universe_profils.json` (champs ajoutés) + `manage_open()` lit déjà.
- **Paires armées (28/08)** : PYTH (arm 6,6% / giveback 2,7%), CHIP (7,7/3,15),
  HBAR, KITE, RED, XRP (6,6/2,7). Backups : `universe_profils.json.bak-avant-trailing-20260828`.
- **Preuve immédiate** : KITE est sorti à +14,7% (trailing) au lieu de +6% (rip) → +0,40$.
- **Justification** : backtest 30j Binance → sur les paires liquides qui montent
  (CHIP +34$, PYTH +7,6$), HOLD écrase le scalping. Le trailing capture l'essentiel
  du gain sans l'exposition totale du hold.

### 5.2 Détecteur d'accumulation 24h (OBSERVATION)
- **Où** : `paper_diprip.py` → `detecter_accumulation()` (appelé dans `probe_aspiration`)
- **Config** (`config/defaults.env`) : `ACCUM_DESCENTE_PCT=2.0`, `ACCUM_DROP_PCT_S=5.0`,
  `ACCUM_MUR_USDT=2000`, `ACCUM_MEMO_SEC=1800`
- **Sortie** : `runs/accumulation_signal.jsonl` — un JSON par candidat :
  `{ts, pair, px0, descente_avant_pct, drop_bid_pct_s, mur_bid_usdt, spoof, m6, m24}`
- **m6/m24** = le résultat à +6h/+24h, remplis au fil du temps, écrits quand m24 arrive.

### 5.3 Profil de liquidité BTC
- `hulk-mexc/scripts/profil_liquidite.py` → `runs/liquidite_profil.json`
- Contient : poc_anchor (64k), value_area [62k, 91,5k], walls {wall_high 82k,
  second_floor 86,5k, floor 61,5k}, verdict texte.

### 5.4 Analyseur de prises (outil)
- `hulk-mexc/scripts/analyser_prises_liquidite.py` — lit les CSVs existants
  (ASPIRATION_CALIB + OBSERVATION_MURS), détecte les prises, calcule descente avant
  + mouvement +1h/+3h, agrège par côté/vitesse/descente.
  Usage : `python3 scripts/analyser_prises_liquidite.py [--seuil 5.0] [--min-mur 2000]`

---

## 6. L'ÉTAT DU SYSTÈME (28/08 18h51 UTC)

- **Moteur paper** : tourne (1 process, lock cohérent, watchdog OK). Dernier état :
  pnl −1,33$, 28 trades, cash 50,60$, positions fermées (tout vendu).
- **Trailing** : actif sur 6 paires (preuve KITE +14,7%).
- **Détecteur accumulation** : actif en observation (0 signal encore — normal, rares).
- **Sondes** : aspiration (moteur, chaque cycle ~20s) + observer_murs (30 min).
- **Pas de process dupliqué** (le journal séparé a été supprimé après vérification).

---

## 7. LA SUITE (ce qu'il faut faire)

### 7.1 Dans 2-3 semaines (point de contrôle)
1. Lire `runs/accumulation_signal.jsonl` : combien de candidats, quel win rate +24h ?
   - **Si win +24h > 55% sur échantillon varié** → l'edge tient → activer le vrai
     trading d'accumulation (le "COUTEAU" backtesté : acheter au creux, sortir au pump).
   - **Si ~50%** → artefact de période → ne rien coder, garder en veille.
2. Refaire tourner `profil_liquidite.py` (les niveaux bougent avec le temps).
3. Refaire `analyser_prises_liquidite.py` (l'échantillon grossit chaque jour).

### 7.2 Idées en attente (non implémentées, à décider)
- **prix_dir (TSMOM) dans couleur_regime.py** comme 5e source : trancherait les ORANGE
  (le cas du 28/08 : ORANGE alors que 4/4 horizons haussiers). Règle proposée :
  le prix (fait) prime sur l'avis IA (opinion).
- **Règle "l'IA ne bloque pas un trend validé"** (clause à documenter).
- **Largeur de marché (breadth)** : % de paires au-dessus de leur MA30.
- **HMM 3 états** : plus tard, si le proxy (TSMOM + liquidité) prouve.
- **Profil de volume intégré au détecteur** : le mur dit OÙ, le TSMOM dit QUAND.

### 7.3 Outils réutilisables créés le 28/08
```
hulk-mexc/scripts/audit_trend_detection.py     # audit des signaux de trend (300j BTC)
hulk-mexc/scripts/backtest_couleur_tsmom.py    # backtest de la couleur TSMOM (HIT/MISS)
hulk-mexc/scripts/backtest_couteau.py          # backtest VANILLE vs COUTEAU vs HOLD
hulk-mexc/scripts/profil_liquidite.py          # profil de volume/liquidité BTC
hulk-mexc/scripts/analyser_prises_liquidite.py # analyse des prises de liquidité
hulk-mexc/docs/AUDIT_TREND_DETECTION_20260828.md  # l'audit détaillé
hulk-mexc/docs/TRANSFERT_IA_20260828.md            # CE document
```

---

## 8. LES CHIFFRES CLÉS À RETENIR (pour ne pas tout relire)

| Fait | Chiffre |
|---|---|
| Réactivité TSMOM 30j au creux du 30/06 | 5 jours (vs 50 pour MA200) |
| Golden cross MA50/200 | inapplicable (jamais repassé haussier) |
| Justesse 7j de tout signal de trend | ≈ 50% = hasard (le court terme est du bruit) |
| Prise du mur sud SEULE → rebond | 50% = pile ou face |
| Descente ≥ 2% + prise sud → rebond | 63% |
| Signal +1h (espérance) | 46% win, moyenne −0,01% = ZÉRO |
| Signal +6h | 55% win, +1,48%, R:R 1,66 |
| **Signal +24h** | **58% win, +4,09%, R:R 3,72** (à confirmer) |
| Ancrage BTC (POC) | 64 000$ |
| Mur de résistance BTC | 82 000$ (vide 82-86k$, toit 88-91k$) |
| Support épais BTC | 61 500$ |
| Positions armées trailing | PYTH, CHIP, HBAR, KITE, RED, XRP |
| Preuve trailing | KITE sorti à +14,7% au lieu de +6% |

---

## 9. NOTES MÉTHODOLOGIQUES (ce qui a bien marché)

1. **La vérification avant de créer** : Christophe a demandé "vérifie s'il y a déjà des
   sondes" → il y en avait → on a supprimé le doublon et utilisé les données existantes
   (~60k lignes). **Toujours chercher avant de créer.**
2. **Win rate ≠ profit** : le 63% de rebond semblait excellent, mais l'espérance à +1h
   était nulle. **Toujours mesurer l'espérance (moyenne × R:R), pas juste le win rate.**
3. **La concentration temporelle** : 60% des signaux sur 2 jours → l'edge peut être un
   artefact de période. **Toujours vérifier la répartition (par jour, par paire).**
4. **Le redémarrage du moteur** : SIGTERM → fin propre du cycle → lock supprimé →
   watchdog relance avec `--resume`. Ne JAMAIS lancer le bot soi-même avec nohup
   (le process meurt avec le shell) et ne JAMAIS toucher au lock à la main sans
   réécrire le bon pid (risque de double-relance).
5. **La phrase qui résume tout** : *le prix (fait) > l'onchain (confirmation) >
   le narratif (bruit). Et on mesure, on observe, on trade — jamais l'inverse.*
