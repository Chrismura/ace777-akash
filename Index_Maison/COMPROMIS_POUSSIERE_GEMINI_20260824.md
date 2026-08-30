# COMPROMIS POUSSIÈRE — GEMINI (24/08/2026) — L'INDICATEUR AU TOP

> **Contexte** : Christophe a demandé de finir la consultation sur l'indicateur
> POUSSIÈRE / BLOCS PRIVATISÉS et son ensemble — « je veux cet indicateur au top
> de son fonctionnement et incassable » — en méthode DIRECTEUR D'ENTRETIEN :
> Gemini conçoit sans nos valeurs, on vérifie, on donne des indices si besoin,
> on pousse jusqu'à « ON NE PEUT PLUS FAIRE MIEUX », puis CONFRONTATION avec
> notre setup réel pour trouver le MEILLEUR COMPROMIS (pas qui a raison).
> **Réalisé par** : Buffy (directeur) + Gemini (conceptrice), 24/08, 6 tours,
> ~26 s d'API au total (direct, pas le hub). Source : `scripts/CONSULTATION_GEMINI_POUSSIERE_20260824/TOUR1-6.md`.

---

## Les 5 tours du dialogue

| Tour | Rôle | Résultat |
|---|---|---|
| 1 | Contexte généraliste (ZÉRO valeur de notre part) | Gemini propose un design : 15 s / 1 h / warm-up / seuils |
| 2 | Indices sur 3 incohérences (15 s trop agressif, volume 1,5 Mo impossible, unité octets) | Elle corrige : 120 s, seuils réconciliés 15 % + 100 BTC |
| 3 | Indices volume exact, normalisation du score, validation réaliste | Elle corrige : volume = somme exacte des satoshis, score normalisé 50/50, backtest 19-20/08 |
| 4 | Poussée au plafond (angles morts de la chaîne) | **« ON NE PEUT PLUS FAIRE MIEUX »** + 7 remparts (verrou, CORRUPT_BLOCK, cold reboot, baseline 3σ…) |
| 5 | Confrontation : notre setup réel vs le sien | Compromis final point par point (ci-dessous) |
| 6 | **Confrontation TERRAIN** : j'ai testé l'API en direct → le « volume exact via le résumé du bloc » est IMPOSSIBLE (header seul) | Elle adapte : échantillonnage borné 75 tx + 0,25 s, zéro appel en régime normal |

---

## LE SETUP FINAL DE COMPROMIS (validé des deux côtés)

| Point | Valeur retenue | Origine | Justification |
|---|---|---|---|
| **Snapshot** | **120 s** | ✅ Accord (les deux) | 30 requêtes/h, safe free-tier, 5 snapshots par bloc de 10 min |
| **Fenêtre** | **60 min** (≈ 6 blocs) | ✅ Accord | Couvre le cycle de vie des tx à frais bas |
| **Fiabilité** | **≥ 6 snapshots** (~12 min = 1 bloc complet) | 🤝 Compromis (nous 3 / elle 15) | 3 = trop court (carnet à peine rempli), 15 = trop pénalisant après micro-coupure ; 6 = un cycle complet de propagation vu |
| **Anti-faux 100 %** | `taux_non_fiable` = null (jamais de données fabriquées) | ✅ Notre principe, elle a cédé | « En onchain, une fausse donnée vaut infiniment pire qu'une absence » |
| **Volume** | **Échantillonnage borné 75 tx** (somme des outputs, 0,25 s entre appels, uniquement si taux ≥ 10 %) | 🤝 Adapté (TOUR 6) | Le « volume exact via le résumé du bloc » est IMPOSSIBLE (testé en direct : `/api/block/{hash}` = header sans txs). Somme = borne inférieure honnête (pas d'extrapolation médiane ×N, qui fausserait les queues lourdes = cas baleine). Zéro appel en régime normal |
| **Alerte** | **τ ≥ 10 % ET vol ≥ 500 BTC** (matrice du Juge) | ✅ Notre double condition, elle a validé | Sa formule (score ≥ 65) aurait RATÉ 10 % + 500 BTC (score 60) ; l'ET logique impose la corrélation taux↔volume |
| **Garde-fous** | SIGALRM + écriture atomique + repli mempool↔blockstream (déjà en place) **+ verrou fcntl anti-doublon + ancrage fraîcheur par hauteur de bloc** | ✅ Sa proposition, adoptée | fcntl = fini les doublons (le cas vigie du 24/08) ; hauteur de bloc = anti-veille macOS (monotonic se fige) |

---

## MISE EN ŒUVRE — APPLIQUÉ (GO Christophe 24/08)

**`detecter_bloc_privatise.py`** — 4 corrections validées à 100 % appliquées :

1. **`MIN_SNAPSHOTS` : 3 → 6** — le faux 100 % du 24/08 s'est résorbé à 6 snapshots ; 6 = un cycle complet de propagation vu. ✅
2. **Verrou `fcntl` anti-doublon** (`data/.bloc_privatise.lock`) — un seul process d'analyse à la fois. Testé en réel : 2 instances manuelles refusées pendant que launchd tenait le verrou → une seule analyse, aucune corruption. ✅
3. **Ancrage hauteur de bloc** — chaque snapshot enregistre `blocks/tip/height` ; la fenêtre glissante = 60 min OU dernier 6 blocs (anti-dérive d'horloge / veille macOS). Vérifié : le carnet porte désormais `hauteur: 963837/963838`. ✅
4. **Volume : échantillon 50 → 75 tx, sleep 0,2 → 0,25 s** — adapté à la réalité API (voir TOUR 6). ✅

**Rejeté avec preuve** : le « volume exact via `/api/block/{hash}` » — testé en direct le 24/08 : mempool.space ET blockstream renvoient le HEADER sans les txs (`tx_count: 5719` mais `len(txs)=0`). La valeur par tx n'existe qu'en pagination 25/appel ou 1 appel/tx → impossible sans exploser l'API. On garde la somme des outputs échantillonnés (borne inférieure honnête), et PAS l'extrapolation médiane ×N (fausserait les queues lourdes = le cas baleine OTC).

**Vérifié après application (run réel 24/08 09:14Z)** : taux 0,65 %, 27 snapshots, `taux_non_fiable: false`, pas d'alerte, veille SAIN. La chaîne reste verte.

### Ce qui ne change pas
- 120 s, fenêtre 60 min, repli multi-source persisté, SIGALRM, écriture atomique, kill-switch, mode actif/observation.
- **`veille_degradation.py`** : rien à changer (gère déjà `taux_non_fiable`)
- **`pont_onchain.py`** : rien à changer (l'indice d'affichage reste 0,5/0,3/0,2 ; l'alerte est portée par la double condition)

---

## Preuves
- Dialogue complet : `scripts/CONSULTATION_GEMINI_POUSSIERE_20260824/TOUR1-6.md` + `etat.json`
- Gemini conclut TOUR 4 : « ON NE PEUT PLUS FAIRE MIEUX » ; TOUR 5 : setup de compromis « chirurgical » ; TOUR 6 : adaptation au terrain
- Test API en direct (24/08, bloc 963837) : `/api/block/{hash}` = header seul, pas de `txs`
- Run réel après application : `data/bloc_privatise.json` (09:14Z, taux 0,65 %, fiable, pas d'alerte)
- L'enquête 20/08 (résidu 0,5-8,3 % à 60 s, déterminisme par bloc) et la release 21/08 (double condition Juge) sont la base de vérification des valeurs

— Compromis établi avec Gemini le 24/08/2026, appliqué et vérifié le même jour (GO Christophe).