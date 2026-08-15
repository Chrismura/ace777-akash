# AVIS GROK (task supervise.decision, morceau M2_routage_budget)

provider: Puter Grok (gratuit)

**Verdict : GO AVEC RESERVES**

Le morceau M2_routage_budget est globalement solide pour un démon 24/7, mais il n’est pas encore au niveau « zéro défaut » exigé par le principe fondateur. Il passe en production avec des réserves opérationnelles.

### Analyse détaillée

**Points solides :**
- Thread-safety correct sur la partie critique (`_blacklock` protège bien `_blacklist` et `_fails`).
- Logique de tempête respectée : les tâches prioritaires (`mission`, `audit.protocol`, `cortana.analyse`, `signets.juge`, `supervise.decision`) ne sont pas coupées quand le budget est atteint en mode tempête. Le code laisse `target_ids` intact et logue correctement en "reserve-storm".
- Backoff progressif + ré-essai automatique bien conçu.
- Patience (retry x2 avec timeout x3) correctement implémentée.
- Filet de sécurité "dernier recours" quand tous les providers sont black-listés.
- Gratuits dynamiques (lecture depuis `providers.json`) → pas de valeur figée.

**Risques identifiés (les réserves)**

| Risque | Niveau | Commentaire | Impact démon 24/7 |
|------|--------|-----------|------------------|
| **Exceptions avalées silencieusement** | Élevé | Beaucoup de `except Exception: pass` (surtout dans `_mode_tempete_actif`, `_gratuits_actifs`, `_regenerer_contexte_vivant`, `_injecter_contexte_vivant`) | Peut masquer une panne de détection tempête ou de contexte vivant sans que personne ne s’en rende compte |
| **Chemins en dur** | Moyen | `~/ace777-test-day1/Index_Maison/...` partout | Si le démon tourne sur une autre machine ou avec un autre utilisateur → rupture |
| **Mode tempête trop passif** | Moyen | En tempête + budget atteint, il logue "réserve storm" mais ne force pas activement les providers gratuits prioritaires. Il garde simplement la liste d’origine | Risque léger de coupure indirecte si les providers payants sont black-listés |
| **Détection tempête fragile** | Moyen | Dépend de plusieurs fichiers JSON externes. Si un fichier est corrompu ou absent, la fonction retourne `False` sans bruit | Peut rater une tempête réelle |
| **Pas de protection sur `usage_today()`** | Bas | Lecture sans verrou, mais acceptable car lecture seule | Faible |

### Recommandations immédiates (à intégrer avant validation famille)

1. **Réduire les exceptions silencieuses** sur les fonctions critiques :
   - `_mode_tempete_actif` devrait au minimum logger en cas d’erreur de lecture des fichiers de stratégie.
   - Idem pour `_regenerer_contexte_vivant`.

2. **Rendre les chemins plus robustes** :
   - Utiliser une variable d’environnement ou un chemin relatif au script plutôt que `~/ace777-test-day1/...` en dur.

3. **Renforcer le comportement en tempête** :
   - Quand `en_tempete and task in taches_prio`, forcer explicitement la liste sur les providers gratuits disponibles plutôt que de garder la liste d’origine.

4. **Ajouter un garde-fou** :
   - Dans `chat_completions`, si après filtrage budget/tempête il ne reste plus aucun provider, lever une erreur claire au lieu d’essayer de continuer.

### Synthèse

Le code est **opérationnellement viable** en l’état pour tourner 24/7, surtout grâce au filet de sécurité et à la logique de patience/backoff. Il ne présente pas de risque majeur de coupure inutile en tempête sur les tâches critiques.

Cependant, le niveau d’exigence "hedge fund suisse" n’est pas encore atteint à cause des exceptions trop larges et des chemins en dur.

**Verdict final : GO AVEC RESERVES**  
On peut le mettre en production, mais il faut traiter les réserves ci-dessus dans les 48h maximum.
