# Hulk DIGEST — 2026-10-14T08:14:17Z

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
| PYTHUSDT | IDLE | 2.63 | 5.96 | 1.36 | -0.03 | 1813937.29 | 2.42 | skipped_fast |
| WUSDT | IDLE | 0.74 | 4.84 | 1.06 | -0.15 | 3737620.86 | 7.88 | skipped_fast |
| XRPUSDT | IDLE | 0.88 | 1.73 | 0.25 | 0.0 | 30344543.43 | 1.45 | skipped_fast |
| ETHUSDT | IDLE | 0.6 | 1.16 | 0.26 | -0.0 | 134198287.51 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.49 | 0.94 | 0.21 | -0.0 | 331772411.46 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 0.98 | 2.86 | 1.16 | -0.05 | 1680982.75 | 1.4 | skipped_fast |
| CCUSDT | IDLE | 1.27 | 2.55 | 2.04 | -0.01 | 581400.89 | 10.58 | skipped_fast |
| KITEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.82 | 9.52 | 0.41 | 0.1 | 71848.29 | 7.77 | skipped_fast |
| CHIPUSDT | IDLE | 2.76 | 5.16 | 2.44 | -0.04 | 81102.58 | 15.66 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 6.35 | 1.71 | 0.04 | 53005.92 | 59.36 | skipped_fast |
| EDELUSDT | IDLE | 1.18 | 2.31 | 0.35 | 0.04 | 216561.91 | 40.57 | skipped_fast |
| REDUSDT | IDLE | 1.44 | 2.74 | 0.89 | -0.0 | 84575.11 | 13.86 | skipped_fast |
| BIOUSDT | IDLE | 1.07 | 2.05 | 0.65 | -0.01 | 69156.47 | 7.22 | skipped_fast |
| ZBCNUSDT | IDLE | 0.57 | 1.1 | 0.29 | -0.02 | 200807.17 | 17.07 | skipped_fast |
| RWAINCUSDT | IDLE | 1.0 | 2.01 | 1.27 | -0.07 | 32462.24 | 10.26 | skipped_fast |
| HBARUSDT | IDLE | 0.82 | 1.61 | 0.18 | -0.01 | 289023.35 | 6.85 | skipped_fast |
| FLUIDUSDT | IDLE | 1.89 | 5.85 | 1.8 | 0.06 | 21308.25 | 21.58 | skipped_fast |
| TELUSDT | IDLE | 1.02 | 1.91 | 0.83 | 0.02 | 117078.35 | 38.96 | skipped_fast |
| RWAUSDT | IDLE | 0.44 | 0.86 | 0.31 | -0.01 | 55621.79 | 15.55 | skipped_fast |
| MNSRYUSDT | IDLE | 0.02 | 0.03 | 0.03 | -0.01 | 37519.4 | 5.58 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
