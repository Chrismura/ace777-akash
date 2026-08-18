# ⚖️ VERDICT FAMILLE — Diagnostic par secteurs (18/08/2026)

**Consultation** : 2 membres (gemini, groq) + juge (signets.juge) · unanime.
**Question** : quel est le goulot n°1 du système, et quelle pépite le débloque ?

---

## 🎯 Le verdict : GO-AVEC-RÉSERVE (unanime 3/3)

### 1. Le goulot n°1 GLOBAL — EXÉCUTION / SIZING (3/3)
La ruine Monte Carlo à **32,5 %** (même en période propre) est LE risque bloquant.
Elle menace directement le PnL positif du run (+29,11 $ au moment de la consultation).
→ EXÉCUTION avant MÉMOIRE, HUB, VEILLE ou GOUVERNANCE.

### 2. La pépite — KELLY (43+105), en mode OMBRE (3/3)
- **gemini** : « Le goulot est le dimensionnement fixe sans dynamique de risque » → Kelly
- **groq** : « Implémenter le dimensionnement Kelly pour sécuriser les 29,11 $ de PnL actuels »
- **juge** : « Kelly (43+105), mais en mode bridé/dry-run pour ne pas fausser le run »

### 3. Discipline séquentielle — UNE pépite par goulot (3/3)
NON à deux pépites simultanées. Kelly seule suffit pour le goulot n°1.

### 4. Timing — GO-AVEC-RÉSERVE pour préparer maintenant (3/3)
On peut **préparer/poser** Kelly maintenant en **dry-run / lecture seule**.
**Aucune activation live** sur les fills avant validation après runtests (22/08).

---

## 🔧 Ce que ça veut dire concrètement (et la bonne nouvelle)

**Le Kelly ombre existe DÉJÀ chez nous** — chantier du 15/08 (signets N°43 + N°105),
livré et testé pour **Hulk** : `Index_Maison/scripts/kelly_ombre.py`, calculé chaque jour
à 07h15 avec la discipline, **`applique: false` TOUJOURS** (mode ombre pur).

→ **La famille a donc validé une direction déjà posée** : le sizing dynamique en mode ombre.
→ **Ce qui manque** : étendre le Kelly ombre à **ACE** (il ne couvre que Hulk aujourd'hui)
et l'intégrer au **chantier sizing** (veilleuse 22/08) — qui décidera de l'application
réelle avec 4 jours de données propres.

## 📋 Les conditions non négociables (juge — à respecter absolument)

1. **Sauvegarde immédiate** avant toute modification
2. **Installation en dry-run / lecture seule** — jamais d'activation live sur les fills
3. **Rollback en une commande** (réversibilité totale, loi maison)
4. **Ne pas toucher** : hub, pont cockpit, radar, paramètres live ALPHA/BETA hors sizing
5. **Activation seulement si** : la simulation montre une baisse de la ruine SANS dégrader le PnL

## ✅ Action immédiate décidée

Rien à installer aujourd'hui — le Kelly ombre Hulk est déjà en place, et le chantier
sizing ACE (veilleuse 22/08) reprendra la main à la fin du run 96h avec :
1. Le Monte Carlo sur 4 jours propres
2. L'extension du Kelly ombre à ACE (dry-run)
3. La décision d'application avec validation humaine

**Le goulot est identifié, la pépite est prête, la discipline est respectée.**
