# 🎯 SET-UP OPÉRATIONNEL — RED (RedStone) — mesuré 30/08/2026 14:11Z

> Décision commune : on ne câble RIEN aveuglément. On mesure le comportement réel et on
> définit le protocole d'entrée/sortie avec la règle de la famille : **fenêtre temporelle +
> déclencheur de micro-structure, jamais l'heure seule.**

---

## 📏 MESURE DU COMPORTEMENT (fraîche, 14:11Z)

### 1. Signal précurseur (divergence, run rejoué à l'instant)
| Volet | RED maintenant | Lecture |
|---|---|---|
| Signal précurseur (m6→delta panier +4h) | **+0.14 → 🟡 léger achat** | Repasse acheteur léger (retombé de +0.16 à +0.14, sous le seuil LEADER 0.15) |
| Timing (corr croisée) | corr 0.63 · **lag +4h** | RED **suit** le panier — retarde de 4h, pas un leader |
| Divergence actuelle | m6 6h **2.46** vs passé **4.01** | DIV réduite → le "pump" RED s'essouffle vs son passé |
| Gating temporel | m6 jour 4.12 · nuit 3.50 · 0% pics>6% | ⚪ distribué — ni diurne ni nocturne dominant |

→ **Lecture : RED est un suivard du panier, mode achat léger, amplitude intraday marquée.**
C'est un profile de **set-up horaire** (cycle), pas de signal précurseur global.

### 2. Comportement prix (fenêtre 6h en direct, 08:07→14:06Z)
```
08h avg 0.10876  09h avg 0.10921  10h avg 0.10953  11h avg 0.10941
12h avg 0.11030  13h avg 0.11068  14h avg 0.11082
min 0.10854 · max 0.11129 · range 6h = 2.53% · prix actuel ~0.11076
```
→ RED **monte en continu depuis 08h** et tape déjà ~0.111, **juste à l'entrée de la fenêtre où
le modèle attend le creux (15-16h)**. Concrètement : la paire est en **fin de montée de matinée
plutôt qu'en creux** — c'est le point de prudence du moment, pas un point d'achat opportun.

---

## 🧪 MÉTRIQUES PRO — VERDICT CORTANA (30/08, validé Christophe)

Les 3 métriques de la norme quant sont maintenant mesurées sur chaque paire (dont RED) :
| Métrique | Valeur RED (14:59Z) | Ce que ça dit |
|---|---|---|
| **Amihud Illiquidity Ratio** | **2.43e-06** | ✅ **GARDER** — si Amihud **triple** → stopper net (assèchement) |
| **Parkinson vol** | 0.01 | ❌ **JETER pour small caps MEXC** (s'emballe sur les mèches → bruit) |
| **Trade Sign Delta** | **+0.08** | ✅ **GARDER ABSOLUMENT** — seuil d'alerte **> +0.20** pour valider le départ |
| corr BTC / ETH 24h | +0.52 / +0.63 | Moyenne (à comparer jour par jour) |

→ **Décision :** la boussole = nos métriques maison (poussière, régime, mur) ; les arbitres
quanti = Trade Sign Delta (seuil +0.20) et Amihud (triple = stop). **Parkinson retiré du suivi.**

## ⚖️ NUANCE VALIDÉE (Christophe, 30/08)
- **Le spoof reste une TENSION à mesurer** (il nous a déjà évité un piège sur BTC) — on le garde.
- **Le mur affiché n'est PLUS un « support »** : c'est une simple information (il peut être retiré
  en 1 s sur micro-cap). La vraie profondeur se mesure par le flux exécuté (Amihud/delta).

---

## 🔗 RED vs BTC/ETH — mesure et CORRECTION (30/08, avis Cortana)

**Mesure (3 jours) :** corr horaire RED~BTC = +0.07 · RED~ETH = −0.01 · BTC~ETH = +0.98.
Par phase : MATIN 08-13h RED~BTC = −0.85 (inverse) · CREUX 14-17h ≈ 0 (solo) · NUIT +0.60.
Niveaux relatifs (100=base) : CREUX RED 98.0 vs BTC 99.7 → RED plonge pendant que le marché reste stable.

**⚠️ Correction après avis Cortana (30/08) : cette dé-corrélation est un ARTEFACT de liquidité
fine, pas une force de l'actif.** Sur une micro-cap 45 M$, des corrélations qui sautent d'un
jour à l'autre (POMPE-PIÈGE → LEADER → NEUTRE en 48h) = bruit de carnet d'ordres (rotations de
MM, arbitrages de bots), pas une décorrélation fondamentale.

**Règle qui en découle (endogénéité) :**
1. Le set-up RED est **STRICTEMENT ENDOGÈNE** : carnet MEXC + mur bid 45K + poussière.
2. **Aucune entrée ne sera déclenchée ni bloquée par le mouvement de BTC/ETH.** Le ratio
   vs BTC/ETH n'est PAS un filtre d'entrée (faux signaux garantis le matin).
3. La diversification réelle vient du fait que RED a son propre cycle horaire — pas d'une
   « maturité » d'actif. À utiliser en connaissance de cause.

---

## 🧭 LA LOGIQUE DU SET-UP (règle famille)

### Objectif
Exploiter le cycle intraday de RED : **acheter la zone creux 15-16h UTC, revendre le pic de
nuit 01-05h** — mais SEULEMENT quand la microstructure confirme (jamais à l'heure seule).

### Le cadre d'entrée (tout doit être vrai — enrichi avis Cortana final 30/08)
1. **Fenêtre** : on autorise l'entrée **uniquement 14h–17h UTC** (interdiction hors fenêtre).
2. **Déclencheur** : la **poussière (tx fantômes) < 15%** (assèchement = vraie accumulation,
   pas de panique) ET le **mur bid 45K$ est testé et tient** (le MM absorbe sans fuir).
3. **Filtre macro (Cortana)** : **PAS d'entrée si BTC ou ETH fait un mouvement directionnel
   > 1.5% en 15 min** (breakout/breakdown) — RED orpheline : une tempête macro détruit le creux.
4. **Garde-fou volatilité** : bloquer l'entrée si le **volume 15 min > 3× la moyenne 24h**
   (signal de panique, pas un creux sain).
5. **FPOB (filtre Cortana, phase réelle)** : mesurer le ratio **Volume Bid/Ask ±2% du mid**
   entre 13h-14h UTC — **interdiction d'entrer si ratio < 1.2** (le mur 45K est grignoté par
   les vendeurs = couteau qui tombe).
6. **Régénération du mur (Cortana)** : si le mur est **grignoté > 30% en < 2 min** sans que le
   **Trade Sign Delta > +0.15** → **annulation immédiate** de l'ordre en cours de déploiement
   (le mur est un leurre, pas un appui).
7. **Exécution (Cortana)** : **50% de la position au premier contact du creux 15-16h**, puis
   **50% uniquement si la poussière < 10%** (désintérêt total des vendeurs) ; stop dur
   dynamique = **1,5× le range de la bougie 15 min**.

### Le cadre de sortie
- **Sortie partielle au pic de nuit (01h–05h)** : scaling out — dégager une partie vers
  0.110-0.112+, garder le reste derrière le trailing de Hulk.
- Le stop/rip **existant de Hulk** gère la suite (RED ultra-volatile, dd15 22,86%).

### Condition de remise en cause
- **Invalider** si RED casse le plancher **0.103-0.104** hors fenêtre (le modèle horaire tombe).
- **Arrêter le set-up** si les frais réels MEXC + slippage dépassent ~1% nets (marge 2,4% → net
  < 1,5% ne vaut pas le risque).

---

## ⏱️ RECOMMANDATION IMMÉDIATE (14:11Z)
RED est à **0.11076, en fin de montée**, à l'entrée de la fenêtre de creux attendu. **On n'achète
pas ici** : le déclencheur « poussière sèche + mur testé » n'est pas confirmé et le prix est
haut de cycle, pas bas. On **attend la fenêtre 15-16h** et on regarde si RED retombe dans la
zone **0.107-0.109** avec poussière basse → c'est là que l'entrée devient valide.

---

## 🔌 DÉCIDÉ (pas câblé aujourd'hui)
- RED reste **en seed** (bag 10$), rien d'activé.
- On **mesure le set-up en observation** : capter poussière + mur + volume 14-17h sur RED.
- **Prochaine validation dans ~7 jours** pour confirmer le cycle (règle Christophe : ce qui vaut
  un temps peut ne plus valoir).

---

## 📈 SUIVI MESURÉ — JOUR PAR JOUR (à comparer, ne rien supprimer)

> Protocole : `hulk-mexc/scripts/suivi_setup_actif.py` (généralisé à TOUTES les paires) —
> mesure à chaque run, journalisée dans `hulk-mexc/runs/SUIVI_SETUP_REDUSDT.jsonl` + `.md`.
> La plist quotidienne (16:35 locale) mesure les 20 paires chaque jour, même heure = comparable.
> On compare les lignes : **différence ou pas ?**

### Jour 1 — 30/08 14:24Z (référence, fenêtre 14-17h)
| Mesure | Valeur | Lecture |
|---|---|---|
| Prix | **0.11081** | HORS zone d'entrée (0.107-0.109) — haut de cycle |
| Régime | COOLING | Pause |
| Poussière (tx fantômes) | **1.2%** | ✅ < 15% (assèchement — déclencheur OK) |
| Mur bid max | **45 240$** | Mur présent et tenu |
| Spoof | 1.68% | Faible — mur réel |
| dd15 | 21.5% | Volatilité rafale élevée (constant) |
| corr BTC 24h | **+0.53** | Moyenne (ce jour-ci, pas le −0.85 du matin) |
| corr ETH 24h | +0.63 | Idem |
| Signal divergence | **neutre (stab 0)** | RED ni leader ni pompe-piège actuellement |
| Verdict | Fenêtre OK · poussière OK · **prix hors zone** | → **pas d'entrée** (le déclencheur prix ne valide pas) |

→ **Jour 1 : le cadre tient — on attend que le prix retombe dans la zone. Aucune entrée.**

### Jour 2+ (à compléter)
| Jour | Date/Heure | Prix | Poussière | Mur | Signal div | Verdict |
|---|---|---|---|---|---|---|
| 2 | _à mesurer_ | | | | | |
| 3 | _à mesurer_ | | | | | |
| 4 | _à mesurer_ | | | | | |
| 5 | _à mesurer_ | | | | | |
| 6 | _à mesurer_ | | | | | |
| 7 | _à mesurer_ | | | | | |

_Règle : on ne supprime pas les lignes passées — c'est l'évolution qui fait foi_ (Christophe).

## Archives
- Signal divergence rejoué : `hulk-mexc/runs/DIVERGENCE_20260830_1411.md` (RED 🟡 léger achat 0.14)
- Fiche pattern + famille : `Crypto_Projet/FICHE_PATTERN_SETUP_RED_20260830.md`,
  `Crypto_Projet/SYNTHESE_RED_SETUP_FAMILLE_20260830.md`