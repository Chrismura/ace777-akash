# APPLICATION PAA-ACE777 — PROTOCOLE UNIQUE (20/08/2026)

> Issue de la consultation canonique de CONTESTATION (tour 1 : 6/6
> GO-AVEC-RÉSERVES 85-88 %) puis TOUR 2 (protocole unique fusionné :
> 6/6 GO-AVEC-RÉSERVES 80-92 %). Les 3 ajouts exigés par la famille ont été
> implémentés et testés. Ce document trace chaque ajout → vérification.

---

## LES 5 RÈGLES DU PROTOCOLE (déjà en place au tour 1)

| Règle | Où | État |
|---|---|---|
| 1. Interdiction de valider sans preuve brute | Wrappers + rapports | ✅ (discipline + DMS) |
| 2. Fail-fast absolu au démarrage | `GO_VORTEX_V2.sh` (lignes 43-58) | ✅ testé 3/3 |
| 3. Miroir inversé / Red Team | `veille_degradation.py --test-panne` | ✅ testé |
| 4. Double validation d'état | `sante_index.py` (launchctl + pgrep) | ✅ 8/8 chaînes |
| 5. Primauté du terminal | Toutes les boucles | ✅ (règle maison) |

## LES 3 AJOUTS EXIGÉS AU TOUR 2 — APPLIQUÉS AUJOURD'HUI

### AJOUT 1 — HEARTBEATS PAR SERVICE (JUGE + ULTRA) ✅
Détecte le « zombie fonctionnel » (process vivant mais figé) — l'angle mort du
double check.

- **Nouveau** : `Index_Maison/scripts/heartbeats.py` — pour chaque service
  critique, vérifie 3 conditions : (a) plist chargée, (b) process répond
  (daemons permanents seulement), (c) sortie de vie FRAÎCHE. Si les 3 → écrit
  `data/heartbeat/[service].ts`. Sinon → `etat/heartbeats.json` signale.
- **Plist** : `com.ace777.heartbeats` (cycle 60 s) chargée.
- **Services couverts (6)** : vigie, veille, dms, sante, superviseur_core, whales.
- ✅ **Vérifié** : SAIN 6/6 services battent.

### AJOUT 2 — LIMITES MÉMOIRE + TRACE DE MORT (ULTRA + INFERX) ✅
Attaque la cause racine probable du 19/08 (OOM silencieux) à la source.

- **Nouveau** : `Index_Maison/scripts/ajouter_limites_memoire.py` — ajoute
  `SoftResourceLimits`/`HardResourceLimits` (RSS 400 Mo, 20 process) aux plists.
- **7 plists durcies** : superviseur-process, superviseur-core,
  veille-degradation, dms-veille, heartbeats, sante-index, vigie-live
  (+ copiées dans `plists/` pour versionnage). Toutes rechargées ✅.
- **Nouveau** : `Index_Maison/scripts/trap_mort.sh` — journalise TOUTE mort
  (TERM/INT/ERR/EXIT) avec signal, rc, ligne, RSS et stack dans
  `/tmp/ace777_morts.log`. Intégré à `superviseur.sh` (celui mort sans trace
  le 19/08).
- ✅ **Vérifié** : trap testé (mort sur `false` → trace complète avec RSS).

### AJOUT 3 — CHAOS TEST SOUS LAUNCHD + DOUBLE CANAL (GEMINI + GROK) ✅
Prouve que l'alerte sort réellement, et ne dépend pas d'un seul canal.

- **Double canal dans `dms_veille.py`** :
  - CANAL A : `data/alertes/DMS_WEBHOOK.json` (webhook local, indépendant de
    la voix et du shell parent) — toujours écrit.
  - CANAL B : alerte vocale (anti-empilement).
- ✅ **Vérifié** : `--test-panne` → canal webhook écrit + alerte vocale lancée.
  (La fausse alerte « plists NON CHARGÉE » du premier essai venait de la
  fenêtre de rechargement des plists pendant le test — état réel re-vérifié :
  SAIN 3/3, toutes plists chargées.)

## ÉTAT FINAL VÉRIFIÉ (20/08 14:01Z)

- `sante_index.py` : **8/8 chaînes OK · état OK**
- `heartbeats.py` : **6/6 services battent · SAIN**
- `veille_degradation.py` : **SAIN 11/11 plists**
- `dms_veille.py` : **OK 3/3**
- Plists critiques : **7/7 durcies et chargées**

## PROCHAINE ÉTAPE (critère final famille)

**Run 72 h d'autonomie** (testnet/paper) sans intervention humaine — le
critère de validation final posé par DEEPSEEK (e) : « aucun système ne peut
être qualifié de production-ready s'il nécessite une intervention avant 3
jours pleins de fonctionnement autonome ». À lancer avec le fail-fast actif
+ surveillance complète. Décision Christophe requise.
