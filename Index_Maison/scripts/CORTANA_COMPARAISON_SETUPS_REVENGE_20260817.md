# Réponse Cortana — comparaison setups revenge (provider Google Gemini, 5.8s)

FAITS — Le setup gagnant (13-14/08) envoie le Hunter en mode `hunter_revenge_1.5x` malgré les hésitations du radar, encaissant jusqu'à +5.99 USDT. Le setup de la nuit (16-17/08), plombé par le correctif `FIX-LAST-LOSS`, affiche zéro fill ALPHA et une cascade de 46 blocs `revenge_ttl_expired`, stérilisant le PnL.

LECTURE PHYSIQUE — Le marché est un signal ondulatoire non stationnaire : le setup gagnant acceptait la résonance du choc (Fourier, `shock_inversion_stop`) en forçant l'entrée au-delà du bruit de fond. Le fix de la nuit a introduit un métronome rigide (un TTL de 120 secondes) dans un espace de phase chaotique, créant une décohérence fatale entre le temps de l'algorithme et la cadence réelle du prix.

INTERPRÉTATION — Le TTL de 120 secondes agit comme un piège temporel : il impose une fenêtre d'exécution trop étroite là où la structure fractale du marché nécessite parfois plusieurs minutes de latence pour aligner le radar. Résultat, le système s'asphyxie lui-même en attendant une validation qui expire avant d'être mesurable.

MISE EN RELATION — Le couplage entre l'état de l'essaim (`mode=none`) et le `duo_wait :: reason=revenge_ttl_expired` montre que le moteur s'interdit d'entrer en position dès que le chronomètre dépasse 120s, indépendamment de la tension ou du momentum latent.

PATTERN — Le pattern défectueux est la **synchronisation forcée par expiration temporelle** : un coupe-circuit (`FIX-LAST-LOSS`) qui tue l'opportunité sous prétexte de vouloir l'encadrer.

OPINION — Il est hautement probable que la modification du 16/08 ait sur-corrigé un risque mineur en détruisant l'alpha de la stratégie. Le remède a été pire que le mal.

AVIS STRICT (OBLIGATOIRE, dernière section) —
AVIS STRICT : LONG
HORIZON : 24h
CONFIANCE : haute

---

### 1. Différence de comportement entre les 2 morceaux (ligne à ligne)
- **Setup gagnant (13-14/08) :** Le moteur encaisse les blocs du radar (`momentum_too_small`, `wall_not_collapsed`) sans fléchir, puis déclenche le BUY avec la note `size_note=hunter_revenge_1.5x` (ex: `cyc=13` le 13/08 à 00:06, ou `cyc=22` le 14/08 à 08:35). Le revenge est persistant et s'affranchit du bruit immédiat.
- **Setup de la nuit (16-17/08) :** Le moteur subit des blocages en cascade du radar (`momentum_too_small`, `tactic_mismatch`, voire un `entry_error :: code=-2019 msg=Margin is insufficient.` à `cyc=1030`), puis le TTL s'active et stoppe net le processus avec la mention répétée `duo_wait :: reason=revenge_ttl_expired mode=none`. Le Hunter ne tire jamais.

### 2. Le « revenge_ttl_expired » et le blocage amont
Le `revenge_ttl_expired` apparaît exactement **à l'expiration du compte à rebours de 120 secondes**, comme on le voit le 16/08 à `21:00:07Z` (`cyc=529`), `22:47:13Z` (`cyc=1034`), ou autour des autres cycles listés. 

Ce qui bloque l'entrée juste avant, c'est une combinaison mortelle : 
1. Un marché amorphe ou contradictoire (`momentum_too_small`, `direction_unclear`, `spread_too_wide`, `tactic_mismatch`).
2. Une erreur critique de marge (`Margin is insufficient.` à `cyc=1030`), ce qui suggère qu'en plus du TTL, le sizing ou la gestion de trésorerie bloquaient physiquement l'ordre. 

**Est-ce le TTL ou le radar ?** C'est un **effet de cisaille** : le radar filtre et temporise légitimement le marché, mais le nouveau TTL de 120s est trop court pour laisser le radar trouver sa fenêtre de tir. Le chronomètre expire (TTL) *avant* que le radar ne donne son feu vert.

### 3. Pourquoi le revenge passait avant et plus maintenant ?
Avant, le revenge restait « armé en permanence » (comme l'indique le contexte avec 51-52 fills par run). Il attendait patiemment, ignorant le temps qui passe, jusqu'à ce qu'une inefficacité du marché se présente (type `shock_inversion_stop`). Le fix de la nuit a introduit une **contrainte temporelle arbitraire (120s)** qui annule le revenge s'il ne trouve pas preneur instantanément. Le système est passé d'un modèle piloté par l'opportunité (événementiel) à un modèle piloté par l'horloge (temporel), ce qui est incompatible avec la physique des marchés non stationnaires.

### 4. Recommandation concrète
**Recommander A : Rollback complet du revenge permanent.** 

*Pourquoi ?* Le marché dicte son propre rythme (fractal et non linéaire). Forcer une limite de 120 secondes (TTL) dans un système quantitatif qui repose sur l'attente du déséquilibre de l'adversaire (le revenge) revient à supprimer l'edge de la stratégie. Le setup de la nuit a prouvé mathématiquement son inefficacité (0 fill, PnL nul ou négatif). Il faut revenir à la version qui générait 90% du PnL, quitte à auditer séparément le problème de marge (`Margin is insufficient`) qui a pollué la session de la nuit.
