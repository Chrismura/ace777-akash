# Suivi de l’info — comptes à écouter

**But :** pas tout Twitter. Une liste courte → Punk / **Cortana (voix)** digère → te dit si c’est **pertinent pour nos améliorations** (tableau vivant) ou bruit.

## Boucle voulue (Christophe)

```
Compte suivi → nouveau post
    → filtre (lien Index / sniper / harness / macro ?)
    → SI pertinent : résumé vocal (Cortana) + note À mon attention
    → SINON : ignorer (ou 1 ligne « skip »)
```

**Critère pertinent =** avance M1–M5, A/B/C, pistes Poly/sniper/judge — **pas** un if de trading ACE.

---

## Comptes retenus (session 2026-07-28)

| Compte | Pourquoi on suit | Pertinence type | Bruit / méfiance | Évals |
|--------|------------------|-----------------|------------------|--------|
| [@RaoulGMI](https://x.com/RaoulGMI) | Liquidité / marée macro | M1 | % marketing | #08 |
| [@macro_synergy](https://x.com/macro_synergy) | Multi-couches → 1 score | C16 | stack JPMaQS entier | #01 |
| [@RuujSs](https://x.com/RuujSs) | Régimes / HMM cadre | C17 | Sharpe tweet | #07 |
| [@undefinedKi](https://x.com/undefinedKi) | Judge / graphe / daemon | M3 S6 | récits $ Anthropic | #10 |
| [@0xSomni](https://x.com/0xSomni) | Agents = graphes | P-Graph | hype papers | #05 |
| [@slash1sol](https://x.com/slash1sol) | Prove me wrong / context | M4 | MiroFish affiliate | #06 |
| [@ridark_eth](https://x.com/ridark_eth) | Sniper calibration Beta | M2 P-Sniper | PnL $424k farm | #09 |
| [@Kropanchik](https://x.com/Kropanchik) | Poly BTC courts / panique | P-Poly | wallets miracles | #03 |
| [@RebellioMarket](https://x.com/RebellioMarket) | TA classique (tri D) | D | packaging 1% | #04 |
| [@MilkRoadAI](https://x.com/MilkRoadAI) | Capex AI / qui est payé | macro soft M1 | « Save this » usine | #11 |
| [@0x_Punisher](https://x.com/0x_Punisher) | Poly ops · ghost fills · courbe fees · anti-fraude | S1 S11 S12 P-Poly | PnL $ public / sweeper hype · **wallet = audit pas copie** | #14 |
| [@Av1dlive](https://x.com/Av1dlive) | Company OS / mémoire agents / Kimi harness | P-Graph M3 · phase équipe | Demo simu / install lourd Mac 8 Go | #16 |

**Wallet public (vérif seulement) :** [profil Poly](https://polymarket.com/@0x13f0bcec1e2e60ec9acc3bee4d2da2fe9694a50f-1774334442364) — 🔴 ne pas mirror ; 🟢 pour confronter le récit aux positions.

### Division du travail (articles longs / anglais)
- **Toi :** flair + lien (ou collage si tu peux). Pas besoin de tout comprendre.
- **IA (Punk/Cursor) :** `LU_PARTIEL`/`LU_COMPLET` → vulgarise en FR → **ce qui compte pour l’Index seulement** (3 puces + IDs S/M/P).
- **Toi :** GO garder / ignorer.  
Voir [[PROTOCOLE_LIENS]].

### Pas en suivi actif (pour l’instant)
- Wallets Poly nommés (Heisenbug, JnSt…) → **REFUS copie** ; idée sniper seule.
- Comptes pure hype sans cadre réutilisable.
- [underground-trading.io](https://underground-trading.io) → **REFUS** (Bitunix referral ; #12).
- [@lumendriada](https://x.com/lumendriada) / herdr → tooling multi-agents 🔵 WATCH ops (#13), pas trading.

---

## Prompt filtre (Punk / Cortana)

Quand un post arrive d’un compte ci-dessus :

1. **Verdict :** PERTINENT / SOFT / IGNORER  
2. **Lien Index :** quel ID ? (M1, C17, P-Sniper, S6b…) ou « aucun »  
3. **Résumé :** 2–3 phrases vulgarisées  
4. **Action :** noter `A_Mon_Attention/` · MAJ tableau · ignorer  
5. **Jamais :** « buy/sell ACE maintenant » sauf GO humain explicite  

---

## Fichiers

| Fichier | Rôle |
|---------|------|
| `COMPTES.md` | cette liste (ajouter / retirer ici) |
| `../01_TABLEAU_VIVANT.md` | améliorations = cible du filtre |
| `../A_Mon_Attention/` | file « à te proposer » |
| Cortana | résumé **vocal** si PERTINENT / SOFT |

## Ajouter un compte (automatisé si validé)

**Règle (2026-07-29) :** si cold-path **valide** un compte (éval + lien Index clair + pas packaging seul) → **dans la même session** :
1. 1 ligne tableau ci-dessus  
2. Map `COMPTE_LIENS` dans `veille-punk/suivi_check.py`  
3. Éval `#N` + note `A_Mon_Attention/` + ligne `MEMOIRE_COLLAB`  
4. OUTBOX prêt sync  

Pas besoin d’attendre un second GO « ajoute le compte » — le GO était la validation.  
Retirer = passer en « Pas en suivi » avec date.  
Détail : [[PREFS_STACK]].

