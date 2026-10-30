# 🩺 DRILL DE RESTAURATION — 🔴 **TROU**

> Testé le **2026-10-30T00:52Z** · mode **lecture seule** (rien installé, rien modifié).
> Question posée : *« si le Mac mourait ce soir, ACE777 reviendrait-il ? »*

## 1. Source — le repo (git) contient-il tout ?
- Branche `main` · HEAD `8b9a01a4f5` du 2026-10-30T00:54:44+01:00
- Fichiers suivis modifiés sur disque : **88**
- Fichiers suivis **supprimés** (perdus) : **0**
- Nouveaux fichiers non versionnés : 32128 au total, dont **17 sensibles** (scripts/plists/règles)
  - `Index_Maison/plists/com.ace777.desaccord.plist`
  - `Index_Maison/scripts/CONSULTATION_CODEUR_GRAPHIQUE_20260814/AVIS_inferx-coder.md`
  - `Index_Maison/scripts/CONSULTATION_CODEUR_GRAPHIQUE_20260814/AVIS_oss20.md`
  - `Index_Maison/scripts/CONSULTATION_FAMILLE_CORTANA_JUGE_CONTRE/AVIS_DEEPSEEK.md`
  - `Index_Maison/scripts/CONSULTATION_FAMILLE_CORTANA_JUGE_CONTRE/AVIS_GEMINI.md`
  - `Index_Maison/scripts/CONSULTATION_FAMILLE_CORTANA_JUGE_CONTRE/AVIS_JUGE.md`
  - `Index_Maison/scripts/CONSULTATION_FAMILLE_CORTANA_JUGE_CONTRE/SYNTHESE.md`
  - `Index_Maison/scripts/CONSULTATION_FAMILLE_VEILLEUSE_20260815/AVIS_openrouter-juge.md`
  - `Index_Maison/scripts/CONSULTATION_FAMILLE_VEILLEUSE_20260815/AVIS_openrouter-ultra.md`
  - `Index_Maison/scripts/REPONSE_CODEUR_5points_cortana.md`
  - `Index_Maison/scripts/SPEC_revue_5points_cortana.md`
  - `Index_Maison/scripts/SPEC_revue_5points_cortana.md.mission.txt`
  - `Index_Maison/scripts/_archives_tronques_20260911/LISEZ_MOI.md`
  - `Index_Maison/scripts/_archives_tronques_20260911/PROD_SUPERVISEUR_GEMINI.py`
  - `Index_Maison/scripts/champion_cortana.json`

### 1bis. Instruments de la boucle — ce que la boucle EXÉCUTE est-il versionné ?
- Scripts/exécutables invoqués par un agent ou par `git_push_auto.sh` : **162**
- 🔴 **1 NON versionnés** → un Mac mort les perdrait, et la boucle ne redémarrerait pas :
  - `Index_Maison/scripts/desaccord.py`
- Hors repo (volet « organes hors repo » ci-dessous) : 2

## 2. Agents launchd — reconstructibles ?
- Installés : **112** · versionnés : **112**
- ✅ **0 agent hors repo** — tous reconstructibles.

## 3. Reconstruction dans un dossier neuf
- Dossier : `/var/folders/y7/571v2gy574z72zvsgqd46wd40000gn/T/drill_restauration_yfatv9v0/LaunchAgents`
- Plists rebâtis + validés (`plutil -lint`) : **112/112**

## 4. Organes invoqués par les agents
- Chemins **dans le repo** (reviennent avec git) : **107**
- Chemins **hors repo** (à sauvegarder autrement, git ne les ramène PAS) : **9**

  **Organes du projet hors git** (git ne les ramène PAS → il faut une autre source) :

  | Chemin | agent | rôle | restaurable ? |
  |---|---|---|---|
  | `~/mirofis/frontend` | `mirofish-front` | surveille | ✅ déjà versionné (git amont https://github.com/666ghj/MiroFish.git) |
  | `~/mirofis/backend` | `mirofish` | surveille | ✅ déjà versionné (git amont https://github.com/666ghj/MiroFish.git) |
  | `~/prise-ia/hub_prise_ia.py` | `prise-ia` | argument | ✅ miroir de sauvegarde (organes_hors_repo/prise-ia) |
  | `~/prise-ia` | `prise-ia` | surveille | ✅ miroir de sauvegarde (organes_hors_repo/prise-ia) |
  | `~/prise-ia/routeur_auto.py` | `routeur-auto` | argument | ✅ miroir de sauvegarde (organes_hors_repo/prise-ia) |

  Manifeste des organes hors repo : `thermo/organes_hors_repo.json` (mis à jour 2026-10-29T23:54Z).

  Outillage système hors repo (4) — réinstallable (Homebrew/Xcode CLT), non bloquant : `/Library/Developer/CommandLineTools/Library/Frameworks/Python3.framework/Versions/3.9/Resources/Python.app/Contents/MacOS/Python`, `/Library/Developer/CommandLineTools/usr/bin/python3`, `/opt/homebrew/bin/npm`, `/opt/homebrew/bin/uv`
- ✅ Aucun chemin invoqué introuvable.

## 5. Scellés (registre des synapses ↔ repo)
- Entrées md5 vérifiées : **208** · écarts : **4** · absents : **0**
  - ⚠️ md5 différent : `Index_Maison/scripts/cortana_analyzer.py`
  - ⚠️ md5 différent : `hulk-mexc/scripts/cortana_propose_params.py`
  - ⚠️ md5 différent : `Index_Maison/REGISTRE_ECHECS_ET_ERREURS.md`
  - ⚠️ md5 différent : `Index_Maison/strategie/JOURNAL_ECRIVAINS.jsonl`

## 5bis. Pré-déclarations (R20.1) — un scellé se touche ANNONCÉ
- Déclarations au registre : **266** · règle active depuis `2026-09-23T15:30:00Z`
- Dette constatée **31** (27-29/09, datée et nommée, radiée de l'alarme — voir `REGISTRE_ECHECS_ET_ERREURS.md` §13)
- 🔴 **27 modification(s) scellée(s) SANS pré-déclaration antérieure** :
  - `Index_Maison/scripts/ada_gardienne.py` — re-scellé le 2026-10-29T23:45:37Z SANS pré-déclaration antérieure
  - `Index_Maison/scripts/sentinel.py` — re-scellé le 2026-10-29T22:06:39Z SANS pré-déclaration antérieure
  - `Index_Maison/scripts/simulateur_plancher_confirme.py` — re-scellé le 2026-10-30T00:18:43Z SANS pré-déclaration antérieure
  - `hulk-mexc/scripts/chiffrage_pnl_net.py` — re-scellé le 2026-10-28T19:36:07Z SANS pré-déclaration antérieure
  - `Index_Maison/scripts/observe_nado.py` — re-scellé le 2026-10-24T19:11:49Z SANS pré-déclaration antérieure
  - `Index_Maison/PLATEFORMES.md` — re-scellé le 2026-10-28T09:21:12Z SANS pré-déclaration antérieure
  - `hulk-mexc/BAC_A_SABLE/REGIMES_15.md` — re-scellé le 2026-10-28T10:59:21Z SANS pré-déclaration antérieure
  - `hulk-mexc/BAC_A_SABLE/ADDENDUM_AFFINAGE_Q6_Q11.md` — re-scellé le 2026-10-28T15:27:24Z SANS pré-déclaration antérieure
  - `hulk-mexc/scripts/cortana_fade_ombre.py` — re-scellé le 2026-10-28T15:45:11Z SANS pré-déclaration antérieure
  - `hulk-mexc/BAC_A_SABLE/PROTOCOLE_BOUCLE_FERMEE.md` — re-scellé le 2026-10-28T16:39:57Z SANS pré-déclaration antérieure
  - `hulk-mexc/scripts/garde_reconciliation.py` — re-scellé le 2026-10-28T19:36:07Z SANS pré-déclaration antérieure
  - `hulk-mexc/scripts/couts_communs.py` — re-scellé le 2026-10-28T19:36:08Z SANS pré-déclaration antérieure
  - `hulk-mexc/runs/TOPO_HOLDS.md` — re-scellé le 2026-10-28T20:00:41Z SANS pré-déclaration antérieure
  - `hulk-mexc/scripts/chiffrage_entree_retest.py` — re-scellé le 2026-10-28T20:24:35Z SANS pré-déclaration antérieure
  - `hulk-mexc/scripts/chiffrage_reentree_repart.py` — re-scellé le 2026-10-28T21:16:05Z SANS pré-déclaration antérieure
  - `hulk-mexc/scripts/chiffrage_attribution_reentree.py` — re-scellé le 2026-10-28T21:16:06Z SANS pré-déclaration antérieure
  - `hulk-mexc/scripts/chiffrage_redeploy_variantes.py` — re-scellé le 2026-10-28T21:16:06Z SANS pré-déclaration antérieure
  - `hulk-mexc/scripts/chiffrage_trailing_serre.py` — re-scellé le 2026-10-28T21:16:06Z SANS pré-déclaration antérieure
  - `hulk-mexc/scripts/chiffrage_redeploy_adaptatif.py` — re-scellé le 2026-10-28T21:28:42Z SANS pré-déclaration antérieure
  - `hulk-mexc/scripts/consulter_famille_metacognition_20261028.py` — re-scellé le 2026-10-28T22:09:00Z SANS pré-déclaration antérieure
  - `hulk-mexc/scripts/hypothese.py` — re-scellé le 2026-10-28T22:16:42Z SANS pré-déclaration antérieure
  - `Index_Maison/POINT_REPRISE_DERNIER.md` — re-scellé le 2026-10-28T22:42:43Z SANS pré-déclaration antérieure
  - `/Users/christophe/ace777-test-day1/Index_Maison/scripts/cortana_analyzer.py` — re-scellé le 2026-10-29T20:26:18Z SANS pré-déclaration antérieure
  - `/Users/christophe/ace777-test-day1/hulk-mexc/scripts/cortana_propose_params.py` — re-scellé le 2026-10-29T20:26:18Z SANS pré-déclaration antérieure
  - `Index_Maison/data/fiches_analyse/blocs_privilises.json` — re-scellé le 2026-10-29T22:06:44Z SANS pré-déclaration antérieure
  - `Index_Maison/scripts/ada_saison.py` — re-scellé le 2026-10-29T23:45:37Z SANS pré-déclaration antérieure
  - `Index_Maison/scripts/desaccord.py` — re-scellé le 2026-10-30T00:36:12Z SANS pré-déclaration antérieure

## 6. Couverture des classes d'erreur — anticiper l'erreur SUIVANTE
- Dénominateur **lu au registre** : **30 classes** (E1, E2, E3, E4, E5, E6, E7, E8, E9, E10, E11, E12, E13, E14, E15, E16, E17, E18, E19, E20, E21, E22, E23, E24, E25, E26, E27, E28, E29, E30)
- Gardes **mécaniques** (existent + branchées) : **21** · **promesses déclarées** : 5 · **ouverture(s)** : 0
- 🔴 **4 trou(s)** — une classe connue dont la garde n'est pas debout :
  - **E27** — classe au registre SANS garde declaree (gardes_erreurs.json)
  - **E28** — classe au registre SANS garde declaree (gardes_erreurs.json)
  - **E29** — classe au registre SANS garde declaree (gardes_erreurs.json)
  - **E30** — classe au registre SANS garde declaree (gardes_erreurs.json)

## 7. Verdict
- 🔴 **4 trou(s) à combler :**
  - 1 instrument(s) que la boucle EXÉCUTE et qui ne sont PAS dans git → perdus à la restauration (Index_Maison/scripts/desaccord.py)
  - 4 scellé(s) dont le md5 ne correspond plus
  - 27 modification(s) de fichier SCELLÉ sans pré-déclaration antérieure (R20.1/R5/R13) : ada_gardienne.py, sentinel.py, simulateur_plancher_confirme.py…
  - 4 classe(s) d'erreur CONNUE(S) dont la garde déclarée est absente ou NON BRANCHÉE (R15 : hors de la boucle = n'existe pas) : E27, E28, E29, E30

---
*Rapport généré par `scripts/drill_restauration.py` (lecture seule). Relancer après toute modification d'organe : un drill, ça se répète.*
