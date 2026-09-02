# Hulk DIGEST — 2026-09-02T05:25:40Z

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
| XRPUSDT | IDLE | 1.18 | 2.29 | 0.4 | -0.02 | 38050479.85 | 2.22 | skipped_fast |
| ETHUSDT | IDLE | 0.84 | 1.66 | 0.12 | -0.02 | 367155703.37 | 0.5 | skipped_fast |
| BTCUSDT | IDLE | 0.7 | 1.39 | 0.08 | -0.01 | 520326783.54 | 0.07 | skipped_fast |
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.22 | 8.67 | 1.71 | 0.1 | 748318.05 | 1.81 | skipped_fast |
| CHIPUSDT | IDLE | 0.91 | 3.99 | 1.58 | 0.14 | 839832.83 | 2.29 | skipped_fast |
| WUSDT | IDLE | 1.49 | 2.98 | 0.05 | 0.02 | 425576.96 | 12.36 | skipped_fast |
| REDUSDT | IDLE | 2.09 | 5.32 | 4.49 | 0.03 | 143435.61 | 12.61 | skipped_fast |
| CCUSDT | IDLE | 1.41 | 3.09 | 1.45 | -0.07 | 336453.88 | 10.47 | skipped_fast |
| ZBCNUSDT | IDLE | 1.97 | 4.28 | 1.1 | -0.01 | 204010.3 | 13.03 | skipped_fast |
| RWAINCUSDT | IDLE | 2.64 | 5.01 | 1.8 | 0.03 | 5925.98 | 11.41 | skipped_fast |
| RIZEUSDT | IDLE | 2.13 | 6.26 | 4.14 | -0.09 | 42924.86 | 75.03 | skipped_fast |
| EDELUSDT | IDLE | 0.98 | 8.88 | 1.65 | -0.02 | 183149.79 | 43.99 | skipped_fast |
| KITEUSDT | IDLE | 1.72 | 4.29 | 0.0 | 0.08 | 69243.07 | 30.48 | skipped_fast |
| BIOUSDT | IDLE | 1.24 | 2.43 | 0.35 | -0.03 | 71419.84 | 3.9 | skipped_fast |
| TELUSDT | IDLE | 1.8 | 3.54 | 0.41 | -0.02 | 89553.26 | 29.52 | skipped_fast |
| HBARUSDT | IDLE | 0.79 | 1.57 | 0.09 | -0.01 | 265563.32 | 1.35 | skipped_fast |
| QNTUSDT | IDLE | 1.07 | 2.1 | 0.23 | 0.05 | 48310.26 | 12.37 | skipped_fast |
| FLUIDUSDT | IDLE | 1.27 | 2.53 | 0.09 | -0.03 | 322.16 | 21.69 | skipped_fast |
| RWAUSDT | IDLE | 0.4 | 0.77 | 0.38 | -0.07 | 56548.42 | 7.69 | skipped_fast |
| MNSRYUSDT | IDLE | 0.35 | 0.69 | 0.04 | -0.02 | 36250.7 | 54.97 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
