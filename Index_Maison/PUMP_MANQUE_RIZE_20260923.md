# PUMP MANQUÉ — RIZEUSDT, 22 → 23/09/2026 : autopsie chiffrée

> **Demande** (Christophe, 23/09 10:2xZ) : « explique-moi pourquoi RIZE a perdu le pump ! »
> **Méthode** : lecture du **log continu du moteur** (ses propres cycles : prix + régime écrits
> par lui), instrument neuf **`hulk-mexc/scripts/chiffrage_pump_manque.py`** (lecture seule,
> 0 ordre, 0 €). Sorties : `runs/CHIFFRAGE_PUMP_MANQUE_RIZE_20260923.{txt,json}`.
> **Rien n'est câblé, rien n'est modifié côté moteur.**

---

## 1. Le fait, daté et chiffré

| | |
|---|---|
| Bas | **2026-09-22T13:44:54Z · 0,001750** |
| Haut | **2026-09-23T07:22:20Z · 0,003182** |
| **Amplitude bas → haut** | **+81,8 %** |
| Depuis la mise à plat (02:15:45Z, 0,001952) | **+63,0 %** |
| Décisions de RIZE sur la fenêtre | **4 805 cycles** (1 toutes les ~20 s) |

## 2. Pourquoi le moteur n'est pas entré — la porte qui a tenu fermé

Régimes **écrits par le moteur lui-même**, à partir de l'instant où la paire est **à plat** :

| Régime | Cycles | Part | Ce que ça veut dire |
|---|---|---|---|
| `IMPULSE_WAIT` | **4 583** | **96,2 %** | rafale détectée, **repli pas encore venu** → sortie anticipée, pas d'entrée |
| `IMPULSE` | 183 | 3,8 % | **seule porte d'entrée ouverte** (et elle est **en bas**, 02:15:45 → 03:30:03Z) |

**Le point dur est là :** la règle d'entrée IMPULSE exige un repli
`impulse_entry = max(dip 4,2 % ; 5 % ; 0,30 × m6)` — soit **5,00 à 12,75 %** sur la fenêtre,
avec un `m6` monté jusqu'à **42,5 %**. Le prix est monté **en ligne droite** : le repli exigé
n'a **jamais** été atteint (c'est la définition même de `IMPULSE_WAIT`, écrite par le moteur,
4 583 cycles d'affilée). ⇒ **Le pump était structurellement in-attaquable. Ce n'est pas un
raté du moteur, c'est une règle qui interdit ce type de mouvement.**

**Et les 3,8 % de cycles où la porte ÉTAIT ouverte ?** Ils sont **au fond**, et c'est **une
autre porte** qui a refusé — lue dans le journal du run :
`VOL:vol_dry_vx=1,08–1,19<1,20_DRY` (24 lignes) et `VOL:vol_DRY_impulse_block`,
plus 9 `MUR-CASSE:16 → 72 %/s`. **Le volume « sec » a bloqué l'entrée au fond.**

> **Le chiffre qui retourne l'intuition :** après ce refus, le prix a encore **baissé de
> −13,8 %** (0,001952 → 0,001750) avant de monter. Si la porte volume n'avait pas bloqué,
> la règle aurait acheté **au début de la baisse** et se serait fait **stoppée à −8,2 %**.
> **La garde qui « a raté le pump » nous a évité une perte réelle.**

## 3. Ce que la règle aurait donné — contre-factuel, séquence complète

Sortie = **la sortie réelle de la paire** lue dans son profil (`calib`) : `stop 8 %` +
`trailing arm 11,4 % / giveback 4,55 %`, **aucun palier rip, aucun 2×** (`manage_open()`).
Ré-entrées autorisées + `STOP_COOLDOWN_HOURS=1` réel. Frais 5 bps/côté.
Départ du contre-factuel = **l'instant où la paire est réellement à plat** (02:15:45Z, dernière
vente du run) — *la 1ʳᵉ version de l'instrument « entrait » dans la position déjà ouverte :
piège attrapé et corrigé dans la même heure.*

| Scénario | Trades | Net (30 $ fixe) | **Net au plafond RÉEL (4,88 $)** |
|---|---|---|---|
| **E0 — règle actuelle** | 1 | **−2,50 $** | **−0,41 $** |
| **E2 — porte du repli levée** | 5 | +12,97 $ | **+2,11 $** |
| **Écart mesuré de la porte** | | **+15,47 $** | **+2,51 $** |

Détail E2 : `−8,2 % (stop)` puis `+10,1 %`, `+22,1 %`, `+16,4 %` (trailing, pics 20,4 / 32,9 /
21,1 %) puis une position ouverte à +3,3 %. **Le premier trade perd dans les deux scénarios**
(entrer « sans repli » à 02:15:45, c'est entrer dans la baisse).

## 4. La vraie limite n'est pas l'entrée, c'est la TAILLE

`RIZE` : archetype `manipulee_fragile`, **mur bid médian 243,78 $**, `mise_max_pct_mur = 2 %`
⇒ **plafond de mise 4,88 $**. Un mouvement de **+81,8 %** sur une position de 4,88 $ vaut
**quelques dollars**. Le composé des 5 multiplicateurs + ce plafond est ce qui rabote (mesuré
le 21/09 : annoncé 32,85 $ vs **engagé 15,16 $**, ratio ×0,35). **On ne peut pas « prendre le
pump » sur un actif dont le carnet ne porte que 4,88 $.**

## 5. Limites DÉCLARÉES (E8) — ce que ce chiffre n'est PAS

- **Une seule porte est rejouée** : celle du repli. Les portes **volume / mur / spread /
  plancher / fusible** **ne le sont pas** — et au fond, c'est **le volume** qui refusait.
  Ce chiffre mesure donc **la porte**, pas le P&L du moteur.
- `dd6` **n'est pas journalisé** : reconstruit sur le chemin de prix (fidélité du régime
  recalculé **68,8 %** → réserve R14). La **preuve** reste la décision écrite par le moteur.
- Sortie réelle parfois scindée 50/50 par le garde-fou d'amplitude (`SELL_FULL`) ; modélisée
  ici en une fois au même niveau de prix.
- Fenêtre de **30 h**, **une** paire, **un** épisode : ce n'est pas un verdict statistique.

## 6. Décision proposée (aucun câblage sans GO)

1. **RIEN TOUCHER MAINTENANT.** Le gain mesuré au plafond réel est **+2,11 $** : on ne modifie
   pas un moteur en production pour ça (R17/R18).
2. **Extension du set-up « sans repli » (mesuré sur EDEL 21/09 : +18,58 $/90 j) aux autres
   paires de rafale** : c'est un **chantier à chiffrer paire par paire** — le même instrument
   tourne sur n'importe quelle paire (`--paire`), sur **toute** la fenêtre du log continu.
   Le déclencheur, si GO : `mode_entree = "IMPULSE"` dans `strategie/universe_profils.json`
   (aujourd'hui **EDEL seule**), 1 ligne par paire, réversible.
3. **La mesure qui manque avant de décider :** rejouer **les 5 portes** (pas seulement le
   repli) sur l'épisode — sans ça, on ne sait pas si E2 aurait réellement pu acheter.

## 7. Le scan des 5 derniers jours — « combien on en laisse, et pourquoi »

Demande Christophe : « trop de ratés ces derniers jours, pas possible, après tous les check-up
c'est pire ». Nouveau mode `--scan` du **même** instrument (lecture seule) : **20 paires**,
fenêtre **18/09 00:54Z → 23/09 08:32Z** (log continu + archives de rotation), zigzag ≥ 20 %
*(seuil d'AFFICHAGE déclaré, pas un seuil de décision)* et **PnL réellement réalisé** par la paire
autour de chaque mouvement (colonne `pnl` du run). Sortie : `runs/CHIFFRAGE_PUMPS_MANQUES_SCAN_20260923.txt`.

| Constat | Chiffre |
|---|---|
| Mouvements ≥ 20 % détectés | **18** (4 **RAPIDES** ≤ 12 h · 14 lents) |
| Mouvements rapides **non achetés** | **3 sur 4** → taux d'intervention **25 %** |
| Amplitude laissée à plat (rien acheté) | **193 %**, dont **94 % sur les rapides** |
| PnL réalisé sur ces 3 pumps RIZE | **0,00 $** |
| Portes qui ont refusé les ratés | **ATTENTE (le repli) 4** · VOL 1 · *aucun refus écrit 2 (trou déclaré)* |
| Paires concernées | **RIZE 3** · FLUID · QNT · CHIP · BIO |
| **PnL du moteur sur la même fenêtre** | **5,85 $ → 42,17 $ = +36,32 $** (colonne `pnl_total`, aucune reconstruction) |

**Les 3 pumps RIZE ratés, datés :** +35,7 % en 3,1 h (19:31→22:40Z) · +31,3 % en 4,3 h
(13:44→18:04Z) · +27,0 % en 8,6 h (22:44→07:22Z) — **tous refusés par `ATTENTE` (`IMPULSE_WAIT`)**, PnL 0,00 $.

### La règle, nommée

Notre entrée **exige un repli** (`impulse_entry = max(dip 4,2 % ; 5 % ; 0,30 × m6)`) ; un pump
vertical n'en donne pas. Conséquence mesurée : **on prend les dérives lentes** (RED +7,29 ·
KITE +5,49 · TEL +4,71 · RWAINC +4,10 · CHIP +4,06 — là où le repli apparaît) **et on rate les
pumps rapides**. C'est une **propriété de la règle**, pas une panne — et RIZE est **la seule paire
perdante** (−1,04 $) parce qu'on y entre tard et qu'on s'y fait stopper.

### Le vrai trou (et il est de moi)

Tous nos instruments mesuraient **le $ des gardes** — ce qu'on **protège** (MUR-CASSE −138 $,
MUR-FAIBLE −107 $, VOL −82 $, SENSE −16,8 $…). **Aucun** ne mesurait **ce qu'on laisse passer**.
Un système peut donc être **100 % vert sur la protection** et rater **193 % d'amplitude** :
c'est exactement notre cas, et c'est pourquoi les check-up ne l'ont jamais vu. Ce scan est le
gardien qui manquait (R15 : un chiffre qu'on ne regarde pas n'existe pas).

### Limites déclarées (E8)

« Intervenu » (un BUY) **n'est pas** « capté » (EDEL : intervenu sur +80,2 % de mouvement,
**+0,37 $** réalisé) · la somme des PnL par jambe est **non additive** (fenêtres qui se
recouvrent) · **2 mouvements sans refus écrit** = trou de mesure · le scan **ne rejoue aucune des
5 portes** : il dit *combien* et *par quelle porte*, pas *combien on aurait gagné*.

### Prochaine étape — chiffrée, avant tout GO

1. **Rejouer les 5 portes** (volume, mur, spread, plancher, fusible) sur les 3 jambes RIZE : le
   mode unitaire ne rejoue aujourd'hui **que la porte du repli**.
2. **Chiffrer paire par paire** l'extension du set-up « sans repli » (mesuré **+18,58 $/90 j** sur
   EDEL le 21/09 — seul `mode_entree = "IMPULSE"` du profil).
3. **Rappeler le plafond réel** : RIZE, 2 % d'un mur médian de 243,78 $ = **4,88 $ de mise** —
   même un pump de +81,8 % ne vaut que quelques dollars sur ce carnet. Le levier n°1 reste **la taille**, pas l'entrée.

## 8. CORRECTIONS — mes erreurs de la 1ʳᵉ passe (3 objections de Christophe, toutes fondées)

### 8.1 « Tu calcules sur un marché qui monte » — OUI, et ça faussait mon chiffre

Mesuré sur la même fenêtre : **BTC 76 535 $ → 85 943 $ = +12,3 %** · **20/20 paires en hausse** ·
**médiane +19,4 %** · moyenne équipondérée **+18,8 %** · **ZÉRO jambe de baisse ≥ 20 %**.
⇒ Dans un marché à +19 %, une « jambe ≥ 20 % » n'est **presque que le marché** : mon
« **193 % d'amplitude laissée** » était **gonflé par le bêta**, pas par un manque de talent.

**LE JUGE QUI MANQUAIT (ajouté) — « acheter et garder » :**

| | 5 jours |
|---|---|
| Marché (équipondéré des 20 paires) | **+18,8 %** |
| BTC | +12,3 % |
| **NOTRE MOTEUR** | **+36,32 $ / ≈150 $ = +24,2 %** |
| **Écart** | **nous BATTONS le marché de +5,4 points** |

**Et RIZE, sur la fenêtre : +0,8 %.** Son pump de +81,8 % a été **entièrement rendu** — c'est une
paire de **vas-et-vient**, pas une paire à détenir.

**Le tri qui compte (ajouté au scan) :** une jambe était-elle **entrable** (repli ≥ 5 % offert,
notre règle l'exige) ? → **1 seule inaccessible** (QNT, repli max 4,8 %) · **6 ENTRABLES et
non prises** ← **ce sont celles-là qui accusent le moteur.**

### 8.2 « Hulk a déjà pris des pumps sur RIZE ? » — **OUI, quatre fois et plus**

Dal journal réel : **8 BUY RIZE**, avec des ventes partielles à **+44,4 % (09/09)**,
**+53,4 % (10/09, m6 = +122,7 % !)**, **+34 % (16/09)**, **+34 % (18/09)**, **+27,5 % (26/08)**.
La raison de BUY écrit elle-même la preuve du mécanisme :
`impulse_pullback_dd6=42.8>=36.8 m6=122.7` (10/09) · `dd6=26.1>=23.9 m6=34.7` (16/09) ·
`dd6=10.1>=8.6 m6=18.9` (09/09).

⇒ **RIZE n'est PAS structurellement in-attaquable — je l'avais écrit à tort.** La règle prend
ses pumps **quand le repli atteint le seuil**. **Et RIZE est pourtant PERDANTE au total :
−1,12 $** (23 ventes) → **le problème n'est pas seulement l'entrée, c'est ce qu'on REND**
(ré-entrée au sommet, stop à −39 % le 22/09).

### 8.3 LA CONTRADICTION QUI RESTE — et c'est un TROU DE MESURE, pas un réglage

Mon calcul reconstitue `dd6` et conclut, sur les **3 jambes RIZE**, que le repli offert
dépassait le repli exigé :

| Jambe RIZE | Repli **exigé** (0,85 × max(4,2 ; 5 ; 0,30×m6)) | Repli **offert** (reconstruit) | Marge |
|---|---|---|---|
| +35,7 % (19:31→22:40) | 6,84 % | 10,53 % | **+3,69 pt** |
| +31,3 % (13:44→18:04) | 5,69 % | 17,45 % | **+11,76 pt** |
| +27,0 % (22:44→07:22) | 4,25 % | 7,97 % | **+3,72 pt** |

**Or le moteur a écrit `IMPULSE_WAIT` sur 96,2 % de ces cycles** → les deux se contredisent.
**Pourquoi je ne peux pas trancher : le moteur N'ÉCRIT PAS `dd6` quand il REFUSE.**
Il ne l'écrit que quand il **achète** (`impulse_pullback_dd6=…`). ⇒ **`ATTENTE:IMPULSE_WAIT`
est un refus MUET sur le chiffre qui décide.**

⇒ **Le geste juste n'est PAS de toucher un seuil : c'est de faire écrire au refus ce que l'achat
écrit déjà** — `dd6_observé`, `seuil_exigé`, `manque en points`. Additif, sans effet sur une seule
décision, réversible, et il rend la question « pourquoi on rate » **répondable pour toujours**.

### 8.4 « On avait déjà vu pour la taille » — OUI, et c'est ma faute

Le **21/09**, `chiffrage_compounding.py` avait déjà établi que **le plafond du mur est le
facteur qui mord** (16/97 achats collés au plafond, compounding inerte à −0,12 $). Mon nouvel
instrument n'a ajouté que le **montant exact** (+2,77 $/5 j) et **confirme** la conclusion du
21/09 **sans la dépasser** : j'ai **re-mesuré** au lieu d'avancer (classe E9 du registre).
Les `2,77 $` restent valables comme chiffre, **pas comme découverte**.

## 9. CORRECTION MAJEURE (23/09, 3ᵉ passe) — LE SEUIL RÉEL ÉTAIT 24 %, PAS 5 %

**§2, §7 et §8 de ce document sont à corriger.** Ils affirment que le repli exigé valait
`max(dip 4,2 % ; 5 % ; 0,30 × m6)` = **5,00 à 12,75 %**. **C'est faux** : la règle applique
**d'abord** `dip = max(dip_pct du profil ; DIP_CADENCE_MULT × cadence)` (`paper_diprip.score_pair`,
l.566 ; `config/defaults.env` : `DIP_CADENCE_MULT=0.50`).

- **La cadence de RIZE est écrite par le moteur lui-même** (colonne 9 du journal du run) :
  **43,6 – 53,9 %** (médiane **49,1 %**) pendant les faits.
- Donc `dip = max(4,2 ; 0,50 × 49,1) = 24,55 %` → porte de régime = **21,70 %**.
  ✔ Vérifié à la source par la ligne que le moteur écrit depuis le 23/09 :
  `ATTENTE:IMPULSE_WAIT dd6=2.50 seuil=21.70 manque=19.20pt m6=12.5` (face à `ZBCN/TEL seuil=4.25`).

**Conséquences, chiffrées** (contre-factuel rejoué avec le seuil réel, chemin dense) :

| Jambe RIZE | Repli **exigé** (réel) | Repli **offert** | Verdict |
|---|---|---|---|
| +35,7 % (22/09 19:31→22:40) | **24,5 %** | 10,2 % | **INACCESSIBLE** |
| +31,3 % (22/09 13:44→18:04) | **24,7 %** | 10,5 % | **INACCESSIBLE** |
| +27,0 % (22/09 22:44→07:22) | **24,5 %** | 9,7 % | **INACCESSIBLE** |

⇒ **Le tableau du §8 (« marge +3,69 / +11,76 / +3,72 pt ») était inversé par mon erreur** :
le repli **exigé** est ~2,4× plus haut que ce que j'avais calculé, il n'y a **aucune marge**,
et le moteur refusait **avec raison**. Le **contrôle de cohérence = 0 contradiction** et la
**fidélité de la reconstruction passe de 68,8 % à 95,8 %** : les deux mesures cessent de se
contredire — c'était mon instrument, pas le moteur.

**Le levier chiffré (porte du repli levée, plafond réel, chemin dense)** : RIZE ×3
**+0,82 / +1,20 / +1,11 $** (cap 4,88 $) · BIO **+4,35 $** · CHIP **−26,47 $** →
**TOTAL −18,99 $** ⇒ **NE PAS TOUCHER** (le détail complet et les limites :
`REFUS_PARLANT_ET_SEUIL_REEL_20260923.md`).

---
*Instrument : `hulk-mexc/scripts/chiffrage_pump_manque.py` (`--paire …` / `--scan`) · sorties : `hulk-mexc/runs/CHIFFRAGE_PUMP_MANQUE_RIZE_20260923.{txt,json}` + `CHIFFRAGE_PUMPS_MANQUES_SCAN_20260923.txt` · 0 ordre, 0 €, aucune écriture moteur.*
