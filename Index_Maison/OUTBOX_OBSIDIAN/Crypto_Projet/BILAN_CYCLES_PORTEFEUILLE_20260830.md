# 📊 BILAN CYCLES JOUR/NUIT — PORTEFEUILLE COMPLET (30/08/2026)

> Suite au delisting QAIT (29/08), on vérifie si la signature « nuit > jour »
> (pic 23h-1h UTC, creux 10h-13h UTC) existe ailleurs dans le portefeuille.
> Données : `hulk-mexc/runs/croisement_contexte.jsonl` (~2000 points/paire,
> 27-30/08). Signature QAIT exacte : pic (23h,0h,1h) vs creux (10h,11h,12h,13h).

---

## 🏆 CLASSEMENT COMPLET (spread pic/creux, signature QAIT)

| Paire | pts | spread pic/creux | max (h) | min (h) | Lecture |
|---|---|---|---|---|---|
| **QAIT** | 1436 | **+7.16%** | 00h | 19h | ⭐ le pattern original (delisted 29/08) |
| **EDEL** | 1997 | **+3.88%** | 00h | 11h | 🟢 **LE COUSIN — même signature** |
| **BIO** | 1997 | +2.35% | 01h | 18h | 🟡 |
| **PYTH** | 1997 | +2.31% | 00h | 11h | 🟡 même creux 11h que EDEL |
| **W** | 1997 | +1.76% | 01h | 22h | 🟡 |
| **HBAR** | 1997 | +1.62% | 01h | 16h | 🟡 |
| **TEL** | 1997 | +1.32% | 01h | 22h | 🟡 |
| **CC** | 1997 | +1.24% | 20h | 09h | 🟡 max décalé (20h) |
| **KITE** | 1997 | +1.18% | 15h | 09h | 🟡 max décalé (15h) |
| **XRP** | 1999 | +1.15% | 01h | 18h | 🟡 |
| **BTC** | 1998 | +1.02% | 01h | 21h | 🟡 bruit de fond |
| **RIZE** | 1997 | +0.79% | 07h | 03h | neutre |
| **ETH** | 1998 | +0.77% | 01h | 21h | neutre |
| **RWAINC** | 1997 | +0.61% | 01h | 08h | neutre |
| **ZBCN** | 1997 | +0.39% | 14h | 22h | neutre |
| **RED** | 1997 | -0.34% | 11h | 16h | neutre |
| **CHIP** | 1997 | **-3.29%** | 14h | 03h | 🔻 **INVERSE (jour > nuit)** |

---

## 🎯 LES 3 ENSEIGNEMENTS

### 1. EDEL est le candidat à suivre (le « remplaçant » de QAIT)
- **+3.88%** sur la signature exacte QAIT, pic à 00h, creux à 11h — presque le même profil.
- **Déjà actif chez Hulk** : en position TRADE (IMPULSE_WAIT, m6 +5.5%), 12 positions, suivi continu.
- Prudence maison : le pattern QAIT n'avait que **2 jours de validation** (sur 14 requis).
  EDEL mérite la même quarantaine statistique avant exploitation.

### 2. PYTH a le même creux 11h qu'EDEL — à surveiller en paire
- +2.31%, creux 11h identique. Possible corrélation de timing entre micro-caps.

### 3. CHIP est l'INVERSE (jour > nuit, -3.29%)
- Pas un bruit : c'est le seul contre-signal net du portefeuille.
- Intéressant pour une stratégie inverse (acheter le matin, vendre le soir) — à creuser.

---

## ⚠️ MÉTHODO / LIMITES (honnêteté)
- Fenêtre courte : 3 jours de données (27-30/08) — le marché a bougé (guerre Iran,
  décret Trump, delisting). **Ces chiffres ne sont PAS une validation**.
- Le spread « brut » n'est pas le spread exploitable (frais, slippage, liquidité).
- Les micro-caps ont des volumes minuscules (RWAINC 0.00 M$, BIO 0.07 M$…) :
  même avec un pattern, l'exécution peut être impossible ou trop coûteuse.

## 📌 PROCHAINE ÉTAPE PROPOSÉE
- **Observateur de cycle EDEL** (même mécanique que l'observateur QAIT :
  profil horaire + journal jour par jour, mode ADVISOIRE 14 jours).
- **Sonde présence paires MEXC** (créée 30/08, tourne toutes les 6h) :
  plus jamais 7h de silence avant de voir un delisting.
