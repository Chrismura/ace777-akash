# 🔧 REVISION TUYAUTERIE & ARCHITECTURE — 09/08/2026 15:45Z

> Examen complet demandé par Christophe : « examiner la tuyauterie et l'architecture, regarder s'il y a des améliorations pour que le prototype soit solide et stable. »
> Base : hub (~/prise-ia), 28 services launchd, 40 scripts, 3 repos git, sync OUTBOX, garde-fous (gatekeeper/heartbeat/no_solo_code).

---

## 🔴 CRITIQUES — à corriger en priorité (stabilité)

| # | Anomalie | Preuve (vérifiée à l'instant) | Impact |
|---|---|---|---|
| **C1** | **Le superviseur timeout sur le hub : TIMEOUT_HUB = 15 s alors que le hub PATIENCE peut attendre jusqu'à 600 s** | `superviseur_auto.py` ligne 66 : `TIMEOUT_HUB = 15`. À 15:09:40 : « Erreur décision hub (timed out) → défaut : none » | **C'est LE timeout qui reste.** Le fix PATIENCE est côté serveur, mais le client superviseur abandonne après 15 s. Chaque heure, la décision est jetée → le superviseur est aveugle |
| **C2** | **`jauge-energie` ne se lance JAMAIS** : plist sans StartInterval, sans StartCalendarInterval, RunAtLoad=false | Plist complet lu : aucun déclencheur + exit -15 | **La jauge en live demandée depuis des jours n'est pas branchée** — aucun suivi d'énergie |
| **C3** | **`test-freebuff` n'est PAS un repo git** | `git status` → « fatal: not a git repository » | Les coder_*.py, journal_erreurs.md, specs sont **sans sauvegarde** → risque de perte |
| **C4** | **`vigie` en erreur launchd (exit 2)** alors qu'en manuel elle passe (exit 0) | launchctl : `- 2 com.ace777.vigie` ; manuel : exit 0 | La sentinelle sécurité ne tourne pas via launchd → environnement (HOME/PATH) probablement manquant dans le plist |
| **C5** | **`AUTOPILOTE.log` (dans reports/) est VIDE (0 octets)** — le vrai log est dans /tmp | reports/AUTOPILOTE.log = 0 o ; /tmp/autopilote.log tourne (15:40) | Confusion : le rapport officiel est vide → on croit que l'autopilote est mort alors qu'il vit |

---

## 🟠 ROBUSTESSE — à renforcer

| # | Point | Preuve | Suggestion |
|---|---|---|---|
| **R1** | **BrokenPipeError bruyant dans hub.err.log** (client coupe) | Traceback complet dans hub.err.log | Attraper BrokenPipeError dans le Handler → log propre, pas de traceback |
| **R2** | **SYNC_LOG.md = 132 Ko sans rotation** ; hub_events.jsonl = 112 Ko | `ls -la` | Rotation/sanction (ex. garder 7 jours, tronquer au-delà) |
| **R3** | **`qwen-elabore.plist.bak` traîne dans LaunchAgents** | ls LaunchAgents | Déplacer les .bak hors de LaunchAgents (hygiène, éviter toute confusion de chargement) |
| **R4** | **Doublon de modèle** : nvidia ET inferx = `deepseek-v4-flash-0731` | providers.json | Vérifier si redondance voulue (fallback) ou nettoyage |
| **R5** | **3 providers désactivés** (groq, mistral, cloudflare-workers-ai) + grok désactivé | providers.json | Les garder documentés ou les retirer de la liste active |

---

## 🟡 ARCHITECTURE — améliorations proposées (soumission famille)

| # | Proposition | Pourquoi |
|---|---|---|
| **A1** | **Timeout du superviseur aligné sur PATIENCE** : `TIMEOUT_HUB` 15 s → 180 s + modèle décision rapide (gemini-flash-lite) | Le superviseur redeviendra décisionnaire chaque heure au lieu de timeouter |
| **A2** | **Jauge d'énergie branchée** : cadence launchd (ex. toutes les 30 min) + RunAtLoad, sortie dans reports/ et cockpit | La jauge en live demandée depuis le début |
| **A3** | **`test-freebuff` → repo git + push auto** (comme les 2 autres repos) | Sauvegarde des specs/codeurs/specs d'audit |
| **A4** | **Un seul point de vérité des cadences** : 28 plists éparpillés → inventaire `CADENCES.md` régénéré + vérifié par verifier_setup | Plus de « job jamais lancé » découvert par Christophe |
| **A5** | **Healthcheck de bout en bout** : verifier_setup vérifie que CHAQUE service critique a tourné récemment (mtime log < cadence × 3) | Détection automatique des jobs morts |
| **A6** | **Rotation des logs** (SYNC_LOG, hub_events, superviseur) | Fichiers sous contrôle, pas d'usine à gaz |

---

## ✅ DÉJÀ SOLIDE (vérifié, à conserver)

- Hub : **blacklist « mort du jour »** active (tests 5/5, auditée) — plus de timeout visible sur providers morts
- **Gatekeeper** : preuve de lecture < 24 h, bloquant dans verifier_setup
- **Heartbeat 1h** : tourne (heartbeat.json 15:22), pause auto si stagnation
- **Push auto** : 2 repos poussent OK (13:29Z)
- **qwen-elabore** : corrigé 03:00 → 09:15 ✓ ; **qwen-btc** : 09:10 + 21:10 ✓
- **Autopilote** : tourne toutes les 15 min, pulse OK
- **graph-cerveau** 11h, **observatoire** 11h, **verif-setup** 12h : cadences OK
- 13 providers, 9 actifs, budget cloud 480

---

## PROCHAINE ÉTAPE (sur GO Christophe)
Soumettre cette liste (C1-C5, R1-R5, A1-A6) aux familles pour audit + priorisation, puis corriger les critiques C1-C5 en premier.
