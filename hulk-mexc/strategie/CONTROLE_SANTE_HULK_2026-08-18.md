# Contrôle santé Hulk — 18/08/2026

> Vérifié par Buffy à la demande de Christophe (question : « Hulk est basé sur ACE, est-il sûr de ne pas avoir le parasite ? »).
> Rien n'a été modifié. Lecture seule.

## Verdict : Hulk est SAIN — aucun parasite

### 1. Dans le code
- `fluid_exit` / `FLUID_EXIT` : **0 occurrence** dans les scripts Hulk (contrairement à ACE qui avait `fluid_exit_inversion`).
- La logique de sortie de Hulk (`manage_open`, paper_diprip.py:1206) est **structurellement différente** :
  - **Stop en %** (`stop-6%_avant_2x`) — pas de vitesse
  - **RIP scale-out 2 paliers** (25 % × 2, runner garde 50 %) — « une pierre trois coups »
  - **2× → stake-out** (objectif double)
- Hulk sort sur des **pourcentages de gain/perte**, jamais sur une **vitesse de chute** → le parasite d'ACE (coupe au bruit dès que le prix bouge vite) n'a pas d'équivalent possible.

### 2. Dans les logs (preuve vivante, depuis 16/08)
| Sortie | Paire | Résultat |
|---|---|---|
| rip_9.8 + rip_9.2 (2 paliers) | RIZE | +0,47 $ |
| rip_6.1 + rip_8.9 (2 paliers) | CHIP | +0,37 $ |
| rip_2.0 (1 palier) | HBAR | +0,05 $ |
| rip_18.4 + rip_17.9 (2 paliers) | RED | +0,91 $ |
| stop-6.0% (1 stop) | CHIP | −0,31 $ + cooldown propre |

- **7 sorties, aucune « vitesse »** : que des rip (gains) et un stop en % (perte maîtrisée).
- **PnL total paper : +1,49 $** — le runner fonctionne (rip jusqu'à +18 % sur RED).

### 3. Point commun avec ACE (et c'est voulu)
- La **sonde d'aspiration** (double lecture du carnet, murs bid/ask) est **en mode OBSERVATION pure** : elle log + calibre (CSV `ASPIRATION_CALIB_*`), **zéro effet sur les entrées/sorties**. Exactement comme le fix fluid chez ACE : on observe avant d'agir.

## Fichiers de preuve
- `hulk-mexc/scripts/paper_diprip.py` (manage_open, ligne 1206)
- `hulk-mexc/runs/PAPER_V1_20260816_214411.csv`
- `hulk-mexc/runs/ASPIRATION_CALIB_20260816_214411.csv` (9 380 mesures, corrélation BTC incluse)

> Hulk est ton investisseur patient (bag, runner, cash) — pas un scalpeur. Sa logique de sortie est saine par construction.
