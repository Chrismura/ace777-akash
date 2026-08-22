# Hulk DIGEST — 2026-08-22T17:07:12Z

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
| PYTHUSDT | IDLE | 1.71 | 8.45 | 0.15 | 0.1 | 49189714.97 | 13.26 | skipped_fast |
| XRPUSDT | IDLE | 1.32 | 7.64 | 3.46 | 0.05 | 214340430.03 | 0.68 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 3.03 | 1.04 | -0.01 | 1123690.96 | 1.29 | skipped_fast |
| CCUSDT | IDLE | 0.93 | 4.25 | 0.22 | 0.1 | 769933.53 | 6.68 | skipped_fast |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 0.9 | -0.09 | 631167.42 | 6.7 | skipped_fast |
| WUSDT | IDLE | 0.61 | 2.58 | 0.61 | -0.01 | 535951.86 | 12.67 | skipped_fast |
| ZBCNUSDT | IDLE | 1.27 | 3.45 | 1.39 | -0.02 | 312660.19 | 15.85 | skipped_fast |
| BIOUSDT | IDLE | 1.03 | 6.91 | 5.64 | -0.08 | 226318.86 | 3.34 | skipped_fast |
| EDELUSDT | IDLE | 1.66 | 3.0 | 2.13 | -0.01 | 74876.78 | 22.83 | skipped_fast |
| KITEUSDT | IDLE | 1.37 | 3.22 | 0.66 | 0.03 | 87594.59 | 11.49 | skipped_fast |
| REDUSDT | IDLE | 0.55 | 5.67 | 3.79 | -0.15 | 123136.03 | 11.83 | skipped_fast |
| RIZEUSDT | IDLE | 1.09 | 2.63 | 0.34 | 0.05 | 46185.22 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.39 | 2.71 | 0.47 | -0.01 | 2322.14 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 1.99 | -0.01 | 181196.21 | 4.72 | skipped_fast |
| RWAINCUSDT | IDLE | 0.8 | 1.53 | 0.43 | 0.01 | 7571.75 | 91.62 | skipped_fast |
| TELUSDT | IDLE | 1.0 | 2.37 | 2.1 | -0.0 | 136266.64 | 48.27 | skipped_fast |
| RWAUSDT | IDLE | 0.59 | 1.14 | 0.24 | 0.02 | 56302.76 | 8.09 | skipped_fast |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 23.09 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
