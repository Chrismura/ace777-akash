# RÉPONSE HUB (task code.ia · via Google Gemini) — 2026-08-12T22:48:52

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
SYSTEME ACE777 — cycles_terminal.py (Jumeau Cockpit Terminal)
================================================================================
Auteur : Buffy (superviseur) · Codeur : hub `code.ia`
Date   : 2026-08-12

Description :
Instrument de lecture seule pour le flux de cycles ALPHA/BETA dans le terminal.
Re-peint le flux en direct (tail -f) ou en mode replay avec les couleurs exactes
du cockpit web. Fournit un résumé par pouls et un bilan de session à la sortie.

Usage :
    python3 cycles_terminal.py
    python3 cycles_terminal.py --replay <fichier> [--vitesse 0.05]
    python3 cycles_terminal.py --tail 100 --no-pulse
    python3 cycles_terminal.py --json
================================================================================
"""

import os
import re
import sys
import glob
import json
import time
import argparse
from datetime import datetime
from typing import Optional, Dict, List, Tuple

# ---------------------------------------------------------------------------
# PALETTE DE COULEURS ANSI TRUECOLOR (Exacte spec cockpit)
# ---------------------------------------------------------------------------
C_RESET = "\x1b[0m"

# Préfixes et corps
C_ALPHA_PRE = "\x1b[38;2;240;160;32m"      # Ambre #f0a020
C_ALPHA_BODY = "\x1b[38;2;240;160;32m"     # Ambre atténué
C_BETA_PRE = "\x1b[38;2;94;231;255m"       # Cyan #5ee7ff
C_BETA_BODY = "\x1b[38;2;94;231;255m"      # Cyan

# États et signaux
C_SKIP = "\x1b[38;2;138;122;85m"           # Gris #8a7a55
C_FILL = "\x1b[38;2;124;255;107m"          # Vert acide #7CFF6B
C_PNL_POS = "\x1b[38;2;124;255;107m"       # Vert acide
C_PNL_NEG = "\x1b[38;2;255;77;77m"         # Rouge #ff4d4d
C_CONF_LOW = "\x1b[38;2;255;77;77m"        # Rouge (alerte < 0.1)
C_TIMESTAMP = "\x1b[38;2;157;255;122m"     # Cyan clair / vert
C_HEADER = "\x1b[38;2;124;255;107m"        # En-têtes de run (vert)

# Regex utilitaires
ANSI_ESCAPE_RE = re.compile(r'\x1b\[[0-9;]*m')
CONF_RE = re.compile(r'conf=([0-9.]+)')
PNL_RE = re.compile(r'pnl=([-\d.]+)')
CYCLE_RE = re.compile(r'#(\d+)')
TS_RE = re.compile(r'(\d{2}:\d{2}:\d{2})')


class SessionStats:
    """Collecte les statistiques pour le pouls et le bilan de fin."""
    def __init__(self) -> None:
        self.alpha_cycles: int = 0
        self.beta_cycles: int = 0
        self.alpha_fills: int = 0
        self.beta_fills: int = 0
        self.alpha_skips: int = 0
        self.beta_skips: int = 0
        self.alpha_pnl: float = 0.0
        self.beta_pnl: float = 0.0
        self.lines_read: int = 0


def trouver_dernier_log() -> str:
    """Trouve le fichier *_LIVE_COLOR.log le plus récent dans le dossier des runs."""
    dossier_runs = os.path.expanduser("~/ace777-test-day1/runs")
    if not os.path.exists(dossier_runs):
        print(f"[ERREUR] Le dossier {dossier_runs} n'existe pas.", file=sys.stderr)
        sys.exit(1)
    
    pattern = os.path.join(dossier_runs, "*_LIVE_COLOR.log")
    fichiers = glob.glob(pattern)
    
    if not fichiers:
        print(f"[ERREUR] Aucun fichier _LIVE_COLOR.log trouvé dans {dossier_runs}", file=sys.stderr)
        sys.exit(1)
        
    dernier = max(fichiers, key=os.path.getmtime)
    return dernier


def nettoyer_ansi(ligne: str) -> str:
    """Retire tous les codes ANSI existants de la ligne source."""
    return ANSI_ESCAPE_RE.sub('', ligne)


def coloriser_ligne(ligne_brute: str, stats: SessionStats, mode_json: bool) -> Optional[str]:
    """Analyse une ligne brute, extrait les métriques, et applique la palette ANSI."""
    ligne_propre = nettoyer_ansi(ligne_brute).strip()
    if not ligne_propre:
        return None

    stats.lines_read += 1

    # Détection du bot source
    is_alpha = "ALPHA" in ligne_propre
    is_beta = "BETA" in ligne_propre

    # Extraction d'éléments clés pour l'audit JSON éventuel
    ts_match = TS_RE.search(ligne_propre)
    ts_str = ts_match.group(1) if ts_match else "00:00:00"
    
    bot_nom = "ALPHA" if is_alpha else ("BETA" if is_beta else "SYSTEM")
    
    # Mode JSON strict demandé
    if mode_json:
        data = {
            "ts": ts_str,
            "bot": bot_nom,
            "raw": ligne_propre[:100]
        }
        return json.dumps(data)

    # Tronquer le message si trop long pour 80-110 colonnes
    if len(ligne_propre) > 100:
        ligne_propre = ligne_propre[:97] + "…"

    # Colorisation selon le contenu
    # 1. En-tête de config
    if "---" in ligne_propre or "ACE777" in ligne_propre or "RUN" in ligne_propre:
        return f"{C_HEADER}{ligne_propre}{C_RESET}"

    # 2. Assignation des couleurs de base selon le bot
    if is_alpha:
        stats.alpha_cycles += 1
        prefix_color = C_ALPHA_PRE
        body_color = C_ALPHA_BODY
    elif is_beta:
        stats.beta_cycles += 1
        prefix_color = C_BETA_PRE
        body_color = C_BETA_BODY
    else:
        prefix_color = C_TIMESTAMP
        body_color = C_RESET

    # 3. Analyse des états (SKIP, FILL, PnL, Conf)
    ligne_colorimee = ligne_propre

    if "SKIP" in ligne_propre or "SKIPPED" in ligne_propre:
        if is_alpha:
            stats.alpha_skips += 1
        elif is_beta:
            stats.beta_skips += 1
        body_color = C_SKIP
    elif "FILLED" in ligne_propre or "entry=" in ligne_propre or "BUY" in ligne_propre or "SELL" in ligne_propre:
        if is_alpha:
            stats.alpha_fills += 1
        elif is_beta:
            stats.beta_fills += 1
        body_color = C_FILL

    # Extraction et coloration du PnL
    pnl_m = PNL_RE.search(ligne_propre)
    if pnl_m:
        val_pnl = float(pnl_m.group(1))
        if is_alpha:
            stats.alpha_pnl += val_pnl
        elif is_beta:
            stats.beta_pnl += val_pnl
        
        pnl_color = C_PNL_POS if val_pnl >= 0.0 else C_PNL_NEG
        ligne_colorimee = ligne_colorimee.replace(pnl_m.group(0), f"{pnl_color}{pnl_m.group(0)}{C_RESET}{body_color}")

    # Extraction et coloration de la confiance (alerte si < 0.1)
    conf_m = CONF_RE.search(ligne_propre)
    if conf_m:
        val_conf = float(conf_m.group(1))
        conf_color = C_CONF_LOW if val_conf < 0.1 else body_color
        ligne_colorimee = ligne_colorimee.replace(conf_m.group(0), f"{conf_color}{conf_m.group(0)}{C_RESET}{body_color}")

    # Formatage final avec préfixe coloré
    # On isole le préfixe [XXX] s'il existe
    if ligne_colorimee.startswith("["):
        fin_prefixe = ligne_colorimee.find("]")
        if fin_prefixe != -1:
            pref = ligne_colorimee[:fin_prefixe+1]
            corps = ligne_colorimee[fin_prefixe+1:]
            return f"{prefix_color}{pref}{C_RESET} {body_color}{corps}{C_RESET}"

    return f"{body_color}{ligne_colorimee}{C_RESET}"


def afficher_pouls(stats: SessionStats) -> None:
    """Affiche la ligne de pouls (résumé synthétique) toutes les 50 lignes."""
    pnl_a_col = C_PNL_POS if stats.alpha_pnl >= 0 else C_PNL_NEG
    pnl_b_col = C_PNL_POS if stats.beta_pnl >= 0 else C_PNL_NEG
    
    pouls = (
        f"\n{C_TIMESTAMP}▸ POULS COCKPIT :{C_RESET} "
        f"{C_ALPHA_PRE}α #{stats.alpha_cycles}{C_RESET} · "
        f"{C_BETA_PRE}β #{stats.beta_cycles}{C_RESET} | "
        f"FILLS {C_ALPHA_PRE}α={stats.alpha_fills}{C_RESET} {C_BETA_PRE}β={stats.beta_fills}{C_RESET} | "
        f"SKIP {C_ALPHA_PRE}α={stats.alpha_skips}{C_RESET} {C_BETA_PRE}β={stats.beta_skips}{C_RESET} | "
        f"PnL {pnl_a_col}α={stats.alpha_pnl:+.3f}{C_RESET} {pnl_b_col}β={stats.beta_pnl:+.3f}{C_RESET}\n"
    )
    sys.stdout.write(pouls)
    sys.stdout.flush()


def afficher_bilan(stats: SessionStats, fichier: str) -> None:
    """Affiche le bilan final propre lors de l'interruption (Ctrl+C)."""
    pnl_a_col = C_PNL_POS if stats.alpha_pnl >= 0 else C_PNL_NEG
    pnl_b_col = C_PNL_POS if stats.beta_pnl >= 0 else C_PNL_NEG
    
    bilan = (
        f"\n\n{C_HEADER}======================================================================{C_RESET}\n"
        f"{C_HEADER} [ACE777] BILAN DE SESSION TERMINAL{C_RESET}\n"
        f" Fichier analysé : {fichier}\n"
        f" Lignes lues     : {stats.lines_read}\n"
        f" --------------------------------------------------------------------\n"
        f" {C_ALPHA_PRE}ALPHA{C_RESET} -> Cycles: {stats.alpha_cycles} | Fills: {stats.alpha_fills} | "
        f"Skips: {stats.alpha_skips} | PnL Global: {pnl_a_col}{stats.alpha_pnl:+.4f}{C_RESET}\n"
        f" {C_BETA_PRE}BETA{C_RESET}  -> Cycles: {stats.beta_cycles} | Fills: {stats.beta_fills} | "
        f"Skips: {stats.beta_skips} | PnL Global: {pnl_b_col}{stats.beta_pnl:+.4f}{C_RESET}\n"
        f"{C_HEADER}======================================================================{C_RESET}\n"
    )
    sys.stderr.write(bilan)


def main() -> None:
    parser = argparse.ArgumentParser(description="Jumeau Cockpit Terminal pour ACE777")
    parser.add_argument("--replay", type=str, help="Chemin vers un fichier log passé à rejouer")
    parser.add_argument("--vitesse", type=float, default=0.0, help="Pause en secondes par ligne en mode replay")
    parser.add_argument("--tail", type=int, default=0, help="Nombre de lignes à lire au démarrage en live")
    parser.add_argument("--no-pulse", action="store_true", help="Désactiver les lignes de pouls périodiques")
    parser.add_argument("--json", action="store_true", help="Sortie brute au format JSON pour audit")
    args = parser.parse_args()

    # Sélection du fichier source
    fichier_log = args.replay if args.replay else trouver_dernier_log()
    
    if not os.path.exists(fichier_log):
        print(f"[ERREUR] Fichier introuvable : {fichier_log}", file=sys.stderr)
        sys.exit(1)

    stats = SessionStats()
    mode_replay = bool(args.replay)

    # En-tête informatif initial
    if not args.json:
        taille_Mo = os.path.getsize(fichier_log) / (1024 * 1024)
        mode_str = f"REPLAY (vitesse={args.vitesse}s)" if mode_replay else "LIVE (tail -f)"
        sys.stdout.write(
            f"{C_HEADER}=== ACE777 TERMINAL COCKPIT [{mode_str}] ==={C_RESET}\n"
            f"Fichier : {fichier_log} ({taille_Mo:.2f} Mo)\n"
            f"Appuyez sur Ctrl+C pour quitter et afficher le bilan.\n"
            f"{C_HEADER}----------------------------------------------------------------------{C_RESET}\n"
        )
        sys.stdout.flush()

    try:
        with open(fichier_log, "r", encoding="utf-8", errors="replace") as f:
            # Si mode live et option --tail demandée, positionner au début des n dernières lignes
            if not mode_replay and args.tail > 0:
                lignes_totales = f.readlines()
                lignes_depart = lignes_totales[-args.tail:]
                for ligne in lignes_depart:
                    colorise = coloriser_ligne(ligne, stats, args.json)
                    if colorise:
                        sys.stdout.write(colorise + "\n")
                sys.stdout.flush()
            elif not mode_replay:
                # Mode live standard : aller directement à la fin du fichier (tail -f)
                f.seek(0, os.SEEK_END)

            # Boucle principale de lecture continue
            while True:
                ligne = f.readline()
                if not ligne:
                    if mode_replay:
                        break  # Fin du fichier en mode replay
                    time.sleep(0.1)  # Attente active de nouvelles lignes en live
                    continue

                colorise = coloriser_ligne(ligne, stats, args.json)
                if colorise:
                    sys.stdout.write(colorise + "\n")
                    sys.stdout.flush()

                # Déclenchement du pouls toutes les 50 lignes (si non désactivé et hors json)
                if not args.json and not args.no_pulse and stats.lines_read % 50 == 0:
                    afficher_pouls(stats)

                # Pause optionnelle en mode replay
                if mode_replay and args.vitesse > 0:
                    time.sleep(args.vitesse)

    except KeyboardInterrupt:
        pass  # Interruption propre par l'utilisateur (Ctrl+C)
    finally:
        if not args.json:
            afficher_bilan(stats, fichier_log)


if __name__ == "__main__":
    main()
```
