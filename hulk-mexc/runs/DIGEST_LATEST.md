# Hulk DIGEST — 2026-09-02T16:48:55Z

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
| XRPUSDT | IDLE | 1.28 | 2.41 | 0.95 | -0.02 | 39619591.22 | 0.75 | skipped_fast |
| ETHUSDT | IDLE | 1.17 | 2.16 | 1.23 | -0.02 | 407096302.47 | 0.04 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.34 | 11.57 | 10.26 | -0.06 | 1028597.6 | 2.47 | skipped_fast |
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 10.66 | 1.58 | 0.16 | 1304788.83 | 3.42 | skipped_fast |
| BTCUSDT | IDLE | 0.82 | 1.58 | 0.42 | -0.0 | 541375669.62 | 0.02 | skipped_fast |
| REDUSDT | IDLE | 2.8 | 5.41 | 1.26 | 0.02 | 159184.98 | 11.33 | skipped_fast |
| WUSDT | IDLE | 1.82 | 3.6 | 0.24 | -0.0 | 367009.25 | 16.61 | skipped_fast |
| CCUSDT | IDLE | 1.37 | 2.61 | 0.86 | -0.02 | 354965.64 | 2.7 | skipped_fast |
| KITEUSDT | IDLE | 1.8 | 7.6 | 1.34 | 0.13 | 98320.48 | 7.88 | skipped_fast |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.66 | 8.53 | 0.31 | -0.04 | 38212.99 | 76.25 | skipped_fast |
| ZBCNUSDT | IDLE | 1.23 | 2.25 | 1.34 | -0.05 | 177051.53 | 11.6 | skipped_fast |
| RWAINCUSDT | IDLE | 1.91 | 5.69 | 2.38 | 0.1 | 10441.8 | 37.79 | skipped_fast |
| BIOUSDT | IDLE | 0.96 | 1.8 | 0.78 | -0.02 | 70035.46 | 3.95 | skipped_fast |
| EDELUSDT | IDLE | 0.68 | 3.61 | 2.51 | 0.05 | 170039.25 | 57.92 | skipped_fast |
| FLUIDUSDT | IDLE | 2.0 | 3.74 | 2.33 | -0.06 | 1836.1 | 21.68 | skipped_fast |
| TELUSDT | IDLE | 1.69 | 3.24 | 0.87 | 0.0 | 75264.35 | 23.49 | skipped_fast |
| HBARUSDT | IDLE | 0.89 | 1.64 | 1.0 | -0.01 | 199932.36 | 1.36 | skipped_fast |
| RWAUSDT | IDLE | 1.26 | 2.47 | 0.38 | 0.02 | 51546.02 | 7.56 | skipped_fast |
| QNTUSDT | IDLE | 1.05 | 2.0 | 0.68 | 0.02 | 68646.88 | 1.55 | skipped_fast |
| MNSRYUSDT | IDLE | 0.27 | 0.52 | 0.19 | -0.01 | 33090.97 | 50.94 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
