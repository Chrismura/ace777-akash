# Hulk DIGEST — 2026-09-08T00:37:45Z

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
| XRPUSDT | IDLE | 0.75 | 1.45 | 0.38 | -0.02 | 36379766.36 | 0.72 | skipped_fast |
| ETHUSDT | IDLE | 0.45 | 0.87 | 0.22 | -0.01 | 322014425.38 | 0.28 | skipped_fast |
| BTCUSDT | IDLE | 0.42 | 0.79 | 0.3 | -0.01 | 425449428.77 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.34 | 2.5 | 1.24 | -0.05 | 473663.75 | 1.84 | skipped_fast |
| CCUSDT | IDLE | 1.5 | 2.86 | 0.94 | -0.05 | 442722.76 | 8.52 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.51 | 9.19 | 6.12 | -0.06 | 112319.03 | 50.33 | skipped_fast |
| CHIPUSDT | IDLE | 1.37 | 5.17 | 2.97 | -0.1 | 217473.59 | 11.21 | skipped_fast |
| KITEUSDT | IDLE | 1.84 | 3.84 | 0.06 | -0.03 | 62668.4 | 10.64 | skipped_fast |
| WUSDT | IDLE | 1.13 | 2.23 | 0.23 | -0.01 | 238198.58 | 16.41 | skipped_fast |
| HBARUSDT | IDLE | 0.98 | 1.83 | 0.9 | 0.0 | 527480.52 | 1.22 | skipped_fast |
| ZBCNUSDT | IDLE | 0.93 | 2.52 | 1.21 | -0.04 | 225236.6 | 15.63 | skipped_fast |
| RWAINCUSDT | IDLE | 2.09 | 5.87 | 4.39 | -0.11 | 4440.19 | 77.94 | skipped_fast |
| RIZEUSDT | IDLE | 1.83 | 5.58 | 1.74 | -0.04 | 53810.46 | 66.11 | skipped_fast |
| REDUSDT | IDLE | 1.24 | 2.37 | 0.74 | 0.04 | 57583.41 | 9.84 | skipped_fast |
| BIOUSDT | IDLE | 1.04 | 1.97 | 0.69 | -0.02 | 66319.18 | 7.33 | skipped_fast |
| QNTUSDT | IDLE | 1.13 | 2.18 | 0.57 | -0.0 | 60932.16 | 4.5 | skipped_fast |
| TELUSDT | IDLE | 0.7 | 1.3 | 0.7 | -0.02 | 79961.58 | 47.06 | skipped_fast |
| MNSRYUSDT | IDLE | 0.41 | 0.74 | 0.53 | -0.02 | 37511.56 | 5.46 | skipped_fast |
| FLUIDUSDT | IDLE | 0.7 | 1.41 | 0.0 | 0.0 | 1666.63 | 21.59 | skipped_fast |
| RWAUSDT | IDLE | 0.38 | 0.73 | 0.14 | -0.01 | 53090.9 | 14.51 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
