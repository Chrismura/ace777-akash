# Hulk DIGEST — 2026-10-26T13:46:48Z

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
| XRPUSDT | IDLE | 1.12 | 2.08 | 1.1 | -0.01 | 20810017.51 | 2.33 | skipped_fast |
| QNTUSDT | IDLE | 2.98 | 15.77 | 3.88 | 0.17 | 1402843.32 | 9.76 | skipped_fast |
| ETHUSDT | IDLE | 0.92 | 1.67 | 1.14 | -0.01 | 116152529.66 | 0.95 | skipped_fast |
| BTCUSDT | IDLE | 0.74 | 1.36 | 0.84 | -0.01 | 269703004.74 | 0.02 | skipped_fast |
| PYTHUSDT | IDLE | 2.71 | 5.13 | 1.91 | 0.05 | 893483.8 | 6.68 | skipped_fast |
| CHIPUSDT | IDLE | 2.74 | 11.18 | 2.69 | 0.09 | 139395.82 | 18.58 | skipped_fast |
| WUSDT | IDLE | 1.63 | 3.18 | 0.49 | 0.01 | 482061.51 | 15.94 | skipped_fast |
| ZBCNUSDT | IDLE | 2.15 | 5.03 | 3.25 | -0.01 | 221216.61 | 25.85 | skipped_fast |
| REDUSDT | IDLE | 2.46 | 4.57 | 2.29 | 0.02 | 61990.22 | 16.51 | skipped_fast |
| CCUSDT | IDLE | 1.17 | 2.13 | 1.45 | -0.0 | 184382.87 | 0.99 | skipped_fast |
| BIOUSDT | IDLE | 1.3 | 2.42 | 1.21 | -0.01 | 59995.61 | 9.04 | skipped_fast |
| EDELUSDT | IDLE | 1.03 | 2.4 | 1.76 | 0.08 | 130925.01 | 31.29 | skipped_fast |
| KITEUSDT | IDLE | 1.33 | 2.56 | 0.67 | 0.02 | 53613.02 | 21.2 | skipped_fast |
| RWAINCUSDT | IDLE | 1.13 | 2.24 | 0.17 | -0.05 | 67371.86 | 11.55 | skipped_fast |
| LAUSDT | IDLE | 1.97 | 3.88 | 2.76 | 0.02 | 64092.12 | 22.51 | skipped_fast |
| MNSRYUSDT | IDLE | 2.42 | 4.38 | 3.04 | -0.01 | 42601.25 | 72.06 | skipped_fast |
| RIZEUSDT | IDLE | 1.12 | 2.16 | 0.57 | 0.01 | 33361.58 | 61.76 | skipped_fast |
| HBARUSDT | IDLE | 1.18 | 2.21 | 1.06 | 0.0 | 193109.67 | 5.18 | skipped_fast |
| IOTAUSDT | IDLE | 1.32 | 2.51 | 0.91 | -0.01 | 65222.63 | 25.91 | skipped_fast |
| WAXLUSDT | IDLE | 1.56 | 2.99 | 0.87 | -0.03 | 52840.53 | 48.09 | skipped_fast |
| RWAUSDT | IDLE | 0.53 | 0.96 | 0.72 | -0.0 | 53979.24 | 39.98 | skipped_fast |
| FLUIDUSDT | IDLE | 0.35 | 1.39 | 0.56 | -0.01 | 7194.79 | 21.25 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
