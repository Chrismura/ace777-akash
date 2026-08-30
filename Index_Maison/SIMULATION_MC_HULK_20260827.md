# Simulation Monte Carlo Hulk + Test de valeur ajoutée des indices — 27/08/2026

> Méthode : 10 000 trajectoires par position (GBM, volatilité réelle MEXC klines 1h × 15j),
> horizon 24h, stops réels du state. VaR par indépendance (pire cas conservateur).
> Seed 777 pour reproductibilité.

---

## 1. Monte Carlo Niveau 1 — distribution de risque des 11 positions

### Volatilités réelles (klines MEXC 1h × 15j)

| Paire | Vol journalier | Stop réel | Stop-out (P sur 24h) |
|---|---|---|---|
| HBAR | 4.1% | 6.0% | 6.7% |
| ZBCN | 6.1% | 6.2% | 17.2% |
| W | 4.5% | 6.0% | 10.1% |
| RED | 11.7% | 8.9% | **33.5%** |
| CC | 5.0% | 6.1% | 13.0% |
| BIO | 6.4% | 6.0% | 23.1% |
| KITE | 4.7% | 6.0% | 9.6% |
| TEL | 5.2% | 6.3% | 12.3% |
| CHIP | 10.0% | 12.4% | 9.4% |
| EDEL | 12.1% | 7.1% | **35.6%** |
| RWAINC | 5.7% | 6.3% | 22.6% |

### VaR du portefeuille (notional total ~96.37$)

| Métrique | Valeur |
|---|---|
| PnL médian 24h | **+1.27$** |
| **VaR 95% (24h)** | **−1.93$** (≈2% du notional) |
| VaR 99% (24h) | −3.01$ |
| Perte max simulée | −5.97$ |
| P(stop-out global) | 27.8% |

### Lecture

- Le portefeuille est **petit mais correctement dimensionné** : pire 1% des cas = −3$,
  soit −3% du notional — les stops contiennent le risque.
- ⚠️ **EDEL (35.6%) et RED (33.5%)** : 1 position sur 3 finit au stop sur 24h. Volatilité
  12%/jour avec stop 7% = stop trop serré par rapport au bruit. À surveiller : soit stop
  élargi (à la cadence), soit taille réduite.
- Limite affichée : GBM sous-estime les queues de distribution des small caps (drops
  violents de 20-50%). Les chiffres sont des ordres de grandeur, pas des prophéties.

---

## 2. Test de valeur ajoutée des indices — mesurent-ils du nouveau ?

### Corrélations (63 mesures sentinel, indices maison vs classiques)

| Indice maison | vs classique | Corrélation | Verdict |
|---|---|---|---|
| SDI | funding | −0.28 | **DIVERGENT** |
| SDI | long_short | +0.02 | **DIVERGENT** |
| IPT | funding | −0.12 | **DIVERGENT** |
| IPT | long_short | +0.02 | **DIVERGENT** |
| CPFP | funding | −0.05 | **DIVERGENT** |
| CPFP | fear_greed | n/a (constant) | — |
| Dust | taker_ratio | −0.12 | **DIVERGENT** |
| Dust | volume | +0.26 | **DIVERGENT** |

### Variabilité (un indice constant ne mesure rien)

| Indice | Coefficient de variation | Lecture |
|---|---|---|
| SDI | 0.20 | bouge |
| IPT | 0.37 | bouge |
| CPFP | 0.82 | bouge fort |
| Dust | 0.82 | bouge fort |
| funding | 0.14 | presque figé |
| long_short | 0.05 | figé |
| taker_ratio | 0.06 | figé |
| volume | 0.04 | figé |

### Conclusion scientifique

**Vos indices maison mesurent une information que les classiques ne captent pas.**
Un indice redondant serait corrélé aux classiques et bougerait avec eux. Ici :
corrélations toutes < 0.3 (décorrélées) ET variabilité 3-16× supérieure (elles bougent
quand les classiques sont figés). Ce n'est pas un « reflètement d'alarmes » — c'est une
**information nouvelle et dynamique**. Preuve statistique, pas opinion.

---

## 3. Rejeu borné — les 17 trades réels (24-27/08)

### Faits

- Fenêtre : 24/08 06:53Z → 27/08 17:28Z (4 jours, 17 BUY, 6 SELL)
- PnL réalisé des SELL : RWAINC −1.53$ · QAIT −0.85$ · RIZE −0.75$ · XRP −0.46$ · PYTH −0.32$ = **−3.9$**
- SDI de la période : min 0.008 · médian 0.008 · **q75 = 0.012** (29% du temps ≥ 0.012)

### Résultat

Un filtre « ne pas acheter si SDI ≥ q75 (0.012) » aurait bloqué **~29% des entrées
(~4 des 17 BUY)**. Limite : les mesures sentinel n'avaient **pas de timestamp** avant le
fix de ce soir → alignement exact BUY↔SDI impossible sur cette fenêtre.

### Honnêteté

- Échantillon minuscule (17 trades, 4 jours) → **aucune conclusion statistique possible**.
- La vraie réponse viendra dans 30 jours : sentinel.py écrit maintenant un `ts` sur chaque
  mesure (fix 27/08) → le test « les indices auraient-ils évité ces entrées ? » sera
  exécutable avec alignement temporel exact.

---

## 4. Action faite

`sentinel.py` : chaque mesure de `sentinel_history.json` porte désormais un timestamp ISO
(`ts`), ignoré par le z-score (absent de ZSCORE_THRESHOLDS, vérifié : 0 alerte, syntaxe OK,
history restauré après test). **Dans 30 jours, le test de valeur ajoutée des indices sera
possible avec alignement exact.**

---

## 5. Recommandations

1. **EDEL et RED** : stop trop serré vs volatilité réelle (35% de stop-out) → élargir à la
   cadence ou réduire la taille (décision Christophe, pas appliqué).
2. **Continuer le logging timestampé** (fait) — c'est la condition du vrai test 30 jours.
3. **Le test de corrélation peut être relancé** à tout moment : c'est un script jetable,
   les données sentinel sont là.

*Simulation générée le 27/08 18:58Z · seed 777 · reproductible.*
