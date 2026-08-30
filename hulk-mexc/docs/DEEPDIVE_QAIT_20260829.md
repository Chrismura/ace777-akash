# 🐋 DEEP-DIVE STRATÉGIQUE QAIT (SEALCOIN) — 29/08/2026

> Deepdive demandé par Christophe après CHIP : « QAIT c'est très particulier, fais un vrai
> deepdive stratégique pour comprendre les corrélations — projet, marché, géographie. »
> Données : 36 jours de trades Hulk + 2 jours de série horaire (croisement_contexte.jsonl,
> 1399 points QAIT) + recherche marché. Par Buffy (chef scientifique).

---

## 1. LE PROJET (recherche)

**QAIT = SEALCOIN** — un protocole **DePIN** (réseau d'infrastructure physique décentralisé) où
les **machines intelligentes se payent entre elles** (énergie, données) avec le token QAIT.
Chaque appareil a un ID numérique sécurisé et peut trader sur le réseau.

| Élément | Valeur | Lecture |
|---|---|---|
| Origine | **Suisse** (site `qait.ch`, lié à **WISeKey** — société suisse de cybersécurité cotée) | Projet "propre" réglementairement, pas un anonymat |
| Lancement | ~mai 2026 (déploiement 28/05) | 3 mois d'existence |
| Listings | **Binance Alpha, KuCoin, Gate.io, MEXC** | **Le marché le plus actif = MEXC (notre exchange !)** |
| Market cap | **2,08 M$** | Micro-cap minuscule |
| FDV (dilué) | 19,8 M$ | ×10 le market cap → grosse dilution à venir |
| Supply | 10 Md max, **5,55 Md verrouillés en wallet** (84 % pas en circulation) | **Bombe à retard** : le wallet locké est énorme |
| Volume 24h | 275 k$ global, **~70 k$ sur MEXC QAIT/USDT** | Très faible — carnet mince |
| Surge | +55 % en 24h sur campagne Binance Alpha (19/08) | Le catalyseur : campagnes de listing |

**Thèse projet** : l'« économie des machines » (machine-to-machine payments) est un narratif
porteur (IA × DePIN × IoT). WISeKey apporte une crédibilité institutionnelle. MAIS le
tokenomics est **inquiétant** : 84 % de la supply verrouillée = les premiers investisseurs
détiennent la quasi-totalité, et la dilution future est massive (FDV 19,8 M$ vs mcap 2 M$).

---

## 2. NOS DONNÉES (36 jours de trading Hulk)

| Métrique | Valeur | Lecture |
|---|---|---|
| Trades QAIT | 58 BUY · **27 SELL full −49,91 $** · 1 SELL_PARTIAL | **LA paire qui fait le plus perdre Hulk** |
| Part des pertes | **−49,91 $ sur −158 $ totaux des SELL full ≈ 1/3** | Elle explique un tiers de l'hémorragie |
| Vol_spike actuel | **13,39x** (volume 13× la médiane !) | Volatilité extrême |
| range15 | **231 %** | Mouvement 6h/15 min énorme |
| Prix (2 j) | 0,001856 → 0,002318 | Montée ~25 % sur la fenêtre |
| Position actuelle | **PAS en position** (sortie) | Hulk l'a quittée |
| Profil murs | illiquide, spread **63 bps** (σ 56 !), murs ~1 100 $ | L'INVERSE de CHIP (3,8 bps, murs 33 k$) |

---

## 3. LA GÉOGRAPHIE (la découverte)

**QAIT pompe la NUIT — c'est l'anti-CHIP.**

| Fenêtre | Pics >10 % | Fréquence |
|---|---|---|
| **Nuit (18h-7h UTC = Asie)** | **650 pics / 650 points = 100 % du temps** | **Toujours en pic la nuit !** |
| Jour (8h-17h UTC = EU/US) | 355 / 749 = 47 % | Beaucoup moins |

- **Pic massif à 7h UTC (98 pics)** = fin Asie / ouverture Europe.
- **Mini-creux à 11-12h UTC (3-5 pics)** = pleine session US... QAIT se TAIT quand les
  marchés occidentaux sont le plus actifs.
- C'est **exactement le gating temporel inversé** de Cortana : pour QAIT, le signal nocturne
  EST le signal (contrairement à CHIP où c'est du bruit).

**Interprétation géographique** : le trading de QAIT est **piloté par la session asiatique**.
Les pics nocturnes = des acteurs Asie (probablement liés au projet, aux mineurs/promoteurs
du réseau DePIN) qui animent le carnet la nuit quand il n'y a pas de contrepartie occidentale.
→ **Marché "vide" manipulable la nuit** : peu de volume, gros mouvements.

---

## 4. LES CORRÉLATIONS (le cœur de ta demande)

| Corrélation | Valeur | Lecture |
|---|---|---|
| **QAIT vs BTC** | **−0,21** | **ANTI-marché** : quand BTC monte, QAIT baisse (et vice-versa) |
| QAIT vs ETH | −0,21 | Idem — anti-ETH aussi |
| QAIT vs XRP | −0,22 | Idem — anti-crypto majeures |
| **QAIT vs panier** | **+0,29** | Suit le panier small-caps en moyenne |
| QAIT vs CHIP | (n/d, données disjointes) | Les deux extrêmes opposés du spectre |

**Le paradoxe QAIT** :
- Elle est **anti-corrélée au marché majeur** (BTC/ETH/XRP) → quand le marché global
  corrige, elle a tendance à monter (fuite vers les micro-caps ? ou manipulation inverse ?)
- Mais **corrélée au panier small-caps** → elle suit le mouvement des petites caps
- Et son signal de divergence (angle 3 du protocole) : **−0,45 = POMPE-PIÈGE n°1** du
  portefeuille — ses pics PRÉCÈDENT les baisses du panier (les 32 pics → panier en baisse
  +2h à 34 % seulement de hausse, 25 % à +4h)

**En clair** : QAIT est un **couteau à double tranchant décorrélé** :
1. Elle apporte de la **diversification** (anti-BTC = couverture naturelle)
2. Mais sa manipulation nocturne + sa dilution massive en font **la pire paire de trading**
   de Hulk (−49,91 $, 27 coupes, spread 63 bps qui mange les allers-retours)

---

## 5. MON VERDICT (Buffy)

**QAIT est LE cas d'école des limites de notre portefeuille** :

1. **Projet : prometteur mais tokenomics toxique.** L'économie des machines (DePIN × IA)
   est un vrai narratif, WISeKey donne une assise crédible. MAIS : 84 % de la supply
   verrouillée = les initiés tiennent le marché, et la dilution (FDV ×10) pèsera sur le
   prix à chaque unlock. C'est le profil « distribution de tokens par un seul acteur »
   que Cortana a pointé comme risque pour CHIP — **appliqué à QAIT c'est plus évident
   encore** : murs de 1 100 $, pas de profondeur réelle.

2. **Géographie : le signal est ASIATIQUE et NOCTURNE.** Les pics 100 % la nuit = le carnet
   est animé par une seule population d'acteurs quand l'Occident dort. Ce n'est pas du
   « leadership » (CHIP) — c'est un **marché piloté**, où un acteur peut pousser le prix
   sans contrepartie. Le gating temporel de Cortana s'applique à l'envers ici : **on ne
   trade QAIT QUE si on comprend la nuit asiatique**, et surtout **jamais avec un stop
   serré** (spread 63 bps le rend impossible).

3. **Trading : la pire paire de Hulk, et c'est mécanique.** 27 coupes à −49,91 $, c'est la
   preuve chiffrée que QAIT **ne se trade pas comme une petite cap normale** : l'amplitude
   (vol_spike 13x, range 231 %) déclenche les stops à 100 % à chaque secousse, et le spread
   de 63 bps mange le peu qui reste. Le fix SELL full va aider (cascade au lieu de coupe),
   mais la racine est plus profonde : **QAIT ne devrait pas être une position de trading —
   c'est une position de POKER long terme sur la thèse DePIN, ou rien.**

4. **Le paradoxe utile** : son anti-corrélation au marché (−0,21 vs BTC) en fait un
   **candidat couverture** : quand le marché global chute, QAIT a statistiquement tendance
   à monter. Si on garde QAIT, c'est pour CETTE raison — pas pour le scalper.

**Recommandation opérationnelle** :
- **Trading** : exclure QAIT du scalping dip/rip (les 27 coupes le prouvent) — ou la
  confiner à une taille microscopique + stop très large (le stop_pct à 10 % est déjà
  ajusté, mais le spread 63 bps tue le reste).
- **Bag** : si on croit à la thèse DePIN Suisse, la garder en **position d'attente** (pas
  de stop technique, pas de DCA agressif) — comme un pari long terme, pas un trade.
- **Protocole divergence** : son signal POMPE-PIÈGE (−0,45) + sa géographie nocturne sont
  **deux avertissements croisés** → confirmer sur les 14 jours avant toute ré-intégration.

**En une phrase** : QAIT est un **projet sérieux sur un marché non sérieux** — le narratif
(économie des machines, WISeKey) est le meilleur du portefeuille, mais le carnet (1 100 $ de
murs), la géographie (100 % nocturne asiatique) et le tokenomics (84 % locké) en font la
**pire paire à trader** — elle nous a coûté −49,91 $ précisément parce qu'on la trade comme
une petite cap normale alors qu'elle est un micro-cap piloté.

---

## 6. À CONFRONTER (prochaines étapes)

- Soumettre ce deepdive à **Cortana** (même boucle "trouve", contexte complet) pour son
  avis indépendant sur le paradoxe « anti-BTC mais POMPE-PIÈGE du panier ».
- Croiser avec la **famille** (le juge) pour décider : exclure du scalping / garder en
  bag / sortir. Aucune décision avant leur avis + 14 jours de protocole divergence.
