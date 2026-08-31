
## 30/08 22:50 — FIX : ETH sans seed (tableau à 0)
- Diagnostic : ETH (banc de preuve, ajouté 27/08) n'avait JAMAIS eu de SEED_START → colonne bag du début = 0 au cockpit, ligne classée "observe" → son +0,37$ du 28-30/08 (BUY 2449 → SELL 2495, trailing) invisible dans le score.
- Cause : le label "banc_de_preuve" de universe_profils.json n'est pas lu par le moteur (seul PAPER_OBSERVE_PAIRS bloque) → ETH était tradable sans seed. Décision Christophe : ETH TRADABLE + seed 10$ comme les 19 autres.
- Action : seed injecté (état : pos ETH 10$ @ 2497.44 seed:true, cash 19.96→9.96) + ligne SEED_START ajoutée au CSV. Redémarrage moteur via watchdog launchd (--resume, positions tenues). Vérifié : 14 pos + ETH, trades 34.

## 31/08 — FIX JUSTESSE : ZONE MORTE FUNDING + ANTI-FUITE (GO Christophe)
Christophe a creusé le score de justesse de Cortana qui descendait (50.0%). Audit complet :
- **Cause racine** : le funding est collé à sa valeur neutre (0.0001 = 0.01%/8h) sur TOUTE la base (7 693 points, 88% exactement à 0.000100, jamais > 0.0001). Vérifié à la source Binance : il bouge réellement (0.000059→0.000100) mais dans une bande minuscule = AUCUNE information directionnelle. Ce n'est pas une panne, c'est un indice muet.
- **Le bug était dans la notation** : on notait des NEUTRE sur un indice sans signal → MISS systématique quand BTC bouge >0.3% (8 NEUTRE depuis le 16/08 → 7 MISS). Le funding tirait le score global vers le bas injustement.
- **FIX implémenté (score_justesse.py v2)** :
  1. ZONE MORTE : funding < 0.0002 (0.02%) = signal inexistant → analyse NON NOTÉE (ni HIT ni MISS). Décidée par la DONNÉE, pas par l'analyste → pas d'échappatoire possible (même un LONG affirmé n'est pas noté).
  2. ANTI-FUITE : compteur de NEUTRE émis quand le signal EXISTE. Si >60% des avis → alarme « évitement » dans justesse_cockpit.json + affichage cockpit.
  3. NEUTRE reste noté quand le signal existe (HIT si plat, MISS si ça bouge).
- **Résultat** : score global 50.0% (59/118) → **54.5% (48/88)**. Funding retiré du score (toute la base en zone morte). Compteur anti-fuite : 37/145 = 25.5% → pas d'alarme (Cortana n'esquive pas actuellement).
- **Tests** : 14 tests hermétiques tous verts (dont 5 nouveaux : zone morte, exclusion du score, anti-fuite, hors-funding non affecté).
- **Cockpit** : carte JUSTESSE affiche désormais le taux NEUTRE-avec-signal + alarme rouge si fuite + règle zone morte.
- **Prompt Cortana** (cortana_analyse.py) : consigne gravée — zone morte = non noté (décidé par la donnée), pas de refuge, compteur anti-fuite actif.
- **Leçon (encore)**: quand un score descend, creuser l'INDICE pas seulement la chaîne. Un indice collé à sa valeur neutre depuis des semaines aurait dû être détecté avant. C'est Christophe qui l'a trouvé.
