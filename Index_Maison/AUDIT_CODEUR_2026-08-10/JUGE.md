# AVIS JUGE (task signets.juge)

provider: OpenRouter Juge (nemotron-3-super-120b free) - verificateur independant

**Verdict : GO AVEC RESERVES**

**Réserves concrètes**

| Fichier | Ligne(s) concernée(s) | Observation |
|---------|----------------------|-------------|
| `deleguer_codeur.py` | Bloc `subprocess.run` (lignes ~48‑55) | Seul `subprocess.TimeoutExpired` est intercepté. Si le lanceur (`lancer_detache.py`) ou le script soumis (`soumettre_hub_illimite.py`) est introuvable (chemin erroné, fichier manquant, problème de permissions), une exception `FileNotFoundError` (ou autre `OSError`) remonterait non capturée, produisant un traceback et arrêtant le flux sans message clair. Bien que cela ne constitue pas une faille de la loi 1quinquies, cela pourrait entraîner une perte de temps/credits en nécessitant une intervention manuelle. Une garde supplémentaire (ex. `try/except FileNotFoundError`) serait souhaitable pour rendre le point d’entrée totalement incassable. |

**Justification du GO**

- **Loi 1quinquies** : Le flux délègue effectivement l’écriture du code au « codeur du hub » (via `soumettre_hub_illimite.py` qui interroge l’API hub). Ada ne fait que spécifier, intégrer et tester (écriture de l’en‑tête, vérification de la mission, poll du résultat). Aucun code n’est généré par Ada elle‑même.
- **Robustesse** : 
  - Timeout illimité (`timeout=None`) dans `soumettre_hub_illimite.py`.
  - Réessais 3× avec différenciation des erreurs HTTP retryables (429, 5xx) vs non‑retryables (4xx).
  - Reconstruction de la requête à chaque essai (état propre).
  - Lancement détaché via `lancer_detache.py` avec `start_new_session=True` (équivalent macOS de `setsid`), survit à la mort du shell.
  - Gardes d’entrée : vérification de la spec (> 20 octets) dans `deleguer_codeur.py` ; vérification de l’existence et de la non‑vacuité du fichier mission dans `soumettre_hub_illimite.py`.
  - Aucun traceback brutal dans les chemins d’erreur attendus (messages clairs, `sys.exit(1)`).
- **Tests réels** : Les trois cas d’échec propres (spec vide, spec trop courte, mission absente) produisent des messages clairs et un code de sortie 1 ; le flux valide aboutit à une réponse complète en 10‑20 s.

**Conclusion**  
Le dispositif respecte la loi 1quinquies et présente une robustesse de niveau production. La seule amélioration mineure serait d’intercepter les erreurs de lancement du processus détaché afin d’éviter tout traceback inattendu. Avec cette réserve, le système peut être considéré comme opérationnel et sûr pour une utilisation en continu.
