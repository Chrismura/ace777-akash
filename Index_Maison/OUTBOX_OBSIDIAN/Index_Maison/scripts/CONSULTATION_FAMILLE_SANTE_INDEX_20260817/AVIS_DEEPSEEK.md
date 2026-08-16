# AVIS DEEPSEEK (task deepseek.analyse, provider NVIDIA build.nvidia.com (100+ modeles), 148.4s)

**VERDICT : GO-AVEC-RÉSERVES**  
**CONFIANCE : 78%**  

---

### 1. VERDICT sur le pré-vol  
Le concept est solide : vérifier la **traversée de la donnée** (maillon par maillon) plutôt que la seule fraîcheur des fichiers est une vraie correction du problème identifié. La plist 5 min est raisonnable pour un pré-vol.  

**Réserves :**  
- Le cockpit 🟢/🔴 est un **état instantané** — sans historique, impossible de distinguer une panne transitoire d'une panne durable.  
- La vérification « donnée présente chez le consommateur » dépend de la **définition de "présente"** : un fichier vide mais frais est-il vert ? (cf. point 3).  

---

### 2. LES 6 CHAÎNES — analyse critique  
| Chaîne | Verdict | Commentaire |  
|--------|---------|-------------|  
| BALEINES | ✅ OK | La plus critique (le bug initial). Bien couverte. |  
| HULK | ⚠️ Réservé | « CSV aspiration » — si le CSV est vide mais frais, c'est vert ? Seuil d'âge ? |  
| LIVE | ✅ OK | Thermo→mission→cockpit, cohérent. |  
| CPFP | ⚠️ Réservé | « Observation 7j » — un marché calme peut produire un fichier vide mais frais → faux positif. |  
| SÉCURITÉ | ✅ OK | Veilleuse elle-même, logique. |  
| SAISON | ⚠️ Réservé | 6 indices — lesquels ? Si un indice est saisonnier (ex. été), il sera rouge hors saison → faux positif. |  

**Chaînes manquantes :**  
- **Hub LLM** (si utilisé pour Ada/Cortana) — non couvert.  
- **Git push auto** — si le code n'est pas poussé, le scan tourne mais rien n'est déployé.  
- **Discipline quotidienne** — non automatisable, mais un indicateur « dernier commit humain » serait utile.  

---

### 3. FAUX POSITIFS / FAUX NÉGATIFS  
**Faux positifs (crier à tort) :**  
- Fichier append-only vide sur marché calme (CPFP, SAISON).  
- Process avec un label différent (ex. `python3 scan.py` vs `scan.py`) → rouge alors que tout fonctionne.  
- Seuil d'âge trop strict (ex. 5 min sur un scan qui prend 10 min en pic).  

**Faux négatifs (rater) :**  
- Donnée présente mais **périmée** (fichier frais, contenu vieux de 2 jours).  
- Process vivant mais **déconnecté** (socket ouvert, mais plus de données entrantes).  
- **Chaîne non couverte** (hub LLM, git push).  

---

### 4. ALERTE VOCALE — pertinence et escalade  
**Pertinente ?** Oui, mais **pas en première ligne**. Une voix qui crie pour un maillon transitoire (ex. process redémarré) créera une accoutumance.  

**Escalade proposée :**  
1. **Log** (toujours) — écriture systématique.  
2. **Carte rouge** (après 2 cycles consécutifs, ~10 min) — visible mais non intrusive.  
3. **Voix** (après 3 cycles, ~15 min) — uniquement si la chaîne est critique (BALEINES, SÉCURITÉ).  
4. **Escalade humaine** (après 30 min) — notification à un humain (pas la voix).  

---

### 5. AMÉLIORATION PROPOSÉE (clause permanente)  
**Une idée concrète :** ajouter un **champ `last_content_hash`** dans chaque maillon.  
- Au lieu de vérifier seulement `mtime` (fraîcheur), comparer le **hash du contenu** entre le maillon amont et aval.  
- Si le hash est identique mais le fichier est vieux → **donnée périmée** (faux négatif actuel).  
- Si le hash diffère mais le fichier est frais → **donnée qui circule** (vrai positif).  
- Coût : un md5 par fichier, déjà utilisé par la veilleuse.  

---

### HYPOTHÈSES  
1. Les 6 chaînes couvrent l'essentiel du flux de production actuel (hors hub LLM et git push).  
2. La plist 5 min est suffisante pour détecter une panne sans surcharger le système.  
3. Le cockpit est consulté par un humain au moins une fois par quart de travail.  

---

### CE QUI CHANGERAIT L'AVIS  
- **Preuve d'un faux négatif** : un cas où une chaîne est verte mais la donnée ne traverse pas (ex. fichier frais mais vide).  
- **Preuve d'un faux positif** : un cas où une chaîne est rouge mais tout fonctionne (ex. process label différent).  
- **Ajout d'une chaîne critique manquante** (hub LLM, git push) qui rendrait le pré-vol incomplet.  

---

### SYNTHÈSE  
GO avec réserves : le concept maillon-par-maillon est juste, mais les seuils d'âge et la définition de « donnée présente » doivent être précisés pour éviter faux positifs/négatifs. L'alerte vocale doit être escaladée (log → carte → voix) pour éviter la sur-alerte. Manque : hub LLM et git push. Amélioration clé : hash de contenu pour détecter la péremption.
