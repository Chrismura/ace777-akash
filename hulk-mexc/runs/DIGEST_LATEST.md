# Hulk DIGEST — 2026-10-27T13:11:07Z

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
| XRPUSDT | IDLE | 1.25 | 2.38 | 0.79 | 0.01 | 21830738.61 | 2.29 | skipped_fast |
| ETHUSDT | IDLE | 0.98 | 1.88 | 0.57 | 0.0 | 156368299.11 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.64 | 1.21 | 0.4 | 0.0 | 346951397.1 | 0.01 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 2.54 | 6.17 | 5.51 | -0.08 | 974928.78 | 4.02 | skipped_fast |
| WUSDT | IDLE | 2.39 | 5.45 | 1.28 | 0.07 | 583447.49 | 31.2 | skipped_fast |
| CHIPUSDT | IDLE | 1.81 | 8.15 | 1.89 | 0.07 | 323966.73 | 20.76 | skipped_fast |
| PYTHUSDT | IDLE | 1.16 | 2.14 | 1.24 | -0.03 | 515378.32 | 5.5 | skipped_fast |
| EDELUSDT | IDLE | 1.27 | 2.41 | 0.83 | 0.01 | 377810.04 | 15.4 | skipped_fast |
| RWAINCUSDT | IDLE | 1.99 | 7.86 | 6.47 | -0.14 | 53352.42 | 6.7 | skipped_fast |
| CCUSDT | IDLE | 1.69 | 3.28 | 0.68 | -0.02 | 232948.74 | 6.1 | skipped_fast |
| REDUSDT | IDLE | 2.46 | 4.88 | 0.24 | 0.02 | 60599.82 | 15.92 | skipped_fast |
| KITEUSDT | IDLE | 2.26 | 4.48 | 0.26 | 0.04 | 54508.84 | 11.97 | skipped_fast |
| ZBCNUSDT | IDLE | 1.18 | 3.29 | 1.85 | 0.02 | 250261.62 | 38.33 | skipped_fast |
| BIOUSDT | IDLE | 1.4 | 2.62 | 1.25 | -0.01 | 56900.12 | 4.54 | skipped_fast |
| HBARUSDT | IDLE | 0.92 | 1.71 | 0.87 | -0.02 | 214209.44 | 10.51 | skipped_fast |
| WAXLUSDT | IDLE | 2.06 | 4.04 | 0.54 | 0.03 | 54100.03 | 62.57 | skipped_fast |
| RIZEUSDT | IDLE | 0.59 | 1.1 | 0.49 | -0.02 | 42290.26 | 42.06 | skipped_fast |
| LAUSDT | IDLE | 1.6 | 3.07 | 0.86 | -0.0 | 61185.23 | 39.66 | skipped_fast |
| IOTAUSDT | IDLE | 1.04 | 2.0 | 0.59 | -0.01 | 95125.17 | 19.03 | skipped_fast |
| FLUIDUSDT | IDLE | 1.18 | 2.16 | 1.37 | 0.03 | 3297.6 | 21.5 | skipped_fast |
| RWAUSDT | IDLE | 1.2 | 2.29 | 0.72 | -0.01 | 57600.86 | 48.35 | skipped_fast |
| MNSRYUSDT | IDLE | 0.44 | 0.77 | 0.72 | -0.0 | 37355.06 | 79.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
