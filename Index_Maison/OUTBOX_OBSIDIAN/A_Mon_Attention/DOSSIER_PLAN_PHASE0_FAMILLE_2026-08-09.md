# 🏗️ DOSSIER FAMILLE — VALIDATION DU PLAN PHASE 0 DE GROK (demande Christophe, 09/08 17:30)

> **Demande de Christophe :** « Soumettre avant à la famille » — valider le plan d'exécution Phase 0 signé par Grok avant toute exécution.
> **Rédigé par Ada (Buffy), factuel, avec preuves.** La famille doit juger : exécuter ou pas, dans quel ordre, avec quelles corrections.

---

## 1. CONTEXTE : LA CHAÎNE DES ÉVÉNEMENTS (09/08, vérifié)

1. **17:00** — Christophe demande de décrire ACE777 + problématiques + incapacité, et de faire dessiner par **Grok** la bonne architecture (en l'autorisant à déléguer).
2. **17:10** — Grok répond (via puter-grok, vérifié) : architecture V2.0 — **28 services → 12-14 max, hub intouchable, superviseur unique, cockpit.py, jauge fusionnée, règle 7** (double signature pour toute modif d'architecture). Verdict sur Ada : GARDER sous 6 conditions + règle 7.
3. **17:25** — Christophe : « Demande-lui s'il PEUT le faire, donne-lui du contexte ». Question posée à Grok avec état réel vérifié + contraintes.
4. **17:25** — Grok répond : **HONNÊTE. « Non, je suis une API, je ne touche jamais la machine. »** Il signe le plan d'exécution Phase 0 que **Ada exécutera sous supervision**.
5. **Maintenant** — Christophe : « Soumettre avant à la famille ». **C'est ce dossier.**

---

## 2. LE PLAN PHASE 0 SIGNÉ PAR GROK (sa réponse complète)

### Prérequis (imposés par Grok)
- Double signature : Ada + Grok (donnée)
- **Backup complet avant tout** : `cp -a ~/ace777-test-day1 ~/Backups/ace777/phase0_$(date +%Y%m%d_%H%M%S)` *(chemin corrigé par checker)*
- Hub vérifié vivant avant / après chaque étape

### Les 5 étapes (ordre strict, ne pas changer)

| # | Étape | Action | Test non-régression | Rollback |
|---|---|---|---|---|
| **1** | **C1 — timeout superviseur** | `TIMEOUT_HUB = 15 → 600` (superviseur_auto.py:66) | import + `/health` OK | restaurer backup |
| **2** | **Jauge** | **Suppression propre** : `launchctl unload` + `rm plist` | `launchctl list \| grep jauge` = vide + `/health` OK | restaurer plist + `launchctl load` |
| **3** | **test-freebuff** | `git init` + commit initial | `git status` propre + `/health` OK | `rm -rf .git` |
| **4** | **Rotation logs** | `RotatingFileHandler` (5 Mo × 3) dans le module de log | rotation fonctionne + `/health` OK | restaurer depuis backup |
| **5** | **Repo unique de référence** | `git init` à la racine de référence + commit | `git log` + `/health` OK | `rm -rf .git` |

### Règles d'exécution (Grok)
- Backup d'abord, vérifier `/health` après CHAQUE étape
- **Si le hub ne répond plus → rollback immédiat de l'étape + arrêt**
- Mode probatoire C6 : 1 action autonome/jour → double signature avant chaque exécution
- Fichiers 444 : ne jamais modifier en direct, passer par le mécanisme tracé

---

## 3. CORRECTIONS DU CHECKER (Ada) — le plan est bon, mais des détails sont faux

| # | Ce que Grok a écrit | La réalité | Correction |
|---|---|---|---|
| 1 | `~/ace777/...` | `~/ace777-test-day1/...` | chemins corrigés partout |
| 2 | port `XXXX` | **port 11435** | `/health` = `http://127.0.0.1:11435/health` |
| 3 | `~/ace777/test-freebuff` | `~/test-freebuff` | chemins corrigés |
| 4 | Étape 2 « jauge » : nom plist exact | `com.ace777.jauge-energie.plist` (vérifié) | nom exact utilisé |
| 5 | Étape 4 : fichier de log | superviseur écrit dans `~/prise-ia/reports/` (vérifié) | adapter le chemin de rotation |

**Verdict checker : plan cohérent avec l'architecture Grok, applicable tel quel après corrections de chemins.**

---

## 4. QUESTIONS À LA FAMILLE (répondre factuel, sans complaisance)

1. **Le plan Phase 0 de Grok est-il correct et complet** pour stabiliser ACE777 sans rien casser ? Manque-t-il une étape critique ?
2. **L'ordre des 5 étapes est-il le bon** ? (C1 timeout → jauge → git test-freebuff → rotation logs → repo unique)
3. **Le choix « supprimer la jauge »** (plutôt que la rebrancher) est-il le bon, sachant que sa fonction (surveiller l'énergie/quota par provider) doit être reprise par le superviseur unique en Phase 1 ? Ou faut-il la rebrancher dès maintenant ?
4. **Le rythme d'exécution** : mode probatoire C6 = 1 action autonome/jour. Faut-il étaler (1 étape/jour) ou grouper (tout en 1 journée avec tests) ?
5. **Risque principal** de chaque étape, et vérification spécifique à ajouter ?
6. **Verdict** : VALIDÉ / VALIDÉ AVEC MODIFICATIONS / REFUSÉ — et ce que Ada doit faire en conséquence.

---

## 5. CONTRAINTES RAPPEL

- Mac Air **8 Go RAM**, macOS, Python 3.9 stdlib
- IA gratuites uniquement, failover obligatoire
- **Rien ne doit casser le hub** (seul point d'entrée, 28 services actifs)
- 6 conditions famille actives (fichiers 444, WORM, double signature, probatoire C6)
- Christophe = seul humain, vérifie tout

---

*Références : REPONSE_GROK.md (architecture) · REPONSE_GROK_EXECUTION.md (plan signé) · BRIEF_GROK_ARCHITECTURE_2026-08-09.md · BRIEF_GROK_EXECUTION_2026-08-09.md · CONDITIONS_FAMILLE_2026-08-09.md · journal_erreurs.md*
