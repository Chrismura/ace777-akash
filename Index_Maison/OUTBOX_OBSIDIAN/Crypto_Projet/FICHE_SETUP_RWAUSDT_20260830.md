# 🎯 FICHE SET-UP INDIVIDUEL — RWAUSDT (Allo (RWA)) — 30/08/2026

> **Système unique, set-up propre à CET actif** (doctrine : même système, pas même set-up).
> Profil automatique : `hulk-mexc/runs/profils_actifs/PROFIL_RWAUSDT.md` (224 points).
> Suivi quotidien : `hulk-mexc/runs/SUIVI_SETUP_RWAUSDT.md` (mesure jour par jour, plist 16:35 locale).

---

## 📊 LE PROFIL (mesuré, 27-30/08)

| Élément | Valeur | Lecture |
|---|---|---|
| **Range total** | 0.9% | Amplitude sur la fenêtre |
| **Creux intraday** | **10h UTC** | Fenêtre d'entrée : **9h / 10h / 11h** |
| **Pic intraday** | **14h UTC** | Fenêtre de sortie : **13h / 14h / 15h** |
| **Pattern jour/nuit** | distribué | Pattern faible (0.0%) — cycle horaire peu marqué, prudent |
| **Volatilité (dd15 moy)** | 4.5% | MODÉRÉ — dd15 moyen 4% |
| **Mur bid max** | 0$ (spoof 0%) | Mur = INFO, spoof = TENSION |
| **Poussière moyenne** | 6.0% | Déclencheur entrée : < 15% |
| **Corrélation BTC** | 0.96 | fortement corrélé BTC (+0.96) → suit le marché |
| **Signal divergence** | neutre (stab 0) | Référence panier |

---

## 🎯 LE SET-UP INDIVIDUEL (adapté à ce comportement — à faire évoluer)

### Entrée (tout doit être vrai)
1. **Fenêtre** : uniquement **9h / 10h / 11h UTC** (le creux de CET actif).
2. **Déclencheur** : poussière < 15% + mur testé qui tient.
3. **NON — actif de marché (filtre macro >1.5% BTC/ETH indispensable)** — fortement corrélé BTC (+0.96) → suit le marché.
4. Garde-fou volume 15min < 3× moyenne 24h · FPOB ratio bid/ask ±2% > 1.2.
5. **Exécution** : 3 tranches (−1/−2/−3%) · stop dynamique 1,5× range 15min.

### Sortie
- Scaling out vers la fenêtre de pic **13h / 14h / 15h UTC**, reste derrière le trailing Hulk.

### Invalidation / risques
- **MODÉRÉ — dd15 moyen 4%**.
- Arrêter si frais réels + slippage > 1% (marge trop fine).
- Signal divergence : neutre (stab 0) — à surveiller (instable sur small caps).

---

## 🧠 DEEPDIVE 3 ROUNDS (30/08) — NON 1.7/10 🚨
- **Synthèse** : `SYNTHESE_FAMILLE_DEEPDIVE_RWA_3ROUNDS_20260830.md` · consultations `scripts/CONSULTATION_FAMILLE_DEEPDIVE_RWAUSDT_ROUNDS_20260830/`.
- **⚠️ CONFUSION RÉSOLUE** : RWAUSDT = **Xend Finance** (ex-XEND, migré 05/2026) — PAS RWA Inc. (RWAINC) ni Allo.
- **Xend Finance** : DeFi pour coopératives/credit unions (Nigeria) · rebranding « RWA » = artifice cosmétique, pas de tokenisation institutionnelle réelle · dilution XEND→RWA à auditer.
- **Risques** : liquidité mortifère (<50k$/24h, slippage 10-30%) · confusion ticker · obsolescence technologique.
- **Décision** : NON unanime · croisement PRIX SEUL · **ne pas agrandir la seed** · sonde delisting active.
- **Croisement** : `paires_croisement.json` → il était ABSENT alors que tradé (faille de gouvernance) → `observation_setup` (30/08).

---

## ⏱️ ÉTAT ACTUEL
- **RWAUSDT est suivie en observation** (doctrine : tous les actifs sous observation).
- Rien n'est câblé de neuf dans Hulk : ce set-up est la **cible d'observation**, à valider
  sur les prochains jours de mesure (jour 1 → jour 2 → ... différence ou pas ?).
- Fiche à réviser avec l'évolution des données (jamais statique).

## Archives
- Deepdive : `OUTBOX_OBSIDIAN/Crypto_Projet/SYNTHESE_FAMILLE_DEEPDIVE_RWA_3ROUNDS_20260830.md`
- Profil : `hulk-mexc/runs/profils_actifs/PROFIL_RWAUSDT.md`
- Suivi : `hulk-mexc/runs/SUIVI_SETUP_RWAUSDT.jsonl` + `.md`
