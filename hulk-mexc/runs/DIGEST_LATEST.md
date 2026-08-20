# Hulk DIGEST — 2026-08-20T06:20:59Z

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
| XRPUSDT | IDLE | 0.83 | 2.58 | 1.17 | 0.1 | 46891005.83 | 0.91 | skipped_fast |
| REDUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.52 | 24.54 | 1.36 | 0.37 | 148674.07 | 25.11 | skipped_fast |
| CHIPUSDT | IDLE | 1.76 | 7.74 | 1.9 | 0.15 | 227958.96 | 10.15 | skipped_fast |
| CCUSDT | IDLE | 0.95 | 3.29 | 0.26 | 0.13 | 386832.1 | 5.91 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.77 | 18.72 | 9.48 | 0.14 | 61988.19 | 211.53 | skipped_fast |
| WUSDT | IDLE | 1.07 | 2.15 | 1.63 | 0.06 | 279349.02 | 14.03 | skipped_fast |
| PYTHUSDT | IDLE | 0.71 | 2.05 | 1.24 | 0.09 | 303348.3 | 2.36 | skipped_fast |
| EDELUSDT | IDLE | 1.46 | 11.14 | 8.4 | 0.22 | 101170.59 | 99.06 | skipped_fast |
| ZBCNUSDT | IDLE | 0.99 | 3.83 | 2.38 | 0.13 | 228702.52 | 35.52 | skipped_fast |
| BIOUSDT | IDLE | 0.99 | 4.73 | 0.0 | 0.17 | 174459.37 | 16.97 | skipped_fast |
| HBARUSDT | IDLE | 1.05 | 2.09 | 0.07 | 0.06 | 366683.85 | 1.4 | skipped_fast |
| QAITUSDT | IDLE | 1.35 | 3.52 | 3.25 | 0.03 | 11472.53 | 38.57 | skipped_fast |
| KITEUSDT | IDLE | 0.84 | 1.51 | 1.24 | 0.05 | 59801.87 | 13.61 | skipped_fast |
| RWAINCUSDT | IDLE | 0.59 | 1.77 | 0.28 | 0.06 | 17210.23 | 61.95 | skipped_fast |
| TELUSDT | IDLE | 0.5 | 2.31 | 1.1 | 0.12 | 189062.0 | 61.8 | skipped_fast |
| QNTUSDT | IDLE | 0.7 | 1.31 | 0.57 | 0.05 | 37358.53 | 8.48 | skipped_fast |
| RWAUSDT | IDLE | 0.49 | 0.87 | 0.77 | 0.02 | 53564.26 | 8.65 | skipped_fast |
| FLUIDUSDT | IDLE | 0.43 | 1.15 | 0.12 | 0.07 | 3488.43 | 22.49 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
