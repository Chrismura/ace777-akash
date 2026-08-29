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

## PROCHAINES ÉTAPES (recommandations famille à implémenter)

- [ ] β dynamique de contagion (Signal 3) — priorité haute (faille 2)
- [ ] Persistance 3 ticks + fraîcheur 1500 ms (croisement) — faille 1
- [ ] Normalisation SAPI par volatilité 1h + heures creuses — faille 3
- [ ] Dynamic Spread Percentile (remplace 70 bps fixe)
- [ ] PathRegistry centralisé + wrapper plists (erreurs répétées)

## Fichiers liés
- Avis complets : `Index_Maison/scripts/CONSULTATION_FAMILLE_OEUVRES_20260829/`
- SPEC SAPI : `Index_Maison/SPEC_SAPI_POUSSIERE_20260829.md`
- Code SAPI : `Index_Maison/CODE_SAPI_POUSSIERE_20260829.md`
- Deepdive RIZE : `hulk-mexc/docs/DEEPDIVE_RIZE_20260829.md`
