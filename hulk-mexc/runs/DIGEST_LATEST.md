# Hulk DIGEST — 2026-08-22T17:18:40Z

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
| PYTHUSDT | IDLE | 1.74 | 8.48 | 0.95 | 0.11 | 49163757.03 | 3.82 | skipped_fast |
| XRPUSDT | IDLE | 1.33 | 7.64 | 3.56 | 0.06 | 214094515.89 | 2.03 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 3.03 | 1.06 | 0.0 | 1097835.1 | 3.87 | skipped_fast |
| CCUSDT | IDLE | 0.94 | 4.25 | 0.54 | 0.11 | 767512.03 | 10.04 | skipped_fast |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 0.96 | -0.1 | 631025.53 | 3.35 | skipped_fast |
| WUSDT | IDLE | 0.59 | 2.58 | 0.21 | -0.0 | 534017.84 | 12.63 | skipped_fast |
| BIOUSDT | IDLE | 1.03 | 6.91 | 5.29 | -0.07 | 226360.76 | 3.33 | skipped_fast |
| ZBCNUSDT | IDLE | 1.26 | 3.45 | 1.1 | -0.01 | 306202.77 | 22.45 | skipped_fast |
| EDELUSDT | IDLE | 1.75 | 3.11 | 2.57 | -0.02 | 74859.05 | 22.96 | skipped_fast |
| KITEUSDT | IDLE | 1.38 | 3.22 | 0.87 | 0.04 | 87934.88 | 11.51 | skipped_fast |
| REDUSDT | IDLE | 0.54 | 5.67 | 3.11 | -0.13 | 121749.68 | 13.56 | skipped_fast |
| RIZEUSDT | IDLE | 1.13 | 2.63 | 1.02 | 0.04 | 46101.26 | 35.54 | skipped_fast |
| QAITUSDT | IDLE | 1.39 | 2.71 | 0.47 | -0.01 | 2322.14 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.85 | 2.69 | 1.87 | -0.01 | 181145.29 | 3.14 | skipped_fast |
| TELUSDT | IDLE | 0.99 | 2.37 | 2.0 | -0.01 | 136278.1 | 42.85 | skipped_fast |
| RWAINCUSDT | IDLE | 0.8 | 1.53 | 0.43 | 0.01 | 7571.75 | 113.06 | skipped_fast |
| RWAUSDT | IDLE | 0.58 | 1.14 | 0.08 | 0.02 | 56242.14 | 8.08 | skipped_fast |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 23.8 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
