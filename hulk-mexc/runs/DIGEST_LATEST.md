# Hulk DIGEST — 2026-10-14T10:15:20Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 2.57 | 5.23 | 2.37 | -0.02 | 1769513.23 | 1.22 | skipped_fast |
| WUSDT | IDLE | 1.1 | 6.53 | 3.05 | -0.19 | 3727907.17 | 8.03 | skipped_fast |
| ETHUSDT | IDLE | 1.07 | 1.94 | 1.32 | -0.01 | 127229872.96 | 0.12 | skipped_fast |
| XRPUSDT | IDLE | 1.01 | 1.8 | 1.51 | 0.0 | 29930833.55 | 0.73 | skipped_fast |
| BTCUSDT | IDLE | 0.73 | 1.31 | 0.97 | -0.0 | 328653187.91 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.33 | 3.18 | 2.46 | -0.05 | 1701338.11 | 0.95 | skipped_fast |
| CCUSDT | IDLE | 1.94 | 3.66 | 3.41 | 0.0 | 574480.1 | 7.43 | skipped_fast |
| CHIPUSDT | IDLE | 2.55 | 4.54 | 3.74 | -0.05 | 80333.13 | 12.53 | skipped_fast |
| KITEUSDT | IDLE | 2.22 | 6.92 | 4.29 | 0.07 | 76489.56 | 8.08 | skipped_fast |
| EDELUSDT | IDLE | 1.31 | 2.49 | 0.92 | 0.04 | 216199.95 | 5.84 | skipped_fast |
| REDUSDT | IDLE | 1.52 | 2.72 | 2.13 | -0.01 | 63822.47 | 15.43 | skipped_fast |
| BIOUSDT | IDLE | 1.33 | 2.35 | 2.01 | -0.01 | 69190.4 | 7.33 | skipped_fast |
| RIZEUSDT | IDLE | 1.62 | 5.66 | 0.34 | 0.05 | 49792.22 | 57.67 | skipped_fast |
| ZBCNUSDT | IDLE | 0.65 | 1.19 | 0.72 | -0.01 | 200968.31 | 12.75 | skipped_fast |
| FLUIDUSDT | IDLE | 2.29 | 6.63 | 5.05 | 0.04 | 18131.32 | 21.29 | skipped_fast |
| HBARUSDT | IDLE | 1.14 | 2.06 | 1.5 | -0.01 | 311558.17 | 5.79 | skipped_fast |
| RWAINCUSDT | IDLE | 0.98 | 2.08 | 1.53 | -0.08 | 34266.1 | 10.34 | skipped_fast |
| TELUSDT | IDLE | 0.92 | 1.74 | 0.72 | 0.03 | 115247.36 | 22.27 | skipped_fast |
| RWAUSDT | IDLE | 0.35 | 0.7 | 0.23 | -0.01 | 56372.02 | 7.77 | skipped_fast |
| MNSRYUSDT | IDLE | 0.15 | 0.29 | 0.01 | -0.01 | 38157.94 | 12.57 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
