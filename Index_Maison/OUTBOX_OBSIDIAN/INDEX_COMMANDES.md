# Index des commandes Terminal

> 🚀 **COMMENCE ICI — POINT DE REPRISE** : `Index_Maison/POINT_REPRISE_DERNIER.md`
> (30 s de lecture : ce qui tourne, ce qui reste, les commandes clés)

**Où :** `~/ace777-test-day1/Index_Maison/INDEX_COMMANDES.md`  
**Miroir Obsidian :** après sync → même nom dans le coffre `Obsidian_ACE777`  
**Sync :**
```bash
bash ~/ace777-test-day1/Index_Maison/OUTBOX_OBSIDIAN/_sync_now.sh
```
Copie les notes (dont cet index) du dossier OUTBOX vers ton coffre Obsidian.

---

## Règle d’or
Ne lance **jamais** ACE ni Hulk sans avoir dit **GO** et sans Mac froid.  
**Test avant réel :** [[PROTOCOLE_VALIDATION_TEST_AVANT_REEL]] · bugs → [[JOURNAL_ERREURS_TEST]].

## 0 — Porte test (avant run lecture / GO)
```bash
cd ~/ace777-test-day1 && ./scripts/verif_sterilite.sh --pre-run
bash ~/ace777-test-day1/Index_Maison/scripts/cockpit_hygiene_check.sh
```
Porte 0 (stérile) + Porte 1 (indicateurs cockpit). Anomalie → une ligne dans `JOURNAL_ERREURS_TEST.md`.

---

## 1 — Coupure / remise en route

```bash
bash ~/ace777-test-day1/Index_Maison/OUTBOX_OBSIDIAN/_sync_now.sh
```
Remet à jour Obsidian avec les notes préparées (console, journal, attention, cet index).

```bash
pgrep -lf 'GO_USINE|paper_diprip|ollama serve' || echo "OK rien qui tourne"
```
Vérifie qu’aucun bot (ACE / Hulk / Ollama) ne tourne en cachette. Si tu vois « OK rien qui tourne », c’est bon.

---

## 2 — État du Mac

```bash
bash ~/ace777-test-day1/Index_Maison/scripts/pulse_sous_loeil.sh
```
**Sous l’œil** — checklist vert/jaune/rouge (ACE/Hulk/Ollama/RAM/heartbeat). Écrit `Index_Maison/SOUS_L_OEIL.md`. Lecture seule. Registre : `AUTO_PROCESSUS.md`.

```bash
bash ~/ace777-test-day1/Index_Maison/scripts/etat_mac.sh
```
Affiche l’heure, la charge CPU, la RAM libre, les gros processus, le disque, et si des bots tournent. Lecture seule — ne change rien.

```bash
bash ~/ace777-test-day1/scripts/hygiene_mac_ram.sh --check
```
Regarde seulement les processus WebKit orphelins qui mangent la RAM (ne les tue pas).

```bash
bash ~/ace777-test-day1/scripts/hygiene_mac_ram.sh
```
Nettoie les WebKit orphelins lourds/vieux. Ne touche pas Cursor ni ACE.

---

## 3 — Grosse hygiène

```bash
bash ~/ace777-test-day1/Index_Maison/scripts/grosse_hygiene.sh
```
Ménage complet à froid : état Mac → RAM → ménage ACE après arrêt → journal/console → **cockpit indicateurs** → sync Obsidian. **Ne lance pas** le trading.

```bash
bash ~/ace777-test-day1/Index_Maison/scripts/cockpit_hygiene_check.sh
```
Hygiène **cockpit** (zone test) : refresh thermo free + mission feed + check pont `:17777` + indicateurs clés (funding/OI/F&G/score).

```bash
bash ~/ace777-test-day1/Index_Maison/scripts/checkup_garage.sh
```
Checkup fantômes PID + stérilité + RAM → écrit `Index_Maison/CHECKUP_DERNIER.md`. Réf. protocole stérilité / rapports fantômes.

```bash
cd ~/ace777-test-day1 && ./scripts/hygiene_apres_arret.sh --kill-orphans
```
Hygiène ACE seule : rapport d’arrêt + tue les orphelins (timers, caffeinate, etc.).

```bash
cd ~/ace777-test-day1 && ./scripts/verif_sterilite.sh
```
Vérifie que la machine est « propre » avant un éventuel run ACE (à faire avant GO, pas à la place du GO).

---

## 4 — Runs ACE (date & plus-value)

```bash
python3 ~/ace777-test-day1/Index_Maison/scripts/liste_runs.py
```
Liste les runs ACE **par date** (du plus récent au plus vieux) avec Alpha / Beta / combo $.

```bash
python3 ~/ace777-test-day1/Index_Maison/scripts/liste_runs.py --pnl
```
Liste les runs ACE **par plus-value** (du meilleur combo $ au pire).

```bash
python3 ~/ace777-test-day1/Index_Maison/scripts/liste_runs.py --pnl --top 5 --cmd
```
Top 5 meilleurs runs + **affiche** la commande de lancement à coller. N’exécute rien.

```bash
python3 ~/ace777-test-day1/Index_Maison/scripts/liste_runs.py --tag NUAGE_TEST_8H_CMP
```
Filtre un run précis par son nom (TAG).

---

## 5 — Console & journal

```bash
python3 ~/ace777-test-day1/Index_Maison/scripts/journal_auto.py
```
Met à jour la console générale + le journal du jour (dans Index_Maison).

```bash
python3 ~/ace777-test-day1/Index_Maison/scripts/journal_auto.py --sync
```
Pareil + essaie de copier vers Obsidian (si le Mac autorise Documents).

```bash
bash ~/ace777-test-day1/Index_Maison/scripts/journal_du_soir.sh
```
Script « journal du soir » (même idée, version bash). Cron déjà à **20:53**.

---

## 5a0 — Mémoire collab (AUTO — tous)

```bash
# 1 ligne après chaque intervention (Cursor le fait aussi via règle)
python3 ~/ace777-test-day1/Index_Maison/scripts/memoire_log.py Humain "★" "où" "quoi en une ligne"

# Changement molette / setup (+ pourquoi)
python3 ~/ace777-test-day1/Index_Maison/scripts/molette_log.py \
  --molette NUAGE_STORM_HUNTER --avant 0 --apres 1 \
  --pourquoi "…" --qui Humain
```

Réf : [[MEMOIRE_COLLAB]] · [[JOURNAL_MOLETTES_SETUP]] · [[COUTUMES_AGORA]]

## 5a — Début / fin de session

**Matin (ou après nuit en vol) :**
```bash
bash ~/ace777-test-day1/Index_Maison/scripts/session_debut.sh --open
bash ~/ace777-test-day1/Index_Maison/scripts/session_debut.sh --vol --open   # force VOL
```

**Avant dodo — prototype qui reste :**
```bash
bash ~/ace777-test-day1/Index_Maison/scripts/session_fin.sh                  # ne tue PAS ACE
bash ~/ace777-test-day1/Index_Maison/OUTBOX_OBSIDIAN/_sync_now.sh
```

Stop explicite seulement : `session_fin.sh --stop-ace`.  
Canon : [[PROTOCOLE_SESSION_DEBUT_FIN]] · backlog finition : [[CHOSES_A_FINIR_REVOIR]].

## 5b — Cockpit ACE777 (ZONE TEST · app native)

**Statut :** stack validée 31 juil. — LaunchAgents + pywebview 1er · Brave `--app` filet.  
Canon : `COCKPIT_LOOK_FIGE.md` · `JOURNAL_COCKPIT.md` · `COCKPIT_LANCEMENT.md`.  
Onglets : OPS · THERMO · BOARD · **GRAPH** (synapses) · VOL


```bash
# Quotidien (daemons + fenêtre native)
bash ~/ace777-test-day1/Index_Maison/scripts/cockpit_up.sh

# Fenêtre seule (si PONT/HTTP déjà ON)
bash ~/ace777-test-day1/Index_Maison/scripts/open_cockpit_app.sh

# Daemons seulement / réparation
bash ~/ace777-test-day1/Index_Maison/scripts/install_cockpit_daemons.sh
bash ~/ace777-test-day1/Index_Maison/scripts/cockpit_up.sh --daemons
```
Recharger page = **⌘R** (F5 = dictation micro). Pas Safari.

```bash
bash ~/ace777-test-day1/Index_Maison/scripts/cockpit_hygiene_check.sh
```

## 5b2 — Thermo Index (board A/B/C live free)

```bash
python3 ~/ace777-test-day1/Index_Maison/scripts/thermo_quotidien_free.py
open ~/ace777-test-day1/Index_Maison/thermo/index.html
```
Thermomètre Index complet (A1–A6 · B7–B12 · C13–C25) + ticker Binance **sans clé**.  
Rafraîchir = relancer le script puis bouton RAFRAÎCHIR (ou recharger la page). Lecture seule — pas de GO.


## 5b3 — Cortana × Thermo (questions + voix)

```bash
python3 ~/ace777-test-day1/Index_Maison/scripts/thermo_quotidien_free.py
python3 ~/ace777-test-day1/Index_Maison/scripts/cortana_thermo.py ask funding
python3 ~/ace777-test-day1/Index_Maison/scripts/cortana_thermo.py ask mois
python3 ~/ace777-test-day1/Index_Maison/scripts/cortana_thermo.py ask mois-dernier
python3 ~/ace777-test-day1/Index_Maison/scripts/cortana_thermo.py ask climat
python3 ~/ace777-test-day1/Index_Maison/scripts/cortana_thermo.py surveille
python3 ~/ace777-test-day1/Index_Maison/scripts/cortana_thermo.py resume          # indices + avis sentiment
python3 ~/ace777-test-day1/Index_Maison/scripts/cortana_thermo.py resume --say   # + voix
python3 ~/ace777-test-day1/Index_Maison/scripts/cortana_thermo.py speak --say

# Résumé horaire auto (launchd) — une fois :
# cp …/com.ace777.cortana.horaire.plist ~/Library/LaunchAgents/
# launchctl load ~/Library/LaunchAgents/com.ace777.cortana.horaire.plist
# Test : ~/ace777-test-day1/Index_Maison/scripts/cortana_horaire.sh
# Mute voix : CORTANA_HORAIRE_SAY=0 …/cortana_horaire.sh

# P3 URGENT (immédiat, pas attendre l'heure)
python3 ~/ace777-test-day1/Index_Maison/scripts/cortana_thermo.py alert "Test alerte"
# poll launchd 10s : com.ace777.cortana.urgent
# C7 défaut 8% : source Index_Maison/config_risk_warm.env · [[RISK_C7]]

# AGENT ON AIR (pastille dashboard)
python3 ~/ace777-test-day1/Index_Maison/scripts/agent_status.py heartbeat
python3 ~/ace777-test-day1/Index_Maison/scripts/agent_status.py set KIMI ON_AIR
open ~/ace777-test-day1/Index_Maison/architecture/index.html
```
Nourrit `ATTENTION_VOCALE` + volet sniff du **cockpit** (`cortana_feed.js`). Lecture seule.

## 5c — Architecture (carte visuelle + TECH)

```bash
open ~/ace777-test-day1/Index_Maison/architecture/index.html
open ~/ace777-test-day1/Index_Maison/architecture/tech.html
```
- **VUE** = carte humaine (HOT / COLD / voix / coffre)  
- **TECH** = spec pour revue IA (contraintes, entrypoints, rubrique)  
Canon : `ARCHITECTURE_AGORA.md` · `architecture/ARCHITECTURE_TECH.md` · `OSSATURE_INDEX.md`.  
**Pas** un bot — lecture visuelle. Données réelles = GO build data plus tard.

---

## 5c — Research Desk (backtest labo)

```bash
cd ~/ace777-test-day1/labo/Backtesting-Engine && npm install && npm run dev
```
Backtest local (Binance public). **Mac froid** — pas pendant ACE. Canon : [[HISTO_RESEARCH_DESK]].

---

## 6 — Veille Punk (info, pas trading)

```bash
cd ~/ace777-test-day1/veille-punk && source obsidian.env
```
Se place dans Punk et pointe vers le bon coffre Obsidian.

```bash
cd ~/ace777-test-day1/veille-punk && ./bin/suivi "@Compte colle le texte du post"
```
Filtre un post vs le tableau Index → note « À mon attention » + résumé vocal si pertinent.

```bash
cd ~/ace777-test-day1/veille-punk && ./bin/suivi --offline "@Compte colle le texte du post"
```
Même chose **sans** Ollama (secours si Mac chaud / RAM faible).

```bash
cd ~/ace777-test-day1/veille-punk && ./bin/speak_attention
```
Lit à voix haute le dernier résumé d’attention (proxy Cortana).

```bash
cd ~/ace777-test-day1/veille-punk && ./bin/check "colle url ou texte"
```
Bullshit check classique (vrai / semi / bullshit) — veille froide.

---

## 7 — Trading (DANGER — GO obligatoire)

```bash
cd ~/ace777-test-day1 && caffeinate -dims ./GO_USINE_NUAGE.sh 08:00:00 MON_TAG
```
Lance ACE testnet pour une durée + un TAG. **Uniquement** si tu as dit GO et que le Mac est froid. Remplace `MON_TAG` (ex. `NUAGE_TEST_8H_CMP`).

**GATE HUB (depuis 12/08 — la bascule officielle) :**

```bash
cd ~/ace777-test-day1 && caffeinate -dims ./GO_VORTEX_V2.sh 04:00:00
```
Lance ACE testnet **avec le juge hub** (grok → gemini) — c'est LE lanceur à utiliser maintenant, pas GO_USINE (qui a le gate OFF). Profil `vortex_v2_collab.env`. Vérifier après boot : `tail -5 runs/supervisor_v9_v2.log` doit afficher `LLM llm_wind` (pas `EMRG`).

```bash
cd ~/ace777-test-day1 && ./ENCHAINER_RUN_4H_HUB.sh
```
Enchaîneur auto : attend la fin du run en cours puis lance GO_VORTEX_V2 4h. Déjà exécuté le 12/08 (preuve 30 min → run 4h de comparaison).

```bash
curl -s http://127.0.0.1:11439/api/tags
```
Check du pont hub (il émule Ollama pour le moteur). Le service `com.ace777.llm-gate-hub` (launchd, KeepAlive) l'auto-relance s'il meurt.

```bash
# Régler la cadence du juge hub (cache du pont)
export LLM_GATE_PONT_CACHE_SEC=90   # 90s = défaut | 30s = plus réactif | 300s = plus économe
# Budget du juge (délai max avant repli règles)
export VORTEX_LLM_BUDGET_SEC=20
```
Variables dans `config_active.env` — effet au prochain run (figées au lancement).

```bash
cd ~/ace777-test-day1 && ./stop_ace777_hard.sh
```
Arrêt ACE forcé (si le soft ne suffit pas).

Arrêt complet du système (ACE + 3 étages + vérif + redémarrage) : **voir §10**.

Hulk paper : pas de commande « magique » ici — dis **GO Hulk** à Cursor (7 positions encore gelées).

---

## 8 — Où lire dans Obsidian

Ouvre le vault **Obsidian_ACE777** → note **AGORA** → **CONSOLE_GENERALE**.  
Cette fiche : **INDEX_COMMANDES**.  
Après coupure : **REPRISE_APRES_COUPURE**.

---

## 9 — Session Buffy (chef d'orchestre · Prise IA · veille)

**But :** tout relancer en 30 s pour qu'on se retrouve (Buffy lit le journal + la mémoire + sa spec [[BUFFY]]).

**1) Check que tout tourne :**
```bash
launchctl list | grep prise-ia
curl -s http://127.0.0.1:11435/health
ollama list | head -5
cd ~/Documents/Obsidian_ACE777 && git pull --rebase && git status --short | head -3
```

**2) Si le hub Prise IA est mort (relance auto via launchd, sinon) :**
```bash
launchctl unload ~/Library/LaunchAgents/com.ace777.prise-ia.plist 2>/dev/null
launchctl load   ~/Library/LaunchAgents/com.ace777.prise-ia.plist
sleep 2 && curl -s http://127.0.0.1:11435/health
```

**3) Test rapide de la tuyauterie (Qwen locale via le hub) :**
```bash
curl -s http://127.0.0.1:11435/v1/chat/completions -H 'Content-Type: application/json' -d '{"messages":[{"role":"user","content":"dis bonjour en 3 mots"}],"max_tokens":30}' | head -c 300
```

**4) Signets X — pipeline (bookmarks → notes Obsidian) :**
```bash
ls -lat ~/Downloads/ | grep -i twitter | head -3   # un nouvel export JSON ?
python3 ~/process_x_bookmarks_master.py            # conversion → Signets_X/
```
> À faire (Buffy + Christophe) : trouver un moyen RAPIDE de télécharger les bookmarks X.

**5) MA commande de lancement (Ada) — tout en un :**
```bash
ada
```
> L'alias `ada` lance `scripts/ada.command` : elle vérifie/relance le hub → teste Qwen → git pull → régénère mon fichier de réveil → affiche ma prochaine action → **lance Freebuff en mode `--continue`**. Ensuite tu écris « on reprend » et je suis là. 🎼
> Sans l'alias : `bash ~/Documents/Obsidian_ACE777/scripts/ada.command` (ou double-clic sur le fichier dans le Finder).

**6) Fin de session (génère mon fichier de réveil + sauvegarde) :**
```bash
python3 ~/Documents/Obsidian_ACE777/scripts/buffy_reveil.py
cd ~/Documents/Obsidian_ACE777 && git add -A && git commit -m "fin de session" && git push
```

---

## Rappel 10 secondes

| Besoin | Quoi coller |
|--------|-------------|
| Mac OK ? | `etat_mac.sh` |
| Ménage | `grosse_hygiene.sh` |
| Qui a gagné $ ? | `liste_runs.py --pnl --cmd` |
| Sync notes | `_sync_now.sh` |
| **Cockpit UI** | `open …/cockpit/index.html` |
| **Test→réel** | notes `PROTOCOLE_VALIDATION_TEST_AVANT_REEL` + `JOURNAL_ERREURS_TEST` |
| **Architecture carte** | note Obsidian `DASHBOARD_ARCHITECTURE` · ou `open …/architecture/index.html` |
| Lire un post | `suivi "…"` |
| Voix | `speak_attention` |
| Trader | seulement avec GO |
| Session Buffy | §9 — check hub + ollama + git |

## 10 — Démarrage / Arrêt (les 2 commandes essentielles)

**🚀 DÉMARRAGE — la commande du matin :**
```bash
bash ~/ace777-test-day1/Index_Maison/scripts/session_debut.sh --open
```
> **Ce que c'est** : la checklist complète de démarrage — vérifie l'état du Mac (RAM/CPU), lance le boot unique, vérifie cockpit/thermo/pont, affiche le plan de vol. **Ne lance JAMAIS le trading.** Options : `--open` (ouvre le cockpit) · `--vol` (lecture seule pendant run) · `--froid` (checks pré-run).

**🛑 ARRÊT — l'arrêt complet du système :**
```bash
cd ~/ace777-test-day1 && ./stop_ace777.sh
```
> **Ce que c'est** : arrête les 4 services 3 étages (watchdog EN PREMIER, sinon il relance tout → superviseur-core → cockpit-pont → cockpit-http) + tous les anciens processus (vortex, genesis, master...). À lancer dans un **nouveau terminal**.

**Vérifier que tout est éteint :**
```bash
launchctl list | grep -E 'superviseur-core|watchdog|cockpit-pont|cockpit-http'   # → rien
pgrep -f 'superviseur_core\.sh'                                                  # → rien
```

**Redémarrer SANS reboot (après un arrêt) :**
```bash
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.ace777.superviseur-core.plist
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.ace777.watchdog.plist
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.ace777.cockpit-pont.plist
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.ace777.cockpit-http.plist
```
> Après REBOOT : les services reviennent tout seuls au login. Doc détaillée : `ERREURS_AI/COMMANDES_ARRET_ACE777.md`.

---

## 11 — RUN DE TEST 16/08 : FIX-LAST-LOSS (TTL revenge 120s)

**🚀 Commande de test (datée 16/08) :**
```bash
cd ~/ace777-test-day1 && ./GO_VORTEX_V2.sh 02:00:00
```
> **Quoi** : run de validation du champion re-scellé `3d760592` (FIX-LAST-LOSS — le TTL revenge se base sur `last_loss_ts` au lieu de figer `ts_ms`). Le run de nuit du 15/08 (fix du 15/08) avait **0 revenge et +0.28 USDT** ; ce fix doit restaurer les revenge (cible 30–60% des fills ALPHA) et le PnL (+2 à +11 attendu).
> **Durée** : `02:00:00` = test rapide · `./GO_VORTEX_V2.sh` (sans arg) = 4h comme d'habitude · run complet : `./GO_VORTEX_V2.sh 04:00:00`.
> **Après le run** : lire `runs/RAPPORT_PNL_AUTO_*.md` (le plus récent) + `engle/journal/ENGLE_JOURNAL_DERNIER.md`. Critères : %revenge 30–60%, `revenge_ttl_expired` présent (nouvelle raison de skip duo), `stale_state` ≈ 0, PnL total > +1 USDT.
> **Doc** : `Index_Maison/CHANTIER_FIX_LAST_LOSS_TTL_2026-08-16.md` · `Index_Maison/ANALYSE_RUNS_2026-08-16.md` · Rollback : voir chantier (backup `BAK_avant_fix_last_loss_ttl_20260816`).

---

## 🔗 Connexions

- [[14_AUDIT_TROIS_JAMBES_SWARM]] — 14_AUDIT_TROIS_JAMBES_SWARM
- [[AUTO_PROCESSUS]] — AUTO_PROCESSUS
- [[REVEIL_BUFFY]] — REVEIL_BUFFY
- [[CONTRAT_AUTOGESTION]] — CONTRAT_AUTOGESTION
