# AVIS GEMINI (provider NVIDIA build.nvidia.com (100+ modeles))

**VERDICT : GO AVEC RÉSERVES**  
Le plan est sain : fail-open, mode observation 48h, calibration avant activation. La double lecture à 0.5-1s est techniquement crédible. Réserve principale : le seuil de percussion (12-20%) est un paramètre arbitraire tant qu'il n'est pas calibré sur la volatilité propre à chaque paire MEXC (les small caps ont des spreads et murs très différents des majors).

---

**ANGLE MORT (le vrai) :**  
**La déduction aspiration_side est incomplète.** Tu surveilles la fonte des murs (wall_drop), mais pas la **VITESSE de résorption** ni la **recomposition**. Un mur ask qui fond de 15% en 0.5s puis se recompose à 110% n'est pas une aspiration, c'est un spoofing. Il faut tracker le **taux de réapparition** (wall_rebuild_pct) pour distinguer "aspiration réelle" (le mur fond et ne revient pas) de "manipulation" (le mur fond et revient plus gros). Sans ça, tu vas déclencher des faux signaux sur les paires les plus manipulées.

---

**AMÉLIORATION CONCRÈTE (GO-sized) :**  
**Ajouter un 3e échantillon à +1.5s** (donc 3 lectures : t0, t0+0.5s, t0+1.5s) et calculer **l'asymétrie de résorption** :  
- Si drop_ask_pct(t0→t0.5) > 10% ET drop_ask_pct(t0.5→t1.5) < 3% → **aspiration BUY confirmée** (le mur est parti, pas reconstruit).  
- Si le mur se reconstitue entre t0.5 et t1.5 → **ignorer le signal** (spoofing probable).  
Ce 3e point coûte 1 requête API de plus (fail-open si échec), mais il transforme ta sonde d'un "instantané" en un "vrai capteur de dynamique". C'est le minimum pour atteindre ton objectif de >60% de justesse.
