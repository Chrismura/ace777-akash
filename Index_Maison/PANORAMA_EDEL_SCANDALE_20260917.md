# PANORAMA EDEL — L'AUTOPSIE DU SCANDALE (17/09/2026, rédigé par Buffy)

**Pour : Antigravity/Gemini — lis ce fichier AVANT de proposer quoi que ce soit sur Hulk/EDEL.**
Tout chiffre ci-dessous est sourcé (fichier + commande de vérification). Règle maison : un chiffre = un fichier source.

---

## 1. Les faits bruts (vérifiés à la source ce soir)

| Mesure | Valeur | Source |
|---|---|---|
| Amplitude EDEL 11→16 sept | 0,0105 → 0,0268 = **+156 %** (« les 160 % ») | croisement_contexte.jsonl, suivi_setup_edel |
| PnL RÉALISÉ EDEL (campagne complète) | **+0,98 $** (pic +1,60 $ le 15/09 18:55) | runs/PAPER_V1_*.csv dédupliqué |
| PnL réalisé TOTAL moteur (tous pairs) | **+5,10 $** | PAPER_V1_20260915_064552_state.json `.pnl_total` |
| Positions encore ouvertes | **16** — capital engagé jamais refermé : **250,42 $** | idem `.positions` (16 clés) |
| EDEL maintenant | prix 0,02113 · position ouverte entrée 0,02029, stake 2,36 $ | croisement_contexte.jsonl 21:28Z + state |
| Part de la montée convertie en cash | **0,6 %** (+0,98 $ sur ~160 $ de mouvement pour 100 $ engagés) | calcul |

**Le « +45 % » a existé quelque part (latence d'equity, « +44 % latent » noté sur RIZE en mémoire 14/09) — mais il n'a JAMAIS été consolidé en réalisé. Le chiffre officiel du moteur reste +5,10 $ sur deux mois.**

## 2. Pourquoi — les 4 mécanismes du désastre (aucun n'est une théorie, tous sont dans le carnet)

**M1 — LE MOTEUR EMPILE SANS JAMAIS RÉCOLTER.** *(précisé le 17/09 tard, voir §7)*
29 BUY uniques EDEL contre 14 sorties. ⚠️ CORRECTION : la reconstruction FIFO « 15 positions fantômes » était un **artefact** — le state officiel (`PAPER_V1_20260915_064552_state.json`) consolide **1 position par paire** (les BUY successifs sont des DCA sur le même bag, les SELL réduisent la qty). Le capital engagé réel reste vrai : **16 bags ouverts, ~250 $ de notional engagé**. Ce qui demeure : les BUY (impulse_pullback, reentry_dump) achètent à chaque accroc pendant que les sorties ne touchent que des miettes.

**M2 — LES SORTIES NE VENDENT QUE DES POUSSIÈRES.**
La preuve la plus violente du carnet : BUY 16/08 @ 0,00756 → SELL 15/09 @ 0,02046 = **+170 % de mouvement capturé pour… +0,51 $ de PnL**. Le moteur a laissé courir la montée sur une quantité résiduelle (déchets de précédents « SELL_PARTIAL 50 % » et dust sweeps) : le gain en pourcentage est réel, le gain en dollars est nul.

**M3 — LA MOITIÉ RESTANTE EST VENDUE AU PIRE, SUR LE SOMMET.**
15/09 02:39 : sortie « stop −13,8 % » à 0,01631 (le creux de la mèche de panique). 17/09 18:54 : « stop −11,95 % » à 0,02042 (pendant le dump). Le garde-fou vend DANS la panique, au plus bas de la mèche — mécaniquement le pire prix de la journée. Et 16 minutes après chaque vente de panique, le moteur RACHÈTE (reentry 18:09, 18:55) au même prix — payant le spread de 80 bps d'EDEL pour rien.

**M4 — L'OBSERVATEUR A INVERSÉ LE SENS DE L'HISTOIRE.** *(corrigé le 17/09 tard, voir §7)*
Pendant TOUTE la montée de +156 %, l'observateur `SUIVI_SETUP_EDELUSDT.jsonl` classait EDEL `POMPE_PIEGE` (stabilité 9→33), `LEADER` seulement après le sommet. ⚠️ CORRECTION importante : **le moteur de trading lui-même a ENTRÉ 9 fois EDEL pendant la ruée** (la fiche `universe_profils.json` impose `mode_entree: IMPULSE`, et le moteur l'a appliqué : BUY 13/09 09:57 · 15/09 02:23, 05:57, 14:56, 18:41 · 16/09 06:57 · 17/09 18:09, 18:55…). Le refus d'accompagner n'était PAS le moteur — c'était l'étiquette de l'observateur. Le vrai crime du moteur pendant la montée : entrer avec des miettes (3 $ max, cf. §7) et se faire stopper dans les mèches.

## 3. Les défauts de mesure découverts pendant l'autopsie (à corriger, GO requis)

1. **Le carnet écrit chaque événement en ×4** (déduplication nécessaire pour tout calcul). Toute statistique lue brute est gonflée ×4.
2. **`DIGEST_WATCHDOG_STDOUT.log` = 14 GO** sur ton disque (log jamais tronqué). À purger/archiver — commande proposée, pas exécutée sans ton GO : `truncate -s 0 ~/ace777-test-day1/hulk-mexc/runs/DIGEST_WATCHDOG_STDOUT.log` (ou déplacement en archive compressée).
3. **Aucune ligne d'equity consolidée** dans le state : impossible de répondre à « combien je vaut » sans refaire le calcul à la main. C'est comme ça que le « +45 % » a pu cohabiter avec un réalisé de +5,10 $ sans que personne ne crie.

## 4. Ce que je soumets au GO du propriétaire (rien n'est appliqué)

| # | Correctif proposé | Contre quoi il agit | Risque |
|---|---|---|---|
| C1 | **Récolte par paliers avec notional minimum** : aucune sortie d'une position tant que la quantité vendable > X $ ; les paliers vendent des tailles réelles, plus des poussières | M2 | faible |
| C2 | **Stop « après sommet »** : le stop ne s'arme que sur retracement depuis le plus haut, avec giveback mesuré en σ de la paire (convention maison déjà en vigueur sur les 8 fiches), et JAMAIS d'exécution dans la mèche (attente d'une bougie de stabilisation) | M3 | moyen — peut sortir plus tard |
| C3 | **Plafond d'empilement** : reentry interdit si position déjà ouverte sur la paire au-delà de N tranches ; les 15 positions fantômes sont d'abord REFERMÉES (inventaire, puis plan de sortie) | M1 | faible |
| C4 | **Equity consolidée écrite dans le state à chaque cycle** (réalisé + non-réalisé, prix de source) — le cockpit affiche la vérité | §3.3 | nul |
| C5 | Purge du log 14 GO + rotation des logs (taille max) | §3.2 | nul |

**Priorité suggérée par le résultat** : C4 (voir la vérité) → C3 (dégeler les 250 $) → C1 (récolter vraiment) → C2 (ne plus vendre au pire) → C5.

## 5. La question pour Antigravity (débats attendus, tu as le droit de contester — avec des sources)

1. Le classement `POMPE_PIEGE` pendant une tendance vraie : le seuil de « stabilité » 9→33 est-il mesuré sur une fenêtre trop courte pour distinguer une pompe d'une impulsion de fond ?
2. Le reentry 16 minutes après un stop de panique : qui a spécifié ce rachat ? Est-il cohérent avec le stop qui vient de vendre ?
3. 16 positions ouvertes sur 20 paires actives : le moteur a-t-il jamais eu une logique de récolte, ou seulement d'accumulation ?

## 7. CORRECTIONS DU SOIR — LA FICHE EDEL CONFRONTÉE AU CARNET (Christophe a exigé d'aller à la source)

**La fiche existe et a été lue** : `hulk-mexc/strategie/universe_profils.json` → `EDELUSDT` (calibrée 30/08, complétée 06/09, trail posé 10/09) :
`archetype: illiquide_calme` · `mode_entree: IMPULSE` (« EDEL ne bouge que par rafales IMPULSE, m6 70 % vs 4 % ») · `dip 5.5 / rip 5.2 / stop 10.3` · `trail arm 10.0 / giveback 4.0` (V4 du 10/09) · `mise_max_pct_mur: 2 %` (mur médian 908 $ → ~18 $ max) · `spread_cout: 53.9 bps`. L'audit des 20 actifs (06/09) la notait : vol **35→37 %**, verdict **« DEEPDIVE (loterie) »**.

**Verdict de la confrontation : la fiche NE démonte PAS l'œuvre du mois — elle est en partie VINDIQUÉE par le carnet :**
1. ✅ **Son diagnostic d'entrée était JUSTE** : EDEL bouge par rafales IMPULSE → le moteur a bien entré 9 fois pendant la ruée (+156 %). Le mode IMPULSE a fonctionné.
2. ✅ **Son trailing a travaillé** : `trailing_peak23.5pct_giveback4` le 13/09 = armé à 23,5 %, sorti 4 pts sous le pic — exactement la spec posée le 10/09.
3. ❌ **Ce qui a tué le PnL n'est PAS dans la fiche — ce sont les couches ajoutées après :**
   - **Le fusible du 10/09** (budget/paire = 1,5×σ) a plafonné EDEL à **3,00 $** (position constatée : 2,36 $). Même un trade PARFAIT ne pouvait rapporter que ~0,30 $. Le moteur avait raison sur la direction, il jouait aux miettes.
   - **Le duo stop-guard + dust_sweep** a liquidé des positions ENTIÈRES dans le creux des mèches : 15/09 02:39 `stop-13.8%_guard_partial_50` puis 02:40 `dust_sweep` = sortie TOTALE à 0,01626–0,01631 (le plus bas de la mèche)… et `REENTRY_MAX:1` a **bloqué tout rachat de 02:40 à 05:57** pendant que le prix remontait de 0,0159 à 0,019. Vendu au pire, raté le rebond, mécaniquement.
   - **`reentry_dump` achète les chutes APRÈS le sommet** : BUY 16/09 06:57 à 0,02669 (le top absolu), puis deux stops dans le dump du 17/09 avec re-entrée immédiate à chaque fois (18:08→18:09, 18:55:19→18:55:40) — le churn payé en spread 80 bps.
   - **Les « énormes » % étaient des miettes** : +170 % / +208 % / +217 % de mouvement capturé sur des bags résiduels de centimes → +0,51 $, +0,31 $, +0,26 $. Le seul vrai gain de récolte : `stake_out_2x` le 05/09, **+5,27 $** — la preuve que le moteur SAIT récolter quand la taille est réelle.

**Le « +45 % » demeure introuvable dans les registres** (réalisé EDEL : +0,98 $, pic +1,60 $ ; total moteur : +5,10 $). Ancres les plus proches : « +44 % latent » sur RIZE (mémoire 14/09, plancher shadow) et le pic trail EDEL 23,5 % du 13/09. Si Christophe retrouve où il a vu ce chiffre (cockpit, capture, fiche), on l'archeologie — aucun chiffre ne se conteste sans source.

## 6. État et garde-fous

- Hulk tourne en **PAPER** (décision Christophe du 30/08) — aucun ordre réel, 0 € du début à la fin.
- Ce fichier est **une analyse** — aucun paramètre moteur modifié. Toute modification = spec figée avant test + GO explicite du propriétaire (règle non négociable n°5).
- Sources primaires : `hulk-mexc/runs/PAPER_V1_*.csv` · `hulk-mexc/runs/PAPER_V1_20260915_064552_state.json` · `hulk-mexc/runs/croisement_contexte.jsonl` · `hulk-mexc/runs/CYCLE_EDEL_20260917_1754.md` · `hulk-mexc/strategie/universe_profils.json` (la fiche EDEL) · `Index_Maison/AUDIT_SETUPS_20_ACTIFS_20260906.md` (verdict « loterie ») · `Index_Maison/MEMOIRE_COLLAB.md` (14/09 : « +44 % latent » RIZE ; 15/09 : audit 472 refus pendant +60,9 % EDEL ; 10/09 : fusible 1,5×σ → EDEL 3,00 $).
