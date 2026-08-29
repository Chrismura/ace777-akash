# 🔬 DEEPDIVE RIZE (RIZE) — 29/08/2026

> Christophe, 29/08 : « deepdive RIZE, de même que [CHIP/QAIT] — va et trouve les
> sources. Prudence : RIZE comme beaucoup n'a pas été approfondi en deepdive. »
> Par Buffy (chef scientifique) — données maison + sources web (CMC AI,
> CoinGecko, Coinbase, Kraken, MEXC).

---

## 1. CE QUE C'EST (le projet)

**RIZE = T-RIZE** — plateforme institutionnelle de **tokenisation d'actifs réels
(RWA)**, transformant des actifs du monde réel en investissements numériques
négociables. Même secteur que QAIT (RWA), mais positionnement différent :
- **Infrastructure de tokenisation institutionnelle** (pas un actif tokenisé unique)
- **Listing Revolut** (12/08/2025) : accès à 60M+ d'utilisateurs
- **Intégration Canton Network** (réseau privé institutionnel $4T, validateur + builder)
- **Pipeline $10B d'actifs réels** à onboarder (2026)
- **Treasury communautaire** : 30 % du supply (1,5 Md tokens) en lock 12 mois puis
  release linéaire 36 mois
- Connexions citées par la communauté : **Chainlink ($LINK)** et **Canton ($CC)**

## 2. LES DONNÉES DU MARCHÉ (web, 29/08/2026)

| Métrique | Valeur | Lecture |
|---|---|---|
| Prix | **0,0046 $** (CoinGecko) | prix du portefeuille : 0,005626 $ (notre snapshot) |
| Rang | **#1215** | micro-cap profonde |
| Market cap | **9,6 M$** | micro-cap |
| FDV | 23,2 M$ (ratio MC/FDV = 0,41) | **41 % du supply en circulation, 59 % à venir** |
| Volume 24h | **112 k$** | très faible — liquidité squelettique |
| Échanges | 4 exchanges, 5 marchés | MEXC présent (c'est là qu'on l'observe) |
| Mouvement notable | **+89,2 % le 24/06/2026** (à 0,01516 $) contre-tendance | forte spéculation, label « volatility bomb » |
| Insight CoinGecko (30j) | « Transparency Report, price dips amidst **no value accrual mechanisms** » | ⚠️ pas de mécanisme d'accrétion de valeur |

## 3. NOS DONNÉES MAISON (le comportement sur MEXC)

```
Archetype : "manipulée_fragile" (le pire profil de notre catalogue)
n_mesures : 4 570 (portefeuille) / 5 332 (murs)
Prix          : 0,005626 $
Mur BID médian : 243 $  (minuscule)
Mur ASK médian : 508 $
Stabilité mur σ : 1.151  (ÉLEVÉ — murs très instables, volatils)
Spread médian  : 46,99 bps (σ 79,94 — très variable)
Spoof %        : 3,36 % (179 spoofs) — au-dessus de la moyenne saine
Drop ≥15%/s    : 216 (4,05 %) — effondrements de carnet fréquents
Fenêtres fortes : UTC 16-23 (soirée US) — fenêtres faibles : AUCUNE
Calib : spoof_alerte 5,82 % · drop_alerte 10 % · spread_cout 94 bps ·
        mise_max_mur 2 % · dip 4,2 % · rip 4,0 % · stop 8 %
```

**Lecture** : profil **manipulée_fragile** confirmé — murs minuscules (243 $),
stabilité σ 1.151 (élevée), spoof 3,36 % (haut), drop 216 (haut). C'est le profil
de micro-cap la plus vulnérable du catalogue : un vacuuming (Signal 3) y serait
dévastateur (trou d'air instantané sur 243 $ de liquidité).

## 4. VERDICT — POUR L'INCLUSION AU CROISEMENT

| Critère | Verdict |
|---|---|
| **Données deepdive** | ⚠️ Nouvelles sources web trouvées (CMC AI, CoinGecko, Coinbase, Kraken) |
| **Profil comportemental** | 🔴 manipulee_fragile — le PLUS fragile du catalogue |
| **Risque de fausse alerte** | 🟡 élevé (spoof 3,4 % + drop 216 + σ 1.151 → risque de faux signal 3) |
| **Valeur fondamentale** | 🟡 T-RIZE a un vrai projet (RWA institutionnel, Revolut, Canton, $10B) MAIS pas de mécanisme d'accrétion de valeur + 59 % du supply à libérer |

**DÉCISION (proposée à Christophe)** : RIZE reste **EXCLUE du croisement**
(prudence maintenue) mais on a maintenant le deepdive de référence :
- Le profil `manipulee_fragile` justifie une **prudence maximale** si elle entre
  un jour au portefeuille (spread_cout 94 bps, murs 243 $, mise_max 2 %).
- Le deepdive a trouvé les sources → **le blocage « pas de deepdive » est levé**
  au sens documentation, mais le profil lui-même recommande la prudence.
- Surveiller : si le prix remonte avec volume (comme le +89 % du 24/06), le
  Signal 3 sur RIZE serait un excellent détecteur de fin de pump (trou d'air).

**Recommandation** : garder RIZE en `exclues_prudence` pour le CROISEMENT de prix
(son prix est volatil et peu fiable), mais on peut envisager de la passer en
`observation_setup` (prix seul) si Christophe veut capturer son comportement
comme SOL — c'est le même mécanisme « set up personnalisé avant entrée ».

## 5. Fichiers liés
- Profil : `hulk-mexc/strategie/universe_profils.json` (RIZEUSDT)
- Murs : `hulk-mexc/runs/murs_observations.json` (RIZEUSDT)
- Statut croisement : `hulk-mexc/strategie/paires_croisement.json` (exclues_prudence)
- Sources web : CMC AI (89 % 24/06, Canton, Revolut, treasury) · CoinGecko
  (MC 9,6M, FDV 23,2M, volume 112k) · Coinbase (T-RIZE RWA) · Kraken (prévisions)
