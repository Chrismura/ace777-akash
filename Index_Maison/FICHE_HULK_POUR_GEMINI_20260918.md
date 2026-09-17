# FICHE HULK — CE QU'IL FAIT ET COMMENT (pour Antigravity/Gemini — 18/09, rédigé par Buffy d'après le code réel)

**À lire avant toute proposition sur Hulk.** Tout est vérifiable dans les fichiers cités en §6. Tu contestes avec des chiffres, tu n'écris pas. Le propriétaire juge.

---

## 1. LA PHILOSOPHIE — le texte canonique (dicté par le propriétaire le 16/08 — source : `hulk-mexc/README.md`)

- Les small caps ne sont **pas des paires à scalper** : ce sont des **projets étudiés un par un**. On y croit. **Le bag (la quantité de tokens détenue) EST le but.**
- **Pas d'argent frais** : la seule façon de faire grandir le portefeuille est de **trader les tokens eux-mêmes** — vendre les rebonds, racheter les creux, redéployer le cash récolté pour accumuler PLUS de tokens.
- **« Une pierre trois coups »** : 1) acheter les creux (dip) · 2) vendre les gains (rip **scale-out 2 paliers**, 25 % chaque palier : small caps = +6 % puis +8 %, XRP/HBAR liquides = +2 % puis +6 %) · 3) laisser un **runner** (la moitié continue courir ; à 2× elle devient bag maison).
- **Le benchmark, c'est « Hulk vs wallet statique »** (si on n'avait rien touché) — pas un indice, pas un autre trader. Objectif : plus-values ET limiter la casse.

## 2. CE QU'IL FAIT, CONCRÈTEMENT (source : `hulk-mexc/scripts/paper_diprip.py`, 2 813 lignes)

Un moteur **papier** (aucune clé API, aucun ordre réel) qui tourne en continu sur 17-20 paires MEXC :

1. **Il mesure chaque paire en continu** (module `ace_sense_mexc`) : tension du carnet, murs bid/ask, spoof (faux murs), vitesse des effondrements de murs (« drops »), spread.
2. **Il juge l'entrée** (`entry_gate` + `veille_gates`) : volume, spread max, fenêtre interdite, veille rouge (skip si contexte dangereux).
3. **Il achète les creux** : chaque paire a SON seuil dip/rip/stop dans sa **fiche** (voir §4).
4. **Il vend selon la philosophie** : rip scale-out 25 %/25 %, trailing « filet » (armé au pic, vend si le prix redescend du giveback), stop si la baisse dépasse le stop de la fiche.
5. **Il gère son cash par paire** : chaque paire garde son propre cash pour se racheter elle-même (design « mini-comptes indépendants »).
6. **Sécurités** : circuit breaker (`circuit_breaker.py`), cooldown anti-re-entry après stop, fusibles par paire (budget de perte journalier calé sur la volatilité mesurée de CHAQUE actif — la plus folle bouge 7,8× la plus sage).

## 3. LE CAS EDEL — ce qui s'est passé VRAIMENT (leçon centrale)

- EDEL a fait **+156 %**. Hulk **a vu et a acheté 9 fois pendant la montée** (fiche IMPULSE appliquée correctement).
- MAIS le **fusible du 10/09** (que Buffy a posé) limitait EDEL à **3,00 $ par achat** (1,5× sa volatilité). Direction juste, taille de miettes → **+0,98 $ réalisé sur +156 % de mouvement**.
- ET le duo stop-guard/dust_sweep **a liquidé des positions entières au fond des chutes** puis le blocage `REENTRY_MAX` a empêché le rachat pendant le rebond.
- **Verdict autopsie (E34/E34bis)** : le cerveau de Hulk était bon, ses réglages de sécurité (posés après la fiche) ont étranglé la taille et vendu au pire. Le backtest à taille réelle (30 $) sur les mêmes signaux donne **+31,18 $** (à valider en forward 7 jours — la fenêtre contient le pump, donc hypothèse, pas preuve).

## 4. LES FICHES IA ET LES SETUPS — où ils vivent

| Document | Fichier | Contenu |
|---|---|---|
| **Fiche vivante de chaque paire** | `hulk-mexc/strategie/universe_profils.json` | 17 profils : archétype (ex. EDEL = `illiquide_calme`), murs médians, spread, spoof, drops, fenêtres horaires, ET la calib **dip/rip/stop/mode_entree/trail arm-giveback** de chaque paire. Exemple EDEL : `mode_entree: IMPULSE, dip 5.5, rip 5.2, stop 10.3, trail 10/4`. |
| **Audit des 20 actifs (06/09)** | `Index_Maison/AUDIT_SETUPS_20_ACTIFS_20260906.md` | Volatilité jour>nuit de chaque actif, verdict par actif (EDEL : « DEEPDIVE (loterie) », vol 35→37 %). |
| **Volatilité mesurée** | `Index_Maison/data/volatilite_paires.json` | σ/jour par paire — sert aux fusibles. |
| **La philosophie canonique** | `hulk-mexc/README.md` | Le texte dicté par le propriétaire — la référence absolue. |
| **Autopsie EDEL complète** | `Index_Maison/PANORAMA_EDEL_SCANDALE_20260917.md` | Les 4 mécanismes du désastre + §7 corrections. |
| **Brief backtest + spec V2** | `Index_Maison/BRIEF_ANTIGRAVITY_EDEL_20260917.md` | Inventaire des données, backtest 30 $, 3 questions ouvertes. |
| **Journal des erreurs** | `engle/JOURNAL_ERREURS.md` | E22→E35 : toutes les fautes des IA, noir sur blanc. |

## 5. CE QUE LE PROPRIÉTAIRE ATTEND DE TOI (Gemini)

1. **Comprends le style** : accumulation patiente sur des projets crus, pas du scalping frénétique. Le benchmark = battre le wallet statique.
2. **Vérifie** : ouvre les fichiers du §4, refais les calculs (klines EDEL : `hulk-mexc/runs/EDELUSDT_1h_klines_20260917.json`).
3. **Conteste la spec V2 EDEL** (brief, 3 questions) : elle est soumise, pas activée.
4. **Tu proposes, tu n'écris pas.** Le propriétaire tranche, Buffy exécute avec spec figée avant test.

## 6. RÈGLES DE LA MAISON (rappel)

Un chiffre = un fichier source · verdict figé AVANT le test · « une variante = un nouveau GO » du propriétaire · papier jusqu'à GO explicite · 0 € réel depuis le début.
