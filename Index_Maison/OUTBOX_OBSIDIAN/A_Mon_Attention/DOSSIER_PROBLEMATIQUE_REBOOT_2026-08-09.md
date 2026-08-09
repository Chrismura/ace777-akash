# 🔄 DOSSIER FAMILLE — VALIDATION PAR REBOOT + SUPERVISEUR SANS RunAtLoad (demande Christophe, 09/08 20:10)

> **Demande de Christophe :** « Soumets la problématique — et si la question c'est éteindre et rallumer, pourquoi je ne le fais pas maintenant ? »
> **Rédigé par Ada (Buffy), factuel, avec preuves.**

---

## 1. LE CONTEXTE

**Phase 0 terminée aujourd'hui** (plan Grok signé + famille VALIDE AVEC MODIFICATIONS) :
- Étape 1 : `TIMEOUT_HUB 15 → 600` (superviseur_auto.py:66)
- Étape 2 : jauge supprimée, remplacée par `surveillance_quotas.py` (30 min)
- Étape 3 : test-freebuff sous git
- Étape 4 : `rotation_logs.py` (6h)
- Étape 5 : .gitignore complété

**La règle de Grok** (architecture V2.0) : *« garder le hub intact jusqu'à preuve de stabilité 48h »*.
**La question posée :** comment prouver la stabilité ? Réponse d'Ada : par le **test de redémarrage** (M1 — reprise après crash, déjà prouvé au kill -9 du hub : relancé en 2s).

**La question de Christophe :** « Si la preuve c'est éteindre/rallumer, pourquoi ne pas le faire MAINTENANT ? » — argument : pas besoin d'attendre demain matin, on est là maintenant pour vérifier.

---

## 2. LA PROBLÉMATIQUE À JUGER

### P1 — Le superviseur n'a pas `RunAtLoad` (découvert 20:05, vérifié)
**Fait :** `com.ace777.superviseur.plist` a seulement `StartInterval = 3600` — **pas de `RunAtLoad`, pas de `KeepAlive`**.
**Conséquence :** après un reboot, le superviseur ne tourne pas au boot — son premier cycle arrive **~1h après l'allumage**.
**Impact :** en mode froid (réveil), aucune décision du superviseur pendant la première heure. Le hub tourne (RunAtLoad+KeepAlive), Ollama tourne (service macOS), mais le cerveau qui décide est muet 1h.
**Question :** faut-il ajouter `RunAtLoad=true` au plist superviseur ? (modif de production → règle 7 → double signature)

### P2 — Le reboot comme test de validation (la question de Christophe)
**Fait :** tous les services critiques redémarrent au boot :
- Hub : `RunAtLoad=true` + `KeepAlive=true` (testé : kill -9 → relancé en 2s)
- Surveillance quotas : `RunAtLoad=true`
- Rotation logs : `RunAtLoad=true`
- Heartbeat : `RunAtLoad=true`
- Qwen BTC : `StartCalendarInterval` 9h10 (normal)
- Ollama : service macOS chargé

**Question :** le reboot immédiat (maintenant, ce soir) est-il le bon test de validation de la Phase 0 ? Ou vaut-il mieux attendre 48h de fonctionnement continu ? Quels sont les risques d'un reboot immédiat ?

### P3 — Les risques d'un reboot maintenant (à évaluer)
1. **Session Freebuff interrompue** : la conversation avec Christophe se coupe (l'ordi s'éteint). Après reboot, il devra rouvrir et retrouver le contexte (dans le vault/journal).
2. **Services qui ne repartent pas** : c'est justement le test — mais si quelque chose ne repart pas, on est là pour le réparer (c'est mieux que de le découvrir demain seul).
3. **Données** : tout est poussé (2 repos GitHub, vault), WORM append-only, backups Phase 0 existants. Rien ne devrait être perdu.
4. **Processus en cours** : aucun run de trading actif (feu tricolore = STOP partout, console 09/08 06:45).

---

## 3. CE QUE ADA A DÉJÀ VÉRIFIÉ (preuves)

| Vérification | Résultat |
|---|---|
| Hub KeepAlive | `RunAtLoad=true` `KeepAlive=true` |
| Surveillance + rotation | `RunAtLoad=true` (créés aujourd'hui, testés) |
| Heartbeat | `RunAtLoad=true` |
| Superviseur | `StartInterval=3600` seulement → **P1** |
| Qwen BTC | calendrier 9h10 → normal |
| Ollama | chargé (PID 665) |
| 29 services ace777 | chargés dans launchd |
| Git | 2 repos poussés (17:08Z), test-freebuff commité |
| Backup Phase 0 | `~/Backups/ace777/phase0_20260809_185734/` (262 Mo, 7 402 fichiers) |

---

## 4. QUESTIONS À LA FAMILLE

1. **P1 :** faut-il ajouter `RunAtLoad=true` au plist superviseur ? (ou le laisser en StartInterval 3600 — est-ce un problème réel ?)
2. **P2 :** le reboot immédiat est-il le bon test de validation de la Phase 0, ou faut-il 48h de fonctionnement continu ? (Grok avait dit 48h — est-ce applicable ici ou excessif pour un Mac personnel qui s'éteint chaque nuit ?)
3. **P2 bis :** la « preuve de stabilité 48h » a-t-elle du sens si l'ordi est éteint la nuit ? (la stabilité se prouve au démarrage, pas en continu — c'est l'argument de Christophe)
4. **P3 :** y a-t-il un risque que j'aie manqué dans le reboot immédiat ?
5. **Verdict :** REBOOT IMMÉDIAT VALIDÉ / VALIDÉ AVEC CONDITIONS / REFUSÉ — et les conditions éventuelles.

---

## 5. CONTRAINTES

- Mac Air 8 Go, macOS, Python 3.9 stdlib
- Christophe = seul humain, vérifie tout
- La session Freebuff actuelle sera coupée par le reboot (le contexte reste dans vault + journal)
- Rien ne doit être perdu : tout est poussé/sauvegardé

*Références : PHASE0_TERMINEE_2026-08-09.md · CONDITIONS_FAMILLE_2026-08-09.md · ARCHITECTURE_GROK_2026-08-09/ · journal_erreurs.md*
