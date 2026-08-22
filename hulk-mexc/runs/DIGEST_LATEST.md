# Hulk DIGEST — 2026-08-22T01:38:38Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.88 | 10.86 | 1.26 | 0.16 | 6785256.04 | 5.87 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.26 | 9.37 | 0.0 | 0.16 | 151262358.38 | 1.34 | skipped_fast |
| HBARUSDT | IDLE | 2.97 | 6.36 | 0.15 | 0.09 | 960441.62 | 1.24 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.79 | 0.09 | 551195.49 | 18.39 | skipped_fast |
| CCUSDT | IDLE | 1.78 | 7.36 | 0.12 | 0.17 | 662306.28 | 8.72 | skipped_fast |
| WUSDT | IDLE | 2.69 | 6.65 | 0.54 | 0.09 | 392350.49 | 8.12 | skipped_fast |
| CHIPUSDT | IDLE | 1.6 | 3.56 | 0.94 | 0.01 | 513103.82 | 3.07 | skipped_fast |
| BIOUSDT | IDLE | 2.52 | 5.57 | 0.94 | 0.04 | 186317.35 | 9.23 | skipped_fast |
| EDELUSDT | IDLE | 2.62 | 5.5 | 1.95 | -0.02 | 79516.15 | 22.12 | skipped_fast |
| RIZEUSDT | IDLE | 1.99 | 8.52 | 4.21 | 0.11 | 60810.42 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 8.27 | 4.99 | 0.16 | 158633.18 | 18.4 | skipped_fast |
| TELUSDT | IDLE | 2.59 | 6.19 | 1.18 | 0.05 | 181991.72 | 10.36 | skipped_fast |
| KITEUSDT | IDLE | 1.59 | 5.17 | 0.0 | 0.13 | 61107.88 | 18.8 | skipped_fast |
| QAITUSDT | IDLE | 2.04 | 4.02 | 0.43 | 0.01 | 3870.41 | 31.31 | skipped_fast |
| QNTUSDT | IDLE | 2.42 | 5.18 | 1.03 | 0.07 | 170073.51 | 19.58 | skipped_fast |
| RWAINCUSDT | IDLE | 1.73 | 3.27 | 1.32 | 0.03 | 9649.22 | 32.03 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 21.18 | skipped_fast |
| RWAUSDT | IDLE | 1.07 | 2.08 | 0.41 | 0.03 | 54748.19 | 8.19 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
