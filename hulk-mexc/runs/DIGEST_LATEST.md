# Hulk DIGEST — 2026-08-22T01:27:41Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.8 | 10.39 | 0.1 | 0.16 | 6714311.12 | 11.66 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.17 | 8.42 | 0.24 | 0.15 | 150032702.73 | 0.68 | skipped_fast |
| HBARUSDT | IDLE | 3.01 | 6.36 | 0.77 | 0.08 | 951290.8 | 1.25 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.75 | 0.11 | 545735.81 | 3.87 | skipped_fast |
| CCUSDT | IDLE | 1.78 | 7.28 | 0.26 | 0.16 | 660433.82 | 6.99 | skipped_fast |
| WUSDT | IDLE | 2.73 | 6.65 | 1.21 | 0.09 | 392247.13 | 12.27 | skipped_fast |
| CHIPUSDT | IDLE | 1.65 | 3.56 | 1.7 | -0.02 | 515075.77 | 3.09 | skipped_fast |
| BIOUSDT | IDLE | 2.52 | 5.57 | 1.01 | 0.04 | 186028.98 | 3.08 | skipped_fast |
| EDELUSDT | IDLE | 2.64 | 5.5 | 2.17 | -0.02 | 79540.2 | 22.17 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.13 | 0.11 | 60662.94 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 0.97 | 8.27 | 4.54 | 0.18 | 158674.67 | 12.75 | skipped_fast |
| QNTUSDT | IDLE | 2.42 | 5.18 | 0.99 | 0.07 | 170145.74 | 3.02 | skipped_fast |
| KITEUSDT | IDLE | 1.5 | 4.63 | 0.33 | 0.12 | 60887.86 | 9.02 | skipped_fast |
| TELUSDT | IDLE | 2.57 | 6.19 | 0.92 | 0.05 | 181099.16 | 46.4 | skipped_fast |
| QAITUSDT | IDLE | 2.06 | 4.02 | 0.7 | 0.01 | 3856.35 | 67.05 | skipped_fast |
| RWAINCUSDT | IDLE | 1.33 | 2.45 | 1.43 | 0.03 | 9552.36 | 16.16 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 21.82 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.33 | 0.04 | 54998.43 | 16.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
