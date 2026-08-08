# Plan — rapatrier l’agora (sans refaire sauter Obsidian)

**Objectif :** un **seul** coffre stable, tout ce qui sert à la collab (toi / Cursor / Gemini / Kimi / Punk / Cortana), **zéro** code lourd ni `target/` dans le vault.

**Vault actuel (stable) :** `Documents/Obsidian_ACE777_LIGHT`  
**Ancien gros vault :** `Documents/Obsidian_ACE777` (en pause)  
**Hors vault (OK) :** `~/Assistant_Vocal_HORS_VAULT/` · `~/Obsidian_BACKUPS_HORS_VAULT/` · `~/crypto-voice-assistant-core/`

**Règle d’or à chaque phase :** copier → ouvrir Obsidian 2–3 min → si OK, phase suivante. Si saute → rollback de la phase, stop.

---

## Carte : où est quoi aujourd’hui

| Contenu | Où | Action finale |
|---------|-----|----------------|
| AGORA, Mémoire collab, Tableau, Swarm basique | **LIGHT** (déjà) | Garder / enrichir |
| Suivi_Info, A_Mon_Attention, Indicateurs, Évals | Gros vault `Index_Maison/` | → LIGHT phase B |
| Swarm_Bus complet (01…08, Punk checks) | Gros vault `Swarm_Bus/` | → LIGHT phase C (md only) |
| Cahier, Hulk notes md | Gros vault | → LIGHT phase D (md only, filtré) |
| Projet_1 Nuage, code, Cargo, `.env` | Gros / HORS | **JAMAIS** dans Obsidian |
| `target/`, backups 4 Go | HORS_VAULT | **JAMAIS** dans Obsidian |
| `.obsidian` corrompu / smart-connections | HORS | Ignorer |

---

## Architecture cible (un vault)

Nom proposé : **`Obsidian_ACE777`** (on pourra **renommer LIGHT → ce nom** à la fin, ou vider le gros et y coller le LIGHT).

```
Obsidian_ACE777/          ← seul coffre ouvert
├── AGORA.md
├── 00_PLAN_RAPATRIEMENT.md
├── Swarm_Bus/            ← md handoffs only
├── Index_Maison/         ← tableau, suivi, attention, évals
├── Cahier/               ← notes md utiles (pas binaires)
└── .obsidian/            ← plugins OFF graph OFF au début
```

**Hors coffre (liens dans une note) :**
- Code vocal / Cortana
- ACE runs / scripts
- Backups lourds

---

## Phase 0 — Gel (fait)

- [x] LIGHT stable
- [x] Code Rust / `target/` hors vault
- [x] Graph / community plugins OFF
- [x] GPU flags prudents (`argv.json`)

**Critère GO phase A :** tu confirmes (comme maintenant) que LIGHT ne saute pas.

---

## Phase A — Hygiene LIGHT (5 min)

1. Note `00_PLAN_RAPATRIEMENT.md` dans LIGHT (= ce fichier).
2. Vérifier liens AGORA → mémoire + tableau.
3. Une ligne dans `09_MEMOIRE_COLLAB` : « plan rapatriement validé ».

**Critère :** OK 2 min.

---

## Phase B — Index Maison complet (priorité agora)

Copier **uniquement des `.md`** depuis  
`Documents/Obsidian_ACE777/Index_Maison/` → LIGHT :

| Priorité | Dossier / fichier |
|----------|-------------------|
| 1 | `Suivi_Info/` |
| 2 | `A_Mon_Attention/` |
| 3 | `00_INDICATEURS_V1.md`, `00_LIRE_MOI.md` |
| 4 | `Evaluations/*.md` |
| 5 | `Decisions/`, `Idees/` si non vides |

**Interdit :** tout fichier non-md, `.env`, binaires.

**Critère :** OK 3 min + file explorer lisible.

---

## Phase C — Swarm_Bus utile

Copier md manquants du gros `Swarm_Bus/` :

- `01_ETAT_GLOBAL.md` … `08_LECONS.md` (templates OK)
- `07_PUNK_VEILLE.md`
- Dossier `Punk/` : **seulement** les 20 derniers `CHECK_*.md` (pas tout l’historique si énorme)

**Critère :** OK 3 min. Pas ouvrir Graph.

---

## Phase D — Notes humaines utiles (filtré)

Depuis le gros vault, **md only**, dossiers candidats :

- `Cahier/` (si notes courtes)
- `Hulk/` (docs, pas logs énormes)
- `Veille_secteur/`
- `ACE777-Constitution.md`

**Skip automatique si fichier > 500 Ko** (sauf GO explicite).

**Critère :** OK 5 min.

---

## Phase E — Un seul nom de coffre

Deux options (choisir une) :

| Option | Comment |
|--------|---------|
| **E1 — LIGHT devient le vrai** | Renommer `Obsidian_ACE777_LIGHT` → `Obsidian_ACE777_STABLE` ; archiver l’ancien gros en `Obsidian_ACE777_ARCHIVE_LOURD` **hors** Documents ou zip HORS_VAULT ; un seul vault dans `obsidian.json` |
| **E2 — Vider le gros et y mettre LIGHT** | Backup gros → HORS ; remplacer contenu par LIGHT ; un path historique |

**Recommandé : E1** (moins risqué).

**Critère :** Manage vaults = **1** entrée ; AGORA s’ouvre.

---

## Phase F — Soft power (plus tard)

1. Réactiver **un** plugin à la fois (jamais Smart Connections tant que fragile).
2. Graph : seulement si Mac tiède + vault < ~50 Mo md.
3. Cortana lit `10_ATTENTION_VOCALE` dans ce vault.
4. Punk `OBSIDIAN_DIR` → path du vault unique.

---

## Checklist anti-crash (chaque phase)

- [ ] Obsidian quitté avant copie
- [ ] Copie md only
- [ ] `du -sh` vault < **100 Mo** idéalement (< 200 Mo max)
- [ ] Rouvrir → rester 2–3 min sur AGORA
- [ ] 1 ligne dans mémoire collab : phase X OK / FAIL

**Si FAIL :** retirer les fichiers de la phase ; ne pas empiler.

---

## Ce qu’on ne rapatrie **jamais**

- `Assistant_Vocal` code / `Cargo.*` / `target/`
- Backups `_backup_vault_merge_*`
- `.obsidian_corrompu`, Smart Connections stopped
- Runs ACE, CSV fills, logs bruts (lien depuis note OK)
- Secrets `.env`

---

## Ordre de GO (humain)

1. **GO A** — hygiene + ce plan dans LIGHT  
2. **GO B** — Index Maison  
3. **GO C** — Swarm  
4. **GO D** — Cahier/Hulk filtrés  
5. **GO E** — un seul vault nommé  
6. **GO F** — plugins / Punk path  

Dis juste `GO B` (etc.) — on exécute **une** phase, on vérifie, on s’arrête.
