# 🏛️ AUDIT FAMILLE DES 3 ŒUVRES DU 29/08 (consultation 6 membres)

> Christophe, 29/08 : « faire audit famille. TRÈS IMPORTANT CAR SOUVENT ERREURS
> RÉPÉTÉES, BRANCHER NOS ŒUVRES... vérifier TOUT. »
> Session : `CONSULTATION_FAMILLE_OEUVRES_20260829` (6/6 réponses : GEMINI,
> DEEPSEEK, JUGE, ULTRA, INFERX, GROK).

---

## LE VERDICT GLOBAL (unanimité)

| Œuvre | Verdict famille | Réserve principale |
|---|---|---|
| **① Croisement externe** | **GO AVEC RÉSERVES** | panne corrélée des 2 sources + faux positifs en forte volatilité |
| **② Signal 3 (livre écorché)** | **GO AVEC RÉSERVES** | contagion BTC binaire aveugle + spread fixe 70 bps inadapté |
| **③ SAPI poussière** | **GO (JUGE/ULTRA/INFERX) · GO CONDITIONNEL (DEEPSEEK/GEMINI/GROK)** | proxy carnet spot = bruit de mesure + corrélation −0.275 faible |

**Le JUGE tranche** : « Codez le SAPI avec le proxy MAIS avec un cordatif
d'isolation (normalisation volatilité 1h + filtre heures creuses UTC). GO. »

## LES FAILLES IDENTIFIÉES (les 3 récurrentes)

### Faille 1 — « Consensus corrompu » (croisement)
> GEMINI : « Si Binance et MEXC partagent le même cloud (AWS) ou subissent une
> latence corrélée, votre écart 5 % valide un prix mort. » INFERX : « deux
> sources qui mentent de concert = aveugle. » ULTRA : « split-brain asymétrique. »

**Correctif famille** : test de **fraîcheur obligatoire** (timestamp delta
< 1500 ms) + **persistance 3 ticks** avant fail + 3e source décentralisée passive.

### Faille 2 — « Effet domino hystérétique » (contagion BTC du Signal 3)
> GROK : « btc_spoof_pct > 5 % abaisse les seuils de TOUTES les paires →
> hyper-sensibilité en cascade, blocage de trading légitime. » JUGE : « un
> spoofing inoffensif sur BTC → siège sur-sensibilisé sur 50 paires. »

**Correctif famille** : coefficient de transmission **β dynamique** (corrélation
glissante 1h BTC vs paire) — si β < 0,2-0,4, la contagion est ignorée pour cette
paire. + **Dynamic Spread Percentile** (spread < percentile 30 des 24h) au lieu
du seuil fixe 70 bps.

### Faille 3 — « Le proxy carnet spot » (SAPI)
> DEEPSEEK : « Ne pas coder avec le proxy seul — un MM légitime qui rééquilibre
> déclenchera une fausse alerte. » JUGE : « Heure creuse (02-06 UTC) élargit le
> spread naturellement → le proxy confond manque de MM avec poussière. »

**Correctif famille** : normaliser le proxy par la **volatilité 1h (σ)** + poids
faible en heures creuses UTC + **terme d'entropie temporelle** (régularité
d'intervalle quasi-robotique d'un script vs chaos retail).

## LES ERREURS RÉPÉTÉES — COMMENT LES RENDRE STRUCTURELLEMENT IMPOSSIBLES

Le point « TRÈS IMPORTANT CAR SOUVENT ERREURS RÉPÉTÉES » — 4 barrières famille :

| Piège récurrent | Barrière structurelle (famille) | Statut |
|---|---|---|
| **Chemins relatifs/absolus** (script qui plante en plist) | Config centralisée `PathRegistry`, validée au démarrage (`sys.exit(1)` si absente) | ⏳ à faire |
| **Plists silencieuses** (process meurt sans alerte) | Wrapper de surveillance → stderr vers webhook + fail-safe (3 morts en 5 min = arrêt) | ⏳ à faire |
| **Source API unique** (mempool down = brique morte) | Circuit breaker + fallback obligatoire (fait pour fee_pressure 29/08 → blockstream) | ✅ fait (partiel) |
| **Fichiers JSONL corrompus** (écritures concurrentes) | Écriture atomique (tmp + os.replace) systématique | ✅ fait (sante_index, pont) |

## CE QUI A ÉTÉ FAIT APRÈS L'AUDIT (même session)

1. **SAPI codé** par le codeur (`CODE_SAPI_POUSSIERE_20260829.md`) + **2 corrections
   supervision** (chemin murs_observations, clé `pair` vs `paire`) → testé : score 0.499 ✓
2. **SAPI branché partout** (le bug de branchage trouvé ET corrigé) :
   - `silent_drain_index.py` : calcule + écrit `sapi` dans sdi_latest.json ✓
   - `thermo_quotidien_free.py` : **propagait sdi/ipt/rbf mais PAS sapi** → corrigé ✓
   - `cortana_analyse.py` : lexique + lecture `sapi` ajoutés → Cortana peut l'analyser ✓
   - `sante_index.py` : chaîne **SAPI POUSSIÈRE** au cockpit → **14/14 chaînes OK** ✓
3. **Vérification complète du branchage** : plists chargées (croisement, signal3,
   thermo, veille-signal) + données fraîches (7/7 ✓) + mempool.space REVENU (200) ✓

## ✅ CORRECTIONS FAMILLE APPLIQUÉES (29/08 soir — GO Christophe « GO 1,2 »)

> Christophe : « GO 1,2 » → ① RIZE passe en observation_setup, ② appliquer les
> corrections famille au SAPI et au Signal 3.

### GO ① — RIZE en OBSERVATION (prix seul)
- `paires_croisement.json` : RIZE déplacé de `deepdive_faits_29aout` vers
  `observation_setup` → **prix croisé SEUL, aucune décision** (profil
  manipulee_fragile documenté dans le deepdive). `deepdive_faits_29aout` est
  maintenant vide (toutes les paires traitées).

### GO ② — Corrections famille appliquées et TESTÉES

**Signal 3 (`signal3_livre_ecorche.py`) — faille 2 (contagion binaire) :**
1. ✅ **β_asset dynamique** : corrélation de Pearson glissante 1h entre
   `btc_delta_pct` et `price_delta_pct` (alignés ±5 s), calculée TOUJOURS pour
   l'audit. La contagion n'est appliquée à une paire QUE si β ≥ 0,3. Testé :
   XRP β=0,18 (n=33) → paire découplée → contagion ignorée ✓. Paires sans
   données 1h → fail-open β=1,0 (prudence, documenté).
2. ✅ **Asymétrie directionnelle** : contagion UNIQUEMENT si delta_btc < 0
   (phase baissière). Testé en direct : btc_spoof=5,11 % mais delta_btc=+0,20
   (haussière) → PAS de contagion ✓ (c'était le cas réel de ce soir).
3. ✅ **Filtre MAD** : le drop n'est retenu que s'il dépasse médiane + 3×MAD
   des 10 dernières mesures (anti-jitter HFT).
4. ✅ **Écriture atomique** (tmp + os.replace) pour les 2 JSON.

**SAPI (`silent_drain_index.py`) — faille 3 (proxy carnet spot) :**
1. ✅ **Normalisation σ1h** : le proxy spread est divisé par σ des 12 derniers
   spreads (≈1h). Carnet vide/volatile → σ élevé → proxy neutralisé (testé :
   spread 10 bps σ élevé → proxy 0,15 ; carnet stable → proxy 1,0) ✓
2. ✅ **Persistance 3 ticks** : alerte UNIQUEMENT si 3 runs consécutifs ≥ 0,75
   (état `sapi_etat.json`). Faux positifs isolés tués ✓
3. ✅ **Écriture atomique** pour sdi_latest.json + sapi_etat.json.

**Croisement externe (`croiser_donnees_externes.py`) — faille 1 (faux positifs) :**
1. ✅ **Persistance 3 ticks** : un fail prix n'est BLOQUANT qu'après 3 runs
   consécutifs en écart (≈1h30 à 30 min/run). Testé par simulation : tick 1 =
   « surveillance », tick 3 = « bloquant » + alerte data_quality écrite ✓
2. ✅ **Écriture atomique** (état, registre d'état, alerte).
3. ✅ État enrichi : `fails_pendants` (1-2 ticks) visible au cockpit sans alerte.

### Reste à faire (recommandations famille non couvertes par le GO)
- [ ] Dynamic Spread Percentile (remplace le seuil fixe 70 bps)
- [ ] Filtre heures creuses UTC (02-06) sur le proxy SAPI
- [ ] Terme d'entropie temporelle (SAPI)
- [ ] PathRegistry centralisé + wrapper plists (erreurs répétées)

## Fichiers liés
- Avis complets : `Index_Maison/scripts/CONSULTATION_FAMILLE_OEUVRES_20260829/`
- SPEC SAPI : `Index_Maison/SPEC_SAPI_POUSSIERE_20260829.md`
- Code SAPI : `Index_Maison/CODE_SAPI_POUSSIERE_20260829.md`
- Deepdive RIZE : `hulk-mexc/docs/DEEPDIVE_RIZE_20260829.md`
