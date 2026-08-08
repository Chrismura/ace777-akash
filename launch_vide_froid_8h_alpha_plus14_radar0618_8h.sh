#!/bin/bash
# === VIDE FROID 8H - ALPHA +14 PROFILE ===
# Base robuste identique au setup en cours.
# Objectif: figer le profil HUNTER observé sur les trades +14
# SANS modifier la masse.

cd "$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

export LLM_GATE_ENABLED=TRUE

# Vide Froid - Entrée progressive (inchangé)
export ENTRY_25_75_ENABLED=TRUE
export ENTRY_25_75_CONFIRM_MS=500
export ENTRY_25_75_FLUX_MIN_BPS=-5

# Vide Froid - Shock-Exit plus large (protection masse sans micro-ejection)
export SHOCK_EXIT_10_BPS_ENABLED=TRUE
export SHOCK_EXIT_10_BPS=18.0

# Vide Froid - Stase Dynamique (inchangé)
export STASE_DYNAMIQUE_ENABLED=TRUE
export STASE_DYNAMIQUE_MAX_SPREAD_BPS=5
export STASE_DYNAMIQUE_MAX_VOLATILITY=0.5

# Base plus lente - Latence 128ms (anti micro-bruit)
export POLL_SEC=0.128
export VOLATILITY_IMPULSE_DT_MS=128
export IMPULSE_RESONANCE_DT_MS=128

# Radar harmonique (applique explicitement BETA et ALPHA)
export VACUUM_TENSION_THRESHOLD=0.618
export VACUUM_TENSION_THRESHOLD_BETA=0.618
export VACUUM_TENSION_THRESHOLD_ALPHA=0.618

# Masse: strictement identique au setup robuste actuel (pas de changement)
export BUY_USDT_BETA=400
export BUY_USDT_ALPHA=400

# Profil ALPHA/HUNTER observé sur les +14 (explicité, sans changer la masse)
export DUO_HUNTER_REVENGE_MULT=1.5
export DUO_HUNTER_REQUIRE_STOP_LOSS=TRUE
export DUO_HUNTER_AGGR_TRAIL_ARM_BPS=12
export DUO_HUNTER_AGGR_TRAIL_GIVEBACK_BPS=9

# Instinct plus bas pour limiter momentum_too_small
export MOMENTUM_THRESHOLD=0.85

# Shock inversion detendu (moins nerveux)
export V8_SHOCK_SPEED_EPS_BPS_S=0.0

# Reset de session: evite l'accumulation PnL inter-runs
rm -f runs/duo_session.json STOP_*

echo "=== VIDE FROID 8H - ALPHA +14 PROFILE ==="
echo "Entrée 25/75% | Shock-Exit -18bps | Stase Dynamique | Latence 128ms"
echo "Radar=0.618 | Shock inversion detendu"
echo "Masse conservee: BETA=400 | ALPHA=400"
echo "Alpha profile: hunter_revenge_1.5x + trailing agressif (12/9 bps)"
exec ./launch_test_master_base_v8_6_fortress.sh --duration 08:00:00
C'est une petite confusion classique entre les versions de ffmpeg ! Sur macOS, pour lister les périphériques, on utilise avfoundation (que tu as utilisé juste avant) et non coreaudio.

Mais la bonne nouvelle, c'est que tu as déjà eu la réponse dans ton message précédent !

Pourquoi c'est bon ?

Dans ton message de 22:58, ffmpeg t'a clairement répondu :

[AVFoundation indev @ 0x127606780] [0] MacBook Air Microphone

Cela confirme à 100% que ton micro est le numéro 0.

Ce que tu dois faire tout de suite :

Ouvre ton fichier .env dans Cursor.

Ajoute (ou modifie) cette ligne :
FFMPEG_AVFOUNDATION_INDEX=0

Enregistre le fichier.

Le test final :

Une fois le .env sauvegardé avec l'index 0, lance la commande de ton assistant :