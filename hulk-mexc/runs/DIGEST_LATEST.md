# Hulk DIGEST — 2026-08-22T10:52:16Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.74 | 16.77 | 11.75 | 0.0 | 51649659.25 | 2.07 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.87 | 23.87 | 12.34 | 0.08 | 218235943.91 | 2.02 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.42 | 15.8 | 11.15 | 0.0 | 1250574.45 | 3.89 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.03 | 22.93 | 11.92 | -0.11 | 663554.86 | 3.38 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 16.84 | 9.7 | 0.01 | 596182.31 | 12.75 | tvl≈1,583,490,295 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.23 | 29.98 | 11.61 | -0.06 | 240517.62 | 3.27 | n/a |
| CCUSDT | IDLE | 2.24 | 11.25 | 7.95 | 0.12 | 817975.19 | 11.28 | no_map |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 37.92 | 11.44 | 0.03 | 154169.33 | 11.74 | tvl≈2,031,082 |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.8 | 9.72 | 7.83 | -0.04 | 423675.86 | 21.01 | n/a |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 9.28 | 5.03 | 0.03 | 73423.44 | 9.19 | no_map |
| EDELUSDT | IDLE | 3.33 | 5.96 | 4.65 | -0.04 | 78951.55 | 22.7 | no_map |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.08 | 9.75 | 6.37 | -0.01 | 189258.32 | 7.82 | n/a |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.58 | 9.12 | 7.42 | -0.04 | 168718.83 | 53.5 | no_map |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.86 | 7.38 | 5.33 | -0.01 | 5711.25 | 23.13 | tvl≈2,553,890,177 |
| QAITUSDT | IDLE | 1.82 | 3.41 | 1.47 | 0.02 | 2551.93 | 67.45 | no_map |
| RWAINCUSDT | IDLE | 1.5 | 2.62 | 2.55 | 0.0 | 11326.93 | 54.35 | no_map |
| RWAUSDT | IDLE | 1.82 | 3.29 | 2.31 | 0.01 | 57384.2 | 8.16 | no_map |
| RIZEUSDT | IDLE | 0.74 | 3.18 | 1.26 | 0.0 | 49229.62 | 46.66 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
