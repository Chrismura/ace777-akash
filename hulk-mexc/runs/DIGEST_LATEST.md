# Hulk DIGEST — 2026-08-22T16:05:38Z

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
| PYTHUSDT | IDLE | 1.51 | 7.24 | 1.58 | 0.04 | 51465372.29 | 1.98 | skipped_fast |
| XRPUSDT | IDLE | 1.37 | 7.64 | 5.29 | 0.04 | 215679864.29 | 3.45 | skipped_fast |
| HBARUSDT | IDLE | 0.85 | 3.03 | 2.24 | -0.02 | 1149608.75 | 1.31 | skipped_fast |
| CCUSDT | IDLE | 0.96 | 4.14 | 1.83 | 0.1 | 763987.12 | 5.95 | skipped_fast |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 0.96 | -0.09 | 624755.87 | 10.05 | skipped_fast |
| WUSDT | IDLE | 0.65 | 2.58 | 1.93 | -0.02 | 549372.25 | 13.91 | skipped_fast |
| ZBCNUSDT | IDLE | 1.34 | 3.49 | 2.34 | -0.06 | 319313.3 | 22.12 | skipped_fast |
| BIOUSDT | IDLE | 0.97 | 6.58 | 4.57 | -0.07 | 218935.28 | 6.61 | skipped_fast |
| KITEUSDT | IDLE | 1.91 | 4.35 | 1.89 | 0.03 | 85397.67 | 13.41 | skipped_fast |
| EDELUSDT | IDLE | 1.34 | 2.41 | 1.79 | -0.03 | 75081.96 | 22.81 | skipped_fast |
| REDUSDT | IDLE | 0.52 | 5.67 | 4.31 | -0.15 | 133654.92 | 10.07 | skipped_fast |
| RIZEUSDT | IDLE | 1.31 | 3.21 | 0.15 | 0.03 | 56517.29 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 2.08 | -0.02 | 183577.5 | 6.31 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.02 | 8954.22 | 75.23 | skipped_fast |
| TELUSDT | IDLE | 0.97 | 2.37 | 1.52 | -0.0 | 138534.5 | 48.01 | skipped_fast |
| RWAUSDT | IDLE | 0.55 | 1.06 | 0.24 | 0.02 | 56380.3 | 16.23 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.04 | 4625.53 | 20.93 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
