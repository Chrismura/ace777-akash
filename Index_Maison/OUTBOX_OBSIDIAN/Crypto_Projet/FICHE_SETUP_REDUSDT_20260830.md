# 🎯 FICHE SET-UP INDIVIDUEL — REDUSDT (RedStone (oracle)) — 30/08/2026

> **Système unique, set-up propre à CET actif** (doctrine : même système, pas même set-up).
> Profil automatique : `hulk-mexc/runs/profils_actifs/PROFIL_REDUSDT.md` (2288 points).
> Suivi quotidien : `hulk-mexc/runs/SUIVI_SETUP_REDUSDT.md` (mesure jour par jour, plist 16:35 locale).

---

## 📊 LE PROFIL (mesuré, 27-30/08)

| Élément | Valeur | Lecture |
|---|---|---|
| **Range total** | 12.1% | Amplitude sur la fenêtre |
| **Creux intraday** | **16h UTC** | Fenêtre d'entrée : **15h / 16h / 17h** |
| **Pic intraday** | **4h UTC** | Fenêtre de sortie : **3h / 4h / 5h** |
| **Pattern jour/nuit** | nuit > jour | Pattern nuit > creux (2.1%) — cycle de nuit (type QAIT/EDEL) |
| **Volatilité (dd15 moy)** | 22.83% | ÉLEVÉ — dd15 moyen 23% (volatile, stops à respecter) |
| **Mur bid max** | 45240.0$ (spoof 1.67%) | Mur = INFO, spoof = TENSION |
| **Poussière moyenne** | 14.6% | Déclencheur entrée : < 15% |
| **Corrélation BTC** | 0.08 | faiblement corrélé BTC (+0.08) → plutôt endogène |
| **Signal divergence** | neutre (stab 0) | Référence panier |

---

## 🎯 LE SET-UP INDIVIDUEL (adapté à ce comportement — à faire évoluer)

### Entrée (tout doit être vrai)
1. **Fenêtre** : uniquement **15h / 16h / 17h UTC** (le creux de CET actif).
2. **Déclencheur** : poussière < 15% + mur testé qui tient.
3. **OUI (dé-corrélé) — mais vérifier si c'est de la liquidité fine** — faiblement corrélé BTC (+0.08) → plutôt endogène.
4. Garde-fou volume 15min < 3× moyenne 24h · FPOB ratio bid/ask ±2% > 1.2.
5. **Exécution** : 50% au contact / 50% si poussière <10% · stop dynamique 1,5× range 15min.

### Sortie
- Scaling out vers la fenêtre de pic **3h / 4h / 5h UTC**, reste derrière le trailing Hulk.

### Invalidation / risques
- **ÉLEVÉ — dd15 moyen 23% (volatile, stops à respecter)**.
- Arrêter si frais réels + slippage > 1% (marge trop fine).
- Signal divergence : neutre (stab 0) — à surveiller (instable sur small caps).

---

## 🏦 DEEPDIVE PROJET (30/08 — 3 rounds famille + vérification 2 sources)

- **RED = RedStone** : oracle modulaire « data layer for onchain finance », architecture Pull (gas réduit sur L2), 110+ chaînes. Sources : redstone.finance, blog.redstone.finance.
- **Backing** : $15M Series A (Arrington Capital) + $22M+ total (Arrington, Lemniscap, Delphi). Source : theblock.co.
- **Famille 3 rounds : GO AVEC RÉSERVES 6.5-6.8/10 (3/3)** — 2e meilleur verdict (derrière PYTH 7.5). Le cobaye est maintenant entièrement documenté (set-up + projet).
- **Valide** : techno Pull adaptée au multi-L2 · backing institutionnel Tier-1 · adoption 110+ chaînes · **endogène (corr BTC 0.08 — rare) → set-up indépendant du marché**.
- **Réserves** : duopole Chainlink/Pyth = étau (guerre des frais) · dilution VC (Early Backers 31.7%) · FDV/supply à auditer.
- **Décision** : position GARDÉE, set-up opérationnel validé = référence, RED = MOTEUR (comme PYTH), surveillance déblocages VC + guerre des frais oracles.
- Synthèse : `SYNTHESE_FAMILLE_DEEPDIVE_RED_3ROUNDS_20260830.md` + avis R1/R2/R3 dans `scripts/CONSULTATION_FAMILLE_DEEPDIVE_REDUSDT_ROUNDS_20260830/`.

---

## ⏱️ ÉTAT ACTUEL
- **REDUSDT est suivie en observation** (doctrine : tous les actifs sous observation).
- Rien n'est câblé de neuf dans Hulk : ce set-up est la **cible d'observation**, à valider
  sur les prochains jours de mesure (jour 1 → jour 2 → ... différence ou pas ?).
- Fiche à réviser avec l'évolution des données (jamais statique).

## Archives
- Profil : `hulk-mexc/runs/profils_actifs/PROFIL_REDUSDT.md`
- Suivi : `hulk-mexc/runs/SUIVI_SETUP_REDUSDT.jsonl` + `.md`
