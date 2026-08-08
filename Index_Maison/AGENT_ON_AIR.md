# AGENT ON AIR — pastille multi-IA

**Hot :** `/tmp/ace777_swarm_pids/.agent_status.json`  
**UI :** `architecture/index.html` (pastille) · `agent_status.js`  
**Script :** `Index_Maison/scripts/agent_status.py`

## Schéma

```json
{
  "updated": "2026-07-30T16:50Z",
  "on_air": "CURSOR",
  "agents": {
    "ACE": { "status": "RUNNING", "ts": "…" },
    "HULK": { "status": "STOPPED", "ts": "…" },
    "CURSOR": { "status": "ON_AIR", "ts": "…" },
    "KIMI": { "status": "IDLE", "ts": "…" }
  }
}
```

## Commandes

```bash
python3 Index_Maison/scripts/agent_status.py heartbeat   # scan ACE/Hulk + CURSOR ON_AIR
python3 Index_Maison/scripts/agent_status.py set KIMI ON_AIR
python3 Index_Maison/scripts/agent_status.py set CURSOR IDLE
python3 Index_Maison/scripts/agent_status.py show
```

Anim : CURSOR = chat punk ambre · KIMI = lune cyan · ACE = éclair vert.

[[CONTRAT_URGENT_ALERT]] · [[RISK_C7]]
