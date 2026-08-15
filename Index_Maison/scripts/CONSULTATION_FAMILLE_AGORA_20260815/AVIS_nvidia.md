# Avis nvidia — AGORA (provider NVIDIA build.nvidia.com (100+ modeles), 108.4s)

**VERDICT : GO-AVEC-RÉSERVE**  
**CONFIANCE : 82 %**

---

**ANALYSE FACTUELLE**

**Points forts du design :**
- E4 est la pièce manquante du cycle : sans réinjection des HIT/MISS, la connaissance stagne. C'est le seul levier qui transforme l'erreur en actif.
- Le cloisonnement texte/valeurs (S1/S2) est sain : Cortana raisonne, Ada calcule. Les natures sont différentes, le risque de contamination est réel mais gérable.
- La légèreté (JSON + stdlib) est un avantage tactique : zéro dette technique, zéro dépendance. À 100 fiches, un JSON reste performant (lecture < 10 ms).

**Réserves :**
- Q1 : un script dédié `lecons_auto.py` est plus propre que d'alourdir la discipline 07h15. Mais il doit être déclenché APRÈS la note de Cortana, pas avant.
- Q2 : le format « 7/20 juste » est trop brut. Il faut une synthèse qualitative : « funding positif : signal faible, corroborer avec fearGreed ».
- Q3 : risque de biais réel si les leçons de Cortana (texte) sont traduites en chiffres pour Ada. Cloisonnement strict : Ada ne lit QUE les verdicts famille validés, jamais les leçons de Cortana.

---

**HYPOTHÈSES :**
1. La justesse de Cortana est mesurée de façon fiable (score_justesse) — sinon E4 est du bruit.
2. Les leçons HIT/MISS sont stables dans le temps (pas de sur-apprentissage sur 2 semaines).
3. Ada n'a pas besoin des leçons de Cortana pour ses modulateurs — ses seuils viennent des audits famille.

---

**CE QUI CHANGERAIT L'AVIS :**
- Si la justesse de Cortana est < 40 % sur 30 jours → E4 amplifierait du bruit → NO-GO.
- Si les leçons de Cortana modifient les modulateurs d'Ada (fuite) → cloisonnement cassé → NO-GO.
- Si le JSON dépasse 5 Mo ou 500 fiches → performance dégradée → basculer SQLite.

---

**AMÉLIORATIONS PROPOSÉES :**
1. **E4 en deux temps** : `lecons_auto.py` écrit dans un fichier STAGING (lecons_brutes.json), puis la discipline 07h15 valide et fusionne dans la base. Évite d'injecter du bruit non relu.
2. **Format de leçon actionnable** : « [indice] → [constat] → [action recommandée] » (ex. « funding → positif mais 7/20 juste → corroborer avec fearGreed avant LONG »). Pas de chiffres bruts dans la fiche injectée.
3. **Métrique A/B simple** : comparer justesse de Cortana sur 30 jours AVANT vs APRÈS activation E4, sur le même périmètre d'indices. Pas besoin de sophistiquer.
