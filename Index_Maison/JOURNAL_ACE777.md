
## 30/08 — Analyse croisée approfondie EDEL (réponse : nouveau pattern ? corrélations ?)
- **LA découverte** : la signature d'EDEL = régime IMPULSE (15% du temps, m6 médian 70.4% vs 4.2% hors = 17× plus de mouvement). 3 rafales en 3 jours, toutes en fin de journée. Après chaque rafale : +0.2 à +0.5% à 30min (n=3).
- Creux horaire instable : 23h → 21h → 11h → 00h selon les jours → aucune fenêtre horaire fiable. Le régime compte, pas l'heure.
- Corrélations : AUCUNE exploitable (max RWAINC +0.146, MNSRY −0.287 sur 25 pts = bruit). EDEL = actif le plus découplé du portefeuille.
- Conséquence set-up : entrer/sortir sur l'allumage du régime IMPULSE, pas sur une heure. Fiche EDEL mise à jour.

## 30/08 — Analyse croisée approfondie EDEL (réponse : nouveau pattern ? corrélations ?)
- **LA découverte** : la signature d'EDEL = régime IMPULSE (15% du temps, m6 médian 70.4% vs 4.2% hors = 17× plus de mouvement). 3 rafales en 3 jours, toutes en fin de journée. Après chaque rafale : +0.2 à +0.5% à 30min (n=3).
- Creux horaire instable : 23h → 21h → 11h → 00h selon les jours → aucune fenêtre horaire fiable. Le régime compte, pas l'heure.
- Corrélations : AUCUNE exploitable (max RWAINC +0.146, MNSRY −0.287 sur 25 pts = bruit). EDEL = actif le plus découplé du portefeuille.
- Conséquence set-up : entrer/sortir sur l'allumage du régime IMPULSE, pas sur une heure. Fiche EDEL mise à jour.

## 30/08 — Set-up « RÉGIME » EDEL construit (suite découverte IMPULSE)
- Création `detecter_rafales_impulse.py` (lecture seule, rejouable) : liste chaque allumage IMPULSE avec prix, durée, +30min/+60min, pic. Sortie runs/rafales_impulse/<PAIRE>.md.
- 4 allumages rejoués sur EDEL : +30min 3/3 UP (moy +0.33%), +60min 2/3 DOWN (moy −0.42%), pic médian rafale ≈ +1%.
- Set-up régime : entrée = allumage IMPULSE + pullback (PAS de fenêtre horaire), exécution 50/50, sortie rapide objectif +0.5 à +1% dans les 30 premières minutes, stop sous l'allumage, JAMAIS de trailing long.
- Rafale 30/08 16:05Z EN COURS (m6 faible 6% = allumage naissant, à ne pas traiter comme les 3 autres).
- Fiche EDEL mise à jour avec le set-up régime + la preuve qui s'accumule (valider dans ~7 jours).
