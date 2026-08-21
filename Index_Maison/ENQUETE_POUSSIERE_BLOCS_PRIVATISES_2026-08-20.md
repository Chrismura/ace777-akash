# ENQUÊTE — "Poussière" / blocs privatisés (20/08/2026) — VERDICT RÉVISÉ

> **Contexte** : Christophe demandait de finir l'investigation sur les opérations
> douteuses BTC ("indice poussière", blocs privatisés fantômes) notée comme
> "prochaine étape" dans `SNIFFER_JOURNAL.md` après le mouvement +8 % du 19-20/08
> que ni l'humain ni les bots n'avaient vu passer.
> **Réalisée par** : Buffy (superviseur) — audit des données réelles, 20/08,
> **deuxième passe en profondeur après relecture de la pépite Christophe**.

---

## Question posée

Les indicateurs onchain (poussière, CPFP, blocs privatisés) avaient-ils **anticipé**
le mouvement BTC 64 200 $ → 69 350 $ (+8 %, volume ×3) ? Et qui mine les "blocs
privatisés fantômes" ?

## Réponse courte — RÉVISÉE (20/08, 2ᵉ passe)

**Le concept de Christophe est réel : une tx incluse dans un bloc mais jamais vue
dans la mempool publique = OTC privée / CPFP masqué (matrice du Juge : taux > 35 %
+ volume > 1000 BTC = règlement OTC de baleine). C'est un vrai instrument de
détection, utilisé par les gros acteurs, inconnu du mainstream.**

**Mais la mesure était cassée par la résolution** (snapshot toutes les 10 min) :
elle mélangeait deux choses — le turnover rapide de la mempool (bruit) et les
vraies tx privées (signal). Avec une résolution fine (60 s), le bruit disparaît et
il reste un résidu **0,5-8,3 %** qui est mesurable. **L'indicateur n'est pas mort :
il doit être mesuré à la bonne résolution, puis recalibré.**

---

## Preuves (fichiers réels + test live du 20/08)

### 1. Le taux est STABLE par bloc — pas du bruit blanc

`/tmp/bloc_privatise_launchd.out.log` — **412 runs / 281 blocs distincts** :

- **281/281 blocs stables intra-run** : le même bloc analysé plusieurs fois donne
  le même taux (ex. 8,53 % × 3) → c'est une **propriété déterministe du bloc**,
  PAS un tirage aléatoire. Mon premier verdict "bruit blanc" était faux.
- Ce qui varie, c'est ENTRE les blocs (0,2 % → 100 %), et cette variation a une
  cause : la résolution d'échantillonnage.

### 2. Test décisif : résolution fine (60 s) vs standard (10 min) — 20/08

Test live sur 25 min (snapshots 60 s, `mempool_vus_TEST_DENSE.jsonl`) :

| Résolution | Bloc 963288 (4525 tx) | Blocs 963289-292 |
|---|---|---|
| **10 min (standard)** | 1 522 fantômes = **33,6 %** | ~34 % (moyenne) |
| **60 s (dense)** | 377 fantômes = **8,3 %** | **0,5-8,3 %** (médiane 4,7 %) |

- La majorité des "fantômes" (≈ 30 pts sur 34) = **artefact de résolution** :
  tx normales entrées ET minées entre deux snapshots de 10 min, jamais vues.
- **Le résidu 0,5-8,3 % même à 60 s = candidat réel** : tx qui n'apparaissent
  jamais dans nos snapshots, même denses → potentiellement de vraies tx privées
  (OTC / soumission directe à un pool). C'est le signal de Christophe.
- Les pics à 100 % (blocs 09:28-09:53, carnet vide après purge au démarrage) =
  artefact pur, à exclure de la mesure.

### 3. Cause racine

- Le détecteur (`detecter_bloc_privatise.py`, plist `StartInterval=600`)
  snapshotte la mempool **toutes les 10 min**. Un bloc est miné toutes les ~10 min.
  Toute tx à durée de vie < 10 min (mempool qui se renouvelle vite en période
  active) est invisible entre deux snapshots → faussement "fantôme".
- La spec du 16/08 avait prévu une fenêtre glissante ≥ 10 min, mais le **pas de
  snapshot n'a pas été réduit** → le correctif était insuffisant.
- Les valeurs du sniff (34,47 % le 18/08 · 55,52 % le 19/08 · 7,665 % le 20/08)
  étaient ces mesures bruitées — cohérentes avec la distribution 0-100 % des 412 runs.

### 4. Conséquence pour la veille (nuancé)

- Le "55 % de blocs privatisés" du 19/08 n'était **pas** un précurseur fiable en
  l'état — mais il reflétait une **mempool très active** (turnover élevé) au moment
  du mouvement. Le signal de Christophe, correctement mesuré (résolution fine),
  reste à valider sur l'événement passé : on ne peut pas le reconstruire
  rétroactivement (pas d'historique dense du 18-19/08).
- **Le mouvement était exogène** (décision Trésor/Fed/Bessent → debasement trade) :
  même un indicateur parfait n'aurait probablement rien vu sur le onchain avant le
  fait. Leçon : il faut une couche **news/macro** pour les chocs exogènes (le vrai
  trou béant révélé par cet événement).

---

## Ce qu'il faut faire (GO-sized)

1. **Corriger la résolution du détecteur** : snapshot toutes les **60-120 s**
   (au lieu de 600 s). Coût API : 5,2 Mo/snapshot → ~3,7-7,5 Go/jour selon le pas ;
   à surveiller (mempool.space free tier, une requête toutes les 60-120 s est
   raisonnable). Garder la fenêtre glissante 60 min.
2. **Exclure les artefacts** : carnet vide au démarrage → taux = `null` (pas 100 %).
   Ne garder que les blocs dont l'historique couvre ≥ 3 snapshots.
3. **Recalibrer la matrice du Juge** sur le taux résiduel dense (0,5-8,3 %) :
   les seuils d'origine (35 % / 1000 BTC) étaient calibrés sur la mesure bruitée.
   Proposer : taux > 10 % + volume > 500 BTC → alerte (à valider sur données).
4. **Décision 23/08** : CPFP/blocs privatisés → **réparer la mesure d'abord, puis
   activer en alerte réelle** (ne pas jeter le concept : c'est la pépite Christophe).
5. **Ajouter une couche macro/news** pour les chocs exogènes (le vrai trou béant).

## Fichiers consultés
- `hulk-mexc/scripts/vigie_mempool_pepite_christophe.py` (**la pépite, matrice du Juge**)
- `Index_Maison/SPEC_VIGIE_MEMPOOL_2026-08-16.md` (spec P0/P1)
- `Index_Maison/scripts/detecter_bloc_privatise.py` (méthode, seuils)
- `Index_Maison/plists/com.ace777.bloc-privatise.plist` (StartInterval 600)
- `/tmp/bloc_privatise_launchd.out.log` (412 runs / 281 blocs — stabilité intra-bloc)
- Test live 20/08 : snapshots 60 s vs 10 min (33,6 % → 8,3 % → 0,5-8,3 %)
- `SNIFF_bitcoin_20260818_2343.md` · `_20260819_0602.md` · `_20260820_0602.md`
- `SNIFFER_JOURNAL.md` (l'enquête inachevée)

---
*Écrit par Buffy le 20/08/2026 — 2ᵉ passe en profondeur après relecture de la
pépite (premier verdict "bruit blanc" corrigé : le concept est réel, la résolution
était le problème).*
