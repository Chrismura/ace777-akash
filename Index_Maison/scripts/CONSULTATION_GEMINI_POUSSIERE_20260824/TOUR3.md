# TOUR 3 (4 s)

Je suis GEMINI. Voici le design final ACE777, épuré et mathématiquement rigoureux.

### a) Intervalle de snapshot et Fenêtre
*   **Snapshot ($\Delta t$) :** **120 secondes (2 min)**. 30 requêtes/heure, protégeant l'API gratuite et limitant le bruit de propagation.
*   **Fenêtre ($W$) :** **3600 secondes (1 heure)** en `set` tournant en RAM (< 15 Mo sur M1).

### b) Fiabilité (Anti-faux 100 %)
*   **Maturité ($M$) :** Invalide si $< 15$ snapshots en mémoire. 
*   **Contre-mesure :** *Warm-up* obligatoire de 30 minutes au démarrage ou après une coupure réseau > 180s (aucun taux émis).

### c) Volume exact en BTC (Sans estimation)
L'endpoint `/api/block/{hash}` retourne un résumé avec la liste des transactions incluant directement leur valeur totale en satoshis (`value` des outputs).
*   **Calcul :** On croise la liste des `txids` fantômes du bloc avec ce résumé. Le volume est la **somme exacte des satoshis** des outputs de ces transactions fantômes, convertie en BTC, sans aucune approximation ni formule vByte.

### d) Seuils et Score normalisé (0-100)
Pour éviter qu’une grandeur n’écrase l’autre, on normalise chaque métrique sur une échelle de **0 à 1** avant pondération (pondération 50/50) :
1.  **Taux normalisé ($N_{tf}$) :** $T_f / 0.50$ (plafonné à 1.0 pour un taux de fantômes $\ge 50\%$).
2.  **Volume normalisé ($N_{vol}$) :** $\min(1.0, \text{Volume\_BTC} / 500\text{ BTC})$ (un bloc absorbant $\ge 500$ BTC de flux cachés sature à 1.0).
*   **Formule de score ACE777 (0-100) :** 
    $$Score = 100 \times (0.50 \times N_{tf} + 0.50 \times N_{vol})$$
    *Seuil d'alerte :* $Score \ge 65$ (ex: $25\%$ de fantômes + $250$ BTC cachés).

### e) Méthode de validation (Réaliste)
1.  **Backtesting Historique (Événement de référence) :** Injection des blocs minés lors de crises de volatilité historique connues (ex: la rupture haussière des 19-20 août où des transferts massifs ont contourné la mempool publique). L'indicateur doit générer un pic de $Score > 80$ spécifiquement sur ces fenêtres temporelles.
2.  **Validation croisée en direct (A/B Testing local) :** Exécution simultanée de deux instances Python sur le Mac M1 : l'une échantillonnant à $\Delta t = 120s$, l'autre à $\Delta t = 240s$. Si la variance du taux de fantômes entre les deux instances sur un même bloc est $< 3\%$, la résolution est validée et exempte de bruit de capture.

### f) Garde-fous (Mac M1 & Python)
1.  **Rate-Limit Shield :** Pause de 1,5s entre les requêtes HTTP, avec backoff exponentiel sur les erreurs `429`.
2.  **Sanity Check :** Si un bloc renvoie un taux de fantômes de $100\%$ avec un volume anormalement bas ou nul, le script invalide le bloc (protection contre les dégradations de l'API).
