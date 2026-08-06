# Journal Cockpit — horloge & évolution

**Rôle :** le cockpit est un **produit à part** (lecture / Cortana / BOARD).  
S’il ne tourne pas comme une horloge → c’est un **problème ops**, pas un détail UI.  
**Ne pas mélanger** avec le juge trading (fills CSV) ni avec [[JOURNAL_ERREURS_TEST]] (sauf P0 partagé).

| Canon | Fichier |
|-------|---------|
| Look | [[COCKPIT_LOOK_FIGE]] |
| Zone test | [[2026-07-30_cockpit_zone_test]] |
| Hygiène | `scripts/cockpit_hygiene_check.sh` |
| Pont | `scripts/cortana_cockpit_bridge.py` (:17777) |
| Voix | [[CORTANA_VOIX]] · pré-son `CORTANA_PRECHIME` |

---

## Horloge (doit être vert avant lecture run)

| # | Check | OK si |
|---|-------|-------|
| H1 | Thermo free | funding / OI / F&G / score présents |
| H2 | Mission feed | `mission.json` frais · run visible |
| H3 | Pont Cortana | pastille **PONT ON** (ex-« FEED OFF » = pont éteint) |
| H3b | Liens ACE / NET | pastilles haut-droite · ACE=LIVE frais · NET=ping Binance |
| H4 | UI | OPS + THERMO + **BOARD** + VOL chargent |
| H5 | Voix | pré-son suave puis Vivienne (pas de cri d’un coup) |
| H6 | News boucle | rotation ~14 s + chime doux (pas spam) |

`COCKPIT_HYGIENE=OK` = H1–H3. Sans pont → NOK lecture live (normal).

```bash
bash ~/ace777-test-day1/Index_Maison/scripts/cockpit_hygiene_check.sh
python3 ~/ace777-test-day1/Index_Maison/scripts/cortana_cockpit_bridge.py   # Terminal dédié
open ~/ace777-test-day1/Index_Maison/cockpit/index.html
```

---

## Journal d’évolution (récent en haut)

| ts | Qui | sev | Quoi | Suite |
|----|-----|-----|------|-------|
| 2026-07-31T0927Z | Cursor | — | **PREFLIGHT OPS** pastilles vert/rouge + PROTO+ · `/preflight` | Allumage fusée · clic = où aller |
| 2026-07-31T0915Z | Cursor | P1 | Thermo écrasait funding/OI/F&G à `None` si API flop → HYGIENE=NOK | `thermo_quotidien_free` garde dernier bon + `degraded` · session_debut refresh thermo |
| 2026-07-31T0915Z | Cursor | — | Panic garde-fous OK (B sans CRASH refusé · mode X refusé) | Preuve A/B réelle = GO quand run test stoppable |
| 2026-07-31T0526Z | Cursor | P1 | Écran noir app `file://` | Fix: HTTP local `:17800` dans `open_cockpit_app.py` |
| 2026-07-30T2120Z | Cursor | P2 | Pré-son suave avant TTS + chime news boucle UI | `cortana_voice.play_prechime` · cockpit `softNewsChime` |
| 2026-07-30T2110Z | Cursor | — | Onglet BOARD = thermo SIMPLE/COMPLET | iframe `thermo/index.html` |
| 2026-07-30T2055Z | Cursor | — | Zone test + hygiène indicateurs | S22 |
| 2026-07-30T21xxZ | ops | P2 | Pont OFF → HYGIENE=NOK | Relancer bridge (attendu) |

---

## Backlog évolution (pas du trading)

| id | Idée | Priorité |
|----|------|----------|
| C-00 | **App fenêtre dédiée** — pywebview 1ˢ · Brave `--app` filet · `cockpit_up.sh` + LaunchAgents pont/HTTP | ✅ 31 juil. |
| C-01 | Launchd / keep-alive pont :17777 | ✅ agents running |
| C-02 | Aligner PnL α affichage ↔ CSV (P1 si trompeur) | ✅ session vs life 30 juil. |
| C-03 | LIQ/ETF free ou n/d explicite figé | 🔵 WARN ok |
| C-04 | Volume chime / pré-son réglable UI | 🔵 |
| C-05 | **Kill-switch A/B** — preuve testnet/paper (gardes UI OK) | 🟡 reste 1×A + 1×B |
| **C-06** | **GRAPH synapses** — onglet connexions dynamiques (ACE/PONT/NET/αβ/Hulk…) | ✅ UI 31 juil. · polish → finition |
| C-07 | Thermo ne doit pas écraser core à None | ✅ 31 juil. |
| **C-08** | **PREFLIGHT OPS** — checklist allumage vert/rouge + où aller | ✅ 31 juil. |

---

## Règle

1. Bug cockpit → **ici** (et Attention si P0/P1).  
2. Bug fills / edge → [[JOURNAL_ERREURS_TEST]].  
3. Évolution UI = lignes backlog + mémoire collab — pas de patch hot pendant run test sans note.
