# Hulk DIGEST — 2026-10-29T09:10:01Z

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
| XRPUSDT | IDLE | 0.73 | 1.35 | 0.72 | -0.03 | 23915279.59 | 0.77 | skipped_fast |
| ETHUSDT | IDLE | 0.69 | 1.31 | 0.43 | -0.02 | 236882404.79 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.48 | 0.91 | 0.39 | -0.02 | 347010696.84 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.86 | 3.52 | 1.39 | -0.03 | 502165.7 | 16.87 | skipped_fast |
| PYTHUSDT | IDLE | 1.58 | 2.97 | 1.23 | -0.02 | 455263.23 | 5.67 | skipped_fast |
| CCUSDT | IDLE | 0.6 | 1.41 | 0.29 | -0.04 | 424962.77 | 5.16 | skipped_fast |
| QNTUSDT | IDLE | 1.56 | 2.91 | 1.42 | -0.03 | 432820.16 | 5.69 | skipped_fast |
| HBARUSDT | IDLE | 1.0 | 1.89 | 0.68 | -0.03 | 557104.96 | 6.76 | skipped_fast |
| EDELUSDT | IDLE | 1.42 | 2.57 | 1.82 | -0.05 | 169017.51 | 15.95 | skipped_fast |
| LAUSDT | IDLE | 3.19 | 5.76 | 4.15 | -0.04 | 56851.75 | 26.29 | skipped_fast |
| CHIPUSDT | IDLE | 0.67 | 3.55 | 1.34 | -0.11 | 242707.9 | 8.37 | skipped_fast |
| BIOUSDT | IDLE | 1.49 | 2.85 | 0.8 | -0.03 | 67730.99 | 9.01 | skipped_fast |
| REDUSDT | IDLE | 1.54 | 2.85 | 1.47 | -0.03 | 64348.54 | 16.24 | skipped_fast |
| ZBCNUSDT | IDLE | 0.8 | 1.43 | 1.08 | -0.01 | 256835.93 | 34.6 | skipped_fast |
| RWAINCUSDT | IDLE | 1.12 | 4.82 | 1.25 | -0.03 | 29837.5 | 7.06 | skipped_fast |
| FLUIDUSDT | IDLE | 2.36 | 4.39 | 3.95 | -0.06 | 6071.59 | 21.55 | skipped_fast |
| KITEUSDT | IDLE | 0.79 | 1.51 | 0.44 | -0.03 | 60651.86 | 11.55 | skipped_fast |
| RIZEUSDT | IDLE | 1.09 | 2.12 | 0.35 | -0.03 | 37620.91 | 39.89 | skipped_fast |
| WAXLUSDT | IDLE | 1.69 | 4.01 | 1.92 | -0.06 | 53755.75 | 43.49 | skipped_fast |
| IOTAUSDT | IDLE | 1.09 | 2.11 | 0.81 | -0.05 | 101586.82 | 19.87 | skipped_fast |
| RWAUSDT | IDLE | 1.1 | 2.01 | 1.26 | 0.0 | 55899.58 | 8.0 | skipped_fast |
| MNSRYUSDT | IDLE | 0.29 | 0.53 | 0.35 | -0.01 | 37410.19 | 56.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
