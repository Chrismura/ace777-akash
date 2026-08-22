# Hulk DIGEST — 2026-08-22T14:57:55Z

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
| PYTHUSDT | IDLE | 1.6 | 7.62 | 2.0 | 0.04 | 51454168.85 | 3.97 | skipped_fast |
| XRPUSDT | IDLE | 1.37 | 7.58 | 5.64 | 0.03 | 213680933.26 | 2.77 | skipped_fast |
| CCUSDT | IDLE | 1.38 | 6.16 | 3.2 | 0.11 | 795935.19 | 3.43 | skipped_fast |
| HBARUSDT | IDLE | 0.96 | 3.34 | 3.13 | -0.02 | 1178421.34 | 1.31 | skipped_fast |
| WUSDT | IDLE | 1.12 | 4.43 | 3.11 | -0.02 | 563171.23 | 14.98 | skipped_fast |
| CHIPUSDT | IDLE | 0.64 | 3.51 | 2.72 | -0.11 | 614054.53 | 6.82 | skipped_fast |
| ZBCNUSDT | IDLE | 1.55 | 4.21 | 1.65 | -0.06 | 323887.32 | 10.67 | skipped_fast |
| KITEUSDT | IDLE | 2.7 | 6.37 | 1.1 | 0.04 | 84514.18 | 30.14 | skipped_fast |
| BIOUSDT | IDLE | 0.99 | 6.58 | 5.74 | -0.06 | 226262.96 | 6.68 | skipped_fast |
| EDELUSDT | IDLE | 1.43 | 2.63 | 1.56 | -0.04 | 78969.13 | 22.7 | skipped_fast |
| QAITUSDT | IDLE | 2.01 | 3.76 | 1.79 | -0.01 | 2374.33 | 67.45 | skipped_fast |
| REDUSDT | IDLE | 0.42 | 5.1 | 4.65 | -0.03 | 150291.3 | 13.75 | skipped_fast |
| RWAINCUSDT | IDLE | 1.26 | 2.4 | 0.85 | 0.01 | 9946.26 | 42.92 | skipped_fast |
| RIZEUSDT | IDLE | 0.79 | 3.28 | 0.47 | 0.03 | 46756.27 | 43.92 | skipped_fast |
| QNTUSDT | IDLE | 0.87 | 2.69 | 2.14 | -0.01 | 188421.55 | 6.3 | skipped_fast |
| TELUSDT | IDLE | 1.3 | 3.24 | 1.78 | 0.01 | 140154.99 | 47.94 | skipped_fast |
| RWAUSDT | IDLE | 0.82 | 1.55 | 0.64 | 0.02 | 57267.0 | 8.1 | skipped_fast |
| FLUIDUSDT | IDLE | 0.98 | 1.87 | 1.32 | -0.04 | 4682.03 | 21.64 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
