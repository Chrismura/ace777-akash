# Hulk DIGEST — 2026-08-22T04:08:40Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.8 | 12.59 | 0.2 | 0.2 | 10061374.24 | 23.92 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.15 | 12.22 | 1.57 | 0.2 | 166751166.72 | 1.27 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.08 | 11.33 | 0.06 | 0.22 | 718008.68 | 14.63 | skipped_fast |
| HBARUSDT | IDLE | 2.1 | 6.03 | 0.49 | 0.1 | 1009532.85 | 2.41 | skipped_fast |
| CHIPUSDT | IDLE | 2.99 | 5.36 | 4.15 | -0.03 | 458721.7 | 15.25 | skipped_fast |
| WUSDT | IDLE | 1.97 | 7.18 | 0.84 | 0.13 | 428380.48 | 11.69 | skipped_fast |
| BIOUSDT | IDLE | 3.01 | 7.36 | 2.23 | 0.07 | 199801.12 | 18.03 | skipped_fast |
| ZBCNUSDT | IDLE | 1.45 | 4.29 | 1.61 | 0.13 | 536810.11 | 17.16 | skipped_fast |
| EDELUSDT | IDLE | 2.02 | 3.95 | 3.47 | -0.05 | 80385.32 | 33.73 | skipped_fast |
| RIZEUSDT | IDLE | 1.85 | 7.71 | 4.99 | 0.1 | 59137.46 | 44.52 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 3.98 | 0.2 | 157847.47 | 10.29 | skipped_fast |
| KITEUSDT | IDLE | 1.6 | 5.55 | 0.45 | 0.13 | 67576.09 | 10.62 | skipped_fast |
| RWAINCUSDT | IDLE | 1.97 | 3.6 | 2.32 | 0.02 | 9399.91 | 54.35 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.55 | 3.8 | 0.78 | 0.09 | 178541.79 | 8.92 | skipped_fast |
| RWAUSDT | IDLE | 1.54 | 3.05 | 0.24 | 0.06 | 56330.74 | 16.04 | skipped_fast |
| TELUSDT | IDLE | 1.03 | 2.4 | 0.76 | 0.07 | 174251.28 | 56.14 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 19.54 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
