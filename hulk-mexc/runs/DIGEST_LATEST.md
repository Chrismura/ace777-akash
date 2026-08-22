# Hulk DIGEST — 2026-08-22T01:16:10Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.74 | 9.41 | 0.43 | 0.15 | 6645135.03 | 1.97 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.17 | 8.4 | 0.34 | 0.16 | 149811221.55 | 2.03 | skipped_fast |
| HBARUSDT | IDLE | 3.02 | 6.36 | 0.89 | 0.08 | 955831.33 | 1.25 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.76 | 0.11 | 539903.64 | 2.9 | skipped_fast |
| CCUSDT | IDLE | 1.76 | 7.18 | 0.01 | 0.16 | 658651.76 | 8.73 | skipped_fast |
| WUSDT | IDLE | 2.7 | 6.65 | 0.62 | 0.09 | 392570.25 | 10.16 | skipped_fast |
| CHIPUSDT | IDLE | 1.65 | 3.56 | 1.67 | -0.0 | 534326.31 | 3.09 | skipped_fast |
| BIOUSDT | IDLE | 2.46 | 5.57 | 0.06 | 0.05 | 187071.93 | 3.05 | skipped_fast |
| EDELUSDT | IDLE | 2.61 | 5.5 | 1.85 | -0.02 | 79585.34 | 33.2 | skipped_fast |
| RIZEUSDT | IDLE | 1.99 | 8.52 | 4.23 | 0.11 | 60504.78 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 0.95 | 8.27 | 3.28 | 0.19 | 159711.19 | 13.36 | skipped_fast |
| QNTUSDT | IDLE | 2.41 | 5.18 | 0.85 | 0.07 | 170439.06 | 3.01 | skipped_fast |
| TELUSDT | IDLE | 2.56 | 6.19 | 0.66 | 0.05 | 181057.39 | 41.22 | skipped_fast |
| KITEUSDT | IDLE | 1.47 | 4.48 | 0.32 | 0.11 | 60978.46 | 10.84 | skipped_fast |
| QAITUSDT | IDLE | 2.06 | 4.02 | 0.7 | 0.01 | 3856.35 | 67.05 | skipped_fast |
| RWAINCUSDT | IDLE | 1.33 | 2.45 | 1.43 | 0.03 | 9646.54 | 16.16 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.49 | 0.03 | 55249.07 | 8.2 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 23.05 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
