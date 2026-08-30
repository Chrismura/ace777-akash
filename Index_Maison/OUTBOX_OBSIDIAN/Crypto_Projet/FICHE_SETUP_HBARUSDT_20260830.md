# 🎯 FICHE SET-UP INDIVIDUEL — HBARUSDT (Hedera) — 30/08/2026

> **Système unique, set-up propre à CET actif** (doctrine : même système, pas même set-up).
> Profil automatique : `hulk-mexc/runs/profils_actifs/PROFIL_HBARUSDT.md` (2288 points).
> Suivi quotidien : `hulk-mexc/runs/SUIVI_SETUP_HBARUSDT.md` (mesure jour par jour, plist 16:35 locale).

---

## 📊 LE PROFIL (mesuré, 27-30/08)

| Élément | Valeur | Lecture |
|---|---|---|
| **Range total** | 7.33% | Amplitude sur la fenêtre |
| **Creux intraday** | **16h UTC** | Fenêtre d'entrée : **15h / 16h / 17h** |
| **Pic intraday** | **1h UTC** | Fenêtre de sortie : **0h / 1h / 2h** |
| **Pattern jour/nuit** | distribué | Pattern faible (0.8%) — cycle horaire peu marqué, prudent |
| **Volatilité (dd15 moy)** | 12.42% | MODÉRÉ — dd15 moyen 12% |
| **Mur bid max** | 63739.0$ (spoof 3.59%) | Mur = INFO, spoof = TENSION |
| **Poussière moyenne** | 14.6% | Déclencheur entrée : < 15% |
| **Corrélation BTC** | 0.87 | fortement corrélé BTC (+0.87) → suit le marché |
| **Signal divergence** | neutre (stab 0) | Référence panier |

---

## 🎯 LE SET-UP INDIVIDUEL (adapté à ce comportement — à faire évoluer)

### Entrée (tout doit être vrai)
1. **Fenêtre** : uniquement **15h / 16h / 17h UTC** (le creux de CET actif).
2. **Déclencheur** : poussière < 15% + mur testé qui tient.
3. **NON — actif de marché (filtre macro >1.5% BTC/ETH indispensable)** — fortement corrélé BTC (+0.87) → suit le marché.
4. Garde-fou volume 15min < 3× moyenne 24h · FPOB ratio bid/ask ±2% > 1.2.
5. **Exécution** : 3 tranches (−1/−2/−3%) · stop dynamique 1,5× range 15min.

### Sortie
- Scaling out vers la fenêtre de pic **0h / 1h / 2h UTC**, reste derrière le trailing Hulk.

### Invalidation / risques
- **MODÉRÉ — dd15 moyen 12%**.
- Arrêter si frais réels + slippage > 1% (marge trop fine).
- Signal divergence : neutre (stab 0) — à surveiller (instable sur small caps).

---

## 🏦 DEEPDIVE PROJET (30/08 — 3 rounds famille + vérification 2 sources)

- **HBAR = Hedera Hashgraph** : DLT enterprise, finalité instantanée, gouverné par le Hedera Council (Google, IBM, Accenture, Boeing, Deutsche Telekom...). Positionnement existant : `ACTEURS_BLOCKCHAIN_XRP_HBAR_CC` (29/08).
- **🔥 Accenture rejoint le Council (30/04/2026)** pour l'IA d'entreprise + NVIDIA/Intel/EQTY sur gouvernance IA vérifiable + Agentic AI Foundation (06/2026) — thèse « couche de confiance de l'IA » confirmée.
- **Famille 3 rounds : GO AVEC RÉSERVES (6.5/10, 3/3)** — premier actif validé. MAIS : **GO long terme institutionnel (3 ans), NON pour le trade tactique court terme**.
- **Réserves** : tokenomics dilution (« piège à valeur ») · volume DEAD + corr BTC 0.87 (aucune dynamique endogène) · faible capture de valeur (TPS ≠ valeur token).
- **Décision** : position paper 20$ = **noyau SOCLE** (patrimoine 3 ans), PAS d'achat tactique tant que volume DEAD, set-up fenêtre 15-17h + filtre macro reste la règle si entrée (jamais hors fenêtre — leçon de l'entrée 28/08).
- Synthèse : `SYNTHESE_FAMILLE_DEEPDIVE_HBAR_3ROUNDS_20260830.md` + avis R1/R2/R3 dans `scripts/CONSULTATION_FAMILLE_DEEPDIVE_HBARUSDT_ROUNDS_20260830/`.

---

## ⏱️ ÉTAT ACTUEL
- **HBARUSDT est suivie en observation** (doctrine : tous les actifs sous observation).
- Rien n'est câblé de neuf dans Hulk : ce set-up est la **cible d'observation**, à valider
  sur les prochains jours de mesure (jour 1 → jour 2 → ... différence ou pas ?).
- Fiche à réviser avec l'évolution des données (jamais statique).

## Archives
- Profil : `hulk-mexc/runs/profils_actifs/PROFIL_HBARUSDT.md`
- Suivi : `hulk-mexc/runs/SUIVI_SETUP_HBARUSDT.jsonl` + `.md`
