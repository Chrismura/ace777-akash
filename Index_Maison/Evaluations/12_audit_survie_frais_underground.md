# Éval #12 — Audit survie bots + frais réels (texte Christophe) & Underground Trading

**Date :** 2026-07-29  
**Sources :**
1. Texte collé (mail / note Christophe, 28 juil. 2026) — cartographie marché, latence, Walk-Forward, Monte Carlo, disjoncteurs, audit PF, frais Binance / Hyperliquid / MEXC  
2. Site [underground-trading.io](https://underground-trading.io) — outils TV / bot ML / dashboard (paywall soft = Bitunix)

**Verdict global texte :** **PERTINENT** — doctrine froide, aligne Index (S1/S2, M1, M5, ACE/Hulk).  
**Verdict site Underground :** **REFUS abo / referral** — rien d’utile *gratuit sans Bitunix* ; chiffres marketing (PF 2.35) **contredisent** ton propre audit.

---

## A — Ton texte : ce qu’on garde

### Cartographie (pros vs mainstream)
- Alpha = jeu à somme nulle locale : pour +1 $ retail, quelqu’un paie.  
- Hype = « problème de code » → faux ; c’est **accès info + vitesse + liquidité**.  
→ Lien **M1** (marée / qui est de l’autre côté) + scepticisme packaging (#04, #09).

### Latence / hype bots Discord
- Colocation vs WiFi alpage : on **ne joue pas** la guerre ns. ACE = testnet + gates, pas HFT.  
- Masse même indicateur → chasse liquidité : argument **anti-copie** de setups TV/Discord.  
→ **REFUS** bots clés en main / mêmes scripts que la foule.

### Walk-Forward + Monte Carlo
- OOS / blocs glissants = anti-overfit → **M5** (pas de si figés sur tout l’historique).  
- Monte Carlo sur **ordre des trades** → Max DD théorique / ruine.  
→ Nouvelle piste process **S9** (protocole d’audit).

### Niches « miettes » (paires, momentum extrême)
- Utile comme **culture** ; **pas** à coller sur le champion ACE.  
→ 🔵 WATCH seulement (hors genesis).

### Disjoncteurs
| Idée texte | Déjà chez nous ? |
|------------|------------------|
| Hard stop quotidien | partiel (STOP / hygiene) — à formaliser % jour |
| Rate limiter ordres | à surveiller (E-spread / API) |
| Heartbeat flux | **oui** (watchdog / heartbeat ACE) |

→ Renforce **S2** gates + kill switches = 🟢 GARDÉ doctrine.

### Audit score (PF / MC / OOS / frais)
| Critère | Seuil texte | Action Index |
|---------|-------------|--------------|
| Profit Factor | 1.2–1.7 OK ; &lt;1.2 bombe ; &gt;2.5 long BT → soupçon overfit | Coller sur fills ACE/Hulk (S1) |
| Monte Carlo DD | si &lt; −25 % trop risqué | S9 |
| Out-of-Sample | courbe plate/↓ = poubelle | S9 + M5 |
| Slippage+fees | si −30 % du PnL théorique → trop de trades | **frais ACE Binance + Hulk MEXC** |

### Frais plateformes (très utile pour nous)
| Exchange | Piège | Lien swarm |
|----------|-------|------------|
| **Binance** (ACE) | funding + paliers VIP / taker | Mesurer funding + slippage dans rapports ; Post-Only = piste soft |
| **MEXC** (Hulk) | « 0 fees » mais **spread / slippage** + rate limit | Paper déjà : ne pas croire 0 % ; tracker prix demandé vs fill |
| **Hyperliquid** | RPC / impact | Hors scope actuel — WATCH |

**Opinion :** excellent texte « anti-hype » — à garder comme **rulebook froid**, pas comme signal d’entrée. Il valide pourquoi on refuse Ridark PnL / bots Discord et pourquoi CSV fills &gt; récit.

---

## B — underground-trading.io (sans abo)

### Ce que c’est
- Landing : indicateurs TradingView, Flux OI, Quantum AI bot, dashboard options.  
- « Gratuit » **si** compte **Bitunix** via referral + **≥ 500 $** volume / 30 j.  
- Sinon : paywall soft (pas de vrai outil exploitable depuis la page publique).

### Utile sans abo ?
| Élément site | Sans Bitunix | Pour ACE/Hulk |
|--------------|--------------|---------------|
| Discours order flow / OI | concepts connus | on a déjà **C13 OI** en GARDÉ — pas besoin de leur stack |
| Quantum AI +125 % / PF **2.356** | hype | ton audit dit PF &gt; 2.5 long = **alerte mensonge** → ironie totale |
| VPS bot Docker | derrière referral | **REFUS** brancher sur champion |
| Discord / YouTube | bruit | pas en Suivi_Info actif |

**Décision :**
- Site → **REFUS** abonnement / referral Bitunix / « unlock premium ».  
- Pas de ligne COMPTES pour Underground (influenceur tooling + affiliate exchange).  
- Idée OI footprint « trapped » → déjà couverte par **C13** (data lecture seule un jour), pas leur produit.

---

## C — Actions Index

| ID | Item | Statut |
|----|------|--------|
| S9 | Protocole audit survie : PF · Monte Carlo · OOS · frais/slippage | 🟢 GARDÉ (doctrine) |
| S10 | Conscience frais réels Binance funding + MEXC spread | 🟢 GARDÉ |
| — | Underground Trading tools / Bitunix deal | 🔴 REFUS |
| — | Pair trading / momentum niche retail | 🔵 WATCH |

Checklist preuves :
- [ ] Sur un run ACE : PF fills + note funding si positions longues
- [ ] Sur Hulk paper : écart prix signal vs fill (proxy slippage)
- [ ] Documenter hard-stop % jour si on le code un jour (hors champion sans GO)

---

## Résumé une phrase
Ton texte = **garde-fou scientifique** ; le site = **boutique déguisée en gratuit** — on prend l’esprit du texte, on laisse le magasin.
