# SYNTHÈSE FAMILLE — PLAN PHASE 0 (Grok signé, corrigé par Ada, jugé par la famille)

**Date :** 09/08 17:35 · **Dossier soumis :** DOSSIER_PLAN_PHASE0_FAMILLE_2026-08-09.md
**Modèles réels (vérifiés usage.jsonl — leçon 16:25) :** Gemini (gemini-flash-lite) · DeepSeek (deepseek-v4-flash) · Juge = **fallback** DeepSeek (quota mort) · Ultra = **fallback** DeepSeek (quota mort)

---

## ⚖️ VERDICT UNANIME : **VALIDÉ AVEC MODIFICATIONS** (confiance : haute ×2, moyenne ×2)

**Personne ne refuse le plan. Personne ne le valide tel quel.** 3 consensus majeurs + des corrections précises par famille.

---

## 1. CONSENSUS (les 4 familles s'accordent)

| # | Consensus | Détail |
|---|---|---|
| C1 | **Supprimer la jauge = bon choix** | MAIS à condition de **documenter** ce qu'elle surveillait avant de la supprimer (fichier `jauge_specs.md`), et de **conserver une copie du plist** dans les Backups |
| C2 | **Grouper, pas étaler sur 5 jours** | 5 jours d'état intermédiaire = 5 fenêtres de risque. Grouper en **1 journée** (2 sessions max), avec **validation de Christophe entre chaque étape** |
| C3 | **Il manque l'Étape 0 : état initial** | Snapshot complet avant toute action : `/health` initial documenté + `launchctl list` complet + **backup validé** (testé restaurable, pas seulement copié) |
| C4 | **Test de non-régression complet, pas juste `/health`** | Vérifier les 28 services (échantillon de 5 critiques) + test de charge léger (10 requêtes) après chaque étape |
| C5 | **Seuil de rollback explicite** | 3 échecs `/health` consécutifs = rollback immédiat + arrêt + rapport à Christophe |
| C6 | **`.gitignore` obligatoire** pour le repo unique | Exclure : secrets, fichiers 444, WORM, backups, logs |

## 2. DIVERGENCE SUR L'ORDRE (à trancher)

| Famille | Ordre proposé | Logique |
|---|---|---|
| Grok (auteur) | 1 → 2 → 3 → 4 → 5 | timeout d'abord, repo en dernier |
| Gemini | 1 → 2 → 3 → 4 → 5 ✅ | identique Grok — « timeout d'abord = stopper l'hémorragie » |
| Juge | 1 → 3 (matin), 2 → 4 → 5 (après-midi) | timeout + git d'abord (moins risqués), le reste ensuite |
| DeepSeek | 1 → 2 → **5** → 3 → 4 | **repo unique AVANT** git test-freebuff + rotation (pour versionner ces fichiers) |
| Ultra | **2** → 1 → 4 → 5 → 3 | **jauge AVANT** timeout (masquerait un problème jauge pendant 600s) |

**Lecture honnête :** 3 familles (Grok, Gemini, Juge) gardent **timeout en premier** ; 2 proposent de bouger le repo unique plus tôt ; 1 veut jauge d'abord. **Je recommande : timeout d'abord (majorité), repo unique remonté après la jauge** (compromis DeepSeek+Juge) — détaillé dans le plan v2.

## 3. LE PLAN PHASE 0 v2 (corrigé selon le consensus)

### Étape 0 — ÉTAT INITIAL (nouveau, exigé par les 4)
- `/health` initial documenté + `launchctl list` complet + `ps aux` des Python
- **Backup complet** : `cp -a ~/ace777-test-day1 ~/Backups/ace777/phase0_$(date +%Y%m%d_%H%M%S)`
- **Validation du backup** : test de restauration sur répertoire temporaire (DeepSeek)
- **`jauge_specs.md`** : documenter CE QUE la jauge surveillait avant suppression (Juge + Ultra)
- Copie du plist jauge dans Backups (Ultra)

### Étape 1 — C1 timeout superviseur
- `TIMEOUT_HUB = 15 → 600` (superviseur_auto.py:66)
- `python3 -m py_compile` avant redémarrage (Gemini) + vérifier que le processus superviseur est **relancé** (DeepSeek)
- Tests : import + `/health` ×3 à 30s + 5 services critiques + charge légère

### Étape 2 — Suppression jauge
- `launchctl unload` + `rm plist` + vérifier `ps aux | grep jauge` = vide (Juge)
- Vérifier que le hub ne référence plus la jauge (`grep jauge` dans les configs) (Ultra)
- **Script de surveillance minimale** des quotas en attendant Phase 1 (DeepSeek — condition stricte : sinon rebrancher)

### Étape 3 — Git test-freebuff (le plus sûr, indépendant du hub)
- `git init` + commit initial dans `~/test-freebuff` (chemin corrigé)
- Vérifier **aucune pollution** : `~/ace777-test-day1` ne doit PAS avoir de `.git` (Juge)

### Étape 4 — Rotation des logs
- `RotatingFileHandler` (5 Mo × 3) sur les logs réels de `~/prise-ia/reports/` (chemin corrigé)
- Test : simuler une rotation + vérifier que le superviseur **continue d'écrire** (relit) (Ultra) + logs existants préservés

### Étape 5 — Repo unique de référence
- `git init` à la racine + **`.gitignore`** (secrets, 444, WORM, backups, logs) AVANT le commit (Juge + DeepSeek)
- Vérifier `git ls-files` : aucun secret, aucun fichier 444 modifié

### Règles transverses (imposées)
- Backup avant chaque session · `/health` + 5 services critiques + charge légère après chaque étape
- **Seuil rollback : 3 échecs `/health` consécutifs → rollback immédiat + arrêt + rapport Christophe**
- **Rythme : 1 journée, validation Christophe entre CHAQUE étape** (jamais de batch sans validation)
- Fichiers 444 : jamais en direct, passer par le mécanisme tracé (gardien + signature)

---

## 4. CE QUE ADA DOIT FAIRE (ordre des familles)

1. ✅ Corriger le plan selon le consensus → **ce document (v2)**
2. ⏳ **Présenter à Christophe pour validation finale** (obligatoire — toutes les familles le disent)
3. ⏳ Re-signature : Grok avait signé la v1 — DeepSeek demande de re-soumettre la v2 à Grok pour re-signature
4. ⏳ **Ne RIEN exécuter avant la validation explicite de Christophe**

---

*Références : AVIS_gemini.md · AVIS_deepseek.md · AVIS_juge.md · AVIS_ultra.md · _verification_modeles.txt · DOSSIER_PLAN_PHASE0_FAMILLE_2026-08-09.md · REPONSE_GROK_EXECUTION.md*
