# Journal d’erreurs — zone test (avant réel)

**Rôle :** un seul endroit pour bugs / écarts pendant les runs **test**.  
**Protocole :** [[PROTOCOLE_VALIDATION_TEST_AVANT_REEL]]  
**Règle :** 1 anomalie = 1 ligne (ou fiche courte). Pas de roman dans le chat.

| Colonne | Sens |
|---------|------|
| id | `E-YYYYMMDD-N` |
| sev | P0 / P1 / P2 / P3 |
| statut | OUVERT · FIXÉ · WONTFIX · SURVEILLÉ |
| où | ACE / Hulk / cockpit / thermo / pont / hygiène |
| quoi | 1 ligne |
| repro | comment revoir |
| suite | fix ou décision |

---

## Ouverts

| id | sev | statut | où | quoi | repro | suite |
|----|-----|--------|-----|------|-------|-------|
| E-20260730-1 | P2 | SURVEILLÉ | cockpit OPS | PnL α parfois « bizarre » à l’œil vs intuition LIVE (CSV FILLED ≈ -4.35 OK) | Comparer `a-pnl` vs somme `pnl` CSV FILLED | Ne pas juger edge dessus · raffiner feed plus tard |
| E-20260730-2 | P2 | OUVERT | pont Cortana | Bridge `:17777` souvent OFF après coupure / sleep | `curl 127.0.0.1:17777/status` | Lancer `cortana_cockpit_bridge.py` avant lecture |
| E-20260730-3 | P3 | WONTFIX* | thermo free | LIQ 24h / ETF souvent n/d | BOARD pills LIQ/ETF | Free API flaky · pas bloquant (*tant que free) |

---

## Clos / histo

| id | sev | statut | où | quoi | suite |
|----|-----|--------|-----|------|-------|
| E-20260730-0 | P1 | FIXÉ* | ACE run | Coupe WiFi → Beta NET_RETRY rc=6 · ACE ne repart pas seul | *comportement attendu* · hygiène + relance manuelle GO |

---

## Template (copier)

```
| E-YYYYMMDD-N | P? | OUVERT | où | quoi | repro | suite |
```

Fiche longue (si P0/P1) → `Index_Maison/A_Mon_Attention/` ou `ERREURS_AI/` + lien ici.

---

## Compteur go-no-go

| Date | Run / tag | Porte 0 | Porte 1 | Porte 2 | Verdict | Notes |
|------|-----------|---------|---------|---------|---------|-------|
| 2026-07-30 | `NUAGE_SETUP_AVANT` (soir) | — | BOARD OK · pont souvent OFF | run en cours / WiFi déjà vu | INCONCLUSIF outils | Zone test cockpit ouverte |

*Après chaque run test : 1 ligne ici.*
