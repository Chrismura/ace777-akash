# Hulk DIGEST — 2026-08-22T02:35:15Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.61 | 10.52 | 1.48 | 0.14 | 7114065.36 | 3.85 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.44 | 12.02 | 0.21 | 0.19 | 156019428.13 | 1.95 | skipped_fast |
| HBARUSDT | IDLE | 2.4 | 5.62 | 0.04 | 0.09 | 973090.62 | 1.23 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.45 | 9.63 | 1.67 | 0.11 | 543718.94 | 23.92 | skipped_fast |
| CCUSDT | IDLE | 1.76 | 6.75 | 0.12 | 0.15 | 653238.41 | 6.93 | skipped_fast |
| CHIPUSDT | IDLE | 2.28 | 5.26 | 0.03 | -0.0 | 457459.73 | 6.0 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.14 | 8.18 | 1.0 | 0.1 | 193534.25 | 14.85 | skipped_fast |
| WUSDT | IDLE | 1.95 | 5.62 | 0.22 | 0.1 | 403163.13 | 11.97 | skipped_fast |
| EDELUSDT | IDLE | 2.49 | 5.02 | 3.15 | -0.04 | 79673.0 | 33.58 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.07 | 0.1 | 61489.23 | 33.96 | skipped_fast |
| REDUSDT | IDLE | 0.99 | 8.27 | 5.98 | 0.17 | 157814.85 | 19.38 | skipped_fast |
| QNTUSDT | IDLE | 2.34 | 5.48 | 0.24 | 0.08 | 172652.5 | 10.42 | skipped_fast |
| KITEUSDT | IDLE | 1.32 | 4.09 | 0.13 | 0.12 | 62435.52 | 11.66 | skipped_fast |
| RWAINCUSDT | IDLE | 1.83 | 3.27 | 2.58 | 0.02 | 9324.96 | 43.38 | skipped_fast |
| QAITUSDT | IDLE | 1.88 | 3.57 | 1.22 | 0.0 | 3930.15 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 2.14 | 5.11 | 1.02 | 0.06 | 176680.48 | 56.95 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 18.31 | skipped_fast |
| RWAUSDT | IDLE | 1.13 | 2.25 | 0.08 | 0.04 | 55152.92 | 8.15 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
