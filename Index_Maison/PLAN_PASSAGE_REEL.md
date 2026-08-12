# PLAN DE PASSAGE AU RÉEL — ACE777

> Document vivant — 2026-08-12. Objectif : savoir EXACTEMENT ce qu'il faut
> pour passer de la simulation au trading réel, sans brûler d'argent.

---

## 1. Où on en est (le constat factuel, vérifié le 12/08)

| Composant | État |
|---|---|
| Radar (BTC/ETH) | ✅ en marche (calme, declenche=non) |
| Hub + providers + famille | ✅ en marche |
| Cockpit (BOARD, THERMO, STRATÉGIE) | ✅ en marche |
| Boucle alerte → analyste → avis ÉCRIT | ✅ en marche (alarme.json frais, log cadence 08:30/20:30) |
| Boucle alerte → avis VOCAL | ⛔ **maillon manquant** : vigie lance analyste sans `--speak` |
| Bots Alpha / Beta | 🛑 à l'arrêt (flags STOP_ALPHA, STOP_BETA) |
| Hulk (MEXC) | 🗄️ archivé (_ARCHIVE_20260807) |
| Journal d'intention des bots | 🔇 muet depuis le 2 août |
| PnL affiché au cockpit | 🧪 run simulé (NUAGE_TEST_8H_CMP3) |
| Ordres réels | ❌ **aucun ordre réel ne passe aujourd'hui** |

**En clair** : la maison (surveillance + IA + cockpit) est solide. La partie
« gagner de l'argent » est en veille complète.

---

## 2. Ce qu'on sait déjà — la preuve papier (rapport_perf_bots.py)

Classement des runs (PAPER, prix simulés) :

| Bot | Trades | Win rate | PnL total | Expectancy/trade | Verdict |
|---|---:|---:|---:|---:|---|
| ACE777 ESCALIER 4H | 113 | 56% | **+10,52 $** | +0,09 $ | Bénéficiaire, le meilleur profil |
| TEST DUO ALPHA HUNTER X7 | 11 | 82% | +6,90 $ | +0,63 $ | Bénéficiaire (petit échantillon) |
| TEST DUO BETA SCOUT X7 | 49 | 55% | +3,80 $ | +0,08 $ | Bénéficiaire |
| ALPHA SNIPER 9H | 142 | 49% | +3,16 $ | +0,02 $ | Sniper : ~1 trade sur 2 gagnant (+41 positions ouvertes non comptées) |
| BETA LOURD RAPIDE 9H | 127 | 49% | +2,02 $ | +0,02 $ | Éclaireur : mêmes traits qu'Alpha |

⚠️ **Lecture honnête** : ces chiffres prouvent la LOGIQUE des stratégies, pas
l'exécution réelle (latence, slippage, frais, limites API). C'est le minimum
requis avant le réel — pas une garantie.

---

## 3. Les 4 phases

### Phase 0 — Sécuriser (le 12/08)
- [x] Rapport de perf en routine (rapport_perf_bots.py, à rejouer après chaque run)
- [x] **Journal d'intention relancé** : plist `com.ace777.journal-intention` (scan toutes les 5 min)
- [x] **Avis vocal activé** : `--speak` dans vigie_live (prix + news) → edge_tts testé OK
- [x] **PANIC CORRIGÉ + RE-TESTÉ (12:35)** : 3 bugs trouvés et corrigés dans stop_ace777.sh —
    (1) il se tuait lui-même via son pkill (exclusion de $$ + scripts d'arrêt),
    (2) superviseur relançait les process pendant le stop (bootout ajouté),
    (3) vigie-live KeepAlive relançait le radar (bootout ajouté).
    Re-test : TOUT coupé ✓ (radar, pont, serveur, app, superviseur) — seul le hub survit (voulu).
- [x] **Run de test usine relancé (14:01, propre)** : BETA_X5 (levier 5) + ALPHA_X13 (levier 13),
    **TESTNET Binance confirmé** (clés ~/.binance_testnet.env, fail-closed vérifié),
    durée 4 h (fin prévue ~18:00) → nouveaux CSV runs/NUAGE_PROD_4H_*.csv → re-mesurer la preuve papier ensuite.
    NOTE : le 1er lancement (12:36) est mort avec la session de l'agent — relancé en
    `start_new_session` (méthode Hulk) → survit. Heartbeat frais vérifié.
    NOTE : Ollama relancé UNIQUEMENT comme garde-fou fail-closed du vieux moteur
    (directive « zéro IA locale » respectée côté maison ; à remplacer par le hub avant le réel).
- [x] **Hulk relancé (13:00, automatique)** : dossier hulk-mexc restauré depuis l'archive,
    PAPER (paper_diprip, zéro clé requise) + VEILLE MEXC (digest_watch, 15 paires) vivants,
    watchdog launchd `com.ace777.hulk-watchdog` relance tout seul toutes les 2 min.
- [x] **CHANTIER HUB — pont LLM gate (14:40-14:50)** : `llm_gate_hub_bridge.py` (codeur hub)
    émule l'API Ollama (/api/tags + /api/generate) mais appelle le hub derrière
    (task supervise.decision, grok→gemini). Moteur champion NON modifié (Voie A validée).
    - Test décisif : vortex réel → pont → hub = `swarm_cohesion 0.65, justification llm_wind,`
      `emergency_override FALSE` → le juge hub est écouté ✓
    - Patch ADDITIF vortex (2 lignes) : timeouts configurables par ENV (défauts inchangés)
    - Service launchd `com.ace777.llm-gate-hub` (KeepAlive) : relance auto testée ✓
      (fix allow_reuse_address pour le rebind après kill)
    - Bascule config_active.env : LLM_OLLAMA_URL→11439 + VORTEX_LLM_READ_TIMEOUT=45
      + VORTEX_LLM_BUDGET_SEC=20 (backup .bak-20260812-pont) — effet au PROCHAIN run
      (celui en cours est figé sur Ollama)
    - REVUE (14:50) : fail-closed preflight renforcé (pont vérifie la santé du hub
      → 503 si hub mort → pas de run sans juge), bind 127.0.0.1, extraction JSON
      robuste (fences markdown), budget 20 s posé. Tous corrigés + retestés ✓
    - NOTE : Ollama restera allumé JUSQU'À la fin du run en cours (~18h), puis sera
      arrêté définitivement (zéro IA locale atteint au prochain run).
    - ✅ CACHE DU JUGE (validé Christophe, réglable) : `LLM_GATE_PONT_CACHE_SEC=90`
      (défaut 90 s, variable d'env). Le pont ne consulte le hub qu'1×/90 s → ~160
      appels/run 4h au lieu de ~1000 (budget cloud 480/j tenu). Clé = hash du
      prompt (cohesion vs radar séparés). Preuve : 1er appel 9,9 s (hub) → appel
      suivant 0,016 s (cache) → prompt différent re-consulte (10,3 s) ✓
    - ⚠️ VÉRIFIÉ : tous les providers gratuits (openrouter-free, puter-grok…) sont
      kind=cloud → comptés dans les 480 (budget d'APPELS, pas d'€). Seul qwen-local
      est hors budget (mais banni par directive). → le cache 90 s EST la solution.
- [ ] Clés MEXC réelles + CoinMarketCap : **dépriorisé par Christophe (12/08)** — CoinGecko
    gratuit testé en repli pour les indices (BTC 64 099 $, ETH 1 910 $, SOL 76,72 $, BNB 613 $, XRP 1,02 $).

### Phase 1 — Petit réel : validation mécanique (1-2 % du capital)
**Objectif** : prouver que la mécanique tient en conditions réelles.
- [ ] Clés API Binance (Alpha/Beta) + MEXC (Hulk) — **lecture seule d'abord**
- [ ] Ordres minimaux (ex. 5-20 $/trade), une paire (BTCUSDT)
- [ ] Mesurer : latence réelle vs 0,0064 s théorique, slippage, frais réels
- [ ] **Critère de sortie** : 5 jours sans bug de mécanique + frais conformes → passer Phase 2

### Phase 2 — Réel progressif : validation économique
- [ ] Taille de position liée au capital (ex. 0,5-1 %/trade, jamais de taille fixe)
- [ ] Réactiver Hulk : bag / escalier / courreur sur son univers 15 cryptos
- [ ] **Critère de sortie** : win rate et expectancy réels ≈ papier (écart < 20 %)

### Phase 3 — Plein régime + extensions
- [ ] Élargir le radar (autres instruments que BTC/ETH)
- [ ] Stratégie indices énergétiques
- [ ] **Hard wallet ACE777** : rapatrier/redéployer les gains à la seconde

---

## 4. Les filets de sécurité (non négociables)

1. **Kill-switch global** : STOP + bouton PANIC cockpit → à tester pour de vrai
2. **Alerte vocale** sur événement majeur (radar → analyste → voix) → maillon à activer
3. **Journal des décisions** relancé (traçabilité = la base de l'apprentissage)
4. **Budget journalier** d'appels IA (déjà en place, à surveiller)
5. **Reprise après redémarrage** : si le Mac reboote en pleine position ouverte,
   le boot du matin doit vérifier les positions (à construire)

---

## 5. Prêt vs à construire

**Déjà prêt** : radar, hub+famille, cockpit, boucle analyse écrite, rapport de
perf, kill-switch basique, budget IA.

**À construire (par ordre)** :
1. Avis vocal des alertes (petit : `--speak` dans vigie)
2. Reprise après redémarrage (boot → vérif positions)
3. Mode petit réel (clés API + montants minimaux)
4. Taille de position liée au capital
5. Hard wallet

---

*Généré avec les faits vérifiés du 12/08 — à mettre à jour à chaque phase.*
