# 🗺️ FUSION_MAP — LA CARTE DE LA FUSION (10/08/2026)

> Écrite AVANT de casser quoi que ce soit (règle codeur + consultation famille : « on ne relit
> jamais le code pendant la fusion »). Objectif : zéro oubli de fonctionnalité.

## 🎯 Architecture cible

```
AVANT (6 services de supervision + monitoring)          APRÈS (2)
─────────────────────────────────────────────           ─────────────────────────
com.ace777.superviseur        (1 h, cerveau grok)   →   com.ace777.superviseur      (1 h, INCHANGÉ)
com.ace777.heartbeat          (1 h)                 ─┐
com.ace777.pulse-sous-loeil   (15 min)              ─┤→   com.ace777.superviseur-core (15 min)
com.ace777.vigie              (30 min)              ─┤      superviseur_core.sh
com.ace777.surveillance-quotas(30 min)              ─┤      (cadences internes par timestamp)
com.ace777.rotation-logs      (6 h)                 ─┘
```

**Règle d'or (codeur + famille)** : superviseur_core **LIT state.json, ne l'écrit JAMAIS**
(le state-generator est le SEUL écrivain) · KeepAlive · intervalle 900 s (> 120 s).

---

## 📋 Ce que chaque service fait — et ce que superviseur_core doit ABSORBER

| # | Service (plist) | Cadence | Ce qu'il fait (vérifié, pas de mémoire) | Absorbé par core ? |
|---|---|---|---|---|
| 1 | `com.ace777.heartbeat` | 1 h | Vérifie hub /health (6 s), RAM, git ; écrit `~/prise-ia/heartbeat.json` ; alerte HEARTBEAT_ALERT.md + fichier PAUSE si anomalie | ✅ **OUI** (cadence 1 h interne) |
| 2 | `com.ace777.pulse-sous-loeil` | 15 min | Lecture seule « machine OK ? » : mode vol/froid, process ACE/Hulk/Ollama, RAM, champion md5, heartbeat age ; écrit `SOUS_L_OEIL.md` (+ miroirs OUTBOX) | ✅ **OUI** (cadence 15 min = celle du core) |
| 3 | `com.ace777.vigie` | 30 min | Sentinelle sécurité : chmod 600 secrets trop ouverts (seul auto-fix), détection nouvelle persistance, ports non-loopback, intégrité fichiers clés (baseline sha256), secrets dans git, FileVault/pare-feu/womp, hub exposé ; état `~/.vigie/` | ✅ **OUI** (cadence 30 min interne) |
| 4 | `com.ace777.surveillance-quotas` | 30 min | Lit `usage.jsonl` + `providers.json` ; vérifie quotas/jour vs cloud_daily_budget ; écrit rapport `reports/SURVEILLANCE_QUOTAS.log` | ✅ **OUI** (cadence 30 min interne) |
| 5 | `com.ace777.rotation-logs` | 6 h | Rotation COPYTRUNCATE des logs > 500 Ko (usage.jsonl, hub_events, reports/*.log, SUPERVISEUR.log), 3 backups, log ROTATION.log | ✅ **OUI** (cadence 6 h interne) |
| 6 | `com.ace777.superviseur` | 1 h | **LE CERVEAU** : lit state/coffre → état → décision via hub `supervise.decision` (grok-4.3, fallback gemini) → agit (escalades, rappels lecture) | ❌ **INCHANGÉ** (reste tel quel) |

---

## 🔢 Ordre de la fusion (à respecter STRICTEMENT)

1. **Écrire** `superviseur_core.sh` (délégué au codeur du hub, task `code.ia`)
2. **TESTER manuellement** superviseur_core.sh SEUL (run réel) → doit produire :
   - `SOUS_L_OEIL.md` (frais, 15 min)
   - `~/prise-ia/heartbeat.json` (frais, 1 h interne)
   - rapport vigie `~/.vigie/SECURITE_VIGIE.md` (30 min interne)
   - `reports/SURVEILLANCE_QUOTAS.log` (30 min interne)
   - `reports/ROTATION.log` (6 h interne)
3. **Comparer** la sortie avec les 5 scripts originaux → même comportement
4. **Charger** le plist `com.ace777.superviseur-core` (StartInterval 900, KeepAlive)
5. **Désactiver** (unload + plist → `DESACTIVES_2026-08-10/`) dans l'ordre : heartbeat → pulse → vigie → quotas → rotation
6. **Vérifier** que le core produit TOUJOURS les 5 sorties après désactivation (non-régression)
7. **Audit famille diff** (loi 1quinquies) → GO → push

---

## ⚠️ Points de vigilance (lus dans le code)

- **vigie.sh** : `exit 2` si alertes actives — ne pas interpréter comme échec ; état persisté `~/.vigie/state.txt` (n'alerte qu'au changement)
- **heartbeat.py** : peut créer `PAUSE_ORCHESTRATRICE` (pause auto) + HEARTBEAT_ALERT.md — comportement à conserver à l'identique
- **pulse_sous_loeil.sh** : écrit 3 rapports (racine + 2 miroirs OUTBOX) — tous les 3 requis
- **rotation_logs.py** : rotation copy+truncate (jamais de suppression du fichier live) — le hub n'est JAMAIS touché
- **superviseur_auto.py** : lit la liste des 14 jobs launchd attendus (ligne 61-62) — **à METTRE À JOUR** quand on désactive les 5 plists, sinon il alertera « job manquant » (⚠️ voir note superviseur_auto.py `JOBS_ATTENDUS`)

---

## 🧪 Critères de non-régression (après désactivation)

| Check | Attendu |
|---|---|
| Hub `/health` | `{"status":"ok","providers":9}` |
| SOUS_L_OEIL.md mtime | < 20 min |
| heartbeat.json mtime | < 70 min |
| SECURITE_VIGIE.md présent | oui |
| SURVEILLANCE_QUOTAS.log présent | oui |
| ROTATION.log présent | oui |
| Aucun des 5 plists chargé | launchctl list vide pour ces labels |
| superviseur (cerveau) vivant | launchctl list |

---

## 📌 Décision famille (source)
`FUSION_CONSULTATION_2026-08-10/` — unanime : améliorer d'abord → Action 2 = créer la
colonne vertébrale AVANT de casser. Pause Qwen déjà faite (10/08) → terrain nettoyé.
