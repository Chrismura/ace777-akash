# Hulk DIGEST — 2026-08-22T04:02:15Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.76 | 11.77 | 0.37 | 0.18 | 9408494.25 | 18.58 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.15 | 12.22 | 1.83 | 0.2 | 166300789.92 | 5.1 | skipped_fast |
| CCUSDT | IDLE | 1.99 | 10.19 | 0.0 | 0.21 | 709951.15 | 13.1 | skipped_fast |
| HBARUSDT | IDLE | 2.11 | 6.03 | 0.52 | 0.11 | 1013561.7 | 7.23 | skipped_fast |
| CHIPUSDT | IDLE | 2.83 | 5.36 | 1.94 | -0.03 | 458905.22 | 3.0 | skipped_fast |
| BIOUSDT | IDLE | 3.02 | 7.36 | 2.52 | 0.07 | 199271.72 | 6.01 | skipped_fast |
| WUSDT | IDLE | 1.98 | 7.18 | 0.89 | 0.14 | 428242.39 | 19.48 | skipped_fast |
| ZBCNUSDT | IDLE | 1.44 | 4.29 | 1.54 | 0.13 | 537543.7 | 19.06 | skipped_fast |
| EDELUSDT | IDLE | 2.01 | 3.95 | 3.26 | -0.04 | 80652.49 | 22.47 | skipped_fast |
| RIZEUSDT | IDLE | 1.85 | 7.71 | 4.7 | 0.1 | 59252.95 | 46.02 | skipped_fast |
| REDUSDT | IDLE | 0.91 | 7.96 | 3.09 | 0.23 | 157744.07 | 12.55 | skipped_fast |
| KITEUSDT | IDLE | 1.59 | 5.55 | 0.29 | 0.13 | 67548.41 | 11.49 | skipped_fast |
| RWAINCUSDT | IDLE | 2.05 | 3.6 | 3.37 | 0.01 | 9366.1 | 43.55 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.54 | 3.8 | 0.58 | 0.09 | 178536.83 | 10.39 | skipped_fast |
| RWAUSDT | IDLE | 1.54 | 3.05 | 0.24 | 0.06 | 56389.02 | 16.04 | skipped_fast |
| TELUSDT | IDLE | 1.01 | 2.4 | 0.41 | 0.07 | 174267.9 | 35.74 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 15.37 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
