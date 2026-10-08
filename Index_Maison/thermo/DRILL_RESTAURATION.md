# 🩺 DRILL DE RESTAURATION — 🔴 **TROU**

> Testé le **2026-10-08T01:11Z** · mode **lecture seule** (rien installé, rien modifié).
> Question posée : *« si le Mac mourait ce soir, ACE777 reviendrait-il ? »*

## 1. Source — le repo (git) contient-il tout ?
- Branche `main` · HEAD `abe51f5183` du 2026-10-08T00:11:38+02:00
- Fichiers suivis modifiés sur disque : **110**
- Fichiers suivis **supprimés** (perdus) : **0**
- Nouveaux fichiers non versionnés : 31100 au total, dont **8 sensibles** (scripts/plists/règles)
  - `Index_Maison/scripts/CONSULTATION_FAMILLE_CORTANA_JUGE_CONTRE/AVIS_DEEPSEEK.md`
  - `Index_Maison/scripts/CONSULTATION_FAMILLE_CORTANA_JUGE_CONTRE/AVIS_GEMINI.md`
  - `Index_Maison/scripts/CONSULTATION_FAMILLE_CORTANA_JUGE_CONTRE/AVIS_JUGE.md`
  - `Index_Maison/scripts/CONSULTATION_FAMILLE_CORTANA_JUGE_CONTRE/SYNTHESE.md`
  - `Index_Maison/scripts/CONSULTATION_FAMILLE_VEILLEUSE_20260815/AVIS_openrouter-juge.md`
  - `Index_Maison/scripts/CONSULTATION_FAMILLE_VEILLEUSE_20260815/AVIS_openrouter-ultra.md`
  - `Index_Maison/scripts/_archives_tronques_20260911/LISEZ_MOI.md`
  - `Index_Maison/scripts/_archives_tronques_20260911/PROD_SUPERVISEUR_GEMINI.py`

### 1bis. Instruments de la boucle — ce que la boucle EXÉCUTE est-il versionné ?
- Scripts/exécutables invoqués par un agent ou par `git_push_auto.sh` : **143**
- ✅ **0 instrument hors git** — tout ce que la boucle exécute revient avec git.
- Hors repo (volet « organes hors repo » ci-dessous) : 2

## 2. Agents launchd — reconstructibles ?
- Installés : **103** · versionnés : **103**
- ✅ **0 agent hors repo** — tous reconstructibles.

## 3. Reconstruction dans un dossier neuf
- Dossier : `/var/folders/y7/571v2gy574z72zvsgqd46wd40000gn/T/drill_restauration_x6zn7xe7/LaunchAgents`
- Plists rebâtis + validés (`plutil -lint`) : **103/103**

## 4. Organes invoqués par les agents
- Chemins **dans le repo** (reviennent avec git) : **100**
- Chemins **hors repo** (à sauvegarder autrement, git ne les ramène PAS) : **9**

  **Organes du projet hors git** (git ne les ramène PAS → il faut une autre source) :

  | Chemin | agent | rôle | restaurable ? |
  |---|---|---|---|
  | `~/mirofis/frontend` | `mirofish-front` | surveille | ✅ déjà versionné (git amont https://github.com/666ghj/MiroFish.git) |
  | `~/mirofis/backend` | `mirofish` | surveille | ✅ déjà versionné (git amont https://github.com/666ghj/MiroFish.git) |
  | `~/prise-ia/hub_prise_ia.py` | `prise-ia` | argument | ✅ miroir de sauvegarde (organes_hors_repo/prise-ia) |
  | `~/prise-ia` | `prise-ia` | surveille | ✅ miroir de sauvegarde (organes_hors_repo/prise-ia) |
  | `~/prise-ia/routeur_auto.py` | `routeur-auto` | argument | ✅ miroir de sauvegarde (organes_hors_repo/prise-ia) |

  Manifeste des organes hors repo : `thermo/organes_hors_repo.json` (mis à jour 2026-10-07T22:11Z).

  Outillage système hors repo (4) — réinstallable (Homebrew/Xcode CLT), non bloquant : `/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python`, `/Library/Developer/CommandLineTools/usr/bin/python3`, `/opt/homebrew/bin/npm`, `/opt/homebrew/bin/uv`
- ✅ Aucun chemin invoqué introuvable.

## 5. Scellés (registre des synapses ↔ repo)
- Entrées md5 vérifiées : **146** · écarts : **3** · absents : **0**
  - ⚠️ md5 différent : `hulk-mexc/scripts/paper_diprip.py`
  - ⚠️ md5 différent : `hulk-mexc/config/defaults.env`
  - ⚠️ md5 différent : `hulk-mexc/scripts/satellite_aspiration.py`

## 5bis. Pré-déclarations (R20.1) — un scellé se touche ANNONCÉ
- Déclarations au registre : **18** · règle active depuis `2026-09-23T15:30:00Z`
- Dette constatée **16** (27-29/09, datée et nommée, radiée de l'alarme — voir `REGISTRE_ECHECS_ET_ERREURS.md` §13)
- 🔴 **2 modification(s) scellée(s) SANS pré-déclaration antérieure** :
  - `hulk-mexc/config/defaults.env` — modifié le 2026-10-05T09:05:31Z SANS pré-déclaration antérieure
  - `hulk-mexc/scripts/satellite_aspiration.py` — modifié le 2026-10-05T08:38:37Z SANS pré-déclaration antérieure

## 6. Verdict
- 🔴 **2 trou(s) à combler :**
  - 3 scellé(s) dont le md5 ne correspond plus
  - 2 modification(s) de fichier SCELLÉ sans pré-déclaration antérieure (R20.1/R5/R13) : defaults.env, satellite_aspiration.py

---
*Rapport généré par `scripts/drill_restauration.py` (lecture seule). Relancer après toute modification d'organe : un drill, ça se répète.*
