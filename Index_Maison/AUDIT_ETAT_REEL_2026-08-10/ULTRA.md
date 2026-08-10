# AVIS ULTRA (task ultra.analyse)

provider: OpenRouter Nemotron 3 Ultra 550B (free) - analyse forte

**VERDICT : GO AVEC RESERVES**

**Conformité immédiate (Points 1, 2, 3) : VALIDE**
- Disque « propre » : 23 plists d'origine (`KeepAlive=False`, `StartInterval=900`), watchdog absent → **zéro risque au reboot**.
- V2 isolées dans `PRETS_ETAPE2_2026-08-10/` (hors `LaunchAgents`) → **activation impossible sans action explicite**.
- Stratégie « attente fusion + GO Christophe » respectée → **aucune casse possible**.

**Réserves concrètes (Bloquantes pour le GO final) :**

1.  **Incohérence critique Inventaire vs Réalité (Superviseur) :**
    - Inventaire Étape 0 : `com.ace777.superviseur-core` → **PID 0 (mort)**.
    - État réel mémoire : **`state = running`**.
    - *Cause probable* : processus lancé *hors* `launchd` (manuel / script) → **non supervisé, non loggué, non redémarré**. Doit être tué et relancé via le plist V2 *au moment de l'activation* pour valider la boucle C2.

2.  **Inventaire Étape 0 obsolète / incomplet :**
    - 6 agents listés seulement (dont 4 à PID 0, 1 à -15, 1 à 1) vs **23 plists sur disque** + hub 9 providers.
    - *Action* : Relancer `launchctl list | grep ace777` **avant activation** pour figer la baseline réelle.

3.  **Preuve de réversibilité (Étape 1) non exhibée :**
    - Règle exige « backup intact, 25 fichiers ». Dossier backup non listé ni hashé ici.
    - *Action* : Fournir `ls -l <backup_dir> | wc -l` + `shasum <backup_dir>/*.plist` dans le dossier de fusion.

4.  **Règle « ÉTAT RÉEL » : Définition incomplète.**
    - Manque : **`launchctl print gui/$(id -u)/com.ace777.superviseur-core`** (état plist chargé + overrides), **contenu exact `WatchPaths`/`QueueDirectories`** des plists V2, **version exacte des scripts** (hash sha256).

**Feu vert conditionnel** : Corriger #1 (kill processus fantôme), produire preuves #3 et #4, mettre à jour inventaire #2. Puis GO définitif.
