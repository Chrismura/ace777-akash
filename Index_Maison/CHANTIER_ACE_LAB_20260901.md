# CHANTIER — ACE LAB · 2026-09-01

> Copie de travail complète du projet + champion scellé en double.
> Pépites Signets_X intégrées au protocole. Testnet uniquement.

## 1. Ce qui existe maintenant

| Emplacement | Rôle | Intégrité |
|---|---|---|
| `~/ace777-test-day1/` | Projet original — champion en production | Champion intact, MD5 `14bcf868d46effba010cac577cbb004c` |
| `~/ace777-test-day1/champion_sealed_20260901T205022Z/` | **Copie scellée #1** (dans le projet) | `genesis_manifest.txt` + `.md5` + `.sha256` + certificat |
| `~/ace-lab-20260901T205042Z/` | **Chantier de travail** — on y ouvre tout | Copie de travail, modifiable librement |

Vérification effectuée : le `genesis_manifest.txt` du chantier a le même MD5
que le champion scellé → point de départ identique, toute divergence sera
désormais **intentionnelle**.

> Pourquoi deux copies ? Le champion a déjà été perdu deux fois. Désormais :
> une copie scellée dans le projet + une copie de travail séparée. On ne
> reconstruira plus jamais à partir d'indices.

## 2. Règles du chantier (rappel)

1. Le champion original est scellé — on ne le touche jamais.
2. Dans le lab, `genesis_manifest.txt` est une copie de travail : on peut la
   modifier, la déboguer, la casser. C'est son but.
3. Une variable à la fois.
4. Testnet uniquement (`BINANCE_MODE=testnet`). LIVE interdit.
5. Chaque expérience produit des données dans `runs/`.

## 3. Pépites Signets_X intégrées au protocole

Source : `~/Documents/Obsidian_ACE777/Evaluations/PEPITES_SIGNETS_APPLICATION.md`

| Pépite | Application au chantier ACE |
|---|---|
| #2 — Backtest vs live (EV surestimé) | Le replay radar-aligned (+8,47 estimé) ne compte pas tant qu'un run testnet ne le confirme pas. |
| #3 — "One number tells you if your edge is real" | Critère d'edge écrit AVANT les runs (voir §4). |
| #4 — La sortie compte plus que la position | Expérience prioritaire : revoir stops/trailing Beta (8 stop_loss = -17,08 net). |
| #17 — Alpha Orchestration Layer (graphe) | Blueprint du futur moteur : signal → neutralisation → risk parity → optimiseur → netting + snapshot isolation. |
| #18/#19 — Loop → Graph, "celui qui produit ne note pas" | Toute modification moteur : test automatisé de bout en bout avant run testnet humain. |
| #1/#7 — Gamma & liquidité (GEX) | Déjà branché côté cockpit (Thermo C23-C25) — à garder pour le contexte régime. |

## 4. Critère d'edge (écrit avant les runs)

Un setup est déclaré **edge réel** si, sur un run testnet d'au moins 2 heures
(ou 30 trades minimum par unité) :

1. **PnL net par trade > frais moyen par trade** (aujourd'hui ~0,55 USDT/trade
   d'après les runs V2–V4) ;
2. **Win rate net > 50 %** sur la fenêtre ;
3. **Aucune sortie `stop_loss`** ne représente plus de 40 % des pertes totales.

Si le critère n'est pas atteint après instrumentation propre + 3 expériences
distinctes → verdict **"stratégie non rentable net Binance"**, on arrête, et
c'est une victoire (pas de vrai argent perdu).

## 5. Journal des expériences

| # | Date | Expérience | Variable | Statut | Résultat |
|---|---|---|---|---|---|
| 0 | 2026-09-01 | Création du chantier | — | ✅ | Copie + scellage double, MD5 vérifié |
| 1 | 2026-09-01 | Radar-aligned (Beta suit le radar) | Suppression `FORCE_ENTRY_SIDE=SELL` Beta | ⏳ Replay fait (+8,47 estimé), run testnet à relancer | — |
| 2 | — | Sorties Beta | Élagage stop_loss / élargissement trailing | 💤 | Dépend de #1 |
| 3 | — | Modèle de confiance | Recalibrage (conf 0,85-0,99 = pires trades) | 💤 | Dépend de #1 |

## 6. Prochaine action

Relancer le run testnet de l'expérience #1 (15 min, compte à plat) puis
comparer `PNL_TOTAL`, `DIAG_VERDICT`, `WHY_ARRET` avec les runs V2–V4.
