# Hulk DIGEST — 2026-10-26T07:44:54Z

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
| XRPUSDT | IDLE | 0.97 | 1.77 | 1.08 | -0.02 | 17637627.55 | 0.78 | skipped_fast |
| ETHUSDT | IDLE | 0.82 | 1.59 | 0.3 | -0.01 | 105876897.28 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.58 | 1.14 | 0.17 | -0.01 | 208585532.02 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.65 | 3.43 | 2.91 | 0.03 | 799115.67 | 4.11 | skipped_fast |
| CHIPUSDT | IDLE | 4.08 | 10.26 | 2.04 | 0.04 | 103423.52 | 17.39 | skipped_fast |
| WUSDT | IDLE | 1.34 | 2.51 | 1.18 | -0.04 | 480073.79 | 13.6 | skipped_fast |
| QNTUSDT | IDLE | 1.22 | 3.64 | 0.54 | 0.05 | 734019.3 | 11.34 | skipped_fast |
| LAUSDT | IDLE | 4.22 | 8.72 | 3.25 | 0.0 | 62331.15 | 38.06 | skipped_fast |
| RWAINCUSDT | IDLE | 2.43 | 4.53 | 4.16 | -0.07 | 67887.2 | 23.42 | skipped_fast |
| ZBCNUSDT | IDLE | 1.74 | 3.14 | 2.57 | 0.01 | 181070.78 | 39.14 | skipped_fast |
| REDUSDT | IDLE | 1.99 | 3.63 | 2.39 | -0.02 | 60387.56 | 15.31 | skipped_fast |
| KITEUSDT | IDLE | 1.65 | 3.01 | 1.88 | 0.0 | 54125.19 | 14.3 | skipped_fast |
| BIOUSDT | IDLE | 1.38 | 2.52 | 1.65 | -0.02 | 61071.93 | 9.1 | skipped_fast |
| CCUSDT | IDLE | 0.87 | 1.58 | 1.05 | 0.0 | 162588.65 | 6.94 | skipped_fast |
| EDELUSDT | IDLE | 0.85 | 2.1 | 1.09 | 0.06 | 140931.01 | 6.29 | skipped_fast |
| WAXLUSDT | IDLE | 1.91 | 3.37 | 2.99 | -0.01 | 52604.54 | 54.98 | skipped_fast |
| HBARUSDT | IDLE | 0.85 | 1.57 | 0.88 | -0.02 | 180410.97 | 6.51 | skipped_fast |
| RIZEUSDT | IDLE | 0.52 | 1.0 | 0.23 | 0.01 | 33145.76 | 59.87 | skipped_fast |
| IOTAUSDT | IDLE | 1.11 | 2.01 | 1.43 | -0.03 | 62366.29 | 23.78 | skipped_fast |
| FLUIDUSDT | IDLE | 0.28 | 1.49 | 0.0 | -0.02 | 19116.06 | 21.48 | skipped_fast |
| RWAUSDT | IDLE | 0.13 | 0.24 | 0.16 | -0.01 | 52859.13 | 23.89 | skipped_fast |
| MNSRYUSDT | IDLE | 0.31 | 0.57 | 0.37 | -0.01 | 38411.09 | 60.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
