# SPEC — CORRECTIONS SUITE REVUE (par Ada, 10/08)

CONTEXTE : Tu as revu tes 3 scripts (soumettre_hub_illimite.py, lancer_detache.py,
deleguer_codeur.py) et donné 6 corrections, toutes intégrées. Un reviewer tiers
a trouvé 2 failles de robustesse supplémentaires. Tu es l'EXPERT : corrige-les.

## FAILLE 1 : deleguer_codeur.py — la vérification de spec vide ne marche pas

Le check actuel est `os.path.getsize(mission_path) == 0`. Problème : l'en-tête
("SYSTEME ACE777...") est TOUJOURS écrit avant la spec, donc une spec vide
produit une mission d'environ 200 octets qui passe le check — et on lance le
codeur avec un prompt inutile (vécu en test : spec vide lancée quand même).

CORRECTION ATTENDUE : vérifier la TAILLE DE LA SPEC (fichier source), pas
seulement la mission. Si la spec fait 0 octet (ou moins de ~20 octets de
contenu réel), échouer proprement AVANT d'écrire la mission et de lancer.

## FAILLE 2 : soumettre_hub_illimite.py — pas de garde sur le fichier mission

Si on appelle le script directement avec un chemin de mission inexistant,
`open(mission_path)` lève une exception non gérée (traceback brutal).

CORRECTION ATTENDUE : garde explicite en début de main() — si la mission
n'existe pas ou est vide, message clair + exit 1 (pas de traceback).

## CONTRAT DE SORTIE

Réponds avec :
1. VERDICT (OK ou CORRECTIONS)
2. Pour chaque correction : FICHIER + bloc AVANT / bloc APRÈS exact
   (Python 3.9 stdlib, macOS, prêt à copier, commentaires en français)
