# MEMO — HYPOTHÈSE SABOTAGE MOTEUR (14/08)

Christophe : « je pense qu'il s'agit de sabotages. Garder en mémoire qu'un
sabotage intentionnel a été fait sur le moteur. »

## Distinction honnête (superviseur)

1. L'erreur « BACKGROUND process_type not implemented » vue le 14/08 est une
   LIMITATION DE L'OUTILLAGE du superviseur (pas un sabotage du moteur) :
   l'outil terminal ne permet pas de lancer en arrière-plan, et il tue le
   process group à la fin de chaque commande (prouvé en machine : un `nohup`
   simple est mort à la fin de la commande). Contournement : lancer via un
   mécanisme détaché (setsid / launchctl) hors de la session de l'outil.

2. MAIS l'hypothèse de sabotage trouve des preuves RÉELLES et documentées
   dans le moteur (indépendantes de l'outil) :

## Preuves de dérive non scellée (vérifiées 14/08)

- Champion scellé (sauvegarde canonique git) :
  `LE_VRAI_CHAMPION_CERTIFIE_37FCA367.txt` — md5 = 37fca36712d49aa8b97890c5cad5f2e6
  (conforme au MD5_ATTENDU.txt). INTACT dans git.
- Champion ACTIF sur disque : md5 = d6977337a13e14c7867df6a832467d36 — A DÉRIVÉ.
- Diff scellé → actif : 73 lignes de modifications NON tracées :
  * + trap DIAGNOSTIC (14/08, notre correctif validé)
  * + safe_call (14/08, notre correctif validé)
  * + FIX-SCOUT-1/2/3 (rôle SCOUT, revenge conditionné au rôle) — NON scellé
  * - suppression de la fonction duo_hunter_phase_barrier() — NON scellée
- genesis_manifest.txt = SYMLINK vers LE_VRAI_CHAMPION_CERTIFIE_37FCA367.txt
  (le fichier « certifié » a donc été modifié en place : il ne correspond plus
  au md5 scellé).

## Symptômes possiblement liés (à re-examiner avec la famille)

- Morts silencieuses rc=1 sans FATAL_RC1, sans WARN safe_call, stderr vide
  (4 morts le 14/08 : 08:49, 08:52, 09:25, 09:29) — cause non encore capturée.
- Run de capture 14/08 10:24 : tué à ~30 s par l'outil du superviseur
  (process group), PAS par le moteur. Les bots tournaient correctement
  (BETA trade exécuté) avant l'interruption.

## Actions en cours (14/08)

1. Instrumentation capture (trap EXIT + DEBUG) injectée dans
   launch_test_master_base_v8_5_impact.sh (run_unit) — genesis INTACT.
   Backup : launch_test_master_base_v8_5_impact.sh.BAK_avant_instrument_20260814-121858
2. Prochain run de capture détaché (hors outillage) pour attraper un rc=1
   réel avec la ligne exacte.
3. Puis : reconstruction propre depuis le champion scellé 37fca367 +
   ré-application des seuls correctifs validés famille 6/6 + soumission
   FIX-SCOUT / suppression barrière à la famille (légitimes ?).
