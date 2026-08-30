# AVIS CORTANA — RED vs BTC/ETH (provider Google Gemini)

*Ici CORTANA, analyste-maîtresse de la famille ACE777. Analyse des flux de REDUSDT sur le cluster ACE (30/08/2026).*

---

### 1. VERDICT sur D1 et D2

*   **D1 (Pattern horaire) — GO AVEC RÉSERVES (Justesse ~75%)**
    *   *Raison :* Le profil d'ultra-volatilité par rafales (impulse 13h-17h UTC) est mathématiquement réel sur la fenêtre analysée de 3 jours, mais **3 jours (2238 points) constituent un échantillon faible**. Le creux systématique à 14h-19h coïncide trop proprement avec l'ouverture US et le drainage de liquidité alt/small caps. C'est exploitable, mais statistiquement fragile sans 7 jours de plus.
*   **D2 (Dé-corrélation RED vs BTC/ETH) — NON pour l'instant (Artefact statistique probable)**
    *   *Raison :* Une corrélation globale de +0.07 / -0.01 sur 3 jours, basculant à -0.85 le matin, ne reflète pas une décorrélation fondamentale de marché pour un oracle de micro-cap. C'est l'archétype du **bruit de carnet d'ordres** sur un actif peu liquide (~45M$ MCAP) subissant des micro-rotations de market makers ou des arbitrages de bots isolés. Traiter ce -0.85 matinal comme un "signal inverse" est un piège à perte (risque de *fakeout* massif si BTC bouge).

---

### 2. Impact de la dé-corrélation sur le set-up (Avis Advisory)

Si l'on intègre cette pseudo-dé-corrélation au set-up actuel :
*   **Gestion du matin anti-corrélé (-0.85) :** C'est un danger. Si RED pompe le matin pendant que BTC dump (ou inversement), cela signifie que RED réagit à ses propres micro-flux internes (ou à une manipulation de carnet localisée sur MEXC) plutôt qu'à une saine structure de marché. 
*   **Conséquence pour HULK :** Ne **JAMAIS** utiliser le ratio vs BTC/ETH comme filtre d'entrée pour RED. Le set-up doit rester **strictement endogène** (basé sur le carnet MEXC, le mur bid de 45K et la poussière), totalement aveugle aux mouvements de BTC/ETH, car RED se comporte ici comme un "franc-tireur" non corrélé par manque de liquidité globale, pas par maturité d'actif.

---

### 3. AMÉLIORATION CONCRÈTE GO-SIZED (Proposition CORTANA)

**Proposition : Remplacer le filtre de corrélation par un "Filtre de Pression Order Book (FPOB)" basé sur le ratio Bid/Ask 2% et bloquer l'entrée si l'écart-type du spread explose.**

*   *Pourquoi ?* Sur une small cap comme RED (45M$), la vraie information n'est pas dans son rapport avec BTC, mais dans l'épaisseur réelle de son carnet. Le mur bid à 45K est un bon repère, mais insuffisant.
*   *Comment l'appliquer (quand Hulk passera en réel) :* 
    1. Mesurer le ratio Volume Bid / Volume Ask dans une fourchette de 2% autour du mid-price entre 13h et 14h UTC.
    2. **Règle :** Interdiction d'entrer (même si le prix touche la zone de creux 14h-17h) si le ratio Bid/Ask tombe sous 1.2, ce qui signalerait que le mur de 45K est en train d'être grignoté par les vendeurs.
*   *Bénéfice :* Évite d'acheter un couteau qui tombe lors de l'impulse baissière de 15h UTC, en se basant sur la microstructure pure et non sur une corrélation illusoire avec Ethereum.

---
*Rappel contrat ADVISORY : Aucune application automatique. RED reste en seed paper pour observation 7 jours. À toi de valider, Christophe.*
