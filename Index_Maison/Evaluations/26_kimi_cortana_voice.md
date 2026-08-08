# Éval #26 — Revue pack Kimi — CORTANA_VOICE (Downloads)

**Date :** 2026-07-30  
**Source :** `~/Downloads/CORTANA_VOICE_PACK/`  
**Intégré (corrigé) :** `Index_Maison/scripts/cortana_voice.py` → branché dans `cortana_thermo.py`

## Verdict

| Item | Statut |
|------|--------|
| Idée humanize chiffres | 🟢 BONNE |
| Sans pip `num2words` (stdlib) | 🟢 BON (C5) |
| Voix Ava Premium | 🔵 pas installée ici → **Amelie** / Thomas |
| README → `crypto-voice-assistant-core` | 🟡 mauvais chemin · notre moteur = Index `cortana_thermo` |
| `speak_status` schéma swarm | 🔴 obsolète (attend `ace`/`hulk` top-level ≠ notre `.agent_status`) |
| Urgent unlink sans archive | 🟡 on garde notre P3 (ack + last) |

## Bug bloquant (pack brut)

Dans `humanize()`, après conversion des nombres :

```python
text = text.replace("-", "moins")  # via replacements["-"]
```

→ **casse le français** : `trente-deux` → `trente moins deux`.  
**Fix :** ne jamais remplacer `-` globalement ; uniquement `+` / `=` isolés.

## Chez toi

```bash
# test humanize
python3 ~/ace777-test-day1/Index_Maison/scripts/cortana_voice.py

# alerte avec nouvelle voix
python3 ~/ace777-test-day1/Index_Maison/scripts/cortana_thermo.py alert "PnL +32.44$ drawdown -8.36%"

# forcer une voix
export CORTANA_VOICE=Amelie   # ou Thomas ; Ava si tu l’installes
```

Installer Ava Premium (optionnel) : Réglages → Accessibilité → Contenu prononcé → Gérer les voix → Ava.
