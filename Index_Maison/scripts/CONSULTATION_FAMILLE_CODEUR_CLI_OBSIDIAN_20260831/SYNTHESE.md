# SYNTHÈSE — Consultation famille (2) + codeur : chantier « Pont CLI Obsidian » (31/08)

**Demande Christophe** : « actione famille, que 2 plus codeur » — valider le plan
« pont CLI Obsidian » (remplacer le bricolage OUTBOX_OBSIDIAN par la CLI officielle,
avec fallback). Avis reçus : **gemini, juge (famille) + codeur = 3/3**.

## Verdict global
**Plan validé (8/10)** — « seule structure acceptable en production pour un système
multi-agents » (codeur). Mais **4 corrections unanimes avant implémentation** :

1. **File d'attente séquentielle obligatoire** (3/3) : la CLI parle à l'app par IPC ;
   Obsidian écrit en mono-thread. Deux IA qui écrivent en parallèle → timeout ou
   requête rejetée. Le pont doit **sérialiser** toutes les écritures (mutex/queue).
2. **Timeout strict 3s + read-back** (3/3) : tout subprocess CLI → `timeout=3.0` ;
   après create, relire et comparer le contenu (hash) — **ne jamais faire confiance
   à exit code 0** (succès possible avant flush disque complet).
3. **Fail-open absolu** (3/3) : l'écriture disque directe reste le **socle primaire**
   (le disque ne plante pas) ; la CLI n'est qu'une couche de **notification /
   indexation secondaire**. Obsidian indexera les fichiers au prochain refresh même
   sans CLI.
4. **Circuit breaker + audit** (juge + codeur) : 3 échecs CLI consécutifs → mode
   « disque pur » pendant 15 min (ne pas marteler une app morte) ; journaliser
   chaque écriture (statut CLI_SUCCESS / FALLBACK) dans un audit jsonl.

## Points tranchés
- **Ne PAS utiliser `obsidian search` pour valider** (gemini) : trop lent sur le gros
  vault → `obsidian read path=` ciblé suffit (si ça renvoie le contenu, c'est écrit).
- **Plugin Local REST API** (juge) : techniquement plus robuste (HTTPS asynchrone),
  mais dépend d'un plugin tiers → rejeté pour l'instant ; la CLI officielle est
  maintenue par Core. À réévaluer si la CLI montre ses limites.
- **URI scheme `obsidian://`** : à proscrire (pas de retour de succès, payload limité).
- **Write & Verify obligatoire** : cycle écriture → read-back → audit pour chaque note.

## Décision Buffy (chef scientifique)
J'implémente `obsidian_cli_bridge.py` avec : queue séquentielle + timeout 3s +
read-back hash + circuit breaker 3 échecs/15 min + fallback écriture disque directe
dans le vault + audit jsonl. **Additif et réversible** : rien n'est basculé tant que
le pont n'a pas tourné quelques jours en parallèle.
