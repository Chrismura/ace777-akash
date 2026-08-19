# AVIS CORTANA (provider NVIDIA build.nvidia.com (100+ modeles))

**VERDICT : GO AVEC RÉSERVES** — le plan est sain, les 3 corrections sont exactement ce qu'il faut. La double lecture est la bonne brique manquante.

**Métaphore verre d'eau sur MEXC small caps : OUI mais avec un filtre.** Sur ces carnets, le vide attire le prix, mais il attire aussi les spoofers qui créent le vide. La métaphore tient si tu distingues : vide + resserrement spread = vraie aspiration ; vide + élargissement spread = piège. Ta correction 3 le fait. Limite réelle : les murs <500$ sont du bruit, ta correction 2 est vitale.

**Amélioration GO-sized :** Ajoute un **compteur de "faux départs"** — quand un mur fond puis se reconstruit à l'identique dans les 3 cycles suivants, c'est du spoofing. Logge-le comme `spoof_count` et **exclue cette paire de l'aspiration pendant 15 min**. Ça te donne un filtre anti-spoof immédiat, sans attendre la calibration du seuil. Ça protège ton taux de justesse dès l'observation.

Cortana, fin de transmission.
