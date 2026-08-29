# Hulk DIGEST — 2026-08-29T10:10:44Z

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
| CHIPUSDT | IDLE | 2.22 | 10.04 | 9.13 | -0.01 | 1300379.88 | 7.43 | skipped_fast |
| XRPUSDT | IDLE | 0.65 | 1.17 | 0.82 | -0.02 | 41266180.68 | 2.17 | skipped_fast |
| PYTHUSDT | IDLE | 1.29 | 2.32 | 1.78 | -0.03 | 464817.88 | 4.27 | skipped_fast |
| CCUSDT | IDLE | 1.77 | 3.33 | 1.39 | 0.0 | 210367.95 | 8.91 | skipped_fast |
| WUSDT | IDLE | 1.41 | 2.5 | 2.1 | -0.03 | 208031.85 | 13.18 | skipped_fast |
| REDUSDT | IDLE | 1.54 | 4.04 | 0.45 | 0.06 | 65897.44 | 11.57 | skipped_fast |
| ZBCNUSDT | IDLE | 0.72 | 1.92 | 0.78 | -0.05 | 197661.46 | 10.17 | skipped_fast |
| BIOUSDT | IDLE | 1.0 | 1.75 | 1.65 | -0.03 | 85039.81 | 3.64 | skipped_fast |
| RIZEUSDT | IDLE | 1.6 | 3.21 | 2.0 | -0.03 | 29282.34 | 56.52 | skipped_fast |
| HBARUSDT | IDLE | 0.77 | 1.34 | 1.3 | -0.03 | 384167.01 | 1.34 | skipped_fast |
| KITEUSDT | IDLE | 0.97 | 1.93 | 0.05 | 0.02 | 64215.19 | 10.92 | skipped_fast |
| EDELUSDT | IDLE | 1.09 | 4.11 | 2.91 | -0.12 | 91149.52 | 77.67 | skipped_fast |
| RWAINCUSDT | IDLE | 1.31 | 2.28 | 2.23 | 0.0 | 3704.35 | 99.45 | skipped_fast |
| QAITUSDT | IDLE | 0.34 | 2.98 | 1.83 | -0.02 | 84169.61 | 62.24 | skipped_fast |
| TELUSDT | IDLE | 0.95 | 1.68 | 1.42 | -0.05 | 81004.74 | 51.95 | skipped_fast |
| QNTUSDT | IDLE | 0.71 | 1.28 | 0.97 | -0.02 | 40983.46 | 6.55 | skipped_fast |
| RWAUSDT | IDLE | 0.5 | 0.91 | 0.57 | 0.01 | 56156.91 | 16.46 | skipped_fast |
| FLUIDUSDT | IDLE | 0.38 | 0.66 | 0.65 | -0.06 | 3665.9 | 20.94 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
