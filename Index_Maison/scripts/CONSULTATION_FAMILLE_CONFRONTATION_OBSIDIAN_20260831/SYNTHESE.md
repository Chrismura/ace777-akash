# SYNTHÈSE — Famille (3/3) : confrontation Obsidian expert (31/08)

**Avis reçus** : gemini, juge, deepseek — 3/3. Verdict global : le plan est
« correct dans l'intention mais naïf dans l'exécution » (juge), « courageux mais
ignore la discipline de code » (gemini 6.5/10, juge 6/10).

## 1. LA CONFRONTATION EST VALIDÉE — ET C'EST PIRE QUE DÉCRIT
Les 3 confirment le diagnostic (0 frontmatter, 0 wikilink, 1341 orphelines =
77% du vault) mais le qualifient plus durement : « cimetière de données » (juge),
« dump de fichiers markdown brut » (deepseek), « les agents écrivent dans le
vide » (juge). **Et ils pointent notre angle mort** : « vous n'avez pas un
problème d'Obsidian, vous avez un problème d'ingestion de données générées par
des agents » (deepseek). Le pont CLI transporte les octets mais est « aveugle sur
le contenu » (gemini).

## 2. CE QU'ON NE COPIE PAS (unanimité 3/3 — contre l'expert)
- **50 types de notes** → on garde **4-5 max** (actif, signal/trade, synthèse_ia,
  veille, journal). Au-delà, les IA hallucinent le type.
- **State machines complexes** (idea→draft→done) → inutile en trading : états
  binaires suffisent (actif/inactif, long/short, traité/ignoré, validé/archivé).
- **Dogme « toutes les requêtes doivent produire du Markdown réel »** → NON pour
  nous : les Bases dynamiques (tableaux de bord) sont légitimes, le trader veut
  l'info fraîche, pas 1000 notes de synthèse statiques qui pourrissent le vault.
- **Plugins GUI lourds / Linter visuel** → notre interface c'est la CLI + md pur.

## 3. LA CORRECTION MAJEURE (3/3, identique chez les trois) : le GATEKEEPER
**Le pont CLI doit valider le contenu AVANT d'écrire, pas après.**
- « C'est la machine qui éduque vos IA, pas l'inverse » (gemini)
- Aucun agent n'écrit un .md brut : il génère un **objet JSON structuré**
  (type + frontmatter validé + corps), le pont **compile** en markdown conforme
  au template et le valide contre un **schéma** (type requis, propriétés
  obligatoires) → rejet 400 si non conforme.
- C'est le « contrat d'interface API-first » (juge) / « schéma d'entrée unique »
  (deepseek).

## 4. LES AUTRES CORRECTIONS (unanimité)
1. **Day Zero rule** : ne PAS migrer les 1733 notes existantes (les archives
   mortes restent) → le nouveau standard s'applique **uniquement aux nouvelles
   créations**. Migration progressive seulement si le nouveau tourne sans
   intervention (juge : semaine 1 templates+daily nouveaux flux, semaine 2 types,
   semaine 3 nettoyage).
2. **Séquencer, pas tout d'un coup** : risquer de casser les ~15 scripts
   d'écriture = crash en boucle des agents.
3. **Daily notes = priorité absolue sous-estimée** (gemini) : le meilleur ROI,
   journal central lisible en un bloc par les LLM.
4. **Wikilinks ne se feront pas tout seuls** : nécessite des consignes strictes
   de nommage/résolution, sinon liens cassés en chaîne (juge).

## 5. DÉCISION BUFFY (chef scientifique)
J'adopte les corrections :
- **4 types stricts** : actif, signal, synthese_ia, journal (+ signet existant).
- **Gatekeeper dans le pont** : `write_note` accepte un dict structuré
  {type, frontmatter, body}, valide contre le schéma du type, compile le markdown.
- **Day Zero** : les nouvelles écritures passent par le pont avec schéma ; les
  anciennes fiches ne sont pas touchées (on les traitera si besoin après).
- **Daily notes d'abord** (le ROI max), puis types, puis wikilinks.
- **Bases pour les tableaux de bord** (pas de matérialisation forcée).
