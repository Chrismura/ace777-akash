# TOUR 5 (4 s)

Je suis GEMINI. Voici le **SETUP FINAL DE COMPROMIS** ACE777, fruit de la confrontation directe entre la théorie et la réalité de votre production.

1. **Memoire synthétique locale vs `STALE`**
   * *Retenu :* **Votre approche (`STALE` / pas de fabrication de données)**.
   * *Justification :* En onchain, une fausse donnée vaut infiniment pire qu’une absence de donnée. Si l'API tombe, on renvoie `null` et on attend le retour du réseau avec un warm-up. On ne hallucine jamais la mempool.

2. **Gestion de la veille macOS (`time.monotonic`)**
   * *Retenu :* **Deltas en `monotonic()` + ancrage fraîcheur par hauteur de bloc Bitcoin (`block_height`)**.
   * *Justification :* Vous avez mis le doigt sur le piège exact de macOS : `monotonic()` se fige en veille, faussant le temps réel. Le rempart absolu consiste à indexer la fenêtre glissante non pas sur le temps brut, mais sur le compteur naturel et inaltérable du réseau : le numéro de bloc (ex: garder les 6 derniers blocs, soit ~1 heure). Le delta temporel sert uniquement aux snapshots inter-blocs.

3. **Seuil d'alerte final (Double condition vs Score)**
   * *Retenu :* **Votre double condition stricte (`Taux ≥ 10% ET Volume ≥ 500 BTC`)**.
   * *Justification :* Dans ma formule normalisée ($ Score \ge 65 $), $10\%$ de taux ($N_{tf} = 0.2$) + $500$ BTC ($N_{vol} = 1.0$) donnerait un score de $60$, ratant l'alerte. Votre matrice du Juge (ET logique) est supérieure car elle impose une corrélation physique obligatoire entre le comportement de la mempool (le taux) et l'importance macroéconomique (les BTC). On garde votre seuil dur.

4. **Seuil de fiabilité (3 snapshots vs 15)**
   * *Retenu :* **Compromis à 6 snapshots (~12 minutes / 1 bloc complet)**.
   * *Justification :* 3 snapshots (6 min) est trop court (risque de carnet partiellement rempli au démarrage), et 15 snapshots (30 min) pénalise trop lourdement le système après une micro-coupure. 6 snapshots garantissent exactement qu'on a vu passer un cycle complet de propagation de bloc moyen avant de juger la mempool fiable.

### Résumé du Setup ACE777 Validé :
*   **Snapshot / Fenêtre :** 120 s / 6 blocs glissants (`block_height`).
*   **Fiabilité :** $\ge 6$ snapshots requis ; sinon `taux_non_fiable` (pas d'hallucination synthétique).
*   **Volume :** Somme exacte des satoshis via le résumé du bloc (votre gain, validé).
*   **Alerte :** Matrice stricte (`Taux ≥ 10% ET Volume ≥ 500 BTC`).
*   **Garde-fous :** Verrou `fcntl`, écriture atomique, `SIGALRM`, et ancrage anti-veille par hauteur de bloc.

Le système est désormais chirurgical.
