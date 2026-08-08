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
| **Cockpit / Index** | Elle **parle** (Vivienne) — elle **n’écoute pas** le micro |
| **App Cortana** (Rust) | `~/crypto-voice-assistant-core/` · mot d’appel **« Cortana »** · Whisper écoute |
| **Brief Index (thermo)** | `python3 …/cortana_thermo.py resume --say` |
| **Auto horaire** | launchd `com.ace777.cortana.horaire` (toutes les 1 h) |
| **Watch live** | `cortana_watch.py` via launchd urgent (~10 s) — fills, bags, dual Ace+Hulk, baleine, gros move BTC, trend, nouvelles notes Attention |
| **Urgence** | fichier `/tmp/ace777_swarm_pids/.urgent_alert.json` · poll 10 s |

Voix Index : **uniquement Vivienne** (`CORTANA_TTS=edge`, rate `-18%`). Plus de mélange avec la voix Mac `say`.
Chaque indice du résumé a un **avis pédagogique** (ex. funding vs moyenne 30j / mois précédent + « en clair »).

### Watch — seuils défaut

| Signal | Seuil | Niveau |
|--------|-------|--------|
| Fill Alfa / Bêta | nouveau fill | SOFT (respecte MUET) |
| Hulk bag / event | nouveau | SOFT |
| Ace **et** Hulk | même fenêtre 120 s | URGENT |
| Baleine | nouveau max ≥ 500k$ | URGENT |
| Move BTC | \|1h\|≥1.5% ou \|4h\|≥2.5% | URGENT |
| Trend | structure A2 / signe 1h | SOFT |
| Attention | nouveau `.md` | SOFT |

```bash
# premier passage (mémorise sans parler)
python3 ~/ace777-test-day1/Index_Maison/scripts/cortana_watch.py --seed

# test détection
python3 ~/ace777-test-day1/Index_Maison/scripts/cortana_watch.py --dry
```

---

## 3. Couper / entendre (cockpit)

1. Lance le **pont** (une fois, laisse tourner) :
```bash
python3 ~/ace777-test-day1/Index_Maison/scripts/cortana_cockpit_bridge.py
```
2. Ouvre le cockpit → boutons **MUET** / **VOIX** / **PARLER**
   - MUET = silence (vidéo)
   - VOIX / PARLER = brief Vivienne
3. Le pont sert aussi le **feed live** (`/mission` ~10 s) et les **alertes du jour** (`/alerts`).

Sans pont : FEED OFF + boutons morts (message dans la bulle).  
Alertes voix ratées → liste « ALERTES DU JOUR » dans la bulle + `thermo/cortana_alerts_YYYYMMDD.json`.

---

## 4. Sync Obsidian

```bash
bash ~/ace777-test-day1/Index_Maison/OUTBOX_OBSIDIAN/_sync_now.sh
```

Puis dans le vault : cherche **Assistant vocal** ou **DASHBOARD_ARCHITECTURE**.

[[INDEX_COMMANDES]] · [[ATTENTION_VOCALE]]
