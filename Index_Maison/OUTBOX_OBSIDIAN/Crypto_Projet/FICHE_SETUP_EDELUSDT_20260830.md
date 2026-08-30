# 🎯 FICHE SET-UP INDIVIDUEL — EDELUSDT (EDEL) — 30/08/2026

> **Système unique, set-up propre à CET actif** (doctrine : même système, pas même set-up).
> Profil automatique : `hulk-mexc/runs/profils_actifs/PROFIL_EDELUSDT.md` (2288 points).
> Suivi quotidien : `hulk-mexc/runs/SUIVI_SETUP_EDELUSDT.md` (mesure jour par jour, plist 16:35 locale).

---

## 📊 LE PROFIL (mesuré, 27-30/08)

| Élément | Valeur | Lecture |
|---|---|---|
| **Range total** | 22.57% | Amplitude sur la fenêtre |
| **Creux intraday** | **21h UTC** | Fenêtre d'entrée : **20h / 21h / 22h** |
| **Pic intraday** | **14h UTC** | Fenêtre de sortie : **13h / 14h / 15h** |
| **Pattern jour/nuit** | distribué | Pattern faible (-1.4%) — cycle horaire peu marqué, prudent |
| **Volatilité (dd15 moy)** | 35.08% | TRÈS ÉLEVÉ — dd15 moyen 35% (rafales brutales, stops serrés obligatoires) |
| **Mur bid max** | 2263.0$ (spoof 1.66%) | Mur = INFO, spoof = TENSION |
| **Poussière moyenne** | 14.6% | Déclencheur entrée : < 15% |
| **Corrélation BTC** | 0.68 | moyennement corrélé BTC (+0.68) |
| **Signal divergence** | POMPE_PIEGE (stab 9) | Référence panier |

---

## 🎯 LE SET-UP INDIVIDUEL (adapté à ce comportement — à faire évoluer)

### Entrée (tout doit être vrai)
1. **Fenêtre** : uniquement **20h / 21h / 22h UTC** (le creux de CET actif).
2. **Déclencheur** : poussière < 15% + mur testé qui tient.
3. **PARTIEL — attention aux secousses macro** — moyennement corrélé BTC (+0.68).
4. Garde-fou volume 15min < 3× moyenne 24h · FPOB ratio bid/ask ±2% > 1.2.
5. **Exécution** : 50% au contact / 50% si poussière <10% · stop dynamique 1,5× range 15min.

### Sortie
- Scaling out vers la fenêtre de pic **13h / 14h / 15h UTC**, reste derrière le trailing Hulk.

### Invalidation / risques
- **TRÈS ÉLEVÉ — dd15 moyen 35% (rafales brutales, stops serrés obligatoires)**.
- Arrêter si frais réels + slippage > 1% (marge trop fine).
- Signal divergence : POMPE_PIEGE (stab 9) — à surveiller (instable sur small caps).

---

## ⏱️ ÉTAT ACTUEL
- **EDELUSDT est suivie en observation** (doctrine : tous les actifs sous observation).
- Rien n'est câblé de neuf dans Hulk : ce set-up est la **cible d'observation**, à valider
  sur les prochains jours de mesure (jour 1 → jour 2 → ... différence ou pas ?).
- Fiche à réviser avec l'évolution des données (jamais statique).

## Archives
- Profil : `hulk-mexc/runs/profils_actifs/PROFIL_EDELUSDT.md`
- Suivi : `hulk-mexc/runs/SUIVI_SETUP_EDELUSDT.jsonl` + `.md`
