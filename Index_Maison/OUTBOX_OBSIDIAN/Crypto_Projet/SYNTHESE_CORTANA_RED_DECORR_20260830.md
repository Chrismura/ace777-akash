# SYNTHÈSE — AVIS CORTANA sur RED (pattern + dé-corrélation) — 30/08/2026

**Objet Christophe :** « oui soumettre à cortana » — validation croisée des 2 découvertes RED
(pattern intraday + dé-corrélation vs BTC/ETH). Session `CONSULTATION_CORTANA_RED_DECORR_20260830/`.
Contexte soumis : fiche pattern + set-up opérationnel + mesures du 30/08.

---

## ⚖️ LES VERDICTS DE CORTANA

| Découverte | Verdict Cortana | Justesse | Raison |
|---|---|---|---|
| **D1 — Pattern intraday (creux 15-16h → pic 01-05h)** | **GO AVEC RÉSERVES** | ~75% | Réel et exploitable, mais 3 jours = échantillon faible ; le creux 14-19h coïncide avec l'ouverture US + drainage des alts — fragile sans 7 jours de plus |
| **D2 — Dé-corrélation RED vs BTC/ETH (0.07 / −0.01, matin −0.85)** | **NON — artefact statistique probable** | — | Pour un oracle de micro-cap, c'est du **bruit de carnet d'ordres** (rotations de MM, arbitrages de bots isolés), pas une décorrélation fondamentale. Le −0.85 matinal comme « signal inverse » = **piège à perte** |

→ **Cortana confirme le pattern horaire (D1) mais REJETTE ma lecture de la dé-corrélation (D2).**

---

## 🎤 MON ARBITRAGE (Buffy, superviseur)

**Elle a raison, et je corrige ma lecture.**

1. **La dé-corrélation n'est pas un signal fondamental — c'est un symptôme de liquidité fine.**
   Sur un actif à 45 M$ avec un volume de carnet limité, les micro-rotations de market makers
   créent des corrélations « fantômes » qui sautent d'un jour à l'autre (on l'a vu : POMPE-PIÈGE
   → LEADER → NEUTRE en 48h). **Ma présentation « actif d'un autre marché » était trop forte.**
   La vérité : RED est peu corrélé **parce qu'il est peu liquide**, pas parce qu'il est mature.

2. **La consigne opérationnelle de Cortana est la bonne : le set-up RED doit rester STRICTEMENT
   ENDOGÈNE** — carnet MEXC, mur bid 45K, poussière — **jamais** basé sur le ratio vs BTC/ETH.
   Le fait que BTC bouge ne doit ni valider ni invalider une entrée sur RED.

3. **Ce qui reste vrai et robuste** : D1 (le cycle horaire, GO avec réserves) + le cadre famille
   (fenêtre + déclencheur) + la réserve 7 jours. Ces trois-là tiennent.

---

## 🔧 L'AMÉLIORATION CORTANA (GO-sized, à retenir pour quand Hulk passera en réel)

**Filtre de Pression Order Book (FPOB)** — remplacer toute référence de corrélation par la
microstructure du carnet :
1. Mesurer le ratio **Volume Bid / Volume Ask dans ±2% du mid-price** entre 13h-14h UTC.
2. **Interdiction d'entrer** (même dans la zone creux 14-17h) si le **ratio Bid/Ask < 1.2**
   → signe que le mur 45K est grignoté par les vendeurs.
3. **Bénéfice** : évite d'acheter le couteau qui tombe pendant l'impulse baissière de 15h, en
   se basant sur la vraie microstructure, pas sur une corrélation illusoire.

→ Cette proposition **enrichit le cadre famille** (poussière <15% + mur testé + volume 15min)
avec une mesure directe du ratio bid/ask 2% — plus fidèle que le mur 45K seul.

---

## ✅ CORRECTION APPLIQUÉE À NOS FICHES
- **Section « RED vs BTC/ETH » du set-up opérationnel** : re-formulée — la dé-corrélation est
  présentée comme **un symptôme de liquidité fine (à ne pas utiliser comme signal)**, pas comme
  une force de l'actif.
- **Règle nouvelle** : le set-up RED est **endogène** (carnet + poussière + mur). Aucune entrée
  ne sera déclenchée ni bloquée par le mouvement de BTC/ETH.
- **FPOB (ratio bid/ask 2% < 1.2 = blocage)** ajouté au cadre d'entrée pour la phase réelle.
- RED reste **en seed, rien n'est câblé**, observation 7 jours (comme décidé avec la famille).

## Archives
- Avis brut : `Index_Maison/scripts/CONSULTATION_CORTANA_RED_DECORR_20260830/AVIS_CORTANA_RED.md`
- Script : `Index_Maison/scripts/consulter_cortana_red_decorr_20260830.py`