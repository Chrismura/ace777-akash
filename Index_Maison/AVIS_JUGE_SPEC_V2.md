# AVIS JUGE — SPEC v2 relance duo

Provider: Google Gemini

**VERDICT : GO AVEC RÉSERVES**

En tant que `signets.juge` (validé par l'architecture vivante ACE777 du 2026-08-14), voici l'audit rigoureux de la **SPEC v2 RELANCE DUO** par rapport aux incidents de la v1 :

---

### Analyse détaillée des points (a) à (d) :

* **(a) Le placement de la fonction `reset_duo_harmony` est-il correct maintenant (dans le lanceur, avant la boucle `while true`) ?**
  * **Statut :** `OK`
  * *Preuve logique :* En définissant la fonction directement à l'intérieur du script lanceur (`launch_vortex_v2_collab_4h_binance.sh`) juste avant la boucle `while true` (et donc après l'initialisation des variables, mais dans le même espace de processus persistant), elle reste entièrement disponible à chaque itération de la boucle. Le piège de l'`exec` (qui remplace le shell parent et vide les fonctions bash importées de l'extérieur) est ainsi totalement contourné.

* **(b) Le bloc double-mort est-il bien après `rc=$?` et avant le bloc STOP existant ?**
  * **Statut :** `OK`
  * *Preuve logique :* Le positionnement garantit que le code de retour (`$?`) de la session qui vient de s'achever est bien capturé dans `rc`. L'analyse de `PROCESS_EXIT.log` via Ruby (compatible macOS/bash 3.2 sans `date -d` ni `mapfile`) s'exécute à chaud avant la logique standard de gestion des fichiers `STOP`, permettant d'intercepter la double-mort simultanée (BETA_X5 + ALPHA_X13_BURST13 en <300s) pour déclencher l'arrêt global d'urgence (`touch STOP STOP_ALPHA STOP_BETA + break`).

* **(c) La clause INTERDIT préserve-t-elle le comportement nominal (pas de `break` sur `rc=0`) ?**
  * **Statut :** `OK`
  * *Preuve logique :* La consigne explicite « *aucun break sur rc=0* » corrige directement le bug introduit par le codeur sur la v1. Le comportement nominal est respecté : une sortie propre (`rc=0`) n'interrompt pas la boucle, autorisant la relance automatique après le `sleep 5` standard, sauf si un fichier `STOP` explicite ou la condition de double-mort est validée.

* **(d) La grille de test 1-5 couvre-t-elle les 2 défauts v1 ?**
  * **Statut :** `GO AVEC RÉSERVES (Mineure)`
  * *Justification de la réserve :* La grille couvre bien le défaut #1 (test 2 : vérification de la fonction `reset_duo_harmony` et de l'état `INIT/RESET`) et le défaut #2 (test 4 : validation que `rc=0` ne déclenche PAS de `break` intempestif). 
  * *Correction minimale demandée au codeur :* Exiger que le test 4 simule explicitement une sortie propre `rc=0` dans un run de test unitaire et chronomètre/vérifie la présence du `sleep 5` suivi d'une nouvelle itération (et non d'un arrêt).

---

### Amélioration prouvée maximale (Clause permanente) :
Pour blinder l'appel Ruby dans le détecteur de double-mort (point b) sous bash 3.2 (macOS/Linux hétérogène), le codeur doit utiliser un one-liner Ruby robuste qui gère proprement l'absence du fichier `PROCESS_EXIT.log` sans lever d'exception bloquante pour le shell :
```bash
ruby -e '
begin
  lines = File.readlines("PROCESS_EXIT.log").last(20)
  # logique de vérification des 300s et des 2 rc=1
  exit(0)
rescue
  exit(1)
end
'
```
Cette précaution évite tout crash du lanceur si le fichier de log est temporairement verrouillé ou absent lors de la première itération.
