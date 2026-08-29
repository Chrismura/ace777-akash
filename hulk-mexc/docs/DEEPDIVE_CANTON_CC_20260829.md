# 🏦 DEEPDIVE — CANTON NETWORK (CC) — 29/08/2026

> Deepdive au standard maison (banque d'affaires) : la société réelle, la
> thèse, le brut (sources primaires), le tokenomics, le marché avec NOS
> données, le risque chiffré, la décision. Demandé par Christophe (GO) — CC
> était en `exclues_prudence`, ce deepdive décide du reclassement.

---

## 1. 🏢 LA SOCIÉTÉ RÉELLE (qui est derrière)

- **Canton Network** = la blockchain publique « privacy-enabled » construite
  pour la finance institutionnelle (tokenisation RWA, règlement, collatéral).
- Créé par **Digital Asset** — la société du **Daml smart contract language**,
  fondée par **Yuval Rooz** (CEO). 10 ans de développement avant le lancement
  permissionless.
- **Investisseurs de Digital Asset** (levée de 135 M$ en juin 2025) :
  **BNP Paribas, Circle Ventures, Citadel Securities, DTCC, Goldman Sachs**.
- **Membres / utilisateurs du réseau (le « gros monde »)** : **Visa**
  (paiements préservant la privacy, mars 2026), **HSBC** (membre premier),
  **Tradeweb** (financement du Trésor US on-chain, août 2025), **BNY**,
  **DTCC**, plus de la moitié des émissions de **digital bonds** 2024 passent
  par Canton.
- Fait notable : **Tharimmune** (biotech) a levé 540 M$ en privé pour bâtir un
  **trésor de guerre en CC** et devenir super-validateur du réseau.

> **Verdict société** : c'est un VRAI acteur institutionnel — pas un anonymat.
> Les plus gros noms de la finance mondiale (Visa, HSBC, BNY, DTCC, Goldman,
> BNP) sont dedans. C'est exactement le profil « société créée autour de la
> blockchain » que Christophe cherche.

---

## 2. 🎯 LA THÈSE

**Ce que fait le réseau** : la tokenisation des actifs réels (RWA) et le
règlement institutionnel sur une chaîne publique **avec privacy par défaut**
(partage « need-to-know », pas d'anonymat — les régulateurs peuvent tout voir
sur demande). C'est LA différence avec Zcash/Bitcoin : la privacy au service
de la conformité, pas contre elle.

**La thèse macro** : le marché RWA tokenisé dépasse **36 Md$** (fin 2025, hors
stablecoins, rapport Canton) — et l'institutionnel (banques, fonds) y va.

**Le narratif** : « Bringing Trillions Onchain » — le pont entre les
institutions et la blockchain. Le réseau parle le langage des banques
(compliance, privacy, auditabilité) que les L1 grand public ne parlent pas.

---

## 3. 🔑 LE TOKENOMICS — le point CRUCIAL (notre leçon QAIT/CHIP)

### Ce que disent les sources primaires (site officiel + interview Yuval Rooz)
- **Pas d'ICO, pas de pré-mine, pas d'allocation VC** : « Every Canton Coin is
  earned, not pre-allocated » (site officiel). Le CEO : « Nous avons refusé
  l'ICO, refusé le pré-mine. »
- **Burn-and-Mint equilibrium** : les frais d'usage sont BRÛLÉS, et de
  nouveaux CC sont MINTS selon la participation. L'offre répond à la demande.
- **Répartition des récompenses** : 35 % super-validateurs / 50 % builders
  d'apps / 15 % utilisateurs — « récompenser l'utilité réelle, pas la
  spéculation ».
- ⚠️ **MAIS la supply totale est « infinite »** (tokenomist) — c'est un modèle
  continu (mint/burn), donc **l'inflation nette dépend de l'usage** : si
  l'usage < mint, le prix se dilue.

### ⚖️ L'analyse du pont de valeur (LE test maison)
| Question (notre leçon) | Réponse pour CC |
|---|---|
| Y a-t-il un mécanisme de capture dans le code ? | ✅ **OUI — frais brûlés + mint lié à l'usage** : plus le réseau est utilisé, plus la demande de CC monte (l'inverse de QAIT où il n'y avait rien) |
| Le token est-il lié au CA des institutions ? | ✅ Indirectement — les frais d'usage du réseau (payés en CC) sont la source. C'est LE pont de valeur que QAIT n'avait pas |
| Risque de dilution ? | ⚠️ Supply « infinie » (mint continu) — mais le burn compense. À surveiller : le ratio mint/burn réel |

> **Verdict tokenomics** : c'est le meilleur design qu'on ait vu dans notre
> panier sur le pont de valeur — à l'opposé de QAIT (rien dans le code) et de
> CHIP (pas de créance). Le risque principal = le mint continu si l'usage ne
> suit pas.

---

## 4. 📊 LE MARCHÉ AVEC NOS DONNÉES (ce qu'on a capturé nous-mêmes)

Données **réelles** de nos DIGEST (observer_murs, 22/07/2026) :

| Métrique | Valeur CC (22/07) | Comparaison QAIT |
|---|---|---|
| **Prix** | 0,1223 $ | — |
| **Spread** | **4,09 bps** | QAIT : 63 bps → carnet 15× plus fin |
| **Volume 24h** | 200 905 $ (quote) | — |
| **Murs** | bid 2 462 $ / ask 5 638 $ | QAIT : ~1 100 $ → CC est plus profond |
| **Cadence** | 2,0 | — |
| **Tension** | 1,35 | — |
| **Hint** | IDLE | — |

### La géographie du prix (web croisé)
- ATH : **0,1942 $ (3 fév. 2026)** · ATL : **0,0589 $ (6 déc. 2025)**
- Cours actuel : ~0,11-0,12 $ → **-42 % sous l'ATH**, +29 % sur 7 jours
- Range : le jeton est jeune (liste depuis fin 2025), forte volatilité
  (X2 entre ATL et ATH en 2 mois)

> **Verdict marché** : carnet plus sain que QAIT (spread 4 bps vs 63), mais
> petit volume (200 k$). C'est un micro-cap institutionnel — la liquidité est
> encore faible, mais la structure de marché est bien meilleure que nos
> pires paires.

---

## 5. ⚠️ LE RISQUE (chiffré)

1. **Dilution (le risque n°1)** : supply « infinie » (mint continu) — si
   l'usage ne suit pas, dilution. **Indicateur à suivre : ratio burn/mint
   mensuel + croissance des ledger events** (3 M/jour en 2025, ×20 sur les
   transfers — à confirmer en continu).
2. **Liquidité** : 200 k$/24h sur MEXC = slippage réel ; les murs sont minces.
   Un stop serré sur CC serait risqué (comme leçon QAIT, mais en moins grave).
3. **Concentration** : Tharimmune (trésor 540 M$ en CC) + gros validateurs —
   un gros acteur qui vend = choc de prix.
4. **Réglementaire** : le modèle « privacy need-to-know » est un pari
   politique — si les régulateurs n'acceptent pas le compromis, la thèse
   s'effondre (mais Visa/HSBC dedans = plutôt bon signe).
5. **Jeunesse** : le jeton n'existe que depuis ~fin 2025. Zéro cycle
   baissier traversé.

---

## 6. 🎯 LA DÉCISION (cadre maison)

| Critère | Verdict CC |
|---|---|
| Société réelle | ✅ Digital Asset + Visa/HSBC/BNY/DTCC/Goldman/BNP |
| Pont de valeur dans le code | ✅ Frais brûlés + mint lié à l'usage (mieux que tout notre panier micro-cap) |
| Tokenomics / dilution | ⚠️ Supply infinie — à surveiller (ratio burn/mint) |
| Marché (nos données) | ✅ Spread 4 bps (sain), mais volume 200 k$ (faible) |
| Géographie trading | Volatilité jeune, -42 % sous l'ATH |
| Corrélation à la thèse de Christophe | ✅ « Société créée autour de la blockchain » + RWA + institutionnel |

### Verdict
**CC mérite de sortir de `exclues_prudence` et de passer en `observation_setup`**
(capture prix + données, PAS de décision de trading tant que la liquidité
reste faible et le token jeune). C'est le meilleur candidat « couche
blockchain institutionnelle » de notre liste — le pont de valeur dans le code
existe (contrairement à QAIT/CHIP).

**Mais rester en observation, pas en deepdive_validees (trading)** tant que :
- le volume MEXC reste < ~1 M$/jour (le slippage rendrait le trading risqué),
- le ratio burn/mint n'a pas été vérifié sur plusieurs mois.

---

## 7. 📌 SOURCES (le brut)

- Site officiel Canton : canton.network (tokenomics, FAQ, press releases)
- Interview Yuval Rooz (CEO Digital Asset) — Cointelegraph Chain Reaction,
  nov. 2025 (« We refused to do an ICO »)
- Communiqué Visa (mars 2026) — paiements privacy sur Canton
- Tradeweb / Digital Asset (août 2025) — Trésor US on-chain
- Tokenomist (supply) · CoinGecko/CoinMarketCap/Kraken (prix, ATH/ATL)
- **Nos données** : `runs/DIGEST_20260722_215007.json` (spread 4,09 bps,
  volume 200 k$, murs 2,5 k$/5,6 k$)

*Deepdive par Buffy, 29/08/2026. À mettre à jour : le ratio burn/mint dès
qu'on a des données continues.*