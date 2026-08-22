# Hulk DIGEST — 2026-08-22T10:06:32Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.71 | 16.77 | 10.6 | 0.02 | 51586514.85 | 2.04 | skipped_fast |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.89 | 23.87 | 13.2 | 0.04 | 215331212.92 | 8.82 | skipped_fast |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.43 | 15.8 | 11.26 | 0.01 | 1258123.6 | 6.48 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.04 | 22.93 | 12.54 | -0.11 | 663740.36 | 6.82 | skipped_fast |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 16.84 | 9.67 | 0.02 | 595116.1 | 12.74 | skipped_fast |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 29.98 | 10.8 | -0.04 | 236879.44 | 6.47 | skipped_fast |
| CCUSDT | IDLE | 2.26 | 11.25 | 8.7 | 0.11 | 812593.3 | 11.38 | skipped_fast |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 37.92 | 10.86 | 0.05 | 155605.34 | 14.36 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.12 | 7.87 | 7.25 | -0.02 | 432884.21 | 19.34 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 9.28 | 5.51 | 0.03 | 73258.24 | 11.12 | skipped_fast |
| EDELUSDT | IDLE | 2.7 | 4.76 | 4.22 | -0.03 | 79228.49 | 11.28 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.08 | 9.75 | 6.45 | -0.0 | 189410.02 | 14.07 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.94 | 7.38 | 6.87 | -0.03 | 170988.38 | 26.55 | skipped_fast |
| FLUIDUSDT | IDLE | 3.77 | 7.38 | 4.07 | 0.01 | 5824.3 | 21.55 | skipped_fast |
| QAITUSDT | IDLE | 1.54 | 2.91 | 1.09 | -0.01 | 3179.54 | 66.45 | skipped_fast |
| RWAINCUSDT | IDLE | 1.21 | 2.11 | 2.07 | 0.0 | 11462.91 | 64.86 | skipped_fast |
| RIZEUSDT | IDLE | 0.76 | 3.18 | 1.91 | -0.0 | 49321.72 | 46.77 | skipped_fast |
| RWAUSDT | IDLE | 1.77 | 3.29 | 1.67 | 0.02 | 57467.62 | 24.3 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
