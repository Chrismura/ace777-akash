# 🤝 PROTOCOLE DE DÉLÉGATION — quand l'IA programme, le chief scientist valide

> **Rôle :** règle de fonctionnement pour déléguer la programmation à des agents/IA sans perdre en qualité ni casser la doctrine.
> **Validé :** Christophe 06/08/2026 — « je valide ton analyse, go ».
> **Principe fondateur :** celui qui écrit n'est JAMAIS celui qui valide (loi gippp69 : 45 % → 82,5 % d'approbation).

---

## Pourquoi (les leçons déjà vécues)

| Preuve | Leçon |
|---|---|
| Audit IA de ce matin : « CRITIQUE » faux positif + correction qui aurait cassé la garde | Un agent qui produit peut *marcher* mais violer la doctrine (ex. suggérer `pgrep` alors qu'on a prouvé qu'il est aveugle) |
| Review de cortana_analyse.py : 4 vrais bugs attrapés (valeurs brutes manquantes, signature, prompt, message d'erreur) | **Vérifier n'est pas trivial** : lire + tester + challenger contre la spec |
| OSSATURE_INDEX : « Overdose → 1 GO à la fois · fluidité > features » | Ne pas empiler les agents — canaliser |

---

## Le flux (toujours dans cet ordre)

```
1. SPEC (Ada/chef)     → ce que je veux + contraintes + doctrine maison + pièges connus
2. PRODUCTION (agent)  → première version du code (Gemini via hub, ou agent dédié)
3. REVIEW (Ada)        → vérifier contre la spec + tests réels
4. VALIDATION (Ada)    → je garde le dernier mot. Toujours. → commit
```

## Ce que je délègue vs ce que je garde

| Je délègue | Je garde |
|---|---|
| Tâches isolées et bien spécifiées (un script, une route, un widget) | La spec · l'architecture · le tri des verdicts |
| Première version de code | Les tests réels · la validation finale · les décisions |
| Recherche / exploration (code search, web, docs) | La doctrine maison et les pièges connus |

---

## Les garde-fous (non négociables)

1. **1 GO à la fois** — pas 9 agents qui tradent/programment en même temps (règle OSSATURE).
2. **Spec écrite avant tout** — un agent sans spec claire produit au hasard.
3. **Review systématique** — code-reviewer + tests réels avant validation.
4. **Doctrine transmise** — l'agent reçoit les contraintes : pas d'ordres depuis l'UI, pgrep aveuglé, pipefail, TCC, etc.
5. **Le chef tranche** — Ada (chef scientifique) a le dernier mot sur ce qui entre dans le repo.

---

## 🛡️ CEINTURE ZÉRO FAUTE — version amendée (validée Christophe 09/08, avis 4 familles)

> Consultation de 4 familles différentes (Gemini · Nemotron juge · DeepSeek V4 · Nemotron Ultra) :
> verdict unanime « PARTIELLEMENT » — la démarche est bonne mais ne suffit pas. Corrections intégrées ci-dessous.
> Dossier : `CONSULTATION_ZERO_FAUTE_2026-08-09/` · Règle : une faute ne doit pas pouvoir s'introduire
> **silencieusement** — soit le test la détecte, soit l'audit la trouve, soit le backup la défait.

### Le flux ZÉRO FAUTE (ordre impératif — remplace le flux simple de la section précédente)

```
1. SPEC (Buffy)        → quoi + contraintes + pièges connus
2. JUGE VALIDE LA SPEC → avant que le codeur écrive quoi que ce soit (sinon la grille
                         valide la faute « conforme à la spec »)  ⚠️ ajout clé des familles
3. PRODUCTION (codeur) → Qwen3-Coder / DeepSeek V4 — borné à la tâche
4. JUGE ÉCRIT LA GRILLE DE TEST AVANT → commandes exactes + résultat attendu, écrites
                         par un TIERS (jamais par celui qui code, jamais par le superviseur)
5. EXÉCUTION AUTO      → test_chantier.sh lance la grille → résultat MACHINE, pas d'interprétation
6. AUDIT FAMILLE DIFFÉRENTE → jamais la même famille qui juge et qui produit
7. GO Christophe       → mise en service
```

### Les 6 couches + les 3 corrections exigées par les familles (consensus)

| Couche | Règle |
|---|---|
| 1. Backup daté | `.bak-<date>` avant tout changement — rien d'irréversible |
| 2. Grille par le juge | écrite AVANT, par un tiers, commandes + résultat attendu |
| 3. Exécution machine | `test_chantier.sh` → résultat automatique, non interprété |
| 4. Famille différente | audit croisé, jamais même famille |
| 5. Petits pas additifs | on ajoute, on ne remplace jamais ; le SAIN protégé (superviseur, autopilote, hub, MiroFish, boot.sh) |
| 6. Rollback | retour au backup daté, tracé |

**Corrections consensus (les familles les exigent) :**
1. **Test de restauration PROUVÉ** — après chaque backup : checksum + restauration sandbox + vérif que le système repart. Un `.bak` jamais vérifié = ceinture décorative.
2. **Reset de l'état runtime avant test** — re-boot du hub, caches purgés : un test ne doit pas tourner sur un état résiduel qui fausse le résultat.
3. **Au-delà du chemin nominal** — la grille doit tester ce qui CASSE : provider down, JSON tronqué, RAM pleine, 500/garbage. (Chaos léger, adapté Mac 8 Go.)

**Honnêteté (toutes les familles) :** le zéro faute ABSOLU n'existe pas — l'objectif réaliste est un système où une faute ne peut pas s'introduire silencieusement. C'est ça, le prototype incassable.

---

## 🔬 Le mécanisme « self-review ≠ check » (@hanakoxbt, intégré 07/08)

Relire son propre travail n'est PAS une vérification — c'est un **deuxième avis de la même source** : mêmes poids, même fenêtre, mêmes angles morts. Si la cause de l'erreur est quelque chose que le modèle ne sait pas, la review ne le sait pas non plus. (Recherche : Huang & co, DeepMind, ICLR 2024 — la self-correction intrinsèque n'aide pas de façon fiable.)

**L'accord n'est pas une preuve de détection** — un reviewer qui valide tout est d'accord avec la réalité la plupart du temps aussi. Ce qui compte, c'est ce qui se passe sur les cas **faux**.

### Les 3 règles opérationnelles
1. **Sortir le check du modèle** : un test qui tourne, un schéma qui valide, un exit code d'un truc qu'on n'a pas écrit. Pas plus malin que le modèle — juste **non corrélé avec lui**, et c'est toute la valeur.
2. **Famille différente** pour les jugements qui exigent un modèle (même famille = mêmes angles morts ; les juges frontier gonflent les scores des outputs qui ressemblent aux leurs). Ex : Gemini vérifie ce que Qwen a produit.
3. **Séparer par nature** : tout ce qui est objectivement vérifiable → au code ; les seuls appels sémantiques → au juge, avec **une rubrique écrite en une ligne**.

> « Une review dans la boucle te dit que le modèle est confiant. Un check hors de la boucle te dit si le travail est fait. »

Source : @hanakoxbt (07/08, Eval 2026-08-07_post_hanakoxbt_verification.md) — complète le principe fondateur (maker ≠ checker).

## Exemple déjà appliqué (06/08)

- Auditeur IA (Gemini) produit → Ada trie (triade de vérification : ✅ corrigé / 📝 accepté / ❌ rejeté).
- `cortana_analyse.py` : Ada spec + test → review attrape 4 bugs → corrigés → validé → commit.

---

[[CHANTIERS]] · [[OSSATURE_INDEX]] · [[PROTOCOLE_VALIDATION_TEST_AVANT_REEL]] · [[Cahier/22_COMPARAISON_ACE_8H_VS_HULK]] · [[MEMOIRE_COLLAB]]

## 🔧 Le flux « Garry Tan » (@dunik_7, intégré 07/08)

> Think → Plan → Build → Review → Test → Ship → Reflect — avec revues (CEO/eng/design) **avant d'écrire**.

| Étape | Chez nous |
|---|---|
| Think + Plan (revues avant d'écrire) | SPEC (Ada/chef) — contraintes + pièges connus |
| Build | PRODUCTION (agent) |
| Review + Test | REVIEW (code-reviewer + tests réels) |
| Ship | VALIDATION (Christophe) → commit |
| Reflect | 1 ligne leçon dans MEMOIRE_COLLAB |

Outils adaptés : `/freeze` (figer la spec), `/guard` (garde-fou explicite), `/qa` (tests), `/retro` (leçon).  
**Harness engineering (@undefinedKi, intégré 07/08) :** même modèle, même budget 53K tokens → 13,3 % → 38,3 % rien qu'en améliorant le **harnais**. Le levier n'est pas le modèle, c'est le harnais — valide notre routeur + notre délégation.

## 🔗 Connexions

- [[TRI_SIGNETS_LOTS_6_23]] — TRI_SIGNETS_LOTS_6_23
- [[CONTRAT_AUTOGESTION]] — CONTRAT_AUTOGESTION
- [[SNIFF_2026-08-07]] — SNIFF_2026-08-07
- [[PEPITES_EN_ATTENTE_2026-08-07]] — PEPITES_EN_ATTENTE_2026-08-07
