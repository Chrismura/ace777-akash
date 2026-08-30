# 🎯 FICHE SET-UP INDIVIDUEL — MNSRYUSDT (Mansory) — 30/08/2026

> **Système unique, set-up propre à CET actif** (doctrine : même système, pas même set-up).
> Profil automatique : `hulk-mexc/runs/profils_actifs/PROFIL_MNSRYUSDT.md` (224 points).
> Suivi quotidien : `hulk-mexc/runs/SUIVI_SETUP_MNSRYUSDT.md` (mesure jour par jour, plist 16:35 locale).

---

## 📊 LE PROFIL (mesuré, 27-30/08)

| Élément | Valeur | Lecture |
|---|---|---|
| **Range total** | 1.22% | Amplitude sur la fenêtre |
| **Creux intraday** | **9h UTC** | Fenêtre d'entrée : **8h / 9h / 10h** |
| **Pic intraday** | **14h UTC** | Fenêtre de sortie : **13h / 14h / 15h** |
| **Pattern jour/nuit** | distribué | Pattern faible (0.0%) — cycle horaire peu marqué, prudent |
| **Volatilité (dd15 moy)** | 2.07% | MODÉRÉ — dd15 moyen 2% |
| **Mur bid max** | 0$ (spoof 0%) | Mur = INFO, spoof = TENSION |
| **Poussière moyenne** | 6.0% | Déclencheur entrée : < 15% |
| **Corrélation BTC** | 0.87 | fortement corrélé BTC (+0.87) → suit le marché |
| **Signal divergence** | neutre (stab 0) | Référence panier |

---

## 🎯 LE SET-UP INDIVIDUEL (adapté à ce comportement — à faire évoluer)

### Entrée (tout doit être vrai)
1. **Fenêtre** : uniquement **8h / 9h / 10h UTC** (le creux de CET actif).
2. **Déclencheur** : poussière < 15% + mur testé qui tient.
3. **NON — actif de marché (filtre macro >1.5% BTC/ETH indispensable)** — fortement corrélé BTC (+0.87) → suit le marché.
4. Garde-fou volume 15min < 3× moyenne 24h · FPOB ratio bid/ask ±2% > 1.2.
5. **Exécution** : 3 tranches (−1/−2/−3%) · stop dynamique 1,5× range 15min.

### Sortie
- Scaling out vers la fenêtre de pic **13h / 14h / 15h UTC**, reste derrière le trailing Hulk.

### Invalidation / risques
- **MODÉRÉ — dd15 moyen 2%**.
- Arrêter si frais réels + slippage > 1% (marge trop fine).
- Signal divergence : neutre (stab 0) — à surveiller (instable sur small caps).

---

## ⏱️ ÉTAT ACTUEL
- **MNSRYUSDT est suivie en observation** (doctrine : tous les actifs sous observation).
- Rien n'est câblé de neuf dans Hulk : ce set-up est la **cible d'observation**, à valider
  sur les prochains jours de mesure (jour 1 → jour 2 → ... différence ou pas ?).
- Fiche à réviser avec l'évolution des données (jamais statique).

## Archives
- Profil : `hulk-mexc/runs/profils_actifs/PROFIL_MNSRYUSDT.md`
- Suivi : `hulk-mexc/runs/SUIVI_SETUP_MNSRYUSDT.jsonl` + `.md`
