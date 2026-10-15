# Hulk DIGEST — 2026-10-15T23:20:32Z

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
| WUSDT | IDLE | 1.41 | 3.79 | 3.59 | -0.05 | 2844361.76 | 15.88 | skipped_fast |
| PYTHUSDT | IDLE | 0.94 | 5.32 | 4.0 | 0.09 | 4488808.61 | 1.08 | skipped_fast |
| ETHUSDT | IDLE | 0.71 | 1.26 | 1.06 | 0.01 | 310598850.81 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.66 | 1.15 | 1.09 | -0.0 | 47637664.01 | 0.75 | skipped_fast |
| BTCUSDT | IDLE | 0.45 | 0.82 | 0.5 | 0.01 | 501916472.76 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.8 | 5.19 | 4.89 | -0.01 | 1356197.92 | 2.46 | skipped_fast |
| CCUSDT | IDLE | 1.21 | 2.56 | 2.5 | -0.08 | 470140.04 | 10.4 | skipped_fast |
| ZBCNUSDT | IDLE | 1.76 | 3.49 | 2.64 | 0.02 | 218132.99 | 13.07 | skipped_fast |
| EDELUSDT | IDLE | 1.32 | 4.73 | 2.92 | -0.12 | 239946.98 | 20.51 | skipped_fast |
| RIZEUSDT | IDLE | 1.96 | 7.69 | 2.48 | 0.05 | 81676.56 | 43.08 | skipped_fast |
| KITEUSDT | IDLE | 1.52 | 2.71 | 2.38 | -0.03 | 68948.48 | 17.08 | skipped_fast |
| CHIPUSDT | IDLE | 0.95 | 4.64 | 1.6 | -0.08 | 152963.13 | 14.84 | skipped_fast |
| HBARUSDT | IDLE | 1.31 | 2.48 | 0.91 | 0.0 | 301424.58 | 8.25 | skipped_fast |
| REDUSDT | IDLE | 0.72 | 2.07 | 2.03 | -0.02 | 72684.84 | 9.64 | skipped_fast |
| RWAINCUSDT | IDLE | 0.86 | 1.76 | 1.53 | 0.01 | 28912.75 | 10.0 | skipped_fast |
| BIOUSDT | IDLE | 0.49 | 1.05 | 0.85 | -0.03 | 83915.32 | 7.78 | skipped_fast |
| TELUSDT | IDLE | 1.01 | 1.99 | 0.22 | 0.01 | 90327.22 | 22.4 | skipped_fast |
| RWAUSDT | IDLE | 0.93 | 1.67 | 1.33 | 0.0 | 54578.18 | 15.9 | skipped_fast |
| FLUIDUSDT | IDLE | 1.0 | 2.38 | 1.2 | -0.04 | 10668.59 | 17.27 | skipped_fast |
| MNSRYUSDT | IDLE | 0.18 | 0.35 | 0.1 | -0.0 | 35130.07 | 4.23 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
