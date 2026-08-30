# AVIS JUGE (task juge.tranche · Google Gemini · 2026-08-27T19:19Z)

VERDICT : GO-AVEC-RÉSERVES
CONFIANCE : 90 %
HYPOTHÈSES :
1. Le 3e écrivain utilise une méthode d'écriture directe ou un remplacement aveugle du fichier au lieu d'une fusion (merge) récursive des dictionnaires existants.
2. Les 36 lecteurs tolèrent un fichier temporaire renommé atomiquement (`os.replace`).

CE QUI CHANGERAIT L'AVIS :
La découverte d'un verrou global `fcntl` déjà actif sur le 3e écrivain, prouvant que le problème vient d'une réinitialisation volontaire du dictionnaire source et non d'une concurrence d'écriture.

AMÉLIORATION PROPOSÉE :
1. **Approche par Fragments Atomiques (Architecture Alternative) :** Remplacer l'unique fichier `live.json` cible par un dossier `thermo/registry/` où chaque module (thermo complet, onchain, 11-clés) écrit son propre fragment (`thermo.json`, `onchain.json`, `subset.json`) de manière isolée. Un lecteur/générateur unique assemble à la volée le payload global en mémoire pour les 36 lecteurs.
2. **Fonction de Merge Stricte + Verrou `fcntl` :** Si l'on conserve un fichier unique, interdire formellement toute écriture brute. Imposer une fonction centrale `atomic_patch(section_key, data)` qui lit le fichier, met à jour *uniquement* la sous-clé concernée (ex: `data['onchain'] = ...`) tout en préservant le reste, le tout protégé par un verrou inter-processus `fcntl.flock`.

SYNTHÈSE :
La perte des 53 clés le 27/08 confirme l'échec de la cohabitation des écrivains partiels sur un fichier unique. Le fix structurel impose soit un découplage par fragments de fichiers isolés (le plus robuste), soit une fonction de fusion protégée par un verrou strict empêchant tout écrasement aveugle du payload global.
