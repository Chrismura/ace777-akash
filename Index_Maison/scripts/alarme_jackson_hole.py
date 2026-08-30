#!/usr/bin/env python3
"""
🕐 ALARMES VOCALES — PROTOCOLE JACKSON HOLE
28 août 2026 — Survivre et profiter de la tempête

Usage:
  python3 alarme_jackson_hole.py          # Mode détection automatique
  python3 alarme_jackson_hole.py --test   # Test toutes les alarmes
  python3 alarme_jackson_hole.py --now    # Alerte immédiate (test)
"""

import os
import sys
import json
import subprocess
from datetime import datetime
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
DATA = BASE / "data"
SCRIPTS = BASE / "scripts"
COCKPIT = DATA / "live.json"
ALARMES_DIR = DATA / "alarmes"

# Fichier d'état pour éviter les alarmes en double
STATE_FILE = ALARMES_DIR / "jackson_hole_state.json"

# ══════════════════════════════════════════════════════════════
# ALARMES DU PROTOCOLE
# ══════════════════════════════════════════════════════════════

ALARMES = {
    "27_22h": {
        "label": "Relance famille",
        "heure": (27, 22, 0),
        "message": (
            "Protocole Jackson Hole. "
            "Il est 22 heures. "
            "Temps de relancer la famille. "
            "Vérifie les données live et prépare le brief. "
            "Jackson Hole est dans 30 heures."
        ),
        "urgence": True,
    },
    "27_23h": {
        "label": "Réponses famille reçues",
        "heure": (27, 23, 0),
        "message": (
            "Protocole Jackson Hole. "
            "Les réponses de la famille sont arrivées. "
            "Analyse les recommandations et ajuste Hulk si nécessaire. "
            "Tu as 30 minutes avant la fenêtre critique."
        ),
        "urgence": True,
    },
    "28_00h": {
        "label": "Ne pas toucher",
        "heure": (28, 0, 0),
        "message": (
            "Protocole Jackson Hole. "
            "Jackson Hole commence. "
            "Ne touche à rien. "
            "Laisse le système tourner. "
            "Ne trade pas. "
            "Bonne nuit et fais confiance au système."
        ),
        "urgence": True,
    },
    "28_12h": {
        "label": "Mi-journée — survie",
        "heure": (28, 12, 0),
        "message": (
            "Protocole Jackson Hole. "
            "Mi-journée. Le marché bouge. "
            "Vérifie le cockpit. "
            "Si le health est au-dessus de 0.85, tout va bien. "
            "Ne touche à rien."
        ),
        "urgence": False,
    },
    "28_17h": {
        "label": "Warsh dans 1 heure",
        "heure": (28, 17, 0),
        "message": (
            "Attention. Protocole Jackson Hole. "
            "Warsh parle dans 1 heure. "
            "C'est le premier Jackson Hole du nouveau directeur. "
            "Volatilité imminente. "
            "Surveille le cockpit. "
            "Ne trade pas pendant son discours."
        ),
        "urgence": True,
    },
    "28_18h30": {
        "label": "Warsh a parlé",
        "heure": (28, 18, 30),
        "message": (
            "Protocole Jackson Hole. "
            "Warsh a parlé. "
            "Le marché réagit. "
            "C'est sa première prise de position publique. "
            "En 2022, son discours a fait chuter BTC de 9%. "
            "Observe. Ne panique pas. "
            "Laisse le système analyser. "
            "Ne trade pas pendant les 2 prochaines heures."
        ),
        "urgence": True,
    },
    "29_09h": {
        "label": "Bilan du 28",
        "heure": (29, 9, 0),
        "message": (
            "Protocole Jackson Hole. "
            "Bilan du 28 août. "
            "Vérifie les résultats et compare avec le postulat. "
            "Le scénario baissier s'est-il confirmé ? "
            "C'est le moment de décider."
        ),
        "urgence": True,
    },
}


def load_state():
    """Charge l'état des alarmes déjà jouées."""
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {"alarmes_jouees": [], "derniere_verification": None}


def save_state(state):
    """Sauvegarde l'état."""
    ALARMES_DIR.mkdir(parents=True, exist_ok=True)
    state["derniere_verification"] = datetime.now().isoformat()
    STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False))


def announce(message, urgency=True):
    """Annonce vocale via edge-tts (déjà utilisé par alerte_vocale.py)."""
    try:
        print(f"\n{'🚨' if urgency else '📢'} ALERTE JACKSON HOLE")
        print(f"   {message[:80]}...")

        # Utiliser le même mécanisme que alerte_vocale.py
        import edge_tts
        import asyncio

        async def _speak():
            voice = "fr-FR-DeniseNeural" if urgency else "fr-FR-HenriNeural"
            communicate = edge_tts.Communicate(message, voice)
            out = ALARMES_DIR / "jackson_hole_alert.mp3"
            await communicate.save(str(out))
            subprocess.Popen(
                ["afplay", str(out)],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )

        asyncio.run(_speak())
        print("   🔊 Alerte vocale jouée")
        return True
    except Exception as e:
        print(f"   ⚠️ Erreur vocale: {e}")
        # Fallback : notification système
        try:
            subprocess.run(
                [
                    "osascript",
                    "-e",
                    f'display notification "{message[:100]}" with title "🌊 Jackson Hole" sound name "Frog"',
                ],
                timeout=5,
            )
        except Exception:
            pass
        return False


def check_timing():
    """Vérifie quelles alarmes doivent jouer maintenant."""
    now = datetime.now()
    state = load_state()
    jouees = set(state.get("alarmes_jouees", []))

    declenchees = []

    for key, alarme in ALARMES.items():
        if key in jouees:
            continue

        jour, heure, minute = alarme["heure"]
        # Créer la date cible (août 2026)
        try:
            target = datetime(2026, 8, jour, heure, minute)
        except ValueError:
            continue

        diff = (now - target).total_seconds()

        # Si on est entre 0 et 30 minutes après l'heure cible
        if 0 <= diff <= 1800:
            declenchees.append(key)
            jouees.add(key)
            announce(alarme["message"], alarme.get("urgence", True))

    if declenchees:
        state["alarmes_jouees"] = list(jouees)
        save_state(state)

    return declenchees


def test_all():
    """Teste toutes les alarmes vocales."""
    print("🧪 TEST TOUTES LES ALARMES — PROTOCOLE JACKSON HOLE")
    print("=" * 60)
    for key, alarme in ALARMES.items():
        print(f"\n📋 {alarme['label']} (28/{alarme['heure'][1]:02d}h{alarme['heure'][2]:02d})")
        announce(alarme["message"], alarme.get("urgence", True))
    print("\n✅ Toutes les alarmes testées")


def show_status():
    """Affiche l'état du protocole."""
    state = load_state()
    jouees = set(state.get("alarmes_jouees", []))
    now = datetime.now()

    print("🌊 PROTOCOLE JACKSON HOLE — ÉTAT")
    print("=" * 60)
    print(f"📅 Maintenant : {now.strftime('%d/%m %H:%M')}")
    print()

    for key, alarme in ALARMES.items():
        jour, heure, minute = alarme["heure"]
        try:
            target = datetime(2026, 8, jour, heure, minute)
        except ValueError:
            continue

        status = "✅ JOUÉE" if key in jouees else "⏳ EN ATTENTE"
        diff_h = (target - now).total_seconds() / 3600

        if diff_h > 0:
            timing = f"dans {diff_h:.1f}h"
        else:
            timing = f"il y a {-diff_h:.1f}h"

        print(f"  {'🚨' if alarme.get('urgence') else '📢'} {alarme['label']}")
        print(f"     28/{jour:02d} {heure:02d}h{minute:02d} — {timing} — {status}")

    print()
    print(f"📋 Alarmes jouées : {len(jouees)}/{len(ALARMES)}")
    if state.get("derniere_verification"):
        print(f"🔍 Dernière vérif : {state['derniere_verification']}")


if __name__ == "__main__":
    if "--test" in sys.argv:
        test_all()
    elif "--now" in sys.argv:
        announce(
            "Test d'alarme. Protocole Jackson Hole actif. "
            "Le système fonctionne correctement.",
            urgency=False,
        )
    elif "--status" in sys.argv:
        show_status()
    else:
        print(f"🌊 Jackson Hole Alarm — {datetime.now().strftime('%d/%m %H:%M')}")
        declenchees = check_timing()
        if not declenchees:
            print("   Aucune alarme à déclencher maintenant")
        else:
            print(f"   {len(declenchees)} alarme(s) déclenchée(s)")
