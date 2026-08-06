# Automatismes — registre unique

**But :** alléger Cursor / toi. Une seule page = ce qui tourne tout seul, ce qui reste manuel, ce qu’on n’automatise **jamais**.

**Sous l’œil (temps réel) :** [[SOUS_L_OEIL]] — pulse lecture seule.

---

## 3 couches (ne pas mélanger)

| Couche | Rôle | Automatiser ? |
|--------|------|----------------|
| **A — Machine** | RAM, PIDs, heartbeat, LIVE frais, champion | ✅ oui (pulse / checkup) |
| **B — Garage cold** | Journal soir, sync console, Attention, comptes validés | ✅ oui (scripts + launchd) |
| **C — Trading hot** | ACE / Hulk GO, purge, orders | ❌ **jamais** sans GO humain |

---

## A — Machine (sous l’œil)

| Processus | Branché ? | Comment | Notes |
|-----------|-----------|---------|-------|
| **Pulse sous l’œil** | 🟡 à brancher | `scripts/pulse_sous_loeil.sh` | Toutes les **15 min** si launchd chargé |
| Checkup garage (froid) | 🟡 manuel / pré-GO | `scripts/checkup_garage.sh` | Fantômes = NOK avant GO |
| État Mac | 🟡 manuel | `scripts/etat_mac.sh` | Lecture |
| Hygiène RAM | 🟡 manuel | `scripts/hygiene_mac_ram.sh` | Pas de kill ACE |
| **Cockpit indicateurs** | 🟡 hygiène | `scripts/cockpit_hygiene_check.sh` | Thermo + mission feed + pont :17777 · **zone test** |

**Modes pulse :**
- **VOL** = ACE et/ou Hulk détectés → attend heartbeat / LIVE / Ollama si ACE
- **FROID** = rien → attend stérilité (process OFF)

Manuel maintenant :
```bash
bash ~/ace777-test-day1/Index_Maison/scripts/pulse_sous_loeil.sh
open ~/ace777-test-day1/Index_Maison/SOUS_L_OEIL.md   # ou Obsidian après sync
```

Brancher le cron 15 min (une fois) :
```bash
cp ~/ace777-test-day1/Index_Maison/scripts/com.ace777.pulse-sous-loeil.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.ace777.pulse-sous-loeil.plist
```

---

## B — Garage cold (déjà / à garder)

| Processus | Branché ? | Comment |
|-----------|-----------|---------|
| Journal du soir | ✅ | `com.ace777.journal-soir` · 20:53 · `journal_soir_launchd.sh` |
| **Thermo FREE quotidien** | ✅ (avec journal) | `thermo_quotidien_free.py` → [[THERMO_DERNIER]] · 0 € · Binance public |
| Console + journal sync | ✅ script | `journal_auto.py --sync` |
| Mémoire collab ligne | ✅ **AUTO** | `scripts/memoire_log.py` · règle Cursor `memoire-auto.mdc` · session_debut/fin |
| **Molettes journal** | ✅ **AUTO** | `scripts/molette_log.py` · [[JOURNAL_MOLETTES_SETUP]] · pourquoi obligatoire |
| Sync OUTBOX → vault | 🟡 Terminal | `OUTBOX_OBSIDIAN/_sync_now.sh` |
| `speak_attention` | ✅ | `bin/speak_attention` |
| Punk `suivi` / `check` | 🟡 manuel | `--offline` si OOM |
| Compte validé → COMPTES | ✅ règle session | Voir [[PREFS_STACK]] |
| **Session recherche → Index** | ✅ règle Cursor | [[PROTOCOLE_SESSION_RECHERCHE]] · `.cursor/rules/recherche-agora.mdc` — validation = écrire (éval/Attention/OUTBOX) **sans redemander** |
| Agent ACTIF vs PASSIF | ✅ prompts | 1 fenêtre écrit · l’autre ops silencieuse |
| **Ollama Launch ×9** | 🔵 WATCH | Claude / ChatGPT / Hermes / OpenClaw… = **catalogue** · jobs cold futurs · **0** pendant ACE · schéma [[ARCHITECTURE_AGORA]] |
| **Anti-éparpillement** | ✅ loi | [[OSSATURE_INDEX]] — 1 place / info · éditer canon avant nouveau fichier |
| **Cockpit UI Arcade** | 🟡 **ZONE TEST** | [[COCKPIT_LOOK_FIGE]] · `cockpit/index.html` · check hygiène · [[2026-07-30_cockpit_zone_test]] |
| **Validation test → réel** | ✅ doctrine | [[PROTOCOLE_VALIDATION_TEST_AVANT_REEL]] · [[JOURNAL_ERREURS_TEST]] · go-no-go humain |
| **Début / fin session** | ✅ scripts | `session_debut.sh` / `session_fin.sh` · [[PROTOCOLE_SESSION_DEBUT_FIN]] |
| **Cockpit app fenêtre** | ✅ | `open_cockpit_app.sh` · pywebview ou Brave `--app` · [[JOURNAL_COCKPIT]] |


---

## C — Trading (GO humain seulement)

| Processus | Branché ? | Notes |
|-----------|-----------|-------|
| ACE `GO_USINE_NUAGE.sh` | ❌ sans GO | Champion intact |
| Hulk `paper_diprip.py` | ❌ sans GO | Terminal séparé |
| Watchdogs ACE/Hulk | avec le run | Pas de cron fantôme |
| Ollama | avec ACE / veille | Pas de cron LLM 6 h sur 8 Go |

---

## Ne jamais automatiser

- GO trading, purge process, force-stop pendant un vol
- Ajout compte sur un titre seul (`LU_PARTIEL`)
- Cron multi-LLM / herdr / Meridian pendant ACE
- Relance ACE/Hulk « parce que le pulse a WARN »

---

## Prompt agent (ne plus réécrire)

Pour un **nouvel agent cold** : coller le brief « État machine + Interdits » (fichier chat ops) + lire `SOUS_L_OEIL.md` + `BRIEF_IA_SNIFF.md`.

Pour **moi (ops)** : « check » = lire `SOUS_L_OEIL` + confirmer PIDs — pas de roman.

---

## État snapshot (MAJ manuelle après gros changement)

| Date | Note |
|------|------|
| 2026-07-30 | Cockpit ZONE TEST · S26 · journals · demain = pywebview + session début/fin |
| 2026-07-30 | Cockpit prototype → **zone test** · hygiène indicateurs obligatoire |
| 2026-07-29 | Pulse créé · journal soir déjà ON · ACE+Hulk session matin (vol) |
