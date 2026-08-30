# 🎯 FICHE SET-UP INDIVIDUEL — PYTHUSDT (Pyth (oracle)) — 30/08/2026

> **Système unique, set-up propre à CET actif** (doctrine : même système, pas même set-up).
> Profil automatique : `hulk-mexc/runs/profils_actifs/PROFIL_PYTHUSDT.md` (2288 points).
> Suivi quotidien : `hulk-mexc/runs/SUIVI_SETUP_PYTHUSDT.md` (mesure jour par jour, plist 16:35 locale).

---

## 📊 LE PROFIL (mesuré, 27-30/08)

| Élément | Valeur | Lecture |
|---|---|---|
| **Range total** | 8.58% | Amplitude sur la fenêtre |
| **Creux intraday** | **10h UTC** | Fenêtre d'entrée : **9h / 10h / 11h** |
| **Pic intraday** | **0h UTC** | Fenêtre de sortie : **23h / 0h / 1h** |
| **Pattern jour/nuit** | distribué | Pattern faible (0.7%) — cycle horaire peu marqué, prudent |
| **Volatilité (dd15 moy)** | 17.04% | ÉLEVÉ — dd15 moyen 17% (volatile, stops à respecter) |
| **Mur bid max** | 31476.0$ (spoof 5.73%) | Mur = INFO, spoof = TENSION |
| **Poussière moyenne** | 14.6% | Déclencheur entrée : < 15% |
| **Corrélation BTC** | 0.82 | fortement corrélé BTC (+0.82) → suit le marché |
| **Signal divergence** | neutre (stab 0) | Référence panier |

---

## 🎯 LE SET-UP INDIVIDUEL (adapté à ce comportement — à faire évoluer)

### Entrée (tout doit être vrai)
1. **Fenêtre** : uniquement **9h / 10h / 11h UTC** (le creux de CET actif).
2. **Déclencheur** : poussière < 15% + mur testé qui tient.
3. **NON — actif de marché (filtre macro >1.5% BTC/ETH indispensable)** — fortement corrélé BTC (+0.82) → suit le marché.
4. Garde-fou volume 15min < 3× moyenne 24h · FPOB ratio bid/ask ±2% > 1.2.
5. **Exécution** : 50% au contact / 50% si poussière <10% · stop dynamique 1,5× range 15min.

### Sortie
- Scaling out vers la fenêtre de pic **23h / 0h / 1h UTC**, reste derrière le trailing Hulk.

### Invalidation / risques
- **ÉLEVÉ — dd15 moyen 17% (volatile, stops à respecter)**.
- Arrêter si frais réels + slippage > 1% (marge trop fine).
- Signal divergence : neutre (stab 0) — à surveiller (instable sur small caps).

---

## ⏱️ ÉTAT ACTUEL
- **PYTHUSDT est suivie en observation** (doctrine : tous les actifs sous observation).
- Rien n'est câblé de neuf dans Hulk : ce set-up est la **cible d'observation**, à valider
  sur les prochains jours de mesure (jour 1 → jour 2 → ... différence ou pas ?).
- Fiche à réviser avec l'évolution des données (jamais statique).

## Archives
- Profil : `hulk-mexc/runs/profils_actifs/PROFIL_PYTHUSDT.md`
- Suivi : `hulk-mexc/runs/SUIVI_SETUP_PYTHUSDT.jsonl` + `.md`
