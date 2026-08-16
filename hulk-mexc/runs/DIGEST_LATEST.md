# Hulk DIGEST — 2026-08-16T22:09:20Z

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
| XRPUSDT | IDLE | 0.68 | 1.26 | 0.7 | -0.01 | 6397420.32 | 1.0 | skipped_fast |
| RIZEUSDT | IDLE | 3.68 | 7.8 | 2.28 | 0.02 | 38022.74 | 59.77 | skipped_fast |
| PYTHUSDT | IDLE | 2.11 | 3.77 | 3.05 | -0.03 | 146536.09 | 5.2 | skipped_fast |
| CHIPUSDT | IDLE | 1.04 | 4.9 | 2.3 | 0.05 | 294564.06 | 6.92 | skipped_fast |
| WUSDT | IDLE | 1.74 | 3.24 | 1.57 | 0.01 | 182024.6 | 15.21 | skipped_fast |
| ZBCNUSDT | IDLE | 1.56 | 2.83 | 1.95 | -0.02 | 193687.01 | 28.09 | skipped_fast |
| BIOUSDT | IDLE | 1.8 | 3.21 | 2.63 | -0.03 | 67309.52 | 4.15 | skipped_fast |
| CCUSDT | IDLE | 0.63 | 1.17 | 1.13 | -0.04 | 332390.79 | 8.43 | skipped_fast |
| EDELUSDT | IDLE | 1.37 | 2.67 | 0.52 | 0.03 | 60502.9 | 65.57 | skipped_fast |
| KITEUSDT | IDLE | 0.82 | 1.43 | 1.35 | -0.03 | 56453.55 | 17.12 | skipped_fast |
| REDUSDT | IDLE | 0.66 | 1.37 | 0.73 | -0.15 | 67727.69 | 14.95 | skipped_fast |
| QAITUSDT | IDLE | 1.25 | 3.83 | 0.0 | -0.01 | 2289.9 | 61.3 | skipped_fast |
| RWAINCUSDT | IDLE | 1.21 | 3.01 | 0.0 | 0.09 | 9973.17 | 73.38 | skipped_fast |
| TELUSDT | IDLE | 1.14 | 2.09 | 1.3 | -0.02 | 95307.01 | 27.82 | skipped_fast |
| HBARUSDT | IDLE | 0.66 | 1.24 | 0.49 | -0.01 | 104460.85 | 1.54 | skipped_fast |
| QNTUSDT | IDLE | 0.93 | 1.63 | 1.47 | -0.02 | 33723.06 | 1.77 | skipped_fast |
| RWAUSDT | IDLE | 0.33 | 0.61 | 0.35 | 0.0 | 51049.41 | 17.45 | skipped_fast |
| FLUIDUSDT | IDLE | 0.32 | 0.62 | 0.11 | 0.02 | 219.43 | 21.96 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
