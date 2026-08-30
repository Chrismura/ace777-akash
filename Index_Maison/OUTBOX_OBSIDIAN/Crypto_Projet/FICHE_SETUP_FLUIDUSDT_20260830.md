# 🎯 FICHE SET-UP INDIVIDUEL — FLUIDUSDT (Fluid) — 30/08/2026

> **Système unique, set-up propre à CET actif** (doctrine : même système, pas même set-up).
> Profil automatique : `hulk-mexc/runs/profils_actifs/PROFIL_FLUIDUSDT.md` (224 points).
> Suivi quotidien : `hulk-mexc/runs/SUIVI_SETUP_FLUIDUSDT.md` (mesure jour par jour, plist 16:35 locale).

---

## 📊 LE PROFIL (mesuré, 27-30/08)

| Élément | Valeur | Lecture |
|---|---|---|
| **Range total** | 0.83% | Amplitude sur la fenêtre |
| **Creux intraday** | **10h UTC** | Fenêtre d'entrée : **9h / 10h / 11h** |
| **Pic intraday** | **15h UTC** | Fenêtre de sortie : **14h / 15h / 16h** |
| **Pattern jour/nuit** | distribué | Pattern faible (0.0%) — cycle horaire peu marqué, prudent |
| **Volatilité (dd15 moy)** | 22.85% | ÉLEVÉ — dd15 moyen 23% (volatile, stops à respecter) |
| **Mur bid max** | 0$ (spoof 0%) | Mur = INFO, spoof = TENSION |
| **Poussière moyenne** | 6.0% | Déclencheur entrée : < 15% |
| **Corrélation BTC** | 0.39 | faiblement corrélé BTC (+0.39) → plutôt endogène |
| **Signal divergence** | neutre (stab 0) | Référence panier |

---

## 🎯 LE SET-UP INDIVIDUEL (adapté à ce comportement — à faire évoluer)

### Entrée (tout doit être vrai)
1. **Fenêtre** : uniquement **9h / 10h / 11h UTC** (le creux de CET actif).
2. **Déclencheur** : poussière < 15% + mur testé qui tient.
3. **OUI (dé-corrélé) — mais vérifier si c'est de la liquidité fine** — faiblement corrélé BTC (+0.39) → plutôt endogène.
4. Garde-fou volume 15min < 3× moyenne 24h · FPOB ratio bid/ask ±2% > 1.2.
5. **Exécution** : 50% au contact / 50% si poussière <10% · stop dynamique 1,5× range 15min.

### Sortie
- Scaling out vers la fenêtre de pic **14h / 15h / 16h UTC**, reste derrière le trailing Hulk.

### Invalidation / risques
- **ÉLEVÉ — dd15 moyen 23% (volatile, stops à respecter)**.
- Arrêter si frais réels + slippage > 1% (marge trop fine).
- Signal divergence : neutre (stab 0) — à surveiller (instable sur small caps).

---

## 🧠 DEEPDIVE 3 ROUNDS (30/08) — GO AVEC RÉSERVES 7.4/10 ✅
- **Synthèse** : `SYNTHESE_FAMILLE_DEEPDIVE_FLUID_3ROUNDS_20260830.md` · consultations `scripts/CONSULTATION_FAMILLE_DEEPDIVE_FLUIDUSDT_ROUNDS_20260830/`.
- **Fluid (ex-Instadapp)** : hub DeFi unifié Lending + Vaults + DEX sur liquidité partagée — architecture de rupture, équipe prouvée (2018+).
- **Réserves** : risque smart contract systémique (modules imbriqués) · fee-switch à prouver (valeur token vs TVL) · rumeur Jupiter/Solana = PAS DE SOURCE, invalidée (ancré EVM).
- **Décision** : candidat MOTEUR · seed gardée · pas d'agrandissement avant vérif TVL (DefiLlama) + fee-switch + fenêtres confirmées.
- **Croisement** : `paires_croisement.json` → `deepdive_validees` (30/08).

---

## ⏱️ ÉTAT ACTUEL
- **FLUIDUSDT est suivie en observation** (doctrine : tous les actifs sous observation).
- Rien n'est câblé de neuf dans Hulk : ce set-up est la **cible d'observation**, à valider
  sur les prochains jours de mesure (jour 1 → jour 2 → ... différence ou pas ?).
- Fiche à réviser avec l'évolution des données (jamais statique).

## Archives
- Deepdive : `OUTBOX_OBSIDIAN/Crypto_Projet/SYNTHESE_FAMILLE_DEEPDIVE_FLUID_3ROUNDS_20260830.md`
- Profil : `hulk-mexc/runs/profils_actifs/PROFIL_FLUIDUSDT.md`
- Suivi : `hulk-mexc/runs/SUIVI_SETUP_FLUIDUSDT.jsonl` + `.md`
