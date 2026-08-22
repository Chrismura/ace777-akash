# Hulk DIGEST — 2026-08-22T17:20:56Z

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
| PYTHUSDT | IDLE | 1.76 | 8.48 | 1.49 | 0.1 | 49155198.28 | 1.92 | skipped_fast |
| XRPUSDT | IDLE | 1.32 | 7.64 | 3.35 | 0.06 | 214140704.7 | 0.68 | skipped_fast |
| CCUSDT | IDLE | 0.93 | 4.25 | 0.27 | 0.12 | 767869.86 | 7.52 | skipped_fast |
| HBARUSDT | IDLE | 0.8 | 3.03 | 0.89 | 0.0 | 1097775.61 | 5.16 | skipped_fast |
| CHIPUSDT | IDLE | 0.56 | 3.36 | 0.6 | -0.09 | 629986.21 | 6.69 | skipped_fast |
| WUSDT | IDLE | 0.59 | 2.58 | 0.09 | 0.0 | 533996.41 | 11.56 | skipped_fast |
| BIOUSDT | IDLE | 1.13 | 7.49 | 6.81 | -0.08 | 227319.79 | 13.53 | skipped_fast |
| ZBCNUSDT | IDLE | 1.27 | 3.45 | 1.31 | -0.01 | 306314.38 | 15.33 | skipped_fast |
| EDELUSDT | IDLE | 1.76 | 3.11 | 2.68 | -0.02 | 74882.79 | 22.99 | skipped_fast |
| KITEUSDT | IDLE | 1.39 | 3.22 | 0.93 | 0.04 | 89705.04 | 7.97 | skipped_fast |
| REDUSDT | IDLE | 0.54 | 5.67 | 2.85 | -0.13 | 121791.9 | 21.58 | skipped_fast |
| RIZEUSDT | IDLE | 1.12 | 2.63 | 0.86 | 0.04 | 46123.65 | 45.71 | skipped_fast |
| QAITUSDT | IDLE | 1.39 | 2.71 | 0.47 | -0.01 | 2322.14 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 1.93 | -0.01 | 181175.12 | 4.72 | skipped_fast |
| TELUSDT | IDLE | 0.99 | 2.37 | 1.94 | -0.01 | 136257.72 | 37.44 | skipped_fast |
| RWAINCUSDT | IDLE | 0.8 | 1.53 | 0.43 | 0.01 | 7571.75 | 107.7 | skipped_fast |
| RWAUSDT | IDLE | 0.57 | 1.14 | 0.0 | 0.02 | 56322.65 | 16.16 | skipped_fast |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 20.86 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
