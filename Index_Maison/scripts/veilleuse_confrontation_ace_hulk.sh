#!/usr/bin/env bash
# =============================================================================
# VEILLEUSE — Confrontation ACE ↔ Hulk
#
# Tourne toutes les 6h (LaunchAgent com.ace777.veilleuse-confrontation).
# Quand la date d'analyse est atteinte, écrit un rappel bien visible dans la
# maison (VEILLE_CONFRONTATION_ACE_HULK.md) pour qu'on ne l'oublie pas.
# Ne lance RIEN — elle ne fait que rappeler (lecture seule).
# =============================================================================
set -uo pipefail

ROOT="/Users/christophe/ace777-test-day1"
MAISON="$ROOT/Index_Maison"
VEILLEUSE_FILE="$MAISON/VEILLE_CONFRONTATION_ACE_HULK.md"

# Date d'analyse : fin du run ACE 96h (22/08 09:41 UTC) → local +2h = 11:41
# Format comparé : YYYY-MM-DD
DATE_ANALYSE="2026-08-22"
NOW="$(date +%Y-%m-%d)"

if [[ "$NOW" < "$DATE_ANALYSE" ]]; then
    # Pas encore l'heure — on s'assure juste que la veilleuse existe (trace)
    if [ ! -f "$VEILLEUSE_FILE" ]; then
        cat > "$VEILLEUSE_FILE" <<'EOF'
# ⏰ VEILLEUSE — Confrontation ACE ↔ Hulk

> Rappel automatique (script veilleuse, toutes les 6h).
> **Date d'analyse : 2026-08-22** (fin du run ACE 96h).
> Protocole : `Index_Maison/PROTOCOLE_CONFRONTATION_ACE_HULK_2026-08-18.md`

**Pas encore l'heure** — la veilleuse est armée. Rien à faire.
EOF
    fi
    exit 0
fi

# Date atteinte → rappel visible (et le protocole existe déjà)
cat > "$VEILLEUSE_FILE" <<'EOF'
# ⏰ VEILLEUSE — Confrontation ACE ↔ Hulk — **DATE ATTEINTE**

> Rappel automatique (script veilleuse).

## 🚀 C'est le moment de lancer l'analyse !

- **Protocole** : `Index_Maison/PROTOCOLE_CONFRONTATION_ACE_HULK_2026-08-18.md`
- **Données prêtes** :
  - Sonde Hulk : `hulk-mexc/runs/ASPIRATION_CALIB_20260816_214411.csv`
  - ACE : `runs/MASTER_VORTEX_V2_COLLAB_4H_*_X5.csv` (run 96h terminé)
- **Fenêtre synchronisée** : 18/08 09:41 → 22/08 09:41 UTC (96h de données communes)

## 📋 Prochaine étape
1. Lancer l'analyse de corrélation (KPI du protocole)
2. Rédiger `Index_Maison/CONFRONTATION_ACE_HULK_ANALYSE.md`
3. Soumettre toute proposition d'action à la famille AVANT activation

---
> « On n'est pas pressés — on fait au mieux. » — Christophe
EOF

echo "⏰ VEILLEUSE: date d'analyse atteinte — rappel écrit."
exit 0
