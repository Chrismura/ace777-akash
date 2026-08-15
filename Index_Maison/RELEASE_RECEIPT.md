# RELEASE RECEIPT — 6 points (ACE777)

**Origine** : signet X N°30 @nykdotdev (« 10 tests verts ne suffisent pas — il manque les garde-fous production ») + N°31 (@nykdotdev, « trou de responsabilité » des systèmes multi-agents). Validé famille (gemini 85% / nvidia 72%, GO-AVEC-RÉSERVE) le 15/08/2026.
**Principe** : chaque déploiement/chantier ACE777 est livré avec un reçu signé — **zéro déploiement orphelin, zéro agent sans propriétaire, reprise rapide si bug**.

**Règle d'or** : pas de « 10 tests verts » comme seule validation. Un chantier n'est **terminé** que quand son Release Receipt est rempli et relu (par le superviseur, et par la famille pour tout changement majeur).

---

## 📋 LE REÇU (template — à remplir pour chaque chantier)

```
# RELEASE RECEIPT — <nom du chantier> — <date>

## 1. PROPRIÉTAIRE NOMINATIF
- Responsable de ce déploiement : <Buffy | codeur | qui>
- Validé par : <famille : gemini/nvidia… si majeur | superviseur si mineur>
- Qui répond en cas de bug : <nom précis — jamais « tout le monde »>

## 2. FRONTIÈRES DE TÂCHE
- Ce que CE chantier fait : <1-2 lignes>
- Ce qu'il NE fait PAS (hors périmètre assumé) : <explicite — évite le glissement>

## 3. GAPS / RISQUES CONNUS
- Limites connues non résolues : <honnête — ce qu'on accepte de ne pas couvrir>
- Signal d'alerte associé : <quoi surveiller pour savoir que ça dérape>

## 4. CLÉS & ACCÈS (révocabilité)
- Ce que ce chantier touche : <fichiers, configs, process, launchd…>
- Comment le désactiver SANS le casser : <commande/flag/switch — réversible ?>

## 5. TESTS VALIDÉS (preuve réelle, pas que des tests verts)
- <chaque vérification faite + résultat : py_compile, tests N/N, smoke, réel…>
- <le cas limite le plus dangereux testé et son résultat>

## 6. PLAN DE REPRISE / ROLLBACK
- Si ça casse : <la 1re action exacte — git checkout ? touch STOP ? flag ?>
- Document de référence : <chantier .md, spec, mémoire — lien>
- Point de retour : <commit/date — où revenir>
```

---

## ✅ EXEMPLE REMPLI — chantier « Bag de départ Hulk » (15/08/2026)

```
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
- Point de retour : dernier commit avant le chantier (77cad5da pour la veille).
```

---

## 🔁 MODE D'EMPLOI (pour tous les acteurs)

1. **Avant de lancer** un chantier : garder les 6 points en tête (surtout 4 et 6 : révocabilité).
2. **À la livraison** : remplir le reçu — c'est la **condition de « chantier terminé »**.
3. **Changement majeur** (stratégie, moteur, architecture) : reçu + passage famille (comme aujourd'hui).
4. **Bug post-déploiement** : le reçu donne immédiatement le propriétaire, le plan de reprise, le point de retour — **plus jamais de « qui a fait ça ? »**.
5. Les reçus remplis s'ajoutent en fin de chaque `CHANTIER_*.md` (ou fichier dédié `RELEASE_RECEIPT_<nom>.md`).

**Contre-exemple qui a motivé ce reçu** : mort silencieuse rc=1 du 14/08 — un fix appliqué sans reçu clair a nécessité une enquête forensique complète pour trouver qui/quoi/comment revenir. Avec ce reçu, 2 minutes suffisent.
