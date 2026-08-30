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

## 🏦 DEEPDIVE PROJET (30/08 — 3 rounds famille + vérification 2 sources)

- **CHIP = token de gouvernance de USD.AI** (Permian Labs, fondé 2021, David Choi/Conor Moore/Ivan Sergeev) : prêt permissionless financé par les GPU, $38M levés (Framework, DCG, Dragonfly, Nasdaq, Delphi, Yzi).
- **🔥 CATALYSEUR MAJEUR 28/08 (2 jours) : Bullish fournit $100M de facilité stablecoin** pour les prêts GPU de USD.AI (après $4M de Bullish Capital en 09/2025) — 8+ sources (PRNewswire, CoinDesk, Cointelegraph, The Defiant, Yahoo).
- Prêts actifs > $100M · $1.2Md facilités approuvées dont $500M QumulusAI · ICO CoinList 0.03$ · 10Md supply · 80% bloqué jusqu'à avril 2027.
- **Famille 3 rounds : NON unanime (2-3.5/10)** mais leur raison « inexistence » est une hallucination (biais inverse, pas de données fraîches) — la vérification 2 sources CORRIGE : projet réel + validation institutionnelle Bullish.
- **Risques réels** : overhang 80% (cliff 04/2027) · GPU price decline (surcapacité H100/B200) comprime les marges emprunteurs.
- **Décision** : position 20$ GARDÉE, CHIP = candidat gros potentiel n°1 (thèse « l'arbre qui cache la forêt » renforcée), pas de portage long aveugle, on trade le comportement (profil INVERSE, LEADER stab 3, dé-corrélé).
- Synthèse : `SYNTHESE_FAMILLE_DEEPDIVE_CHIP_3ROUNDS_20260830.md` + avis R1/R2/R3 dans `scripts/CONSULTATION_FAMILLE_DEEPDIVE_CHIPUSDT_ROUNDS_20260830/`.

---

## ⏱️ ÉTAT ACTUEL
- **CHIPUSDT est suivie en observation** (doctrine : tous les actifs sous observation).
- Rien n'est câblé de neuf dans Hulk : ce set-up est la **cible d'observation**, à valider
  sur les prochains jours de mesure (jour 1 → jour 2 → ... différence ou pas ?).
- Fiche à réviser avec l'évolution des données (jamais statique).

## Archives
- Profil : `hulk-mexc/runs/profils_actifs/PROFIL_CHIPUSDT.md`
- Suivi : `hulk-mexc/runs/SUIVI_SETUP_CHIPUSDT.jsonl` + `.md`
