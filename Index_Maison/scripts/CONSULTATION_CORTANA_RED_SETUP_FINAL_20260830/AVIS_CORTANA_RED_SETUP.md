# AVIS CORTANA — SET-UP RED (provider Google Gemini)

Analyse CORTANA — Dossier RED (RedStone) · 30/08/2026
Contrat : ADVISORY (Proposition pure, exécution 0%). Justesse évaluée > 60% (passage en mode correctif/propositif activé).

---

### 1. VERDICT SUR LE SET-UP
**GO AVEC RÉSERVES STRICTES**
* **Raison courte et nette :** Le cycle intraday est mathématiquement exploitable (creux 14-19h / pic 01-05h, écart ~2,5%), mais le set-up actuel souffre d'un **angle mort critique** : il mélange des métriques macro-micro contradictoires (corrélation BTC/ETH qui saute de +0.07 à +0.63) et repose sur un mur de carnet (bid) dont la tension (spoof 1.67%) est sous-exploitée face à la brutalité des rafales (dd15 max 27,8%).

---

### 2. CORRECTIONS ET AMÉLIORATIONS (Au-delà de la validation)
*Ce que tu proposes est bon, mais voici ce qui manque pour blindé le process (Clause Permanente : je propose du neuf).*

* **Correction 1 (Filtre de corrélation instable) :** La corrélation BTC/ETH est passée de quasi-nulle (+0.07) à forte (+0.63). **Proposition :** Interdire l'entrée 14-17h UTC si BTC ou ETH est en *Breakout/Breakdown* 15 min (mouvement directionnel > 1.5% sur les majors). RED est une small cap orpheline : si le marché global bouge, le "creux endogène" est détruit par la macro.
* **Amélioration 2 (Dynamique du Mur & Spoofing) :** Traiter le mur affiché (45 240$) non comme un seuil passif, mais via son *taux de régénération*. **Proposition :** Si le mur est grignoté de plus de 30% en < 2 minutes sans que le Trade Sign Delta ne devienne positif (> +0.15), **annulation immédiate** de l'ordre d'achat en cours de déploiement (le mur est un leurre, pas un appui).
* **Amélioration 3 (Répartition des 3 tranches) :** Entrer en −1/−2/−3% est trop linéaire pour une volatilité de 22% (dd15). **Proposition :** Condenser l'entrée sur le pire de la secousse 15h-16h UTC : 50% de la position sur le premier contact du creux, et 50% *uniquement* si la poussière < 10% confirme le désintérêt total des vendeurs.

---

### 3. AUDIT DES MÉTRIQUES (Pro vs Maison) : Garder ou Jeter ?

* **Amihud (Illiquidité / Impact prix : 2.43e-06) :** **À GARDER (mais sous conditions).** Sur MEXC small cap, l'Amihud est vital pour estimer combien de $ font bouger le prix de 1%. À 2.43e-06, la liquidité est fine mais gérable pour une taille "Hulk seed 10$". Si l'Amihud triple subitement, on stoppe net (assèchement).
* **Parkinson (Volatilité high/low : 0.01) :** **À JETER (pour ce set-up précis).** Le Parkinson mesure la volatilité intra-bougie basée sur les extrêmes (High/Low). Sur une small cap gavée de mèches de manipulation et de spoofing, le Parkinson s'emballe pour du bruit. Préférer l'écart-type classique des clôtures 15 min ou le range réel nettoyé des mèches extrêmes.
* **Trade Sign Delta (+0.08) :** **À GARDER ABSOLUMENT.** C'est ton meilleur thermomètre temps réel de l'agression acheteuse/vendeuse. Un delta à +0.08 montre une légère pression acheteuse cachée pendant que le prix stagne ou baisse (accumulation discrète dans la zone creuse 14-17h). Seuil d'alerte : doit passer > +0.20 pour valider le départ du trade.
* **Nos métriques maison (Poussière, Mur, Régime) :** **SUPERIEURES AUX PROS POUR CE CAS.** 
  * Le *Régime IMPULSE 13-17h* est ton meilleur repère temporel.
  * La *Poussière (<15%)* détecte le washout mieux qu'aucun indicateur académique.
  * **Verdict comparatif :** Garde *Trade Sign Delta* et *Amihud* comme arbitres quanti, jette *Parkinson*, et sers-toi toujours de la *Poussière/Régime* comme de la boussole principale.
