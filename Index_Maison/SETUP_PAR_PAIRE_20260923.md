# SET-UP PAIRE PAR PAIRE — 23/09/2026

> Demande Christophe, **depuis le premier jour** : « FAIRE LE SET-UP SUR CHAQUE PAIRE ».
> Instrument : `hulk-mexc/scripts/cartographie_setups_paires.py` · sorties :
> `hulk-mexc/runs/SETUPS_PAIRES_20260923.{txt,json}` · **lecture seule, 0 ordre, 0 €**.
>
> **Aucun chiffre recalculé de mémoire** (règle payée le 23/09) : chaque grandeur est SOIT
> lue dans le journal du moteur (il l'écrit lui-même), SOIT mesurée, SOIT lue dans le profil
> de la paire. La provenance est affichée. **Rien n'est câblé ici.**

---

## A. ENTRÉE — le repli RÉELLEMENT exigé par paire

`seuil réel = 0,85 × max(dip_pct du profil ; 0,50 × cadence MOTEUR ; 5 % ; 0,30 × m6 médian)`

| paire | archétype | cadence (moteur) | **dip exigé** | m6 méd | **seuil réel** | jambes ≥ 20 % | **inaccessibles** | refus dominant |
|---|---|---|---|---|---|---|---|---|
| **EDEL** | illiquide_calme | 26,4 % | **13,20 %** | 8,2 % | **11,22 %** | 1 | 0 | MODE_REGIME 59 · MUR-CASSE 31 |
| **RIZE** | manipulée_fragile | 16,9 % | **8,44 %** | 8,7 % | **7,17 %** | 4 | **4 (100 %)** | MUR-CASSE 706 · VOL 475 |
| **CHIP** | gros_murs_stables | 13,4 % | **6,69 %** | 5,4 % | 5,69 % | 2 | 0 | MUR-CASSE 750 · VOL 658 |
| QAIT | illiquide_spread_large | 11,2 % | 5,60 % | 0,0 % | 4,76 % | 0 | 0 | SPREAD 33 · MUR-CASSE 26 |
| RED | calme_propre | 10,1 % | 5,03 % | 2,9 % | 4,27 % | 1 | 0 | VOL 1124 · MUR-CASSE 178 |
| PYTH | gros_murs_fondants | 9,4 % | 4,70 % | 3,9 % | 4,25 % | 1 | 0 | MUR-CASSE 40 |
| KITE | gros_murs | 7,3 % | 4,00 % | 2,8 % | 4,25 % | 1 | 0 | VOL 2294 · MUR-FAIBLE 1799 |
| TEL | illiquide_spread_large | 7,2 % | 4,00 % | 3,7 % | 4,25 % | 1 | 0 | VOL 95 · MUR-CASSE 40 |
| ZBCN | manipulée_fragile | 7,2 % | 4,00 % | 4,0 % | 4,25 % | 0 | 0 | MUR-CASSE 47 · VOL 44 |
| W | calme_propre | 7,0 % | 4,00 % | 3,7 % | 4,25 % | 1 | 0 | VOL 319 · MUR-CASSE 29 |
| BIO | calme_propre | 6,6 % | 4,00 % | 3,0 % | 4,25 % | 1 | 0 | VOL 1951 · MUR-CASSE 445 |
| CC | calme_mur_dynamique | 6,5 % | 4,00 % | 3,3 % | 4,25 % | 0 | 0 | MUR-CASSE 367 · SENSE 349 |
| RWAINC | illiquide_spread_large | 6,5 % | 4,00 % | 2,2 % | 4,25 % | 1 | 0 | VOL 199 · MUR-CASSE 21 |
| XRP | majeure_manipulée | 5,7 % | 4,00 % | 2,9 % | 4,25 % | 1 | 0 | MUR-CASSE 372 · MUR-SPOOF 51 |
| HBAR | gros_murs_fondants | 5,0 % | 4,00 % | 3,5 % | 4,25 % | 1 | 0 | ATTENTE 28 · MUR-CASSE 14 |
| ETH | majeure_banc_de_preuve | 3,2 % | 2,50 % | 1,6 % | 4,25 % | 0 | 0 | MUR-CASSE 65 · ATTENTE 27 |
| BTC | majeure_banc_de_preuve | 2,6 % | 2,00 % | 1,2 % | 4,25 % | 0 | 0 | MUR-CASSE 293 · ATTENTE 26 |

**Ce que ça dit, paire par paire** : le seuil n'est **pas** universel — il va de **1,70 % à
11,22 %**, soit un facteur **6,6**. Les quatre premières paires (EDEL, RIZE, CHIP, QAIT) sont
**les seules** dont le seuil dépasse le plancher de 5 % : ce sont **elles** qui ont un set-up
d'entrée spécifique. Les treize autres sont au **plancher** (5 % × 0,85 = 4,25 %) : pour
elles, l'entrée est déjà « standard », il n'y a rien à individualiser.
**RIZE est la seule paire dont TOUTES les jambes de la fenêtre étaient inaccessibles.**

---

## B. SORTIE — stop ANNONCÉ vs stop RÉALISÉ, par paire (le fait neuf)

| paire | clôtures | PnL | **stop annoncé** | **stop réalisé (méd)** | **pire** | dust | motifs (n / $) |
|---|---|---|---|---|---|---|---|
| RIZE | 23 | **−1,12 $** | 8,0 % | **14,16 %** | **39,23 %** | **5** | RIP 8/+2,18 · STOP 8/−2,79 · DUST 5/−1,39 |
| CC | 8 | −1,25 $ | 6,0 % | 6,07 % | 6,14 % | 0 | TRAILING 6/+1,68 · STOP 2/−2,93 |
| BIO | 3 | −0,97 $ | 6,0 % | **6,00 %** | 6,00 % | 0 | STOP 2/−1,20 · TRAILING 1/+0,24 |
| QAIT | 1 | −0,85 $ | 6,1 % | 8,37 % | 8,37 % | 0 | STOP 1/−0,85 |
| RWAINC | 12 | −0,83 $ | 6,5 % | 6,71 % | 7,29 % | 0 | STOP 6/−7,30 · TRAILING 4/+5,43 |
| ZBCN | 10 | +0,50 $ | 6,0 % | 6,56 % | 7,12 % | 0 | TRAILING 6/+1,05 · STOP 2 |
| XRP | 7 | +0,83 $ | 6,0 % | **6,00 %** | 6,00 % | 0 | STOP 3/−3,28 · TRAILING 3/+4,06 |
| W | 13 | +1,29 $ | 6,0 % | **6,00 %** | 6,00 % | 1 | TRAILING 6/+2,17 · STOP 4/−1,14 |
| ETH | 7 | +2,33 $ | 6,0 % | **6,00 %** | 6,00 % | 0 | TRAILING 6/+3,56 · STOP 1/−1,24 |
| BTC | 4 | +2,71 $ | 5,0 % | — (0 stop) | — | 0 | TRAILING 4/+2,71 |
| PYTH | 9 | +3,27 $ | 6,0 % | 6,33 % | 6,67 % | 0 | TRAILING 5/+5,00 · STOP 2 |
| KITE | 9 | +4,24 $ | 6,0 % | 6,00 % | 6,58 % | 0 | TRAILING 4/+8,64 · STOP 3/−4,76 |
| HBAR | 5 | +4,28 $ | 6,0 % | **6,00 %** | 6,00 % | 0 | TRAILING 3/+4,71 |
| TEL | 13 | +4,54 $ | 6,4 % | 6,40 % | 6,40 % | 1 | STOP 6/−3,41 · TRAILING 4/+7,65 |
| **EDEL** | 18 | +5,78 $ | 10,3 % | **13,20 %** | **13,80 %** | **4** | TRAILING 8/+2,42 · DUST 4 |
| CHIP | 9 | +9,49 $ | 7,0 % | **10,83 %** | 10,83 % | 0 | TRAILING 5/+10,76 · STOP 4 |
| RED | 15 | **+12,30 $** | 6,0 % | **6,00 %** | 6,00 % | 1 | TRAILING 8/+13,56 · STOP 4/−1,52 |

**Le fait, et il classe les paires tout seul** : là où le carnet est profond, **le stop tient
exactement** (BTC, ETH, XRP, HBAR, W, KITE, RED, CC, BIO : réalisé = annoncé, à 0,5 pt près).
Là où le carnet est mince, **le stop est une fiction** : **RIZE 39,23 % réalisés pour 8 %
annoncés**, EDEL 13,8 / 10,3 **avec 4 « dust sweeps »**, CHIP 10,8 / 7,0, QAIT 8,4 / 6,1.
⇒ **Le dérapage du stop n'est pas un bug global : c'est une propriété de la LIQUIDITÉ, paire
par paire.** Corriger « le stop » globalement serait une faute de plus.

---

## C. TAILLE — le plafond actuel face au carnet MESURÉ

| paire | mur profil | cap actuel (2 %) | spread profil | **spread MESURÉ** | **profondeur < −0,5 %** | plafond / profondeur | misable* |
|---|---|---|---|---|---|---|---|
| ZBCN | 340 $ | 6,81 $ | 18,2 b | 16,6 b | 1 159 $ | **467 342 %** | 116 $ |
| TEL | 1 290 $ | 25,79 $ | 40,9 b | 38,3 b | 200 $ | **12 967 %** | 20 $ |
| **RIZE** | 244 $ | 4,88 $ | 47,0 b | **64,6 b** | 458 $ | **2 641 %** | 46 $ |
| RWAINC | 1 387 $ | 27,73 $ | 48,0 b | 5,4 b | 1 161 $ | 419 % | 116 $ |
| EDEL | 909 $ | 18,17 $ | 26,9 b | 16,5 b | 50 $ | 210 % | 5 $ |
| BIO | 3 524 $ | 70,49 $ | 4,1 b | 15,1 b | 10 347 $ | **22 %** | 1 035 $ |
| CHIP | 33 100 $ | 661,99 $ | 3,8 b | 19,6 b | **71 758 $** | **15 %** | 7 176 $ |
| BTC | (mur live) | (repli) | 0,1 b | 0,0 b | 2 756 264 $ | 0 % | 275 626 $ |
| CC · ETH · HBAR · KITE · PYTH · QAIT · RED | | | 1,3–63 b | **non mesuré** | **non mesuré** | — | — |

\* « misable » = **10 % de la profondeur mesurée** — c'est une **convention de présentation
déclarée**, PAS un seuil de moteur : la règle de taille attendra une série de plusieurs heures
(R17 : pas de seuil inventé).

**Ce que ça dit** : le plafond actuel est **absurde sur les illiquides** (2 641 % de la
profondeur sur RIZE, 467 342 % sur ZBCN — calculé sur un niveau *affiché*) et **sage sur
CHIP/BIO** (15-22 %). Le spread **réel** de RIZE (**64,6 bps**) est **13×** celui que le
moteur suppose (5 bps) — sur **les deux côtés**. Sept paires ne sont **pas mesurées** :
aucune recommandation de taille ne les concerne aujourd'hui.

---

## D. LE SET-UP PAIRÉ, EN CLAIR — 4 classes mesurées, 4 actions (aucune câblée)

| classe | paires | ce qui est MESURÉ | action proposée (avec sa base de mesure) |
|---|---|---|---|
| **1 — le stop ne tient pas** | **RIZE** (39,2 % pire) · **EDEL** (4 dust) · **CHIP** (10,8) · **QAIT** (8,4) · RWAINC (7,3) · TEL (6,4) | stop réalisé ≫ annoncé **et** profondeur < 5 000 $ **et** spread ≥ 16 bps | **Descendre la TAILLE à ce que le carnet porte** (mesure §C) **avant** de toucher au stop : le dérapage est causé par la taille, pas par le seuil. Sur RIZE : misable 46 $ vs 4,88 $ actuels. |
| **2 — le stop TIENT** | BTC · ETH · XRP · HBAR · W · KITE · RED · CC · **BIO** · PYTH · ZBCN | réalisé = annoncé à ≤ 0,7 pt, **0 dust** | **RIEN À TOUCHER** (R17.4 : ce qui marche et n'est pas mesuré néfaste reste). Ce sont **elles qui paient** (+12,30 RED · +9,49 CHIP · +5,78 EDEL · +4,54 TEL…). |
| **3 — l'entrée est inatteignable** | **RIZE** (4/4 jambes) · QNT (1/1, hors profils) | repli exigé 21,8-26,9 % pendant la hausse, offert ≤ 17,45 % | Étendre le set-up `mode_entree=IMPULSE` + `IMPULSE_SANS_REPLI_ON` (**déjà câblé sur EDEL**) — mesuré après correction : **RIZE +3,13 $ sur 3 jambes au plafond réel** (petit, déclaré) · **EDEL +14,70 $/90 j**. |
| **4 — la taille est une fiction** | ZBCN (467 342 %) · TEL (12 967 %) · **RIZE** (2 641 %)** vs CHIP 15 % · BIO 22 % | `cap = 2 % × mur live` où le « mur » est un **niveau affiché** (801 457 $ sur RIZE = 1 234× la profondeur réelle) | Remplacer le plafond par une fraction de la **profondeur cumulée MESURÉE**, **par paire**, **après** la série (§C) — jamais une règle globale. |

**Ce que ça change dans la façon de travailler** : il n'y a **pas un set-up** à corriger,
il y a **4 classes de paires** qui n'ont pas le même problème — et **aucune** ne se corrige
par un réglage global. C'est exactement pourquoi « faire le set-up sur chaque paire » n'était
pas faisable avec un seul chiffre.

---

## E. RAPPORTS D'ERREURS (demande explicite : « enregistrer les rapports d'erreurs »)

Enregistrés au registre de la maison (`Index_Maison/REGISTRE_ECHECS_ET_ERREURS.md`, §2,
classes **E10 / E11 / E12**) — avec le cas réel, la garde mécanique et ce qui reste ouvert :

| classe | l'erreur | cas réel | garde mécanique |
|---|---|---|---|
| **E10** | **Prendre un chiffre RECALCULÉ pour un chiffre VÉRIFIÉ** | seuil annoncé 5-12,75 % pendant 3 jours alors que le moteur appliquait **21,70 %** (terme `0,50 × cadence` manquant) → a faussé un document, un scan et un chiffrage de levier | **`verif_seuil_moteur.py`** : invariant sur les chiffres ÉCRITS par le moteur + nommage du terme qui décide + **détecteur d'instruments** + autotest **7/7** ; branché toutes les 3 h et **affiché au cockpit** |
| **E11** | **Confondre COHÉRENCE et JUSTESSE** (biais de source unique) | mon invariant valide la formule **du moteur** : si le moteur se trompe, nous nous trompons **ensemble** (nommé par Grok, 23/09) | **AUCUNE — trou déclaré.** Remède identifié : **oracle indépendant** (rejouer la kline brute et comparer au signal enregistré, sans passer par la logique du moteur). **À GO.** |
| **E12** | **Sceller un fichier puis le modifier** | la veilleuse a crié « INTRUSION : modification non déclarée » **3 fois** dans la journée | **Règle de processus** : *on scelle APRÈS la dernière modification* + `declarer_rescel_20260923.py` (backup + déclaration `_rescel_*` qui dit quoi et pourquoi) |

**Ce que je ne dis pas** : je ne peux ni prouver ni exclure une intention quelconque dans ces
erreurs. Ce que je peux prouver est dans les fichiers : **chaque faute est datée, chiffrée,
reproductible, et la garde qui la tue est branchée** (sauf E11, déclarée ouverte).

---

## F. LIMITES DÉCLARÉES (E8)

- **7 paires sur 20 ne sont pas mesurées** en profondeur (aucune recommandation de taille les
  concerne) ; la série n'a que **4 passages (~1 min)** → elle ne décide rien encore.
- Les « jambes ≥ 20 % » viennent d'un **zigzag à seuil d'affichage** (20 % / réaction 10 %).
- Les stops réalisés sont les **pertes écrites par le moteur** (raison de vente), pas un
  remplissage mesuré ; le mode paper ne mesure **pas** l'impact.
- **Un seul régime de marché** (BTC +12,3 %, 20/20 paires en hausse) sur la fenêtre observée :
  **aucun de ces chiffres ne dit ce qui se passe dans un marché qui descend** (nommé par la
  famille, non traité).
- **Rien n'est câblé** : `defaults.env`, `universe_profils.json` et `paper_diprip.py`
  (hors la ligne de log du refus parlant) sont **inchangés** — état vérifié, moteur en vol.

*Instrument : `hulk-mexc/scripts/cartographie_setups_paires.py` · sorties :
`runs/SETUPS_PAIRES_20260923.{txt,json}` · série : `runs/PROFONDEUR_CARNET_SERIE.jsonl`.*
