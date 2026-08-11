#!/usr/bin/env python3
from pathlib import Path
from datetime import datetime, timezone

vault = Path.home() / "Documents" / "Obsidian_ACE777"
text = f"""# Où est quoi — le garage

Mis à jour : {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%MZ')}

## Dans Obsidian (oui)
Notes, décisions, agora, Index, Swarm (md), Cahier, coutumes.
**Coffre unique :** Documents/Obsidian_ACE777

| Note | Rôle |
|------|------|
| [[AGORA]] | Entrée |
| [[COUTUMES_AGORA]] | Règles |
| [[OU_EST_QUOI]] | Cette carte |
| [[00_PLAN_RAPATRIEMENT]] | Plan |
| [[Swarm_Bus/09_MEMOIRE_COLLAB]] | Journal |
| [[Index_Maison/01_TABLEAU_VIVANT]] | Améliorations |

## Hors Obsidian (non — volontaire)
| Quoi | Où |
|------|-----|
| Code vocal | ~/crypto-voice-assistant-core/ et ~/Assistant_Vocal_HORS_VAULT/ |
| Archives lourdes | ~/Obsidian_BACKUPS_HORS_VAULT/ |
| ACE / Hulk + runs | ~/ace777-test-day1/ |
| Secrets / builds | .env et target/ hors coffre |

## Pourquoi pas tout dans Obsidian ?
**Oui, tu as bien compris.** Obsidian = notes / collab. Pas le code, pas les builds, pas les fills bruts.
Sinon le Mac 8 Go plante (écran noir).

## Avant un test
1. Rien qui tourne sans GO
2. Lire COUTUMES_AGORA si nouvel agent
3. Vault léger (notes md)
"""
(vault / "OU_EST_QUOI.md").write_text(text, encoding="utf-8")
print("OK", vault / "OU_EST_QUOI.md", len(text))
