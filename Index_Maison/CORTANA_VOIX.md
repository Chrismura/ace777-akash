# Cortana — voix (récupération « film »)

**Problème :** `say` Amelie/Thomas = robotique + mélange. La vraie Cortana ACE = **edge-tts** (Vivienne).

**Défaut validé (Christophe) :** `fr-FR-VivienneMultilingualNeural` · rate `-18%` · `CORTANA_TTS=edge` (pas de repli Mac).

| Voix edge | Style |
|-----------|--------|
| `fr-FR-VivienneMultilingualNeural` | **défaut** · suave |
| `fr-FR-DeniseNeural` | classique app Cortana |
| `fr-FR-EloiseNeural` | plus jeune |
| `fr-CA-SylvieNeural` | Québec |

```bash
# test (vitesse un peu posée)
python3 ~/ace777-test-day1/Index_Maison/scripts/cortana_voice.py "Bonjour. Je parle plus lentement."

# encore plus lent si besoin
EDGE_TTS_RATE=-15% python3 …/cortana_voice.py "test"

# forcer vieux say (secours offline explicite)
CORTANA_TTS=say python3 …/cortana_voice.py "test"
```

**Écoute micro :** le cockpit Index **ne t’entend pas** (sortie seule). Pour parler à Cortana → app Rust `~/crypto-voice-assistant-core/`.

Alertes / horaire utilisent déjà `cortana_thermo` → `cortana_voice.speak`.

### Pré-son suave (anti surprise)
Avant chaque TTS : pad doux 2 tons (~0,5 s) puis Vivienne.  
News en boucle (UI) : même esprit — chime Web Audio à chaque rotation (~14 s), pas de voix.

```bash
# défaut ON
CORTANA_PRECHIME=1
CORTANA_PRECHIME_VOL=0.22   # 0.0–1.0 pour afplay

# couper le pré-son TTS seulement
CORTANA_PRECHIME=0
```

Journal produit cockpit (horloge / évolution) : [[JOURNAL_COCKPIT]].
