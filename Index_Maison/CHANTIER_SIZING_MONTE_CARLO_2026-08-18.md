# CHANTIER — Sizing / Ruine Monte Carlo (18/08/2026)

**Statut** : 📊 ANALYSE RELANCÉE ET FAITE (08/09 — la veilleuse a bien rappelé) — voir §6 ci-dessous. Question sizing prête à soumettre à la famille.
**Origine** : Monte Carlo de résistance (18/08) + considération Christophe (données polluées par le chantier)
**GO** : Christophe — « mettre en chantier à faire avec veilleuse qu'on oublie pas »

---

## 6. RELANCE DU 08/09 — les 4,4× ne tiennent PAS (veilleuse à date)

Commande exécutée (lecture seule) : `python3 Index_Maison/scripts/monte_carlo_ace.py --depuis 2026-08-18`
→ rapport : `MONTE_CARLO_ACE_2026-09-08_depuis_2026-08-18.md`

### 6.1 Comparaison 18/08 (1 jour propre) vs 08/09 (fenêtre 18/08 → fin d'ère VORTEX_COLLAB ~22/08)

| Métrique | Période propre (18/08) | Fenêtre élargie (08/09) | Verdict |
|---|---|---|---|
| PnL / cycle réel | +0,0124 $ | **+0,0036 $** | ÷ 3,4 — l'edge ne tient pas |
| PnL / trade | +0,2109 $ | **+0,0563 $** | ÷ 3,8 |
| Win rate | 56,9 % | **48,6 %** | −8,3 pts |
| Ruine (DD ≥ 25 %) | 32,5 % | **100,0 %** | TOUS les mondes mélangés meurent |
| DD médian | 19,8 % | **91,0 %** | × 4,6 |
| DD pire cas (95ᵉ) | 42,8 % | **346,5 %** | × 8 |
| PnL total réel | +65,4 $ (1 j) | **+141,77 $** (4 j) | positif mais fragile |

Base commune : 2 517 fills / 39 502 cycles, P(fill) réel 6,37 % (BETA 9,4 % · ALPHA 3,4 %), 5 000 chemins, graine 42, capital 20 $.

### 6.2 Lecture honnête (chiffres consignés, zéro interprétation au-delà)

1. **La journée du 18/08 était un meilleur des cas, pas un nouveau régime.** Élargir la fenêtre à la fin de l'ère VORTEX_COLLAB dégrade TOUTES les métriques de 3 à 8×. Le « 4,4× » ne tient pas.
2. **Cohérent avec la découverte des 13 gros coups (07/09)** : le profit est concentré dans de rares événements (holds 5-9 s) → mélanger l'ordre les disperse et le creux devient mortel. Ruine 100 % ≠ edge négatif : la somme réelle est positive (+141,77 $) — c'est le CHEMIN qui tue, exactement le « signe du drift vs taille » du signet Di_Krass.
3. **CAVEAT COMPTABLE MAJEUR (déjà tranché au vault 07/09)** : ces CSV sont legacy BRUT (frais jamais loggés avant le fix 15/08). Le +141,77 $ est BRUT ; au modèle famille (8 bps AR), l'estimation de frais ~4 000 $ sur ces 2 517 fills rend la fenêtre NETTE fortement négative. Les deux analyses (18/08 et 08/09) sont sur la même base brute → la COMPARAISON reste valide, les NIVEAUX absolus ne le sont pas.
4. **La gate IRM OFF explique une partie de la dégradation** : les jours post-18/08 ont trade le bruit en compression (comme la nuit du 07→08/09 : 63 trades, brut −0,98, frais 44,23). La gate ON 0.85 testée aujourd'hui sur la copie anti-2022 vise exactement ce gaspillage.

### 6.3 Question à soumettre à la famille (PAS décidée ici)

> Le sizing d'ACE (BETA x5 ~590 $, ALPHA x13 ~6 000 $ engagés) face à un edge de +0,0036 $/cycle BRUT :
> (a) réduire la taille (creux moins profonds, drift/cycle plus petit — le MIT/Di_Krass dit que ça ne change pas le signe) ;
> (b) augmenter P(fill) sans casser le win rate (gate IRM bien réglée = fills de meilleure qualité, pas plus nombreux) ;
> (c) Kelly ombre étendu à ACE (dossier existe : SPEC_KELLY_OMBRE_2026-08-15.md) — couvre Hulk, pas encore ACE.
> **Donnée nouvelle pour la consultation : ruine 100 % sur ordres mélangés malgré total positif → le levier n'est pas le problème n°1, la CONCENTRATION de l'edge (rareté des gros coups) l'est.**

---

## 1. Le constat (preuves à la main)

### 1.1 Le rêve vs la réalité (leçon 0x_Punisher)
- P(fill) réel d'ACE : **6,5 %** des cycles (BETA 9,4 % · ALPHA 3 %) — 84 018 cycles, 5 455 fills
- PnL moyen / trade : **+0,0427 $** (le rêve) → PnL moyen / **cycle réel** : **+0,0028 $** (la réalité)
- Un SKIP n'est pas gratuit : chaque cycle = temps, tension, lecture des murs. 84 018 cycles × 0,5 s ≈ **11,7 h de travail** pour +233 $.

### 1.2 Les données étaient polluées par le chantier (considération Christophe — CONFIRMÉE)
| Jour | P(fill) | PnL du jour |
|---|---|---|
| 13/07 | 6,9 % | **-17,9 $** (crash) |
| 16/08 | 3,2 % | -0,5 $ (moteur quasi à l'arrêt) |
| 18/08 (base scellée) | 5,9 % | **+65,4 $** |

+ **trou de 30 jours** (13/07 → 12/08 : zéro donnée — moteur arrêté par les chantiers).

### 1.3 AVANT / APRÈS (Monte Carlo, 5 000 chemins, graine 42, capital 20 $)
| Métrique | 13 jours de chantier | **Période propre (18/08)** | Gain |
|---|---|---|---|
| PnL / cycle réel | +0,0028 $ | **+0,0124 $** | **4,4×** |
| PnL / trade | +0,0427 $ | +0,2109 $ | 5× |
| Win rate | 40,3 % | **56,9 %** | +16,6 pts |
| Ruine (DD ≥ 25 %) | 80,6 % | **32,5 %** | ÷ 2,5 |
| DD médian | 39,8 % | **19,8 %** | ÷ 2 |
| DD pire cas (95ᵉ) | 103,9 % | 42,8 % | ÷ 2,4 |

Rapports : `MONTE_CARLO_ACE_2026-08-18.md` + `MONTE_CARLO_ACE_2026-08-18_depuis_2026-08-18.md`

---

## 2. Le problème à trancher

**Même en période propre, 32,5 % de ruine (creux ≥ -25 % du capital) sur 20 $, c'est trop.**
La question : la **taille des positions** (BETA x5 ~590 $ engagés, ALPHA x13 ~6 000 $ engagés)
est **grosse par rapport au gain réel par cycle** (+0,0124 $) → les enchaînements de pertes
creusent profond avant la remontée.

Options possibles (à soumettre à la famille, PAS décidées ici) :
- Réduire le levier/la taille (creux moins profonds, mais PnL/cycle plus petit)
- Ajuster le filtre pour plus de fills sans casser le win rate (+23 % de PnL/cycle si 6,5 % → 8 %)
- Kelly / sizing dynamique (dossier Kelly ombre existe déjà : `SPEC_KELLY_OMBRE_2026-08-15.md`)

> **⚖️ 18/08 — famille consultée (secteurs) : goulot n°1 GLOBAL = EXÉCUTION/sizing.**
> Pépite validée = **Kelly en mode ombre** (dry-run, jamais d'activation live avant preuve).
> Le Kelly ombre couvre Hulk — **reste à l'étendre à ACE** (dry-run) + décision d'application.
> Verdict complet : `scripts/CONSULTATION_FAMILLE_SECTEURS_20260818/VERDICT_FAMILLE_SECTEURS.md`

> **🔖 18/08 — signet X (Di_Krass) : confirmation externe indépendante.**
> « Le MIT l'a filmé : la taille du compte ne change RIEN à la ruine. Roulette à 47 %,
> le drift gagne toujours, le capital n'achète que du temps. **C'est le signe du drift
> (l'edge) qui compte, jamais la taille.** » → rejoint notre constat Monte Carlo : le
> levier ne sauve pas, seul le PnL/cycle réel (le signe) compte. À citer dans la
> consultation famille du 22/08 comme appui externe.

---

## 3. Étapes (à la fin du run 96h — 22/08)

1. Relancer `python3 Index_Maison/scripts/monte_carlo_ace.py --depuis 2026-08-18`
   (4 jours propres de base scellée → statistique plus solide qu'1 seule journée)
2. Comparer : les 4,4× tiennent-ils ? Ruine / DD médian / PnL par cycle ?
3. Rédiger l'analyse + soumettre la question du sizing à la famille (consultation)
4. Verdict famille → proposition chiffrée → GO Christophe → codeur si besoin
5. Release Receipt à la clôture (règle maison : rien ne se supprime, tout est réversible)

---

## 4. Veilleuse

- Script : `Index_Maison/scripts/veilleuse_sizing_monte_carlo.sh` (toutes les 6h)
- LaunchAgent : `com.ace777.veilleuse-sizing-monte-carlo` (StartInterval=21600)
- Fichier rappel : `Index_Maison/VEILLE_SIZING_MONTE_CARLO.md` — passe en « DATE ATTEINTE » le 22/08
- ⏰ **Date d'analyse : 2026-08-22** (fin du run ACE 96h, même fenêtre que la confrontation ACE↔Hulk)

---

## 5. Réversibilité

- `launchctl unload ~/Library/LaunchAgents/com.ace777.veilleuse-sizing-monte-carlo.plist`
- `rm` du script + plist + fichier veilleuse → retour à l'état antérieur. Rien ne se supprime d'autre.
