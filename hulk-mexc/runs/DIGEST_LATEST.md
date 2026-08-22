# Hulk DIGEST — 2026-08-22T17:21:34Z

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
| PYTHUSDT | IDLE | 1.77 | 8.48 | 1.82 | 0.1 | 49147398.24 | 11.57 | skipped_fast |
| XRPUSDT | IDLE | 1.33 | 7.64 | 3.61 | 0.06 | 214168441.16 | 1.36 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 3.03 | 1.0 | 0.0 | 1097778.49 | 3.87 | skipped_fast |
| CCUSDT | IDLE | 0.94 | 4.25 | 0.34 | 0.12 | 766972.26 | 9.19 | skipped_fast |
| CHIPUSDT | IDLE | 0.56 | 3.36 | 0.56 | -0.09 | 631809.36 | 3.34 | skipped_fast |
| WUSDT | IDLE | 0.59 | 2.58 | 0.15 | 0.0 | 533955.95 | 11.56 | skipped_fast |
| BIOUSDT | IDLE | 1.21 | 7.96 | 7.37 | -0.09 | 227333.91 | 27.07 | skipped_fast |
| ZBCNUSDT | IDLE | 1.27 | 3.45 | 1.32 | -0.01 | 306380.71 | 14.82 | skipped_fast |
| EDELUSDT | IDLE | 1.76 | 3.11 | 2.68 | -0.02 | 74907.82 | 22.99 | skipped_fast |
| KITEUSDT | IDLE | 1.38 | 3.22 | 0.86 | 0.05 | 89683.82 | 7.08 | skipped_fast |
| REDUSDT | IDLE | 0.54 | 5.67 | 2.63 | -0.13 | 121791.33 | 21.51 | skipped_fast |
| RIZEUSDT | IDLE | 1.12 | 2.63 | 0.82 | 0.04 | 46114.16 | 45.71 | skipped_fast |
| QAITUSDT | IDLE | 1.39 | 2.71 | 0.47 | -0.01 | 2322.14 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 1.93 | -0.01 | 181192.27 | 7.87 | skipped_fast |
| TELUSDT | IDLE | 0.98 | 2.37 | 1.84 | -0.01 | 136251.44 | 26.76 | skipped_fast |
| RWAINCUSDT | IDLE | 0.8 | 1.53 | 0.43 | 0.01 | 7571.75 | 113.06 | skipped_fast |
| RWAUSDT | IDLE | 0.57 | 1.14 | 0.0 | 0.02 | 56293.67 | 16.16 | skipped_fast |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 20.09 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
