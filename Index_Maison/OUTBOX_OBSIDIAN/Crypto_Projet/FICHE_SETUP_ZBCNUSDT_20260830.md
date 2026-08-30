# 🎯 FICHE SET-UP INDIVIDUEL — ZBCNUSDT (Zebec) — 30/08/2026

> **Système unique, set-up propre à CET actif** (doctrine : même système, pas même set-up).
> Profil automatique : `hulk-mexc/runs/profils_actifs/PROFIL_ZBCNUSDT.md` (2288 points).
> Suivi quotidien : `hulk-mexc/runs/SUIVI_SETUP_ZBCNUSDT.md` (mesure jour par jour, plist 16:35 locale).

---

## 📊 LE PROFIL (mesuré, 27-30/08)

| Élément | Valeur | Lecture |
|---|---|---|
| **Range total** | 14.84% | Amplitude sur la fenêtre |
| **Creux intraday** | **22h UTC** | Fenêtre d'entrée : **21h / 22h / 23h** |
| **Pic intraday** | **1h UTC** | Fenêtre de sortie : **0h / 1h / 2h** |
| **Pattern jour/nuit** | jour > nuit | Pattern INVERSE (nuit < creux de 1.7%) — l'actif vit le JOUR, pas la nuit |
| **Volatilité (dd15 moy)** | 11.51% | MODÉRÉ — dd15 moyen 12% |
| **Mur bid max** | 6505.0$ (spoof 4.78%) | Mur = INFO, spoof = TENSION |
| **Poussière moyenne** | 14.6% | Déclencheur entrée : < 15% |
| **Corrélation BTC** | 0.77 | moyennement corrélé BTC (+0.77) |
| **Signal divergence** | POMPE_PIEGE (stab 4) | Référence panier |

---

## 🎯 LE SET-UP INDIVIDUEL (adapté à ce comportement — à faire évoluer)

### Entrée (tout doit être vrai)
1. **Fenêtre** : uniquement **21h / 22h / 23h UTC** (le creux de CET actif).
2. **Déclencheur** : poussière < 15% + mur testé qui tient.
3. **PARTIEL — attention aux secousses macro** — moyennement corrélé BTC (+0.77).
4. Garde-fou volume 15min < 3× moyenne 24h · FPOB ratio bid/ask ±2% > 1.2.
5. **Exécution** : 3 tranches (−1/−2/−3%) · stop dynamique 1,5× range 15min.

### Sortie
- Scaling out vers la fenêtre de pic **0h / 1h / 2h UTC**, reste derrière le trailing Hulk.

### Invalidation / risques
- **MODÉRÉ — dd15 moyen 12%**.
- Arrêter si frais réels + slippage > 1% (marge trop fine).
- Signal divergence : POMPE_PIEGE (stab 4) — à surveiller (instable sur small caps).

---

## ⏱️ ÉTAT ACTUEL
- **ZBCNUSDT est suivie en observation** (doctrine : tous les actifs sous observation).
- Rien n'est câblé de neuf dans Hulk : ce set-up est la **cible d'observation**, à valider
  sur les prochains jours de mesure (jour 1 → jour 2 → ... différence ou pas ?).
- Fiche à réviser avec l'évolution des données (jamais statique).

## Archives
- Profil : `hulk-mexc/runs/profils_actifs/PROFIL_ZBCNUSDT.md`
- Suivi : `hulk-mexc/runs/SUIVI_SETUP_ZBCNUSDT.jsonl` + `.md`
