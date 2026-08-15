# SPEC — COCKPIT RELOOK V2 (heure + graph + live)

Fichier cible UNIQUE : `/Users/christophe/ace777-test-day1/Index_Maison/cockpit/index.html` (4069 lignes, servi par le serveur local :17800, daemon `com.ace777.cockpit-http`).

NE MODIFIE AUCUN AUTRE FICHIER. Produis le code JS/CSS/HTML de remplacement, prêt à coller, en français. Une seule mission : le code complet des blocs à remplacer (markers `BEFORE` → `AFTER`).

## CONTEXTE GÉNÉRAL

Le cockpit affiche 2 graphes dans l'onglet GRAPH :
1. **COSMOS HUB** (`#cosmos-canvas`, bloc `<div id="cosmos-hub" class="cosmos-container">`) : le HUB central + providers en orbite circulaire. Les labels (noms des providers) se superposent quand ils sont nombreux → illisible.
2. **SYNAPSES** (ancien canvas `#synapses`, `.card.graph-card`) : des « bulles » (cercles avec le nom écrit DANS le cercle, `fillText` dans `soma nodes`) → noms illisibles qui se superposent.

Le feed du hub est un SNAPSHOT : `<script src="hub.js">` (ligne 14) définit `window.__HUB__` UNE FOIS au chargement. Le serveur :17800 sert aussi `hub.json` (même contenu, avec `Cache-Control: no-store`) — il est régénéré toutes les 120s par launchd `com.ace777.hub-cockpit-feed`. → Pour le LIVE, le cockpit doit **poller `hub.json`** (relative `hub.json`, même dossier) toutes les ~10 s.

## PROBLÈMES À CORRIGER (5 chantiers)

### C1 — HEURE UNIFIÉE EN LOCALE PARTOUT
Actuellement : le clock (`tickClock`) et le refresh (`forceRefresh`) affichent l'heure **UTC** (`...toISOString().slice(11,19)+'Z'`), alors que le cosmos affiche l'heure **locale** (`toLocaleTimeString('fr-FR')`) → décalage de 2 h selon l'endroit. Règle : **TOUT en heure locale, format `HH:MM:SS`, jamais de `Z`**, avec le libellé « locale » discret.

Occurrences exactes à modifier (code actuel) :

**A) `tickClock()` (ligne ~2396)** :
```js
  function tickClock(){
    document.getElementById('clock').textContent = new Date().toISOString().slice(11,19)+'Z';
  }
```
→ heure locale : `new Date().toLocaleTimeString('fr-FR')` (HH:MM:SS). Le `#clock` est dans le header avec `<span class="live"><i></i>` — ajouter un libellé discret « heure locale » (ex. titre `title="heure locale"`, et le texte affiché = `HH:MM:SS` sans Z). NE PAS toucher à l'icône pulsante.

**B) `forceRefresh()` (ligne ~2782)** :
```js
      if(meta) meta.textContent='refresh '+new Date().toISOString().slice(11,19)+'Z';
```
→ `meta.textContent='MAJ '+new Date().toLocaleTimeString('fr-FR')+' (locale)'`.

**C) `saySticky` session (ligne ~2772)** :
```js
        saySticky('Feed à jour · α '+(M.alpha&&M.alpha.pnl!=null?Number(M.alpha.pnl).toFixed(2):'—')+'$ · session '+(M.sessionSince?String(M.sessionSince).slice(11,16)+'Z':'—'), 12000);
```
→ convertir `M.sessionSince` en heure locale (ex. `new Date(M.sessionSince).toLocaleTimeString('fr-FR', {hour:'2-digit',minute:'2-digit'})`), jamais de Z.

**D) Cosmos — queue (ligne ~3621)** :
```js
                const t = call.ts ? new Date(call.ts).toLocaleTimeString('fr-FR', { hour: '2-digit', minute: '2-digit' }) : '--:--';
```
→ OK déjà local. Ajouter les secondes `{ hour:'2-digit', minute:'2-digit', second:'2-digit' }` pour la cohérence live.

**E) Cosmos — feed (ligne ~3632)** :
```js
                '<div class="cd-k" style="margin-top:4px;">Feed ' + new Date(window.__HUB__.generated_at).toLocaleTimeString('fr-FR') + '</div>';
```
→ idem, ajouter `+ ' (locale)'` et les secondes.

### C2 — GRAPH SYNAPSES SANS BULLES (relook neurone/synapse)
L'ancien canvas `#synapses` doit devenir un VRAI graphe synapse : **plus de bulles** (pas de cercle plein avec texte dedans). Les noms doivent être **toujours lisibles, jamais superposés**.

Modifier la section `// soma nodes` dans `drawSynapses()` (lignes ~2330-2362). Code actuel :
```js
    // soma nodes
    Object.keys(nodes).forEach(id=>{
      const n=nodes[id];
      const x=n.x*W, y=n.y*H;
      const r = id==='cockpit'?22: (id==='ace'||id==='pont'?16:13);
      const glow = n.lv>=2 ? 0.55+0.25*Math.sin(synapseT*3+x) : n.lv===1? 0.25 : 0.08;
      synCtx.beginPath();
      synCtx.fillStyle=`rgba(0,0,0,.55)`;
      synCtx.arc(x,y,r+6,0,Math.PI*2); synCtx.fill();
      synCtx.beginPath();
      synCtx.strokeStyle=n.col;
      synCtx.globalAlpha=0.25+glow;
      synCtx.lineWidth=2;
      synCtx.arc(x,y,r+4+glow*6,0,Math.PI*2); synCtx.stroke();
      synCtx.globalAlpha=1;
      synCtx.beginPath();
      synCtx.fillStyle=n.lv===0?'#2a2218':n.col;
      synCtx.arc(x,y,r,0,Math.PI*2); synCtx.fill();
      synCtx.fillStyle=n.lv===0?'#8a7a55':'#050804';
      synCtx.font='bold 10px Orbitron';
      synCtx.textAlign='center'; synCtx.textBaseline='middle';
      synCtx.fillText(n.label, x, y+1);
      if(id===synSel){
        synCtx.strokeStyle='#eaf6ff'; synCtx.globalAlpha=0.95; synCtx.lineWidth=1.6;
        synCtx.beginPath(); synCtx.arc(x,y,r+10+2*Math.sin(synapseT*4),0,Math.PI*2); synCtx.stroke();
        synCtx.globalAlpha=1;
      } else if(id===synHover){
        synCtx.strokeStyle=n.col; synCtx.globalAlpha=0.85; synCtx.lineWidth=1.5;
        synCtx.beginPath(); synCtx.arc(x,y,r+8,0,Math.PI*2); synCtx.stroke();
        synCtx.globalAlpha=1;
      }
    });
```
Règles pour le nouveau rendu :
- **Nœud = petit soma** (point/disque de rayon 4-6 px, PAS de gros cercle) avec halo lumineux coloré `n.col` (état ON/SLOW/OFF conservé).
- **Label écrit à côté du soma** (jamais dedans), avec une fine « leader line » du soma vers le label, police `Share Tech Mono`/Orbitron 11-12 px, couleur `#e8dcc0` (ou `n.col` pour le survol), ombre noire pour la lisibilité.
- **Anti-chevauchement simple** : le label est placé selon la position du nœud (à droite si x < 0.5·W, à gauche sinon ; en dessous si y < 0.5·H, au-dessus sinon), avec un petit décalage constant. Si 2 labels se chevauchent (distance entre leurs boîtes < 10 px), décaler verticalement le plus bas de +14 px (passe de correction en Y). 11 nœuds max → faisable.
- `synSel`/`synHover` : garder l'anneau de sélection + label surligné plus gros.
- Le `meta` (`graph-meta`) et `graph-pulse-lab` restent inchangés.
- Le fond (nébuleuse, micro-étoiles, dendrites courbes, sparks, bursts) reste inchangé — c'est déjà un bon rendu synapse.

### C3 — COSMOS RELOOK : labels lisibles + beau (le HUB mérite un super graphique)
Le graphe COSMOS (`buildNodes` + `drawNodes`) doit devenir beau ET lisible :
- **Hub central** : garder le style actuel (anneaux orbitaux) — il plaît.
- **Providers** : remplacer le layout circulaire serré par une **orbite aérée** (rayon `R = min(W,H)*0.36` → `*0.42`, et si plus de 8 providers, répartir sur 2 anneaux concentriques pour éviter les superpositions).
- **Labels** : NE PAS écrire les noms sous les nœuds de façon superposée. Utiliser le même système que C2 : leader line + label décalé selon la position (droite/gauche/haut/bas selon le quadrant), anti-chevauchement vertical. Le nom doit être lisible en permanence (pas seulement au survol).
- **Tooltip** (`#cosmos-tooltip`) et **fiche détail** (`#cosmos-detail`, clic) : CONSERVÉS tels quels (le user les adore : « les fenêtres d'information top »).
- Palette : CONSERVER les couleurs actuelles du cosmos (cyan `#7de7ff`, violet `#b388ff`, vert `#7CFF6B`, ambre `#ffc857`, rose `#ff6ad5`) — le user aime les couleurs du web actuel. Ne change que la disposition/lisibilité.

Modifier `buildNodes()` (ligne ~3195, le placement `target` des providers) et `drawNodes()` (ligne ~3540, la partie labels). Code actuel (placement) :
```js
        // Providers sur un cercle
        const step = data.length ? (Math.PI * 2) / data.length : 0;
        data.forEach((p, i) => {
            const angle = i * step - Math.PI / 2;
            const color = !p.enabled ? palette.red : ((p.calls_24h || 0) === 0 ? palette.idle : palette.acid);
            const radius = Math.max(13, Math.min(22, CFG.nodeBase + (p.calls_24h || 0) * 0.25));
            nodes.push({
                id: p.id, type: 'provider', x: 0, y: 0, vx: 0, vy: 0,
                radius: radius, color: color,
                label: CFG.labels[p.id] || p.id,
                target: { x: Math.cos(angle) * R, y: Math.sin(angle) * R },
                data: p
            });
        });
```

### C4 — TABLEAUX CÔTÉ À CÔTÉ (fin des lignes vides)
Les cartes de droite (`cosmos-right`) sont empilées en colonne → lignes vides entre les infos. Les mettre **côte à côte** (grille).

HTML actuel (lignes ~1310-1325) :
```html
    <div class="cosmos-right">
        <div class="cosmos-card">
            <h3>🌌 Budget Cloud</h3>
            <div id="cosmos-budget"></div>
        </div>
        <div class="cosmos-card">
            <h3>⚡ File d'attente Live</h3>
            <div id="cosmos-queue" class="cosmos-queue"></div>
        </div>
        <div class="cosmos-card">
            <h3>📊 Quotas par Tâche</h3>
            <div id="cosmos-tasks"></div>
        </div>
        <div class="cosmos-card">
            <h3>🖥️ État du Hub</h3>
            <div id="cosmos-health"></div>
        </div>
        <details class="cosmos-card">
            <summary style="cursor:pointer; color:#7de7ff; font-family:'Orbitron',sans-serif; font-size:12px;">
                📡 Événements Récents
            </summary>
            <div id="cosmos-events" class="cosmos-events"></div>
        </details>
    </div>
```
Changement :
- CSS `.cosmos-right` (ligne ~768) : `display:flex; flex-direction:column; gap:15px` → **`display:grid; grid-template-columns:repeat(2, minmax(0,1fr)); gap:12px; align-content:start`**.
- `cosmos-budget` + `cosmos-health` dans la 1re colonne, `cosmos-queue` + `cosmos-tasks` dans la 2e → ordre DOM : Budget, État du Hub, File d'attente, Quotas (réordonner les divs), puis `details` Événements en `grid-column: 1 / -1`.
- Sur petits écrans (media query existante ligne ~696) : repasser en 1 colonne.
- Ajouter un mini-header live dans `cosmos-health` : « MAJ HH:MM:SS (locale) » qui se met à jour à chaque polling (voir C5).

### C5 — LIVE : POLLING hub.json (10 s)
Le `window.__HUB__` doit se rafraîchir en continu. Ajouter, dans le bloc COSMOS (l'IIFE qui contient `renderCosmos`), un poller :
```js
    // LIVE : le feed hub.json est régénéré par launchd (~120s) et servi avec no-store.
    // On le relit toutes les 10 s pour que l'état du HUB soit toujours frais.
    function pollHubLive() {
      fetch('hub.json', {cache: 'no-store'})
        .then(r => r.json())
        .then(data => {
          window.__HUB__ = data;
          buildNodes();
          renderCosmos();
          const meta = document.getElementById('graph-meta');
          if (meta && data.generated_at) {
            const age = Math.max(0, Math.round((Date.now() - new Date(data.generated_at).getTime()) / 1000));
            meta.textContent = 'HUB LIVE · MAJ ' + new Date(data.generated_at).toLocaleTimeString('fr-FR') + ' · ' + age + 's';
          }
        })
        .catch(() => { /* hub.json pas encore prêt — on réessaiera */ });
    }
    pollHubLive();
    setInterval(pollHubLive, 10000);
```
- Le premier appel au chargement + toutes les 10 s.
- Après chaque mise à jour, `buildNodes()` + `renderCosmos()` → le graphe ET les cartes (budget, file d'attente, quotas, santé) se rafraîchissent en direct, sans recharger la page.
- Garder le bouton `↻` (`__cosmosRefresh`) existant.
- IMPORTANT : le `#cosmos-health` doit afficher l'état du hub de façon claire (OK/NOK), le nombre de providers, et la MAJ (locale).

## CONTRAINTES GLOBALES (non négociables)
1. JS vanilla (aucune lib externe, pas de D3 — canvas 2D déjà en place).
2. Le fichier est chargé par pywebview/Brave : `fetch` relative OK, pas de CORS (même origine :17800).
3. Aucune modification de la structure des autres onglets (OPS, THERMO, BOARD, VOL, STRATÉGIE).
4. Tous les blocs `renderCosmos` (budget, queue, tasks, health, events) restent fonctionnels — ne fais que modifier l'affichage (heure locale, grille), pas la logique de données.
5. Le rendu doit être SOBRE et LISIBLE, style « hedge fund » : pas de surcharge, pas d'effets qui fatiguent, mais la touche cosmique/CRT actuelle conservée.
6. Produis des blocs `BEFORE → AFTER` complets et précis (je fais le remplacement à l'identique des chaînes), ou le code complet des fonctions modifiées avec leur nom exact. Pas de numéros de lignes inventés, pas de fonctions inexistantes.

## SORTIE ATTENDUE
Pour chaque chantier C1..C5 : un bloc `### Cx — <nom>` avec :
- l'ANCIEN code (extrait exact, tel quel),
- le NOUVEAU code complet à coller,
- éventuellement le CSS à ajouter/modifier (avec l'ancien extrait CSS).
Si tu ajoutes de nouvelles fonctions, donne-les complètes. Sois précis — chaque `BEFORE` doit matcher le code réel du fichier.
