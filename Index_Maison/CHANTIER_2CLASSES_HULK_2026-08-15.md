# CHANTIER — 2 classes de paires Hulk (core liquides vs small caps bag) — 15/08/2026

**Statut : APPLIQUÉ + TESTÉ** · hors genesis · réversible.

## Décision famille (gemini 70% / nvidia 72%)
GO-AVEC-RÉSERVE : thèse small caps fondée pour les projets à adoption institutionnelle vérifiable (pas tous les small caps). 2 classes de paires : A core liquides (règles actuelles) / B small caps bag (filtres assouplis, taille réduite, PAS de stop technique, plafond).

## Livré (paper_diprip.py + defaults.env)
- `BAG_PAIRS` (vide par défaut = comportement INCHANGÉ), `BAG_MAX_POSITIONS=5`, `BAG_POSITION_MULT=0.5`, `BAG_NO_TECH_STOP=1`.
- `is_bag(pair)` helper.
- `buy()` : plafond positions bag simultanées + taille ×0,5 pour les bags.
- `manage_open()` : pas de stop technique pour les bags (le bag tient ; stake-out 2× conservé).
- `vol_ok_for_entry()` : bag → `vol_ok_bag` (plus de blocage DEAD/DRY).
- `sense_ok()` : bag → spread large toléré.
- Heartbeat : `bag=N/5`.
- Premier bag proposé : **CCUSDT (Canton, vérifié)** — déclaré quand Christophe GO.

## Vérifications (vertes)
- `py_compile` OK · tests 5/5 : vide→inchangé · CCUSDT bag→True/XRP False · vol DEAD→vol_ok_bag · core→vol_ok_liq · sizing 20→10.

## Retour arrière (réversible)
- `git checkout -- hulk-mexc/scripts/paper_diprip.py` + supprimer les 4 lignes BAG_* de defaults.env.

## Suite (plan Christophe)
- **Couche de connaissance** (bookmarks/recherche → base par projet → injectée) — prochain chantier.

---

# AJOUT — Bag de départ (accélérer les tests, boucle bag dès jour 1) — 15/08/2026

**Statut : APPLIQUÉ + TESTÉ** · réversible.

## Décision (Christophe)
Correction : bag vide par défaut = impossible de tester la boucle bag (il faut des semaines pour qu'une position arme un bag). Lancement avec un bag de départ ~10$ → boucle bag (DCA, crash, rip) testable **dès le premier jour**.

## Livré (paper_diprip.py + defaults.env)
- `SEED_BAGS_ON=1`, `SEED_BAGS_USDT=10`, `SEED_BAGS_ENTRY_DD_PCT=8`, `SEED_BAGS_PAIRS=CCUSDT`.
- `seed_bags()` : bag maison flag `seed:true` (réalisme paper, ne pollue pas l'analyse du PnL réel) — même philosophie que le SEED positions existant.
- Entrée seedée ~8% **au-dessus** du prix actuel → bandeau DCA **actif immédiatement** (dd ≥ bag_slow_dd dès le 1er tick).
- `BAG_PAIRS=CCUSDT` activé en même temps (1er bag Classe B : règles d'exception testées d'un coup).
- Liquidité 20$ du budget trading **conservée** pour acheter (boucle buy testée en parallèle).

## Vérifications (vertes)
- `py_compile` OK · test fonctionnel : CCUSDT qty=94.42 entry=0.1059 seed=True · −1% → DCA non armé (dd=1%) · −10% → DCA armé (dd=10%) ✅

## Retour arrière (réversible)
- `git checkout -- hulk-mexc/scripts/paper_diprip.py` + supprimer les lignes SEED_BAGS_* et BAG_PAIRS de defaults.env.
