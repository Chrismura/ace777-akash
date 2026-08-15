# CHANTIER — Discipline continue Cortana + Ada (boucle quotidienne auto) — 15/08/2026

**Statut : APPLIQUÉ + TESTÉ + AUTOMATISÉ (launchd)** · hors genesis · réversible.

## Demande Christophe
Discipline journalière AUTOMATIQUE (même si on oublie, ça se nourrit non stop), visible si intervention nécessaire, pour Cortana ET Ada. Objectif affiché : 93% de justesse (« zéro faute »).

## Livré
1. **`Index_Maison/scripts/discipline_quotidienne.py`** (nouveau) — chaque jour :
   - Re-note **Cortana** (subprocess `score_justesse.py` → justesse_v2.json frais) — la boucle F1 se nourrit.
   - Note **Ada v1** (`justesse_ada_v1.json`) : zone (VERT/JAUNE/ROUGE/PRENDS_LA_PERTE) vs volatilité BTC sur les 24h suivantes (ROUGE→HIT si vol≥1.5% ou baisse ; VERT→HIT si calme<1%).
   - Écrit `thermo/DISCIPLINE_QUOTIDIENNE.md` (visibilité) + `DISCIPLINE_ALERT.md`.
   - **Alertes** (rc=3 si intervention) : Cortana <50% · Ada <60% · boucle affamée (>48h sans analyse) · baisse ≥5 pts vs hier.
2. **`Index_Maison/plists/com.ace777.discipline-quotidienne.plist`** → installé `~/Library/LaunchAgents/` + `launchctl load` ✅ (07:15, avant la cadence 8h30 → la note fraîche nourrit les analyses).

## Vérifications (vertes)
- `plutil -lint` OK · `py_compile` OK · run réel : Cortana re-notée 44% (37/84), **alerte déclenchée** (score<50% → rc=3), Ada 0/0 (journal trop récent, se remplit dès demain), rapport écrit.

## Notes honnêtes
- Ada = 0/0 aujourd'hui (ses entrées ont <24h de recul sur history.jsonl → l'accuracy se remplit au fil des jours).
- La métrique Ada v1 est une première approximation (zone vs volatilité BTC 24h) — à affiner quand elle aura des données.

## Retour arrière (réversible)
- `launchctl unload ~/Library/LaunchAgents/com.ace777.discipline-quotidienne.plist && rm ~/Library/LaunchAgents/com.ace777.discipline-quotidienne.plist`
- Supprimer `discipline_quotidienne.py` (et les fichiers de sortie).

## Prochain chantier (GO Christophe)
- **2 classes de paires Hulk** (core liquides vs small caps bag).
