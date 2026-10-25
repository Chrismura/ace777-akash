# Hulk DIGEST — 2026-10-25T14:04:24Z

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
| ETHUSDT | IDLE | 0.56 | 1.06 | 0.45 | -0.02 | 133584557.31 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.53 | 0.99 | 0.49 | 0.01 | 21820815.71 | 1.54 | skipped_fast |
| BTCUSDT | IDLE | 0.36 | 0.66 | 0.35 | -0.0 | 196067641.91 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.08 | 1.92 | 1.64 | -0.05 | 811425.11 | 16.07 | skipped_fast |
| PYTHUSDT | IDLE | 2.11 | 3.99 | 1.52 | 0.03 | 486903.16 | 2.81 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.47 | 10.5 | 8.43 | -0.03 | 19137.95 | 21.48 | skipped_fast |
| EDELUSDT | IDLE | 1.56 | 2.99 | 0.84 | -0.04 | 475537.67 | 40.54 | skipped_fast |
| CHIPUSDT | IDLE | 1.97 | 5.7 | 4.0 | 0.04 | 102035.54 | 15.94 | skipped_fast |
| QNTUSDT | IDLE | 1.95 | 3.77 | 0.83 | 0.02 | 412184.32 | 1.09 | skipped_fast |
| CCUSDT | IDLE | 1.14 | 2.2 | 0.54 | -0.0 | 188588.1 | 2.98 | skipped_fast |
| ZBCNUSDT | IDLE | 0.88 | 1.9 | 1.3 | 0.02 | 233706.5 | 28.91 | skipped_fast |
| REDUSDT | IDLE | 1.09 | 1.96 | 1.43 | -0.02 | 67626.83 | 0.7 | skipped_fast |
| BIOUSDT | IDLE | 0.97 | 1.82 | 0.76 | -0.03 | 65361.62 | 9.0 | skipped_fast |
| RIZEUSDT | IDLE | 1.02 | 2.61 | 0.92 | -0.03 | 40017.02 | 18.46 | skipped_fast |
| KITEUSDT | IDLE | 0.82 | 1.5 | 0.96 | -0.04 | 58948.1 | 9.92 | skipped_fast |
| RWAINCUSDT | IDLE | 0.84 | 1.54 | 0.98 | -0.02 | 57433.33 | 16.36 | skipped_fast |
| WAXLUSDT | IDLE | 2.15 | 4.07 | 1.5 | -0.02 | 53694.13 | 39.1 | skipped_fast |
| LAUSDT | IDLE | 0.91 | 3.5 | 2.95 | -0.14 | 72444.92 | 1.78 | skipped_fast |
| HBARUSDT | IDLE | 0.57 | 1.06 | 0.52 | 0.0 | 195019.04 | 7.81 | skipped_fast |
| RWAUSDT | IDLE | 1.24 | 2.25 | 1.49 | -0.0 | 51811.89 | 47.81 | skipped_fast |
| IOTAUSDT | IDLE | 0.76 | 1.41 | 0.77 | -0.02 | 64739.54 | 28.08 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.74 | 0.09 | -0.0 | 37284.16 | 77.07 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
