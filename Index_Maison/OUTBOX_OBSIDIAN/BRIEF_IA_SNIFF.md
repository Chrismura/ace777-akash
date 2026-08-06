# Brief IA — sujets à sniffer (intérêts Christophe)

**Statut :** document **vivant** — évolue avec tes intérêts (MAJ manuelle + ligne mémoire).  
**Pour :** Punk · Cursor · Gemini · Kimi · Cortana · toute IA qui fait de la veille / recherche.  
**Pas pour :** lancer un trade, modifier le champion, coller un bot Discord/TV.  
**Source canon :** `Evaluations/12_audit_survie_frais_underground.md` (+ texte audit 28 juil. 2026).

Quand tu lis un post, un repo, un site « bot miracle », un indicateur payant, **sniffe d’abord** ces axes. Si ça n’en touche aucun → probablement bruit.

### Journal d’évolution (append)
| Date | Changement |
|------|------------|
| 2026-07-29 | Création (audit #12 + sniff) |
| 2026-07-29 | Note : tooling multi-agents (ex. herdr / @lumendriada) = **ops swarm**, pas alpha trading — voir #13 |
| 2026-07-29 | Chemin phase équipe : [[PHASE_EQUIPE_AGENTS]] (marches 0→4) |
| 2026-07-29 | [[PROTOCOLE_LIENS]] — anti-faux « j’ai tout lu » sur X/paywall |
| 2026-07-29 | [[PROTOCOLE_CONTRA_SOFT]] + #15 N01ennn — CONTRA manuel (pas cron LLM) |
| 2026-07-29 | #16 @Av1dlive Meridian · pref Kimi API · auto-add comptes validés ([[PREFS_STACK]]) |
| 2026-07-29 | [[PROTOCOLE_SESSION_RECHERCHE]] — agent ACTIF écrit Index à chaque validation ; PASSIF = ops |
| 2026-07-29 | [[ARCHITECTURE_AGORA]] — schéma 3 plans · Ollama Launch×9 = WATCH cold (S15) |
| 2026-07-29 | [[ACE_DIAMANT_ARCHIVE]] — R&D fév. Pattern Diamant clarifié (#18 / S16) |
| 2026-07-29 | [[VALEUR_INFORMATION]] S14 — scorer A (économie) + B ($) avant d’investir temps |

---

## 1 — Cartographie (qui paie le +1 $ ?)
- Alpha retail vs pros (latence, colocation, flux).  
- Hype « c’est juste du code » = **faux** → info + vitesse + liquidité.  
- Masse même bot/indicateur → chasse aux stops.  
→ Lien **M1**. Méfiance packaging Discord/Telegram/TV.

## 2 — Validation scientifique (anti-overfit)
- **Walk-Forward / Out-of-Sample** (pas un seul backtest sur tout l’histo).  
- **Monte Carlo** sur l’ordre des trades → Max DD / ruine.  
- **Profit Factor** réaliste ~**1.2–1.7** ; PF très haut sur long BT → soupçon mensonge/overfit.  
→ Lien **M5** · process **S9**.

## 3 — Disjoncteurs / survie
- Hard stop % jour, rate-limit ordres, heartbeat flux.  
- Boucle API / bug = risque #1 bot maison.  
→ Lien **S2** · ce qu’ACE a déjà (STOP, watchdog) vs ce qui manque encore.

## 4 — Frais & exécution réelle
- **Binance** : funding + VIP / taker (ACE).  
- **MEXC** : « 0 fees » mais **spread / slippage** (Hulk).  
- Slippage + commissions qui mangent &gt;30 % du PnL théorique → stratégie morte.  
→ **S10** · toujours comparer récit vs **fills CSV (S1)**.

## 5 — Niches lentes (culture, pas coller sur ACE)
- Paires / cointégration, momentum extrême à petite size.  
→ 🔵 WATCH hors champion. **REFUS** one-click vers live ACE.

## 6 — Boutiques « gratuites »
- Ex. underground-trading.io = outils derrière referral exchange.  
→ **REFUS abo** ; sniffer seulement l’*idée* (OI déjà C13), jamais leur stack.

---

## Verdicts types (à coller mentalement)

| Tu vois… | Tu dis… |
|----------|---------|
| « matched » API sans fill/chain | ghost fill — S11 reconcile |
| Fee plate alors que courbe / micro-edge | S12 — math fee+gas **avant** le bid |
| PnL / PF miracle sans OOS ni fills | BULLSHIT / IGNORER |
| Indicateur vendu à 50k traders | chasse liquidité — SOFT au mieux |
| Walk-forward, Brier, calibration, judge | PERTINENT → Index |
| « 0 fees » MEXC / free bot VPS | regarder slippage + S10 |
| Funding / OI / latence / kill-switch | PERTINENT process |

## Règle d’or sniff
**Cherche la preuve falsifiable** (fills, OOS, MC, frais) — pas le storytelling.  
Intérêt Christophe = **améliorer l’Index / gates / hygiène**, pas « trouver le bot qui print ».  
Avant de garder : scorer [[VALEUR_INFORMATION]] — **A** (économie) + **B** ($).
