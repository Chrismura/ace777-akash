# CONFRONTATION DÉTAILLÉE — Notre Obsidian vs le système de l'expert (31/08/2026)

**Méthode Christophe** : « regarde dans les détails comment c'est organisé et copie
si c'est mieux ». Référence : Sébastien Dubois (guide « Obsidian Automation → AI
Operating System », vault 20 000 notes, 400 skills IA, ~50 types de notes).
Confrontation point par point, vérifiée sur NOS fichiers réels.

---

## 1. VERDICT GLOBAL PAR POINT (mesuré sur nos fichiers)

| # | Point | L'expert | Nous (mesuré) | Verdict |
|---|---|---|---|---|
| 1 | **Frontmatter / propriétés** | Registre de ~50 types de notes, chacun avec propriétés requises + types + valeurs autorisées + tags obligatoires | **0 frontmatter** sur nos 60 fiches Crypto_Projet (juste `---` vides), journaux avec tags inline seulement | ❌ **Eux nettement mieux → copier** |
| 2 | **Types de notes (schema)** | Note type = reconnaissance (tag/dossier/pattern) → dossier + template + propriétés automatiques | Aucun type défini : fiches nommées MAJUSCULES_SOULIGNÉ_DATE mais sans structure commune | ❌ **Eux mieux → copier (simplifié)** |
| 3 | **Templates** | TPL Dispatcher : un template racine reconnaît le type et applique le bon template (frontmatter, sections, dossier) | **0 template** configuré (plugin désactivé, aucun templates.json) | ❌ **Eux mieux → copier** |
| 4 | **État (state machine)** | Chaque type a des états (ex. article : idea → draft → done) ; le changement d'état déclenche des actions (déplacer, archiver, horodater) | Statuts ad hoc dans les tableaux du cockpit, non standardisés dans les fiches | ❌ **Eux mieux → copier (pour nos statuts : en_observation/tradé/delisté)** |
| 5 | **Sync (1 seul canal)** | « Use exactly ONE sync mechanism » — git + CLI, pas de double écriture | **3 mécanismes** : OUTBOX manuel (cp) + obsidian-git + CLI (nouveau) | ⚠️ **Eux mieux → notre plan A corrige** |
| 6 | **Liens entre notes** | Wikilinks partout (navigation, graphe, backlinks) | **0 wikilink** dans Crypto_Projet (0/60 fiches), 1341 notes orphelines | ❌ **Eux mieux → copier (liens actif ↔ synthèse)** |
| 7 | **Graphe** | Utilisé comme outil de navigation réel | Activé mais vide (orphelines) | ⚠️ Conséquence du #6 |
| 8 | **Query matérialisées** | « Un résultat qui n'existe qu'au rendu n'est pas dans tes fichiers » → Dataview Serializer écrit les résultats en Markdown réel | Nos tableaux cockpit sont des JSON → pas lisibles par les IA hors app | ⚠️ **Eux mieux → nos Bases + exports md** |
| 9 | **Daily notes / journal** | Note du jour = point d'entrée de tout, templates appliqués, navigation jour précédent/suivant | Plugin désactivé ; journaux dispersés (Cahier/, Index_Maison/...) avec formats différents | ❌ **Eux mieux → copier (daily notes + template)** |
| 10 | **Backup** | Git sous tout + file recovery + snapshot avant opérations risquées | obsidian-git ✅ + file recovery ✅ (déjà bien) | ✅ **Pareil, on est bons** |
| 11 | **Fichiers = API** | Tout est texte brut → grep, git, scripts, IA travaillent dessus | ✅ Même principe (on vit dedans) | ✅ **Pareil** |
| 12 | **Outils de base** | Templater + Linter (formatage auto) + filing automatique = « 80% de la friction » | Aucun des 3 | ❌ **Eux mieux → copier (Templater + Linter)** |
| 13 | **Traçabilité des agents** | Agents laissent une trace visible (commande exécutée, fichier modifié) | Pont CLI a l'audit ✅ ; les autres scripts écrivent sans audit | ⚠️ **Mi-chemin → généraliser l'audit** |

## 2. CE QU'ON A DE MIEUX QUE LUI (à garder, pas copier)
- **Notre stack IA est plus riche** : famille (6 modèles), Cortana, short BTC,
  satellite aspiration, machine divergence — lui a des skills, nous avons des
  agents opérationnels.
- **Git maison + journal** : nous journalisons chaque action (JOURNAL_ACE777.md)
  — lui automatise plus, nous documentons plus.
- **Pont CLI avec fail-open + circuit breaker** : notre pont (audit, queue,
  fallback disque) est déjà « bulletproof » — mieux que le wrapper simple qu'il
  décrit.

## 3. CE QU'ON COPIE (les 5 changements concrets, dans l'ordre)
1. **Frontmatter uniforme sur les fiches** (statut, actif, date, source, tags) —
   la base de tout (chantier B).
2. **Types de notes simplifiés** : 4-5 types au lieu de 50 (fiche_actif,
   synthèse_consultation, veille, journal, signet) — chacun avec template +
   propriétés + dossier.
3. **Templates** : un modèle par type, appliqué par nos agents via le pont CLI
   (`create template=...`).
4. **Daily notes** : activer le plugin + template → journal central des agents.
5. **Wikilinks** : chaque fiche actif lie sa synthèse, son événement, son signet →
   le graphe se remplit.

## 4. LA RÈGLE D'OR QU'IL RAPPELLE (et qu'on adopte)
« Make the structure machine-readable. Conventions in your head do not automate. »
→ Nos conventions doivent devenir des fichiers (templates, registre de types,
propriétés) que les IA peuvent lire et respecter.
