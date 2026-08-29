# Hulk DIGEST — 2026-08-29T05:06:06Z

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
| XRPUSDT | IDLE | 0.45 | 0.88 | 0.17 | -0.02 | 44223839.81 | 1.44 | skipped_fast |
| CHIPUSDT | IDLE | 1.75 | 8.91 | 1.82 | 0.08 | 1133836.03 | 7.14 | skipped_fast |
| QAITUSDT | IDLE | 2.35 | 20.42 | 14.43 | -0.02 | 96080.9 | 10.17 | skipped_fast |
| PYTHUSDT | IDLE | 0.81 | 1.48 | 0.98 | -0.02 | 524667.81 | 2.1 | skipped_fast |
| RIZEUSDT | IDLE | 2.56 | 6.2 | 2.02 | -0.04 | 29240.17 | 56.03 | skipped_fast |
| CCUSDT | IDLE | 0.95 | 1.75 | 0.95 | -0.01 | 244625.67 | 8.1 | skipped_fast |
| EDELUSDT | IDLE | 1.33 | 5.29 | 1.49 | -0.09 | 90968.17 | 18.9 | skipped_fast |
| KITEUSDT | IDLE | 1.5 | 2.76 | 1.58 | -0.0 | 73700.04 | 10.21 | skipped_fast |
| WUSDT | IDLE | 0.97 | 1.92 | 0.2 | -0.02 | 208953.15 | 16.2 | skipped_fast |
| REDUSDT | IDLE | 1.37 | 3.09 | 1.17 | -0.02 | 61288.87 | 13.81 | skipped_fast |
| HBARUSDT | IDLE | 0.69 | 1.23 | 1.05 | -0.03 | 468240.73 | 1.32 | skipped_fast |
| ZBCNUSDT | IDLE | 0.67 | 1.87 | 0.01 | -0.06 | 173660.85 | 1.52 | skipped_fast |
| BIOUSDT | IDLE | 0.5 | 0.94 | 0.36 | -0.02 | 83608.89 | 3.59 | skipped_fast |
| TELUSDT | IDLE | 1.62 | 3.0 | 1.57 | -0.05 | 95191.14 | 57.01 | skipped_fast |
| FLUIDUSDT | IDLE | 0.92 | 1.61 | 1.58 | -0.04 | 3732.19 | 21.61 | skipped_fast |
| QNTUSDT | IDLE | 0.58 | 1.13 | 0.16 | -0.01 | 41178.03 | 6.5 | skipped_fast |
| RWAINCUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.02 | 3438.94 | 76.67 | skipped_fast |
| RWAUSDT | IDLE | 0.34 | 0.66 | 0.16 | 0.0 | 54112.23 | 8.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
