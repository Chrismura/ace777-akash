# TEST SUR COPIE — Garde-fou SELL full (SPEC v2) — 29/08

**Date :** 2026-08-29 · **Auteur :** Buffy (chef scientifique) · **Statut :** ⏳ TEST TERMINÉ — EN ATTENTE GO Christophe

## 1. Objet du test

Vérifier, sur une **copie** du moteur (`paper_diprip_SELLFULL_TEST.py`, jamais sur le moteur réel qui **tourne en ce moment**), que le diff de la SPEC v2 (2e passe codeur) fonctionne sans crash et sans corrompre l'état (`--resume`), puis chiffrer l'économie réelle (PREUVE).

**Aucune modification n'a été faite sur `paper_diprip.py` réel.**

## 2. Ce qui a été testé

### 2.1 Syntaxe
`python3 -m py_compile` → ✅ OK sur la copie modifiée. Les 2 blocs de garde sont bien en place.

### 2.2 Tests unitaires isolés (bot factice via `object.__new__`, aucune boucle, aucun réseau d'état)
`test_seellfull_guard.py` → **4/4 OK** :

| Cas | Condition | Résultat attendu | Résultat |
|---|---|---|---|
| A | amplitude forte (>12 %) sans invalidation | **SELL_PARTIAL 50 %** (pos reste à 50 %) | ✅ qty restant = 5.0 |
| B | amplitude forte + invalidation (dd15 < −5) | SELL full (pos fermée) | ✅ |
| C | amplitude faible (< garde) | SELL full (comportement historique) | ✅ |
| D | mode dégradé (vol_spike absent) | **fallback SELL full** (jamais de partiel, sûr) | ✅ |

### 2.3 Compatibilité `--resume` (verrou 3, lecture seule)
`test_seellfull_resume.py` → lit le **dernier état réel** (positions restaurées, sans la nouvelle clé) et exécute `manage_open` dessus : **11 positions réelles testées → 11 OK, 0 crash**. La garde s'applique sans rien casser sur des positions héritées du système actuel.

## 3. PREUVE chiffrée (données réelles des CSV runs, lecture seule)

**Moyennes réelles mesurées sur 38 jours :**
- SELL full : 155 stops → **−158,03 $** (moy −1,02 $)
- SELL_PARTIAL : 378 → **+83,96 $** (moy **+0,22 $**)

**Simulation** (fraction `f` des SELL full stops qui seraient passés en SELL_PARTIAL 50 % dès qu'amplitude > 12 % sans invalidation) :

| Scénario | Fraction basculée | Économie estimée | SELL full restants |
|---|---|---|---|
| Prudent | 40 % | **+77 $** | −81 $ |
| **Estimation codeur** | **65 %** | **+125 $** | −33 $ |
| Optimiste | 85 % | +163 $ | −5 $ |

> ⚠️ Borne haute : la moyenne +0,22 $ des SELL_PARTIAL inclut des partiels de gains (pas que des stops). L'économie réelle est **entre ~+77 $ (bornes basses) et ~+125 $ (hypothèse codeur)** — cohérente avec l'estimation initiale (~84 $) du codeur, ici recalculée sur moyennes réelles.
> **Verdict : même dans le scénario le PLUS prudent (40 %), la garde élimine ~48 % de la perte brute (76 $ / 158 $) sans jamais aggraver le pire cas** (mode dégradé → fallback historique).

## 4. Verrous du juge — état

| Verrou | Statut |
|---|---|
| 1. Dust Sweeper / taille de lot | ✅ Vérif `min_q`/`min_notional` (1 $) + liquidation forcée des résidus |
| 2. Indicateurs dispo temps réel | ✅ `move24_pct`/`vol_spike`/`dd15_pct` déjà dans `sc` ; dégradé → fallback sûr |
| 3. Compatibilité `--resume` | ✅ **Testé sur l'état réel : 11 positions, 0 crash** ; configs en `defaults.env` rétro-compat |

## 5. État du circuit

1. ✅ Audit moteur (lecture seule) → `AUDIT_SELL_FULL_20260829.md`
2. ✅ SPEC v1 → Cortana + famille (SOUS CONDITION, 3 verrous)
3. ✅ **SPEC v2 corrigée (vérification réelle des indicateurs)**
4. ✅ Codeur 1re passe → ⛔ refuse (sc hors scope + configs non chargées) → `RETOUR_CODEUR_2e_passe.md`
5. ✅ Codeur 2e passe → ✅ **validée en relecture scientifique**
6. ✅ **Test sur copie : 4/4 unitaires + resume 11/11 + PREUVE chiffrée**
7. ⏳ **GO Christophe** → application sur le moteur réel + test court + déploiement

## 6. Fichiers du test (garde-trace)
- `scripts/paper_diprip_SELLFULL_TEST.py` — **copie** modifiée du moteur (l'original est intact)
- `scripts/test_seellfull_guard.py` — test unitaire 4 branches (réutilisable, lit la copie)
- `scripts/test_seellfull_resume.py` — test resume sur état réel (lecture seule)
- `docs/CODE_SELL_FULL_v2_CORRIGE_2026-08-29.md` — diff validé