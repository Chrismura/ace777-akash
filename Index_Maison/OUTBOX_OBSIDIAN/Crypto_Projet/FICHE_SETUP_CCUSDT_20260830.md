# 🎯 FICHE SET-UP INDIVIDUEL — CCUSDT (CC (Canton Network)) — 30/08/2026

> **Système unique, set-up propre à CET actif** (doctrine : même système, pas même set-up).
> Profil automatique : `hulk-mexc/runs/profils_actifs/PROFIL_CCUSDT.md` (2288 points).
> Suivi quotidien : `hulk-mexc/runs/SUIVI_SETUP_CCUSDT.md` (mesure jour par jour, plist 16:35 locale).

---

## 📊 LE PROFIL (mesuré, 27-30/08)

| Élément | Valeur | Lecture |
|---|---|---|
| **Range total** | 11.17% | Amplitude sur la fenêtre |
| **Creux intraday** | **7h UTC** | Fenêtre d'entrée : **6h / 7h / 8h** |
| **Pic intraday** | **15h UTC** | Fenêtre de sortie : **14h / 15h / 16h** |
| **Pattern jour/nuit** | distribué | Pattern faible (0.5%) — cycle horaire peu marqué, prudent |
| **Volatilité (dd15 moy)** | 13.06% | MODÉRÉ — dd15 moyen 13% |
| **Mur bid max** | 25445.0$ (spoof 1.19%) | Mur = INFO, spoof = TENSION |
| **Poussière moyenne** | 14.6% | Déclencheur entrée : < 15% |
| **Corrélation BTC** | -0.04 | faiblement corrélé BTC (-0.04) → plutôt endogène |
| **Signal divergence** | neutre (stab 0) | Référence panier |

---

## 🎯 LE SET-UP INDIVIDUEL (adapté à ce comportement — à faire évoluer)

### Entrée (tout doit être vrai)
1. **Fenêtre** : uniquement **6h / 7h / 8h UTC** (le creux de CET actif).
2. **Déclencheur** : poussière < 15% + mur testé qui tient.
3. **OUI (dé-corrélé) — mais vérifier si c'est de la liquidité fine** — faiblement corrélé BTC (-0.04) → plutôt endogène.
4. Garde-fou volume 15min < 3× moyenne 24h · FPOB ratio bid/ask ±2% > 1.2.
5. **Exécution** : 3 tranches (−1/−2/−3%) · stop dynamique 1,5× range 15min.

### Sortie
- Scaling out vers la fenêtre de pic **14h / 15h / 16h UTC**, reste derrière le trailing Hulk.

### Invalidation / risques
- **MODÉRÉ — dd15 moyen 13%**.
- Arrêter si frais réels + slippage > 1% (marge trop fine).
- Signal divergence : neutre (stab 0) — à surveiller (instable sur small caps).

---

## ⏱️ ÉTAT ACTUEL
- **CCUSDT est suivie en observation** (doctrine : tous les actifs sous observation).
- Rien n'est câblé de neuf dans Hulk : ce set-up est la **cible d'observation**, à valider
  sur les prochains jours de mesure (jour 1 → jour 2 → ... différence ou pas ?).
- Fiche à réviser avec l'évolution des données (jamais statique).

## Archives
- Profil : `hulk-mexc/runs/profils_actifs/PROFIL_CCUSDT.md`
- Suivi : `hulk-mexc/runs/SUIVI_SETUP_CCUSDT.jsonl` + `.md`
