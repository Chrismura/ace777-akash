# [PARTIE 5] — ARCHITECTURE DE MÉMOIRE LOCALE (OBSIDIAN)

**Statut:** ✅ Compilé  
**Réf:** ACE777_SAUVEGARDE_ULTIME_V3.5  

---

## 5.1. Structuration du Coffre-Fort de Fichiers Markdown (.md)

### Principe

Tout artefact ACE777 est stocké en **texte pur UTF-8** (.md, .csv, .sh, .json) — zéro format propriétaire. Compatible MacBook Air M1 offline, grep, Obsidian, Khoj, git.

### Arborescence coffre V3.5 (implémentation)

```
ace777-test-day1/
├── 29$/historique/ACE777_SAUVEGARDE_ULTIME_V3.5/   ← COFFRE ACTIF
│   ├── INDEX.md
│   ├── parties/PARTIE_01..05_*.md
│   ├── scripts/preflight_total_365j.sh
│   ├── scripts/verif_sterilite.sh
│   ├── snapshots/launch_vide_froid_4h_binance_NUAGE_V2.2.1.sh
│   ├── genesis/genesis_manifest.txt_ACTIF_37fca367
│   ├── rapports/RAPPORT_PNL_AUTO_20260710_*.md
│   ├── logs_meches/trade_*.log|csv|txt
│   └── conversation/README.md → liens transcripts
├── runs/
│   ├── NUAGE_PROD_4H_*.csv              ← fills bruts prod
│   ├── NUAGE_PROD_4H_LIVE_COLOR.log      ← duo intercalé terminal
│   └── RAPPORT_PNL_AUTO_*.md             ← bilans auto post-run
├── master_base/pnl/                      ← archive rapports datés
└── genesis_manifest.txt                  ← CHAMPION INTACT md5 37fca367
```

### Standards de nommage

| Type | Pattern | Exemple |
|---|---|---|
| Rapport PnL | `RAPPORT_PNL_AUTO_YYYYMMDD_HHMMSS.md` | `RAPPORT_PNL_AUTO_20260710_204206.md` |
| CSV fills | `{TAG}_{UNIT}.csv` | `NUAGE_PROD_4H_ALPHA_X13_BURST13.csv` |
| LIVE intercalé | `{TAG}_LIVE_COLOR.log` | `NUAGE_PROD_4H_LIVE_COLOR.log` |
| Snapshot moteur | `genesis_manifest.txt_{LABEL}_{md5prefix}` | `genesis_manifest.txt_ACTIF_37fca367` |
| Trade clé | `trade_YYYYMMDD_HHMM_desc.*` | `trade_20260714_1247_LIVE.log` |

### Bilans sessions NUAGE_PROD_4H certifiés (14–15/07/2026)

| Session | UTC | Durée | BETA | ALPHA | Total |
|---|---|---|---|---|---|
| Matin champion | 11:26→~15:00 | ~3h | -0,25 | +35,49 | **~+35,24** |
| Soir #1 | 20:50→22:04 | 1h14 | +0,57 | +1,39 | **+1,95** |
| Nuit #2 (timer OK) | 22:22→02:22 | **4h00** | -2,44 | +9,95 | **+7,51** |
| Matin 15/07 | 04:49→05:25 | 36m | +0,35 | -0,96 | **-0,61** (Ctrl+C) |

---

## 5.2. Indexation Vectorielle (Khoj & Smart Connections sur GitHub)

### Fonctionnement technique

1. **Corpus indexé:** tous les `.md` du coffre + en-têtes CSV + rapports PnL + transcripts conversation
2. **Embeddings locaux:** modèle sentence-transformers exécuté en batch (pas pendant run trading)
3. **Charge CPU:** **0% constante** en run — indexation nocturne ou post-session uniquement
4. **Smart Connections (Obsidian):** graphe de liens entre concepts (`duo_hunter_signal`, `NUAGE gate 800ms`, `204206`, etc.)

### Requêtes types (retrieval instantané)

| Question naturelle | Fichier retrouvé |
|---|---|
| « bilan session nuit 22:22 timer » | `RAPPORT_PNL_AUTO_20260714_221939.md` |
| « trade +32 juillet 12h47 » | `logs_meches/trade_20260714_1247_*` |
| « jalon +29 dollars » | `rapports/RAPPORT_PNL_AUTO_20260710_204206.md` |
| « preflight ping solde » | `scripts/preflight_total_365j.sh` |
| « zombies tail pid » | `snapshots/launch_vide_froid_4h_binance_NUAGE_V2.2.1.sh` |

### Workflow assistant + coffre

```
User question → Khoj embedding search → top-3 chunks .md
           → Agent lit fichier source intégral (pas résumé)
           → Réponse citant path + ligne
```

### GitHub = remote coffre

- Push du dossier `29$/historique/` = backup off-machine
- Obsidian = vue humaine locale (graph, backlinks)
- Khoj = retrieval agent (semantic search)

### Assemblage monolithe final

```bash
cd "/Users/christophe/ace777-test-day1/29$/historique/ACE777_SAUVEGARDE_ULTIME_V3.5"
{
  echo "# ACE777 — MANIFESTE DE SAUVEGARDE ULTIME V3.5 (MONOLITHIQUE)"
  echo "**Assemblé:** $(date -u +%Y-%m-%dT%H:%M:%SZ)"
  echo ""
  cat parties/PARTIE_01_STERILITE.md
  echo ""
  cat parties/PARTIE_02_SEMANTIQUE.md
  echo ""
  cat parties/PARTIE_03_JALON_29USD.md
  echo ""
  cat parties/PARTIE_04_THEORIE.md
  echo ""
  cat parties/PARTIE_05_OBSIDIAN.md
  echo ""
  echo "---"
  echo "## ANNEXE — Enveloppe NUAGE V2.2.1 INTÉGRALE"
  echo '```bash'
  cat snapshots/launch_vide_froid_4h_binance_NUAGE_V2.2.1.sh
  echo '```'
} > ../ACE777_SAUVEGARDE_ULTIME_V3.5.md
```
