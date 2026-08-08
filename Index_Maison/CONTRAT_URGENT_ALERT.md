# Contrat URGENT — bus fichier (P3)

**Hot file (consommé) :** `/tmp/ace777_swarm_pids/.urgent_alert.json`  
**Archive :** `Index_Maison/thermo/.urgent_alert.last.json`  
**Poll :** launchd `com.ace777.cortana.urgent` · **10 s**  
**Reader Python :** `cortana_thermo.py poll|urgent|alert`  
**Reader Rust (à brancher) :** même path · pastille rouge egui · `say` via tool sûr (pas `os.system`)

## Schéma

```json
{
  "ts": "2026-07-30T16:45Z",
  "level": "URGENT",
  "title": "DD global",
  "msg": "ACE+Hulk sous -8%",
  "source": "risk_guardian|manual|test",
  "ack": false,
  "max_global_dd_pct": 8.0
}
```

## Règles

1. Write atomique (`.tmp` + `rename`/`replace`)
2. Speak **avant** remove (sinon alerte perdue si `say` échoue)
3. Jamais `os.system(f"say '{msg}'")` — quotes / injection
4. Cortana ≠ orchestrateur (C3) — voix + UI only
5. Risk Guardian WARM écrit ce fichier ; ne place pas d’ordre

## Test

```bash
python3 Index_Maison/scripts/cortana_thermo.py alert "Test bus /tmp"
# ou
python3 -c "…"  # write title+msg
```

[[RISK_C7]] · [[Evaluations/15_kimi_archi_risk_warm]]
