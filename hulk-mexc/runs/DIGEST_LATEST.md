# Hulk DIGEST — 2026-10-18T13:02:16Z

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
| XRPUSDT | IDLE | 0.65 | 1.2 | 0.63 | -0.0 | 19450009.08 | 2.32 | skipped_fast |
| ETHUSDT | IDLE | 0.5 | 0.92 | 0.53 | -0.0 | 89164457.84 | 0.62 | skipped_fast |
| BTCUSDT | IDLE | 0.41 | 0.77 | 0.39 | 0.01 | 194766252.55 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.24 | 3.23 | 1.83 | -0.07 | 1397631.45 | 2.55 | skipped_fast |
| WUSDT | IDLE | 1.76 | 3.28 | 2.61 | -0.08 | 1055548.11 | 16.6 | skipped_fast |
| WAXLUSDT | WATCH_PULLBACK — tension haute + reflux | 3.98 | 14.22 | 10.71 | -0.01 | 71535.25 | 36.95 | skipped_fast |
| HBARUSDT | IDLE | 1.78 | 3.84 | 1.95 | 0.06 | 545489.92 | 6.81 | skipped_fast |
| QNTUSDT | IDLE | 1.75 | 3.24 | 1.75 | -0.03 | 502722.38 | 2.55 | skipped_fast |
| RWAINCUSDT | IDLE | 2.52 | 5.63 | 0.0 | 0.06 | 16161.3 | 9.98 | skipped_fast |
| EDELUSDT | IDLE | 1.24 | 3.33 | 1.11 | -0.08 | 230983.85 | 3.74 | skipped_fast |
| REDUSDT | IDLE | 1.51 | 2.75 | 1.84 | -0.01 | 76955.78 | 10.88 | skipped_fast |
| CHIPUSDT | IDLE | 1.51 | 2.74 | 1.8 | -0.07 | 68567.55 | 9.52 | skipped_fast |
| CCUSDT | IDLE | 0.63 | 1.13 | 0.91 | -0.03 | 259080.49 | 2.98 | skipped_fast |
| RIZEUSDT | IDLE | 1.92 | 3.83 | 0.0 | 0.03 | 46470.89 | 59.53 | skipped_fast |
| KITEUSDT | IDLE | 1.12 | 2.1 | 0.91 | -0.04 | 67989.61 | 11.33 | skipped_fast |
| BIOUSDT | IDLE | 0.92 | 1.65 | 1.21 | -0.03 | 81252.5 | 4.21 | skipped_fast |
| ZBCNUSDT | IDLE | 0.64 | 1.2 | 0.49 | -0.02 | 159685.92 | 14.75 | skipped_fast |
| IOTAUSDT | IDLE | 1.19 | 2.11 | 1.79 | -0.04 | 68398.74 | 31.08 | skipped_fast |
| LAUSDT | IDLE | 0.95 | 1.66 | 1.54 | -0.05 | 54416.22 | 22.41 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.71 | 1.68 | -0.04 | 2785.76 | 21.35 | skipped_fast |
| MNSRYUSDT | IDLE | 0.35 | 0.69 | 0.1 | -0.0 | 34045.24 | 12.78 | skipped_fast |
| RWAUSDT | IDLE | 0.13 | 0.24 | 0.16 | 0.0 | 50003.17 | 15.94 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
