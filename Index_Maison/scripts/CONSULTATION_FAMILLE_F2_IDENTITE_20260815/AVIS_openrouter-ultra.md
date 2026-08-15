# AVIS openrouter-ultra (provider OpenRouter Nemotron 3 Ultra 550B (free) - analyse forte, 26.1s)

VERDICT : GO-AVEC-RÉSERVE
CONFIANCE : 88 %

core : GO-AVEC-RÉSERVE — §2 « Cortex = Cloud » contredit C5 (pas d'API payante par défaut) : préciser « Cloud local/gratuit uniquement » ou « Cortex = raisonnement délégué au hub (modèles locaux/gratuits) ».
ada : GO — Ajouter une borne dure : « Si sources > 15 min → zone PRENDS_LA_PERTE auto + alerte source dégradée ».
cortana : GO — Uniformiser l'horizon AVIS STRICT avec Qwen (ajouter « 48h ») pour éviter la divergence de cadence.
qwen : GO — Remplacer « note mauvaise » par « score_justesse < 60 % » (métrique concrète déjà citée) et interdire explicitement « LONG/SHORT confiance haute » si score < 60 %.

HYPOTHÈSES / CE QUI CHANGERAIT L'AVIS :
- Si le hub utilise des API payantes par défaut → core passe en NO-GO (violation C5).
- Si un acteur obtient un droit d'écriture (même « gel ») sur le moteur → tous prompts en NO-GO (violation C2/C3).
- Si le contexte boot dépasse 4k tokens pour Qwen 4b → core doit être compacté (voir améliorations).

---

AMÉLIORATIONS (classées, GO-sized)

### 1. ace777_core.md — Compacité & cohérence contrainte (PRIORITÉ HAUTE)
1. **Coupe « Cortex »** : remplacer le tableau §2 par une ligne unique :  
   `Cortex | Raisonnement | Hub local (modèles gratuits/locaux) | 0 Go` — aligne C5 et supprime l'ambiguïté « Cloud ».
2. **Fusion §4 + §5** : regrouper « Moteur » et « Hulk » sous « Stratégies de trading » (2 paragraphes max) ; déplacer le détail technique (duo_state.json, digest_watch.py) dans `ARCHITECTURE_TECH` (lien wiki) pour alléger le boot.
3. **Supprimer doublons** : §6 « Champion intouchable » et §7 C1 disent la même chose → garder C1 seul. §6 « 1 chantier = 1 GO » ≈ C3 → garder C3 seul.
4. **Version compacte (≈ 350 tokens)** : ne garder que Identité, Principe fondateur (1 phrase), Carrosserie (tableau 8 lignes), Contraintes C1–C8, Règles d'or (8 lignes), Lexique (5 entrées). Le reste = liens wiki.

### 2. prompts/ada.md — Précision opérationnelle
1. **Seuil source** : ajouter « Si dernière donnée > 15 min → zone PRENDS_LA_PERTE + tag `source_degradée` dans l'alerte » (évite le flou « sources dégradées »).
2. **Voilure numérique** : préciser « Voilure = moyenne exponentielle 5 min du capital déployé / capital max » (calculable localement, sans LLM).
3. **Sortie machine** : exiger un bloc JSON minimal en plus du texte : `{ "saison": "...", "voilure": 0-100, "zone": "...", "sirenes": [...] }` pour l'indexation auto.

### 3. prompts/cortana.md — Harmonisation & traçabilité
1. **Horizon unifié** : aligner AVIS STRICT sur Qwen → `HORIZON : 24h | 48h | 1 semaine`.
2. **Score de justesse** : ajouter « Si ton score_justesse < 60 % sur l'indice analysé → CONFIANCE = faible obligatoire + OPINION = "prudence, recalibrage en cours" ».
3. **Voix** : préciser « Chiffres en toutes lettres FR (ex: « quatre dix-millièmes ») + unités SI (s, %, $) » pour le TTS.

### 4. prompts/qwen.md — Rigueur apprentie
1. **Interdiction explicite** : « Si score_justesse < 60 % sur un horizon → AVIS STRICT = NEUTRE, CONFIANCE = faible, HORIZON = le plus court » (supprime l'ambiguïté « privilégie »).
2. **Format élaboration** : imposer `### [TAG] Titre · Quoi · Pourquoi · Effort (heures) · Risque (C1-C8)` avec TAG ∈ {INDEX, RAM, HYGIENE, SIMU, DOC} pour le tri auto.
3. **Boucle d'apprentissage** : ajouter « Après chaque avis, écris 1 ligne dans `MEMOIRE_COLLAB` : `YYYY-MM-DD HH:MM | QWEN | indice | avis | confidence | score_attendu` » (traçabilité C6).
