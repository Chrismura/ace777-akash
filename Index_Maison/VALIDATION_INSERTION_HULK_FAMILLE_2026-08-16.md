# signets.juge — insertion HULK disjoncteur (provider Google Gemini, 2.2s)

**1) VERDICT : VALIDÉ AVEC RÉSERVES**

**2) RÉSERVES éventuelles :**
* Le `subprocess.run` est une mauvaise idée : surcharge inutile, latence, gestion des chemins fragiles, et risque de désynchro en cas de timeout. Un **import direct** (`from disjoncteur import verifier_et_brigader`) dans le même process est techniquement plus propre et plus rapide, *tant qu'il ne modifie pas la logique interne du moteur HULK*, mais le codeur a le droit d'utiliser un appel externe s'il le préfère pour l'isolation. 
* Le point d'insertion exact doit se situer **stictement avant** l'appel réseau ou la simulation de l'ordre, au moment précis où HULK calcule la taille du trade (`taille_proposee`).

**3) CONDITIONS avant GO :**
* **Fail-closed absolu (Règle d'or) :** Si le disjoncteur plante, lève une exception, ou si le `subprocess` crash/timeout, **le trade est immédiatement rejeté** (`return False` ou abandon du fill). Aucune exception ne doit laisser passer un ordre par défaut.
* **Capital réel :** La variable `capital_ref` passée au disjoncteur doit impérativement être la valeur dynamique lue depuis l'état réel du compte HULK (balance courante), et en aucun cas une constante en dur (ex: 10000).
* **Non-violation C3 :** Le wrapper se contente de *rogner* ou *bloquer* la taille proposée. Il ne génère, signe ou n'injecte aucun ordre de son propre chef. 

*La Famille ACE777 accorde le GO sous réserve stricte du respect de ces conditions.*
