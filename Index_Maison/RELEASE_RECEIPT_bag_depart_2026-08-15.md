# RELEASE RECEIPT — Bag de départ Hulk (SEED_BAGS) — 2026-08-15

## 1. PROPRIÉTAIRE NOMINATIF
- Responsable : Buffy (superviseur) — implémentation codeur (code.ia)
- Validé par : Christophe (GO) + famille (2 classes : gemini 70% / nvidia 72%)
- Qui répond en cas de bug : Buffy

## 2. FRONTIÈRES DE TÂCHE
- Fait : bag seedé 10$ (CCUSDT, entry +8% → DCA armé jour 1, flag seed:true),
  boucle bag testable dès le 1er tick, BAG_PAIRS=CCUSDT activé (classe B).
- Ne fait PAS : ne touche pas au moteur ACE (genesis), ni aux positions seedées
  existantes (SEED_USDT=20 conservé), ni aux règles de la classe A.

## 3. GAPS / RISQUES CONNUS
- Limite : le bag seedé est du réalisme paper (virtuel, flag seed:true) — il ne
  compte pas dans l'analyse du PnL réel.
- Signal d'alerte : si le bag seedé déclenche DCA/ventes anormales (log BAG_*).

## 4. CLÉS & ACCÈS (révocabilité)
- Touche : paper_diprip.py (seed_bags()), config/defaults.env (SEED_BAGS_*, BAG_PAIRS).
- Désactivation : SEED_BAGS_ON=0 + vider BAG_PAIRS → retour au comportement d'avant.

## 5. TESTS VALIDÉS
- py_compile OK · test fonctionnel : CCUSDT qty=94.42 entry=0.1059 seed=True ·
  −1% → DCA non armé (dd=1%) · −10% → DCA armé (dd=10%) ✅
- Cas limite : comportement INCHANGÉ si BAG_PAIRS vide (régression testée 5/5).

## 6. PLAN DE REPRISE / ROLLBACK
- Si ça casse : git checkout -- hulk-mexc/scripts/paper_diprip.py + supprimer
  les lignes SEED_BAGS_* et BAG_PAIRS de defaults.env.
- Référence : Index_Maison/CHANTIER_2CLASSES_HULK_2026-08-15.md (section AJOUT)
- Point de retour : dernier commit avant le chantier.
