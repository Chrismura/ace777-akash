# Hulk DIGEST — 2026-10-26T17:26:12Z

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
| ETHUSDT | IDLE | 1.1 | 2.11 | 0.62 | -0.01 | 138185654.9 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.05 | 2.01 | 0.6 | -0.01 | 24354320.82 | 1.54 | skipped_fast |
| BTCUSDT | IDLE | 0.88 | 1.69 | 0.5 | -0.0 | 346545491.59 | 0.25 | skipped_fast |
| QNTUSDT | IDLE | 1.9 | 7.97 | 6.59 | 0.1 | 1507925.74 | 5.27 | skipped_fast |
| PYTHUSDT | IDLE | 2.05 | 3.76 | 2.22 | 0.03 | 943225.91 | 3.99 | skipped_fast |
| WUSDT | IDLE | 3.18 | 6.6 | 1.15 | 0.02 | 600806.25 | 35.32 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.22 | 13.37 | 9.95 | -0.14 | 63001.94 | 19.13 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.23 | 15.42 | 1.94 | 0.2 | 265856.81 | 24.26 | skipped_fast |
| EDELUSDT | IDLE | 2.2 | 4.44 | 1.48 | 0.08 | 123858.79 | 30.54 | skipped_fast |
| RIZEUSDT | IDLE | 2.49 | 4.69 | 1.93 | -0.0 | 29077.71 | 67.22 | skipped_fast |
| BIOUSDT | IDLE | 1.74 | 3.28 | 1.32 | -0.01 | 60145.46 | 4.48 | skipped_fast |
| ZBCNUSDT | IDLE | 1.26 | 2.63 | 1.78 | -0.08 | 204890.88 | 29.77 | skipped_fast |
| REDUSDT | IDLE | 1.57 | 2.98 | 1.1 | 0.01 | 63006.41 | 14.93 | skipped_fast |
| CCUSDT | IDLE | 0.94 | 1.7 | 1.14 | -0.02 | 190912.9 | 10.96 | skipped_fast |
| KITEUSDT | IDLE | 1.2 | 2.22 | 1.23 | 0.0 | 53791.6 | 11.45 | skipped_fast |
| HBARUSDT | IDLE | 1.06 | 1.97 | 1.06 | -0.01 | 243449.34 | 7.78 | skipped_fast |
| WAXLUSDT | IDLE | 2.05 | 4.01 | 0.57 | -0.01 | 53686.35 | 46.91 | skipped_fast |
| LAUSDT | IDLE | 1.69 | 3.41 | 1.9 | 0.01 | 66992.98 | 22.29 | skipped_fast |
| IOTAUSDT | IDLE | 1.31 | 2.44 | 1.2 | -0.01 | 76918.22 | 2.34 | skipped_fast |
| FLUIDUSDT | IDLE | 1.31 | 2.35 | 2.0 | -0.04 | 1388.64 | 21.55 | skipped_fast |
| RWAUSDT | IDLE | 0.77 | 1.44 | 0.63 | -0.0 | 54533.47 | 31.85 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.74 | 0.18 | -0.01 | 42909.62 | 73.51 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
