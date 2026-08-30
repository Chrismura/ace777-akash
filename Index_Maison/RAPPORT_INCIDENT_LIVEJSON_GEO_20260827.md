# RAPPORT INCIDENT — live.json écrasé / geopol disparu — 27/08/2026

## Symptôme (signalé par Christophe)

« Cortana me dit que geo ne marche pas. » → `thermo/live.json` réduit à 11 clés
(2 307 o) au lieu de 64 (≈15 ko) : geopol, mark, gex, rbf, pipeline_health absents.
Le juge affichait `geopol=[absent]`. Le cockpit perdait la carte géopolitique.

## Cause racine — DEUX incidents distincts (honnêteté totale)

### 1. MA faute (18:58) — test sentinel.py

Pour tester l'ajout du timestamp, j'ai écrit un `live.json` de test FAKE (11 clés :
chg1h, volQuote, funding, whaleUsd, liq24Usd, sdi, ipt, onchain, longShort,
takerRatio, fearGreed) dans `thermo/live.json` (fichier de PRODUCTION) et mon
`finally` n'a restauré que `sentinel_history.json`, PAS live.json.
→ live.json est resté écrasé. **Inadmissible : un test ne doit jamais écrire dans un
fichier de production sans restore systématique dans le finally.**

### 2. Race condition documentée (25/08) + pérennisation par le pont_onchain

`consulter_famille_pipeline_unifie_20260825.py` ligne 35 (écrit par l'IA du 25/08) :
> « RACE CONDITION : 3 scripts écrivent dans live.json séparément »

Écrivains identifiés :
- `thermo_quotidien_free.py` → payload COMPLET 64 clés (write_text ligne 1128)
- `pont_onchain.py` → injecte onchain via SafeLiveWriter (merge propre, fcntl+tmp+os.replace) ✓
- ~~`cortana_dashboard.py`~~ → **INNOCENT (corrigé dans ce rapport)** : sa ligne 276 redirige
  déjà THERMO_LIVE vers tmp/ avant d'écrire (ligne 302 écrit dans tmp/live.json).
  L'accusation initiale était erronée — vérifiée ligne à ligne le 27/08 21:30.

Le mtime 21:06 observé = le **pont_onchain** (cycle 5 min) qui a relu mon fichier corrompu
(11 clés) et l'a réécrit en mergeant onchain dedans : le fichier est resté corrompu
(geopol/mark/gex absents) mais le mtime se mettait à jour à chaque cycle. C'est la
« pérennisation » du dommage par un écrivain qui ne vérifie pas la complétude de la source.

**Leçon 2 : un merge (pont_onchain) doit vérifier que la source est complète avant de
s'appuyer dessus — sinon il propage un fichier déjà corrompu.**

## Restauration (21:11)

1. live.json restauré depuis `thermo/live.js` (20:53, la source propre 64 clés,
   geopol 0.3462) + OUTBOX cohérent (64 clés, geopol OUI) = double vérification.
2. Run thermo 21:12 → payload complet réécrit : **geopol 0.3483 · 5/5 modules ·
   mark 80 197 · gex ok · onchain ok**.
3. Le juge lit : `geopol=0.3483 🟢 n=5/5 ml=calme`.
4. Watch 60s : pont_onchain (5 min) fusionne SANS casser (64 clés stables).
5. sentinel_history intact (66 mesures, timestamp ajouté fonctionnel, 0 pollution).

## Avis famille (6/6 GO-AVEC-RÉSERVES, 19:19Z)

GEMINI, DEEPSEEK, ULTRA, INFERX, GROK, JUGE — convergence :
1. **Verrou fcntl obligatoire** sur toute écriture (déjà dans SafeLiveWriter).
2. **Fusion stricte** : un écrivain partiel ne peut JAMAIS supprimer des clés hors de
   son scope (ne jamais écrire `open(..., "w")` avec un dict partiel).
3. **Option robuste** : fragments isolés `thermo/registry/` (chaque module écrit son
   fragment, un assembleur unique construit le payload) — élimine la classe entière
   de bugs.
4. Réserve commune : les 36 lecteurs tolèrent os.replace (vérifié : pont_onchain
   fonctionne déjà ainsi).

## Actions appliquées (27/08 21:30)

1. **Durcissement `cortana_dashboard.py` (défensif, car le script était innocent)** :
   - garde `_verifier_tmp()` : refuse d'écrire si THERMO_LIVE/MISSION/ADA_LIVE/SAISON_LIVE
     ne pointent pas vers tmp/ (protection anti-écrasement de la classe d'erreur) ;
   - `restore()` désormais dans un `finally` garanti même si le test plante.
   Testé : syntaxe OK + run_tests() vert (le script de test reste fonctionnel).
2. **Mon fix sentinel.py (timestamp)** : conservé (utile), mais la leçon est tracée :
   un test écrit TOUJOURS dans un tmp et restaure TOUT dans le finally.
3. **Restauré** : live.json complet (64 clés, geopol 0.3483, mark 80 197) depuis live.js.

## À décider (famille : 6/6 GO-AVEC-RÉSERVES)

1. **Pont_onchain : vérifier la complétude de live.json avant de merger** (sinon il
   propage un fichier corrompu — leçon 2 ci-dessus).
2. **Interdire l'écriture brute** de live.json : toute écriture passe par
   SafeLiveWriter + merge (règle à documenter dans le code).

## Leçon tracée

- Un test écrit TOUJOURS dans un tmp, JAMAIS dans un fichier de production ;
  si exception : finally restaure TOUT ce qui a été touché.
- La race condition live.json est documentée comme R11 dans l'audit Hulk.
