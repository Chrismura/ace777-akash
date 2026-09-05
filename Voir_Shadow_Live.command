#!/usr/bin/env bash
# VISIONNER SHADOW MODE — double-clique sur ce fichier pour ouvrir le live coloré
# (lecture seule : ça n'arrête jamais le moteur. Ctrl+C ou ferme la fenêtre pour quitter.)
cd "$HOME/ace777-test-day1" || exit 1
clear
echo "Tableau de bord SHADOW MODE — Ctrl+C pour fermer l'affichage (le moteur continue)…"
sleep 1
python3 watch_shadow.py
echo ""
echo "Affichage fermé. Le moteur tourne toujours."
echo "Pour rouvrir : double-clique à nouveau sur ce fichier."
