# AVIS GROK (task supervise.decision, morceau M3_serveur_final)

provider: Puter Grok (gratuit)

**Verdict : GO AVEC RESERVES**

### Analyse en superviseur opérationnel (focus M3_serveur_final + cohérence hub)

Le morceau est **globalement solide** pour un démon 24/7, surtout dans l’esprit "hedge fund suisse" que tu vises. Il respecte bien les principes fondateurs (valeur fixe → on coule, gratuits jamais coupés, tempête prioritaire, zéro dépendance externe). Cependant, il reste quelques zones de fragilité qui justifient des réserves plutôt qu’un GO franc.

### Points forts (ce qui tient la route)

- **Logique tempête** : Correctement implémentée. Quand `en_tempete` + tâche prioritaire (`signets.juge`, `audit.protocol`, `mission`, `cortana.analyse`, `supervise.decision`), le `target_ids` reste intact. C’est le comportement attendu. Pas de coupure inutile en tempête sur les tâches critiques.
- **Filet de sécurité dernier recours** (`tried == 0`) : Bien pensé. Évite la panne silencieuse totale quand tout est blacklisé.
- **Thread-safety** : `_blacklock` est utilisé correctement sur les structures partagées critiques (`_blacklist`, `_fails`). Le reste (lecture routing/providers) est majoritairement read-only ou append-only, donc acceptable.
- **Dynamisme** : Les gratuits sont bien dynamiques via `_gratuits_actifs()`. Pas de liste figée dans le code.
- **Patience + backoff progressif** : Robuste. Les timeouts lents ne sont pas considérés comme des échecs définitifs immédiatement.

### Risques identifiés

| Risque | Niveau | Commentaire | Impact 24/7 |
|-------|--------|-----------|-------------|
| **Exceptions avalées silencieusement** | Moyen | Beaucoup de `except Exception: pass` (surtout dans `_mode_tempete_actif`, `log_event`, lecture fichiers events/usage) | Peut masquer une dégradation progressive |
| **Détection tempête fragile** | Moyen | `_mode_tempete_actif()` fait beaucoup de `try/except` silencieux sur des fichiers externes (`ada_gardienne_live.json`, `alarme.json`, etc.). Si un fichier est corrompu ou le chemin change, on peut rater une tempête | Coupure potentielle sur tâches prio |
| **Filtrage budget après complexité** | Faible | La logique budget s’applique après le routage complexité, mais l’indentation et le flux peuvent prêter à confusion en relecture | Risque faible de bug subtil |
| **Tâches prioritaires en dur** | Moyen | `taches_prio` est un set codé en dur dans `chat_completions`. Doit vivre dans `routing.json` pour rester "valeur fixe → on coule" | Maintenance à long terme |
| **Pas de watchdog / heartbeat** | Faible | `serve_forever()` tout seul. Pas de mécanisme de redémarrage automatique si le process se fige | Risque classique démon |
| **Logs et fichiers** | Faible | Ouvertures sans `with` dans certains chemins + `log_message` désactivé | Peut compliquer le debug en production |

### Risque de panne silencieuse

**Modéré.**  
Le plus gros risque vient des `except Exception: pass` dans les fonctions de détection d’état (tempête, contexte vivant). Si `_mode_tempete_actif()` ou `_regenerer_contexte_vivant()` se met à échouer silencieusement, le système peut continuer à tourner en mode "calme" alors qu’il est en tempête, ou perdre le contexte vivant sans qu’on s’en rende compte.

Le filet de sécurité dernier recours (`tried == 0`) protège bien contre le "tout blacklisé = mort", mais il ne protège pas contre une dégradation progressive invisible.

### Risque de coupure inutile en tempête

**Faible.**  
La logique est correcte : les tâches prioritaires conservent leur `target_ids` complet même en budget calme + tempête. Les gratuits ne sont jamais coupés. C’est conforme à la décision du 13/08.

### Recommandations (pour passer en GO franc)

1. **Rendre `taches_prio` dynamique** → le mettre dans `routing.json` (ex: `"priority_tasks"`).
2. **Remplacer les `except Exception: pass`** par un logging minimal (même juste `log_event("error", ...)` dans les cas critiques).
3. **Ajouter un heartbeat simple** dans `/health` (ex: timestamp du dernier cycle réussi) ou un petit thread watchdog.
4. **Uniformiser les ouvertures de fichiers** avec `with` partout où c’est possible.

### Verdict final

**GO AVEC RESERVES** — Le morceau est suffisamment robuste pour tourner en démon 24/7 aujourd’hui, à condition d’accepter un niveau de surveillance un peu plus élevé sur les détections d’état (tempête et contexte). Il ne présente pas de faille critique qui ferait planter le hub de façon silencieuse ou couper des tâches prioritaires en tempête.

Tu peux le déployer, mais je te recommande de traiter les réserves dans les 48-72h avant de le considérer comme "niveau hedge fund suisse" définitif.

Prêt pour le GO complet une fois les réserves traitées.
