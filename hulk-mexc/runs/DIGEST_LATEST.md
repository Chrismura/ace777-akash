# Hulk DIGEST — 2026-09-02T21:59:27Z

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
| XRPUSDT | IDLE | 1.14 | 2.2 | 0.54 | -0.0 | 36222938.25 | 1.48 | skipped_fast |
| ETHUSDT | IDLE | 0.71 | 1.33 | 0.56 | -0.01 | 356561678.4 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.42 | 0.79 | 0.34 | 0.0 | 508228763.33 | 0.01 | skipped_fast |
| PYTHUSDT | IDLE | 1.09 | 3.96 | 2.27 | 0.13 | 1341930.34 | 3.45 | skipped_fast |
| CHIPUSDT | IDLE | 1.58 | 6.3 | 0.87 | -0.05 | 984630.42 | 7.09 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.36 | 33.7 | 15.86 | 0.09 | 49468.33 | 95.08 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.47 | 8.19 | 1.88 | -0.03 | 184205.68 | 6.67 | skipped_fast |
| WUSDT | IDLE | 2.13 | 4.07 | 1.31 | -0.0 | 248035.39 | 10.24 | skipped_fast |
| CCUSDT | IDLE | 1.38 | 2.52 | 1.61 | -0.03 | 410023.74 | 7.28 | skipped_fast |
| KITEUSDT | IDLE | 1.6 | 7.81 | 2.32 | 0.17 | 140202.97 | 9.06 | skipped_fast |
| BIOUSDT | IDLE | 1.99 | 3.59 | 2.54 | -0.0 | 68796.66 | 11.83 | skipped_fast |
| EDELUSDT | IDLE | 1.37 | 7.24 | 5.61 | 0.07 | 161732.82 | 43.01 | skipped_fast |
| RWAINCUSDT | IDLE | 2.1 | 6.05 | 0.79 | 0.1 | 10828.71 | 37.16 | skipped_fast |
| REDUSDT | IDLE | 1.03 | 1.85 | 1.43 | 0.0 | 113432.67 | 19.21 | skipped_fast |
| QNTUSDT | IDLE | 1.93 | 3.44 | 2.8 | 0.0 | 59862.35 | 10.96 | skipped_fast |
| HBARUSDT | IDLE | 0.74 | 1.46 | 0.16 | -0.0 | 181590.37 | 2.7 | skipped_fast |
| TELUSDT | IDLE | 1.45 | 2.66 | 1.56 | 0.03 | 75630.94 | 41.02 | skipped_fast |
| RWAUSDT | IDLE | 1.16 | 2.16 | 1.13 | 0.01 | 52089.93 | 15.26 | skipped_fast |
| FLUIDUSDT | IDLE | 0.41 | 0.83 | 0.0 | -0.01 | 2377.13 | 20.76 | skipped_fast |
| MNSRYUSDT | IDLE | 0.26 | 0.5 | 0.12 | 0.0 | 24325.29 | 30.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
