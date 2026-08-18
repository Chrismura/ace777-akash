#!/usr/bin/env bash
# =============================================================================
# VEILLEUSE — Sizing / Ruine Monte Carlo (chantier 18/08)
#
# Tourne toutes les 6h (LaunchAgent com.ace777.veilleuse-sizing-monte-carlo).
# Quand la date d'analyse est atteinte (fin du run ACE 96h = 22/08), écrit un
# rappel bien visible dans la maison (VEILLE_SIZING_MONTE_CARLO.md).
# Ne lance RIEN — elle ne fait que rappeler (lecture seule).
# =============================================================================
set -uo pipefail

ROOT="/Users/christophe/ace777-test-day1"
MAISON="$ROOT/Index_Maison"
VEILLEUSE_FILE="$MAISON/VEILLE_SIZING_MONTE_CARLO.md"

# Date d'analyse : fin du run ACE 96h (22/08 09:41 UTC) → local +2h = 11:41
# Format comparé : YYYY-MM-DD
DATE_ANALYSE="2026-08-22"
NOW="$(date +%Y-%m-%d)"

if [[ "$NOW" < "$DATE_ANALYSE" ]]; then
    # Pas encore l'heure — on s'assure juste que la veilleuse existe (trace)
    if [ ! -f "$VEILLEUSE_FILE" ]; then
        cat > "$VEILLEUSE_FILE" <<'EOF'
# ⏰ VEILLEUSE — Sizing / Ruine Monte Carlo

> Rappel automatique (script veilleuse, toutes les 6h).
> **Date d'analyse : 2026-08-22** (fin du run ACE 96h).
> Chantier : `Index_Maison/CHANTIER_SIZING_MONTE_CARLO_2026-08-18.md`

**Pas encore l'heure** — la veilleuse est armée. Rien à faire.
EOF
    fi
    exit 0
fi

# Date atteinte → rappel visible
cat > "$VEILLEUSE_FILE" <<'EOF'
# ⏰ VEILLEUSE — Sizing / Ruine Monte Carlo — **DATE ATTEINTE**

> Rappel automatique (script veilleuse).

## 🚀 C'est le moment de trancher le sizing !

- **Chantier** : `Index_Maison/CHANTIER_SIZING_MONTE_CARLO_2026-08-18.md`
- **Constat 18/08** : même en période propre, **32,5 % de ruine** (creux ≥ -25 % du capital)
  → la taille des positions est grosse par rapport au gain réel par cycle (+0,0124 $).

## 📋 Prochaine étape
1. Relancer `python3 Index_Maison/scripts/monte_carlo_ace.py --depuis 2026-08-18`
   (4 jours propres de base scellée → statistique solide, pas juste 1 journée)
2. Comparer : les 4,4× tiennent-ils ? Ruine / DD médian / PnL par cycle ?
3. Rédiger l'analyse et soumettre la question du sizing à la famille AVANT toute activation
4. Verdict famille → GO Christophe → codeur si besoin → Release Receipt

---
> « On n'est pas pressés — on fait au mieux. » — Christophe
EOF

echo "⏰ VEILLEUSE: date d'analyse atteinte — rappel écrit."
exit 0
