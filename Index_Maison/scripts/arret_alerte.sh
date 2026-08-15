#!/usr/bin/env bash
# Raccourci d'arrêt d'urgence des alertes vocales ACE777.
# Crée STOP_ALERTE (global + local) et tue les process vocaux en cours.
# Usage : arret_alerte  (ou bash Index_Maison/scripts/arret_alerte.sh)

RACINE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "Arrêt d'urgence des alertes vocales..."

mkdir -p "$RACINE/data/alertes"
touch "$RACINE/STOP_ALERTE"
touch "$RACINE/data/alertes/STOP_ALERTE"

# Arrêt immédiat garanti : tue les boucles vocales (python) + les lecteurs audio
pkill -f "alerte_vocale.py" 2>/dev/null || true
killall edge_tts 2>/dev/null || true
killall say 2>/dev/null || true

# Nettoyage des fichiers d'arrêt (pour repartir propre)
rm -f "$RACINE/STOP_ALERTE" "$RACINE/data/alertes/STOP_ALERTE" 2>/dev/null || true

echo "Signal d'arrêt envoyé. Les boucles vocales vont s'interrompre."
