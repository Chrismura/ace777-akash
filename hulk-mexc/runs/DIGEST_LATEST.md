# Hulk DIGEST — 2026-10-19T15:00:46Z

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
| ETHUSDT | IDLE | 1.37 | 2.52 | 1.45 | 0.01 | 159965215.87 | 0.37 | skipped_fast |
| XRPUSDT | IDLE | 1.0 | 1.86 | 0.98 | 0.02 | 31099898.58 | 0.77 | skipped_fast |
| BTCUSDT | IDLE | 0.86 | 1.58 | 0.97 | 0.01 | 340293038.5 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.62 | 4.93 | 2.01 | -0.0 | 963397.18 | 4.05 | skipped_fast |
| QNTUSDT | IDLE | 1.93 | 5.54 | 3.45 | 0.03 | 872751.6 | 5.55 | skipped_fast |
| WUSDT | IDLE | 2.03 | 3.91 | 0.94 | -0.0 | 493155.94 | 16.94 | skipped_fast |
| CCUSDT | IDLE | 1.88 | 4.43 | 1.75 | 0.06 | 367175.7 | 8.62 | skipped_fast |
| RWAINCUSDT | IDLE | 2.29 | 6.71 | 3.34 | 0.06 | 90840.64 | 25.81 | skipped_fast |
| HBARUSDT | IDLE | 1.31 | 2.33 | 1.9 | -0.05 | 585561.7 | 4.84 | skipped_fast |
| CHIPUSDT | IDLE | 1.96 | 5.07 | 3.91 | -0.0 | 83650.39 | 14.67 | skipped_fast |
| EDELUSDT | IDLE | 1.39 | 2.9 | 1.21 | 0.03 | 233358.97 | 14.79 | skipped_fast |
| ZBCNUSDT | IDLE | 0.73 | 2.44 | 2.2 | 0.01 | 264803.8 | 8.54 | skipped_fast |
| KITEUSDT | IDLE | 1.6 | 3.68 | 0.49 | 0.07 | 59319.94 | 10.78 | skipped_fast |
| REDUSDT | IDLE | 1.15 | 2.24 | 0.38 | 0.01 | 59294.42 | 8.01 | skipped_fast |
| BIOUSDT | IDLE | 1.11 | 2.07 | 0.97 | 0.01 | 70990.23 | 12.78 | skipped_fast |
| RIZEUSDT | IDLE | 1.4 | 2.63 | 1.07 | -0.05 | 54194.19 | 55.22 | skipped_fast |
| LAUSDT | IDLE | 1.58 | 2.87 | 1.91 | 0.0 | 59065.74 | 20.97 | skipped_fast |
| FLUIDUSDT | IDLE | 1.32 | 3.43 | 2.07 | 0.03 | 5240.03 | 20.97 | skipped_fast |
| WAXLUSDT | IDLE | 1.09 | 3.81 | 3.0 | 0.06 | 78270.22 | 47.61 | skipped_fast |
| IOTAUSDT | IDLE | 1.12 | 2.16 | 0.51 | 0.01 | 75996.07 | 42.5 | skipped_fast |
| RWAUSDT | IDLE | 0.68 | 1.27 | 0.55 | 0.02 | 54884.76 | 23.71 | skipped_fast |
| MNSRYUSDT | IDLE | 0.29 | 0.53 | 0.27 | -0.0 | 40493.51 | 37.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
