# Hulk DIGEST — 2026-09-23T05:07:06Z

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
| XRPUSDT | IDLE | 2.43 | 5.64 | 1.96 | 0.08 | 113982532.02 | 1.85 | skipped_fast |
| PYTHUSDT | IDLE | 1.01 | 4.62 | 2.84 | 0.05 | 1779280.41 | 1.51 | skipped_fast |
| ETHUSDT | IDLE | 0.81 | 1.52 | 0.67 | 0.02 | 406334740.72 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.7 | 1.33 | 0.43 | 0.02 | 878496869.2 | 0.0 | skipped_fast |
| HBARUSDT | IDLE | 1.31 | 2.84 | 1.98 | 0.08 | 1807149.98 | 2.01 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.85 | 9.79 | 1.42 | 0.06 | 220529.07 | 17.55 | skipped_fast |
| WUSDT | IDLE | 1.99 | 3.68 | 1.99 | 0.04 | 319185.67 | 9.0 | skipped_fast |
| CCUSDT | IDLE | 1.4 | 2.72 | 0.58 | -0.02 | 412069.7 | 3.46 | skipped_fast |
| EDELUSDT | IDLE | 1.36 | 6.66 | 2.04 | -0.06 | 271342.94 | 46.45 | skipped_fast |
| CHIPUSDT | IDLE | 1.39 | 2.65 | 1.82 | -0.01 | 199534.1 | 10.77 | skipped_fast |
| BIOUSDT | IDLE | 1.77 | 3.38 | 1.08 | 0.05 | 111232.24 | 13.22 | skipped_fast |
| KITEUSDT | IDLE | 1.27 | 4.42 | 3.35 | 0.12 | 129956.57 | 8.78 | skipped_fast |
| RIZEUSDT | IDLE | 0.92 | 18.71 | 4.24 | 0.47 | 57405.38 | 49.84 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 2.57 | 0.75 | 0.03 | 59421.04 | 13.76 | skipped_fast |
| QNTUSDT | IDLE | 1.08 | 3.57 | 1.57 | 0.12 | 213343.74 | 7.96 | skipped_fast |
| RWAINCUSDT | IDLE | 0.62 | 1.57 | 0.69 | 0.04 | 21227.29 | 5.4 | skipped_fast |
| TELUSDT | IDLE | 0.89 | 3.93 | 0.8 | 0.15 | 108972.57 | 42.99 | skipped_fast |
| FLUIDUSDT | IDLE | 1.23 | 2.42 | 0.33 | 0.03 | 4320.56 | 43.15 | skipped_fast |
| RWAUSDT | IDLE | 0.44 | 0.8 | 0.5 | 0.01 | 53035.64 | 14.42 | skipped_fast |
| MNSRYUSDT | IDLE | 0.36 | 0.72 | 0.05 | 0.01 | 40103.82 | 6.4 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
