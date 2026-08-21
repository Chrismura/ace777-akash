# ENQUÊTE — VIGIE MARCHÉ MORTE + SYSTÈMES DE RELANCE (20/08/2026)

> **Contexte** : Christophe a demandé (à juste titre) : "il y aurait dû y avoir
> plusieurs systèmes de relance, j'ai demandé plein de checks des index pour pas
> que ça arrive". Vérité établie : **les systèmes existaient mais n'étaient pas
> chargés**, et un seul script (lancé manuellement) relançait la vigie marché.

---

## Chronologie factuelle

| Moment | Événement |
|---|---|
| 19/08 12:10 UTC (14:10 locale) | **`journal_radar.log` s'arrête** → la vigie marché (`vigie_live.py`) est morte |
| 19/08 14:09:12 locale | **`superviseur.sh` meurt** (dernière ligne : `vérif | hub:OK | vigie:OK | cockpit:OK`) |
| 19/08 13:13→20:57 UTC | Run `MASTER_VORTEX_V2_COLLAB_4H` tourne pendant ce temps (−48,66 $) |
| 19/08 15:43 locale | Commit S-10 (correctif frais NET) — **ne touche pas aux stops** (vérifié : 0 ligne) |
| 20/08 (aujourd'hui) | Rebranchements effectués (ci-dessous) |

## Pourquoi rien n'a relancé la vigie

1. **`superviseur.sh`** = le SEUL script avec le module relance vigie marché
   (vérifie `journal_radar.log` heartbeat ≤ 180 s → `restart_process vigie`).
   → Lancé **manuellement** (log : `Superviseur démarré (PID 59478)` le 19/08 03:44).
   → **Mort le 19/08 14:09:12** (dernière ligne log), probablement tué par la
   pression mémoire (le run ACE tournait, RAM déjà critique 136 Mo au checkup 14/08).
   → **Personne ne l'a relancé** car sa plist launchd n'était PAS chargée.

2. **`com.ace777.superviseur-process.plist`** (qui lance `superviseur.sh`) :
   existait sur disque mais **N'ÉTAIT PAS CHARGÉE** dans launchctl.

3. **`com.ace777.superviseur.plist`** (chargée) lance **`superviseur_auto.py`**
   (cycle IA décisionnel) — PAS `superviseur.sh`. Elle ne relance pas la vigie.

4. **`superviseur_core.sh`** (launchd, KeepAlive) vérifie la **vigie SÉCURITÉ**
   (`vigie.sh` : permissions/persistance), **PAS** la vigie marché (`vigie_live.py`).

5. **`sante_index.py`** (le "check des index" demandé par Christophe, 6 chaînes :
   baleines, hulk, live, cpfp, sécurité, saison) → **ZÉRO référence à la vigie
   marché** (`grep vigie_live` = 0). Le radar n'était surveillé par AUCUNE chaîne.

**Conclusion : le radar était couvert par exactement un seul processus, lancé à la
main, sans garde-fou. C'est le trou dans le filet.**

## Réparations faites (20/08)

| Action | État |
|---|---|
| Recharger `com.ace777.vigie-live` (plist existait, non chargée) | ✅ PID 38557, journal radar écrit à nouveau |
| Charger `com.ace777.superviseur-process` (relanceur vigie marché via launchd) | ✅ PID 42482, log superviseur actif |
| Vérifier hub (`:11435`) | ✅ OK, 20 providers |

## Ce qui reste à faire (GO Christophe)

1. **Ajouter la chaîne VIGIE MARCHÉ à `sante_index.py`** : `vigie_live.py` vivant
   + `journal_radar.log` frais (≤ 5 min) → sinon ALERTE. C'est le "check des index"
   que tu avais demandé et qui manquait.
2. **Rétablir le garde-fou anti-doublon** : la plist `vigie-live` a `KeepAlive=true`
   → si le superviseur relance aussi, risque de doublons (leçon 16/08 : 13 vigies
   en 7 h). Arbitrer : vigie sous launchd KeepAlive OU sous superviseur, pas les deux.
3. **Enquêter le kill de 14:09** : probablement OOM (RAM 8 Go, run ACE + hub + vigie
   + cockpit + superviseur simultanés). Voir `chantier RAM` / priorisation.

## Fichiers consultés
- `Index_Maison/scripts/superviseur.sh` (module relance vigie + heartbeat)
- `Index_Maison/scripts/superviseur_core.sh` (vigie SÉCURITÉ, pas marché)
- `Index_Maison/scripts/superviseur_auto.py` (cycle IA, pas de relance vigie)
- `Index_Maison/scripts/sante_index.py` (6 chaînes, 0 vigie marché)
- `Index_Maison/scripts/superviseur.log` (mort à 14:09:12 le 19/08)
- `~/Library/LaunchAgents/com.ace777.{vigie-live,superviseur-process,superviseur,superviseur-core}.plist`

---
*Écrit par Buffy le 20/08/2026 — suite de l'audit en profondeur (demande Christophe).*
