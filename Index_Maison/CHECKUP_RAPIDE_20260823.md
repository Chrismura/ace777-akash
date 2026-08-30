# 🔍 CHECKUP RAPIDE — après correctifs du 23/08/2026

> Liste courte pour vérifier que tout tourne en 2 minutes.
> Tout doit être vert sauf mention « ATTENDU ».

## 1. Le hub (IA)

| Vérif | Commande | Attendu |
|---|---|---|
| Hub vivant | `launchctl list \| grep prise-ia` | PID non nul |
| Health | `curl -s http://127.0.0.1:11435/health` | `{"status": "ok", "providers": 15}` |
| Orca actif | `grep -c "orcarouter/free" ~/prise-ia/providers.json` | `≥ 1` (présent, enabled) |
| Modèle mort corrigé | `grep -c "glm-5.2" ~/prise-ia/providers.json` | `≥ 1` (gpt-oss-20b:free retiré) |
| providers.json stable | `stat -f "%Sm" ~/prise-ia/providers.json` | pas modifié depuis > 1 h (plus de boucle) |

## 2. Les plists (32 corrigés)

| Vérif | Commande | Attendu |
|---|---|---|
| Aucune boucle | `python3 -c "import plistlib,glob; [print(f) for f in glob.glob('$HOME/Library/LaunchAgents/com.ace777.*.plist') if (lambda d: d.get('KeepAlive') and (d.get('StartInterval') or d.get('StartCalendarInterval')))(plistlib.load(open(f,'rb'))) and 'superviseur-core' not in f]"` | **rien affiché** |
| XML valides | `for f in ~/Library/LaunchAgents/com.ace777.*.plist; do plutil -lint "$f" >/dev/null 2>&1 \|\| echo "❌ $f"; done` | rien affiché |
| Jobs chargés | `launchctl list \| grep -c "com.ace777"` | ≥ 50 |
| superviseur-core | `launchctl list \| grep superviseur-core` | PID non nul (daemon, KeepAlive OK) |
| DMS (qui surveille) | `launchctl list \| grep dms-veille` | chargé, heartbeat récent dans le log |

## 3. La chaîne d'apprentissage (Cortana)

| Vérif | Commande | Attendu |
|---|---|---|
| Production analyses | `launchctl list \| grep analyste-cadence` | chargé (08:30 + 20:30) |
| Professeur | `launchctl list \| grep discipline-quotidienne` | chargé (07:15) |
| Scoreur registre | `launchctl list \| grep scoreur-registre` | chargé (07:30) |
| Note Cortana | `python3 -c "import json; d=json.load(open('$HOME/ace777-test-day1/Index_Maison/scripts/justesse_v2.json')); print(d['pct'])"` | ~46 % (à améliorer) |
| Boucle affamée | `python3 -c "import json; d=json.load(open('$HOME/ace777-test-day1/Index_Maison/etat/veille_degradation_etat.json')); print(d['heartbeats'].get('analyses_cortana'))"` | `OK` **ou** `STALE_ALERTE` = production pas encore repartie (ATTENDU si providers saturés) |
| Pattern boucle | `python3 -c "import json; d=json.load(open('$HOME/ace777-test-day1/Index_Maison/etat/veille_degradation_etat.json')); print(d.get('pattern_boucle'))"` | `OK (aucun KeepAlive+intervalle)` |

## 4. Justesse (mesurée 23/08)

| Moteur | Période mesurable | Résultat |
|---|---|---|
| **IA (Cortana)** | 06/08 → 18/08 (pas de données avant) | **47/102 = 46,1 %** |
| **Mécanique (registre)** | 11/08 → 18/08 (pas de données avant) | **6/8 vrais paris = 75 %** (60/68 étaient des tautologies ⚪ exclues) |

⚠️ **Période 09/07 → 05/08 : AUCUNE donnée** (les analyses commencent au 06/08, le registre au 11/08). Impossible de mesurer juillet.

## 5. Ce qui reste « rouge » (attendu, pas un bug)

- `analyses_cortana STALE` : la production a été coupée 19→23/08 ; réactivée le 23/08 mais les providers gratuits étaient saturés (429). Repartira aux prochaines cadences quand la saturation passe. **La surveillance la montre — c'est son rôle.**
- ULTRA/INFERX saturés (audit famille incomplet pour eux).

## Sauvegarde

Tous les plists d'origine : `~/Library/LaunchAgents/BACKUP_plists_20260823/`
