# Hulk DIGEST — 2026-08-22T16:36:13Z

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
| PYTHUSDT | IDLE | 1.73 | 8.54 | 0.06 | 0.08 | 51433348.23 | 3.85 | skipped_fast |
| XRPUSDT | IDLE | 1.34 | 7.64 | 4.08 | 0.05 | 215107350.2 | 2.73 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 3.03 | 1.1 | -0.01 | 1126412.04 | 5.17 | skipped_fast |
| CCUSDT | IDLE | 0.98 | 4.14 | 2.52 | 0.07 | 762165.1 | 9.4 | skipped_fast |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 0.86 | -0.11 | 627313.96 | 3.35 | skipped_fast |
| WUSDT | IDLE | 0.62 | 2.58 | 0.8 | -0.01 | 543447.01 | 10.59 | skipped_fast |
| ZBCNUSDT | IDLE | 1.28 | 3.49 | 1.29 | -0.03 | 315856.99 | 23.51 | skipped_fast |
| BIOUSDT | IDLE | 0.96 | 6.58 | 4.13 | -0.06 | 219793.15 | 3.29 | skipped_fast |
| KITEUSDT | IDLE | 1.94 | 4.35 | 2.26 | 0.02 | 85131.7 | 13.46 | skipped_fast |
| EDELUSDT | IDLE | 1.41 | 2.52 | 2.01 | -0.03 | 74876.15 | 34.23 | skipped_fast |
| REDUSDT | IDLE | 0.52 | 5.67 | 4.18 | -0.15 | 130699.02 | 21.94 | skipped_fast |
| RIZEUSDT | IDLE | 1.33 | 3.23 | 0.29 | 0.06 | 49214.52 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | -0.01 | 2317.66 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.87 | 2.69 | 2.3 | -0.02 | 183022.01 | 4.74 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.02 | 8093.79 | 69.84 | skipped_fast |
| TELUSDT | IDLE | 1.0 | 2.37 | 2.1 | -0.0 | 137264.09 | 64.34 | skipped_fast |
| RWAUSDT | IDLE | 0.55 | 1.06 | 0.24 | 0.02 | 56564.4 | 16.22 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.03 | 4618.58 | 22.37 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
