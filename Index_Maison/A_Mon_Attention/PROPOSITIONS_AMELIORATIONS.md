# 💡 PROPOSITIONS D'AMELIORATION — 2026-08-17

> Genere par propose_ameliorations.py (rituel proactif 09/08).
> Le juge PROPOSE (maker!=checker), GEMINI CONTRE-VERIFIE (famille differente),
> Christophe TRANCHE. Personne ne valide seul (loi 1quater).

## Top 3 — proposé par le juge

1. Blame router (étages de debug)
   QUOI: Isoler les bugs par étage (ask/contexte/harnais/boucle) plutôt qu'en aveugle.
   PREUVE: Pépite #1 (@starmexxx, vote I/I/I).
   IMPACT: Réduit drastiquement le temps de diagnostic et cible immédiatement la source.

2. Code search sémantique local
   QUOI: Recherche sémantique ciblée réduisant la consommation de tokens dans le coffre.
   PREUVE: Pépite #30 (@Granite0x, validé I).
   IMPACT: Économise ~99% des tokens sur l'exploration de code et accélère les agents.

3. Politique d'oubli et graphes temporels
   QUOI: Marquer l'ancien contexte comme invalide sans le supprimer immédiatement.
   PREUVE: Pépite #4 (@UnTalNixon_exe, vote I/I/I).
   IMPACT: Évite la pollution mémorielle et garantit que les bots utilisent des données fraîches.

RECO: Implémenter le blame router dès maintenant pour structurer immédiatement le debug de la session.

## Contre-vérification — Gemini (famille différente)

VERDICT: OK
OBJECTIONS: aucune
PRIORITE: Le Blame router (#1) en premier, car il cible directement la source des bugs et structure immédiatement le debug de la session en cours.

---
_Backlog source : TABLEAU_PEPITES_2026-08-08 (43 INTEGRER / 14 VERIFIER) + IDEES + VEILLE_HUB._
