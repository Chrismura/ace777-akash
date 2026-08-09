# AVIS JUGE (via NVIDIA build.nvidia.com (100+ modeles)) — signets.juge

## ANALYSE CRITIQUE — REBOOT IMMÉDIAT + SUPERVISEUR SANS RunAtLoad

---

### 1. P1 — RunAtLoad sur le superviseur : problème réel, correction obligatoire

**Fait vérifié :** `com.ace777.superviseur.plist` a `StartInterval=3600` sans `RunAtLoad` ni `KeepAlive`.

**Conséquence factuelle :** après reboot, le superviseur ne tourne pas pendant ~1h. Pendant cette fenêtre :
- Le hub tourne (KeepAlive) et exécute ses cycles.
- La surveillance quotas ne tourne pas (elle dépend du superviseur ? — à confirmer, mais probablement).
- Aucune décision de coupure/alerte n'est prise.

**Jugement :** c'est un **défaut de conception réel**. Le superviseur est le cerveau décisionnel. Le laisser muet 1h après chaque boot est inacceptable pour un système qui se veut auto-régulé.

**Action requise :** ajouter `RunAtLoad=true` au plist superviseur. C'est une modification de production → règle 7 → double signature. **Cette modification doit être faite AVANT le reboot**, sinon le test de reboot validera un système incomplet.

---

### 2. P2 — Reboot immédiat vs 48h continu

**La règle de Grok** (« 48h de stabilité ») a été formulée dans un contexte où le système tournait en continu. Or, ce Mac est un **ordinateur personnel qui s'éteint chaque nuit**. La règle n'a pas été adaptée à cette réalité.

**Ce que le reboot immédiat teste réellement :**
- Démarrage à froid de tous les services.
- Reprise du hub après coupure brutale.
- Persistance des données (tout est poussé).
- Comportement de launchd au boot.

**Ce que le reboot immédiat ne teste pas :**
- La stabilité en fonctionnement continu prolongé (fuites mémoire, accumulation d'erreurs).
- Le comportement du superviseur sur plusieurs cycles horaires.

**Jugement :** le reboot immédiat est **un test valide et nécessaire**, mais il ne remplace pas une observation en continu. Il valide la **reprise à froid**, pas la **stabilité à chaud**. Les deux sont complémentaires.

---

### 3. P2 bis — La preuve 48h a-t-elle du sens si l'ordi est éteint la nuit ?

**Argument de Christophe :** la stabilité se prouve au démarrage, pas en continu.

**Analyse factuelle :**
- Si l'ordi est éteint 8h/nuit, un « 48h continu » prend en réalité ~3 jours calendaires.
- Les pannes typiques de ce système (hub qui meurt, superviseur muet) se manifestent **au démarrage ou après un événement**, pas en continu.
- La « stabilité 48h » de Grok visait à vérifier que le hub ne crashe pas en fonctionnement. Ce point est **déjà prouvé** par le kill -9 → relance en 2s.

**Jugement :** l'argument de Christophe est **partiellement fondé**. La preuve de stabilité au démarrage est plus pertinente que la durée continue pour ce système. MAIS : une observation de quelques heures après le reboot (pour vérifier que le superviseur fait son cycle horaire) reste nécessaire.

---

### 4. P3 — Risques manqués dans le reboot immédiat

| Risque identifié | Évaluation |
|---|---|
| Session Freebuff coupée | Mineur — contexte dans vault + journal |
| Services ne repartent pas | C'est le test — on est là pour réparer |
| Données perdues | Nul — tout est poussé + backup 262 Mo |
| Aucun run de trading actif | Confirmé — feu tricolore STOP |

**Risques NON identifiés dans le dossier :**

1. **Le superviseur sans RunAtLoad** (P1) — c'est LE risque principal. Si on reboote maintenant, le superviseur ne tournera pas pendant 1h. Si un problème survient pendant cette fenêtre, personne ne le détectera.

2. **Le hub pourrait ne pas repartir proprement** malgré KeepAlive. Le kill -9 a été testé, mais un reboot complet est différent (arrêt propre de launchd, puis redémarrage). Risque faible mais non nul.

3. **Le plist superviseur modifié (RunAtLoad) devra être rechargé** avant le reboot. Si on oublie, le test sera invalide.

4. **Le journal de bord** : après reboot, il faudra vérifier que le journal reprend correctement (pas de doublon, pas de perte).

---

### 5. VERDICT

**Conditions requises AVANT le reboot :**

1. **Ajouter `RunAtLoad=true` au plist superviseur** (modification de production → double signature).
2. **Recharger le plist superviseur** (`launchctl unload` + `load`).
3. **Vérifier que le superviseur tourne** après rechargement (PID actif).
4. **Pousser les modifications** (plist + code) sur les repos GitHub.
5. **Documenter le test de reboot** dans le journal (heure, attentes, procédure de vérification post-reboot).

**Après le reboot, vérifications obligatoires (dans les 15 min) :**
- Hub actif (PID, log).
- Superviseur actif (PID, log) — **cette fois avec RunAtLoad, il doit tourner immédiatement**.
- Surveillance quotas + rotation logs actifs.
- Heartbeat actif.
- Ollama chargé.
- Journal de bord reprend correctement.

**Après vérification, observation de 2-3h** pour confirmer que le superviseur fait son cycle horaire sans erreur. Ce n'est pas 48h, mais c'est suffisant pour valider la reprise à froid + le premier cycle.

---

VERDICT FINAL : VALIDE AVEC CONDITIONS puis CONFIANCE : haute
