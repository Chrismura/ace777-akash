# Hulk DIGEST — 2026-09-02T17:50:34Z

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
| XRPUSDT | IDLE | 1.14 | 2.19 | 0.65 | -0.02 | 39279449.14 | 1.5 | skipped_fast |
| ETHUSDT | IDLE | 1.05 | 1.93 | 1.07 | -0.02 | 414150041.86 | 0.08 | skipped_fast |
| PYTHUSDT | IDLE | 2.16 | 10.66 | 2.39 | 0.14 | 1328494.37 | 5.18 | skipped_fast |
| BTCUSDT | IDLE | 0.65 | 1.26 | 0.24 | -0.0 | 542957247.85 | 0.0 | skipped_fast |
| CHIPUSDT | IDLE | 2.49 | 9.13 | 6.61 | -0.02 | 1035070.15 | 2.44 | skipped_fast |
| WUSDT | IDLE | 1.9 | 3.6 | 1.28 | -0.02 | 355983.07 | 11.53 | skipped_fast |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.55 | 11.33 | 0.71 | 0.0 | 38167.13 | 74.01 | skipped_fast |
| CCUSDT | IDLE | 1.45 | 2.56 | 2.23 | -0.05 | 353256.19 | 0.91 | skipped_fast |
| ZBCNUSDT | IDLE | 2.41 | 4.3 | 3.46 | -0.06 | 176848.82 | 39.43 | skipped_fast |
| KITEUSDT | IDLE | 1.76 | 8.95 | 0.0 | 0.19 | 98574.1 | 14.45 | skipped_fast |
| RWAINCUSDT | IDLE | 1.97 | 5.69 | 2.96 | 0.07 | 10094.13 | 27.17 | skipped_fast |
| REDUSDT | IDLE | 1.25 | 2.43 | 0.48 | 0.03 | 151635.24 | 9.51 | skipped_fast |
| EDELUSDT | IDLE | 0.66 | 3.52 | 2.59 | 0.07 | 169636.71 | 24.95 | skipped_fast |
| BIOUSDT | IDLE | 0.86 | 1.67 | 0.35 | -0.02 | 68544.48 | 3.93 | skipped_fast |
| TELUSDT | IDLE | 1.95 | 3.77 | 0.81 | 0.01 | 77624.44 | 52.4 | skipped_fast |
| FLUIDUSDT | IDLE | 1.96 | 3.74 | 1.74 | -0.06 | 1875.95 | 23.96 | skipped_fast |
| HBARUSDT | IDLE | 0.77 | 1.46 | 0.54 | -0.01 | 208682.07 | 1.36 | skipped_fast |
| QNTUSDT | IDLE | 1.36 | 2.69 | 0.21 | 0.01 | 64098.56 | 7.67 | skipped_fast |
| RWAUSDT | IDLE | 1.26 | 2.47 | 0.38 | 0.02 | 51687.24 | 7.56 | skipped_fast |
| MNSRYUSDT | IDLE | 0.26 | 0.51 | 0.12 | -0.01 | 32230.35 | 28.88 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
