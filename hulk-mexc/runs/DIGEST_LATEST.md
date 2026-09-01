# Hulk DIGEST — 2026-09-01T21:28:09Z

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
| XRPUSDT | IDLE | 1.67 | 3.01 | 2.14 | -0.03 | 34432916.15 | 2.22 | skipped_fast |
| ETHUSDT | IDLE | 1.5 | 2.8 | 1.4 | -0.02 | 331123902.53 | 0.21 | skipped_fast |
| BTCUSDT | IDLE | 1.09 | 2.04 | 0.98 | -0.02 | 534402301.25 | 0.0 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.19 | 11.2 | 1.68 | 0.17 | 631418.0 | 6.63 | skipped_fast |
| PYTHUSDT | IDLE | 1.98 | 3.94 | 0.1 | 0.04 | 661623.92 | 3.91 | skipped_fast |
| ZBCNUSDT | IDLE | 3.52 | 6.37 | 4.44 | 0.01 | 201450.18 | 16.66 | skipped_fast |
| WUSDT | IDLE | 2.0 | 4.18 | 1.46 | 0.07 | 395175.95 | 10.2 | skipped_fast |
| CCUSDT | IDLE | 1.56 | 3.39 | 2.95 | -0.08 | 334418.07 | 10.59 | skipped_fast |
| REDUSDT | IDLE | 1.91 | 5.97 | 2.97 | 0.09 | 115314.17 | 11.33 | skipped_fast |
| BIOUSDT | IDLE | 1.96 | 3.43 | 3.24 | -0.04 | 70468.4 | 7.88 | skipped_fast |
| RIZEUSDT | IDLE | 2.63 | 4.92 | 3.37 | -0.05 | 43753.69 | 75.1 | skipped_fast |
| KITEUSDT | IDLE | 1.58 | 3.03 | 0.89 | 0.04 | 68604.91 | 13.0 | skipped_fast |
| EDELUSDT | IDLE | 0.85 | 6.39 | 5.4 | -0.08 | 134719.11 | 45.81 | skipped_fast |
| RWAINCUSDT | IDLE | 1.48 | 2.8 | 1.04 | -0.02 | 6420.69 | 17.56 | skipped_fast |
| TELUSDT | IDLE | 2.65 | 4.83 | 3.09 | -0.05 | 93966.4 | 54.27 | skipped_fast |
| FLUIDUSDT | IDLE | 2.52 | 4.41 | 4.22 | -0.03 | 129.84 | 21.91 | skipped_fast |
| HBARUSDT | IDLE | 0.89 | 1.66 | 0.78 | 0.0 | 250435.15 | 1.35 | skipped_fast |
| QNTUSDT | IDLE | 1.56 | 2.79 | 2.22 | 0.03 | 47412.06 | 6.35 | skipped_fast |
| MNSRYUSDT | IDLE | 0.93 | 1.66 | 1.3 | -0.02 | 34424.73 | 39.93 | skipped_fast |
| RWAUSDT | IDLE | 0.41 | 0.93 | 0.69 | -0.01 | 59381.53 | 7.72 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
