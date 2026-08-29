# AVIS DEEPSEEK (task deepseek.analyse · Google Gemini · 2026-08-29T18:40Z)

**VERDICT : GO-AVEC-RÉSERVES**
**CONFIANCE : 82 %**

**HYPOTHÈSES :**
1. La persistance du régime de liquidité sur les small caps de la famille ACE777 est inférieure à 4 heures, rendant la fenêtre de 24h aveugle aux chocs micro-structurels rapides.
2. Le volume UTC 02-06 correspond à un creux effectif de la liquidité globale de la paire, mais l'absence de déclencheur dynamique crée des faux négatifs hors de cette fenêtre rigide.

**CE QUI CHANGERAIT L'AVIS :**
L'observation dans les logs de production d'un décrochage de spread supérieur à 3 écarts-types non capté par le p30-24h, ou l'absence de corrélation de volume entre les small caps durant les phases de fausses alertes SAPI.

---

### Analyse et Contestations point par point (Preuves à l'appui)

#### Critique A — « La fenêtre 24h du p30 = miroir rétroviseur »
* **Position : CORTANA A PARTIELLEMENT RAISON (MAIS SA PROPOSITION EST INSUFFISANTE)**
* **Preuve / Contre-exemple :** Nos données réelles sur `ZBCNUSDT` montrent un spread à 20.32 bps pour un seuil dynamique à 18.34 bps. Sur une small cap, la liquidité s'évapore en quelques minutes (ex: murs de 243 $ sur RIZE). Une fenêtre de 24h lisse les ruptures violentes. Cependant, remplacer simplement par un ATR court terme sans borne introduit un bruit insupportable sur les carnets non lissés.
* **Amélioration proposée (Clause permanente) :** Ne pas utiliser un ATR pur, mais une **fenêtre hybride pondérée par EMA exponentielle (EWMA sur 4h couplée au p30 sur 24h)**. Formule : $\text{Seuil} = 0.7 \times \text{p30}_{24h} + 0.3 \times \text{p30}_{4h}$. Cela conserve l'amortisseur anti-bruit tout en réagissant en moins de 60 minutes aux chocs de régime.

#### Critique B — « La plage horaire UTC rigide (02-06) = angle mort »
* **Position : CORTANA A RAISON**
* **Preuve / Contre-exemple :** Fixer UTC 02-06 est un artefact calendaire rigide. L'activité institutionnelle ne respecte pas l'horloge UTC. La preuve est que nos scripts relèvent des anomalies de spread en dehors de cette plage, non captées par le proxy actuel ×0.35.
* **Amélioration proposée (Clause permanente) :** Remplacer la plage UTC par un **détecteur de rupture de volume par rapport à la moyenne mobile 24h glissante**. Si le volume panier chute de $\ge 60 \%$ par rapport à la MM24h sur une fenêtre glissante de 3h, alors le multiplicateur s'active dynamiquement, indépendamment de l'heure UTC.

#### Critique C — « L'entropie temporelle est trop LOCALE, ignore la synchronisation multi-paires »
* **Position : CORTANA SE TROMPE SUR LA PRIORITÉ (Complexité injustifiée)**
* **Preuve / Contre-exemple :** Ajouter une matrice de corrélation croisée des intervalles d'inter-arrivée en temps réel sur toutes les paires surcharge inutilement le wrapper `PathRegistry` pour un gain incertain à ce stade (risque de latence I/O sur le heartbeat).
* **Amélioration proposée (Clause permanente) :** Au lieu d'une matrice lourde, introduire un **compteur d'alerte agrégé cross-pairs minimaliste** : si $\ge 3$ paires déclenchent simultanément un `CV < 15 %` dans une fenêtre de 60 secondes, incrémenter le bonus SAPI global de `+0.25` au lieu de `+0.10`.

---

**SYNTHÈSE :**
La critique de Cortana est globalement pertinente sur l'inertie de la fenêtre 24h et la rigidité horaire. Valider le passage à un système hybride EWMA 4h/24h pour le spread (Corr 1 amendée) et substituer la plage UTC par un ratio de volume glissant de 3h (Corr 2 amendée). Refuser la matrice de corrélation lourde de Cortana au profit d'un compteur d'essaim simple sur l'entropie.
