# Avis gemini — AGORA (provider Google Gemini, 3.9s)

Avis du conseil d'architecture ACE777 sur le design AGORA (15/08/2026).

---

### Q1 : Boucle E4 (lecons HIT/MISS auto)
**Option (b) intégrée à la discipline 07h15**, avec un module interne `lecons_auto.py` appelé par le script de la routine matinale. Cadence : **Quotidienne** (immédiatement après le calcul du `score_justesse`). La centralisation au réveil évite la multiplication des crons désynchronisés.

### Q2 : Formatage d'une leçon actionnable pour Cortana
Le format doit être un **axiome décisionnel court (≤ 20 mots)** combinant la condition et la probabilité empirique, sans bruit statistique. 
*Exemple :* `[AXIOME_FUNDING] Funding positif extrême sans relais onchain = piège à acheteurs (Fiabilité : 7/20, taux d'erreur 65%).`
Pas de données brutes, uniquement des invariants comportementaux.

### Q3 : Cloisonnement Texte (Cortana) vs Chiffres (Ada)
Le design actuel est **sain mais nécessite un cloisonnement strict**. 
* Risque : Que Cortana interprète mal les nuances d'Ada ou que Ada subisse des biais narratifs.
* Règle : `CONNAISSANCE_PROJETS.json` doit séparer explicitement deux namespaces : `narratifs_cortana` (textes) et `parametres_ada` (seulement des floats/int validés). Ada ne lit jamais les fiches textuelles de Cortana ; elle consomme uniquement les variables injectées dans `live.json`.

### Q4 : Pérennité du JSON unique vs SQLite
**Le fichier JSON unique est valable pour le long terme (jusqu'à ~500 fiches)** grâce au mécanisme de péremption (30j/90j) et d'archive froide déjà prévus. SQLite est inutile ici : notre force est l'auditabilité textuelle directe par git. Pas de complexité superflue.

### Q5 : Mesure d'impact (AGORA)
Métrique : **Moyenne mobile à 7 jours du `score_justesse` de Cortana** comparée à la baseline historique sans AGORA. On valide l'A/B implicite en observant la pente du score après l'injection des leçons E4.

---

### VERDICT & SYNTHÈSE

* **VERDICT :** GO-AVEC-RÉSERVE (sous réserve du cloisonnement strict namespace texte/chiffres Q3).
* **CONFIANCE :** 91 %
* **HYPOTHÈSES :** 
  1. Le volume quotidien des leçons E4 reste gérable (< 5 nouvelles par jour grâce au filtrage).
  2. Le format court pré-mâché évite la surcharge cognitive de Cortana.
* **CE QUI CHANGERAIT L'AVIS :** Une dégradation mesurée de la justesse de Cortana liée à une pollution de son contexte par des leçons contradictoires.
* **AMÉLIORATION PROPOSÉE :** 
  1. Ajouter un champ `namespace: "cortana"` ou `"ada"` obligatoire dans le schéma JSON pour garantir l'étanchéité des sorties.
  2. Imposer un TTL court (7 jours) pour les leçons issues des HIT/MISS avant qu'elles ne soient validées en "règle structurelle".
