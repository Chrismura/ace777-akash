# Hulk DIGEST — 2026-10-20T18:21:37Z

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
| XRPUSDT | IDLE | 2.08 | 3.93 | 1.6 | 0.02 | 23544061.32 | 0.75 | skipped_fast |
| ETHUSDT | IDLE | 2.05 | 3.91 | 1.29 | 0.02 | 148836706.69 | 0.65 | skipped_fast |
| BTCUSDT | IDLE | 1.34 | 2.55 | 0.93 | 0.01 | 323731692.39 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 3.26 | 7.6 | 1.29 | 0.07 | 1006437.36 | 3.87 | skipped_fast |
| WUSDT | IDLE | 3.17 | 6.16 | 1.26 | 0.01 | 694652.66 | 14.98 | skipped_fast |
| QNTUSDT | IDLE | 3.27 | 6.0 | 3.58 | 0.01 | 720408.37 | 1.02 | skipped_fast |
| ZBCNUSDT | IDLE | 4.07 | 7.65 | 3.32 | 0.02 | 190266.33 | 22.0 | skipped_fast |
| CHIPUSDT | IDLE | 2.78 | 9.87 | 4.58 | 0.08 | 175401.56 | 11.07 | skipped_fast |
| EDELUSDT | IDLE | 1.63 | 15.52 | 2.46 | 0.32 | 336942.53 | 19.58 | skipped_fast |
| CCUSDT | IDLE | 1.8 | 3.41 | 1.26 | 0.02 | 407928.46 | 4.74 | skipped_fast |
| REDUSDT | IDLE | 2.96 | 5.63 | 1.88 | 0.03 | 59533.0 | 7.88 | skipped_fast |
| BIOUSDT | IDLE | 2.95 | 5.72 | 1.16 | 0.06 | 63112.38 | 8.11 | skipped_fast |
| HBARUSDT | IDLE | 2.54 | 4.66 | 2.83 | 0.01 | 399779.52 | 4.8 | skipped_fast |
| KITEUSDT | IDLE | 1.89 | 3.46 | 2.08 | 0.02 | 84830.54 | 9.04 | skipped_fast |
| IOTAUSDT | IDLE | 3.17 | 5.95 | 3.47 | 0.05 | 92707.79 | 25.83 | skipped_fast |
| LAUSDT | IDLE | 3.13 | 6.0 | 1.74 | 0.03 | 56335.45 | 22.41 | skipped_fast |
| RWAINCUSDT | IDLE | 1.32 | 4.0 | 3.53 | -0.05 | 71385.84 | 5.38 | skipped_fast |
| WAXLUSDT | IDLE | 2.98 | 5.42 | 3.58 | -0.04 | 55925.34 | 46.58 | skipped_fast |
| RIZEUSDT | IDLE | 1.05 | 4.33 | 1.8 | 0.02 | 69664.99 | 60.97 | skipped_fast |
| FLUIDUSDT | IDLE | 2.12 | 4.1 | 1.0 | 0.05 | 4946.21 | 16.42 | skipped_fast |
| RWAUSDT | IDLE | 0.78 | 1.42 | 0.93 | 0.01 | 52051.61 | 7.84 | skipped_fast |
| MNSRYUSDT | IDLE | 0.82 | 1.52 | 0.86 | 0.0 | 40312.57 | 19.94 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
