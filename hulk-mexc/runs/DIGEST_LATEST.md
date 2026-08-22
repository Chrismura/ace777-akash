# Hulk DIGEST — 2026-08-22T01:17:13Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.73 | 9.41 | 0.25 | 0.15 | 6649945.87 | 1.96 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.17 | 8.4 | 0.31 | 0.16 | 149894009.23 | 5.42 | skipped_fast |
| HBARUSDT | IDLE | 3.01 | 6.36 | 0.71 | 0.09 | 955104.36 | 3.74 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.9 | 0.11 | 547047.93 | 40.7 | skipped_fast |
| CCUSDT | IDLE | 1.76 | 7.18 | 0.1 | 0.17 | 659491.72 | 9.61 | skipped_fast |
| WUSDT | IDLE | 2.69 | 6.65 | 0.54 | 0.09 | 392577.35 | 13.22 | skipped_fast |
| CHIPUSDT | IDLE | 1.64 | 3.56 | 1.58 | -0.0 | 530725.2 | 6.18 | skipped_fast |
| BIOUSDT | IDLE | 2.46 | 5.57 | 0.09 | 0.05 | 187047.29 | 6.1 | skipped_fast |
| EDELUSDT | IDLE | 2.63 | 5.5 | 2.06 | -0.02 | 79585.37 | 33.2 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.03 | 0.11 | 60514.79 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 0.96 | 8.27 | 3.62 | 0.2 | 159812.04 | 12.63 | skipped_fast |
| QNTUSDT | IDLE | 2.41 | 5.18 | 0.85 | 0.07 | 170451.91 | 4.52 | skipped_fast |
| TELUSDT | IDLE | 2.56 | 6.19 | 0.72 | 0.05 | 181094.18 | 41.22 | skipped_fast |
| KITEUSDT | IDLE | 1.47 | 4.48 | 0.31 | 0.12 | 60958.88 | 10.84 | skipped_fast |
| QAITUSDT | IDLE | 2.06 | 4.02 | 0.7 | 0.01 | 3856.35 | 67.05 | skipped_fast |
| RWAINCUSDT | IDLE | 1.33 | 2.45 | 1.43 | 0.03 | 9646.54 | 16.16 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 22.33 | skipped_fast |
| RWAUSDT | IDLE | 1.07 | 2.08 | 0.41 | 0.04 | 55241.49 | 16.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
