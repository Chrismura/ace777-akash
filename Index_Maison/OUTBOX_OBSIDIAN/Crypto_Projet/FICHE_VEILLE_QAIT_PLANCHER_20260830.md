# 📌 FICHE VEILLE — QAIT (PLANCHER) — mise à jour 30/08/2026

> **Statut : 🟡 EN VEILLE PLANCHER** — QAIT **retiré de MEXC** (delisted). Christophe attend qu'il
> atteigne **son plancher** pour un **achat RÉEL**. Cette fiche garde le contexte pour ne rien oublier.

---

## 🚨 L'ÉVÉNEMENT : QAIT delisted de MEXC

| Fait | Détail |
|---|---|
| **Premier échec API** | 29/08 2026 à **14:03:43Z** (HTTP 400 Bad Request) |
| **Dernier prix connu** | **0.001965 USDT** le 29/08 à 14:02:43Z |
| **Vérification exchangeInfo MEXC** | QAITUSDT **absent** (2072 symbols listés, QAIT non présent) |
| **Binance** | QAITUSDT aussi en HTTP 400 (pas listé non plus) |
| **Erreurs moteur accumulées** | 548 appels API 400 gaspillés en boucle (arrêté le 30/08) |

→ Le delisting n'est PAS un bug de nos sondes : la paire n'existe plus sur les exchanges testés.

## 🧹 Ce qu'on a fait (30/08, GO Christophe)

1. **Retiré QAITUSDT** de `PAPER_PAIRS` et `PAPER_EXTRA_PAIRS` (`config/defaults.env`) → le moteur
   Hulk ne tente plus la paire (fini les 548 erreurs/jour).
2. **Moteur relancé** (watchdog) pour recharger la config.
3. **Cette fiche** : QAIT reste en **veille plancher** — pas oublié, juste sorti de la rotation active.

## 🎯 L'OBJECTIF : achat réel au plancher

- Christophe attend que QAIT **atteigne son plancher** pour acheter en **vrai** (pas en paper).
- Le **creux historique du cycle** QAIT (profil 28-29/08) : zone **10h-13h UTC**, prix moyen creux ≈ **0.00195**.
- Dernier prix connu : **0.001965** (29/08 14:02Z).

## ⚠️ LE RISQUE (honnête)

- QAIT delisted de MEXC **et** Binance → la liquidité peut être repartie ailleurs (DEX ? autre CEX ?).
- Si QAIT **ne revient pas** sur un marché accessible, il n'y aura pas de « plancher » à acheter.
- **Action à prévoir** : surveiller si QAIT réapparaît sous un ticker/nouveau marché (relisting, migration).
  Une sonde légère `veille_relisting.py` peut être créée pour crier si QAIT revient sur MEXC/Binance.

## 📎 Liens utiles

- Dernier état QAIT dans le portefeuille cockpit : figé au dernier prix (reel 29.14$ / hold 27.86$, seed 10$).
- Cycle QAIT (données figées au 29/08 14:02 — plus de points après le delisting) : `hulk-mexc/runs/CYCLE_QAIT_*.md`
- Source de données coupée : `hulk-mexc/runs/croisement_contexte.jsonl` (dernier point QAIT 29/08 14:02:43Z)
