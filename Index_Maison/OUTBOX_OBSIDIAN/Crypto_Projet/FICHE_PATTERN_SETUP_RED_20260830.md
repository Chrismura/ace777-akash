# 📌 FICHE PATTERN & SET-UP — RED (RedStone) — 30/08/2026

> **Objet :** pattern de prix intraday et set-up de gestion, trouvés sur **nos propres données**
> (`croisement_contexte.jsonl`, 2238 points REDUSDT sur 3 jours — 27→30/08), au même
> standard que la fiche QAIT/plancher et l'approche "contrôle l'amplitude".
> Données fraîches vérifiées à 13:48Z.

---

## 🪨 CE QU'EST RED = RedStone (pas juste un ticker)

| Fait | Détail | Source |
|---|---|---|
| **Projet réel** | **RedStone** — oracle blockchain (fournit des données de prix fiables aux dApps/DeFi) | MEXC, CoinGabbar |
| **Secteur** | Oracles = **infra critique** de la DeFi (le même métier que Chainlink) | MEXC |
| **Prix actuel** | **0.10741 USDT** (13:48Z) · market cap **~44,9 M$** | MEXC live |
| **Référence moteur** | `REDUSDT`, seedée **10$** dans le portefeuille (bag, pas encore achetée par Hulk) | state 12:13Z |

→ C'est une **petite cap real-economy/infra** (oracle), pas un meme. Volatile par nature :
les oracles se financent pendant les cycles volatils, pas dans les marche-plats.

---

## 🔍 LE PATTERN DÉCOUVERT (sur 2238 points, 3 jours)

### 1. Un cycle intraday très marqué : creux en JOURNÉE, pic en SOIRÉE/NUIT

Moyenne du prix par heure UTC (ventilé sur 3 jours — toutes les valeurs en USDT) :

```
   15-16h  ██  INDT 0.1062-0.1068   ← LE CREUX (pire moment: 15-16h UTC)
   14h     0.10719
   19h     0.10704                 ← début de remontée
   20h     0.10751
   21h     0.10881  ‾‾‾ remontée
   22h     0.10917
   23h     0.10887
   00-04h  0.1091-0.1105  ← Pics (01h/04h = les plus hauts)
```

**Lecture claire :**
- **Le creux moyen se situe entre 14h et 19h UTC** (prix moyen 0.10620-0.10683), **pire à 15-16h** (0.1062).
- **Le pic moyen se situe entre 21h et 05h UTC**, **meilleurs à 01h et 04h** (0.1096-0.1105).
- L'écart typique jour→nuit : **~2,4 à 2,8%** entre moyennes — répété chaque journée
  (28/08 : 10,0% de range sur 24h ; 29/08 : 7,1% ; 30/08 : 3,0%).

### 2. C'est une paire ultra-volatile par rafales (ni continue, ni calme)

| Métrique | Valeur | Traduction |
|---|---|---|
| **dd15 moyen** | **22,86%** | En 15 min, RED bouge souvent ≥ 20% dans la journée — gros coups de vente/d'achat |
| **move6h moyen** | 3,8% (max 6,8%) | Tendance 6h bien présente |
| **Range total 3 jours** | **12,1%** (0.102→0.114) | Ampleur du cycle global |
| **Régimes** | 1501× COOLING · 644× IMPULSE_WAIT · 93× IMPULSE | Le plus souvent "pause" mais **rafales IMPULSE concentrées 13→17h UTC** |

### 3. Le régisseur : les IMPULSE arrivent EXACTEMENT dans la fenêtre de creux

Comptage des points en régime **IMPULSE** par heure (c'est LE signal clé) :

```
13h:  6     14h: 15    15h: 30    16h: 40    17h: 2
```

→ **Les 30-40 IMPULSE (rafales) se concentrent à 15-16h UTC, pile quand le prix est au creux.**
C'est le moment où ça **déprime** — typiquement un marché conduit par des ordres institutionnels
asiatiques/algorithmiques qui larguent en pleine journée asiatique, puis la paire se refait
en soirée/nuit européenne+américaine.

### 4. Les murs et la poussière (nos artisanal metrics)

| Donnée | Nuit (pic) | Jour (creux) | Lecture |
|---|---|---|---|
| Mur bid max | 45 240 $ (constant) | 45 240 $ | **Mur d'achat stable et réel** — spoof faible (1,67%) → pas une façade |
| Poussière (tx fantômes) | **17,8%** | **20,2%** | Légèrement plus d'activité cachée pendant les creux |
| Integer wall | 0.97-0.99 | 0.97-0.99 | Mur solide en permanence |

→ Le mur d'achat soutient la paire même dans le creux de 15-16h → la zone de creux est
**un plancher technique** : le mur absorbe et la paire repart en soirée.

---

## 🎯 LE SET-UP (comment exploiter ce pattern avec Hulk)

Ce que cela veut dire pour **notre portefeuille** (RED seedée 10$, Hulk la gère) :

### Pour une entrée longue / accumulation
- **Typiquement favorable 15-16h UTC** (creux intraday + IMPULSE de vente + mur qui tient).
  Un achat près de 0.106-0.107 (zone creux) maximise la marge avant le rebond de nuit.
- **Réserve de prudence** : RED est ultra-volatile en 15 min (dd15 22,86%) → **pas d'entrée
  forcée**, attendre la conjonction creux + mur présent + poussière basse/stable.

### Pour une sortie / prise de profit
- **Typiquement favorable 01h-05h UTC** (pic de nuit). Vendre/encaisser près de 0.110-0.112.
- Le trailing/stop de Hulk gère le reste — RED est un bon candidat à **scaling out**
  (dégager une partie au pic, garder le reste).

### Comparaison QAIT (pour ne pas mélanger)
| | QAIT (Sealcoin) | RED (RedStone) |
|---|---|---|
| Creux intraday | 10h-13h UTC | **15h-16h UTC** |
| Pic intraday | fin de nuit | **01h-05h UTC** |
| Statut | delist MEXC, plancher | **en portefeuille, gérée** |

---

## ⚠️ Risques & limites honnêtes
1. **3 jours de données = validation précoce** : le pattern intraday est net, mais on ne l'a
   pas encore vu sur un mois complet. À reconfirmer chaque semaine (comme on l'a fait pour
   les autres — "ce qui est valable un temps peut ne plus l'être").
2. **Volatilité par rafales** : dd15 à 22% veut dire que Hulk DOIT garder ses stops
   accessibles — RED peut casser un plancher d'un coup.
3. **Market cap 44,9 M$** = petite cap : liquidité modérée (mur 45 K$), pas de grosse bouée
   de sauvetage institutionnelle.
4. **Fichier source** : `hulk-mexc/runs/croisement_contexte.jsonl` (2238 points RED,
   27/08 23:46Z → 30/08 13:48Z). Aucune donnée inventée, tout est mesuré chez nous.

---

## 📋 Prochaine étape recommandée
- Laisser tourner RED en seed et vérifier la semaine prochaine que le cycle **creux 15-16h →
  pic 01-05h** se reproduit (2-3 jours de plus suffisent).
- Si confirmé : **ajouter la fenêtre 15-16h UTC comme "zone d'entrée favorable"** dans le
  scoring/accumulation de la paire (set-up personnalisé), au même titre que le set-up
  jour/nuit d'EDEL.
- Eventuellement croiser avec un deep-dive **secteur oracles** (que disent RedStone vs
  Chainlink/Pyth sur nos perspectives géostratégiques) — mais c'est secondaire pour le set-up
  de court terme.