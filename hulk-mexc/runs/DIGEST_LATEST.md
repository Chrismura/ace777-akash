# Hulk DIGEST — 2026-10-21T01:28:51Z

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
| XRPUSDT | IDLE | 0.71 | 1.36 | 0.42 | 0.03 | 24329648.18 | 0.75 | skipped_fast |
| ETHUSDT | IDLE | 0.65 | 1.23 | 0.5 | 0.03 | 170226106.71 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.44 | 0.84 | 0.28 | 0.02 | 327114119.57 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.21 | 3.77 | 1.98 | 0.1 | 1190149.51 | 3.76 | skipped_fast |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 3.5 | 13.11 | 11.59 | -0.06 | 80535.38 | 11.12 | skipped_fast |
| WUSDT | IDLE | 1.53 | 2.76 | 2.01 | 0.03 | 652934.92 | 18.73 | skipped_fast |
| QNTUSDT | IDLE | 1.55 | 2.98 | 0.85 | 0.02 | 810899.08 | 0.51 | skipped_fast |
| CHIPUSDT | IDLE | 0.93 | 2.9 | 2.68 | 0.06 | 445506.5 | 9.04 | skipped_fast |
| CCUSDT | IDLE | 0.95 | 1.76 | 0.98 | 0.01 | 369812.74 | 12.34 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.02 | 12.76 | 10.01 | 0.07 | 17191.27 | 21.48 | skipped_fast |
| EDELUSDT | IDLE | 0.41 | 3.64 | 0.5 | 0.34 | 364565.43 | 16.67 | skipped_fast |
| RIZEUSDT | IDLE | 1.74 | 6.76 | 5.69 | 0.04 | 75379.94 | 64.04 | skipped_fast |
| ZBCNUSDT | IDLE | 1.32 | 2.6 | 0.28 | 0.04 | 192756.27 | 22.23 | skipped_fast |
| BIOUSDT | IDLE | 1.02 | 1.84 | 1.28 | 0.05 | 60923.02 | 4.06 | skipped_fast |
| REDUSDT | IDLE | 1.02 | 1.97 | 0.42 | 0.04 | 58185.62 | 18.32 | skipped_fast |
| KITEUSDT | IDLE | 0.73 | 1.33 | 0.86 | 0.0 | 73449.08 | 9.04 | skipped_fast |
| HBARUSDT | IDLE | 0.79 | 1.47 | 0.67 | 0.02 | 349062.65 | 7.14 | skipped_fast |
| WAXLUSDT | IDLE | 1.87 | 3.28 | 3.01 | -0.03 | 56250.74 | 9.49 | skipped_fast |
| LAUSDT | IDLE | 1.73 | 3.4 | 0.45 | 0.06 | 54715.72 | 20.05 | skipped_fast |
| IOTAUSDT | IDLE | 0.93 | 1.64 | 1.44 | 0.03 | 75100.38 | 21.55 | skipped_fast |
| MNSRYUSDT | IDLE | 0.21 | 0.41 | 0.09 | -0.0 | 39747.06 | 7.12 | skipped_fast |
| RWAUSDT | IDLE | 0.33 | 0.63 | 0.23 | 0.0 | 52824.06 | 31.3 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
