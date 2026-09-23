# 🩺 DRILL DE RESTAURATION — 🔴 **TROU**

> Testé le **2026-09-23T12:18Z** · mode **lecture seule** (rien installé, rien modifié).
> Question posée : *« si le Mac mourait ce soir, ACE777 reviendrait-il ? »*

## 1. Source — le repo (git) contient-il tout ?
- Branche `main` · HEAD `9ebe75464e` du 2026-09-23T13:18:41+02:00
- Fichiers suivis modifiés sur disque : **116**
- Fichiers suivis **supprimés** (perdus) : **0**
- Nouveaux fichiers non versionnés : 27038 au total, dont **52 sensibles** (scripts/plists/règles)
  - `Index_Maison/scripts/CONSULTATION_FAMILLE_CORTANA_JUGE_CONTRE/AVIS_DEEPSEEK.md`
  - `Index_Maison/scripts/CONSULTATION_FAMILLE_CORTANA_JUGE_CONTRE/AVIS_GEMINI.md`
  - `Index_Maison/scripts/CONSULTATION_FAMILLE_CORTANA_JUGE_CONTRE/AVIS_JUGE.md`
  - `Index_Maison/scripts/CONSULTATION_FAMILLE_CORTANA_JUGE_CONTRE/SYNTHESE.md`
  - `Index_Maison/scripts/CONSULTATION_FAMILLE_VEILLEUSE_20260815/AVIS_openrouter-juge.md`
  - `Index_Maison/scripts/CONSULTATION_FAMILLE_VEILLEUSE_20260815/AVIS_openrouter-ultra.md`
  - `Index_Maison/scripts/SESSIONS_FAMILLE/BRIEF_T01_jugement.md`
  - `Index_Maison/scripts/SESSIONS_FAMILLE/SUPERVISION_BUFFY_23_09/AVIS/T01_deepseek-ai_DeepSeek-V3-0324.md`
  - `Index_Maison/scripts/SESSIONS_FAMILLE/SUPERVISION_BUFFY_23_09/AVIS/T01_gemini-flash-lite-latest.md`
  - `Index_Maison/scripts/SESSIONS_FAMILLE/SUPERVISION_BUFFY_23_09/AVIS/T01_nvidia_nemotron-3-super-120b-a12b_free.md`
  - `Index_Maison/scripts/SESSIONS_FAMILLE/SUPERVISION_BUFFY_23_09/BRIEF_T01.md`
  - `Index_Maison/scripts/SESSIONS_FAMILLE/SUPERVISION_BUFFY_23_09/MEMOIRE.md`
  - `Index_Maison/scripts/SESSIONS_FAMILLE/SUPERVISION_BUFFY_23_09/META.json`
  - `Index_Maison/scripts/SESSIONS_FAMILLE/SUPERVISION_BUFFY_23_09/transcript.jsonl`
  - `Index_Maison/scripts/_archives_tronques_20260911/LISEZ_MOI.md`

### 1bis. Instruments de la boucle — ce que la boucle EXÉCUTE est-il versionné ?
- Scripts/exécutables invoqués par un agent ou par `git_push_auto.sh` : **137**
- ✅ **0 instrument hors git** — tout ce que la boucle exécute revient avec git.
- Hors repo (volet « organes hors repo » ci-dessous) : 2

## 2. Agents launchd — reconstructibles ?
- Installés : **101** · versionnés : **101**
- ✅ **0 agent hors repo** — tous reconstructibles.

## 3. Reconstruction dans un dossier neuf
- Dossier : `/var/folders/y7/571v2gy574z72zvsgqd46wd40000gn/T/drill_restauration_ar7ezomp/LaunchAgents`
- Plists rebâtis + validés (`plutil -lint`) : **101/101**

## 4. Organes invoqués par les agents
- Chemins **dans le repo** (reviennent avec git) : **99**
- Chemins **hors repo** (à sauvegarder autrement, git ne les ramène PAS) : **9**

  **Organes du projet hors git** (git ne les ramène PAS → il faut une autre source) :

  | Chemin | agent | rôle | restaurable ? |
  |---|---|---|---|
  | `~/mirofis/frontend` | `mirofish-front` | surveille | ✅ déjà versionné (git amont https://github.com/666ghj/MiroFish.git) |
  | `~/mirofis/backend` | `mirofish` | surveille | ✅ déjà versionné (git amont https://github.com/666ghj/MiroFish.git) |
  | `~/prise-ia/hub_prise_ia.py` | `prise-ia` | argument | ✅ miroir de sauvegarde (organes_hors_repo/prise-ia) |
  | `~/prise-ia` | `prise-ia` | surveille | ✅ miroir de sauvegarde (organes_hors_repo/prise-ia) |
  | `~/prise-ia/routeur_auto.py` | `routeur-auto` | argument | ✅ miroir de sauvegarde (organes_hors_repo/prise-ia) |

  Manifeste des organes hors repo : `thermo/organes_hors_repo.json` (mis à jour 2026-09-23T11:18Z).

  Outillage système hors repo (4) — réinstallable (Homebrew/Xcode CLT), non bloquant : `/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python`, `/Library/Developer/CommandLineTools/usr/bin/python3`, `/opt/homebrew/bin/npm`, `/opt/homebrew/bin/uv`
- ✅ Aucun chemin invoqué introuvable.

## 5. Scellés (registre des synapses ↔ repo)
- Entrées md5 vérifiées : **131** · écarts : **2** · absents : **0**
  - ⚠️ md5 différent : `Index_Maison/scripts/verifier_regles_or.py`
  - ⚠️ md5 différent : `hulk-mexc/scripts/chiffrage_stop_serre.py`

## 6. Verdict
- 🔴 **1 trou(s) à combler :**
  - 2 scellé(s) dont le md5 ne correspond plus

---
*Rapport généré par `scripts/drill_restauration.py` (lecture seule). Relancer après toute modification d'organe : un drill, ça se répète.*
