# AVIS GEMINI (task audit.protocol)

provider: Google Gemini

AUDIT PROTOCOLE ACE777 — `GEMINI` (Membre de la famille ACE777)

**VERDICT : GO AVEC RESERVES**

---

### Analyse critique selon les exigences ACE777 :

1. **Le verrou anti-doublon et le verrou de consultation :**
   - *Point de vigilance initial (le bug du 13/08) :* Le verrou ne doit pas être relâché trop tôt dans un bloc `finally` pendant que le trio tourne, sinon un appel à 10s relance une consultation en parallèle.
   - *Vérification du code soumis :* Le code fourni concerne `budget_hub.py` (calcul dynamique), l'intégration du hub (`hub_prise_ia.py`), et les tests (`test_budget_storm.py`). Il ne contient pas directement la boucle de lancement de `consulter_famille()` ou le fichier de lock global du hub (`hub.lock`). C'est un livrable propre et ciblé sur le budget/storm, mais **le superviseur doit s'assurer que le verrou global du hub (`hub.lock`) englobe l'intégralité du traitement du trio** dans `hub_prise_ia.py` et ne se libère pas prématurément.

2. **Anti-spam :**
   - L'anti-spam doit être écrit **au début** de la consultation, même en cas d'échec. Le code d'intégration fourni gère proprement les états et l'absence de crash (try/except non fatal), respectant l'esprit ACE777.

3. **Mode tempête :**
   - Le code détecte correctement le fichier `strategie/etat_tempete.json` via `mode_tempete_actif()`.
   - La réserve storm (20%) est correctement isolée (`cloud_daily_reserve`) et autorise le passage des tâches prioritaires (`signets.juge`, `audit.protocol`, `mission`, `cortana.analyse`, `supervise.decision`) sans blocage par le cap calme. C'est parfaitement aligné avec la doctrine « ACE777 est une machine de tempête ».

4. **Budget dynamique & Providers gratuits :**
   - La table `CAPACITES` est complète (incluant `puter-grok`, `inferx-coder`, `openrouter-ultra`, `openrouter-juge`).
   - Le dictionnaire `GRATUITS` protège les providers qui ne coûtent rien : lorsqu'un budget calme est atteint, les providers payants sont écartés mais les gratuits restent éligibles (`bascule famille`). Plus aucun repli fictif sur le local (C9).

5. **Intégrabilité (Zéro placeholder) :**
   - Les scripts `budget_hub.py` et `test_budget_storm.py` sont complets, écrits en Python 3.9 stdlib, typés (`Optional`, `Dict`, etc.), non fataux (`try...except` globaux) et munis de commentaires en français.
   - Le bloc d'intégration pour `hub_prise_ia.py` est directement copiable.

---

### Réserves concrètes pour l'intégration finale :

1. **Vérification du verrou global (`hub_prise_ia.py`) :**
   - *Réserve :* S'assurer que le fichier `hub.lock` (ou le mécanisme de verrouillage du hub) englobe bien l'appel réseau vers les providers du trio (qui prend 30 à 60s) et ne se libère qu'à la *fermeture complète* de la requête, pour éviter toute ré-entrance intempestive de la boucle 10s (rappel du bug du 13/08).
2. **Chemin du fichier d'état tempête :**
   - Dans le bloc d'intégration du hub, `etat_path = os.path.join(P, 'strategie/etat_tempete.json')`. Vérifier que le dossier `strategie/` est bien initialisé et accessible en écriture par le processus de surveillance.
