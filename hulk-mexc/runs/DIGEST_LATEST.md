# Hulk DIGEST — 2026-08-22T16:41:58Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.07 | 10.19 | 0.27 | 0.09 | 51084521.23 | 9.5 | skipped_fast |
| XRPUSDT | IDLE | 1.32 | 7.64 | 3.34 | 0.06 | 214861029.66 | 2.71 | skipped_fast |
| CCUSDT | IDLE | 0.98 | 4.14 | 2.35 | 0.08 | 759993.81 | 8.54 | skipped_fast |
| HBARUSDT | IDLE | 0.79 | 3.03 | 0.7 | -0.0 | 1126091.11 | 11.59 | skipped_fast |
| CHIPUSDT | IDLE | 0.56 | 3.36 | 0.7 | -0.1 | 626928.44 | 3.34 | skipped_fast |
| WUSDT | IDLE | 0.61 | 2.58 | 0.62 | -0.01 | 543747.13 | 8.45 | skipped_fast |
| ZBCNUSDT | IDLE | 1.28 | 3.49 | 1.3 | -0.03 | 314836.95 | 17.87 | skipped_fast |
| BIOUSDT | IDLE | 0.95 | 6.58 | 3.75 | -0.06 | 219606.08 | 6.55 | skipped_fast |
| KITEUSDT | IDLE | 1.9 | 4.35 | 1.72 | 0.02 | 85072.35 | 14.3 | skipped_fast |
| EDELUSDT | IDLE | 1.4 | 2.52 | 1.9 | -0.03 | 74851.09 | 34.15 | skipped_fast |
| REDUSDT | IDLE | 0.51 | 5.67 | 3.5 | -0.13 | 129129.11 | 22.68 | skipped_fast |
| RIZEUSDT | IDLE | 1.32 | 3.23 | 0.17 | 0.08 | 47201.37 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | -0.01 | 2322.14 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 1.99 | -0.01 | 181884.78 | 11.0 | skipped_fast |
| TELUSDT | IDLE | 1.0 | 2.37 | 2.05 | -0.0 | 136841.43 | 26.7 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.03 | 7676.54 | 75.23 | skipped_fast |
| RWAUSDT | IDLE | 0.54 | 1.06 | 0.16 | 0.02 | 56501.1 | 8.1 | skipped_fast |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 20.82 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
