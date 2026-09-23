CONTEXTE — Buffy, superviseur du prototype ACE777/HULK (trader PAPER sur MEXC, 0 € réel).
Mission demandée par Christophe : « compare les données MEXC une par une avec celles de Hulk,
compare chaque séquence de trading, vérifie ce qu'on mémorise, rejoue tout avec les derniers
set-up, puis CONTESTE cet audit avec les erreurs que tu as commises. »

=== 1. CE QUI A ÉTÉ MESURÉ (chiffres extraits des rapports d'instruments, pas de mémoire) ===
- GO1 : 20 paires moteur · 17 profils · 7 vues live à l'instant du contrôle (âge 6.7 s).
- GO1 : 17 trous de données nommés (dont 4 paires sans profil, 13 sans vue live).
- GO1 : anomalies au-delà des seuils de lecture : 0.
- GO1 : le `prix` du profil est faux jusqu'à 81.72 % (RIZEUSDT) ; 16/17 profils mesurés dérivent.
- GO2 : 124 séquences reconstruites (115 fermées, 9 ouvertes) · 1 anomalie(s) de reconstruction.
- GO2 : vérification MEXC sur 100 séquences → 78 conformes · 22 prix hors minute · 15 non vérifiables (budget).
- GO2 : brut inscrit 39.7 $ · coûts estimés 3.51 $ · NET 36.19 $.
- GO2 : formule du journal = pnl = (price - entry) * sell_qty  → BRUT, sans frais ni spread
- GO2 motif « stop/guard » : n=32 brut -33.73 $ net -34.87 $ giveback méd 8.91 %.
- GO2 motif « autre » : n=1 brut 0.0 $ net -0.05 $ giveback méd 0.0 %.
- GO2 motif « trailing » : n=67 brut 73.43 $ net 71.11 $ giveback méd 2.54 %.
- GO2/horodatage : 13 prix fautifs · 13 retrouvés dans une AUTRE minute · 0 introuvables dans ±6 min.
- GO2/horodatage : distribution des décalages (minutes) {'-5': 3, '-4': 1, '-2': 5, '-1': 4} → verdict « A. RETARD D'HORODATAGE (le prix est vrai, l'heure est fausse) ».
- GO3 : couverture — 24 trous ; journal 76153 lignes.
- GO3 cohérence : horodatages désordonnés 0 · discontinuités pnl_total 0 · doublons trading 0 · SKIP répétés 559.
- GO3 : spread présent dans le TEXTE de 99.4 % des ventes (pas une colonne, absent à l'entrée).
- GO3 : 6 colonnes manquantes nommées : mise_visee, mur_utilise, seuil_exige, dd6_observe, stop_nominal, spread_paye.
- GO3 re-injection : 30 sorties de stop → réalisé -2.68 $ vs stop nominal (négatif = MIEUX que le nominal), avec des cas extrêmes à −16,5 % et −39,2 % pour un stop annoncé de 8 %.

=== 2. MES ERREURS, NOMMÉES (elles sont enregistrées dans un registre, classes E1→E13) ===
- E10 : j'ai publié pendant TROIS JOURS un seuil d'entrée recalculé de tête (5-12,75 %) alors que
  le moteur appliquait 21,70 %. Le terme dominant (`dip = max(dip_pct ; 0,50 × cadence)`) manquait.
  Ce chiffre faux a servi à publier « RIZE structurellement inattaquable » et à chiffrer un levier.
- E13 : j'ai daté 4 lignes de la mémoire collaborative DE TÊTE (10:40Z au lieu de 09:47Z, etc.),
  soit des lignes dans le futur. Le temps traité comme un seuil : estimé ≠ vérifié.
- E12 : j'ai scellé des fichiers PUIS je les ai modifiés — la veilleuse a crié trois fois, à raison.
- Corrigé aujourd'hui dans mon propre audit : j'avais écrit « le stop ne tient pas (14,16 % réalisés
  pour 8 % annoncés) » — c'était une perte AGRÉGÉE de séquence, pas le niveau touché ; et
  « le spread n'est pas mémorisé » — faux, il est dans le texte des ventes à 99 %.
- Méthode : « un chiffre recalculé n'est pas un chiffre vérifié » ; tout seuil recalculé doit être
  confronté à ce que le moteur ÉCRIT (garde-fou `verif_seuil_moteur.py`, 6/6 conformes, autotest 7/7).

=== 3. CE QUE J'EN CONCLUS (et que je vous demande de DÉMOLIR si c'est abusif) ===
1. 13/20 paires n'ont aucune vue live → le cap de mise se lit sur un profil figé (RIZE : 4,88 $
   calculé sur 243,78 $ alors que le carnet mesuré vaut 364,74 $) ; 4 paires n'ont aucun profil.
2. Le prix de remplissage paper a 1 à 5 minutes de retard (13/13 des prix fautifs existent dans une
   minute ANTÉRIEURE, aucun prix fantôme) → tous nos post-mortems alignés sur l'heure du journal
   sont décalés ; le mécanisme exact (cache de cycle `last_price` vs photo d'aspiration, satellite
   limité à 5 paires par passe) est OPEN.
3. Le PnL inscrit est BRUT (pas de frais ni de spread) : −3,51 $ de coûts sur 39,70 $ (8,8 %).
4. 32 sorties de stop coûtent 33,73 $ contre +73,43 $ pour 67 traînîngs ; le stop est une
   VÉRIFICATION périodique sur un prix en cache, pas un ordre au repos → dépassements jusqu'à
   −16,5 % et −39,2 % pour un stop annoncé de 8 %.
5. Aucun bag utilisé sur la fenêtre ; giveback médian RIZE 20,8 % ; 6 colonnes manquent au journal
   (mise visée, mur utilisé, seuil exigé, dd6 observé, stop nominal, spread payé).
6. La mise médiane représente de 0,03 % (CHIP) à 13,2 % (TEL) de la profondeur mesurée à −0,5 %.

=== 4. MISSION : CONTREDIRE ===
Répondez à ces questions, dans l'ordre, en étant factuel :
1. Quelle conclusion de la section 3 est ABUSIVE au vu des seuls chiffres fournis ? (mesure
   insuffisante, corrélation prise pour causalité, n trop faible, fenêtre haussière…)
2. Quelle mesure MANQUE pour trancher la plus importante des cinq ?
3. Le retard d'horodatage (fait n°2) est-il une explication PLAUSIBLE des « contradictions » que je
   traquais (post-mortems incohérents), ou est-ce que je me raconte une histoire ? Quel test
   trancherait, réalisable sur un Mac, sans argent réel ?
4. QUELLE ERREUR de méthode suis-je en train de commettre MAINTENANT, que ce brief ne dit pas ?
5. Dans quel ORDRE traiter : (a) vue live sur les 20 paires, (b) horodatage du journal,
   (c) stop au repos, (d) colonnes manquantes, (e) net de coûts dans le reporting ? Et pourquoi ?
6. Qu'est-ce qui vous ferait changer d'avis (fait mesurable) ?

Puis, en fin de réponse :
  VERDICT : sur cet audit (fiable | utile mais incomplet | non fiable)
  CONFIANCE : 0-100 %
  HYPOTHÈSES : 2-3
  CE QUI CHANGERAIT L'AVIS : fait(s) mesurable(s)
  AMÉLIORATION PROPOSÉE : 1-3 idées concrètes (ou « aucune »)
  SYNTHÈSE (5 lignes max).

Factuel, concis, français. Pas de flagornerie, pas de généralités. Information manquante ->
« information insuffisante ». Vous DONNEZ UN AVIS : vous ne touchez à RIEN, aucun ordre.
