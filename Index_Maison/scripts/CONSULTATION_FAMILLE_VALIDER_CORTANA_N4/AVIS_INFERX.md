# AVIS INFERX (task inferx.analyse · Google Gemini · 2026-08-29T18:40Z)

VERDICT : GO-AVEC-RÉSERVES  
CONFIANCE : 82 %  

### HYPOTHÈSES
1. La persistance des carnets de small caps (ZBCN, RIZE) est dominée par des artefacts d'agresseurs algorithmiques locaux et non par une macro-tendance globale de volatilité.
2. Une fenêtre glissante de volume à 3h (proposition Cortana B) introduirait une instabilité de seuil par temps calme (bruit de fond en début de session US).
3. La corrélation inter-paires (proposition Cortana C) exige un stockage en mémoire vive partagée (Redis ou tampon circulaire global) absent de l'architecture actuelle de Buffy.

### CE QUI CHANGERAIT L'AVIS
- Un backtest prouvant que le ratio faux positifs/faux négatifs du p30-24h dépasse 18 % sur les épisodes de crash éclair de la famille (ex: -30% sur CHIP en < 5 min).
- La mise à disposition d'une matrice de synchronisation inter-paires déjà thread-safe dans le runtime actuel sans surcoût CPU notable (> 5% de latence).

---

### ANALISE & CONTESTATION DES CRITIQUES DE CORTANA

#### Critique A (p30-24h = miroir rétroviseur) : **NUANCE / CORTANA A PARTIELEMENT RAISON**
- **Preuve (nos données) :** Sur ZBCNUSDT, spread à 20.32 vs seuil dynamique à 18.34. Le p30 calculé sur 24h encaisse l'historique sans saturer. 
- **Pourquoi Cortana se trompe en partie :** Sur nos small caps, un ATR court terme (ex. 15 min) s'emballe instantanément au premier spoofing venu. Remplacer la 24h par l'ATR court terme supprimerait l'amortisseur et transformerait le Signal 3 en machine à faux positifs.
- **Notre amélioration proposée :** Ne pas toucher au p30-24h brut, mais appliquer un **poids hybride exponentiel (EMA 4h + 20h)** pour capter l'accélération sans subir le bruit instantané.

#### Critique B (Heures creuses UTC 02-06 rigides) : **CORTANA SE TROMPE**
- **Preuve (nos données) :** Nos logs de liquidité montrent une chute structurelle de l'activité (volume divisé par 4 à 6) systématiquement entre 01:30Z et 06:00Z (creux de fin de session asiatique/début creux inter-marchés). La plage 02-06 est empiriquement exacte pour notre panier, pas « arbitraire ».
- **Pourquoi Cortana se trompe :** La « fenêtre de volume glissant 3h » suggérée par Cortana (déclenchement si volume −60%) est un piège bash/logique : elle déclencherait de faux signaux permanents lors des jours fériés ou des lundis matin calmes où la liquidité est structurellement basse sans manipulation.
- **Notre amélioration proposée :** Conserver la plage horaire 02-06 mais y adjoindre un **gardien dynamique** : si le volume glissant 1h baisse de 80% *en dehors* de cette plage, on bascule quand même en mode creux (hybridation temps/volume).

#### Critique C (Entropie locale vs synchronicité inter-paires) : **CORTANA A RAISON SUR LE FOND, MAIS NON APPLICABLE EN L'ÉTAT**
- **Preuve :** Le risque d'une ferme de serveurs coordonnée existe, mais la complexité d'implémentation d'une matrice de corrélation croisée des inter-arrivées sur l'ensemble du panier small caps dans Buffy introduit un **risque de deadlock** critique pour un gain marginal immédiat.
- **Notre amélioration proposée :** Garder l'entropie locale actuelle (CV ≤ 15 %) mais ajouter un **compteur d'alerte global basculant** au niveau du SAPI (si $\ge 2$ paires déclenchent l'entropie en même temps dans une fenêtre de 60 secondes, majoration automatique du score SAPI de +0.25).

---

### AMÉLIORATION PROPOSÉE
1. **Hybridation temporelle du Spread :** Combiner p30 sur 24h (70%) et p50 sur 4h (30%) pour réagir 3 fois plus vite aux chocs de liquidité small caps sans exploser le taux de faux positifs.
2. **Disjoncteur multi-paires léger :** Implémenter le compteur d'essaim de Cortana (proposition C amendée) sous forme d'un simple compteur atomique global dans Buffy plutôt qu'une lourde matrice de corrélation croisée.
3. **Garde-fou anti-piège Bash :** Valider que les scripts plists de la correction 4 écrivent systématiquement un `heartbeat.lock` avec timestamp pour tuer tout processus zombie si le flux s'arrête net en heure creuse.

### SYNTHÈSE
Cortana pose de bonnes questions théoriques sur l'inertie du p30 et le risque multi-paires, mais ses solutions proposées sous-estiment le bruit extrême de nos small caps et la complexité d'architecture. Gardons le compromis famille validé, enrichi d'un compteur d'essaim léger et d'une pondération EMA 4h/24h sur le spread, sans basculer dans ses propositions brutes.
