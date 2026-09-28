# Hulk DIGEST — 2026-09-28T16:25:41Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| WUSDT | IDLE | 1.76 | 8.49 | 4.77 | -0.1 | 2947904.0 | 7.22 | skipped_fast |
| XRPUSDT | IDLE | 2.08 | 3.98 | 1.15 | -0.0 | 65030103.08 | 1.98 | skipped_fast |
| QNTUSDT | IDLE | 0.69 | 16.85 | 8.84 | 0.23 | 21332784.27 | 7.74 | skipped_fast |
| HBARUSDT | IDLE | 1.36 | 12.5 | 1.37 | 0.35 | 9139901.03 | 7.91 | skipped_fast |
| PYTHUSDT | IDLE | 2.26 | 5.98 | 2.44 | -0.04 | 1460213.23 | 4.97 | skipped_fast |
| ETHUSDT | IDLE | 0.87 | 1.72 | 0.12 | 0.0 | 358728326.59 | 1.6 | skipped_fast |
| BTCUSDT | IDLE | 0.83 | 1.66 | 0.06 | -0.01 | 779857082.05 | 0.16 | skipped_fast |
| CCUSDT | IDLE | 1.71 | 6.53 | 2.95 | -0.02 | 1382629.42 | 9.19 | skipped_fast |
| EDELUSDT | IDLE | 2.11 | 13.46 | 6.13 | 0.06 | 190594.55 | 31.07 | skipped_fast |
| CHIPUSDT | IDLE | 2.72 | 6.46 | 3.74 | -0.06 | 75587.3 | 11.3 | skipped_fast |
| RWAINCUSDT | IDLE | 1.84 | 9.21 | 5.82 | 0.05 | 17644.14 | 33.21 | skipped_fast |
| BIOUSDT | IDLE | 1.59 | 4.83 | 1.53 | -0.06 | 111675.61 | 6.74 | skipped_fast |
| REDUSDT | IDLE | 1.91 | 4.49 | 1.45 | -0.05 | 61590.24 | 19.68 | skipped_fast |
| ZBCNUSDT | IDLE | 1.25 | 2.31 | 1.32 | -0.04 | 234814.04 | 24.38 | skipped_fast |
| KITEUSDT | IDLE | 1.49 | 5.91 | 0.73 | -0.07 | 100549.12 | 9.32 | skipped_fast |
| TELUSDT | IDLE | 2.52 | 4.97 | 0.43 | -0.01 | 148849.74 | 37.79 | skipped_fast |
| FLUIDUSDT | IDLE | 1.54 | 3.49 | 3.37 | -0.08 | 3879.18 | 19.72 | skipped_fast |
| RIZEUSDT | IDLE | 0.45 | 2.68 | 0.86 | -0.14 | 66085.08 | 112.89 | skipped_fast |
| RWAUSDT | IDLE | 0.85 | 1.67 | 0.14 | -0.01 | 60699.12 | 14.3 | skipped_fast |
| MNSRYUSDT | IDLE | 0.5 | 0.96 | 0.33 | -0.01 | 34133.07 | 47.58 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
