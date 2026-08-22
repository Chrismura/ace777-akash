# Hulk DIGEST — 2026-08-22T01:07:52Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.5 | 8.23 | 0.2 | 0.14 | 6582403.84 | 1.98 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.19 | 8.4 | 0.71 | 0.16 | 148908332.97 | 3.4 | skipped_fast |
| HBARUSDT | IDLE | 3.01 | 6.36 | 0.74 | 0.09 | 955208.8 | 1.25 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.89 | 0.11 | 542802.94 | 24.71 | skipped_fast |
| CCUSDT | IDLE | 1.73 | 6.94 | 0.2 | 0.16 | 653214.94 | 11.4 | skipped_fast |
| WUSDT | IDLE | 2.69 | 6.65 | 0.46 | 0.09 | 392301.94 | 11.16 | skipped_fast |
| CHIPUSDT | IDLE | 1.57 | 3.56 | 0.46 | 0.02 | 537867.78 | 6.11 | skipped_fast |
| BIOUSDT | IDLE | 2.44 | 5.53 | 0.09 | 0.05 | 187075.55 | 6.1 | skipped_fast |
| EDELUSDT | IDLE | 2.64 | 5.5 | 2.28 | -0.03 | 79702.01 | 22.2 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.08 | 0.11 | 60391.26 | 32.26 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 8.27 | 2.37 | 0.22 | 159855.5 | 19.47 | skipped_fast |
| QNTUSDT | IDLE | 2.41 | 5.18 | 0.75 | 0.07 | 170506.61 | 7.52 | skipped_fast |
| TELUSDT | IDLE | 2.56 | 6.19 | 0.77 | 0.05 | 181195.77 | 36.05 | skipped_fast |
| KITEUSDT | IDLE | 1.37 | 4.01 | 0.12 | 0.11 | 60856.79 | 12.65 | skipped_fast |
| QAITUSDT | IDLE | 2.06 | 4.02 | 0.7 | 0.01 | 3856.35 | 67.05 | skipped_fast |
| RWAINCUSDT | IDLE | 1.33 | 2.45 | 1.43 | 0.03 | 9646.54 | 16.16 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.04 | 55087.7 | 16.42 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 16.04 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
