# Hulk DIGEST — 2026-10-15T07:36:10Z

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
| PYTHUSDT | IDLE | 3.11 | 9.59 | 3.6 | 0.05 | 2718170.77 | 3.5 | skipped_fast |
| WUSDT | IDLE | 2.15 | 7.71 | 5.38 | -0.1 | 2686060.73 | 17.68 | skipped_fast |
| ETHUSDT | IDLE | 2.0 | 4.16 | 1.95 | -0.05 | 337593194.92 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.75 | 3.27 | 1.53 | -0.05 | 62042804.34 | 0.77 | skipped_fast |
| BTCUSDT | IDLE | 0.99 | 1.88 | 0.71 | -0.03 | 545760372.64 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 2.22 | 6.67 | 3.83 | -0.09 | 1194398.47 | 4.6 | skipped_fast |
| CCUSDT | IDLE | 1.81 | 5.73 | 5.42 | -0.12 | 452813.32 | 6.51 | skipped_fast |
| HBARUSDT | IDLE | 2.02 | 4.37 | 2.44 | -0.06 | 645492.3 | 6.13 | skipped_fast |
| RIZEUSDT | IDLE | 2.36 | 16.03 | 8.83 | -0.04 | 65264.91 | 57.45 | skipped_fast |
| EDELUSDT | IDLE | 2.15 | 5.07 | 3.7 | -0.07 | 204033.69 | 12.6 | skipped_fast |
| CHIPUSDT | IDLE | 1.7 | 11.79 | 10.26 | -0.22 | 121542.86 | 18.02 | skipped_fast |
| BIOUSDT | IDLE | 2.24 | 7.56 | 5.49 | -0.1 | 84148.81 | 4.06 | skipped_fast |
| REDUSDT | IDLE | 2.25 | 4.29 | 1.44 | 0.01 | 66997.07 | 14.6 | skipped_fast |
| ZBCNUSDT | IDLE | 0.84 | 2.34 | 0.14 | -0.06 | 219562.67 | 5.61 | skipped_fast |
| KITEUSDT | IDLE | 1.18 | 5.33 | 4.12 | -0.14 | 77786.96 | 10.89 | skipped_fast |
| RWAINCUSDT | IDLE | 1.24 | 2.68 | 1.46 | 0.01 | 25898.8 | 15.3 | skipped_fast |
| FLUIDUSDT | IDLE | 2.02 | 6.25 | 2.73 | -0.04 | 21489.86 | 21.3 | skipped_fast |
| TELUSDT | IDLE | 1.4 | 2.6 | 1.27 | -0.04 | 100289.86 | 17.48 | skipped_fast |
| MNSRYUSDT | IDLE | 0.84 | 1.5 | 1.18 | -0.02 | 31932.43 | 25.6 | skipped_fast |
| RWAUSDT | IDLE | 0.62 | 1.13 | 0.8 | -0.03 | 54908.77 | 16.12 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
