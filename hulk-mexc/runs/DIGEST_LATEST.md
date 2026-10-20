# Hulk DIGEST — 2026-10-20T07:10:47Z

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
| ETHUSDT | IDLE | 0.65 | 1.18 | 0.85 | -0.01 | 126618549.5 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.48 | 0.87 | 0.57 | -0.01 | 299286531.59 | 0.0 | skipped_fast |
| XRPUSDT | IDLE | 0.49 | 0.9 | 0.47 | -0.01 | 20464160.51 | 1.54 | skipped_fast |
| PYTHUSDT | IDLE | 1.69 | 3.09 | 1.95 | -0.04 | 1040683.11 | 2.76 | skipped_fast |
| WUSDT | IDLE | 2.08 | 3.83 | 2.22 | 0.01 | 744158.13 | 13.83 | skipped_fast |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.43 | 14.0 | 0.59 | 0.11 | 249391.22 | 16.42 | skipped_fast |
| CCUSDT | IDLE | 2.43 | 4.35 | 3.34 | 0.01 | 481565.71 | 8.64 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.58 | 13.3 | 10.82 | -0.07 | 66876.24 | 65.54 | skipped_fast |
| QNTUSDT | IDLE | 2.14 | 3.91 | 2.47 | -0.02 | 706043.92 | 1.03 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.98 | 8.0 | 0.22 | 0.04 | 93261.5 | 15.66 | skipped_fast |
| ZBCNUSDT | IDLE | 1.34 | 2.41 | 1.79 | -0.02 | 160120.56 | 15.88 | skipped_fast |
| KITEUSDT | IDLE | 1.51 | 3.02 | 2.27 | 0.07 | 79376.12 | 9.01 | skipped_fast |
| RWAINCUSDT | IDLE | 1.2 | 2.25 | 1.02 | 0.04 | 73674.13 | 5.17 | skipped_fast |
| BIOUSDT | IDLE | 1.1 | 2.06 | 0.92 | -0.0 | 66716.61 | 4.24 | skipped_fast |
| REDUSDT | IDLE | 1.06 | 2.01 | 0.77 | 0.01 | 58218.93 | 10.88 | skipped_fast |
| HBARUSDT | IDLE | 0.97 | 1.9 | 0.26 | -0.01 | 365416.02 | 4.77 | skipped_fast |
| FLUIDUSDT | IDLE | 2.3 | 4.4 | 1.28 | -0.01 | 4185.78 | 12.81 | skipped_fast |
| IOTAUSDT | IDLE | 1.44 | 2.74 | 0.97 | 0.01 | 89649.85 | 28.42 | skipped_fast |
| LAUSDT | IDLE | 1.21 | 2.21 | 1.35 | -0.01 | 55463.82 | 20.97 | skipped_fast |
| WAXLUSDT | IDLE | 1.26 | 3.0 | 0.95 | -0.05 | 56957.33 | 69.08 | skipped_fast |
| MNSRYUSDT | IDLE | 0.13 | 0.26 | 0.06 | 0.0 | 39994.59 | 7.12 | skipped_fast |
| RWAUSDT | IDLE | 0.13 | 0.24 | 0.16 | 0.01 | 51635.56 | 23.54 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
