# Hulk DIGEST — 2026-08-22T17:19:53Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 1.74 | 8.48 | 1.04 | 0.1 | 49158533.75 | 3.82 | skipped_fast |
| XRPUSDT | IDLE | 1.32 | 7.64 | 3.47 | 0.06 | 214069325.01 | 1.35 | skipped_fast |
| CCUSDT | IDLE | 0.94 | 4.25 | 0.36 | 0.11 | 767340.56 | 5.85 | skipped_fast |
| HBARUSDT | IDLE | 0.8 | 3.03 | 0.98 | 0.0 | 1097813.81 | 5.16 | skipped_fast |
| CHIPUSDT | IDLE | 0.56 | 3.36 | 0.63 | -0.09 | 630037.88 | 6.69 | skipped_fast |
| WUSDT | IDLE | 0.59 | 2.58 | 0.13 | 0.0 | 534027.97 | 12.62 | skipped_fast |
| BIOUSDT | IDLE | 1.13 | 7.41 | 6.9 | -0.08 | 227062.43 | 16.92 | skipped_fast |
| ZBCNUSDT | IDLE | 1.26 | 3.45 | 1.17 | -0.01 | 306232.63 | 18.87 | skipped_fast |
| EDELUSDT | IDLE | 1.76 | 3.11 | 2.68 | -0.02 | 74882.83 | 22.99 | skipped_fast |
| KITEUSDT | IDLE | 1.4 | 3.22 | 1.05 | 0.04 | 87994.8 | 12.42 | skipped_fast |
| REDUSDT | IDLE | 0.54 | 5.67 | 3.11 | -0.13 | 121691.69 | 19.88 | skipped_fast |
| RIZEUSDT | IDLE | 1.13 | 2.63 | 1.02 | 0.04 | 46112.55 | 45.71 | skipped_fast |
| QAITUSDT | IDLE | 1.39 | 2.71 | 0.47 | -0.01 | 2322.14 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 1.91 | -0.01 | 181163.7 | 1.57 | skipped_fast |
| TELUSDT | IDLE | 0.98 | 2.37 | 1.79 | -0.01 | 136272.91 | 42.78 | skipped_fast |
| RWAINCUSDT | IDLE | 0.8 | 1.53 | 0.43 | 0.01 | 7571.75 | 113.06 | skipped_fast |
| RWAUSDT | IDLE | 0.57 | 1.14 | 0.0 | 0.02 | 56258.79 | 16.16 | skipped_fast |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 21.56 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
