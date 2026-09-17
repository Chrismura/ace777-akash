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

**M1 — LE MOTEUR EMPILE SANS JAMAIS RÉCOLTER.**
29 BUY uniques EDEL contre 14 sorties. 15 positions empilées n'ont jamais été refermées (du 16/08 au 17/09). Le carnet note des « reentry_dump » et « impulse_pullback » qui ACHÈTENT à chaque accroc de prix pendant que les sorties, elles, ne touchent jamais la taille réelle.

**M2 — LES SORTIES NE VENDENT QUE DES POUSSIÈRES.**
La preuve la plus violente du carnet : BUY 16/08 @ 0,00756 → SELL 15/09 @ 0,02046 = **+170 % de mouvement capturé pour… +0,51 $ de PnL**. Le moteur a laissé courir la montée sur une quantité résiduelle (déchets de précédents « SELL_PARTIAL 50 % » et dust sweeps) : le gain en pourcentage est réel, le gain en dollars est nul.

**M3 — LA MOITIÉ RESTANTE EST VENDUE AU PIRE, SUR LE SOMMET.**
15/09 02:39 : sortie « stop −13,8 % » à 0,01631 (le creux de la mèche de panique). 17/09 18:54 : « stop −11,95 % » à 0,02042 (pendant le dump). Le garde-fou vend DANS la panique, au plus bas de la mèche — mécaniquement le pire prix de la journée. Et 16 minutes après chaque vente de panique, le moteur RACHÈTE (reentry 18:09, 18:55) au même prix — payant le spread de 80 bps d'EDEL pour rien.

**M4 — LE CLASSEMENT INVERSE LE SENS DE L'HISTOIRE.**
Pendant TOUTE la montée de +156 %, EDEL était classé `POMPE_PIEGE` (stabilité 9→33 : « trop rapide, c'est un piège »). Il est passé `LEADER` seulement après le sommet. Le moteur a refusé d'accompagner le mouvement, puis a acheté les dumps de la descente. Refuser la montée, acheter la chute : le double inverne.

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

## 6. État et garde-fous

- Hulk tourne en **PAPER** (décision Christophe du 30/08) — aucun ordre réel, 0 € du début à la fin.
- Ce fichier est **une analyse** — aucun paramètre moteur modifié. Toute modification = spec figée avant test + GO explicite du propriétaire (règle non négociable n°5).
- Sources primaires : `hulk-mexc/runs/PAPER_V1_*.csv` · `hulk-mexc/runs/PAPER_V1_20260915_064552_state.json` · `hulk-mexc/runs/croisement_contexte.jsonl` · `hulk-mexc/runs/CYCLE_EDEL_20260917_1754.md` · `Index_Maison/MEMOIRE_COLLAB.md` (14/09 : « +44 % latent » RIZE ; 15/09 : audit 472 refus pendant +60,9 % EDEL).
