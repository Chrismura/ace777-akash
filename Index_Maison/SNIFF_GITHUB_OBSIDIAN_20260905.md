# SNIFFER DU VRAI — GitHub · Améliorations Obsidian + cockpit + apprentissage — 2026-09-05

> Mission : envoyer le sniffer sur GitHub chercher des améliorations pour l'écosystème
> (Obsidian, cockpit, interaction, apprentissage), soumettre à la famille via le hub
> avec le prompt sniffer + clause famille.
> Provider : Google Gemini (hub, task analyse.profonde) · Budget restant 388/624.

---

## FAITS BRUTS (état réel mesuré)

- Coffre Obsidian ~3 438 notes ; purgé aujourd'hui : 1 596 archives miroirs + 94 doublons.
  Il reste 28-30 liens cassés **expliqués** (dossiers exclus volontaires + artefacts).
- Cause racine du merdier : **DEUX ponts écrivaient dans le coffre** (obsidian_writer.py V2
  + _sync_now.sh V1 jamais débranché) → doublons + graph pollué. Corrigé (P0-P3).
- Push GitHub mort 3 jours : `croisement_contexte.jsonl` (286 Mo, croissance illimitée)
  commité par l'auto-sync → GitHub refuse >100 Mo. Corrigé (retiré du suivi + .gitignore).
- `journal_intention.jsonl` (29 Mo) : prochain fichier à croissance illimitée.
- DIGEST log : rotation faite (6,8 Go libérés).
- Cortana : score_justesse jugé stagnant ; boucles d'apprentissage à vérifier.
- Hub : 12 providers, réseau instable (alpage, groupe électrogène, MacBook Air).
- Architecture : Index_Maison = vérité · OUTBOX → obsidian_writer (5 min) · _sync_now
  restreint aux fichiers vivants · git coffre = agent com.ace777.gitpush-vault ·
  cockpit = serveur statique 127.0.0.1:17800.

## PÉPITES GITHUB — classement famille

| # | Pépite | Verdict | Pourquoi |
|---|--------|---------|----------|
| 1 | Vinzent03/find-unlinked-files (orphelins + liens cassés) | **SOFT** | Utile, mais nos liens restants sont documentés (exclusions volontaires). Pas de plugin lourd permanent. |
| 2 | ipshing/obsidian-broken-links | **SOFT** | Analyse fine headings/blocs ; notre priorité = stabilité pipeline, pas micro-nettoyage. |
| 3 | sarwarkaiser/obsidian-broken-links-cleaner | **BULLSHIT** | Nettoyage auto des wikilinks = risque de casser la structure de l'Index. L'humain garde le contrôle. |
| 4 | Vinzent03/obsidian-git (backup git dans Obsidian) | **BULLSHIT** | Dette : on a déjà l'agent com.ace777.gitpush-vault. Un 2e git en fond sur ligne instable = conflits. |
| 5 | promptfoo (CLI d'évaluation LLM, self-hosted) | **PERTINENT** | Idéal pour auditer le score_justesse stagnant de Cortana, sans SaaS ni alourdissement. |
| 6 | Git pre-commit hooks (check-added-large-files) | **PERTINENT** | Réponse chirurgicale au plantage de 3 jours (fichier 286 Mo). Bloque en amont tout commit >50 Mo. |
| 7 | Local RAG / mémoire agents (LightRAG, Obsidian Mind) | **BULLSHIT** | Violation règle OSSATURE : 1 GO à la fois, pas de RAG+agents en plus des 12 providers. |

## DIVERGENCE(S)

Le narratif communautaire pousse vers l'autonomie via des **plugins graphiques Obsidian**
(git, liens, mémoire RAG). Pourquoi ça ne s'applique pas : sur MacBook Air/alpage avec un
seul écrivain légitime (obsidian_writer.py), multiplier les plugins d'arrière-plan ou les
surcouches RAG recrée exactement le merdier qu'on vient de purger (doublons, conflits
d'écriture, gros fichiers non maîtrisés). Notre force = pilotage par scripts locaux stricts.

## TOP 3 IMPLANTABLES (ordre de valeur) — RÉALISATION 05/09 soir

1. **Git pre-commit hook (>50 Mo)** ✅ FAIT — `Index_Maison/scripts/git_precommit_large_files.sh`,
   symlinké dans `.git/hooks/pre-commit` du coffre ET du projet. Testé : fichier 60 Mo REFUSÉ
   (rc=1), petit fichier passe (rc=0). Bug v1 corrigé (exit dans un pipe = sous-shell → le refus
   ne remontait pas à git) : boucle via process substitution `< <(...)`. Aucun commit de test
   resté (soft reset + HEAD propre, origin/main intact).
2. **Rotation automatique des JSONL à croissance illimitée** ✅ FAIT —
   `Index_Maison/scripts/rotation_jsonl.py` (COPYTRUNCATE + gzip, seuils par fichier :
   croisement_contexte 100 Mo, autres 50 Mo). Testé réel : `croisement_contexte.jsonl`
   315 841 378 o → 0 + archive `.1.gz` de 4,8 Mo, écrivain vivant vérifié (le fichier regrossit).
   Branché dans `superviseur_core.sh` (check_rotation, 6 h) — pas de nouvel agent.
3. **Éval prompts Cortana** ✅ FAIT (décision terrain) — promptfoo installé ? NON : npm a
   téléchargé **1,7 Go sans finir en 17 min** sur la ligne de l'alpage (21:25-21:42) → dette
   interdite par la famille. Remplacé par **`Index_Maison/scripts/eval_cortana_prompt.py`**
   (stdlib pur, zéro dépendance) : envoie le prompt canon `cortana.md` à Ollama local
   (qwen2.5-coder:1.5b, zéro budget) ou au hub (`--hub`), vérifie les sorties obligatoires
   (AVIS STRICT LONG/SHORT/NEUTRE · HORIZON 24h/48h/1 semaine · CONFIANCE haute/moyenne/faible ·
   aucun verbe d'ordre · score<60% → CONFIANCE faible). Testé : modèle local 1,5b = ÉCHEC détecté
   (codeur, pas de structure) ; hub (Gemini, vrai cerveau Cortana) = PASS ✅.

## VERDICT FINAL

- **STATUT : GO-AVEC-RÉSERVES (exécuté)**
- **CONFIANCE : 90/100**
- Réserves tenues : rien d'autre installé ; 1 seul écrivain dans le coffre ; les 3 pièces sont
  locales, légères, sans nouvel agent ni SaaS.