# AVIS JUGE (task signets.juge)

provider: OpenRouter Juge (nemotron-3-super-120b free) - verificateur independant

**VERDICT : NON**  

**Réserves concrètes**  

- **Fichier :** `superviseur_core.sh`  
- **Ligne approximative :** juste après l’ouverture de la boucle `while true; do` (dans le bloc APRÈS soumis, autour de la ligne qui commence par `R_HEARTBEAT="SKIP"; …`).  

**Pourquoi**  
La spécification exige de **conserver le comportement `--force`** : lorsque la variable d’environnement `FORCE=1`, le superviseur doit exécuter un cycle complet immédiatement (en ignorant les timestamps) puis poursuivre la boucle sans sortir. Le code soumis ne contient aucune logique pour tester ou traiter `FORCE` ; donc cette exigence n’est pas satisfaite.  

Tous les autres points (C2 : boucle infinie avec `sleep 60`, C10 : watchdog qui kickstart/load et journalise, non‑fatalité des checks, compatibilité bash 3.2) sont conformes.  

**Action requise**  
Ajouter, à l’intérieur de la boucle `while true; do`, un test du type :

```bash
if [ "$FORCE" = "1" ]; then
    # Forcer l’exécution de tous les checks en réinitialisant les timestamps
    : > "$HOME/.superviseur_core/heartbeat.last"
    : > "$HOME/.superviseur_core/pulse.last"
    : > "$HOME/.superviseur_core/vigie.last"
    : > "$HOME/.superviseur_core/quotas.last"
    : > "$HOME/.superviseur_core/rotation.last"
fi
```

(ou tout autre mécanisme qui fasse que `check_due` retourne vrai pour chaque check lors de cette itération). Une fois ce bloc ajouté, le code sera entièrement conforme et le verdict pourra passer à **GO**.
