# Hulk DIGEST — 2026-08-22T15:52:36Z

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
| PYTHUSDT | IDLE | 1.59 | 7.62 | 1.56 | 0.04 | 51489275.98 | 3.95 | skipped_fast |
| XRPUSDT | IDLE | 1.39 | 7.64 | 6.09 | 0.03 | 216061785.3 | 2.79 | skipped_fast |
| CCUSDT | IDLE | 1.3 | 5.65 | 2.24 | 0.09 | 759053.78 | 7.67 | skipped_fast |
| HBARUSDT | IDLE | 0.86 | 3.03 | 2.36 | -0.02 | 1152864.09 | 3.93 | skipped_fast |
| CHIPUSDT | IDLE | 0.62 | 3.51 | 1.89 | -0.1 | 603616.49 | 3.38 | skipped_fast |
| WUSDT | IDLE | 0.79 | 3.17 | 1.97 | -0.03 | 554289.34 | 14.98 | skipped_fast |
| KITEUSDT | IDLE | 2.74 | 6.37 | 1.73 | 0.03 | 85536.92 | 8.92 | skipped_fast |
| ZBCNUSDT | IDLE | 1.31 | 3.49 | 1.89 | -0.05 | 320431.77 | 19.54 | skipped_fast |
| BIOUSDT | IDLE | 0.98 | 6.58 | 5.14 | -0.07 | 219400.41 | 3.32 | skipped_fast |
| EDELUSDT | IDLE | 1.42 | 2.52 | 2.12 | -0.03 | 75031.65 | 22.81 | skipped_fast |
| REDUSDT | IDLE | 0.52 | 5.67 | 4.46 | -0.16 | 134674.37 | 13.75 | skipped_fast |
| QAITUSDT | IDLE | 1.99 | 3.76 | 1.48 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| RIZEUSDT | IDLE | 0.78 | 3.28 | 0.13 | 0.03 | 56481.71 | 45.5 | skipped_fast |
| QNTUSDT | IDLE | 0.88 | 2.69 | 2.45 | -0.03 | 184212.94 | 3.16 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 9767.54 | 59.06 | skipped_fast |
| TELUSDT | IDLE | 1.11 | 2.75 | 1.52 | 0.0 | 139075.74 | 42.71 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4625.53 | 21.73 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.23 | 0.4 | 0.02 | 56598.08 | 24.36 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
