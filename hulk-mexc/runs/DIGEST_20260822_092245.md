# Hulk DIGEST — 2026-08-22T09:22:45Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 19.14 | 10.03 | 0.05 | 39813523.03 | 1.99 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.83 | 23.87 | 10.49 | 0.12 | 219573845.46 | 1.32 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.38 | 15.8 | 10.0 | 0.04 | 1300406.78 | 3.82 | empty_tvl |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 17.58 | 8.22 | 0.05 | 597568.77 | 13.49 | tvl≈1,583,490,295 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 29.98 | 10.54 | -0.02 | 237799.39 | 3.23 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.1 | 41.27 | 11.51 | 0.06 | 154683.5 | 11.47 | tvl≈2,081,438 |
| CCUSDT | IDLE | 2.21 | 11.25 | 6.85 | 0.13 | 796971.5 | 8.58 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.13 | 8.0 | 6.5 | -0.01 | 466481.04 | 17.64 | n/a |
| KITEUSDT | IDLE | 4.24 | 9.68 | 3.84 | 0.06 | 73004.95 | 13.6 | no_map |
| QAITUSDT | IDLE | 1.54 | 2.91 | 1.09 | 0.01 | 3209.57 | 66.45 | no_map |
| RIZEUSDT | IDLE | 0.8 | 3.36 | 1.82 | -0.02 | 50334.86 | 46.77 | no_map |
| TELUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| CHIPUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAINCUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| EDELUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| QNTUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| FLUIDUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
