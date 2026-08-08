# ACE777 — COFFRE-FORT V3.5 — INDEX MAÎTRE

**Réf:** `ACE777_SAUVEGARDE_ULTIME_V3.5`  
**Auteur:** Christophe — Maître d'Œuvre & Direction Technique  
**Dépôt racine:** `/Users/christophe/ace777-test-day1`  
**Champion disque (INTACT):** `genesis_manifest.txt` md5 **`37fca367`**

---

## Protocole de compilation (ordre strict)

| Étape | Fichier | Statut |
|-------|---------|--------|
| **1** | [parties/PARTIE_01_STERILITE.md](parties/PARTIE_01_STERILITE.md) | ✅ Compilé |
| **2** | [parties/PARTIE_02_SEMANTIQUE.md](parties/PARTIE_02_SEMANTIQUE.md) | ✅ Compilé |
| **3** | [parties/PARTIE_03_JALON_29USD.md](parties/PARTIE_03_JALON_29USD.md) | ✅ Compilé |
| **4** | [parties/PARTIE_04_THEORIE.md](parties/PARTIE_04_THEORIE.md) | ✅ Compilé |
| **5** | [parties/PARTIE_05_OBSIDIAN.md](parties/PARTIE_05_OBSIDIAN.md) | ✅ Compilé |
| **FIN** | [../ACE777_SAUVEGARDE_ULTIME_V3.5.md](../ACE777_SAUVEGARDE_ULTIME_V3.5.md) (monolithe assemblé) | ✅ Assemblé |

**Règle:** une partie à la fois. Code brut intégral — zéro résumé de blocs.

---

## Arborescence du coffre

```
ACE777_SAUVEGARDE_ULTIME_V3.5/
├── INDEX.md                          ← ce fichier
├── parties/                          ← compilation ordonnée (1→5)
│   ├── PARTIE_01_STERILITE.md
│   ├── PARTIE_02_SEMANTIQUE.md
│   ├── PARTIE_03_JALON_29USD.md
│   ├── PARTIE_04_THEORIE.md
│   └── PARTIE_05_OBSIDIAN.md
├── scripts/                          ← sources plomberie (copies byte)
│   ├── preflight_total_365j.sh
│   └── verif_sterilite.sh
├── snapshots/                        ← enveloppe NUAGE éphémère archivée
│   └── launch_vide_froid_4h_binance_NUAGE_V2.2.1.sh
├── genesis/                          ← moteurs md5 (37fca367, sauvegardes)
├── rapports/                         ← PnL certifiés (204206 + chaîne 10/07)
├── logs_meches/                      ← extractions LIVE/CSV trades clés
└── conversation/                     ← transcripts (liens vers ../conversation/)
```

---

## Sources vivantes (hors coffre — ne pas modifier champion)

| Ressource | Chemin |
|-----------|--------|
| Genesis actif | `/Users/christophe/ace777-test-day1/genesis_manifest.txt` |
| Config | `/Users/christophe/ace777-test-day1/config_active.env` |
| Enveloppe /tmp | `/tmp/launch_vide_froid_4h_binance_NUAGE.sh` |
| Runs prod | `/Users/christophe/ace777-test-day1/runs/NUAGE_PROD_4H_*` |
| Coffre 29$ | `/Users/christophe/ace777-test-day1/29$/` |

---

## Note date jalon Partie 3

L'index original cite « 10 juin ». Le jalon **+29 USDT** certifié = **2026-07-10**, session **204206** (20:27 UTC).  
Voir `rapports/RAPPORT_PNL_AUTO_20260710_204206.md`.

---

## Commande assemblage monolithe (après parties 1→5)

```bash
cd "/Users/christophe/ace777-test-day1/29$/historique/ACE777_SAUVEGARDE_ULTIME_V3.5"
cat parties/PARTIE_0{1,2,3,4,5}_*.md > ../ACE777_SAUVEGARDE_ULTIME_V3.5.md
```
