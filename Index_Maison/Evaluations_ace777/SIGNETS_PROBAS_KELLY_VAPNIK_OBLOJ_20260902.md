# SIGNETS_X — LES PÉPITES PROBABILITÉS / HASARD / THÉORIE DES JEUX
> Trouvaille du 2026-09-02 · Buffy (lecture) + Gemini (R27-R28, session EDGE_JUILLET) · demandé par le propriétaire

## État des lieux du coffre
- `~/Documents/Obsidian_ACE777/Signets_X/` : **836 bookmarks X** (dossiers mensuels 2025-01 → 2026-09), un fichier par post.
- **138 seulement évalués** par la famille (lots 6-31, cf. `TAGS_138_SIGNETS_RECAP.md`) → **~700 jamais évalués**.
- Un fiche `Bookmark_Master_N.md` (138) = ancien index, la matière vit dans les dossiers `2026-MM/`.

## Les 4 pépites d'or (lues intégralement)

### 1. Kelly / Bernoulli / Thorp — le sizing décide de la survie
`2026-08/2026-08-07 @CorvusXBT - There is a bet with infinite expected value...` (id 2085803166231392311)
- Paradoxe de Saint-Pétersbourg → Bernoulli 1738 (maximiser le log de la richesse) → John Kelly 1956 (fraction optimale de mise) → Ed Thorp (29 années profitables consécutives).
- **Citation clé** : « Finding an edge and sizing it are two completely different skills. The famous funds that detonate are rarely wrong about their edge. They are wrong about their size. The optimal bet is smaller than you think, and the cost of ignoring that is not lower returns, it is eventual zero. »
- **Lien ACE** : nos masses BETA 200 / ALPHA 800 (levier x13) n'ont jamais été validées par un calcul de Kelly. Le gate H est un Kelly approximatif (ne miser que quand la machine gagne).

### 2. Vapnik — le théorème de l'overfitting par la recherche elle-même
`2026-08/2026-08-01 @CorvusXBT - In 1968 he proved...` (id 2083478661131378815, déjà tagué `validation-anti-overfit` par la famille)
- **Citation clé** : « Test one rule on ten years and a good result is evidence. Test ten thousand rules on the same ten years and the best one is arithmetic. The strategy you found is only as trustworthy as the number of strategies you rejected to find it. »
- **Lien ACE** : nos 28 rounds de variantes = l'espace d'hypothèses géant que Vapnik met en garde. Le Shadow Mode 14 jours = le test hors-échantillon qui seul sépare la découverte de l'artefact.

### 3. Obłój — théorème d'échantillonnage optionnel (Oxford)
`2026-07/2026-07-31 @Di_Krass_ - Every trader believes the edge is in the exit` (id 2083296438549983286)
- **Citation clé** : « If the game is fair, no exit rule on Earth makes you money. You can't out-time a fair game. You can only be the one who owns it. »
- **Lien ACE** : prouve mathématiquement le diagnostic R26 — dans le chop, le jeu net (frais 1,76/trade) est quasi négatif, aucun trailing ne peut le sauver. Le salut vient du FILTRE D'ENTRÉE (gate H, murs >40$), jamais des sorties.

### 4. t-stat ≥ 3 — le seuil pratique des quants
`2026-07/2026-07-31 @0x_Punisher - ONE NUMBER TELLS YOU IF YOUR EDGE IS REAL` (id 2083258282739687569)
- **Citation clé** : « School told you t above 2 counts as significant. In trading that's not nearly enough. You want 3 or higher. » (raisons : fat tails + tests multiples)
- **Lien ACE** : notre edge validé est à **t = 2,66 (BETA) / 2,17 (ALPHA)** — au-dessus du seuil académique, SOUS le seuil pratique. À recalculer en NET (après frais) au rapport J+1.

## Secondaires
- [5] Diaconis / dés pipés (`2026-08-04 @Flandermaxx`) : « Fairness is not a property of the die. It is a property of the die plus the throw plus the surface. » → l'edge = signal × régime × frais. Métaphore validée par Gemini R27.
- [6] Théorie des jeux infinis (`2026-08-01 @alexeixbt`) : ne pas chercher à battre, chercher à rester dans le jeu.
- [7] Vernon Smith Nobel (`2026-08-07 @0xSpivach`) : psychologie, edge cognitif hors conformité.
- Hors sujet ACE : Shor/crypto quantique, dérivées MIT, « 25 quants » (teaser vide).

## Validation croisée Gemini (R27, intégral archivé dans GEMINI_SESSION_EDGE_JUILLET)
Sa conclusion : **« ACE777 ne gagnera jamais par la complexité de ses sorties, ni par la multiplication de ses règles, mais par la rigueur de son sizing (Kelly), la conscience de ses sur-optimisations (Vapnik), et son refus de trader un jeu dont l'intermédiaire (les frais) possède la table (Obłój). La vérité était déjà écrite dans les signets du coffre. Il ne restait plus qu'à la faire traverser au code. »**
- Kelly → condamne le levier x13 historique d'ALPHA.
- Vapnik → le Shadow Mode 14j = seul juge de paix.
- Obłój → exception à son théorème : le gate H isole des sous-régimes NON fair-play (Orages, Mars) ; dans le neutre, aucun trailing ne sauve.
- t-stat → nos 2,66/2,17 = « mirage statistique » tant que < 3.

## Suit en R28 (contexte J0 + trend BTC fourni par Buffy)
Verdict Gemini : système « vivant mais fragile » · seuil médiane 1,53 < 2,00 FRANCHI · **position flottante BETA = le vrai juge de paix** (syndrome « 100% win rate sur les sorties fermées, explosion sur les positions ouvertes ») · gel R24 maintenu, tout se joue à J+1.

## À faire plus tard (pas maintenant, gel)
- [ ] Recalculer t-stat en NET sur ALPHA/BETA.
- [ ] Scan des ~700 signets non évalués (même méthode : titres puis lecture ciblée).
- [ ] Discipline de sizing type Kelly à discouter APRES J+14 si le Shadow survit.
