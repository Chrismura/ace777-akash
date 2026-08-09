# JAUGE SPECS — documentation avant suppression (exigence famille Juge + Ultra, 09/08)

> **But :** conserver le SAVOIR de ce que la jauge surveillait avant sa suppression,
> pour que le superviseur unique (Phase 1) reprenne cette fonction sans rien réinventer.

## Ce qu'était la jauge
- **Script :** `~/ace777-test-day1/Index_Maison/scripts/jauge_energie.py` (créé 09/08)
- **Serveur HTTP :** `0.0.0.0:8898`, page HTML `JAUGE_ENERGIE`, **auto-refresh 30s**
- **Plists :** `com.ace777.jauge-energie.plist` (KeepAlive le matin → passée « à la demande » 13:04 → morte)
- **Copie de sauvegarde du plist :** `~/Backups/ace777/phase0_20260809_185734/com.ace777.jauge-energie.plist`

## Ce qu'elle surveillait (fonctions du script)
| Donnée | Source | Usage |
|---|---|---|
| **Santé hub** | `GET http://127.0.0.1:11435/health` (timeout 4s) | affiche OK/NOK + nb providers |
| **RAM libre** | `vm_stat` (Pages free + wired) | affiche Mo libres, seuil visuel 300 Mo |
| **Appels du jour** | `~/prise-ia/usage.jsonl` (compte les entrées du jour) | total + par provider |
| **Appels cloud du jour** | usage.jsonl `kind == 'cloud'` | compteur budget cloud |
| **Budget cloud/jour** | `~/prise-ia/routing.json` → `cloud_daily_budget` | affiche la limite |

## Seuils visuels (non bloquants — la jauge ALERTE, elle ne coupe pas)
- Hub : vert si `status == ok`, rouge sinon
- RAM libre : vert > 300 Mo, orange sinon
- Barres de répartition par provider (part des appels)

## Ce que le superviseur unique devra reprendre (Phase 1)
1. **Comptage par provider** : appels/jour depuis usage.jsonl → détecter les quotas morts (0 quota restant)
2. **Budget cloud** : total cloud/jour vs `cloud_daily_budget` → alerter à l'approche
3. **RAM** : surveillance libre (8 Go total, seuil d'alerte 300 Mo)
4. **Vue d'ensemble** : l'équivalent du cockpit Grok — 1 commande = tout voir

## Décision famille (unanimité)
- **Supprimer** la jauge (instable, déconnectée de la vision V2.0 de Grok) est le BON choix
- **Condition** : la fonction doit être reprise par le superviseur unique en Phase 1 — documentée ici pour ne rien perdre
- DeepSeek exige en plus : **script de surveillance minimale des quotas** dès la suppression (sinon rebrancher)

*Référence : scripts/jauge_energie.py (code complet, dans le repo + backup)*
