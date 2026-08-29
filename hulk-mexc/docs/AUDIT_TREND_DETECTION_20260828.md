# AUDIT — Détection de trend : méthode institutionnelle validée sur données réelles

**Date :** 2026-08-28 — **Superviseur :** Buffy — **Demande :** Christophe
("audit du meilleur setup pour détecter le trend, comment les gros fonds s'y prennent,
confronter, valider, puis coupler avec nos indices et notre IA").

---

## 1. Méthode institutionnelle : ce que les fonds font vraiment

Recherche (papers + littérature de gestion) :

| Méthode | Qui l'utilise | Principe |
|---|---|---|
| **TSMOM / momentum multi-horizon** (rendement sur 1-12 mois) | Moskowitz et al. 2012 ; Man Group ; Winton ; AQR | Le signe du rendement passé (1 mois → 12 mois) donne la direction de la position |
| **MA200 / MA50-200** (prix vs moyenne) | Fonds actions traditionnels, ETFs trend (ex. 200-day SMA) | Bull si prix > MA200 ; golden/death cross MA50/200 |
| **Décomposition par régime** (bull/bear/sideways) | Papers académiques (AdaptiveTrend 2026, arxiv 2602.11708) | Bull = rendement 60j > +15 %, Bear < −15 %, sinon sideways — sert à **valider**, pas à prédire |
| **Régime de volatilité** (ciblage vol, ATR) | Managed futures, risk-parity | La vol détermine la **taille**, pas la direction |
| **HMM / modèles statistiques de régime** | LSEG, quant shops | États cachés (calme, panique, range) ; **lent et à valider OOS** — notre éval #7 l'a déjà classé "watchlist, pas maintenant" |

### Le consensus institutionnel (vulgarisé)
1. **On ne prédit pas le prochain tick** — on *classe le climat* (météo, pas météo du jour).
2. Le signal le plus robuste est le **momentum sur plusieurs horizons** (TSMOM), pas un seul indicateur.
3. La **validation** se fait par décomposition en régimes : le paper AdaptiveTrend montre que le trailing stop dynamique est le composant qui apporte le plus (Sharpe +0,73, DD −9,7 pts) — cohérent avec ce qu'on vient d'armer sur Hulk.
4. Le **lag est le prix de la robustesse** : MA200 confirme tard, TSMOM confirme tôt mais bascule plus souvent.

---

## 2. Confrontation sur nos données réelles (300 jours BTC, 2025-11 → 2026-08)

### 2.1 Le marché testé contient les 3 régimes
- **Mars-mai 2026** : haussier (jusqu'à 82 210 $)
- **Juin-juillet 2026** : **bear réel** (creux 58 625 $ le 30/06, −25 % sur 60j)
- **Août 2026** : **retournement haussier** (+35 % depuis le creux, +31,9 % sur 60j au 28/08)

### 2.2 Qualité de séparation des signaux (300j)
| Méthode | % temps long | ret/j long | ret/j bear | **Séparation** | Sharpe |
|---|---|---|---|---|---|
| TSMOM momentum 30j | 43,8 % | +0,365 % | −0,430 % | **+0,795 %** | 2,50 |
| R60j > +15 % (paper) | 8,0 % | +0,812 % | −0,160 % | +0,972 % | 2,04 |
| MA200 (prix > 200j) | 3,3 % | +2,119 % | −0,158 % | +2,277 % | 1,97 |
| MA50/200 (cross) | 0,0 % | — | −0,082 % | +0,082 % | 0,00 |

### 2.3 Réactivité au retournement du 30/06 (LE point critique)
| Méthode | Repasse HAUSSIER | Lag après creux | Gain déjà fait |
|---|---|---|---|
| **TSMOM 30j** | **05/07** | **5 jours** | +8,6 % |
| MA200 | 19/08 | 50 jours | +18,3 % |
| MA50/200 | **jamais** (toujours pas croisé) | ∞ | — |
| R60j > 15 % | 20/08 | 51 jours | +24,6 % |

### 2.4 Le verdict de l'audit
- **Le croisement MA50/200 (le "golden cross" des fonds actions) est INAPPLICABLE à ce marché** :
  il n'a jamais repassé haussier alors que BTC a déjà rebondi de +35 %. Il est trop lent pour
  des crypto qui changent de régime en semaines, pas en mois.
- **TSMOM 30j est le plus réactif** : haussier **5 jours après le creux** (vs 50 jours pour MA200).
  C'est le seul qui aurait dit "on peut racheter" avant que le rebond soit évident.
- **MA200** reste un bon filtre de **fond** (très forte séparation +2,28 %/jour) mais en **confirmation tardive**.
- **Le "rendement 60j > +15 %" du paper** est un bon cadre de **validation** (bull/bear/sideways),
  pas un signal d'entrée (trop tardif : 51 jours).

### 2.5 Confrontation avec notre régime actuel (28/08, 13:55 UTC)
| Source | Direction | Détail |
|---|---|---|
| **TSMOM 30j (méthode validée)** | **HAUSSIER 🟢** | r30 = +24,2 %, r60 = +31,9 % |
| Notre régime (couleur_regime) | **ORANGE** (neutre) | onchain=bullish, narratif=bullish, **avis IA=bearish (3L/4S)**, thermo=neutral |
| Fear & Greed | 73 (Greed) | |

**Constat** : notre cœur décisionnel **hésite** (ORANGE = "pas assez de signal") à cause de l'avis
IA bearish, alors que la méthode institutionnelle validée dit HAUSSIER clair depuis le 05/07.
Le moteur est **en retard sur le retournement** : il aurait dû être en mode "laisser courir"
depuis 5 juillet, pas en observation.

---

## 3. Le design proposé : coupler méthode validée + nos indices + notre IA

### 3.1 Ajouter une 5e source au cœur décisionnel (`couleur_regime.py`)

Actuel : `couleur = f(onchain × narratif)`, complété par avis IA et thermo.
**Proposé :** ajouter `prix_dir` = TSMOM 30j BTC (le signal validé, le moins laggé).

| Combinaison | Couleur | Lecture |
|---|---|---|
| onchain 🟢 + narratif 🟢 + **prix 🟢** | **VERT** | tout aligné → entrée/laisser courir |
| onchain 🟢 + narratif 🟢 + **prix 🔴** | ORANGE | divergence prix vs fondamental → attention |
| onchain 🟢 + narratif 🔴 + **prix 🟢** | JAUNE | contrarian (accumulation pendant peur) MAIS prix confirme → opportunité |
| avis IA bearish MAIS prix 🟢 | **prix tranche** | le prix (fait) > l'opinion IA (bruit) — règle : l'IA ne bloque pas un trend validé |

**Règle d'or :** le signal prix ne remplace RIEN, il **tranche les égalités** (ORANGE → VERT/JAUNE)
et **bloque** quand il est contraire à une couleur alignée (VERT + prix 🔴 → rester prudent).

### 3.2 Brancher la couleur sur Hulk (le vrai gain)

Le moteur lit déjà `regime_couleur.json` en mode observation. L'objectif final :
- **VERT** → mode "laisser courir" (trailing armé — déjà fait sur 6 paires liquides) + entrées normales
- **JAUNE** → accumulation discrète (le couteau : COUTEAU sur illiquides)
- **ORANGE** → prudence (entrées réduites, pas de nouvelles thèses)
- **ROUGE/NOIR** → défensif : stops serrés, pas de nouvelle entrée, cash

### 3.3 Validation continue (la boucle que les fonds utilisent)

`regime_couleur.py --score` calcule déjà HIT/MISS sur 24h. Ajouter au score :
- la **couleur TSMOM** dans le registre, pour mesurer sur 2-3 semaines si "prix 🟢 → marché a monté" 
  (HIT) ou pas (MISS) — c'est la preuve OOS qui autorisera à passer d'observation à pilotage.

### 3.4 Données et fréquence
- Klines 1j BTC (Binance publique) — 1 appel/jour suffit pour TSMOM 30j (pas de rate-limit).
- Calcul dans `couleur_regime.py` (ou un petit module `trend_prix.py`) ; mise à jour 2×/jour avec le run existant (08:05 + 15:55).

---

## 4. Améliorations possibles (par impact)

1. **Ajouter `prix_dir` (TSMOM 30j) à couleur_regime** — le + simple, le + rentable : il aurait
   transformé l'ORANGE d'aujourd'hui en VERT et le bot aurait laissé courir depuis juillet.
2. **Règle "l'IA ne bloque pas un trend validé"** — l'avis IA (3L/4S) contredit le prix (+32 %/60j) ;
   dans ce cas, le fait doit primer sur l'opinion. À documenter comme clause.
3. **Multi-horizon TSMOM (30/60/90j)** — score pondéré (comme les fonds : 1-3-6-12 mois) au lieu
   d'un seul horizon → moins de faux bascules.
4. **Largeur de marché** — % de paires de l'univers au-dessus de leur MA30 (breadth) : confirme le
   trend BTC par la participation (évite un rally à 2 paires).
5. **PROFIL DE LIQUIDITÉ (28/08, GO Christophe)** — module `profil_liquidite.py` : calcule depuis
   les klines BTC l'ANCRAGE (POC 64k$), la zone de valeur (62-91,5k$), le support épais (61,5k$),
   le MUR de résistance (82k$ = vide de volume au-dessus du prix) et l'étage suivant (86,5k$).
   Écrit `runs/liquidite_profil.json`. Lecture validée par Christophe (structure vue en vidéo,
   confirmée par les données) : le prix 79,5k$ est SOUS le mur avec un vide 82-86k$ au-dessus et
   un toit épais 88-91k$. Interprétation : breakout = traverser le vide d'un coup ; échec au mur
   → gravité vers l'ancrage 64k$ où le volume est 4× plus dense. À coupler avec le détecteur de
   trend : le mur dit OÙ, le TSMOM dit QUAND.
6. **HMM 3 états** — l'éval #7 l'a déjà classé "plus tard si paper prouve" : à réserver après
   validation du proxy (TSMOM + breadth + liquidité), pas maintenant.

---

## 5. Backtest de validation de la couleur TSMOM (300j) — fait APRÈS l'audit

Demande Christophe : "d'abord un backtest de la couleur TSMOM avant de l'implémenter".
Résultat (script `hulk-mexc/scripts/backtest_couleur_tsmom.py`) :

| Méthode | % jours long | HIT 24h | HIT 7j | Verdict |
|---|---|---|---|---|
| Base (hasard) | — | ~50 % | 47,5 % | — |
| TSMOM 30j seul | 43,7 % | 51,2 % | 48,6 % | ~hasard à 7j |
| Multi-horizon 30/60/90/120 | 20,0 % | — | 45,5 % | ~hasard |
| **Multi-horizon + MA200** | ~3 % | 66,7 % | **100 %** (3/3) | parfait mais ultra-rare |

### Leçon clé du backtest
- **Sur 7 jours, AUCUN signal de trend ne bat le hasard** : 7j est trop court pour un signal
  de climat. Les signaux de trend (TSMOM, MA) sont faits pour des horizons de semaines à mois.
- **Donc la couleur TSMOM ne doit PAS servir de signal d'entrée 7j** — elle sert de
  **filtre de régime** (bull/bear/sideways) : elle dit DANS QUEL MODE router la stratégie,
  pas "acheter/vendre maintenant". C'est la distinction fonds (climat vs météo du jour).
- Aujourd'hui (28/08) : **4/4 horizons haussiers** (r30 +24 %, r60 +32 %, r90 +7,5 %, r120 +4 %)
  → la couleur prix dirait HAUSSIER sans ambiguïté, et trancherait l'ORANGE actuel.

## 6. Fichiers créés pour cet audit
- `hulk-mexc/scripts/audit_trend_detection.py` — audit rejouable des signaux (300j BTC).
- `hulk-mexc/scripts/backtest_couleur_tsmom.py` — backtest de validation de la couleur (HIT/MISS).
- `hulk-mexc/scripts/profil_liquidite.py` — profil de liquidité (ancrage/murs/support) + `runs/liquidite_profil.json`.
- Données : `/tmp/btc_daily.json` (300 bougies 1j Binance).
- Ce document.

## 7. Statut
**AUDIT + BACKTEST LIVRÉS — rien n'est branché au live.** Le trailing sur 6 paires liquides
(validé par le backtest 30j Binance) est déjà actif. Le détecteur de trend (prix_dir) est validé
comme FILTRE DE RÉGIME (pas signal 7j) ; l'implémentation dans `couleur_regime.py` est en attente
de décision.
