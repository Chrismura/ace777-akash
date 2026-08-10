# 🔄 JOURNAL DE FUSION — 10/08/2026

## Fusion 1/2 : com.ace777.analyse-usage — DÉSACTIVÉ ✅
- **Rôle** : rapport hebdo d'usage (dimanche 9h00, `analyse_usage.py --days 7 --write`)
- **Pourquoi** : service mort / rapport jetable / zéro dépendant actif
- **Audit C5** : seule référence = superviseur_auto.py (JOBS_ATTENDUS) → corrigé
- **Protocole** : backup plist → bootout → déplacement hors LaunchAgents → test
- **Backup** : `~/Library/LaunchAgents/DESACTIVES_2026-08-10/com.ace777.analyse-usage.plist`
- **Rollback** : recopier le plist dans LaunchAgents + `launchctl bootstrap gui/$(id -u)`

## Patch JOBS_ATTENDUS (codeur + famille) — INTÉGRÉ ✅
- **Problème** : le CERVEAU (superviseur_auto.py) surveille JOBS_ATTENDUS et relance
  les jobs manquants → il aurait relancé analyse-usage désactivé (tentatives + escalade)
- **Solution** : retirer `com.ace777.analyse-usage` de JOBS_ATTENDUS
- **Flux** : spec → codeur (réponse 40 s) → famille (GO 4/4 : GEMINI, DEEPSEEK, JUGE, ULTRA) → intégré + testé
- **Preuve** : dry-run = `jobs_manquants=[]`, `action=none`, `résultat=rien à faire`
- **Backup** : `superviseur_auto.py.bak_patch_jobs_20260810`

## Fusion 2/2 : com.ace777.superviseur (ancien) — CONSERVÉ (découverte)
- ⚠️ Ce n'est PAS un doublon : c'est le CERVEAU de supervision intelligent
  (cycle lire → état → décision → agir : relance des jobs morts max 3/jour,
  escalade humaine, push git). superviseur-core = seulement les 5 checks mécaniques.
  → Rôles COMPLÉMENTAIRES, les 2 restent.

## Candidats écartés par l'audit C5 (chaîne de sécurité VIVANTE)
- **veille-hub / eval-offres / catalogue / observatoire** : circuit de validation des
  intégrations (9h05 → 9h30 → 10h → 11h, sondes 48h + GO hebdo). Désactiver = casser la sécurité.
- **propose-ameliorations** : vérifié par verifier_setup.py (check launchd cycle matin)
- **graph-cerveau** : alimente data.js → cortana_analyse / cortana_brief / coffre_ask

## État final
- Services ace777 : **22** (était 23) · Hub : OK 9 providers · Cerveau : nominal
- Prochaine étape : verif-setup (débloqué par tag) à sa prochaine exécution 12:00
