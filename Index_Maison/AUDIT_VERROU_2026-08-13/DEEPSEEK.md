# AVIS DEEPSEEK (task mission)

provider: Puter Grok (gratuit)

**Verdict : NON**

Le code livré ne respecte pas les règles critiques de la spec, particulièrement sur le verrou et l’intégrabilité réelle. Il contient le bug originel sous une forme légèrement modifiée.

### Réserves majeures (bloquantes)

**1. `Index_Maison/scripts/famille_session.py` – Verrou relâché trop tôt (bug originel persistant)**

Lignes 92-100 (fonction `consulter_famille`) :

```python
thread = threading.Thread(target=_exec_trio, daemon=True)
thread.start()
time.sleep(0.1)
return True
...
finally:
    _relacher_lock(lock_fd)
```

Le verrou est relâché après 0,1 s alors que le trio tourne encore (30-60 s). Un appel lancé 10 s plus tard pourra acquérir le lock → re-consultation → boucle possible. C’est exactement le défaut signalé dans la spec (verrou doit tenir **pendant toute la durée** de la consultation).

Le verrou ne protège que le démarrage, pas l’exécution du trio. C’est un échec sur la règle 1a.

**2. Placeholder au lieu du trio réel**

Lignes 78-82 :

```python
def _exec_trio():
    try:
        # Ici se trouve le code réel du trio hub (non modifié)
        # ... appels cloud ...
        pass
    except Exception:
        pass
```

Le code n’est pas intégrable tel quel. Le trio hub réel est absent et remplacé par `pass`. La spec demande du code intégrable sans placeholder.

**3. Anti-spam correct sur le papier, mais affaibli par le verrou défectueux**

`marquer_consulte()` est bien appelé au début (lignes 68-69), ce qui couvre le cas d’échec. Cependant, comme le verrou est relâché très vite, l’anti-spam seul ne suffit pas à empêcher les doublons en rafale si plusieurs processus ou appels rapides contournent le check.

**4. Tests insuffisants et non hermétiques**

Le fichier `test_famille_verrou.py` ne teste pas les vraies fonctions du module. Il refait des simulations manuelles de lock et ne couvre pas :
- Le cas réel de deux appels espacés de 10-15 s pendant que le thread tourne.
- Le comportement avec le vrai `consulter_famille()`.
- La libération tardive du lock.

Les tests T1/T2/T3 ne sont pas réalisés sur le code livré.

**5. Points mineurs mais à corriger**

- `budget_hub.py` : la table `CAPACITES` est complétée, mais la fonction `calculer_budget_journalier` ne gère pas correctement la distinction gratuit/payant pour la réserve storm (logique incomplète).
- `est_tempete()` lit `alarme.json` sans chemin complet (risque de fichier introuvable selon le cwd).
- Absence de journalisation `reserve-storm` et `budget-recalcule` dans `hub_events.jsonl` comme demandé en 3g.

### Ce qui est correct

- Anti-spam écrit au début (même en échec) → respecté.
- Détection tempête (ROUGE / PRENDS_LA_PERTE / vortex / alarme) présente.
- Providers gratuits ne sont pas coupés dans la logique budget (partiellement).
- Code en Python 3.9 stdlib + commentaires en français.

### Conclusion

Le verrou est posé au début mais **relâché trop tôt**, ce qui laisse le bug de boucle famille possible. Le trio réel est absent (placeholder). Le code n’est pas intégrable en l’état.

**Action requise** : refaire le verrou pour qu’il tienne jusqu’à la fin réelle du trio (soit en passant le fd au thread, soit en utilisant un verrou plus long, soit en supprimant le `finally` prématuré). Retirer les `pass` et intégrer le vrai code du trio. Rendre les tests réellement hermétiques sur le module.
