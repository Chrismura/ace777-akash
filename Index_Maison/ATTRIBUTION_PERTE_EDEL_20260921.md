# ATTRIBUTION DE LA PERTE — EDELUSDT

**21/09/2026 · Buffy · 0 ordre, 0 €, moteur non touché.**

Question posée (Christophe) : *« sur EDEL à mon avis ce n'est pas la liquidité, c'est l'entrée
qu'il a ratée — mais ce dernier spike, celui d'avant pas (je crois). D'où vient la perte ?
Et chaque actif a sa fiche, tout doit être écrit. »*

Réponse : **il a raison sur les trois points.** Voici les mesures.

---

## 1. L'actif : son histoire, telle que le moteur l'a écrite lui-même

Zigzag ≥ 15 % sur le log continu (`runs/croisement_contexte.jsonl` **+ ses archives de
rotation**, sinon la fenêtre vivante ne fait que 24 h et l'histoire disparaît — leçon du 20/09).

| # | De | prix | Vers | prix | Amplitude | Durée |
|---|---|---|---|---|---|---|
| 1 | pic 16/09 12:09Z | 0,02808 | creux 17/09 19:06Z | 0,01806 | 🔻 **−35,7 %** | 31 h |
| 2 | creux 17/09 19:06Z | 0,01806 | pic 18/09 19:03Z | 0,02495 | 🔺 **+38,2 %** | 24 h |
| 3 | pic 18/09 19:03Z | 0,02495 | creux 20/09 06:56Z | 0,01905 | 🔻 **−23,6 %** | 36 h |
| — | **EN COURS** | creux 20/09 06:56Z | 0,01905 | aujourd'hui 0,02958 | 🔺 **+55,3 %** | en cours |

C'est **exactement le récit de Christophe** : EDEL monte de ~40 %, redonne tout dans la
descente — et c'est **de cette descente que part le nouveau set-up** (`EDEL_SPEC_V2_SIMU_20260918.json`,
écrit le 18/09 00:27, pendant le creux). Le cycle **actuel est une hausse de +55,3 %** depuis
le fond du 20/09 06:56Z.

## 2. Ce que le moteur a capté sur ces cycles

| | mesuré |
|---|---:|
| Seed (24/08 : 1 144,16 tokens @ 0,00874 = 10,00 $) | — |
| **Réalisé total sur EDEL** (12 entrées / 18 sorties) | **+1,85 $** |
| dont le **seed** (3 sorties : 05/09 +105 %, 05/09 crash −38,5 %, 07/09 balayage) | **+1,66 $** |
| dont les **11 ré-entrées** du pump précédent | **+0,19 $** |
| **L'actif a fait +238 %** (0,00874 → 0,02958) | |

## 3. D'où vient la perte : **deux causes distinctes**, mesurées

### Cause A — l'ENTRÉE ratée sur le dernier spike (Christophe a raison)

- Dernière sortie : **20/09 00:12-00:13Z**, 219,76 tokens pour **4,36 $** à 0,01981.
- Le fond est à **0,01905 le 20/09 06:56Z** → **on a vendu 3,8 % au-dessus du fond**, ~7 h avant.
- Ensuite : **+55,3 %**. On n'a **rien retenté**.

**Pourquoi aucune ré-entrée** — ce n'est pas une porte qui a refusé, c'est un **déclencheur
qui n'a jamais pu s'armer** :

```
profil EDEL   : mode_entree = IMPULSE   (EDEL ne bouge que par rafales IMPULSE : m6 70 % vs 4 %)
règle         : IMPULSE_PULLBACK_MIN_PCT = 5  ·  IMPULSE_PULLBACK_FRAC = 0,30
                → il faut un REPLI ≥ max(5 %, 30 % du mouvement 6 h)
pendant le pump : 1 796 points de log, 100 % en régime IMPULSE_WAIT,
                  m6 de +9,8 % à +36,6 % → seuil exigé jusqu'à ~11 %
                  le prix est monté DROIT (aucun repli) → dd6 ≈ 0 → JAMAIS armé
```

**La règle d'entrée exige un repli : un pump en ligne droite est structurellement
in-attaquable.** C'est un angle mort de conception, pas un réglage.

**Le manque, chiffré** :
| scénario | manque |
|---|---:|
| la position qu'on avait (219,76 tokens) gardée jusqu'à 0,02958 | **+2,14 $** |
| ré-entrée au fond (0,01905) avec le plafond mur d'EDEL (21,8 $) | **+12,05 $** |
| ré-entrée au fond avec la base moteur (30 $) | **+16,58 $** |

### Cause B — la SORTIE du seed (le vrai trou historique)

| | |
|---|---:|
| Seed 10,00 $ → si **gardé** jusqu'à 0,02958 | **33,84 $** (+23,84 $) |
| Ce que le moteur a réalisé sur le seed | +1,66 $ |
| **MANQUE** | **−22,19 $** |

Mécanique : le **05/09 à 00:40Z** on vend la moitié à **+105 %** (bien), puis **1 minute plus
tard** le paquet restant est crash-vendu (‑38,5 %, `crash_dd=38.5>=20`) — **le fond du
mouvement** ; le 07/09 un balayage solde le reste. On liquide l'actif **à son premier
doublement**, 10 jours avant ses +238 %.

## 4. Ce que Christophe avait raison de corriger : **ce n'est PAS la liquidité**

| mesure EDEL (profil + log) | valeur | lecture |
|---|---:|---|
| solidité du mur (`wall_strength`) | **0,889** | mur fort |
| mur bid moyen | **1 088 $** | présent |
| spread médian | **26,95 bps** | normal pour un small cap |
| Amihud (illiquidité) | **6,6e−06**, en **baisse** le 20-21/09 | on pouvait sortir sans casser le prix |

Ma phrase précédente (« le vrai limiteur c'est la liquidité ») était une conclusion **générale
sur la chaîne de sizing**, pas une mesure du cas EDEL — je la corrige ici : **sur EDEL, ni la
liquidité ni le mur n'ont empêché quoi que ce soit.**

## 5. Ce que ça implique (à trancher, non touché)

1. **Cause A (déclencheur `IMPULSE` sans repli)** : c'est un **levier d'entrée** — à chiffrer
   avant de toucher (rejouer le mois en autorisant une entrée sur force/momentum sans repli,
   avec le stop qui va avec). Le `EDEL_SPEC_V2` déclare **+12,15 $ · n=16 · WR 75 %** et
   **aucun code ne le lisait** : il est désormais porté par la fiche de l'actif.
2. **Cause B (sortie)** : c'est la **même fuite** que la radiographie du 20/09 (« la fuite est
   à la sortie »), confirmée paire par paire.
3. **La règle tenue** : chaque actif a sa fiche (`runs/SUIVI_SETUP_<PAIRE>.md`, 20 actifs) et
   elle porte désormais **son historique de cycles, ce que le moteur y a capté, et ses setups
   déclarés** — plus rien du travail d'un actif ne peut se perdre.

---

## 6. LES DEUX CALCULS REFETS (GO Christophe 21/09) — `chiffrage_entree_sortie_replay.py`

**Critères PRÉ-ENREGISTRÉS avant lecture** (pour ne pas déplacer le but) : un levier ne compte
que si (a) le gain est **du même signe dans les deux moitiés** (60 % / 40 % hors échantillon)
et (b) il n'est **pas porté par une seule paire** (< 70 % du net). Mise fixe 30 $, frais 5 bps/côté,
entrée au tick suivant (pas de look-ahead).

### 6.1 GO 1 — l'ENTRÉE : **66 % des rafales sont structurellement inaccessibles** (n = épisodes)

Sur **90 jours × 20 paires** (klines 1 h), une rafale = suite de ticks où m6 ≥ 8 % avec amplitude ≥ 5 %.

| | nb | amplitude moyenne |
|---|---:|---:|
| rafales relevées | 38 | |
| **ACCESSIBLES** (dd6 atteint max(dip, 5 %, 0,30·m6)) | 13 | +23,2 % |
| **INACCESSIBLES** (jamais — le prix monte droit) | **25 = 66 %** | +11,4 % |

Amplitudes manquées : **RIZE 128 % · EDEL 54 % · CHIP 42 % · RWAINC 20 % · RED 11 %.**

> **C'est la réponse à la question posée.** La règle de repli ne « filtre » pas : elle **ferme
> la majorité des rafales**. Sur un actif restreint à IMPULSE (EDEL), c'est presque tout.

Effet en $ (30 $ fixe) : **EDEL, 90 j** : entrée actuelle **−1,10 $** (4 trades) · entrée sans repli **+15,89 $** (15 trades).
Mais au niveau portefeuille, l'entrée seule est **incohérente entre moitiés** (test −3,08 → +30,59 $
mais 1re moitié +19,84 → −3,17 $) → **non validée seule**, à combiner avec la sortie (§6.2).

### 6.2 GO 2 — la SORTIE : la garder vaut mieux que la sortir (cohérent sur les deux moitiés)

| combinaison | net 1re moitié | net test | verdict |
|---|---:|---:|---|
| E0 + X0 *(actuel)* | +19,84 $ | **−3,08 $** | référence |
| E0 + X1 *(1er palier à ×2, plus de stop sous le multiple)* | +25,56 $ | **+71,65 $** | ✅ cohérent — mais 58 % du net sur **1 paire** (EDEL) ⚠️ |
| **E2 + X2** *(sans repli + trailing seul)* | +21,80 $ | **+59,42 $** | ✅ cohérent · **9/13 paires gagnantes · top paire 42 %** |

**E2+X2 = +62,50 $ sur 90 jours à mise fixe** (30 $), contre la référence, et c'est la variante la
**moins concentrée**. Le levier : l'entrée récupère l'amplitude (6.1), la sortie **ne la redonne plus**.

### 6.3 Limites écrites (à ne pas oublier)

- Source klines = **reproduction** de m6/dd6 (le moteur les calcule sur ses propres ticks) ; l'effet
  **isolé** des deux règles est mesuré, **pas** le P&L absolu du moteur.
- 90 jours = **une** composition de régimes ; n faible en test (9-43 trades).
- Les variantes de sortie **élargissent le pire trade** (−5,19 $ → −13,00 $) : plus de gain, **plus de
  drawdown** — c'est le prix, et il se déclare.
- Rien n'est câblé : ces chiffres sont une **hypothèse à forward-tester**, pas une modification.

### Provenance (tout est rejouable)
- `hulk-mexc/runs/croisement_contexte.jsonl` + `.1.gz` + `.2.gz` (prix par paire, par cycle)
- `hulk-mexc/runs/PAPER_V1_*.csv` (2 plus récents, **dédoublonnés** : le moteur copie son
  journal à chaque `--resume`)
- `hulk-mexc/strategie/universe_profils.json` (seuils réels du profil EDEL)
- `hulk-mexc/config/defaults.env` (`IMPULSE_PULLBACK_MIN_PCT`, `IMPULSE_PULLBACK_FRAC`)
- `hulk-mexc/runs/EDEL_SPEC_V2_SIMU_20260918.json`, `EDEL_SETUP_BACKTEST_20260917.json`
- `hulk-mexc/scripts/chiffrage_entree_sortie_replay.py` (GO 1 + GO 2 ; `--klines` = 90 j, sinon log moteur)
- `hulk-mexc/runs/SIMU_KL_*_90d.json` (klines 1 h, 20 paires, 20/06 → 18/09)
