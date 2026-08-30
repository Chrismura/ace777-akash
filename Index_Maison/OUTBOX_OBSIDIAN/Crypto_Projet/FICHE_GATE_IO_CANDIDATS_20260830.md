# 🚪 FICHE CANDIDATS GATE.IO — MIS DE CÔTÉ (30/08/2026)

> Christophe envisage d'ouvrir une ligne sur **Gate.io** pour 4 tokens **absents de MEXC**.
> Décision 30/08 : **mis de côté pour l'instant** — cette fiche garde tout le contexte
> pour quand on décidera d'y aller. Aucun ordre, aucune config activée.

---

## 📋 LES 4 CANDIDATS (vérifiés sur Gate.io le 30/08 via API publique)

| # | Token | Ticker | Paire Gate.io | Prix (30/08) | Vol 24h Gate | Sur MEXC ? | Note |
|---|---|---|---|---|---|---|---|
| 1 | **Quant** | QNT | `QNT_USDT` | $61.41 | 34,383 USDT | ❌ (mais déjà en watch MEXC) | Overledger — interopérabilité blockchain, gros projet ($907M mcap) |
| 2 | **Xend Finance** | RWA | `RWA_USDT` | $0.001225 | 13,569 USDT | ❌ | DeFi coopératives — **≠ notre RWAUSDT (Allo), ≠ RWAINC** (voir avertissement ci-dessous) |
| 3 | **Root Network** | ROOT | `ROOT_USDT` | $0.0001604 | 10,720 USDT | ❌ | Couche 1 pour applications Web3 (Futureverse) |
| 4 | **Lagrange** | LA | `LA_USDT` | $0.05682 | 3,031 USDT | ❌ | Zero-knowledge / data availability |

**→ Les 4 sont ABSENTS de MEXC, PRÉSENTS sur Gate.io. Aucun n'est dans la rotation Hulk.**

---

## 🎯 POURQUOI GATE.IO (et pas MEXC)
- MEXC ne liste pas ces 4 tokens → impossible de les trader chez nous actuellement.
- Gate.io les liste tous → une seule plateforme couvre les 4 (économie d'effort).

## ⚠️ CE QU'IL FAUDRA VÉRIFIER AVANT D'OUVRIR LA LIGNE
1. **Volumes faibles** : LA = 3k$/24h, ROOT = 10.7k$ — quasi illiquides (même profil que
   les micro-caps qui se font delister). QNT est le seul avec un vrai marché ($34k + mcap $907M).
2. **⚠️ ATTENTION — TROIS TOKENS « RWA » DIFFÉRENTS (vérifié 30/08 CoinGecko + MEXC) :**
   - **RWAINC = RWA Inc.** (rwa.inc) → dans NOTRE portefeuille Hulk (contrat 0xe2b1dc2d…)
   - **RWA = Xend Finance** (xend.finance) → le candidat Gate.io (contrats 0x3096e7bf…/0x45635542…)
   - **RWAUSDT sur MEXC = Allo** (allo.xyz, fullName « Allo ») → c'est NOTRE watch RWAUSDT actuel !
   → La ligne Gate.io sur « RWA » = Xend Finance, qui est un token que nous ne suivons
     encore NULLE PART. Ne pas croire qu'on le capture déjà.
3. **API Gate.io** : pas de clé configurée — il faudra des clés API Gate si on veut que
   Hulk/une sonde lise les prix en continu.
4. **Décision d'investissement** : c'est du réel → attendre la validation complète du
   contexte (deepdive par token) avant tout ordre, comme pour les autres.

## 📌 CE QU'ON A FAIT (30/08)
- **MNSRY (Mansory)** : vérifié — **il EST sur MEXC** (0.007441, vol 34.5k$/24h) →
  ajouté à `PAPER_WATCH_PAIRS` (observation active). Contrairement au souvenir de
  Christophe, pas besoin de Gate.io pour lui.
- **QNT, RWA, ROOT, LA** : mis de côté (aucune config) — cette fiche est leur mémoire.

## 🔗 LIENS
- API Gate.io tickers : `https://api.gateio.ws/api/v4/spot/tickers` (gratuit, sans clé)
- Quant : quant.network · Xend Finance : xend.finance · Root Network : therootnetwork.com
