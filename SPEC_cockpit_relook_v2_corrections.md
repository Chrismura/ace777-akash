# SPEC v2 — COCKPIT RELOOK : CORRECTIONS FAMILLE (réserves convergentes 6 membres)

Fichier cible UNIQUE : `/Users/christophe/ace777-test-day1/Index_Maison/cockpit/index.html` (servi :17800, no-store).
La v1 (heure locale + synapse relook + cosmos lisible + grille + polling live) est VALIDÉE et INTÉGRÉE.
La famille 6 a rendu GO AVEC RÉSERVES : voici les corrections convergentes à appliquer. Produis les blocs `BEFORE → AFTER` exacts (chaînes réelles du fichier).

## R1 — HEURE LOCALE PARTOUT (4 traces UTC restantes, convergence 6/6)
Le pont :17777 envoie tous les `ts` en UTC (`2026-08-13T17:57Z`). Il reste 4 endroits qui affichent l'heure brute UTC :
1. **SESSION (cartes Alpha/Beta)** — code actuel :
```js
      meta.textContent = since
        ? ('SESSION depuis '+String(since).slice(11,16)+'Z'+(life!=null?(' · life '+life+'$'):''))
        : ('SESSION'+(life!=null?(' · life '+life+'$'):''));
```
→ remplacer par heure locale : `'SESSION depuis '+new Date(since).toLocaleTimeString('fr-FR',{hour:'2-digit',minute:'2-digit'})` (sans Z, sans 'Z').

2. **Stream trades Alpha/Beta** — code actuel :
```js
        return `<div class="trade ${kind}"><span>${(r.ts||'').slice(11,19)}</span><span>${sideU.slice(0,4)}</span><span>${meta||r.reason||''}</span><span class="${cls(r.pnl)}">${p}</span></div>`;
```
→ heure locale : `${r.ts ? new Date(r.ts).toLocaleTimeString('fr-FR') : ''}`.

3. **Stream trades Hulk** — code actuel :
```js
        return `<div class="trade ${kind}"><span>${(r.ts||'').slice(11,19)}</span><span>${ev.slice(0,4)}</span><span>${meta}</span><span class="${isOpen?'neu':cls(r.pnl)}">${pnlShow}</span></div>`;
```
→ même conversion.

4. **Alertes jour (bulle Cortana)** — code actuel :
```js
      return `<div class="item ${clsA}">${(a.ts||a.logged_ts||'').slice(11,16)} ${a.title||'?'}</div>`;
```
→ `new Date(a.ts||a.logged_ts||'').toLocaleTimeString('fr-FR',{hour:'2-digit',minute:'2-digit'})`.

## R2 — ANTI-CHEVAUCHEMENT LABELS COSMOS PLUS ROBUSTE (convergence 6/6)
La boucle actuelle (dans `drawNodes`, bloc `// Labels providers — leader line + anti-chevauchement`) fait un décalage vertical `while guard<10`. Rendre le placement robuste :
- **Tri préalable par angle polaire** (`Math.atan2(n.y, n.x)`) avant le placement des labels.
- Après le tri, le placement initial alterne de façon stable : les providers triés par angle reçoivent leur label à l'extérieur de leur orbite ; le décalage vertical (±14 px) reste en filet de sécurité mais avec `guard` porté à 20 et une passe de lissage finale (si 2 labels restent à distance < 12 px, décaler de +14).
- Objectif : aucune superposition visible quel que soit le nombre de providers (jusqu'à 14).
- Conserve : leader line `#4a5568` (ou couleur du nœud au survol), texte `#e8dcc0`, 11px, shadow, hub label central inchangé.

## R3 — POLLING ROBUSTE + INDICATEUR DÉGRADÉ (convergence 4/6 : DEEPSEEK, ULTRA, INFERX, GROK)
Code actuel de `pollHubLive` :
```js
    function pollHubLive() {
        fetch('hub.json', { cache: 'no-store' })
            .then(r => r.json())
            .then(data => {
                window.__HUB__ = data;
                buildNodes();
                renderCosmos();
            })
            .catch(() => { /* hub.json pas encore prêt — on réessaie */ });
    }
    pollHubLive();
    setInterval(pollHubLive, 10000);
```
Améliorer :
- `r.ok` vérifié (si !r.ok -> throw) ; try/catch complet.
- Compteur `hubPollFail` : à chaque échec, `hubPollFail++` ; s'il atteint 3, ajouter une classe `degraded` au `#cosmos-health` et afficher « LIVE (dégradé) » (texte discret, couleur ambre) — si le feed revient, `hubPollFail=0` et retirer la classe.
- En cas d'échec, ne PAS écraser `window.__HUB__` (les dernières données restent affichées) et continuer de poller.
- `r.json()` peut échouer (JSON invalide) -> même traitement que les échecs réseau.

## R4 — SUSPENDRE LE POLLING QUAND L'ONGLET EST CACHÉ (convergence 3/6 : JUGE, INFERX, GROK)
- Si `document.hidden` est vrai, NE PAS lancer de fetch (mais garder l'intervalle). Au retour de visibilité, un poll immédiat se fait (listener `visibilitychange`).
- Ajouter le listener :
```js
    document.addEventListener('visibilitychange', () => { if (!document.hidden) pollHubLive(); });
```

## CONTRAINTES
- JS vanilla, canvas 2D, aucune lib. Ne modifie que les blocs indiqués. Rien d'autre.
- Toutes les fonctions citées existent déjà — ne crée pas de nouvelles fonctions hors périmètre, pas de numéros de lignes inventés.
- La conversion d'heure doit gérer les valeurs vides (`null`/`''` -> afficher `--:--` ou `—`, jamais `Invalid Date`).
- SORTIE : blocs `BEFORE → AFTER` complets et exacts pour R1 (4 points), R2 (bloc labels), R3 (pollHubLive + CSS dégradé si besoin), R4 (listener).
