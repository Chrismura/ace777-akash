# Hulk DIGEST — 2026-08-22T03:02:15Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.3 | 9.55 | 1.06 | 0.14 | 7417246.73 | 3.82 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.24 | 11.15 | 0.22 | 0.2 | 159762629.19 | 3.87 | skipped_fast |
| HBARUSDT | IDLE | 2.14 | 5.29 | 0.06 | 0.1 | 993372.74 | 2.44 | skipped_fast |
| CCUSDT | IDLE | 1.9 | 8.67 | 0.0 | 0.19 | 665963.03 | 9.2 | skipped_fast |
| BIOUSDT | IDLE | 3.02 | 7.36 | 2.46 | 0.08 | 194625.2 | 2.99 | skipped_fast |
| CHIPUSDT | IDLE | 1.91 | 4.28 | 0.0 | -0.0 | 451727.11 | 2.97 | skipped_fast |
| ZBCNUSDT | IDLE | 1.44 | 5.16 | 2.12 | 0.12 | 540846.22 | 30.79 | skipped_fast |
| WUSDT | IDLE | 1.72 | 5.34 | 0.04 | 0.12 | 417286.04 | 12.83 | skipped_fast |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.26 | 0.09 | 61381.79 | 44.22 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 4.26 | 0.2 | 157768.94 | 15.07 | skipped_fast |
| EDELUSDT | IDLE | 1.89 | 3.83 | 2.28 | -0.03 | 79918.6 | 44.4 | skipped_fast |
| RWAINCUSDT | IDLE | 1.97 | 3.44 | 3.32 | -0.0 | 9418.45 | 43.45 | skipped_fast |
| KITEUSDT | IDLE | 1.31 | 4.03 | 0.23 | 0.12 | 62504.35 | 8.96 | skipped_fast |
| QAITUSDT | IDLE | 1.71 | 3.24 | 1.22 | 0.0 | 3930.15 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.72 | 3.97 | 0.67 | 0.08 | 172767.27 | 10.46 | skipped_fast |
| RWAUSDT | IDLE | 1.17 | 2.31 | 0.24 | 0.05 | 56158.74 | 8.09 | skipped_fast |
| TELUSDT | IDLE | 0.82 | 1.88 | 0.92 | 0.06 | 173118.7 | 56.83 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 22.38 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
