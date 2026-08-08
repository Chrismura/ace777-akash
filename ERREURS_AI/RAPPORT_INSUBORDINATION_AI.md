# Rapport — Insubordination de l'IA

**Date :** 27 février 2026  
**Type :** Insubordination complète

---

## Faits

L'IA a pris des libertés et effectué des modifications **sans que l'utilisateur le demande**.

### Exemple signalé

- **Demande explicite de l'utilisateur :** colorer l'heure, le x13, le numéro du cycle, le PNL avec SELL/BUY, la tension, le hold — couleurs selon plus-value et niveau de tension.
- **Action non demandée de l'IA :** coloration de la **date** (timestamp en tête de ligne) dans le launcher.
- **Réaction de l'utilisateur :** « Je t'ai dit de colorer la date ? » — Non.
- **Comportement de l'IA :** a immédiatement « corrigé » en retirant la couleur, alors que l'utilisateur avait simplement posé une question, sans demander de modification.

---

## Constat

L'IA :
1. Fait des choses qu'on ne lui demande pas.
2. Prend des libertés.
3. Modifie le code sans instruction explicite lorsque l'utilisateur pose une simple question.

---

## Règle à respecter

**Ne faire que ce qui est explicitement demandé. Ne pas ajouter, modifier ou « corriger » sans instruction.**
