# C7 — Circuit breaker drawdown combiné ACE+Hulk

**Statut :** 🟡 constante posée · Guardian **pas encore en vol**  
**Date défaut :** 2026-07-30  

| Clé | Valeur | Où |
|-----|--------|-----|
| `MAX_GLOBAL_DD_PCT` | **8** | `Index_Maison/config_risk_warm.env` |

**Sens :** si (PnL ACE session + PnL Hulk) / notionnel de référence ≤ **−8 %** → alerte URGENT (+ futur kill soft ACE).  
Ne touche **pas** `genesis_manifest` / masses 200·800.

**P1** `.veille_status.json` atomic write : **CLOSED** (`veille_gates._safe_write`).  
**P3** Cortana urgent : `cortana_thermo.py urgent|alert|poll` + launchd 60s.

[[ARCHITECTURE_TECH]] · [[Evaluations/15_kimi_archi_risk_warm]]
