# 🎯 FICHE SET-UP INDIVIDUEL — QNTUSDT (Quant) — 30/08/2026

> **Système unique, set-up propre à CET actif** (doctrine : même système, pas même set-up).
> Profil automatique : `hulk-mexc/runs/profils_actifs/PROFIL_QNTUSDT.md` (224 points).
> Suivi quotidien : `hulk-mexc/runs/SUIVI_SETUP_QNTUSDT.md` (mesure jour par jour, plist 16:35 locale).

---

## 📊 LE PROFIL (mesuré, 27-30/08)

| Élément | Valeur | Lecture |
|---|---|---|
| **Range total** | 1.16% | Amplitude sur la fenêtre |
| **Creux intraday** | **9h UTC** | Fenêtre d'entrée : **8h / 9h / 10h** |
| **Pic intraday** | **14h UTC** | Fenêtre de sortie : **13h / 14h / 15h** |
| **Pattern jour/nuit** | distribué | Pattern faible (0.0%) — cycle horaire peu marqué, prudent |
| **Volatilité (dd15 moy)** | 12.89% | MODÉRÉ — dd15 moyen 13% |
| **Mur bid max** | 13740.0$ (spoof 0%) | Mur = INFO, spoof = TENSION |
| **Poussière moyenne** | 6.0% | Déclencheur entrée : < 15% |
| **Corrélation BTC** | 0.92 | fortement corrélé BTC (+0.92) → suit le marché |
| **Signal divergence** | neutre (stab 0) | Référence panier |

---

## 🎯 LE SET-UP INDIVIDUEL (adapté à ce comportement — à faire évoluer)

### Entrée (tout doit être vrai)
1. **Fenêtre** : uniquement **8h / 9h / 10h UTC** (le creux de CET actif).
2. **Déclencheur** : poussière < 15% + mur testé qui tient.
3. **NON — actif de marché (filtre macro >1.5% BTC/ETH indispensable)** — fortement corrélé BTC (+0.92) → suit le marché.
4. Garde-fou volume 15min < 3× moyenne 24h · FPOB ratio bid/ask ±2% > 1.2.
5. **Exécution** : 3 tranches (−1/−2/−3%) · stop dynamique 1,5× range 15min.

### Sortie
- Scaling out vers la fenêtre de pic **13h / 14h / 15h UTC**, reste derrière le trailing Hulk.

### Invalidation / risques
- **MODÉRÉ — dd15 moyen 13%**.
- Arrêter si frais réels + slippage > 1% (marge trop fine).
- Signal divergence : neutre (stab 0) — à surveiller (instable sur small caps).

---

## 🧠 DEEPDIVE 3 ROUNDS (30/08) — GO AVEC RÉSERVES 5.7/10
- **Synthèse** : `SYNTHESE_FAMILLE_DEEPDIVE_QNT_3ROUNDS_20260830.md` · consultations `scripts/CONSULTATION_FAMILLE_DEEPDIVE_QNTUSDT_ROUNDS_20260830/`.
- **Quant Network (Overledger)** : OS d'interopérabilité DLT + systèmes legacy (SWIFT/ISO 20022) — optionalité macro institutionnelle (CBDC/tokenisation).
- **Réserves** : pas de preuve on-chain de capture de valeur par le token · concurrence Chainlink CCIP · liquidité fragile · « Fusion mainnet Q1 2026 » = mirage marketing non confirmé.
- **Décision** : traiter en **tactique mean-reversion**, PAS conviction · fenêtres creux 8-10h UTC · jamais de portage long aveugle (coût d'opportunité).
- **Croisement** : `paires_croisement.json` → `observation_setup` → `deepdive_validees` (30/08).

---

## ⏱️ ÉTAT ACTUEL
- **QNTUSDT est suivie en observation** (doctrine : tous les actifs sous observation).
- Rien n'est câblé de neuf dans Hulk : ce set-up est la **cible d'observation**, à valider
  sur les prochains jours de mesure (jour 1 → jour 2 → ... différence ou pas ?).
- Fiche à réviser avec l'évolution des données (jamais statique).

## Archives
- Deepdive : `OUTBOX_OBSIDIAN/Crypto_Projet/SYNTHESE_FAMILLE_DEEPDIVE_QNT_3ROUNDS_20260830.md`
- Profil : `hulk-mexc/runs/profils_actifs/PROFIL_QNTUSDT.md`
- Suivi : `hulk-mexc/runs/SUIVI_SETUP_QNTUSDT.jsonl` + `.md`
