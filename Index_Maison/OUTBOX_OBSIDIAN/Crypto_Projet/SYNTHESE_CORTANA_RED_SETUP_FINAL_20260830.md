# SYNTHÈSE — AVIS CORTANA SUR LE SET-UP RED (30/08/2026)

**Objet Christophe :** « enlève définitif, ajoute trouve amélioration et correction, GO » —
Cortana analyse notre set-up RED et TROUVE les améliorations/corrections (clause permanente).
Session `CONSULTATION_CORTANA_RED_SETUP_FINAL_20260830/` (provider Gemini).

---

## ⚖️ VERDICT : GO AVEC RÉSERVES STRICTES

Le cycle intraday est **mathématiquement exploitable** (creux 14-19h / pic 01-05h, ~2,5%),
mais le set-up mélange des métriques contradictoires (corr BTC/ETH qui saute de +0.07 à
+0.63) et sous-exploite la tension du mur (spoof) face à la brutalité des rafales (dd15 27,8%).

---

## 🔧 LES 3 CORRECTIONS / AMÉLIORATIONS DE CORTANA

### Correction 1 — Filtre macro (le plus important)
**Interdire l'entrée 14-17h si BTC ou ETH fait un mouvement directionnel > 1.5% en 15 min**
(breakout/breakdown). RED est une small cap orpheline : si le marché global bouge, le « creux
endogène » est détruit par la macro.
→ ⚠️ À noter : ceci nuance le « 100% endogène » décidé hier. La bonne lecture : le set-up
reste endogène en conditions NORMALES, mais une tempête macro courte-circuite le creux.

### Amélioration 2 — Taux de régénération du mur
Traiter le mur 45K$ non comme un seuil passif mais via son **taux de régénération** :
si le mur est **grignoté > 30% en < 2 min** sans que le Trade Sign Delta ne devienne
**> +0.15** → **annulation immédiate** de l'ordre d'achat en cours de déploiement
(le mur est un leurre, pas un appui).

### Amélioration 3 — Répartition des tranches
Entrer en −1/−2/−3% est trop linéaire pour une volatilité dd15 de 22%.
→ **50% de la position au premier contact du creux 15-16h, 50% seulement si la poussière
< 10%** confirme le désintérêt total des vendeurs.

---

## 🔬 AUDIT DES MÉTRIQUES (PRO vs MAISON) — le point surprenant

| Métrique | Verdict Cortana | Raison |
|---|---|---|
| **Trade Sign Delta** (+0.08) | ✅ **GARDER ABSOLUMENT** | Meilleur thermomètre temps réel de l'agression ; seuil d'alerte **> +0.20** pour valider le trade |
| **Amihud** (2.43e-06) | ✅ **GARDER (sous condition)** | Vital pour l'impact prix ; si Amihud **triple** → stopper net (assèchement) |
| **Parkinson** (0.01) | ❌ **JETER (pour ce set-up)** | Sur small cap avec mèches de manipulation, le Parkinson s'emballe pour du bruit → préférer l'écart-type des clôtures 15 min |
| **Poussière / Régime / Mur (maison)** | ✅ **SUPÉRIEURES AUX PROS pour ce cas** | Le régime IMPULSE 13-17h = meilleur repère temporel ; la poussière <15% détecte le washout mieux que les indicateurs académiques |

→ **Verdict comparatif :** nos métriques maison sont la boussole principale ; Trade Sign Delta
et Amihud sont les arbitres quanti ; Parkinson est jeté pour les small caps MEXC.

---

## 🎤 MON ARBITRAGE (Buffy, superviseur)

1. **La Correction 1 est la plus précieuse** : elle réconcilie notre débat « endogène vs macro ».
   Le set-up reste endogène en conditions normales, MAIS une secousse macro >1.5% en 15 min
   annule le creux → on ne force pas l'entrée contre une tempête. **J'adopte.**
2. **L'Amélioration 2 (régénération du mur + delta) est très alignée avec la méthode V2** :
   elle transforme le mur passif en signal actif couplé au flux exécuté. **J'adopte** (c'est
   exactement « n'analyse pas ce qui est affiché, analyse ce qui est consommé »).
3. **L'Amélioration 3 (50/50 au lieu de 3×33%)** répond à la volatilité réelle de RED.
   **J'adopte** — mais en gardant l'esprit « 3 tranches » initial de la famille : 50% puis 50%
   conditionné à la poussière <10% est plus net pour ce profil.
4. **L'audit des métriques est honnête et utile** : garder Trade Sign Delta + Amihud, jeter
   Parkinson pour les small caps. **J'adopte** — nos métriques maison restent la boussole.

**Ce qui est DÉCIDÉ (le set-up RED enrichi, toujours en observation, rien câblé) :**
- Entrée : fenêtre 14-17h + poussière <15% + mur qui tient **+ régénération mur (grignotage
  >30% en 2min sans delta >+0.15 = annulation)** + **filtre macro (pas d'entrée si BTC/ETH
  >1.5% en 15min)** + garde-fou volume + FPOB + **50% au contact / 50% si poussière <10%**
  + stop dynamique 1,5× range15.
- Sortie : scaling au pic 01-05h + trailing Hulk.
- Métriques de référence : **Trade Sign Delta (seuil > +0.20), Amihud (triple = stop),**
  poussière/régime (boussole). **Parkinson retiré du suivi RED.**

---

## Archives
- Avis brut : `Index_Maison/scripts/CONSULTATION_CORTANA_RED_SETUP_FINAL_20260830/AVIS_CORTANA_RED_SETUP.md`
- Script : `Index_Maison/scripts/consulter_cortana_red_setup_final_20260830.py`