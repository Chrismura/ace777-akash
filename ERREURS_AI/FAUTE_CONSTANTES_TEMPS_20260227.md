# FAUTE GRAVE — Constantes de temps (2026-02-27)

## Erreur

**Modification des constantes de temps** : l'IA a appliqué `timeout=0.5` au lieu de respecter l'ordre impératif `timeout=0.2` (maximum 0.3).

## Règle — ORDRE IMPÉRATIF

**Interdiction de modifier les constantes de temps.**

Dans tout `requests.get()` pour Binance/ACE777 :
- `timeout=0.2` (ou maximum 0.3)
- `verify=False` (obligatoire pour passer le verrou LibreSSL Mac M1)

Sans discussion. C'est un ordre.

## Conséquence

Si timeout > 0.3 : sortie de la Base 16, latence excessive, comportement incohérent.

## Règle à respecter

Ne jamais modifier timeout ni retirer verify=False. Toujours : `requests.get(url, timeout=0.2, verify=False)` ou `timeout=0.3` au maximum.
