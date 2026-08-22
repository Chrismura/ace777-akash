# Hulk DIGEST — 2026-08-22T17:24:03Z

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
| PYTHUSDT | IDLE | 1.76 | 8.48 | 1.46 | 0.1 | 49143821.98 | 1.92 | skipped_fast |
| XRPUSDT | IDLE | 1.32 | 7.64 | 3.4 | 0.06 | 213867432.38 | 1.35 | skipped_fast |
| HBARUSDT | IDLE | 0.8 | 3.03 | 0.97 | 0.01 | 1096565.91 | 5.16 | skipped_fast |
| CCUSDT | IDLE | 0.93 | 4.25 | 0.13 | 0.12 | 767316.33 | 10.0 | skipped_fast |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 0.73 | -0.09 | 631329.69 | 3.35 | skipped_fast |
| WUSDT | IDLE | 0.59 | 2.58 | 0.01 | 0.0 | 533541.05 | 10.5 | skipped_fast |
| BIOUSDT | IDLE | 1.19 | 7.96 | 6.3 | -0.07 | 228161.59 | 3.36 | skipped_fast |
| ZBCNUSDT | IDLE | 1.28 | 3.45 | 1.5 | -0.02 | 306437.21 | 22.03 | skipped_fast |
| EDELUSDT | IDLE | 1.76 | 3.11 | 2.68 | -0.02 | 74907.8 | 22.99 | skipped_fast |
| KITEUSDT | IDLE | 1.39 | 3.22 | 0.89 | 0.05 | 89102.65 | 7.08 | skipped_fast |
| REDUSDT | IDLE | 0.53 | 5.67 | 2.3 | -0.14 | 121729.6 | 14.33 | skipped_fast |
| RIZEUSDT | IDLE | 1.12 | 2.63 | 0.86 | 0.04 | 46136.04 | 45.71 | skipped_fast |
| QAITUSDT | IDLE | 1.39 | 2.71 | 0.47 | -0.01 | 2322.14 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 1.96 | -0.01 | 181242.43 | 4.72 | skipped_fast |
| TELUSDT | IDLE | 0.98 | 2.37 | 1.79 | 0.01 | 134448.76 | 37.46 | skipped_fast |
| RWAINCUSDT | IDLE | 0.8 | 1.53 | 0.43 | 0.01 | 7571.75 | 107.7 | skipped_fast |
| RWAUSDT | IDLE | 0.57 | 1.14 | 0.0 | 0.02 | 56247.78 | 8.07 | skipped_fast |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 22.34 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
