# AVIS ULTRA (task ultra.analyse)

provider: OpenRouter Nemotron 3 Ultra 550B (free) - analyse forte

**VERDICT : GO AVEC RESERVES**

**Réserves concrètes :**
1. **Zone grise `DESACTIVES_2026-08-10`** : Le répertoire de quarantaine n'est pas versionné (gitignore probable). Perte machine = perte rollback documenté. *Action : commit le plist backup ou script de restauration autonome.*
2. **Test d'intégration incomplet** : Le dry-run valide l'état *statique* (liste vide), mais aucun test de *charge* (simulation crash d'un job listé + vérif relance effective par le CERVEAU) n'est tracé. *Action : log d'un cycle superviseur réel post-patch.*
3. **Drift config `TIMEOUT_RESEAU = 5`** : Valeur dure en ligne 68 sans constante partagée. Si `superviseur-core` ou `cockpit-http` divergent, escalade incohérente. *Action : centraliser timeouts dans `config.yaml` hub.*
4. **Observabilité "CERVEAU" muette** : Aucune métrique (Prometheus/JSONL) n'est exigée sur les décisions de relance/escalade du `superviseur`. Impossible d'auditer sa santé sans logs bruts. *Action : hook `decision_log` obligatoire.*
