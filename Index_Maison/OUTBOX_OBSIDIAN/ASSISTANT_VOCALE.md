# Assistant vocal · Cortana — liens & commandes

**Où c’est rangé :** cette note (Index) · miroir Obsidian après `_sync_now.sh`  
**Aussi :** [[DASHBOARD_ARCHITECTURE]] · [[CORTANA_VOIX]] · `Swarm_Bus/10_ATTENTION_VOCALE`

---

## 1. Ouvrir le cockpit (1 clic)

| Quoi | Lien |
|------|------|
| **Cockpit arcade** | [cockpit/index.html](file:///Users/christophe/ace777-test-day1/Index_Maison/cockpit/index.html) |
| Architecture VUE | [architecture/index.html](file:///Users/christophe/ace777-test-day1/Index_Maison/architecture/index.html) |
| Thermo | [thermo/index.html](file:///Users/christophe/ace777-test-day1/Index_Maison/thermo/index.html) |

Terminal :
```bash
open ~/ace777-test-day1/Index_Maison/cockpit/index.html
```

Avant (feeds) :
```bash
python3 ~/ace777-test-day1/Index_Maison/scripts/cockpit_mission_feed.py
python3 ~/ace777-test-day1/Index_Maison/scripts/thermo_quotidien_free.py
```

---

## 2. Comment enclencher Cortana

| Mode | Comment |
|------|---------|
| **App Cortana** (Rust) | Dis le mot d’appel **« Cortana »** (wake phrase) · TTS Vivienne/edge |
| **Brief Index (thermo)** | `python3 …/cortana_thermo.py resume --say` |
| **Auto horaire** | launchd `com.ace777.cortana.horaire` (toutes les 1 h) |
| **Urgence** | fichier `/tmp/ace777_swarm_pids/.urgent_alert.json` · poll 10 s |

---

## 3. Couper la voix (vidéo / silence)

```bash
# MUET
python3 ~/ace777-test-day1/Index_Maison/scripts/cortana_mute.py on

# RÉACTIVER
python3 ~/ace777-test-day1/Index_Maison/scripts/cortana_mute.py off

# état
python3 ~/ace777-test-day1/Index_Maison/scripts/cortana_mute.py status
```

Fichier : `/tmp/ace777_swarm_pids/.cortana_mute`  
Bouton **MUET** aussi dans le widget Cortana du cockpit (écrit via script — voir §4).

---

## 4. Sync Obsidian

```bash
bash ~/ace777-test-day1/Index_Maison/OUTBOX_OBSIDIAN/_sync_now.sh
```

Puis dans le vault : cherche **Assistant vocal** ou **DASHBOARD_ARCHITECTURE**.

[[INDEX_COMMANDES]] · [[ATTENTION_VOCALE]]
