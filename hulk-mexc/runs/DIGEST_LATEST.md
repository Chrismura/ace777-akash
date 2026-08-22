# Hulk DIGEST — 2026-08-22T03:07:33Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.32 | 9.95 | 0.66 | 0.16 | 7491397.64 | 15.15 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.24 | 11.15 | 0.32 | 0.21 | 160114554.44 | 3.87 | skipped_fast |
| HBARUSDT | IDLE | 2.15 | 5.29 | 0.3 | 0.1 | 996619.32 | 3.66 | skipped_fast |
| CCUSDT | IDLE | 1.94 | 8.96 | 0.28 | 0.19 | 666858.76 | 9.22 | skipped_fast |
| BIOUSDT | IDLE | 3.01 | 7.36 | 2.34 | 0.06 | 195389.16 | 3.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.93 | 4.28 | 0.3 | -0.01 | 449212.92 | 2.98 | skipped_fast |
| WUSDT | IDLE | 1.77 | 5.61 | 0.13 | 0.12 | 417666.4 | 13.8 | skipped_fast |
| ZBCNUSDT | IDLE | 1.46 | 5.16 | 2.59 | 0.12 | 541907.82 | 61.32 | skipped_fast |
| EDELUSDT | IDLE | 1.9 | 3.83 | 2.39 | -0.02 | 79855.9 | 11.13 | skipped_fast |
| RIZEUSDT | IDLE | 1.81 | 7.71 | 4.24 | 0.1 | 61386.56 | 44.22 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 3.83 | 0.21 | 158036.3 | 17.39 | skipped_fast |
| RWAINCUSDT | IDLE | 1.97 | 3.44 | 3.32 | -0.0 | 9418.45 | 10.86 | skipped_fast |
| KITEUSDT | IDLE | 1.32 | 4.12 | 0.0 | 0.12 | 63791.94 | 10.72 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.0 | 3843.06 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.69 | 3.97 | 0.18 | 0.09 | 172818.17 | 5.95 | skipped_fast |
| RWAUSDT | IDLE | 1.17 | 2.31 | 0.24 | 0.05 | 56143.93 | 24.24 | skipped_fast |
| TELUSDT | IDLE | 0.92 | 2.19 | 0.46 | 0.07 | 173199.02 | 71.61 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 22.33 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
