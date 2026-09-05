#!/usr/bin/env bash
# VISION MOTEUR — double-clique pour voir CE QUE LE BOT CALCULE en direct
# (H, slots, trailing, distances) — lecture seule, le moteur n'est jamais touché.
# Ctrl+C ou ferme la fenêtre pour quitter l'affichage.
cd "$HOME/ace777-test-day1" || exit 1
clear
echo "VISION MOTEUR — Ctrl+C pour fermer l'affichage (le moteur continue)…"
sleep 1
python3 shadow_vision.py
echo ""
echo "Affichage fermé. Le moteur tourne toujours."
