# 🎯 SET-UP OPÉRATIONNEL — RED (RedStone) — mesuré 30/08/2026 14:11Z

> Décision commune : on ne câble RIEN aveuglément. On mesure le comportement réel et on
> définit le protocole d'entrée/sortie avec la règle de la famille : **fenêtre temporelle +
> déclencheur de micro-structure, jamais l'heure seule.**

---

## 📏 MESURE DU COMPORTEMENT (fraîche, 14:11Z)

### 1. Signal précurseur (divergence, run rejoué à l'instant)
| Volet | RED maintenant | Lecture |
|---|---|---|
| Signal précurseur (m6→delta panier +4h) | **+0.14 → 🟡 léger achat** | Repasse acheteur léger (retombé de +0.16 à +0.14, sous le seuil LEADER 0.15) |
| Timing (corr croisée) | corr 0.63 · **lag +4h** | RED **suit** le panier — retarde de 4h, pas un leader |
| Divergence actuelle | m6 6h **2.46** vs passé **4.01** | DIV réduite → le "pump" RED s'essouffle vs son passé |
| Gating temporel | m6 jour 4.12 · nuit 3.50 · 0% pics>6% | ⚪ distribué — ni diurne ni nocturne dominant |

→ **Lecture : RED est un suivard du panier, mode achat léger, amplitude intraday marquée.**
C'est un profile de **set-up horaire** (cycle), pas de signal précurseur global.

### 2. Comportement prix (fenêtre 6h en direct, 08:07→14:06Z)
```
08h avg 0.10876  09h avg 0.10921  10h avg 0.10953  11h avg 0.10941
12h avg 0.11030  13h avg 0.11068  14h avg 0.11082
min 0.10854 · max 0.11129 · range 6h = 2.53% · prix actuel ~0.11076
```
→ RED **monte en continu depuis 08h** et tape déjà ~0.111, **juste à l'entrée de la fenêtre où
le modèle attend le creux (15-16h)**. Concrètement : la paire est en **fin de montée de matinée
plutôt qu'en creux** — c'est le point de prudence du moment, pas un point d'achat opportun.

---

## 🔗 RED vs BTC vs ETH — le pattern de dé-corrélation (découverte 30/08)

**Corrélations horaires (prix, 3 jours) : RED~BTC = +0.07 · RED~ETH = −0.01 · BTC~ETH = +0.98**
→ RED est quasi **DÉ-CORRÉLÉ** de BTC/ETH (qui, eux, bougent ensemble à 0.98). Pour le
portefeuille, RED = un actif « d'un autre marché » : bonne dose de diversification.

**Par phase :**
| Phase | RED~BTC | RED~ETH | Lecture |
|---|---|---|---|
| MATIN 08-13h | **−0.85** | **−0.89** | ❗ **INVERSEMENT corrélé** : quand BTC monte le matin, RED baisse (et vice-versa) |
| CREUX 14-17h | +0.10 | −0.01 | Dé-corrélé : le creux de RED se fait **en solo** |
| NUIT 21-05h | +0.60 | +0.59 | RED suit moyennement le rebond général de nuit |

**Niveau relatif moyen (100 = base) :**
```
           RED    BTC    ETH
MATIN     100.5   99.9   99.9     <- RED fort quand BTC/ETH plats
CREUX      98.0   99.7   99.9     <- RED plonge EN SOLO, marche stable
SOIR       98.2   99.3   99.3
NUIT      100.5  100.1  100.0     <- RED remonte, marche aussi
```

**Conséquence pour le set-up :**
1. ✅ **Le creux 15-16h de RED est indépendant du marché** (BTC/ETH restent stables). Le set-up
   tient même si le panier vacille peu → vraie diversification.
2. ⚠️ **Attention au matin (08-13h) : RED est inversement corrélé à BTC.** Une position RED en
   ce moment peut compenser OU s'opposer au reste du portefeuille — à connaître pour ne pas
   lire un faux signal (un repli BTC ne tire pas forcément RED vers le bas le matin).

---

## 🧭 LA LOGIQUE DU SET-UP (règle famille)

### Objectif
Exploiter le cycle intraday de RED : **acheter la zone creux 15-16h UTC, revendre le pic de
nuit 01-05h** — mais SEULEMENT quand la microstructure confirme (jamais à l'heure seule).

### Le cadre d'entrée (tout doit être vrai)
1. **Fenêtre** : on autorise l'entrée **uniquement 14h–17h UTC** (interdiction hors fenêtre).
2. **Déclencheur** : la **poussière (tx fantômes) < 15%** (assèchement = vraie accumulation,
   pas de panique) ET le **mur bid 45K$ est testé et tient** (le MM absorbe sans fuir).
3. **Garde-fou volatilité** : bloquer l'entrée si le **volume 15 min > 3× la moyenne 24h**
   (signal de panique, pas un creux sain).
4. **Exécution fragmentée** : entrer en **3 tranches** (−1%, −2%, −3%) sous le prix médian
   de la fenêtre ; stop dur dynamique = **1,5× le range de la bougie 15 min**.

### Le cadre de sortie
- **Sortie partielle au pic de nuit (01h–05h)** : scaling out — dégager une partie vers
  0.110-0.112+, garder le reste derrière le trailing de Hulk.
- Le stop/rip **existant de Hulk** gère la suite (RED ultra-volatile, dd15 22,86%).

### Condition de remise en cause
- **Invalider** si RED casse le plancher **0.103-0.104** hors fenêtre (le modèle horaire tombe).
- **Arrêter le set-up** si les frais réels MEXC + slippage dépassent ~1% nets (marge 2,4% → net
  < 1,5% ne vaut pas le risque).

---

## ⏱️ RECOMMANDATION IMMÉDIATE (14:11Z)
RED est à **0.11076, en fin de montée**, à l'entrée de la fenêtre de creux attendu. **On n'achète
pas ici** : le déclencheur « poussière sèche + mur testé » n'est pas confirmé et le prix est
haut de cycle, pas bas. On **attend la fenêtre 15-16h** et on regarde si RED retombe dans la
zone **0.107-0.109** avec poussière basse → c'est là que l'entrée devient valide.

---

## 🔌 DÉCIDÉ (pas câblé aujourd'hui)
- RED reste **en seed** (bag 10$), rien d'activé.
- On **mesure le set-up en observation** : capter poussière + mur + volume 14-17h sur RED.
- **Prochaine validation dans ~7 jours** pour confirmer le cycle (règle Christophe : ce qui vaut
  un temps peut ne plus valoir).

## Archives
- Signal divergence rejoué : `hulk-mexc/runs/DIVERGENCE_20260830_1411.md` (RED 🟡 léger achat 0.14)
- Fiche pattern + famille : `Crypto_Projet/FICHE_PATTERN_SETUP_RED_20260830.md`,
  `Crypto_Projet/SYNTHESE_RED_SETUP_FAMILLE_20260830.md`