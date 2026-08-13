# 📌 POINT DE REPRISE — DERNIER (à lire en premier)

> **Pour la prochaine session (Buffy ou autre IA)** : lis CE fichier d'abord.
> 30 secondes. Pas plus. Le détail est dans les liens, pas ici.

---

## 1. Ce qui s'est passé (13/08)

**Coupure batterie → position orpheline → diagnostiqué et réparé.**

- La coupure (nuit 12→13/08) a laissé une position **BTCUSDT SHORT -0.0184 (lev 13)** sur le testnet.
- Elle bloquait la marge → `Margin is insufficient` (-2019) → `Abort leverage error` → **ALPHA exit 1 en boucle**, duo cassé, runs morts en silence.
- Fix complet (validé par Christophe, GO 1→5) :
  1. Arrêt propre (run + watchdogs + master zombie)
  2. **Fermeture de la position orpheline** (API hedge, reduceOnly)
  3. Nettoyage fichiers de run corrompus
  4. **Re-scellement du champion** `98c80b5c` = `9fe9f105` (sans barrière) + FIX-SCOUT, vérifié par diff — c'est le champion authentique du 10/07 restauré le 12/08 23:29Z + patch
  5. **Vérif md5 champion intégrée au preflight** (C1 mécanique) + **garde-fou compte à plat** (positionRisk ≠ 0 → refus de lancer, C8)
- **Run 8h relancé 08:44Z** (setup d'hier : GEMINI_TEST x13 fixe, profil collab), fin ~16:44Z — sain, 0 erreur de marge.

## 2. Ce qui tourne MAINTENANT (état à vérifier en premier)

| Quoi | État attendu |
|---|---|
| **Run ACE 8h** | lancé 08:44Z, fin ~16:44Z — vérifier `tail runs/MASTER_VORTEX_V2_COLLAB_4H_LIVE_COLOR.log` |
| **Champion** | `genesis_manifest.txt` md5 = **98c80b5cf71db06697533aa48c5fd335** (scellé) |
| **Pont hub** | `curl http://127.0.0.1:11439/api/tags` → répond |
| **Hub** | `curl http://127.0.0.1:11435/health` → `status ok` |
| **Hulk paper** | `paper_diprip.py` (PID détaché) — vérifier `pgrep -f paper_diprip` |

## 3. Ce qui reste à faire (par ordre)

1. **📊 Bilan du run 8h** (après ~16:44Z) : `runs/BILAN_PATCHE_8H_20260813.md` ou PnL des CSV → valider le FIX-SCOUT (revenge conditionné au rôle SCOUT)
2. **🐟 MiroFish (membre oublié)** : en PAUSE budgétaire depuis le 10/08, clé ZEP posée → réactivation = **décision collective** + `launchctl load` (à la demande seulement)
3. **💰 Budget cloud** : 480/jour, compteurs à surveiller (dépassé 522/480 le 12/08 → bascule gemini tient)
4. **Hulk** : plist `com.ace777.hulk-watchdog` manque `AbandonProcessGroup=true` → paper/veille relancés par launchd meurent en boucle. Fix proposé : ajouter la clé au plist (en attente).

## 4. Les commandes clés

```bash
# Gate hub = LE lanceur (pas GO_USINE qui a le gate OFF)
cd ~/ace777-test-day1 && caffeinate -dims ./GO_VORTEX_V2.sh 04:00:00

# Vérifier le preflight (champion + compte à plat) AVANT tout lancement
cd ~/ace777-test-day1 && ./scripts/preflight_ace777.sh

# Vérifier qu'il n'y a pas de position orpheline (coupure ?)
# → le preflight le fait, sinon : source ~/.binance_testnet.env + positionRisk

# Arrêt complet
cd ~/ace777-test-day1 && ./stop_ace777.sh
```

## 5. Où trouver le détail (seulement si besoin)

- **Enquête forensique moteurs** : `AUDIT_MOTEURS_CURSOR.md` (le 12/08 21:49Z)
- **Index des commandes** : `Index_Maison/INDEX_COMMANDES.md`
- **Journal du jour** : `Index_Maison/Journal_2026-08-13.md`
- **Mémoire collab** : `Index_Maison/MEMOIRE_COLLAB.md` (les traces d'interventions)
- **Molette/setup** : `Index_Maison/JOURNAL_MOLETTES_SETUP.md`

---
*Gravé le 13/08 ~10:45 par Buffy. Règle : ce fichier est écrasé à chaque fin de
session — il reflète TOUJOURS le dernier état.*
