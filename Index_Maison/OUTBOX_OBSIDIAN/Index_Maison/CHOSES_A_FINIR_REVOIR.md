# Choses à finir / revoir

**Rôle :** backlog honnête — pas la piste du jour.  
**MAJ :** 2026-07-31T14:26Z

## Phase finition (cosmétique — **gelé** jusqu’à GO finition)

| # | Item | Notes | Statut |
|---|------|-------|--------|
| F-01 | Cerveau HTML style Argona | `graph_cerveau/index.html` · grain 1px OK après fix `drawSquare` · polish densite/HUD plus tard | ⏸ finition |
| F-02 | Fond graphe Obsidian natif | snippet `ace777-graph-galactique` · **install TCC** Terminal humain · WebGL ≠ pulses | ⏸ finition |
| F-03 | Install vault Documents | `install_obsidian_graph_style.sh` (Cursor = Operation not permitted) | ⏸ finition |
| F-04 | Cockpit onglet GRAPH = même langage grain | optionnel · stack après F-01 | ⏸ finition |

**Doctrine :** cosmétique ≠ bloquant. Essentiel = fonctionnement · logique · setups · cockpit · **protocoles validation test mode pro**.

Réf : [[CERVEAU_GALACTIQUE]] · [[COCKPIT_LOOK_FIGE]]

---

## Essentiel ouvert (piste active)

| # | Item | Notes | Statut |
|---|------|-------|--------|
| E-01 | Cadence **début session** chaque matin | `session_debut.sh` · **raté 31 juil. matin** (dérive cosmétique) | 🔴 à ancrer |
| E-02 | Cadence **fin session** avant dodo (vol qui reste) | `session_fin.sh` **sans** `--stop-ace` · snapshot + OUTBOX | 🟡 scripts OK · ancrer usage |
| E-03 | Cockpit fiable (pont / feed session / daemons) | HYGIENE=OK 31 juil. · thermo garde stale · ACE **off** 09:15Z SIGTERM | 🟡 ACE off — pas de relance sans GO |
| E-04 | Validation test avant réel (portes P0→P2) | [[PROTOCOLE_VALIDATION_TEST_AVANT_REEL]] · [[JOURNAL_ERREURS_TEST]] | 🟢 doctrine · appliquer |
| E-05 | Kill-switch rouge A/B — **preuve** testnet/paper | Gardes OK (refus B sans CRASH) · reste 1×A + 1×B sur run test | 🟡 |
| E-06 | Sync Obsidian TCC | `_sync_now.sh` dans Terminal humain | 🟡 récurrent |
| E-07 | **STORM_HUNTER** — retest option | Défaut OFF · journal [[JOURNAL_MOLETTES_SETUP]] · GO + A/B plus tard (cycle 14:14 Alpha skip spread) | 🟡 à ne pas oublier |

---

## Règle
Finir / revoir cosmétique **seulement** en phase finition explicite.  
Avant toute action du jour : **début session** → plan de vol → essentiel.

[[PLAN_DE_VOL]] · [[PROTOCOLE_SESSION_DEBUT_FIN]] · [[PROTOCOLE_VALIDATION_TEST_AVANT_REEL]]
