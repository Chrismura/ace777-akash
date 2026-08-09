# AVIS ULTRA (via NVIDIA build.nvidia.com (100+ modeles)) — ultra.analyse

## ANALYSE CRITIQUE — REBOOT IMMÉDIAT + SUPERVISEUR SANS RunAtLoad

---

### 1. P1 — RunAtLoad sur le superviseur : OUI, OBLIGATOIRE

**Fait :** le superviseur est le cerveau décisionnel. Sans `RunAtLoad`, après reboot, il reste muet pendant ~1h (premier cycle `StartInterval` à H+1).

**Conséquence concrète :** si un problème survient dans les 60 premières minutes (hub qui crashe, quota dépassé, anomalie), personne ne décide. Le hub a `KeepAlive=true` donc il repartira seul, mais sans supervision — c'est exactement le scénario que la Phase 0 devait éliminer.

**Verdict P1 :** `RunAtLoad=true` est **indispensable**. C'est une modification de production → règle 7 → double signature. **À faire AVANT tout reboot.**

---

### 2. P2 — Reboot immédiat : OUI, mais APRÈS correction P1

**Analyse factuelle :**
- La règle de Grok (48h) visait à prouver la stabilité en fonctionnement continu. Mais l'argument de Christophe est **techniquement valide** : sur un Mac personnel qui s'éteint chaque nuit, la stabilité se prouve au **démarrage**, pas en continu.
- Le kill -9 du hub (relancé en 2s) prouve déjà la reprise à chaud. Le reboot prouve la reprise à froid — c'est le test manquant.
- **Risque du reboot immédiat :** faible. Tout est poussé, sauvegardé, aucun run actif. La session Freebuff sera coupée mais le contexte est dans le vault.
- **Risque d'attendre 48h :** on découvrira un éventuel problème de démarrage demain matin, seul, sans Christophe présent pour aider. C'est **pire**.

**Verdict P2 :** le reboot immédiat est **le bon test**, à condition que P1 soit corrigé d'abord.

---

### 3. P2 bis — La règle des 48h : NON APPLICABLE ici

**Fait :** l'ordi s'éteint chaque nuit. La « stabilité 48h » est un concept pour des serveurs 24/7. Ici, la vraie question est : **est-ce que tout redémarre proprement ?** Ça se teste en 5 minutes, pas en 48h.

**L'argument de Christophe est correct.** La règle de Grok était adaptée à un contexte serveur, pas à un Mac personnel avec extinction nocturne. La Phase 0 est terminée, les tests unitaires sont passés, les backups existent. Attendre 48h n'apporte **aucune information supplémentaire** sur la capacité de redémarrage.

---

### 4. P3 — Risques manqués dans le reboot immédiat

**J'ai vérifié les points listés (session, services, données, processus). Voici ce qui manque :**

1. **Le superviseur sans RunAtLoad (P1)** — c'est LE risque principal. Sans correction, le reboot révélera un superviseur muet pendant 1h. Ce n'est pas un échec du test, mais c'est un défaut connu qu'on doit corriger AVANT, pas après.

2. **Le fichier de verrouillage (lockfile)** : si un processus a laissé un `.lock` (hub, superviseur, quotas), le redémarrage pourrait échouer silencieusement. **À vérifier avant reboot** : `ls ~/Library/Logs/ace777/*.lock` ou équivalent.

3. **Le service Qwen BTC (StartCalendarInterval 9h10)** : après un reboot ce soir, le calendrier launchd est-il conservé ? Oui, launchd persiste les calendriers. Mais si le reboot a lieu après 9h10 demain matin, le service ne se lancera pas avant le lendemain. **À vérifier : l'heure du reboot vs 9h10.**

4. **Le vault/journal** : Christophe devra retrouver le contexte après reboot. Le fichier `PHASE0_TERMINEE_2026-08-09.md` existe, mais il faut **un fichier de reprise explicite** (`REPRISE_APRES_REBOOT.md`) avec les 3 prochaines actions à faire. Sinon, risque de confusion au réveil.

---

### 5. VERDICT

**REBOOT IMMÉDIAT VALIDÉ AVEC CONDITIONS :**

1. **CORRIGER P1 AVANT** : ajouter `RunAtLoad=true` au plist superviseur, recharger le service (`launchctl unload/load`), vérifier qu'il tourne.
2. **VÉRIFIER LES LOCKFILES** avant reboot.
3. **CRÉER `REPRISE_APRES_REBOOT.md`** dans le vault avec les 3 prochaines actions.
4. **VÉRIFIER L'HEURE** : si le reboot est prévu après 9h10, décaler à demain matin (ou accepter que Qwen BTC ne tourne pas ce jour-là).
5. **DOUBLE SIGNATURE** pour la modification du plist superviseur (règle 7).

**Après reboot :** vérifier dans l'ordre : (1) hub actif, (2) superviseur actif (avec RunAtLoad), (3) surveillance quotas, (4) rotation logs, (5) heartbeat, (6) Ollama. Documenter dans le journal.

---

VERDICT FINAL : VALIDE AVEC CONDITIONS puis CONFIANCE : haute
