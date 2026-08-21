# Hulk DIGEST — 2026-08-21T23:00:08Z

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
| PYTHUSDT | IDLE | 1.51 | 5.77 | 0.18 | 0.12 | 5931358.49 | 4.06 | skipped_fast |
| XRPUSDT | IDLE | 1.68 | 6.54 | 0.39 | 0.15 | 137232059.73 | 2.77 | skipped_fast |
| CCUSDT | IDLE | 1.89 | 7.47 | 0.23 | 0.14 | 661981.64 | 7.94 | skipped_fast |
| HBARUSDT | IDLE | 2.24 | 5.03 | 0.33 | 0.09 | 878358.35 | 2.51 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.33 | 9.96 | 0.52 | 0.15 | 508803.78 | 25.83 | skipped_fast |
| WUSDT | IDLE | 2.74 | 6.91 | 1.19 | 0.09 | 372934.64 | 16.35 | skipped_fast |
| CHIPUSDT | IDLE | 1.52 | 4.54 | 2.08 | 0.05 | 543076.46 | 3.08 | skipped_fast |
| BIOUSDT | IDLE | 2.29 | 5.04 | 0.98 | 0.03 | 187854.79 | 3.11 | skipped_fast |
| REDUSDT | IDLE | 1.32 | 11.01 | 7.9 | 0.19 | 157194.37 | 12.92 | skipped_fast |
| EDELUSDT | IDLE | 2.28 | 5.04 | 0.0 | -0.02 | 82553.54 | 21.81 | skipped_fast |
| RWAINCUSDT | IDLE | 2.18 | 4.07 | 1.96 | 0.01 | 10217.99 | 16.16 | skipped_fast |
| QAITUSDT | IDLE | 2.36 | 4.38 | 2.29 | -0.02 | 3921.68 | 43.69 | skipped_fast |
| TELUSDT | IDLE | 2.53 | 6.45 | 0.87 | 0.05 | 186677.45 | 10.36 | skipped_fast |
| QNTUSDT | IDLE | 2.45 | 4.92 | 0.0 | 0.07 | 90747.48 | 1.5 | skipped_fast |
| KITEUSDT | IDLE | 1.22 | 3.58 | 1.26 | 0.1 | 61363.34 | 12.0 | skipped_fast |
| RIZEUSDT | IDLE | 0.96 | 4.7 | 1.94 | 0.06 | 56409.87 | 46.99 | skipped_fast |
| RWAUSDT | IDLE | 1.02 | 2.0 | 0.25 | 0.04 | 54220.02 | 16.39 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 21.82 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
