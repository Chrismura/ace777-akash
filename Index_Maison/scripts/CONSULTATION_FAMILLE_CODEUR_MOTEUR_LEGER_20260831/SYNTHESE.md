# SYNTHÈSE — Moteur léger et costaud (consultation famille 6/6 + codeur, 31/08)

**Sujet** : rendre Hulk (moteur paper MEXC) plus léger (moins d'appels réseau) et
plus costaud (robuste aux timeouts / rate-limit / corruption). Diagnostic de
Buffy soumis : ~200-270 appels/min vs limite ~200 MEXC, timeout 40s×4, monolithe.
Plan proposé : batch prix / timeout agressif / espacer les coûteux / cœur-satellites /
circuit-breaker 429.

**7/7 avis** (gemini, grok, nvidia, deepseek, juge, ultra + codeur).

---

## CONSENSUS (7/7)
| Élément | Verdict |
|---|---|
| Étape 1 — batch prix | **Indispensable, immédiat** (passer 21→1 appel) |
| Étape 4 — cœur/satellites | **La voie, structurelle** : le cœur = +lire état +décider +exécuter, ZÉRO appel d'analyse lourd ; les sondes = satellites qui écrivent des fichiers |
| Étape 5 — circuit-breaker 429 | **Critique** : backoff exponentiel + mode « safe », pas une pause naïve |

## CORRECTIONS IMPOSÉES PAR LA FAMILLE (je me suis trompé sur 2 points)
1. **Étape 2 (timeout 10s×2) contestée par 7/7** : sur un MacBook en Wi-Fi, 10s
   trop court = faux positifs d'erreurs réseau. → timeout raisonnable (~15s) +
   **1 seul retry immédiat** + backoff exponentiel UNIQUEMENT sur 429/5xx + en
   cas d'échec, **fallback sur le dernier prix validé avec warning** (pas de
   saut de paire).
2. **Le cache prix 15-20s est piégé** : la boucle tourne déjà toutes les 20s ;
   un cache de 15-20s peut servir deux fois la même photo ou un prix périmé de
   39s dans un cycle lent. → **1 seul appel batch au DÉBUT de chaque cycle, figé
   pour tout le tour de boucle** (pas de cache temporel aveugle).

## PRÉCAUTIONS D'IMPLÉMENTATION (unanimité)
- Parser le batch en dict `{symbol: price}` UNE fois par cycle.
- Paire absente du batch / delistée → **fallback ou ignorer, JAMAIS casser** (KeyError).
- Écriture **atomique** de tous les fichiers inter-process (fichier .tmp puis
  `os.replace()`).
- **Drift temporel** : ne pas faire `time.sleep(20)` mais dormir jusqu'au prochain
  tick absolu (`sleep = prochain_tick - now`), sinon la boucle dérive.

## AMÉLIORATIONS AJOUTÉES PAR LA FAMILLE (au-delà du plan)
| Amélioration | Proposée par |
|---|---|
| **Écriture atomique** des JSON (anti-corruption) | ~6/7 |
| **Staleness check** : vérifier l'âge des fichiers satellites lus → mode dégradé | deepseek |
| **WebSocket MEXC** pour les prix (zéro REST, la solution définitive) | nvidia |
| **Rate-limiter client** (token bucket ~3 req/s) lissé | deepseek |
| **RAM disk /tmp** pour l'inter-process (zéro usure SSD, zéro latence) | juge, ultra |
| **Purge mémoire** stricte (fenêtres glissantes) contre le memory leak | grok, nvidia |
| Backoff exponentiel intelligent | grok, codeur, deepseek |

---

## PLAN D'EXÉCUTION REVISÉ (Buffy, chef scientifique)

**PHASE 1 (aujourd'hui, risque faible, gain ~−95% d'appels)**
- Batch prix : 1 appel `/ticker/price` au début du cycle → dict {symbol: price},
  fallback paire absente, garde-fou anti-crash. Cache = durée du cycle uniquement.
- Timeout ajusté : ~15s × 1 retry, backoff sur 429/5xx, fallback dernier prix.
- Écriture atomique du contexte (croisement_contexte.jsonl) via .tmp + os.replace.
- Correction du drift temporel de la boucle.

**PHASE 2 (validation puis)**
- Espacer les coûteux : klines→5 min, carnet→rotation (paires proches d'une décision).
- Sortir les sondes (aspiration, carnet, GEX) du cœur → satellites avec leurs
  propres fréquences, écritures atomiques, staleness check.

**PHASE 3 (chantier séparé)**
- WebSocket prix (remplace le REST batch à terme) + stockage inter-process en RAM.

> Principe de validité dynamique (29/08) : chaque phase est validée par les
> chiffres avant de passer à la suivante. Rien n'est gravé dans le marbre.