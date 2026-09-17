# BRIEF EDEL — SIMULATION 3 MAINS (Buffy + Antigravity + Christophe juge) — 17/09 23:15Z

**Pour Antigravity/Gemini. Lis ce fichier + les 2 sources. Conteste avec des chiffres. Ne modifie AUCUN fichier — tu proposes, le propriétaire tranche.**

## Contexte en 6 lignes
EDEL a fait +156 % (11→16/09). Réalisé moteur : **+0,98 $**. Autopsie : `Index_Maison/PANORAMA_EDEL_SCANDALE_20260917.md` (§7 = version corrigée après confrontation à la fiche). La fiche EDEL (`hulk-mexc/strategie/universe_profils.json`) est **vindiquée** sur ses choix (IMPULSE, trail 10/4). Les coupables : **fusible 1,5×σ → stake 3,00 $** (miettes) + **stop-guard/dust_sweep liquidant dans les mèches** + **reentry au top**. Tout ça = couches ajoutées par Buffy après la fiche. Consigné E34/E34bis.

## L'inventaire des données (demande explicite de Christophe — vérifié à la source)
| Donnée | Où | Portée |
|---|---|---|
| Carnet de trades complet | `hulk-mexc/runs/PAPER_V1_20260915_064552.csv` (8 Mo) + 190 CSV depuis 22/07 | 2 mois — ATTENTION : chaque event écrit ×4, dédupliquer |
| Klines 1h/4h MEXC EDEL | `hulk-mexc/runs/EDELUSDT_1h_klines_20260917.json` + `_4h_` | **500 bougies max = 20 jours. La paire n'existe sur MEXC que depuis le 28/08.** |
| Profil/fiche EDEL | `hulk-mexc/strategie/universe_profils.json` | calibrée 30/08, trail 10/4 posé 10/09 |
| Microstructure (murs/spoof/spread) | `runs/CORPUS_ASP_20260917.csv` (2,1 Mo) + `murs_observations.json` | 16/08 → 17/09 |
| Contexte riche (régime, tension, murs live) | `runs/croisement_contexte.jsonl` (EDELUSDT) | **2 jours seulement (15→17/09) — et les MURS y sont GELÉS** (1 088 $ / 2 263 $ identiques 3 jours de suite, E35) |
| Murs EDEL réels — 2 fenêtres | `ASPIRATION_CALIB_*` (16→30/08, 1 686 mesures, mur médian ~908 $) + `CORPUS_ASP_20260917.csv` (17/09, 358 mesures, mur bid ~2 272 $) | **TROU 31/08→14/09 : aucune mesure de murs pendant la 1re jambe du pump** |
| L2 SNAPS (carnet d'ordres 1 s) | `runs/L2_*_SNAPS.csv` | **BTC UNIQUEMENT — EDEL jamais couverte par le L2 (trou structurel, E35)** |
| Volatilité mesurée | `Index_Maison/data/volatilite_paires.json` | 10/09, σ EDEL ≈ 10 %/j |

## Le backtest du 17/09 (`runs/EDEL_SETUP_BACKTEST_20260917.json`) — et ses limites
Stake 30 $ réel, frais 0,05 %/côté, entrée dip≥X % en tendance haussière (close>SMA24h), sortie rip/stop/trail :
- **Top : dip≥4 %, rip 6 %, stop 12 %, trail 10/4 → +31,18 $ net, 16 trades, WR 88 %** sur 20 jours
- **AVERTISSEMENT méthodologique (Buffy)** : la fenêtre contient le pump de +156 % → une grille dip-buy y gagne par construction ; n=16 ; UN SEUL régime de marché. **Ce chiffre n'est pas une preuve d'edge, c'est une hypothèse à tester en FORWARD (papier, 7 jours) avant d'y croire.**
- Convergence notable : le trail 10/4 de la fiche V4 est dans toutes les meilleures grilles.

## La spec proposée — EDEL SETUP V2 « récolte » (à valider ou contester)
1. **Stake fixe 30 $/position** (budget paire du design 28/08) — ABOLITION du fusible 3 $ pour EDEL ; le risque max = stop 12 % = −3,60 $/trade
2. Entrée : **dip ≥ 5 % depuis le max 48h ET close > SMA24h** (tendance) — plus strict que le backtest (dip 4) pour réduire le mirage de régime
3. Sorties : **rip 6 % (sortie 50 %) · trail arm 10 / gb 4 (la fiche) · stop 12 %** — JAMAIS de dust_sweep de position entière
4. **Cooldown 2 h après un stop** — interdiction du reentry dans la mèche (le crime du 15/09 02:40→05:57)
5. **Reentry_dump interdit au-delà de dd6 > 15 %** (le crime du 16/09 @ 0,02669)
6. **Forward test papier 7 jours AVANT tout verdict** — critères figés maintenant : net > 0 sur ≥ 5 trades, WR > 55 %, aucune sortie dans une mèche > 8 %/h

## Conséquence directe pour la spec (donnée neuve du 17/09 soir)
Les murs bid EDEL ont **×2,5 entre la calibration (908 $) et aujourd'hui (2 272 $)** — la liquidité réelle a suivi le pump. Le plafond « 2 % du mur » calé sur l'ancien mur = 18 $ est **obsolète** ; lu sur les murs actuels = ~45 $. La spec V2 doit lire le plafond **sur le flux de murs du jour** (CORPUS_ASP), jamais sur un cache figé — et le retour d'expérience du fusible 3 $ est cohérent : taille min 30 $, plafond live, stop 12 % = risque max −3,60 $.

## Les 3 questions à Antigravity (conteste, chiffre à l'appui)
1. Le backtest 20 jours/1 régime : quel test additionnel exigerait un quant rigoureux AVANT d'activer cette spec en papier ?
2. Le stop 12 % sur σ=10 %/j : trop large ou juste ? Simule l'alternative stop = 1,5×σ si tu la préfères — sur les MÊMES klines (fichier json fourni).
3. La règle « récolte 50 % au rip 6 % » : sur les klines, vérifie si sortir 50 % au rip améliore ou dégrade le net vs sortie full-trail seule.

## Règles (rappel)
Un chiffre = un fichier source · tu proposes, tu n'écris pas · le propriétaire juge · papier jusqu'à son GO explicite · 0 € réel.
