# GROK — verdict famille

Provider: Puter Grok (gratuit)

**Verdict : GO AVEC RÉSERVES**

**Analyse du code livré**  
Les 5 points demandés par Christophe sont globalement bien couverts :

- Heure : passage complet en `toLocaleTimeString('fr-FR')` + libellés « (locale) ». Cohérence bonne sur clock, refresh, sessionSince et queue.
- Graph synapse : soma réduit (r=4-6), labels externes + leader lines + anti-chevauchement basique implémentés.
- Cosmos : logique `useTwoRings` + `R/R2` + boucle `drawnLabels` avec décalage vertical correct.
- Tableaux : passage en `grid-template-columns: repeat(2,1fr)` avec ordre demandé et `grid-column:1/-1` sur Événements.
- LIVE : `pollHubLive()` avec `fetch(..., {cache:'no-store'})` toutes les 10 s + mise à jour `window.__HUB__` et re-render. Preuves de test (budget 1613/624) confirment le rafraîchissement.

**Réserves**  
L’anti-chevauchement reste fragile (while guard<10 + décalage fixe ±14). Risque de superposition persistant au-delà de 12-14 providers. Pas de gestion d’erreur fetch visible (pas de try/catch ni fallback). Aucun contrôle de visibilité d’onglet (le polling continue en arrière-plan).

**Améliorations recommandées (priorité 1-2)**  
1. Rendre l’anti-chevauchement plus robuste (force-directed léger ou itérations supplémentaires avec coût limité).  
2. Ajouter `try/catch` + retry exponentiel sur le fetch hub.json + état « connexion perdue ».  
3. Suspendre le polling quand `document.hidden` (Page Visibility API).  
4. Vérifier les autres onglets (pas seulement hub) pour toute trace UTC restante.  
5. Ajouter un petit indicateur visuel pendant le fetch (léger spinner ou classe « updating »).

Globalement solide et conforme à la demande. Les réserves portent uniquement sur la robustesse et la résilience, pas sur le respect fonctionnel.
