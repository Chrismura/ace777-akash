# SYNTHESE DES 5 DÉCOUVERTES — 22/08/2026

> Session : reprise après coupure + signets X · tout est tracé, rien n'est perdu.
> Règle : chaque découverte = verdict + action (FAIT / OBSERVER / À PILLER / HORS SUJET).

---

## 1. @rvaniaaaa — « The Second Brain Is Not a Storage System. It's a Compiler. » ✅ APPLIQUÉ

**Concept** : RAG re-dérive la connaissance à chaque requête ; un wiki compilé la dérive une fois et la maintient. 3 dossiers (raw/ wiki/ output/) + CLAUDE.md vivant + boucle quotidienne.

**Verdict** : 🔥 valide notre philosophie (MEMOIRE_COLLAB, OSSATURE = déjà 70% de ça).

**Action** :
- ✅ `SKILLS_TRADING.md` créé (les skills sont des fichiers compilés, pas des prompts dans le chat)
- ✅ `BASE_SYSTEM.md` créé (le « CLAUDE.md vivant » de la flottille)
- ⚠️ Avertissement retenu : « garbage in = garbage compiled » → le tri qualité passe AVANT l'ingestion.

---

## 2. @quantscience_ — Nautilus Trader 📌 OBSERVER

**Concept** : framework de trading algo Python+Rust open-source, backtest + live, gestion native des partial fills et des commissions.

**Verdict** : pertinent pour NOTRE angle mort (CSV vs Binance : +315 affiché vs −90.56 réel), mais migration trop lourde pour ACE (réécriture du moteur).

**Action** :
- 📌 **OBSERVER** (comme CPFP/ADA, date butoir à fixer)
- Usage possible : référentiel de vérité pour la compta des fills, backtest propre, socle si changement d'exchange.

---

## 3. @quantscience_ — 67 Claude trading skills (repo agiprolabs/claude-trading-skills) ✅ APPLIQUÉ

**Concept** : 67 skills (format SKILL.md standard, 30+ outils compatibles, pas que Claude). MIT, gratuit.

**Verdict** : 🔥 les prompts sont transposables à notre hub gratuit (Gemini/Groq/Nara/Mistral).

**Action** :
- ✅ 5 skills adaptés dans `SKILLS_TRADING.md` : slippage / exit / kelly / walkforward / risk
- ✅ Tâche `trading.skills` ajoutée à `routing.json` (gemini→groq→nara, quota 10/j)
- ✅ Script `prise-ia/scripts/skill_trading.py` + mémoire auto-écrite dans MEMOIRE_COLLAB
- ✅ 5 skills exécutés et réponclus via le hub

**Résultats clés des skills** :
- **Kelly** : ACE 2.75%/trade (0.5× Kelly) vs disjoncteur 10% actuel → le disjoncteur est 3.6× trop large · HULK edge < 2% → ne devrait pas trader
- **Slippage** : seuil de rentabilité Binance = 160 bps · MEXC 100 bps · Hyperliquid 50 bps → argument exchange
- **Exit** : hiérarchie Hard stop > trailing ATR > TP > time stop · ATR(14)×2 stop / ×2.5 trailing
- **Risk** : trous = pas de limite journalière codée, drawdown non limité, pas de circuit breaker auto · 3 améliorations priorisées
- **Walkforward** : 40 runs insuffisants (il en faut 100+) · protocole CSV+Ruby léger à mettre en place

---

## 4. @quantscience_ / QuantMuse (0xemmkty/QuantMuse) 🔨 À PILLER

**Concept** : système quant complet Python+C++ (factor analysis, backtest, VaR/CVaR, dashboard Streamlit).

**Verdict** : 🟡 trop lourd à installer (80 Mo deps, C++/CMake, OpenAI payant) mais de bonnes idées.

**Action** :
- 🔨 **À PILLER** : le factor analysis (momentum/value/volatility) et les métriques backtest (Sharpe, drawdown, win rate) — rien d'équivalent chez nous
- ❌ PAS à installer. On prend les concepts, on les adapte en scripts légers.

---

## 5. @rohit4verse — « Move semantic state, never KV state » + les 7 couches 🔧 AMÉLIORATIONS APPLIQUÉES

**Concept** : quand tu changes d'agent, tu perds tout si l'état vit dans le cache KV du modèle. Solution : l'état sémantique dans des fichiers (décisions, specs, mémoire). 7 couches : 1 kernel persistant, skills importés comme modules, harness = variable, tout écrit sur disque, sub-agents = appels de fonction, boucle d'auto-amélioration, **system prompt de base qui ne bouge jamais**.

**Verdict** : 🔥 confirme le compiler-vs-storage, et donne 3 améliorations concrètes.

**Action** :
- ✅ **BASE_SYSTEM.md** créé (P0 — le system prompt figé, toute l'histoire de la sécurité)
- ✅ **Mémoire auto-écrite** dans skill_trading.py (P1 — chaque skill appelé → 1 ligne MEMOIRE_COLLAB)
- ✅ **Skills rechargeables** (P2 — déjà le cas : le script relit SKILLS_TRADING.md à chaque appel)
- 🔵 P3 (plus tard) : sub-agents asynchrones — lourd pour 8 Go, à ne pas faire maintenant

---

## Tableau récapitulatif

| # | Découverte | Verdict | Action |
|---|---|---|---|
| 1 | Second Brain = Compiler (rvaniaaaa) | ✅ | SKILLS_TRADING.md + BASE_SYSTEM.md |
| 2 | Nautilus Trader (quantscience_) | 📌 OBSERVER | référentiel fills / socle exchange |
| 3 | 67 skills trading (agiprolabs) | ✅ | 5 skills → hub gratuit |
| 4 | QuantMuse | 🔨 À PILLER | factor analysis + métriques backtest |
| 5 | Rohit semantic state / 7 couches | ✅ | BASE_SYSTEM + mémoire auto |

---

## Prochaines étapes proposées

1. **Décision exchange** avec les chiffres slippage (160 vs 100 vs 50 bps) — le skill 3 alimente la SPEC_CONSULTATION_EXCHANGE
2. **Implémenter le circuit breaker auto** (skill risk, trou n°1)
3. **Protocole walkforward** (skill 4) : CSV des runs + script Ruby léger
4. **Factor analysis** léger (QuantMuse) si on veut enrichir ACE