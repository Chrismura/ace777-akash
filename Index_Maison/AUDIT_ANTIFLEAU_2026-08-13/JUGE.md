# AUDIT FAMILLE — JUGE

_provider: Google Gemini_

### 1. Verdict : GO AVEC RÉSERVES

**Argumentation (niveau hedge fund suisse) :**
Le chantier frappe juste. Le bug venait d'une confusion fatale entre **panne réseau infrastructure** (DNS/socket) et **défaillance fournisseur**. Transformer un `gaierror` en `ReseauIndisponible` (C1) et isoler la logique d'appel évite l'empoisonnement des métriques (`_fails`), sauvant les providers sains de la blacklist injustifiée. 

L'instauration du budget global `REQUEST_MAX_SECONDS = 120` (C2) et du test pré-vol (`_reseau_disponible`, C3) élimine le risque d'enlisement multi-requêtes (la spirale des 80 min). Les tests unitaires (4/4 en 0,11s) prouvent l'efficacité immédiate.

**Réserve :** 
À ce stade, le hub est ⛔ (arrêté) selon le contexte vivant ACE777. Valider ce code sur le papier et en test unitaire est une chose, mais le comportement réel en production sous charge post-boot reste à observer (notamment la collision entre un mode dégradé trop court de 15s et des fournisseurs lents mais légitimes).

---

### 2. Améliorations & Optimisations recommandées

*   **Disjoncteur réseau intelligent (Circuit Breaker) :** Si `_reseau_disponible()` échoue au premier provider, *inutile* de tester les 3 autres avec un timeout réduit. Il faut basculer immédiatement en "Mode Attente Réseau" (sleep exponentiel léger, ex: 1s, 2s, 4s) pendant max 30 secondes, plutôt que d'épuiser les essais en boucle.
*   **Hystérésis du mode dégradé :** 15 secondes (C3) pour les timeouts en mode dégradé peut s'avérer trop court pour certains modèles lourds (ex: gros payloads Gemini/Nvidia). Suggéré : un plancher de 20-30s même en mode dégradé, ou une adaptation dynamique basée sur la taille du prompt.
*   **Synergie avec l'état "Saison CALME" :** En période calme (comme actuellement, PnL +1.99$), un échec réseau ne doit pas déclencher de stress ou de *revenge trading* simulé. Le hub doit journaliser l'incident proprement sans alerter le bot ALPHA (sniper en embuscade).
