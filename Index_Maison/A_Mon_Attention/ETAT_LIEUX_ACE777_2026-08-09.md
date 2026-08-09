# 📋 ÉTAT DES LIEUX ACE777 — 2026-08-09 (extrait mécaniquement, pas de mémoire)

> **Méthode :** faits lus dans les vrais fichiers (launchctl, plists, routing.json, providers.json,
> mission.json, cortana_feed.json, scripts) — pas de souvenirs, pas de prose interprétée.
> **Usage :** référence factuelle pour toute décision d'architecture. Généré par collecte directe.

---

## 1. COUCHE SYSTÈME (ce qui tourne)

### Les 29 services launchd (noms réels)
```
autopilote · superviseur · heartbeat · prise-ia (hub) · veille-hub · catalogue
eval-offres · propose-ameliorations · observatoire · surveillance-quotas
analyste-cadence · analyse-usage · verif-setup · rotation-logs · gitpush · gitpush-vault
cockpit-http · cockpit-pont · graph-cerveau · cortana.horaire · cortana.urgent
journal-soir · brief-matin · pulse-sous-loeil · vigie · qwen-btc · qwen-elabore
mirofish · mirofish-front
```

### Le hub (cerveau central, port 11435)
- État : **OK** · 9 providers actifs
- **17 tâches routées** :
  - `supervise.decision` → **puter-grok** (grok-4.3) · fallback gemini ← **le superviseur décide ICI** (décroché de qwen 09/08)
  - `ada.sanity` (démarrage) → qwen-local (secours offline)
  - `cortana.brief` / `cortana.analyse` / `audit.protocol` / `coffre.ask` → gemini · fb qwen-local
  - `qwen.elabore` / `qwen.btc` / `signets.synthese` / `chat.local` → qwen-local (élève + léger)
  - `signets.lot2` → openrouter-free · `analyse.profonde` / `mission` → nvidia · `signets.juge` → openrouter-juge · `ultra.analyse` → openrouter-ultra · `inferx.analyse` → inferx · `code.ia` → inferx-coder
- **Auto-réparation : OUI** (KeepAlive + RunAtLoad, testé « relancé en 2 s »)

### Les 9 providers actifs
qwen-local (qwen3.5:4b) · gemini-flash-lite · openrouter-free (gpt-oss-20b) · nvidia (deepseek-v4-flash) · openrouter-juge (nemotron-120b) · openrouter-ultra (nemotron-550b) · inferx (deepseek) · inferx-coder (Qwen3-Coder) · **puter-grok (grok-4.3)**

### Qwen — rôle réel (5 tâches, aucune critique)
`ada.sanity` (démarrage) · `signets.synthese` · `chat.local` · `qwen.elabore` · `qwen.btc`
→ **Élève (professeur la note) + secours hors-ligne + tâches légères.**

### Protections mécaniques en place
WORM journal (append-only) · gardien.py (double signature) · gatekeeper.py · heartbeat.py · verifier_setup.py

### Chiffres
114 scripts · 33 scripts s'appellent entre eux (26 connexions uniques) · 13 scripts de surveillance · repo 268 Mo · vault 35 Mo · hub 880 Ko

---

## 2. COUCHE TRADING (ce qui produit — mission.json, temps réel)

| Indicateur | Valeur (21:05Z) | Lecture |
|---|---|---|
| Run en cours | `NUAGE_TEST_8H_CMP3` | test actif |
| PnL combiné | **-8,54** | ↓ léger |
| Alerte | amber | surveillance |
| Cycle swarm | 585 | compteur actif |
| ALPHA | actif (fichier `_ALPHA_X13_BURST13.csv`) · **4 fills** | moteur α |
| BETA | actif (fichier `_BETA_X5.csv`) · **33 fills** | moteur β |
| HULK | `file: null` · 0 bags · 0.0 | à l'arrêt |
| THERMO | climate `ok` · **score 88** · direction up | indice température |
| Analyses enregistrées | `thermo/analyses/YYYY-MM-DD.jsonl` (Qwen + master, notés par le professeur) | |

### Connexions du graphe synapses (cockpit)
cockpit ↔ pont ↔ ace ↔ live ↔ α ↔ β ↔ hulk ↔ net ↔ binance ↔ cortana ↔ thermo — badges ON/SLOW/OFF

---

## 3. COUCHE VOCALE (CORTANA — ce qui parle)

- **Voix : Vivienne** (edge-tts neuronal « suave ») · repli macOS say
- **Services** : `cortana.horaire` (rituel horaire) + `cortana.urgent` (urgences)
- **Scripts** : voice · brief · analyse · thermo · horaire · urgent_poll · watch · mute · cockpit_bridge
- **Dernier résumé** (20:51Z) : « Climat calme, score 88… Bitcoin 65 108 $, -0,07 % sur 1h »
- **Alertes 09/08** : 10 · **Mute : NON**
- **Feed** : `thermo/cortana_feed.json` (mémoire mécanique de la couche vocale)

---

## 4. LA DÉCOUVERTE (pourquoi cette fiche existe)

**Chaque couche a déjà SA mémoire mécanique — sauf la couche système :**

| Couche | Mémoire mécanique | Statut |
|---|---|---|
| Trading | `mission.json` (temps réel) | ✅ déjà là |
| Vocal | `cortana_feed.json` (temps réel) | ✅ déjà là |
| Système | ~~prose éparpillée~~ → **à créer : `state.json`** | ⬜ LE chantier |

**Conclusion :** le système est déjà à 2/3 du chemin de la mémoire mécanique sans que
personne ne l'ait vu. Le chantier qui reste : un `state.json` de la couche système,
généré par la machine (mêmes données que cette fiche), consulté par l'IA au lieu de
relire la prose. C'est la sortie de la boucle infernale (voir conversation 09/08).

---

---

## 5. MISE À JOUR 10/08 00:20 — CORRECTIONS + ÉTAT RÉEL (nouvelle collecte mécanique)

### ⚠️ Correction 1 : Mirofish est un MEMBRE DE L'ÉQUIPE, PAS un bot de trading
- **Vraie nature** (fiche `FICHE-MIROFISH.md`) : simulation sociale multi-agents (recherche-grade),
  monde numérique + foule d'agents IA + rapport de prédiction. **Jamais d'exécution** (doctrine).
- Installé 08/08 · testé avec Christophe le 09/08 matin.
- État : **TOURNE** (backend `com.ace777.mirofish` port 5001 + front `com.ace777.mirofish-front` port 3000).
- ⚠️ **Budget** : consomme des tokens via le hub → NVIDIA NIM (deepseek-v4-flash).
  Christophe pensait l'avoir arrêté pour ne pas claquer le budget — **à trancher : le laisser ou l'arrêter**
  (`launchctl stop com.ace777.mirofish` + `com.ace777.mirofish-front`).

### 🔍 Correction 2 : PAS de bot fantôme — mission.json est le feed du cockpit
- Écrit par `cockpit_mission_feed.py` (ligne 450) — **feed légitime**, pas un job fantôme.
- Le run `NUAGE_TEST_8H_CMP3` affiché = **dernier run connu (historique)**, pas un run actif.
- Preuve : 2 lectures à 6 s d'intervalle le 10/08 00:18 → **md5 identique, timestamp identique** (00:18:11).

### ✅ État réel vérifié le 10/08 00:18
| Élément | État |
|---|---|
| Bots alpha/beta/hulk | ✅ **ARRÊTÉS** (autopilote `PULSE=NOK mode=FROID ace=0 hulk=0`) |
| hub (11435) | ✅ vivant (PID 47505) — 9 providers |
| cockpit-http + cockpit-pont | ✅ vivants (PIDs 652, 672) |
| mirofish + front | ✅ vivants (PIDs 664, 653) — à trancher (budget) |
| RAM | 73 % libre (8 Go) — aucun risque OOM |
| Plus gros conso RAM | freebuff/Buffy 2,5 Go (session en cours) |

*Généré le 09/08/2026 · MIS À JOUR le 10/08 00:20 · source : collecte mécanique directe*
