# Choses à finir / revoir

**Rôle :** backlog honnête — pas la piste du jour.  
**MAJ :** 2026-08-18

## 🛠 Ressources externes — à ne pas oublier

| # | Item | Notes | Statut |
|---|------|-------|--------|
| R-01 | **Claude chat (gratuit, sans API)** | Décision 18/08 : garder pour **checks légers mais importants** (2e avis ponctuel, lecture de morceaux de code). Pas branchable au hub (pas d'API free). Ne pas confondre avec un « cerveau » de la maison. | ✅ décidé 18/08 — à utiliser |
| R-02 | **Data Formulator (Microsoft, open source)** | Pépite du 18/08 : visualisation de données pilotée IA, tourne avec Ollama local, gratuit. **Pas encore installé** (uvx dispo). | 🟡 à installer (GO) |

---

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
| E-08 | **ALPHA rc=1 — cause racine** (14/08) | Mort silencieuse ~13 min après départ, juste après un fill · `set -euo pipefail` + stderr avalé · trap FATAL_RC1 posé (genesis_manifest) → **relancer un run pour attraper la ligne** · audit famille 6/6 dans A_Mon_Attention | 🔴 priorité |
| E-09 | **Auto-relance Alpha + « jamais chasseur solitaire »** | Famille 6/6 : relancer l'unité morte (max 3, pause) ou stopper le binôme proprement · sinon BETA tourne seul 2h (E-DUO) | 🟡 chantier |
| E-10 | **Cortana dit la vérité** | Elle lit live/mission figés → annonce « Alpha et Beta actifs » (faux) · doit lire `/status` (ace.state) | 🔴 |
| E-11 | **Mute partiel** | 5 chemins voix locaux ignorent `.cortana_mute` (VOIX, 🐈, brief 8h10, analyste, yeux) — à aligner sur cortana_voice | 🟡 |
| E-12 | **Deux briefs (doublon chaîne)** | brief complet/opinion + brief court « perroquet » · identifier les générateurs et n'en garder qu'un (brief 4/j) | 🟡 |
| E-13 | **Fenêtre info IA graph** | S'ouvre sur le bouton rafraîchissement (signalé 14/08) — non vérifié | 🟡 |
| E-14 | Budget cloud / baromètre conso / brief 4j / schéma architecture | Chantiers notés (tableau) — pas traités | 🟡 |
| E-15 | **Shadow Mode Scénario C — run 14 jours** | Lancé 02/09 17:26Z (pid 51855) · verdict 16/09 · GEL total : aucune modif avant J+14 · J+1 : stats 24h brut → Gemini, analyse séparée puis confrontation famille · Détail complet : [[CHANTIER_SHADOW_MODE_SC_20260902]] | 🟢 EN COURS |

---

## Règle
Finir / revoir cosmétique **seulement** en phase finition explicite.  
Avant toute action du jour : **début session** → plan de vol → essentiel.

[[PLAN_DE_VOL]] · [[PROTOCOLE_SESSION_DEBUT_FIN]] · [[PROTOCOLE_VALIDATION_TEST_AVANT_REEL]]
