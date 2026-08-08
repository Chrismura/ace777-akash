# Éval #9 — @ridark_eth « Ultra-Precision Polymarket Sniper » ($424k / mois)

- **Date :** 2026-07-28
- **Compte :** [@ridark_eth](https://x.com/ridark_eth) — content Web3 / bots / Poly (bruyant, farm engagement)
- **Post :** wallet **JnStTrdrBnusFnd** — +$424,734 / mois · max win $25.3K · 87 preds · créé mars 2026 · « Rare / Safe Predictions / Ultra-Precision Sniper »
- **Famille :** même usine que les autres posts Ridark (ex. « 5m sniper $150k / semaine », Claude bots, formules OU/OBI copiées-collées)

## Focus Christophe = **SNIPER**, pas IP

Ce qui intéresse : **peu de tirs, haute précision, mispricing**, pas le thermomètre liquidité.

### Phrase clé du thread (relecture)

> *Market Says 1%. Reality Delivers 0.43%. Build the Bot That Actually Knows the Difference.*

Ça, c’est le **vrai** sniper — pas le screenshot $424k.

| | |
|--|--|
| Market 1 % | Prix du share ≈ cote implicite (foule / book) |
| Reality 0.43 % | Fréquence **empirique** (historique / modèle) du même événement |
| Différence | Edge de **calibration** : où la cote ≠ la base rate |
| Bot | Mesure les deux en continu ; trade seulement l’écart (avec frais / latency) |

**Sens du trade :** si le marché dit 1 % et que la réalité sort à 0.43 %, le « Yes » est **trop cher** → fade (vendre Yes / acheter No), pas « sniper le 1 % parce que rare ».  
L’inverse (marché 0.43 %, réalité ~1 %) = acheter le sous-coté.

Vulgarisé : le sniper ne « prédit » pas — il a une **table de vérité** et tire quand le board ment.

### Pattern sniper (à garder comme idée)

| Élément | Vulgarisé |
|---------|-----------|
| Calibration gap | Cote vs fréquence réelle (1 % vs 0.43 %) |
| Rare | 87 coups / mois ≠ spam 30k micro-bets — seulement les gaps |
| Entry « discount » | Acheter le côté **sous-coté** (souvent ~37–52¢ dans leurs autres threads 5m) |
| Fenêtre courte | BTC Up/Down 5m — edge microstructure + base rate, pas « BTC 100k » |
| Zero emotion | Exécution règle ; pas le récit de la semaine |
| Mispricing foule | Panic sell / overreaction → même famille **dip Hulk** / panique board (éval #3) |

→ Sniper = **attendre le coup où le book ment vs la réalité mesurée**, tirer, sortir. Aligné ACE/Hulk « gates + size », pas FOMO.

### Pattern marketing (à jeter)

| Red flag | Pourquoi |
|----------|----------|
| +$424k / mois screenshot | Non vérifié ; survivorship ; bots ; wash ; farm followers |
| Compte créé mars 2026 + PnL monstrueux | Trop beau / trop vite |
| « Safe predictions » | Oxymore trading — safe ≠ $25k win |
| Même auteur enchaîne $150k/semaine, Claude 6 bots, formules PhD | Usine à contenu, pas playbook audit |
| Nom wallet *BonusFnd* | Vibes promo / farm |

## Part 7 — « The Complete Bot (Architecture and Worked Example) »

Lu comme **bloc architecture** (pas comme code à cloner).

### Ce que cette partie vend
Assembler le sniper en couches + un exemple chiffré bout-en-bout :

```
[feeds] → [fair / reality p] → [market p] → [edge?] → [risk] → [exécute] → [log/fills]
```

| Couche | Job |
|--------|-----|
| Data | Book Poly (CLOB WS) + discovery (Gamma) + éventuellement spot BTC |
| Reality | Estime 0.43 % (base rate / modèle) |
| Market | Lit 1 % (mid / best ask) |
| Edge | Gap > frais + slippage + seuil |
| Risk | Size, max pertes, skip si depth morte |
| Exec | Ordre + paper/live |
| Audit | Fills = vérité (culture ACE) |

**Worked example** = marcher un trade : cote 1 ¢, réalité 0.43 %, frais X → edge net Y → size Z.  
Utile pédagogiquement ; les chiffres du thread ≠ edge live garanti.

### Prendre / laisser (Part 7)

| Prendre | Laisser |
|---------|---------|
| Découpage modular (comme swarm cold/hot) | « Complete bot » = alpha prêt |
| Edge **après** frais/slippage dans l’exemple | Copier l’archi GitHub promo sans paper |
| Exemple chiffré comme **template de checklist** | Croire que Part 7 = le wallet $424k |

Aligné ACE : champion intouchable ; un jour module Poly paper = même schéma feeds→edge→risk→exec→CSV.

## Code — `ProbabilityBot` (Beta–Binômiale) — **OUI utile**

Snippet Christophe. Cœur « reality vs market », pas le PnL viral.

| Méthode | Job |
|---------|-----|
| `fit_prior` | α,β depuis fréquences de buckets (moments) |
| `estimate(k,n)` | Reality = moyenne Beta + IC (ex. 95 %) |
| `edge(..., market_price)` | `prob − price` ; `tradeable` si `width < 0.20` |

**Solide :** bayésien (pas surconfiant à n petit) · IC = gate sniper · edge = calibration gap.  
**Trous :** `min_trials` déclaré mais **non branché** · pas de frais/slip · pas de signe buy/fade · pas d’exec CLOB · k/n peut être hors-régime.

| Prendre | Laisser |
|---------|---------|
| Spec / proto **paper** Poly | Live demain / copier wallet |
| `width` comme frein (style RED/heat) | Croire mean Beta = vérité fills |
| Doctrine sniper rare + seuil | Brancher sur champion ACE |

**Guillemets :** piste `Polymarket / prediction` (éval #3) — angle sniper + Beta gate.

## Part 5 — `bucket_key` (ce qui compte comme évidence)

```python
# major|underdog|mid|level  ← 4 axes concaténés
# tier · favoritism(price) · time · goal_diff state
```

**Job :** ne compter dans k/n **que** les situations « mêmes empreintes ».  
Sinon tu estimes précisément **la mauvaise chose**.

| Axe | Vulgarisé |
|-----|-----------|
| `league` tier | Quel monde (major ≠ minor) |
| `favoritism` via price | Qui est favori / underdog (cote) |
| `minute` | Moment du match |
| `goal_diff` state | Score déjà décanté ou égalité |

Exemple thread : `major|underdog|mid|level` → 8/28.

### Solide
- Features qui **changent** vraiment la proba (pas décoration)  
- Clé stable = lookup index rapide  
- Couple naturel avec **fallback** (lâcher un axe si n < min_trials)

### Pièges
| | |
|--|--|
| Trop d’axes | Buckets vides → variance / faux 100 % |
| Trop peu | Tu mélanges des mondes ≠ |
| Features crypto | League/minute/goal ≠ BTC 5m — **rebrander** (ex. vol régime \| hour \| funding \| side) |
| Look-ahead | Ne pas mettre l’outcome dans la clé |

## Part 6 — Calibration (Brier + log loss)

Oui lu. Prouver que « 26 % » **arrive vraiment ~26 %** du temps — sinon tu sizes sur du mensonge.

| Outil | Job vulgarisé |
|-------|----------------|
| Reliability diagram | Par bins : predit vs réalisé → doit coller la diagonale |
| `brier_score` | MSE des probas — plus bas = mieux ; baisse d’edge avant le PnL |
| `log_loss` | Punit fort le **très sûr et faux** (0.99 qui rate) |
| Platt / isotonic | Recalibrer si biais systématique (held-out) |

```python
# Brier = mean((p - o)^2)
# LogLoss = -mean(o*log(p) + (1-o)*log(1-p))  # clip anti log(0)
```

**Doctrine :** estimateur sans calibration live = spreadsheet déguisé.  
Couple ACE : comme CSV fills > storytelling — ici Brier/logloss > « joli posterior ».  
Piège : bons scores en backtest + look-ahead dans buckets = glow puis collapse live.

```python
# spécifique → plus gros → GLOBAL si rien n’atteint min_trials (défaut 8)
```

**Job :** ne jamais fabriquer une « distro » avec 3 points. Si le bucket fin est trop maigre, **remonter** d’un cran (lâcher un axe), jusqu’à la base rate globale.

| Étape | Effet |
|-------|--------|
| `bucket_hierarchy` | Du plus précis au plus flou |
| `n >= min_trials` | Seuil discipline (le `8` du `ProbabilityBot`) |
| `GLOBAL` | Filet : « underdogs en général » si tout est thin |

C’est le **partial pooling** du thread : le spécifique emprunte au général jusqu’à avoir assez de preuves.

**Solide :** branche enfin `min_trials` (absent de `edge()` nu) · anti blow-up thin bucket.  
**Piège :** ordre de la hiérarchie (quel axe lâcher en premier) = design, pas magie ; GLOBAL trop large = biais.

Couple obligatoire avec `bucket_key` + IC width.

Texte thread (Steps 1–5). **Math vérifiée OK.** C’est *le* playbook sniper en clair.

| Step | Chiffres | Vulgarisé |
|------|----------|-----------|
| Bucket | major\|underdog\|mid\|level · 8 wins / 28 | Index de familles d’événements |
| Prior | Beta(2,8) → base rate 20 % | « Les underdogs de cette famille gagnent ~1/5 » |
| Naive | 8/28 = **28.6 %** | Fausse confiance |
| Posterior | Beta(10,28) → **26.3 %** | Shrink vers 20 % ; poids data **74 %** (28/38) |
| IC 95 % | **13.8 % – 41.2 %** (width 0.274) | Conviction moyenne, pas un lock |
| Market | YES **0.22** | |
| Edge | 0.263 − 0.22 = **+4.3 ¢** | Lean ; IC **contient** encore 0.22 → pas hammer |
| Size | Petit + Kelly haircut sur width | Pas le camion |
| Trap n=3 | Naive 100 % → Bayes ~38 % · width ~0.50 | `tradeable=False` sur width — sauve le blow-up |

**Loop entier :** ingest → bucket → count → posterior + IC → vs market → size par width → repeat.

### Mapping ACE / Hulk / Poly

| Exemple | Chez vous |
|---------|-----------|
| Bucket index | Comme paniers / régimes (pas un seul « BTC up ») |
| Shrink + IC | Anti-overfit / anti-FOMO |
| Edge 4 ¢ + width large | SKIP size grosse (gates) |
| Width trap | = frein RED / min_trials — **garder** |
| Répéter sur events | Cold path multi-marchés un jour |

**Décision :** ce loop = **spec sniper canonique**. Paper Poly seulement si GO ; pas live ; pas champion.
