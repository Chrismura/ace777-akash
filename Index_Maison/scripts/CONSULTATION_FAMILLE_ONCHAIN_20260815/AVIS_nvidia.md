# AVIS nvidia (provider NVIDIA build.nvidia.com (100+ modeles), 330.8s)

**VERDICT : GO-AVEC-RÉSERVE**  
**CONFIANCE : 72%**  

---

**1. Design du pont (injecter dans live.json)**  
- **OUI**, c'est le bon choix. Un fichier dédié créerait un 3e canal de lecture → risque de désynchronisation. live.json est déjà le point de convergence Cortana/Ada.  
- **Risque saturation** : faible si clés préfixées `onchain_*` et regroupées sous une seule sous-section `onchain`. Éviter de polluer le namespace racine.  
- **Confusion avec whaleN/whaleUsd** : à clarifier dans LEXIQUE (Cortana doit savoir que `whaleN` = proxy aggTrades, `onchain_whaleBlocsN` = réel). Sinon double comptage.  

**2. Clés proposées**  
- **Bonnes** : `whaleBlocsN`, `whaleBlocsBtc`, `whaleFragN`, `whaleFragBtc`, `whaleDir`, `whaleAlerte`.  
- **Manque** :  
  - `whaleCumul24hBtc` (Σ BTC sur 24h glissantes, pas juste le scan récent) → permet à Ada de voir la tendance, pas un pic isolé.  
  - `whaleSource` (liste des adresses étiquetées impliquées) → utile pour Cortana (ex. "Binance hot" vs "Genesis").  
  - `whaleEcartSeuil` (distance en % au seuil de déclenchement) → Ada peut pondérer la force du signal.  

**3. ADA — Intégration sans casser la philosophie**  
- **Pondération raisonnable** : 5-10% du poids total de la pression (vs 40-50% pour le price action).  
- **Mécanisme** : utiliser `whaleCumul24hBtc` comme **modulateur** de la voilure existante, pas comme déclencheur.  
  - Si cumul > seuil auto-appris (ex. 2× la moyenne mobile 7j) → réduire voilure de 5-8% (sortie exchange = pression vendeuse).  
  - Si cumul < seuil → voilure normale.  
- **Jamais de blocage** : le modulateur est plafonné à ±10% de la voilure calculée par ailleurs.  

**4. CORTANA — Impact à 44% de justesse**  
- **Risque de brouillage** : oui, si on ajoute un indice brut. Mais `whaleDir` + `whaleSource` sont **plus informatifs** que funding/fearGreed (événements discrets, pas du bruit continu).  
- **Mode d'ajout** : ne pas l'ajouter comme feature numérique brute. L'ajouter comme **condition contextuelle** dans le prompt (ex. "Un gros bloc de 1200 BTC vient de sortir de Binance → si le prix est en range, privilégier une lecture baissière").  
- **Test A/B** : comparer justesse avec/sans sur 7 jours avant activation définitive.  

---

**HYPOTHÈSES**  
1. Les étiquettes d'adresses (Binance, Bitfinex) sont fiables à ≥90% (vérifiées double).  
2. Le scan 5 min capture ≥80% des gros mouvements (pas de faille mempool).  
3. Ada peut apprendre un seuil relatif sur `whaleCumul24hBtc` en ≤14 jours.  

**CE QUI CHANGERAIT L'AVIS**  
- **NO-GO** si : les étiquettes d'adresses se révèlent fausses >20% (test sur 48h).  
- **GO plein** si : le test A/B Cortana montre +3 points de justesse en 7 jours.  

**AMÉLIORATIONS PROPOSÉES**  
1. **Fenêtre glissante 24h** pour `whaleCumul24hBtc` (au lieu du scan récent seul).  
2. **Log de corrélation** : enregistrer quotidiennement la corrélation entre `whaleCumul24hBtc` et le prix 4h plus tard → ajuster la pondération Ada dynamiquement.  
3. **Alerte visuelle** dans le terminal de supervision (pas seulement booléen) : afficher la source et le montant en clair.  

---

**SYNTHÈSE**  
Design validé : injection dans live.json via pont idempotent, clés préfixées `onchain_*` + `whaleCumul24hBtc` ajouté. Ada : modulateur ±10% sur voilure, seuil auto-appris, pondération 5-10%. Cortana : ajout contextuel (pas numérique), test A/B 7 jours avant activation. Pérennisation par plist launchd. Risque principal : fiabilité des étiquettes → vérification 48h avant GO plein.
