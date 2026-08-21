# Hulk DIGEST — 2026-08-21T21:34:33Z

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
| PYTHUSDT | IDLE | 1.17 | 4.51 | 0.47 | 0.1 | 5641831.68 | 2.06 | skipped_fast |
| XRPUSDT | IDLE | 1.1 | 3.73 | 0.88 | 0.11 | 129306130.19 | 0.71 | skipped_fast |
| CHIPUSDT | IDLE | 1.88 | 5.61 | 3.7 | 0.05 | 517509.59 | 6.19 | skipped_fast |
| ZBCNUSDT | IDLE | 1.97 | 8.19 | 4.23 | 0.09 | 487950.79 | 41.43 | skipped_fast |
| CCUSDT | IDLE | 1.18 | 3.36 | 0.03 | 0.1 | 645288.06 | 8.24 | skipped_fast |
| HBARUSDT | IDLE | 1.53 | 3.04 | 0.09 | 0.07 | 816963.12 | 1.28 | skipped_fast |
| WUSDT | IDLE | 1.93 | 3.83 | 0.19 | 0.07 | 367960.52 | 12.51 | skipped_fast |
| BIOUSDT | IDLE | 2.42 | 5.2 | 1.97 | 0.02 | 187997.15 | 3.14 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 11.01 | 8.84 | 0.18 | 154212.68 | 11.41 | skipped_fast |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.85 | 0.02 | 10130.99 | 10.82 | skipped_fast |
| EDELUSDT | IDLE | 2.0 | 4.12 | 1.98 | -0.05 | 83558.59 | 22.42 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 9.54 | 1.27 | 0.02 | 56020.72 | 45.77 | skipped_fast |
| KITEUSDT | IDLE | 1.28 | 4.0 | 1.34 | 0.11 | 61058.46 | 12.89 | skipped_fast |
| QAITUSDT | IDLE | 2.33 | 4.38 | 1.83 | -0.01 | 3809.29 | 103.88 | skipped_fast |
| TELUSDT | IDLE | 1.91 | 4.81 | 1.1 | 0.03 | 182978.21 | 52.8 | skipped_fast |
| QNTUSDT | IDLE | 1.38 | 2.65 | 0.74 | 0.04 | 62895.36 | 10.82 | skipped_fast |
| RWAUSDT | IDLE | 0.59 | 1.17 | 0.08 | 0.04 | 53954.78 | 33.09 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 21.9 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
