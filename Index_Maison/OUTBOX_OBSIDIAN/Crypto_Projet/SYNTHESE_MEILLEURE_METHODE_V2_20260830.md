# SYNTHÈSE V2 — LA MEILLEURE MÉTHODE D'ANALYSE (prompt neutre, 30/08/2026)

**Pourquoi V2 :** Christophe a corrigé le tir — le 1er prompt leur avait donné notre méthode
(et ils ont répondu « à notre méthode »). Le 2e prompt (GO Christophe) leur demande LA méthode
depuis zéro, sans rien leur révéler de ce qu'on fait. Clause permanente gravée DANS le prompt
(« prouve la meilleure logique, proposer est attendu, avis strict »).
Session `CONSULTATION_MEILLEURE_METHODE_20260830/` (DEEPSEEK + ULTRA + CODEUR, provider Gemini).

---

## 🏆 LE CONSENSUS — la méthode pro en une phrase

> **N'analyse pas ce qui est AFFICHÉ (le carnet), analyse ce qui est CONSOMMÉ (les trades
> exécutés et leur impact réel sur le prix).**

Les 3 disent la même chose, avec des mots différents : sur des micro-caps MEXC, **le carnet
d'ordres est majoritairement du spoofing/layering** — s'y fier pour décider est « un suicide
statistique » (DEEPSEEK). La vérité est dans le **flux de transactions exécutées**.

## 📐 LES 4 DIMENSIONS DE LA NORME (consensus des 3)

| Dimension | Métriques clés | Pourquoi |
|---|---|---|
| **A. Liquidité réelle** | **Amihud Illiquidity Ratio** (impact prix par $ de volume) + effective spread (Roll/Corwin-Schultz) + profondeur ±1-2% | LA métrique reine : peux-tu sortir 10 000$ sans casser le prix ? |
| **B. Volatilité/régime** | **Parkinson/Garman-Klass** (High/Low) + ratio de variance + realised vol sur barres de VOLUME | Capture la vraie amplitude, pas les bougies vides |
| **C. Flux/toxité** | **VPIN** (probabilité de flux informé) + **Trade Flow Imbalance / Trade Sign Delta** (acheteurs vs vendeurs agressifs, règle Lee-Ready) | Détecte l'accumulation cachée avant la cassure |
| **D. Friction d'exécution** | Market impact empirique par taille d'ordre | Ne pas s'auto-impacter à l'entrée/sortie |

**Fréquence : VOLUME BARS (ex : 1 barre = 0,5-1% du volume journalier moyen), PAS du temps
calendaire (1 min = hérésie sur small caps).**

## 🗑️ CE QUI EST DU BRUIT SUR MEXC (les 3 — sans concession)

| Métrique | Verdict | Pourquoi |
|---|---|---|
| **Carnet L2 affiché (murs, profondeur)** | ❌ BRUIT PUR | Spoofing permanent, ordres fantômes qui disparaissent |
| **Volume brut affiché** | ❌ BRUIT PUR | Wash trading endémique |
| **RSI / MACD / oscillateurs 1-5 min** | ❌ BRUIT PUR | Lagging, faux signaux constants |
| **VWAP/TWAP classiques** | ❌ BRUIT | Ratent les retours sur pumps & dumps |

## ✅ CE QUI DISCRIMINE (le vrai signal)

- **Amihud Illiquidity Ratio** (×3 consensus)
- **VPIN / Trade Sign Delta** (agressivité réelle taker) (×3)
- **Volatilité Parkinson** (×2)
- **OBI ±0,5-2%** (seulement les 5 premiers ticks — au-delà = vent) (ULTRA)
- **Rolling Beta vs BTC** (l'actif bouge-t-il tout seul ou suit-il le marché ?) (ULTRA)

## 🔧 ARCHITECTURE (consensus — pas d'usine à gaz)

- **WebSocket persistant MEXC** : flux trades (`deals`) + carnet L2 limité (5-10 niveaux) — 1 connexion pour 20 paires, zéro risque de rate-limit REST.
- **Stockage** : **DuckDB + Parquet** (DEEPSEEK, ULTRA) ou TimescaleDB (codeur) — 10 000 lignes/jour = < 50 Mo/an.
- **Calcul** : rolling windows (1h/4h/24h) sur barres de volume → matrice de set-up.

---

## 🎤 MON AVIS STRICT (clause permanente — avis franc, pas de complaisance)

**Ce que je retiens comme VRAI et ACTIONNABLE :**

1. **Ils ont raison sur le point le plus important** : le carnet affiché de MEXC est du bruit,
   la vérité est dans le **flux exécuté**. Notre mur 45K$ « réel » de RED n'est qu'un mur
   affiché — il peut être retiré en 1 seconde (déjà dit par la famille hier). **Le passage à
   la mesure du flux exécuté (trades) + Amihud est LA direction à prendre.**

2. **L'Amihud Illiquidity Ratio est la métrique qui manque le plus à notre système.** On a le
   prix, les murs, la poussière — mais pas « combien le prix bouge par dollar de volume ».
   C'est LA question pour un portefeuille de micro-caps : peux-tu sortir sans te faire
   massacrer ? **À ajouter.**

3. **Le volume bars vs time bars est une refonte profonde de notre collecte** (croisement à
   1 min). C'est un chantier technique sérieux — mais il répond exactement à la critique
   « notre horloge 1 min est mauvaise » d'hier. À planifier, pas à bâcler.

4. **⚠️ Point de vigilance honnête (mon désaccord nuancé)** : ils décrètent « carnet = bruit
   pur » — c'est vrai à l'échelle du HFT tier-1, mais chez nous le mur + spoof nous ont déjà
   servi (piège spoof évité sur BTC). La vérité est au milieu : **le carnet est du bruit si on
   le prend pour de la profondeur réelle ; il reste utile si on le mesure comme TENSION
   (spoof, retraits) — pas comme support.** Je garde le spoof, je dégrade le « mur = support ».

5. **Ce qui manque chez nous** (à ajouter au suivi RED comme test) : Amihud, Trade Sign Delta
   (agressivité taker), Parkinson. Ce sont les 3 métriques pro les moins coûteuses à calculer
   depuis notre flux existant.

**Proposition concrète (GO-sized) :** enrichir `suivi_setup_red.py` avec **Amihud + Trade Sign
Delta + Parkinson** (calculables depuis les trades/klines déjà capturés) et les comparer à nos
métriques actuelles sur RED pendant les 7 jours d'observation. Si elles discriminent mieux →
généraliser au portefeuille.

---

## Archives
- Avis bruts : `Index_Maison/scripts/CONSULTATION_MEILLEURE_METHODE_20260830/AVIS_{DEEPSEEK,ULTRA,CODEUR}.md`
- Script : `Index_Maison/scripts/consulter_meilleure_methode_analyse_20260830.py` (prompt neutre validé Christophe)