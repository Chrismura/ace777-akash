# 🎯 FICHE SET-UP INDIVIDUEL — CHIPUSDT (CHIP (USD.AI, compute)) — 30/08/2026

> **Système unique, set-up propre à CET actif** (doctrine : même système, pas même set-up).
> Profil automatique : `hulk-mexc/runs/profils_actifs/PROFIL_CHIPUSDT.md` (2288 points).
> Suivi quotidien : `hulk-mexc/runs/SUIVI_SETUP_CHIPUSDT.md` (mesure jour par jour, plist 16:35 locale).

---

## 📊 LE PROFIL (mesuré, 27-30/08)

| Élément | Valeur | Lecture |
|---|---|---|
| **Range total** | 25.88% | Amplitude sur la fenêtre |
| **Creux intraday** | **3h UTC** | Fenêtre d'entrée : **2h / 3h / 4h** |
| **Pic intraday** | **14h UTC** | Fenêtre de sortie : **13h / 14h / 15h** |
| **Pattern jour/nuit** | jour > nuit | Pattern INVERSE (nuit < creux de 4.7%) — l'actif vit le JOUR, pas la nuit |
| **Volatilité (dd15 moy)** | 11.63% | MODÉRÉ — dd15 moyen 12% |
| **Mur bid max** | 61779.0$ (spoof 3.86%) | Mur = INFO, spoof = TENSION |
| **Poussière moyenne** | 14.6% | Déclencheur entrée : < 15% |
| **Corrélation BTC** | -0.2 | faiblement corrélé BTC (-0.20) → plutôt endogène |
| **Signal divergence** | LEADER (stab 3) | Référence panier |

---

## 🎯 LE SET-UP INDIVIDUEL (adapté à ce comportement — à faire évoluer)

### Entrée (tout doit être vrai)
1. **Fenêtre** : uniquement **2h / 3h / 4h UTC** (le creux de CET actif).
2. **Déclencheur** : poussière < 15% + mur testé qui tient.
3. **OUI (dé-corrélé) — mais vérifier si c'est de la liquidité fine** — faiblement corrélé BTC (-0.20) → plutôt endogène.
4. Garde-fou volume 15min < 3× moyenne 24h · FPOB ratio bid/ask ±2% > 1.2.
5. **Exécution** : 3 tranches (−1/−2/−3%) · stop dynamique 1,5× range 15min.

### Sortie
- Scaling out vers la fenêtre de pic **13h / 14h / 15h UTC**, reste derrière le trailing Hulk.

### Invalidation / risques
- **MODÉRÉ — dd15 moyen 12%**.
- Arrêter si frais réels + slippage > 1% (marge trop fine).
- Signal divergence : LEADER (stab 3) — à surveiller (instable sur small caps).

---

## 🏦 DEEPDIVE PROJET — ⚠️ DÉJÀ FAIT HIER (DEEPDIVE_GLOBAL_20260829.md)

> **Le deepdive CHIP complet existe depuis le 29/08** : société (Permian Labs, Choi/Moore),
> financement ($38M : Framework, DCG, Dragonfly, Nascent, Delphi, Yzi), lancement 21/04/2026,
> listings 7 exchanges, thèse USD.AI, tokenomics (10Md, 80% bloqué, cliff avril 2027),
> décision validée (deepdive_validees). **Ne pas refaire — aller voir le DEEPDIVE_GLOBAL.**

### 🔥 SEUL COMPLÉMENT 30/08 : catalyseur Bullish $100M (28/08)
- **Bullish fournit $100M de facilité stablecoin** pour les prêts GPU de USD.AI (28/08/2026),
  après $4M de Bullish Capital (09/2025). 8+ sources : PRNewswire, CoinDesk, Cointelegraph,
  The Defiant, Yahoo, news.bitcoin.com. → valide la thèse « connections avec les gros de
  la finance » (écosystème Peter Thiel). À ajouter au DEEPDIVE_GLOBAL.

---

## ⏱️ ÉTAT ACTUEL
- **CHIPUSDT est suivie en observation** (doctrine : tous les actifs sous observation).
- Rien n'est câblé de neuf dans Hulk : ce set-up est la **cible d'observation**, à valider
  sur les prochains jours de mesure (jour 1 → jour 2 → ... différence ou pas ?).
- Fiche à réviser avec l'évolution des données (jamais statique).

## Archives
- Profil : `hulk-mexc/runs/profils_actifs/PROFIL_CHIPUSDT.md`
- Suivi : `hulk-mexc/runs/SUIVI_SETUP_CHIPUSDT.jsonl` + `.md`
