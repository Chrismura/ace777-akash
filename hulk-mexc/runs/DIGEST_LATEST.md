# Hulk DIGEST — 2026-08-21T23:07:46Z

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
| PYTHUSDT | IDLE | 1.68 | 6.26 | 0.24 | 0.12 | 5972078.85 | 2.02 | skipped_fast |
| XRPUSDT | IDLE | 1.75 | 6.77 | 0.23 | 0.15 | 138300408.74 | 1.38 | skipped_fast |
| CCUSDT | IDLE | 1.91 | 7.42 | 1.12 | 0.14 | 665402.58 | 8.9 | skipped_fast |
| HBARUSDT | IDLE | 2.38 | 5.19 | 0.0 | 0.09 | 888794.81 | 1.25 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.51 | 10.07 | 0.55 | 0.14 | 510145.21 | 20.56 | skipped_fast |
| WUSDT | IDLE | 2.74 | 6.91 | 1.21 | 0.08 | 376504.15 | 12.3 | skipped_fast |
| CHIPUSDT | IDLE | 1.17 | 3.56 | 1.09 | 0.05 | 544884.64 | 3.07 | skipped_fast |
| BIOUSDT | IDLE | 2.29 | 5.04 | 1.08 | 0.02 | 187368.16 | 3.11 | skipped_fast |
| EDELUSDT | IDLE | 2.53 | 5.5 | 0.65 | -0.02 | 82493.02 | 32.7 | skipped_fast |
| RWAINCUSDT | IDLE | 2.18 | 4.07 | 1.96 | 0.02 | 10205.68 | 16.16 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 43.69 | skipped_fast |
| REDUSDT | IDLE | 0.87 | 7.3 | 5.0 | 0.18 | 157266.71 | 18.63 | skipped_fast |
| TELUSDT | IDLE | 2.67 | 6.51 | 0.31 | 0.07 | 185107.21 | 51.52 | skipped_fast |
| QNTUSDT | IDLE | 2.5 | 5.21 | 0.0 | 0.07 | 99032.98 | 1.5 | skipped_fast |
| KITEUSDT | IDLE | 1.11 | 3.12 | 1.15 | 0.1 | 61510.66 | 11.12 | skipped_fast |
| RIZEUSDT | IDLE | 1.04 | 4.7 | 1.74 | 0.06 | 56644.83 | 115.65 | skipped_fast |
| RWAUSDT | IDLE | 1.02 | 2.0 | 0.25 | 0.04 | 54356.92 | 24.58 | skipped_fast |
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
