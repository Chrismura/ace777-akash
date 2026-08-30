# SYNTHÈSE — SET-UP RED soumis à la famille (ULTRA + JUGE) + codeur — 30/08/2026

**Objet Christophe :** « oui mais aux 6 → 2 plus le codeur, toi et moi, suffisent. GO »
Session `CONSULTATION_RED_SETUP_20260830/` (AVIS_ULTRA, AVIS_JUGE, AVIS_CODEUR — provider Google Gemini).
**Contexte soumis :** fiche `FICHE_PATTERN_SETUP_RED_20260830.md` (2238 pts RED sur 3 jours, creux 15-16h → pic 01-05h).

---

## ⚖️ LES ARRETS (3/3 — GO mais TOUS AVEC RÉSERVES)

| Membre | Verdict | Réserve-clé |
|---|---|---|
| **ULTRA** | GO AVEC **RÉSERVES SÉVÈRES** | Actif 44M$ + dd15 22% sans kill-switch de liquidité = décimation en cas de décrochage macro |
| **JUGE** | GO AVEC RESERVES | dd15 22% + échantillon 3 jours trop court = risque à encadrer strictement |
| **CODEUR** | GO AVEC **RÉSERVES TRÈS STRICTES** | Échantillon 3j suffisant pour observer, insuffisant pour une *exécution aveugle* |

→ **Aucun ne rejette le pattern (le cycle horaire est réel et répliqué).** Mais tous refusent
l'exécution « à heure fixe aveugle ». C'est LA convergence à retenir.

---

## 🎯 LE CONSENSUS — 3 réserves identiques (à prendre au sérieux)

### 1. Le mur à 45 240$ = mirage en stress (les 3 le disent)
Sur une market cap 44M$, un mur de cette taille **s'évapore en une seconde** si le marché
global (BTC/ETH) décroche. Le « creux d'accumulation » peut devenir une chute libre sans
plancher. → **Ne pas traiter 45K$ comme un ancrage absolu.**

### 2. Échantillon 3 jours = overfitting (les 3 le disent)
Valider un cycle intraday sur 72h, c'est **trader le hasard d'une semaine calme**. Si le
régime macro change (on est en saison CALME 🧊), les heures pivot peuvent se déplacer.
→ **Le pattern est une hypothèse de travail, pas une certitude.**

### 3. Frais + slippage mangent la marge (ULTRA + codeur)
Écart jour/nuit ~2,4-2,8%. Si MEXC taker/maker + slippage dépassent ~1%, **la marge nette
fond de moitié**, surtout en zone de liquidité mince 01-05h. → Le net peut être < 1,5%.

### Bonus codeur (pertinent) : répliquer « l'heure du creux » sur 15 paires = hérésie
Chaque token a sa propre structure de carnet dictée par son teneur de marché. **On ne peut
pas figer 15-16h pour tout le monde.**

---

## 🔧 LA SOLUTION COMMUNE (leur amélioration converge sur la MÊME chose)

Tous proposent **la même architecture en 2 temps** :

> **Fenêtre temporelle (opportunité) + Déclencheur de micro-structure (confirmation), jamais l'heure seule.**

**Sous-consignes concrètes :**
1. **Fenêtre** : Hulk surveille RED **uniquement 14h-17h UTC** (interdiction d'entrer en dehors).
2. **Déclencheur réel pour l'achat** (tous) :
   - le prix touche la zone psychologique/technique ET
   - la **poussière (tx fantômes) < ~15%** (assèchement = vraie accumulation, pas de panique) ET
   - le **mur bid de 45K$ est testé et tient** (preuve que le MM absorbe sans fuir).
3. **Garde-fou volatilité (ULTRA, le plus dur)** : bloquer l'entrée si le volume 15 min
   précédentes > 3× la moyenne 24h (panique, pas un creux sain).
4. **Exécution fragmentée (ULTRA)** : entrer en **3 tranches** (-1%, -2%, -3%) sous le prix
   médian de la fenêtre, stop dur dynamique = 1,5× le range de la bougie 15 min.
5. **Heure du Creux Locale (HCL, codeur)** : pour généraliser à d'autres paires, calculer
   l'heure pivot par **moyenne glissante 7 jours par token**, pas une heure figée globale.

---

## 🎤 MON AVIS (Buffy, superviseur)

Je valide **totalement** la direction d'ULTRA/JUGE/codeur, et je la vulgarise :

- **Le pattern n'est pas mort — il est nuancé.** Le creux 15-16h / pic 01-05h reste la
  structure dominante de nos 2238 points. Ce qui change, c'est qu'on ne doit pas *programmer
  un achat à 15h pile* : on doit **autoriser l'entrée dans la fenêtre 14-17h ET attendre que
  la microstructure confirme** (poussière qui sèche + mur qui résiste).
- **C'est exactement l'esprit de nos autres set-ups** (QAIT = plancher + zone heure ;
  EDEL = cycle nuit→jour) : l'heure est le **cadre**, le signal de micro-structure est le
  **verdict**. L'heure seule fait des biais ; l'heure + confirmation fait un set-up.
- **La vraie faiblesse qu'ils ont attrapée ensemble :** le mur 45K$ et le range 2,4-2,8% sont
  bons dans le calme d'août. Ils ne tiendront pas un régime macro baissier. Notre discipline
  « valider d'abord » est préservée.

**Ce que je tranche (corrigé + GO-size, sans sur-engager Hulk) :**
1. **On ne câble RIEN maintenant** — on garde RED en seed, ce point a été discuté.
2. On transforme le set-up en **protocole d'observation encadré** sur 7 jours de plus pour
   valider la fenêtre 14-17h + le déclencheur poussière/mur, avant toute activation.
3. Quand on activera, ce sera sous la forme **« fenêtre 14-17h + poussière <15% + mur testé »**
   → jamais « acheter à 15h parce que le CSV le dit ». C'est là que réside le GO.

**Frais nets à vérifier d'abord** : si taker+slippage > ~1% sur RED, le set-up perd sa
pertinence (marge 2,4% → net <1,5%). À mesurer avant tout.

---

## Archives
- Avis bruts : `Index_Maison/scripts/CONSULTATION_RED_SETUP_20260830/AVIS_{ULTRA,JUGE,CODEUR}.md`
- Script réutilisable : `Index_Maison/scripts/consulter_red_setup_20260830.py`
- Fiche source : `OUTBOX_OBSIDIAN/Crypto_Projet/FICHE_PATTERN_SETUP_RED_20260830.md`