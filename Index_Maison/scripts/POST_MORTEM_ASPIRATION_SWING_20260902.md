# POST-MORTEM — TABLE RONDE ACE777 × GEMINI (14 ROUNDS)
**Date :** 2026-09-02 · **Session :** `GEMINI_SESSION_EDGE_JUILLET.md` (transcript complet)
**Objet :** Carte [ASPIRATION-SWING-01] — replay, verdict, et sort de l'écosystème ACE

---

## 1. Ce qui a été fait

- 14 rounds de table ronde avec Gemini (audit → réfutations croisées → conception)
- Historique complet conservé : `Index_Maison/scripts/GEMINI_SESSION_EDGE_JUILLET.{json,md}`
- Données regroupées par setup (S1-S8, 18k+ trades), WR par setup, fenêtres 80-90% localisées
- Gate régime causal testé (amplitude 2h) : réel mais insuffisant
- Disjoncteur stop-storm joué sur CSV réels : **86 déclenchements, -10 694 USDT évités (89%)**
- Klines 1m réelles téléchargées (7201 bougies) + funding réel (16 taux) en cache `runs/`
- Replay complet de la carte [ASPIRATION-SWING-01] : 453 murs >40$ dédupliqués

## 2. Résultats du replay ASPIRATION-SWING-01

| Variante | NET | /trade | WR | PF |
|---|---|---|---|---|
| Carte originale (TP = 0.5×/0.75× mur, stop 1.5×ATR 1h) | -57.88 | -0.128 | 22% | 1.13 |
| TP recalibrés ×amplitude suivie (0.5x→2x) | -56.7 à -116.8 | -0.13 à -0.26 | 4-10% | 0.19-1.11 |
| Stop ATR 1m (serré) | -65.64 | -0.145 | 8% | 0.72 |

**Critères de succès (PF > 1.50, net > 0) : jamais atteints → critère d'abandon déclenché.**

## 3. Les trois découvertes structurelles

1. **Follow-through asymétrique** : après un mur >40$, continuation 75% du temps mais médiane +18.1$ (26 bps) ; les 25% contre vont à ~64$ médiane. Profil inverse de celui requis pour survivre aux coûts.
2. **Paradoxe du TP maker** : mécaniquement valide (83-92% de fills passifs, zéro adverse selection à la sortie) mais **les fills sélectionnent les perdants** — ils arrivent sur les mouvements faibles, le stop mange les violents.
3. **Timing d'entrée inversé** : le wall_drop de 40$+ est déjà consommé au fill. Le moteur entre sur le résidu (+18$ médian), pas sur la chute. Les holds de 8s à +0.3/+0.6 bps étaient le résidu terminal avant retour de pendule.

## 4. Verdicts validés/enterrés (consolidé)

**VALIDÉ (conservé, instrumenté) :**
- Physique du Manifeste : vide → aspiration → percussion (φ=1.618, 37.8°, 0.85) — le signal est réel
- Disjoncteur stop-storm (N=10/30min, cooldown 2h) : -89% de pertes
- `swarm_cohesion` comme coupe-circuit proactif (perte de synchronie = tempête de stops)

**ENTERRÉ (replay, zéro ordre) :**
- Taker HF 8 bps (edge brut réel t=2.66 mais 65x trop petit)
- Donchian swing V2 (réfutée par protocole R4/R6)
- ASPIRATION-SWING maker en sortie (ce post-mortem)
- Entrée anticipative dans le mur (condamnée R14 : piège à adverse selection, spoofing)

## 5. Mot de la fin (Gemini, R14)

> *"Tu n'as pas construit un mauvais bot, Christophe ; tu as construit un sismographe d'une précision diabolique. Mais on ne gagne pas sa vie en tradant les secousses qu'un sismographe détecte après coup. Conserve le cockpit, admire la physique de ton Manifeste, mais pose les armes de l'exécution sur ce marché-là."*

## 6. État opérationnel recommandé

1. **Champion en shadow mode** (zéro ordre, CSV + télémétrie vivants) — le sismographe tourne
2. **Disjoncteur + cohésion** : à intégrer dans le cockpit comme gardes-fous permanents
3. **Replay scripts** archivés dans `/tmp` → à copier dans `scripts/` si Christophe veut les rejouer
4. **Prochaine ère si reprise de la capture** : il faudrait des coûts d'exécution ~10x plus bas (maker institutionnel, VIP, ou autre venue) — hors de portée du testnet actuel

---
*Généré par la table ronde Buffy × Gemini — aucun ordre passé, champion intact (md5 14bcf868d46effba010cac577cbb004c).*
