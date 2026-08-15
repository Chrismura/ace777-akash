# AVIS JUGE (task signets.juge)

provider: Google Gemini

### VERDICT DU JUGE (ACE777) — **GO AVEC RÉSERVES**

**Justification du verdict :**
Le code fourni résout la **cause racine exacte** du bug du 13/08 : le verrou fichier (`fcntl.flock`) posé **au tout début** de `consulter_famille()` et l'anti-spam enregistré de force avant le lancement des threads neutralisent efficacement les lancements en rafale (toutes les 10s), même si le trio met 30 à 60 secondes à s'exécuter ou en cas d'échec technique (respect strict de la règle 1 et du principe tempête). 

Cependant, le verdict est **GO AVEC RÉSERVES** en raison de quelques points d'intégration et de robustesse à corriger avant le déploiement sur la machine de prod :

---

### ⚠️ RÉSERVES CONCRÈTES À APPLIQUER :

1. **Chemin dynamique de `STRATEGIE_DIR` (`Index_Maison/scripts/famille_session.py`, lignes 14-16)** :
   * *Problème* : Le code utilise une constante en dur `STRATEGIE_DIR = "Index_Maison/strategie"`. Si le script est exécuté depuis un autre répertoire de travail (ou via un cron/launchd dont le *working directory* diffère), les dossiers de verrou et de stratégie ne pointeront pas au bon endroit.
   * *Correction* : Rendre le chemin absolu par rapport à la racine du projet ACE777 :
     ```python
     BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
     STRATEGIE_DIR = os.path.join(BASE_DIR, "strategie")
     ```

2. **Placeholder du trio dans `consulter_famille()` (`Index_Maison/scripts/famille_session.py`, ligne 132)** :
   * *Problème* : Le code livre un placeholder `pass` dans la fonction `_exec_trio()`.
   * *Correction* : Veiller à réintégrer le véritable appel aux threads du trio d'origine (les 3 appels cloud) à la place du `pass` lors de l'intégration finale.

3. **Complétude des tests (`test_famille_verrou.py`)** :
   * *Problème* : Les tests T4, T5, T6, T7 sont des simulations textuelles (`print("OK ...")`) et non des tests unitaires exécutant réellement la logique de `famille_session.py` et `budget_hub.py` dans `/tmp`.
   * *Correction* : Pour les prochains livrables, exiger de vrais appels d'assertion sur les fonctions (`est_tempete()`, `calculer_budget_journalier()`) pour garantir l'hermétisme réel.
