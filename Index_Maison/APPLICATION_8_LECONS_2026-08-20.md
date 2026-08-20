# 🔧 APPLICATION DES 8 LEÇONS — corrections faites le 20/08/2026

> **Contexte** : Christophe a validé l'audit et demandé d'appliquer les 8 leçons
> gravées ("pour que ça n'arrive plus"). Ce fichier trace CHAQUE leçon → sa
> correction → son état → sa vérification. Toutes les corrections respectent C1
> (genesis intangible : wrappers/molettes/scripts externes uniquement, jamais le
> champion).

---

## Leçon 1 — « Ton concept prime : creuser la mesure, pas condamner l'idée »
**Correction** : le détecteur blocs privatisés est réparé, pas jeté.
- Résolution : snapshot **120 s** au lieu de 600 s (`Index_Maison/plists/com.ace777.bloc-privatise.plist`
  + `~/Library/LaunchAgents/` — les deux, plist rechargée).
- Nouveau garde-fou dans `detecter_bloc_privatise.py` : si la fenêtre contient
  moins de `MIN_SNAPSHOTS=3` snapshots (démarrage/purge/coupure), le taux est
  marqué `taux_fantome=null` + `taux_non_fiable=true` — **fini les 100 % fantômes
  sur carnet vide**.
- Recalibration des seuils du Juge : À FAIRE sur le taux résiduel dense
  (0,5-8,3 % observé le 20/08) — pas sur l'ancien bruit (33,75 %).
**État** : ✅ fait + testé (run manuel : n_snapshots=8, taux fiable).

## Leçon 2 — « Jamais 'bruit' sans tester la résolution »
**Correction** : le test de résolution (60 s vs 10 min) est documenté dans
`ENQUETE_POUSSIERE_BLOCS_PRIVATISES_2026-08-20.md` (33,6 % → 8,3 % → 0,5-8,3 %).
Le détecteur tourne maintenant à la résolution fine.
**État** : ✅ fait (décision intégrée à la leçon 1).

## Leçon 3 — « Un garde-fou écrit ≠ un garde-fou actif »
**Correction** : la chaîne **VIGIE MARCHÉ** est ajoutée à `sante_index.py` (le
check des index) — elle vérifie :
1. process `vigie_live.py` vivant,
2. `journal_radar.log` frais (≤ 5 min),
3. plists de relance chargées : `superviseur-process` + `superviseur-core` +
   `vigie-live`.
→ Si l'un manque : ALERTE (le trou du 19/08 ne peut plus passer silencieux).
**État** : ✅ fait — `sante_index` = **7/7 chaînes OK** (testé).

## Leçon 4 — « Accuser un commit = lire son diff d'abord »
**Correction** : procédure gravée (règle de conduite) :
`git show <commit> -- <fichier>` AVANT tout verdict. Le cas S-10 (accusé à tort)
est documenté dans `ENQUETE_SCELLE_CHAMPION_2026-08-20.md` + la mémoire.
**État** : ✅ fait (documentaire).

## Leçon 5 — « Le filet STOP_MARKET est fragile : calibrer »
**Correction** : garde-fou dans `GO_VORTEX_V2.sh` (wrapper, C1 OK) :
- Si `ACE_STOP_MARKET_ENABLED=TRUE` et `ACE_STOP_MARKET_BPS < 20` → **lancement
  REFUSÉ** ("fausse sécurité") : le run du 19/08 activait le filet à 8 bps →
  Binance rejetait (-2021 Order would immediately trigger) → positions SANS filet.
- Activation propre documentée : `ACE_STOP_MARKET_ENABLED=TRUE ACE_STOP_MARKET_BPS=20`
  (0,20 % — filet anti-crash, pas un scalpel).
- **Bug connu -4116 (clientAlgoId dupliqué après relance)** : interne au genesis →
  C1 interdit de le corriger directement. Nécessite un patch champion encadré
  (backup + re-scellage + GO famille) — chantier à ouvrir.
**État** : ✅ fait + testé (3/3 cas : désactivé OK, 8 bps refusé, 20 bps OK).

## Leçon 6 — « Pas de patch en plein run avec relances auto »
**Correction** : verrou md5 dans `launch_vortex_v2_collab_4h_binance.sh` (la boucle
de relance) :
- Au 1er lancement : md5 du champion mémorisé (`/tmp/ace777_champion_md5_<tag>.lock`).
- À CHAQUE relance : si le champion disque ≠ verrou → **relance REFUSÉE** avec
  message clair (le patch S-10 du 19/08 est entré en service à mi-course via les
  relances auto → c'est interdit maintenant).
**État** : ✅ fait + testé (verrou créé, inchangé → OK, modifié → ⛔ refus).

## Leçon 7 — « Le vrai trou était l'infra, pas les indicateurs »
**Correction** : la couche macro/news EXISTE déjà dans `vigie_live.py`
(RSS cointelegraph + google news, KEYWORDS fed/crash/guerre, alerte + voix,
cooldown 30 min) — le problème était que la **vigie ne tournait pas**.
→ Vigie relancée (PID 38557) + relance automatique branchée (superviseur-process,
PID 42482) + surveillée par sante_index (leçon 3).
**État** : ✅ fait.

## Leçon 8 — « Ce qui déconne est souvent débranché, pas mal conçu »
**Correction** : audit plists critiques (leçon 8) → **`superviseur-core` était
ABSENTE de launchd** (plist écrite le 10/08, jamais chargée) → rechargée
(PID 48899). L'audit complet des 9 plists critiques : ✅ toutes chargées
(vigie-live, superviseur-process, superviseur-core, bloc-privatise, macro-tempete,
cpfp, whales, pont-onchain, sante-index).
**État** : ✅ fait.

---

## Récapitulatif des fichiers modifiés (20/08, 2ᵉ passe)
| Fichier | Leçon | Changement |
|---|---|---|
| `Index_Maison/scripts/detecter_bloc_privatise.py` | 1+2 | MIN_SNAPSHOTS, taux null si non fiable |
| `Index_Maison/plists/com.ace777.bloc-privatise.plist` | 1+2 | StartInterval 600 → 120 |
| `Index_Maison/scripts/sante_index.py` | 3+8 | Chaîne VIGIE MARCHÉ + 3 plists de relance |
| `GO_VORTEX_V2.sh` | 5 | Garde-fou filet (BPS min 20) |
| `launch_vortex_v2_collab_4h_binance.sh` | 6 | Verrou md5 anti-patch-en-plein-run |
| `~/Library/LaunchAgents/com.ace777.superviseur-core.plist` | 8 | Chargée (était absente) |
| `Index_Maison/APPLICATION_8_LECONS_2026-08-20.md` | — | Ce fichier (trace) |

## À faire (GO Christophe)
- [ ] Recalibrer les seuils du Juge blocs privatisés sur le taux résiduel dense (0,5-8,3 %)
- [ ] Patch champion encadré pour -4116 (clientAlgoId unique après relance) — procédure C1
- [ ] Décision 23/08 : CPFP/ADA (activer ou jeter) — checklist dans `DECISION_CPFP_ADA_2026-08-20.md`

---
*Appliqué et vérifié par Buffy le 20/08/2026 — suite du GO Christophe (8 leçons).*
