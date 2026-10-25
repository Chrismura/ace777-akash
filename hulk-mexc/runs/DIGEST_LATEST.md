# Hulk DIGEST — 2026-10-25T17:06:46Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| ETHUSDT | IDLE | 0.73 | 1.42 | 0.22 | 0.02 | 88687626.25 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.68 | 1.32 | 0.2 | 0.02 | 14916174.99 | 0.77 | skipped_fast |
| BTCUSDT | IDLE | 0.38 | 0.74 | 0.08 | 0.01 | 145336179.96 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.84 | 3.61 | 0.43 | -0.01 | 631632.77 | 20.57 | skipped_fast |
| ZBCNUSDT | IDLE | 3.71 | 7.49 | 0.52 | 0.08 | 206789.97 | 25.42 | skipped_fast |
| PYTHUSDT | IDLE | 1.6 | 3.08 | 0.78 | 0.05 | 412045.08 | 2.77 | skipped_fast |
| EDELUSDT | IDLE | 1.77 | 3.31 | 1.55 | -0.01 | 407742.97 | 33.49 | skipped_fast |
| KITEUSDT | IDLE | 2.74 | 5.12 | 2.41 | 0.0 | 54122.1 | 13.27 | skipped_fast |
| QNTUSDT | IDLE | 2.05 | 4.09 | 0.03 | 0.07 | 453064.25 | 2.11 | skipped_fast |
| CHIPUSDT | IDLE | 2.18 | 4.83 | 2.73 | 0.04 | 93330.45 | 15.68 | skipped_fast |
| CCUSDT | IDLE | 1.47 | 2.91 | 0.19 | 0.03 | 178644.89 | 11.64 | skipped_fast |
| FLUIDUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.56 | 13.42 | 0.0 | 0.03 | 18769.6 | 21.32 | skipped_fast |
| REDUSDT | IDLE | 1.44 | 2.86 | 0.07 | -0.02 | 66206.16 | 15.16 | skipped_fast |
| BIOUSDT | IDLE | 1.08 | 2.12 | 0.31 | 0.01 | 60400.75 | 4.43 | skipped_fast |
| RWAINCUSDT | IDLE | 0.95 | 1.72 | 1.2 | -0.01 | 58562.17 | 5.5 | skipped_fast |
| RIZEUSDT | IDLE | 1.27 | 2.61 | 1.26 | -0.01 | 45150.63 | 64.89 | skipped_fast |
| WAXLUSDT | IDLE | 1.89 | 3.71 | 0.4 | 0.03 | 53650.79 | 34.13 | skipped_fast |
| HBARUSDT | IDLE | 0.97 | 1.92 | 0.13 | 0.02 | 137544.92 | 11.55 | skipped_fast |
| LAUSDT | IDLE | 1.0 | 4.32 | 0.0 | -0.09 | 70130.5 | 18.82 | skipped_fast |
| IOTAUSDT | IDLE | 1.0 | 1.97 | 0.21 | 0.01 | 61701.73 | 25.43 | skipped_fast |
| RWAUSDT | IDLE | 0.72 | 1.36 | 0.48 | 0.01 | 50979.94 | 15.91 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.74 | 0.13 | 0.0 | 36651.1 | 77.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
