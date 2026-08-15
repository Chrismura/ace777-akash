# 📊 TABLEAU UNIQUE — Synthèse des vérifications (runs 14/08 + nuit 15/08)

**Généré le 15/08/2026** · Buffy (superviseur) · Sources : CSV scellés `runs/SCELLE/` + klines Binance Futures + `genesis_manifest.txt` (md5 8d9ee8d6)

---

## 🏁 1. LE MOTEUR — même champion scellé sur les 3 runs ✅

| Vérification | Résultat | Preuve |
|---|---|---|
| Genesis utilisé | **IDENTIQUE** (md5 `8d9ee8d6`) | Les 4 signatures scellées portent le même genesis_md5 |
| Headers CSV | **IDENTIQUES** (12 colonnes) | ts,cycle,side,status,entryPrice,exitPrice,qty,bps,pnl,exitReason,holdSec,msg |
| CSV "différents" ? | **NON** — c'est le même fichier append-only copié à 2 moments du scellement | 17 333 premières lignes IDENTIQUES octet à octet ; fichier 15 = fichier 14 + 3 629 lignes (la nuit) |
| Scellement (intégrité) | **INTACT** | sha256 + md5 correspondent, chmod 444, `verifier_test.sh` |
| Fix mort rc=1 (14/08) | **VALIDÉ** — plus aucune mort rc=1 | 7h06 sans mort (vs 6 morts avant), toutes fins rc=0 |

## 📈 2. LE MARCHÉ — 3 régimes différents (tendance CHANGÉE 2 fois) ✅

| Run | Fenêtre (UTC) | Tendance | Variation | Haut / Bas | Amplitude | Pente 15m |
|---|---|---|---|---|---|---|
| Run 4h #1 | 12:51 → 15:57Z | 🔺 **HAUSSIÈRE** | +0.40% | 63 062 / 62 484 | 0.92% | +22.7 $/bougie |
| Run V2 | 16:24 → 20:24Z | 🔻 **BAISSIÈRE** (inverse !) | -0.27% | 63 215 / 62 781 | 0.69% | -18.6 $/bougie |
| Run Nuit 8h | 21:45 → 05:44Z | 🔺 **HAUSSIÈRE douce** | +0.31% | 63 170 / 62 771 | 0.63% | +8.7 $/bougie |

**Vue 1h :** creux 62 484 (14:00) → rebond → sommet 63 215 (17:00) → dérive → creux 62 771 (22:00) → remontée lente → sommet 63 170 (03:00).

## 🤖 3. LES RUNS — bilan complet (duo ALPHA x13 / BETA x5)

| Run | Durée | Sessions | ALPHA trades | ALPHA PNL | BETA trades | BETA PNL | **TOTAL** |
|---|---|---|---|---|---|---|---|
| Run 4h #1 | 3h06 | 1 | 65 | **+28.26$** | 155 | +0.40$ | **+28.66$** |
| Run V2 | 4h00 | 3 | 37 | **+16.61$** | 156 | +1.97$ | **+18.58$** |
| Run Nuit 8h | 7h59 | **1 (zéro relance)** | 56 | **+8.61$** | 205 | +2.51$ | **+11.11$** |
| **Cumul 14/08** | **15h05** | — | 158 | **+53.48$** | 516 | +4.88$ | **+58.36$** |

**Nuit détail :** ALPHA 56 trades (24 win / 10 loss) · BETA 205 (73 win / 57 loss) · fin rc=0 propre à 05:44Z · 0 crash, 0 relance.

## 🎯 4. LE PATTERN REVENGE — LE point d'analyse ⚠️

| Run | % trades ALPHA en revenge | PNL ALPHA venant du revenge | % trades BETA en revenge |
|---|---|---|---|
| Run 4h #1 | **80%** (52/65) | **91%** (+25.61$) | **0%** |
| Run V2 | **68%** (25/37) | **57%** (+9.55$) | **0%** |
| Run Nuit | **91%** (51/56) | **96%** (+8.28$) | **0%** |

- **Les 3 plus gros trades nuit** (+5.41 / +2.80 / +2.40$) : TOUS en revenge.
- **Corrélation revenge ALPHA ↔ perte BETA** : seulement **14%** ≤30s (le TTL est 20s !), 59% ≤5min → **le TTL ne filtre plus rien**.
- Pertes BETA nuit : 33 · Revenge ALPHA : 51 · 17/33 pertes BETA suivies d'un revenge avant le prochain trade.

## 🕳️ 5. LES FLAT (entrée = sortie, PNL = 0)

| Run | Flat | % des trades ALPHA | Raison dominante |
|---|---|---|---|
| Run 4h #1 | 16 | **25%** | shock_inversion_stop (14) |
| Run V2 | 12 | **32%** | shock_inversion_stop (11) |
| Run Nuit | 22 | **39%** | shock_inversion_stop (19) |

Notionnel médian des flat : ~7 800-12 600$ bloqué pour zéro gain. Filtre de qualité OU capital immobilisé pour rien → à trancher.

## 🔍 6. LES INCOHÉRENCES TROUVÉES (par Buffy)

| # | Incohérence | Détail | Gravité |
|---|---|---|---|
| 1 | **Heartbeat neutralise le TTL** | `duo_touch_heartbeat` (ligne 1545) rafraîchit ts_ms à CHAQUE cycle SCOUT sans changer le reste → l'état "perte SCOUT" ne devient jamais stale → ALPHA reste armé en revenge en continu (TTL 20s inopérant) | 🔴 Haute (explication probable du revenge 91%) |
| 2 | **CSV : colonne décalée** | `holdSec` contient le message détaillé (radar=... size_note=...) au lieu de la durée ; `msg` toujours vide | 🟡 Moyenne (traçage) |
| 3 | **BETA "inutile" ?** | 3-4x plus de trades qu'ALPHA mais 0.40-2.51$ vs 8.61-28.26$ | 🟡 À valider (rôle SCOUT ?) |
| 4 | **Flat massifs** | 25% → 39% des trades ALPHA entrent/sortent au même prix | 🟡 À valider |

## 👨‍👩‍👧‍👦 7. CONCLUSION FAMILLE — ⏳ EN ATTENTE

**Dossier prêt** : `Index_Maison/scripts/consulter_famille_moteur_identique.py` (5 questions : 1) même moteur ? 2) revenge normal ? hypothèse heartbeat 3) BETA inutile ? 4) flat ? 5) CSV ?)

**⏳ NON LANCÉ** — terminal Freebuff en panne (broker ENOENT) au moment de la rédaction. À lancer dès le redémarrage. Rien n'est modifié sans validation famille/juge.

---

*Fichier de référence : ce tableau est la synthèse unique. Le détail vit dans : REVEIL_2026-08-15.md, Bilan_2026-08-14.md, MEMOIRE_COLLAB.md, runs/SCELLE/, commits GitHub 4b5af0e5 + b177c4db + 103f65d8.*
