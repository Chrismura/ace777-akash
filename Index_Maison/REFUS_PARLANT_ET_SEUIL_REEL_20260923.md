# REFUS PARLANT + LE SEUIL RÉEL — RIZE, 23/09/2026

> Demande Christophe : **« go 1,2,3 »** — (1) rendre le refus parlant, (2) rejouer les portes de
> l'épisode RIZE, (3) chiffrer et décider.
> **Résultat en une ligne : le moteur n'a pas raté RIZE — il lui était INTERDIT d'entrer, et
> il le refusait avec raison. Le mur n'est pas le repli de 5 % : c'est `0,50 × la cadence de
> la paire`, soit 24,55 % de repli exigé sur RIZE. Et le levier qui lève ce mur COÛTE
> −18,99 $ au plafond réel sur les 7 jambes ratées : NE PAS TOUCHER.**

Instrument : `hulk-mexc/scripts/chiffrage_pump_manque.py` (lecture seule) · **0 ordre, 0 €**.

---

## 1. GO 1 — LE REFUS PARLE (et il a parlé en 2 minutes)

**Ce qui a changé dans le moteur : 1 ligne.** `ATTENTE:<régime>` → `ATTENTE:<régime> dd6=…
seuil=… manque=…pt m6=…` (+30 lignes de commentaire). Le préfixe `ATTENTE:<régime>` reste
**intact** (les instruments existants lisent `reason.split(":")[0]`) · **aucun seuil, aucune
porte, aucune décision, aucun ordre** touché · réversible en 1 ligne · `git diff` = 30
insertions / 1 remplacement, **vérifié ligne à ligne**.

**Preuve live** (2 min après la relance, journal du run) :

```
2026-09-23T09:01:58Z  RIZEUSDT  SKIP  IMPULSE_WAIT  …  ATTENTE:IMPULSE_WAIT dd6=2.50 seuil=21.70 manque=19.20pt m6=12.5
2026-09-23T09:01:58Z  ZBCNUSDT  SKIP  IMPULSE_WAIT  …  ATTENTE:IMPULSE_WAIT dd6=3.63 seuil=4.25  manque=0.62pt  m6=5.5
2026-09-23T09:01:58Z  TELUSDT   SKIP  IMPULSE_WAIT  …  ATTENTE:IMPULSE_WAIT dd6=2.65 seuil=4.25  manque=1.60pt  m6=5.7
```

**Ce que ça a immédiatement révélé** : un seuil de **21,70 %** pour RIZE pendant que les
autres paires sont à **4,25 %**. Arithmétique vérifiée à la source (`paper_diprip.score_pair`,
l.566 + `config/defaults.env`) :

```
dip  = max(dip_pct du profil ; DIP_CADENCE_MULT × cadence) = max(4,2 ; 0,50 × 51,06) = 25,53 %
need = max(dip ; IMPULSE_PULLBACK_MIN_PCT ; IMPULSE_PULLBACK_FRAC × m6)
     = max(25,53 ; 5 ; 0,30 × 12,5) = 25,53 %      →  porte de régime = 0,85 × 25,53 = 21,70 %  ✔
```

**D'où mon erreur, nommée** : mes documents précédents affirmaient « le repli exigé est
`max(dip 4,2 % ; 5 % ; 0,30 × m6)` = **5 à 12,75 %** ». **FAUX** : il manquait le terme
**dominant**, `0,50 × cadence` — la cadence de RIZE, écrite par le moteur lui-même dans son
journal (colonne 9), vaut **43,6–53,9 %** (médiane **49,1 %**). Mon instrument lisait
`profil.dip_pct` (4,2 %) et ignorait la cadence. **Le mur réel était 4× plus haut que ce que
je t'ai annoncé.**

---

## 2. GO 2 — LES PORTES DE L'ÉPISODE, AVEC LE SEUIL RÉEL

Le mouvement (journal du moteur) : bas **22/09 13:44:54Z 0,001750** → haut
**23/09 07:22:20Z 0,003182** = **+81,8 %** · 4 913 cycles de décisions après la mise à plat
(22/09 02:15:45Z) · régimes écrits : **IMPULSE_WAIT 4 690 (96,2 %)** / IMPULSE 183 (3,8 %,
tous au fond, 02:15→03:30).

| grandeur | valeur (écrite ou reconstruite) | source |
|---|---|---|
| Cadence de RIZE pendant les faits | **43,6 – 53,9 %** (médiane 49,1) | **moteur** (colonne 9) |
| Repli **exigé** (`0,85 × need`) | **21,82 – 26,93 %** | règle (`dip = 0,50 × cadence`) |
| Repli **offert** par le prix (max) | **17,45 %** | reconstruit (sommet 6 h) |
| **Manque** | **7,16 à 26,93 points** | — |

**Contrôle de cohérence (le test qui tranche)** : cycles restés `IMPULSE_WAIT` alors que le
repli reconstruit ≥ le seuil exigé → **0**. Et la fidélité du régime recalculé passe de
**68,8 % → 95,8 %** par la seule correction du seuil. **Les deux mesures cessent de se
contredire : elles disent la même chose, et c'est le moteur qui avait raison.**

**Les autres portes** (journal du run) : les 183 cycles `IMPULSE` (seule porte ouverte) sont
**au fond** et refusés par le **volume sec** (`vol_dry_vx=1,08–1,19<1,20`, `vol_DRY_impulse_block`
×24, +9 `MUR-CASSE`). Après ce refus, le prix a **encore baissé de −13,8 %** : la garde a
**évité une perte**, elle n'a pas raté un gain.

**Scan 5 jours (20 paires, chemin dense, seuil RÉEL par paire)** — 18 jambes ≥ 20 % dont
**4 rapides** (≤ 12 h) :

- **4 jambes INACCESSIBLES par construction** (repli offert < repli exigé) : **RIZE ×3** (cadence
  47,7–49,4 % → besoin 23,9–24,7 % ; offert 16,8 / 10,5 / 9,7 %) + **QNT** (besoin 5,0 ; offert 4,8).
- **3 jambes ENTRABLES et non prises** : FLUID, CHIP (VOL 55), BIO (ATTENTE 24).

Contexte de marché (objection « tu calcules sur un marché qui monte ») : BTC **+12,3 %**,
**20/20 paires en hausse**, jambes de HAUSSE 18 / de BAISSE 0. Le moteur fait **+36,32 $**
(5,85 → 42,17 $, colonne `pnl_total`, aucune reconstruction) ≈ **+24,2 %** sur sa base de 150 $.

---

## 3. GO 3 — LE LEVIER CHIFFRÉ AU PLAFOND RÉEL, ET LE VERDICT

Méthode : chemin **dense** (log + archives), sortie = **la sortie réelle de la paire** (profil),
entrée **comptée au plafond réel** (`2 % du mur bid médian`), E0 = règle actuelle,
E2 = porte du repli levée. Les 4 autres portes (volume/mur/spread/plancher/fusible) **ne sont
pas rejouées** → E2 est une **borne haute**, pas une promesse.

| jambe ratée | E0 (actuel) | E2 (repli levé) | écart | plafond |
|---|---|---|---|---|
| RIZE 22/09 13:44 → 18:04 | +0,00 $ | **+0,82 $** | +0,82 $ | 4,88 $ |
| RIZE 22/09 19:31 → 22:40 | +0,00 $ | **+1,20 $** | +1,20 $ | 4,88 $ |
| RIZE 22/09 22:44 → 23/09 07:22 | +0,00 $ | **+1,11 $** | +1,11 $ | 4,88 $ |
| BIO 18/09 → 23/09 | +0,00 $ | **+4,35 $** | +4,35 $ | 70,49 $ |
| CHIP 18/09 → 19/09 | +79,50 $ | +53,03 $ | **−26,47 $** | 661,99 $ |
| **TOTAL** | | | **−18,99 $** | |

Et sur l'épisode RIZE lui-même (séquence complète, ré-entrées + cooldown réels) :
**E0 = −0,41 $ · E2 = +2,11 $** au plafond de **4,88 $**.

**VERDICT : NE PAS TOUCHER.** Trois raisons, chiffrées :

1. **Les refus du moteur sont arithmétiquement justes** (0 contradiction, fidélité 95,8 %).
   Il n'y a **pas** de bug d'entrée sur RIZE à réparer.
2. **Le levier est négatif au total** : **−18,99 $** au plafond réel sur les 7 jambes ratées
   (+3,13 $ sur RIZE, mais **−26,47 $ sur CHIP** : entrer sans le repli fait acheter plus tôt,
   plus haut, et se faire stopper plus souvent).
3. **Le levier positif sur RIZE vaut +3,13 $ / 5 j** — soit **≈ 0,09 %** du PnL de la fenêtre
   (36,32 $) — sur un plafond de mise de **4,88 $**. **On ne modifie pas un moteur en
   production pour 3 $, et surtout pas sans avoir mesuré ce que l'autre porte (volume) en
   pense** (R17/R18).

**Ce qui reste vrai, et que je répète sans l'embellir** : RIZE est **la seule perdante** de la
fenêtre (−1,04 $, 23 ventes) alors que ses jambes montent jusqu'à +37 % — **c'est la SORTIE et
le va-et-vient qui coûtent là, pas l'entrée**, et la **taille** (mur médian 243,78 $ → 4,88 $ de
mise) plafonne tout. Ce sont les deux seuls chantiers qui restent, et ils sont déjà chiffrés
(plafond ≈ +2,77 $/5 j, borne haute ; sortie : à n ≥ 20).

---

## 4. LIMITES DÉCLARÉES (E8)

- **dd6 exact non journalisé** : il est reconstruit (sommet 6 h sur le chemin dense) — mais la
  décision du moteur (le régime) est écrite, et la fidélité recalculée est affichée (**95,8 %**).
- **Une seule porte rejouée** (le repli) : volume/mur/spread/plancher/fusible ne le sont pas.
  E2 est une **borne haute** ; sur CHIP, la porte qui a refusé en vrai est le **volume** (55 refus).
- **Le journal du run est cumulatif** : lire un fichier figé datait mal les « jambes ratées »
  (corrigé le 23/09 — l'instrument lit désormais **le plus récent**, la vérité la plus complète).
- **Jambe ≥ 20 % / réaction 10 %** : seuils d'**AFFICHAGE** déclarés, pas des décisions.
- **5 jours, 1 marché haussier (+12,3 % BTC), 18 jambes** → **aucun verdict statistique**.

## 5. ÉTAT (vérifié à l'instant)

| | |
|---|---|
| Moteur | **pid 97897 vivant** (relancé 09:01:25Z par la procédure maison/launchd, journal cumulatif) |
| État | **pnl 42,1679 $ · 9 positions · 175 trades** — identiques avant/après le patch |
| Patch moteur | **1 ligne** (`ATTENTE:{regime}` → `+_detail`), `git diff` = 30 insertions / 1 remplacement, logique de décision **intacte** |
| Veilleuse | **STABLE (exit 0)** |
| Tracebacks | **aucun** dans le journal du watchdog |
| Instruments | `hulk-mexc/scripts/chiffrage_pump_manque.py` (corrigé : seuil réel + journal cumulatif + chiffrage des jambes ratées) |
| Sorties | `hulk-mexc/runs/CHIFFRAGE_PUMPS_MANQUES_SCAN_20260923.txt` (à régénérer) |

**À retenir pour ne pas refaire l'erreur** : *un seuil qui n'est pas lu dans l'unité de la
paire n'est pas un seuil, c'est une hypothèse.* Le repli exigé n'est **pas** « 5 % » — il est
**proportionnel à la cadence de la paire** ; pour RIZE c'est **~24 %**, et c'est **écrit par le
moteur** depuis toujours (colonne 9) — il suffisait de le lire.
