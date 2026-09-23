# AVIS nvidia/nemotron-3-super-120b-a12b:free (provider Google Gemini, 9.5s)

1. **Conclusion abusive au vu des chiffres fournis** : 
La conclusion n°1 (affirmant que le cap de mise se lit sur un profil figé induisant une erreur sur RIZE : 4,88 $ sur 243,78 $ vs carnet à 364,74 $) est abusive. Les chiffres GO1 montrent que 16/17 profils mesurés dérivent et que le prix du profil est faux jusqu'à 81,72 % sur RIZE, mais **aucune corrélation mesurée** ne prouve formellement que cette dérive du profil fausse directement le calcul du cap de mise (le $). C'est une extrapolation logique, pas un fait mesuré.

2. **Mesure manquante pour trancher** : 
Pour trancher, il manque la mesure exacte de la **profondeur réelle du carnet d'ordres au moment précis de l'exécution de l'ordre paper** (et non une vue live à l'instant du contrôle ou un profil figé), croisée avec le calcul exact de la taille de mise exécutée par le moteur.

3. **Le retard d'horodatage et les post-mortems** : 
C'est une explication **plausible**. Les faits n°2 le prouvent : 13/13 prix fautifs retrouvés dans une minute antérieure (décalage -1 à -5 minutes), 0 prix fantôme. 
*Test pour trancher sur Mac sans argent réel* : Lancer un rejeu hors-ligne (backtest déterministe) en injectant les flux MEXC bruts avec journalisation à la microseconde (timestamp système local vs timestamp payload MEXC) pour mesurer l'écart systématique entre l'heure de réception de la donnée et l'heure d'écriture dans le journal.

4. **Erreur de méthode commise MAINTENANT** : 
Tu commets une **erreur d'auto-absolution par la confession** (biais de transparence). En listant tes erreurs passées (E10, E13, E12) dès le début du brief, tu t'octroies un brevet d'objectivité et d'infaillibilité pour les conclusions que tu tires ensuite, en oubliant de soumettre tes propres affirmations de la section 3 au même filtre rigoureux que celui appliqué au moteur (pas de garde-fou `verif_seuil_moteur.py` pour tes propres déductions).

5. **Ordre de traitement des chantiers** :
*   **(b) Horodatage du journal** : En premier. Si l'heure est fausse, toutes les séquences temporelles, post-mortems et corrélations de prix sont caducs. On ne peut pas analyser des données dont on ne maîtrise pas la chronologie.
*   **(e) Net de coûts dans le reporting** : Ensuite. Correction immédiate de la formule du PnL (intégrer frais et spread) pour cesser de piloter avec un chiffre brut faux de 8,8 %.
*   **(c) Stop au repos** : Puis. Comprendre le risque de slippage extrême (−39,2 %) inhérent à la vérification périodique.
*   **(d) Colonnes manquantes** : Ensuite. Injecter les 6 colonnes pour rendre traçables les décisions du moteur.
*   **(a) Vue live sur les 20 paires** : En dernier. Nécessaire pour l'affinage, mais secondaire tant que la base temporelle et financière (b et e) fausse l'historique.

6. **Ce qui ferait changer d'avis (fait mesurable)** : 
La démonstration par un rejeu complet avec les 6 colonnes manquantes et l'horodatage corrigé que le PnL net reste stable et positif malgré le retard de prix et les dépassements de stop.

---

**VERDICT** : utile mais incomplet
**CONFIANCE** : 75 %
**HYPOTHÈSES** : 
1. Le cache de cycle `last_price` est la cause racine du décalage d'horodatage de 1 à 5 minutes.
2. L'absence des 6 colonnes dans le journal masque la vraie nature des dépassements de stop.
**CE QUI CHANGERAIT L'AVIS** : L'ajout des 6 colonnes manquantes dans le journal et la preuve par rejeu que le PnL net reste rentable après correction des frais et du spread.
**AMÉLIORATION PROPOSÉE** : 
1. Imposer un script de validation automatique (type `verif_seuil_moteur.py`) pour chaque nouveau rapport généré par Buffy.
2. Synchroniser l'horodatage du journal sur le timestamp d'entrée de la donnée MEXC et non sur l'écriture du cache.
**SYNTHÈSE** : 
L'audit de Buffy met en lumière des dérives techniques majeures (prix du profil faux, retards d'horodatage de 1 à 5 min, PnL brut non fiscalisé par les frais, et stops en cache glissants jusqu'à -39 %). Bien que rigoureux sur l'extraction des chiffres, il pèche par quelques extrapolations non mesurées. L'urgence absolue est de corriger l'horodatage et d'intégrer les coûts réels dans le PnL avant de juger la viabilité des set-ups.
