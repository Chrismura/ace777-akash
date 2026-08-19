# Cortana — voix (récupération « film »)

**Problème :** `say` Amelie/Thomas = robotique + mélange. La vraie Cortana ACE = **edge-tts** (Denise).

**Défaut (19/08) :** `fr-FR-DeniseNeural` (français **pur**, non-multilingue) · rate `-18%` · `CORTANA_TTS=edge` (pas de repli Mac).

> ⚠️ **Pourquoi on a quitté Vivienne (19/08)** : `fr-FR-VivienneMultilingualNeural` est
> **multilingue** → dès qu'un ticker / mot anglais glisse dans le texte, elle **bascule
> de langue** et prend un **accent espagnol** insupportable. Denise (General, non-multilingue)
> ne peut pas dériver : elle lit tout en français.

| Voix edge | Style |
|-----------|--------|
| `fr-FR-DeniseNeural` | **défaut** · classique app Cortana · français pur |
| `fr-FR-VivienneMultilingualNeural` | suave mais multilingue → accent espagnol (retirée) |
| `fr-FR-EloiseNeural` | plus jeune · français pur |
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
Avant chaque TTS : pad doux 2 tons (~0,5 s) puis Denise.  
News en boucle (UI) : même esprit — chime Web Audio à chaque rotation (~14 s), pas de voix.

```bash
# défaut ON
CORTANA_PRECHIME=1
CORTANA_PRECHIME_VOL=0.22   # 0.0–1.0 pour afplay

# couper le pré-son TTS seulement
CORTANA_PRECHIME=0
```

Journal produit cockpit (horloge / évolution) : [[JOURNAL_COCKPIT]].
