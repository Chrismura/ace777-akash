# Veille Hulk — MEXC + DefiLlama + Qwen (piste B)

## Rôles

| Couche | Qui | Fait quoi |
|--------|-----|-----------|
| Trading truth | **MEXC** | prix, carnet, volume |
| Amont | **DefiLlama** (API DeFi) | TVL si dispo — **pas** un LLM |
| Superviseur | **Qwen** (manuel) | lit digest, note, alerte — **ne trade pas** |
| Exécution | `paper_diprip.py` | **piste A séparée** |

Voir `docs/TRACKS_SEPARES.md`.

## Lancer la veille

```bash
cd /Users/christophe/ace777-test-day1/hulk-mexc

# une passe
python3 scripts/digest_watch.py

# LIVE — terminal dédié (scan → scan, sans pause 60s)
python3 scripts/digest_watch.py --live
# arrêt : touch STOP_DIGEST
```

Qwen n’est **pas** branchée en websocket sur MEXC. Le digest tourne en boucle = « presque direct ».  
Écriture seulement si signal nouveau → `VEILLE_ALERT.md` + `VEILLE_CALLS.jsonl`.

Sorties :
- `runs/DIGEST_LATEST.md` (toujours à jour)
- `runs/VEILLE_ALERT.md` (dernier signal)
- `runs/VEILLE_CALLS.jsonl`
- `runs/VEILLE_QWEN_NOTES.md`

## Prompt Qwen

> Lis `runs/DIGEST_LATEST.md`. Résume spikes/dumps et risques.  
> Note 1–3 paires dans `VEILLE_QWEN_NOTES.md`. Pas d’ordres.  
> On comparera plus tard avec le paper Hulk.
