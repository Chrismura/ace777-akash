# TOUR 3 — LE GARDIEN A CRIÉ SUR MON PROPRE INSTRUMENT, ET LES CHIFFRES QUE JE VOUS AI SOUMIS ÉTAIENT FAUX

Ce tour est court, et il ne demande pas votre avis sur une méthode : **il vous annonce que la
boucle que vous avez validée au tour 1 reposait sur un seuil faux, de mon fait.** Je l'ai corrigé
contre moi-même, et je vous le donne avant que vous ne vous appuyiez dessus une seconde fois.

## 1. LA FAUTE (classe E20) — et ce n'est pas moi qui l'ai vue

En rejouant les gardiens de fin de tour, `hulk-mexc/scripts/verif_seuil_moteur.py` est passé
**au rouge tout seul** : *« 2 fichiers à corriger — `boucle_setups_main.py`, `mesures_jury_tour2.py` :
instruments qui recalculent un seuil d'entrée SANS le terme cadence »*.

**Il avait raison.** L'instrument qui a produit les chiffres du tour 1 (la boucle des set-ups)
jugeait chaque achat contre **le plancher du profil** (`calib.dip_pct`, ex. 4,0 %) et le tableau par
famille contre un **« 2 % » plat**. Or le seuil réel du moteur est :

```
dip  = max( plancher_du_profil ; DIP_CADENCE_MULT × cadence_de_la_paire )
seuil d'entrée = max( dip ; IMPULSE_PULLBACK_MIN_PCT ; IMPULSE_PULLBACK_FRAC × m6 )
```

**MESURÉ, terme par terme** (cadence lue dans le journal du moteur) :

| paire | plancher | cadence médiane | × 0,50 | seuil effectif | terme dominant |
|---|---|---|---|---|---|
| EDELUSDT | 5,50 % | 26,4 % | 13,20 % | **13,20 %** | cadence |
| RIZEUSDT | 4,20 % | 16,9 % | 8,44 % | **8,44 %** | cadence |
| CHIPUSDT | 4,00 % | 13,4 % | 6,69 % | **6,69 %** | cadence |
| QAITUSDT | 4,00 % | 11,2 % | 5,60 % | **5,60 %** | cadence |
| REDUSDT | 4,00 % | 10,0 % | 5,01 % | **5,01 %** | cadence |
| les 16 autres | 2,50–4,00 % | 2,6–9,4 % | 1,32–4,70 % | **5,00 %** | porte pullback |

## 2. CE QUE ÇA CHANGE DANS CE QUE JE VOUS AI SOUMIS

| chiffre publié (tour 1) | chiffre vrai, après correction |
|---|---|
| « **28 %** d'entrées conformes au motif » | **5 % (3/60)** |
| `remploi de cash` — 7/26 au-dessus de 2 % | **1/26** au-dessus du seuil effectif |
| `impulsion/pullback` — 7/14 | **1/14** (seuil médian **13,20 %**) |
| `re-entrée après dump` — 5/7 | **1/7** (seuil médian **8,44 %**) |
| `cooling` — 0/13 | **0/13 — inchangé** |

**Votre conclusion « la famille `cooling` entre sans baisse préalable » est donc CONFIRMÉE et plus
forte encore** : elle ne tient pas le seuil, et les familles qui annoncent une condition de baisse
non plus. Ce qui **change pour vous** : votre reproche « les défauts de conception » s'appuyait sur
un compteur **7 à 5 fois trop indulgent** — et c'est **contre moi** qu'il se retourne, pas contre
la machine.

**PORTÉE, déclarée avant que vous ne la releviez** : ma « chute » est mesurée sur les **bougies
1 min** (plus haut de la fenêtre → prix d'achat). Le moteur, lui, écrit **son propre `dd6`** dans
son motif (`impulse_pullback_dd6=5.1>=5.0`). Ce ne sont pas la même grandeur : les lignes
`impulsion/pullback` et `re-entrée` sont **indicatives, pas une preuve d'infraction**. La preuve
d'un franchissement, c'est le `dd6` écrit par le moteur — **je ne l'ai pas encore lu ligne à ligne,
et je ne le déclare pas fait.**

## 3. CE QUI A CHANGÉ, MÉCANIQUEMENT

- `hulk-mexc/scripts/verif_seuil_moteur.py` : **✔ CONFORME** — plus aucun instrument de la maison
  ne recalcule un seuil d'entrée sans la cadence.
- `boucle_setups_main.py` : la formule du moteur est reproduite **terme par terme**, et l'instrument
  publie désormais `dip_plancher_profil_pct` · `dip_terme_cadence_pct` · `dip_effectif_pct` ·
  `dip_requis_pct` · **`dip_terme_dominant`** (quel terme décide) — plus un seul chiffre nu.
- `mesures_jury_tour2.py` §8 : l'audit plancher-vs-effectif que DeepSeek exigeait est passé de
  « INFORMATION INSUFFISANTE » à **FAIT**, paire par paire.
- Registre : **E17 → E18 → E19 → E20**, quatre classes le même jour, toutes publiées.

## 4. CE QUE JE VOUS DEMANDE (une seule question)

**Votre verdict du tour 1 tient-il encore ?** Il a été rendu sur des chiffres que je viens de
corriger **contre moi-même**. Trois réponses possibles, et je les accepte toutes :

1. **il tient** — les défauts désignés (stop de niveau 39-44 %, latence de lecture, `cooling`) ne
   dépendent pas de ce compteur ;
2. **il doit être refait** — et je le referai avec les chiffres corrigés avant d'aller plus loin ;
3. **il ne tient plus** — et je le retirerai publiquement, comme j'ai retiré le « stop 8 % ».

Et une seconde, si vous la jugez utile : **quatre classes d'erreurs en une journée (E17, E18, E19,
E20) dont trois trouvées par mes propres gardiens** — est-ce un progrès du contrôle, ou la preuve
que je travaille trop vite sur des chiffres que je ne vérifie pas ? Répondez sec, je préfère.

Terminez par vos 3 sections habituelles (VERDICT / CE QUE J'EXIGE AVANT LE PROCHAIN TOUR / CE QUI
ME FERAIT CHANGER D'AVIS). Rappel : une voix substituée ne compte pas comme indépendante — vous
n'étiez que **2 voix indépendantes** au tour 2 (DeepSeek servi par Gemini), et le gardien l'a dit.
