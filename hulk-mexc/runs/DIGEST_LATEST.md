# Hulk DIGEST — 2026-08-22T01:48:44Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.88 | 10.86 | 1.22 | 0.15 | 6831095.51 | 1.96 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.36 | 10.49 | 0.05 | 0.17 | 152471406.22 | 5.97 | skipped_fast |
| HBARUSDT | IDLE | 2.98 | 6.36 | 0.31 | 0.08 | 960808.63 | 1.24 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.8 | 0.08 | 555606.87 | 19.85 | skipped_fast |
| CCUSDT | IDLE | 1.78 | 7.36 | 0.17 | 0.16 | 661352.67 | 8.74 | skipped_fast |
| WUSDT | IDLE | 2.68 | 6.65 | 0.31 | 0.09 | 392156.67 | 14.19 | skipped_fast |
| CHIPUSDT | IDLE | 1.61 | 3.56 | 1.03 | 0.01 | 512274.45 | 3.07 | skipped_fast |
| BIOUSDT | IDLE | 2.52 | 5.73 | 0.0 | 0.06 | 185904.6 | 6.08 | skipped_fast |
| EDELUSDT | IDLE | 2.62 | 5.5 | 1.95 | -0.02 | 79516.18 | 11.07 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 3.95 | 0.11 | 60968.07 | 45.71 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 8.27 | 4.91 | 0.17 | 157285.44 | 16.79 | skipped_fast |
| KITEUSDT | IDLE | 1.59 | 5.17 | 0.09 | 0.12 | 61303.33 | 8.96 | skipped_fast |
| QNTUSDT | IDLE | 2.44 | 5.18 | 1.19 | 0.06 | 171657.36 | 6.04 | skipped_fast |
| TELUSDT | IDLE | 2.61 | 6.19 | 1.53 | 0.04 | 182058.05 | 41.58 | skipped_fast |
| QAITUSDT | IDLE | 2.04 | 4.02 | 0.43 | 0.01 | 3870.41 | 31.31 | skipped_fast |
| RWAINCUSDT | IDLE | 1.77 | 3.27 | 1.79 | 0.03 | 9235.4 | 74.83 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 20.54 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.49 | 0.04 | 54595.88 | 16.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
