# Éval #14 — @0x_Punisher · ghost fills (off-chain vs on-chain)

**Date :** 2026-07-29  
**Post :** https://x.com/0x_Punisher/status/2081362888397070432  
**Titre affiché :** « Sweeper bot V2: Everything i got wrong… + $32k public PnL »  
**Qui :** trader Polymarket / investigation fraudes (bio)

## Verdict
**PERTINENT (pattern)** · **SOFT/IGNORER (PnL $32k / sweeper copy)**  

Le code que tu as collé est la partie utile. Le packaging « $32k public » = sniff BRIEF → pas une preuve pour nous.

---

## Pattern à garder (doctrine fills)

### 1) `confirm_fill` — deux vérités
```text
API dit "matched"  = claim off-chain (peut mentir / être en avance)
tx settled on-chain = vérité
timeout → traiter comme NON fill
```
→ Exactement notre **S1** poussé d’un cran : **récit API ≠ fill réel**.

### 2) `reconcile` — chasse aux fantômes
```text
position ouverte en mémoire
mais pas settled on-chain
→ mark_phantom / tear down
→ log "ghost fill removed"
```
→ Même famille que nos **PID fantômes** / state mensonger (checkup garage, `nuit_ghost_loop.pid`).  
Pour Poly / tout CLOB : **state local peut inventer une position**.

## Lien Index
| ID | Lien |
|----|------|
| **S1** | fills = juge — ici : on-chain (ou CSV exchange) > status API |
| **S11** (nouveau) | Reconcile / ghost fill : timeout + tear-down si pas de vérité |
| **P-Poly** | Contexte Polymarket sweeper — piste, pas copie bot |
| **M3** | Judge PASS/FAIL machine avant de croire le worker |
| **BRIEF sniff** | PnL public sans notre OOS/fills → méfiance |

## Ce qu’on ne fait pas
- Copier le sweeper / chasser le $32k.  
- Brancher ça sur le champion ACE.  
- Croire `state == matched` Binance/MEXC sans croiser fill CSV / position exchange.

## Traduction ACE / Hulk (froid)
| Maison | Équivalent Punisher |
|--------|---------------------|
| CSV fills ACE | `settled_on_chain` |
| `get_order` / WS « filled » | claim off-chain |
| state Hulk 7 pos gelées | risque « phantom » si mal réconcilié |
| checkup fantômes PID | même esprit, couche process |

**Action un jour (hors GO trading) :** une passe `reconcile` lecture seule — positions state vs fills CSV / API positions — loguer les fantômes, ne pas auto-trader.

## Compte & wallet public
[@0x_Punisher](https://x.com/0x_Punisher) → **suivi actif** (COMPTES).  
Wallet Poly (transparence / audit claims) :  
`https://polymarket.com/@0x13f0bcec1e2e60ec9acc3bee4d2da2fe9694a50f-1774334442364`  
*(param `via=punisher` = tracking referral — ignorer pour copie)*

| Usage | Statut |
|-------|--------|
| **Vérifier** ses claims (fills vs récit, M4 / S1) | 🟢 OK |
| **Copier** le wallet / mirror trades | 🔴 REFUS (comme autres wallets Poly) |
| Money math (fees+gas vs cent) | 🟢 déjà S12 |

Snapshot lecture `LU_PARTIEL` (2026-07-29) : Positions Value ≈ **$5 295** · ~**13 098** predictions · P/L 1D affiché ≈ **+$467** · positions actives listées vides sur le scrape.  
→ Chiffres UI ≠ preuve sweeper $32k ; servir à **contrôler**, pas à idolâtrer.

---

## Résumé une phrase
**« matched » sans settlement = fantôme ; reconcile ou tu trades un rêve.**

---

## Suite — courbe de frais + zone sweeper (extrait V2)

**Verdict :** **PERTINENT** (structure) · **REFUS copie** (drift 0.95 / chase ms)

### Ce n’est pas du « goût »
La fee Poly **n’est pas plate** : courbe — **minimale aux extrêmes** (≈0.01 / ≈0.99), **maximale vers 0.50**.  
Sweeper à **≥0.99** = zone où la taxe plateforme **presque disparaît**, alors que le gross edge n’est qu’~**1 cent** par share (payer 0.99 → recevoir 1.00).

Une fee « erreur d’arrondi » sur un bet directionnel à 50c **mange tout** ce cent.

### Deux conséquences (doctrine)
1. **Ne pas descendre le book** (0.95 / 0.90) en croyant « même trade » : gross edge ↑ mais fee ↑ + vrai risque d’outcome.  
2. **Taille mini = fees + gas**, pas la confiance. Si fee+gas > cent capturé → fill = **donation**. Math **avant** le bid.

### Latence (20 ms wall)
V1 a **oversell** les microsecondes. Le mur utile ≈ **dizaines de ms**, pas la guerre ns colocation.  
→ Aligne alpage/WiFi : on ne joue pas HFT ; on joue **structure + gates**.

### Lien Index
| ID | Lien |
|----|------|
| **S10** | frais ≠ flat — toujours modéliser la *forme* des fees |
| **S12** | Edge net = gross − fees − gas ; zone de prix = edge structurel |
| **S9** | « râpe à fromage » — micro-edge tué par frais |
| **P-Poly / M2** | sniper rare + width ; pas chasser le book |
| **BRIEF** | PnL sweeper = bruit ; courbe fees + math taille = signal |

### Traduction ACE/Hulk (sans copier le sweeper)
- Scalp / micro-edge **sans** mesurer taker+funding+slippage = donation (S10/S12).  
- Ne pas « améliorer » un trade en élargissant le prix d’entrée sans refaire le compte fee.  
- Latence : soigner stale NUAGE / heartbeat, **pas** fantasmer µs.
