# STRATÉGIE D'AMPLITUDE — EDELUSDT (09/10/2026)

**Reprise de la fiche EDEL → où se dégage réellement la plus-value.**
Demande : « reprends la fiche EDEL, sors une stratégie avec des gains dans l'amplitude ».
Tout est **mesuré** sur des bougies, **paper uniquement**, **rien n'est câblé** (câblage = GO explicite).

Instrument : `hulk-mexc/scripts/backtest_edel_amplitude.py` (lecture seule, rejouable, multi-paires).
Prix : `hulk-mexc/runs/replay_cache/*_1h_45j.json` (1080 bougies 1 h, 24/08 → 08/10).
Frais **53,9 bps/côté** (spread_cout EDEL) → aller-retour ≈ 108 bps. Budget **30 $** par ligne.

---

## 1. Rappel de la fiche EDEL

| | |
|---|---|
| archétype | `illiquide_calme` · `mode_entree: IMPULSE` |
| seuils fiche | dip 5,5 % · rip 5,2 % · stop 10,3 % · trail arm 10,0 / giveback 4,0 |
| mur médian | 908 $ → **mise max 2 % ≈ 18 $** |
| spread coût | 53,9 bps · vol 35–37 % |

**Le fait qui commande tout** : sur 11→16/09, EDEL a fait **+156 %** et le moteur a converti ça en **+0,98 $** réalisé — **0,6 % de la montée convertie en cash**. Le seul vrai gain de récolte de l'histoire du moteur sur cette paire (`stake_out_2x`, **+5,27 $**) prouve que le moteur **sait récolter quand la taille est réelle** :
> le levier n'est pas le seuil de sortie, c'est **l'AMPLITUDE + la TAILLE**.

Sur la fenêtre de cache (45 j) EDEL fait **×4,04** (0,00875 → 0,03534 ; sommet 0,05282) → le `hold`, le juge, vaut **+90,51 $**.

---

## 2. Ce qui est mesuré — spécimen EDEL complet (mêmes bougies, mêmes frais, même budget)

`capture = part du mouvement hold convertie en cash`

| moteur | net $ | capture | achat/sortie | frais | DDmax | exposé |
|---|---:|---:|---:|---:|---:|---:|
| **A. moteur actuel** (approx. fiche EDEL) | **+8,50** | **9,4 %** | 20 / 20 | 2,21 | 10,5 % | 86 % |
| B. récolte — 1re prop. (trailing ATR) | +29,28 | 32,4 % | 29 / 19 | 3,24 | 24,0 % | 47 % |
| D. tendance portée (sortie régime seule) | +27,47 | 30,3 % | 18 / 10 | 2,09 | 38,4 % | 64 % |
| F. D + récolte par paliers (C1 maison) | +31,23 | 34,5 % | 19 / 16 | 2,22 | 38,4 % | 64 % |
| **G. SPEC RETENUE (symétrique)** | **+36,63** | **40,5 %** | 30 / 19 | 3,37 | **23,9 %** | 45 % |
| **G + filtre tendance (SMA240)** | **+44,25** | **48,9 %** | 18 / 10 | 2,18 | **17,9 %** | 33 % |
| C. hold (rien faire) | +90,51 | 100 % | — | — | — | 100 % |

**Lecture.** Le moteur convertit **9,4 %** ; la spec retenue en convertit **48,9 %** — **×5,2**, avec un drawdown **plus faible** (17,9 % vs 10,5 % mais **33 % de temps exposé au lieu de 86 %**). B/D/F montrent *pourquoi* : le trailing en cours de tendance **rend l'amplitude** ; la sortie **symétrique** sur le régime la **garde**.

**Stabilité 2 moitiés (EDEL, spec G)** : h1 **+18,85 $** / h2 **+13,42 $** (gate240 : +28,13 / +2,91). Le moteur, lui, est **négatif en 2e moitié** (−1,16 $) — la spec G reste positive des deux côtés.

---

## 3. La spec retenue — « G · récolte d'amplitude » (prête à câbler, sur GO)

Fenêtre 1 h. SMA = moyenne simple des **n dernières clôtures**. Aucun lookahead (on agit à la clôture).

1. **Entrée** — `close > SMA24` **ET** `close > plus-haut des 24 clôtures précédentes` (cassure = rafale IMPULSE), **ET** `close > SMA240` (filtre de tendance longue, 10 j). Mise = `budget / 3`, tranche min `budget / 8` (pas de poussière).
2. **Pyramide** — ajoute `budget / 3` à chaque **+8 % au-dessus du dernier ajout**, jusqu'à 3 tranches. On grossit **avec** la tendance.
3. **Sortie totale** — dès qu'une clôture repasse **sous la SMA24** (1 clôture). Pas de stop dans la mèche, pas de trailing fixe, pas de giveback en %.
4. **Taille conforme fiche** (mur × 2 % ≈ 18 $) : à 18 $, `+37,01 $` sur la même fenêtre (capture 68 %) — la mise fixe **réduit la taille après une perte**, ce qui amortit les drawdowns.

Ce que ça **n'est pas** : un stop serré, un giveback en %, un plafond d'empilement qui bloque. **Ce sont exactement les couches ajoutées après le 10/09 qui ont tué le PnL d'EDEL** (fusible 1,5×σ, stop-guard + dust_sweep, `REENTRY_MAX`) — elles ne figurent pas ici.

---

## 4. CROSS-CHECK multi-paires — l'edge est **ciblé**, pas global

20 paires, mêmes règles, mêmes frais, mêmes caches 45 j :

| paire | moteur | specG | G+gate240 | hold |
|---|---:|---:|---:|---:|
| EDELUSDT | +8,50 | **+36,63** | **+44,25** | +90,51 |
| QNTUSDT | +19,04 | **+43,92** | **+46,57** | +82,71 |
| WUSDT | +5,53 | +2,47 | +1,69 | +22,17 |
| CHIPUSDT | +2,68 | −4,72 | −5,52 | +15,77 |
| PYTHUSDT | +4,44 | −0,89 | +1,23 | +14,25 |
| … 15 autres | … | … | … | … |
| RIZEUSDT | +11,34 | +8,75 | +0,95 | −3,78 |
| **SOMME** | **+66,43** | +60,75 | **+76,99** | +270,47 |

**Le honnête à dire** : la spec G **ne bat le moteur que sur 2/20 paires** (3/20 avec le filtre) — mais **sur celles qui tendent, elle le pulvérise** : **EDEL −8,50 → +44,25** et **QNT +19,04 → +46,57**, soit **+53 $ sur 2 lignes en 45 j** là où le moteur n'en fait que +27,5. Ailleurs elle whipsaw (CHIP, PYTH, ZBCN, RED, ETH, BTC : légèrement négative) → c'est **le filtre SMA240** qui coupe ces faux départs : la somme passe de +60,75 à **+76,99 vs +66,43** pour le moteur.

⇒ **Conclusion opérationnelle** : ce n'est **pas un remplacement global**. C'est un **MODE PAR PAIRE**, à activer **uniquement sur les paires en tendance longue haussière** (aujourd'hui : **EDEL, QNT** — précisément les deux plus grosses pertes du moteur vs hold, −23,64 $ et −15,06 $ au cockpit du 09/10).

---

## 5. LE VRAI VERDICT — c'est la **SORTIE** qui détruit la valeur (« le hold gagne ? »)

Question de Christophe : *« donc le hold bat tout ? »* — **OUI, sur cette fenêtre, et voici pourquoi ça change tout.**

| EDEL, 45 j | net $ | capture | DDmax | capital |
|---|---:|---:|---:|---|
| hold (bar 0 — l'oracle) | **+90,51** | 100 % | 33,2 % | 100 % du temps |
| **entrer au 1er signal, NE JAMAIS SORTIR** | **+64,23** | **71,0 %** | — | 100 % |
| spec G (sortie `close < SMA24`) | +44,25 | 48,9 % | 17,9 % | 33 % |
| moteur actuel | +8,50 | 9,4 % | 10,5 % | 86 % |

**20 paires, mêmes règles** : **« entrer au 1er signal, ne jamais sortir » = +256,36 $** — contre **+66,43 $** pour le moteur et +60,75 $ pour la spec G. **×4.**

**Contre-épreuve** : allonger la sortie *dégrade* au lieu d'améliorer (sortie `SMA72` +39,59 · `SMA120` +26,45 · `SMA240` +36,92 · `SMA480` +22,96, tous *moins bons* que `SMA24` +44,25). Donc la spec G est **déjà au meilleur de ce qu'une règle de sortie peut faire** : le reste de l'écart avec le hold n'est **pas** récupérable en réglant un seuil.

⇒ **Le diagnostic change de nature.** Ce n'est pas la qualité de l'**entrée** qui plafonne le PnL — c'est l'**appareil de sortie** (dip/rip/stop/trail/giveback). Chaque sortie transforme une pâte qui compose en cash qui ne compose plus, et paie 108 bps pour le privilège. **Le seul levier restant est de sortir beaucoup moins.**

**Le prix, qu'il ne faut pas cacher** : « ne jamais sortir » = **aucun stop**, capital **immobilisé 100 % du temps**, et un drawdown de **−33,2 %** sur EDEL (93 % du temps sous l'eau). Et **réserve R8 majeure** : ces 20 caches sont des paires que le moteur **suit** — si le choix de l'univers est lui-même biaisé vers le haut (survivance), le ×4 est gonflé ; je **ne peux pas l'exclure**, donc ce +256 $ est un **plafond**, pas un résultat acquis.

## 6. Sensibilité (honnêteté R8)

Grille EDEL (net $ / DDmax), entrée SMA n × sortie régime :

| | buf0 cf1 | buf1 cf2 | buf1.5 cf2 |
|---|---:|---:|---:|
| SMA12 | +10,44 / 21 % | +47,31 / 24 % | +31,69 / 34 % |
| SMA24 | **+36,63 / 24 %** | +37,40 / 32 % | +37,07 / 34 % |
| SMA36 | +48,76 / 23 % | +37,06 / 29 % | +34,09 / 30 % |
| SMA48 | +47,42 / 24 % | +34,29 / 39 % | +35,15 / 38 % |
| SMA72 | +30,43 / 35 % | +27,47 / 38 % | +26,21 / 39 % |

→ **le signe est robuste** (tout est positif, +10 à +49 $) mais **la magnitude n'est pas fiable au dollar près**. J'ai **retenu la spec symétrique** (SMA24, buf 0, confirm 1) plutôt que le maximum de grille (SMA36/SMA48) pour ne pas ajuster aux données.

## 7. Limites déclarées (à ne pas maquiller)

- **1 fenêtre de 45 j, bougies 1 h.** C'est une **étude**, pas une preuve hors échantillon. Une telle règle ne vaut que sur des paires qui **tendent** — elle le dit elle-même (§4).
- Mèches intra-heure mal vues (ce qui **favorise** la sortie sur clôture).
- Frais au spread de la fiche (53,9 bps/côté) ; **pas de slippage d'impact** modélisé.
- Le paramètre exact (SMA 24/240, +8 %, 3 tranches) est **choisi**, pas prouvé.
- Le `hold` reste devant (**×4**) : la récolte **conserve ~40–49 %** de la pâte — déjà 5× mieux que le moteur, mais pas le hold.
- « A. moteur actuel » est une **approximation déclarée** de la fiche (dip/stop/trail/giveback), pas le moteur câblé.

## 8. Ce qu'il reste à faire (et ce qui exige un GO)

1. **Trancher la question de fond que la mesure pose** : si la **sortie** est le problème, la bonne expérience suivante n'est pas « quel seuil de sortie », mais **« sort-on du tout ? »** — et **combien de paires l'univers peut-il porter en restant investi** (capital immobilisé).
2. **Vérifier le biais de survivance** de l'univers des 20 caches (le +256 $ en dépend directement) **avant** d'en tirer une règle : rejouer sur un univers NON filtré.
3. **GO** pour câbler un mode par paire (spec G) dans `paper_diprip.py`, flags réversibles, **paper uniquement**. Rien n'est câblé à cette heure.
4. Toute modif moteur = **spec figée avant test** + **pré-déclaration AVANT écriture** + re-scellement.
