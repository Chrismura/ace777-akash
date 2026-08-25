# INTEGRATIONS HEBDOMADAIRES — 2026-08-25

> Genere par observatoire.py (correction famille 09/08).
> Regle : un provider integre auto n'est JAMAIS actif directement.
> Il passe 48h en observation (sondes), puis Christophe valide la liste
> chaque vendredi (GO hebdomadaire). Sans GO -> pas d'activation.

## ACTIVÉS AUJOURD'HUI (48h propres + GO hebdo)

| Provider | Modele | Detail | Etat |
|----------|--------|--------|------|
| obs-1786774656 | nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free | 4/5 | actif + sain (sondes OK) |
| obs-1786774667 | nvidia/nemotron-3.5-lightning:free | 4/5 | actif + sain (sondes OK) |

## RETIRÉS (rollback auto > 5% erreurs)

| Provider | Modele | Detail | Etat |
|----------|--------|--------|------|
| obs-1786688184 | cohere/north-mini-code:free | 100% | ROLLBACK auto (désactivé) |
| obs-1786774646 | nvidia/nemotron-3-nano-30b-a3b:free | 100% | ROLLBACK auto (désactivé) |
| obs-1786795252 | nvidia/nemotron-3.5-content-safety:free | 100% | ROLLBACK auto (désactivé) |
| obs-1787033767 | google/diffusiongemma-26b-a4b-it | 100% | ROLLBACK auto (désactivé) |
| obs-1787206650 | google/gemma-4-26b-a4b-it:free | 100% | ROLLBACK auto (désactivé) |
| obs-1787248844 | nvidia/nemotron-nano-9b-v2:free | 100% | ROLLBACK auto (désactivé) |
