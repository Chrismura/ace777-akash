# Hulk DIGEST — 2026-09-01T23:28:48Z

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
| XRPUSDT | IDLE | 1.09 | 1.99 | 1.33 | -0.02 | 35232290.16 | 1.48 | skipped_fast |
| ETHUSDT | IDLE | 0.9 | 1.74 | 0.4 | -0.02 | 341993411.9 | 0.17 | skipped_fast |
| BTCUSDT | IDLE | 0.74 | 1.44 | 0.24 | -0.02 | 527440369.57 | 0.0 | skipped_fast |
| CHIPUSDT | IDLE | 2.24 | 11.2 | 3.42 | 0.15 | 737532.36 | 2.25 | skipped_fast |
| PYTHUSDT | IDLE | 2.89 | 5.74 | 0.29 | 0.06 | 695973.92 | 1.92 | skipped_fast |
| WUSDT | IDLE | 2.27 | 4.18 | 3.52 | 0.04 | 410031.21 | 1.04 | skipped_fast |
| ZBCNUSDT | IDLE | 2.3 | 4.07 | 3.56 | -0.01 | 205074.03 | 10.98 | skipped_fast |
| CCUSDT | IDLE | 0.86 | 1.94 | 1.23 | -0.07 | 325340.84 | 9.68 | skipped_fast |
| REDUSDT | IDLE | 1.93 | 5.85 | 3.97 | 0.09 | 118134.38 | 73.98 | skipped_fast |
| KITEUSDT | IDLE | 1.45 | 2.78 | 0.82 | 0.04 | 68096.93 | 10.57 | skipped_fast |
| EDELUSDT | IDLE | 0.71 | 5.41 | 4.95 | -0.09 | 144832.73 | 18.62 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 4.22 | 1.93 | -0.06 | 40848.21 | 74.83 | skipped_fast |
| BIOUSDT | IDLE | 1.07 | 1.9 | 1.55 | -0.05 | 69469.6 | 3.94 | skipped_fast |
| FLUIDUSDT | IDLE | 2.56 | 4.47 | 4.28 | -0.03 | 229.45 | 17.31 | skipped_fast |
| RWAINCUSDT | IDLE | 1.41 | 2.61 | 1.45 | -0.02 | 5822.68 | 29.4 | skipped_fast |
| TELUSDT | IDLE | 2.16 | 3.91 | 2.71 | -0.05 | 94516.47 | 36.34 | skipped_fast |
| HBARUSDT | IDLE | 0.87 | 1.58 | 1.1 | 0.0 | 249392.6 | 1.35 | skipped_fast |
| QNTUSDT | IDLE | 1.52 | 2.91 | 0.87 | 0.04 | 46452.35 | 6.26 | skipped_fast |
| RWAUSDT | IDLE | 0.4 | 0.93 | 0.54 | -0.04 | 58675.61 | 7.71 | skipped_fast |
| MNSRYUSDT | IDLE | 0.82 | 1.46 | 1.14 | -0.02 | 34396.66 | 54.97 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
