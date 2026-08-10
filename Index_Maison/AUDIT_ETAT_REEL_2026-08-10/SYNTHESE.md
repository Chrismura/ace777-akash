# ⚖️ AUDIT FAMILLE — ÉTAT RÉEL DU SYSTÈME — 10/08/2026

Leçon Christophe : « pourquoi le JUGE ne l'a pas vu ? pas normal, on est en brut » → on soumet le CODE mais pas le DISQUE. Ce dossier soumet l'ÉTAT RÉEL (plists disque, configs chargées, ce qui se lancerait au reboot).

| Membre | Verdict | Réserves |
|---|---|---|
| **GEMINI** | ✅ **GO** sans réserve | « État parfaitement maîtrisé, stérile de tout risque de lancement intempestif au reboot. » Règle ÉTAT RÉEL : « juste, indispensable et adoptée. » |
| **JUGE** | ✅ **GO AVEC RÉSERVES** (1) | Réserve : 23 plists sur disque → **RÉFUTÉE par preuve** : identiques au backup étape 1 = services existants normaux, zéro ajout |
| **DEEPSEEK** | ✅ **GO AVEC RÉSERVES** (2) | R1 superviseur non surveillé (acceptable en fusion) · R2 anomalies inventaire (expliquées : PID - = lancés sur demande) |
| **ULTRA** | ✅ **GO AVEC RÉSERVES** (4) | R1 processus fantôme superviseur → **corrigé (nettoyé)** · R2 inventaire obsolète → **relancé** · R3 preuve backup → **fournie** · R4 règle ÉTAT RÉEL enrichie |

## Réserves → réponses

1. **JUGE : 23 plists sur disque** → preuve par basename : `diff` IDENTIQUE au backup étape 1 → ce sont les services existants normaux (hub, cockpit, superviseur...), **zéro ajout non validé**.
2. **ULTRA R1 : processus fantôme** → détecté (PID 36579, reste de test) → **tué** ✅ · launchd superviseur-core = not running + StartInterval 900 → relancé automatiquement (comportement original) ✅
3. **ULTRA R3 : preuve réversibilité** → backup 23 plists + checksums (SHA-256 superviseur-core fourni) ✅
4. **ULTRA R4 : règle ÉTAT RÉEL enrichie** → ajout de : launchctl print par service, hash SHA-256 des scripts, WatchPaths/QueueDirectories des plists v2, comparaison disque vs backup.

## Décisions validées par la famille (4/4)
1. ✅ Étape 2 préparée mais PAS activée
2. ✅ Plists v2 rangés dans PRETS_ETAPE2 (hors LaunchAgents) → **rien ne se lance au reboot**
3. ✅ Activation = étape séparée, uniquement après fin de fusion + GO Christophe
4. ✅ Règle « ÉTAT RÉEL » obligatoire dans chaque dossier famille

## État final
- Disque = état d'origine (23 plists, identique au backup étape 1)
- Watchdog absent de LaunchAgents (rangé dans PRETS_ETAPE2)
- Hub 9 providers OK · aucun processus fantôme · tout réversible
