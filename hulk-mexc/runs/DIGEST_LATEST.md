# Hulk DIGEST — 2026-10-14T22:27:05Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.01 | 8.93 | 1.95 | 0.1 | 2054336.65 | 3.51 | skipped_fast |
| WUSDT | IDLE | 1.3 | 4.66 | 2.79 | -0.11 | 2368726.5 | 9.14 | skipped_fast |
| ETHUSDT | IDLE | 1.12 | 2.01 | 1.6 | -0.04 | 233190396.79 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.87 | 1.65 | 0.64 | -0.03 | 46669394.13 | 1.5 | skipped_fast |
| BTCUSDT | IDLE | 0.38 | 0.68 | 0.59 | -0.02 | 445318832.19 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 2.2 | 4.0 | 2.7 | -0.04 | 1101379.1 | 2.45 | skipped_fast |
| CCUSDT | IDLE | 1.84 | 3.74 | 3.52 | -0.08 | 401805.93 | 6.94 | skipped_fast |
| RWAINCUSDT | IDLE | 3.39 | 8.46 | 2.19 | -0.03 | 26546.83 | 10.17 | skipped_fast |
| ZBCNUSDT | IDLE | 2.14 | 3.89 | 2.62 | -0.03 | 204898.52 | 2.28 | skipped_fast |
| EDELUSDT | IDLE | 2.37 | 4.34 | 2.67 | -0.03 | 174721.89 | 18.05 | skipped_fast |
| KITEUSDT | IDLE | 1.85 | 5.27 | 4.17 | -0.01 | 86722.58 | 8.64 | skipped_fast |
| HBARUSDT | IDLE | 1.19 | 2.29 | 0.65 | -0.03 | 531907.81 | 2.36 | skipped_fast |
| CHIPUSDT | IDLE | 1.3 | 3.68 | 3.55 | -0.08 | 101644.32 | 13.41 | skipped_fast |
| BIOUSDT | IDLE | 1.48 | 2.71 | 1.64 | -0.04 | 66727.53 | 7.55 | skipped_fast |
| TELUSDT | IDLE | 2.61 | 4.58 | 4.27 | -0.02 | 100627.79 | 28.58 | skipped_fast |
| REDUSDT | IDLE | 1.19 | 2.29 | 0.63 | 0.01 | 61961.85 | 10.19 | skipped_fast |
| RIZEUSDT | IDLE | 0.65 | 3.64 | 1.96 | -0.01 | 49847.87 | 61.89 | skipped_fast |
| FLUIDUSDT | IDLE | 1.31 | 4.08 | 1.36 | 0.05 | 19165.45 | 21.7 | skipped_fast |
| RWAUSDT | IDLE | 0.32 | 0.56 | 0.48 | -0.03 | 55945.66 | 7.97 | skipped_fast |
| MNSRYUSDT | IDLE | 0.41 | 0.73 | 0.56 | -0.01 | 35981.69 | 35.24 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
