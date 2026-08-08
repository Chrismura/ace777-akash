# PLAN COUCHES ENGLE B1→B3 — setups évolutifs (réversibles)

**Date :** 2026-07-19  
**Base intouchable :** usine NUAGE V2.2.1 (`cksum 812033996 22672`) + champion `37fca367` + `GO_USINE_NUAGE.sh`  
**Règle d’or :** tout changement = couche **OFF par défaut** → OFF = comportement usine byte-identique.

---

## Architecture

```
Champion 37fca367          ← JAMAIS modifié sans GO moteur
Usine V2.2.1 + wait-timer  ← socle (coffre 20260718)
    ↓
B0 déjà livré              ← A1 telemetry, A2 IRM lecture seule, hygiène Mac
    ↓
B1 JOURNAL (ce chantier)   ← post-run / à la demande — zéro impact live
    ↓
B2 ADAPT LOG (ce chantier) ← ENGLE_ADAPT=0 défaut ; =log → posture écrite, pas SKIP
    ↓
B3 un knobs (plus tard)    ← un seul seuil env, A/B 4h, sinon rollback
```

---

## B1 — Journal Engle

| | |
|--|--|
| Script | `scripts/engle_journal.rb` |
| Sortie | `engle/journal/ENGLE_JOURNAL_<TAG>_<ts>.md` + `ENGLE_JOURNAL_DERNIER.md` |
| Déclencheur | `update_state_md.sh` (après PnL) ou manuel |
| Impact moteur | **Aucun** |
| Rollback | ne plus appeler le script / ignorer `engle/journal/` |

Contenu : régimes IRM session + top SKIP BETA/ALPHA + fills/PnL + posture recommandée (conseil seulement).

---

## B2 — Adapt log-only

| | |
|--|--|
| Script | `scripts/engle_adapt.rb` |
| Env | `ENGLE_ADAPT=0` (défaut) · `ENGLE_ADAPT=log` |
| Boot | ligne dans `GO_USINE_NUAGE.sh` après IRM |
| Fichier posture | `runs/engle_adapt_posture.json` (si log) |
| Impact moteur | **Aucun** — pas de SKIP, pas de knobs appliqués |
| Rollback | `unset ENGLE_ADAPT` ou `ENGLE_ADAPT=0` |

Postures (conseil) :
- **COMPRESSE** → `WAIT_COLD` — ne pas assouplir ; calme = piège fills
- **TRANSITOIRE** → `WATCH` — observer, usine inchangée
- **CLUSTER** → `HUNT_WINDOW` — fenêtre chasse théorique (B3 plus tard)

---

## B3 — Un levier (pas encore codé)

Candidats (un seul par campagne A/B) :
1. Gate stase âge max (autour de 800 ms) — env wrapper seulement
2. Soft anomaly — env seulement
3. **Interdit en B3 :** baisser momentum en COMPRESSE, INDEX SYNC ON, touch genesis

Rollback B3 : retirer env + relancer `GO_USINE` (restaure snapshot usine).

---

## Commandes utiles (marché calme OK)

```bash
# Journal maintenant (run en cours ou fini)
cd /Users/christophe/ace777-test-day1
ruby scripts/engle_journal.rb

# Posture log (sans toucher moteur)
ENGLE_ADAPT=log ruby scripts/engle_adapt.rb boot

# Usine pure (défaut)
ENGLE_ADAPT=0 ruby scripts/engle_adapt.rb boot
```

---

## Interdits

- Modifier `genesis_manifest.txt` / masses / leviers sans GO explicite
- Brancher un SKIP live sur IRM sans GO Christophe
- Empiler plusieurs knobs B3 d’un coup
