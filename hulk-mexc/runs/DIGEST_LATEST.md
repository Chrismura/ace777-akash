# Hulk DIGEST — 2026-08-21T22:56:49Z

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
| PYTHUSDT | IDLE | 1.49 | 5.71 | 0.06 | 0.11 | 5916771.91 | 2.03 | skipped_fast |
| XRPUSDT | IDLE | 1.67 | 6.54 | 0.13 | 0.15 | 136933006.34 | 2.07 | skipped_fast |
| CCUSDT | IDLE | 1.89 | 7.47 | 0.33 | 0.15 | 660891.03 | 7.07 | skipped_fast |
| HBARUSDT | IDLE | 2.19 | 4.91 | 0.01 | 0.09 | 876846.79 | 1.26 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.24 | 9.66 | 0.0 | 0.15 | 508306.1 | 24.34 | skipped_fast |
| WUSDT | IDLE | 2.67 | 6.91 | 0.11 | 0.09 | 372806.92 | 10.12 | skipped_fast |
| CHIPUSDT | IDLE | 1.53 | 4.54 | 2.17 | 0.05 | 542171.2 | 6.16 | skipped_fast |
| BIOUSDT | IDLE | 2.28 | 5.04 | 0.92 | 0.03 | 187754.42 | 6.21 | skipped_fast |
| REDUSDT | IDLE | 1.32 | 11.01 | 7.46 | 0.19 | 157355.27 | 8.84 | skipped_fast |
| EDELUSDT | IDLE | 2.29 | 5.04 | 0.11 | -0.03 | 82543.53 | 32.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.18 | 4.07 | 1.96 | 0.01 | 10217.99 | 16.16 | skipped_fast |
| TELUSDT | IDLE | 2.53 | 6.45 | 0.82 | 0.05 | 186729.58 | 10.36 | skipped_fast |
| QAITUSDT | IDLE | 2.31 | 4.38 | 1.63 | -0.01 | 3896.16 | 63.29 | skipped_fast |
| KITEUSDT | IDLE | 1.22 | 3.58 | 1.11 | 0.11 | 61282.94 | 9.22 | skipped_fast |
| QNTUSDT | IDLE | 2.44 | 4.88 | 0.0 | 0.07 | 88323.45 | 1.51 | skipped_fast |
| RIZEUSDT | IDLE | 0.96 | 4.7 | 2.01 | 0.06 | 56408.38 | 46.99 | skipped_fast |
| RWAUSDT | IDLE | 0.97 | 1.92 | 0.16 | 0.04 | 54075.25 | 16.38 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 8.42 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
