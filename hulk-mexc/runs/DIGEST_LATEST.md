# Hulk DIGEST — 2026-08-22T16:38:24Z

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
| PYTHUSDT | IDLE | 1.9 | 9.35 | 0.29 | 0.09 | 51429745.22 | 17.23 | skipped_fast |
| XRPUSDT | IDLE | 1.33 | 7.64 | 3.89 | 0.05 | 215044185.88 | 2.72 | skipped_fast |
| HBARUSDT | IDLE | 0.8 | 3.03 | 0.92 | -0.0 | 1126082.03 | 5.16 | skipped_fast |
| CCUSDT | IDLE | 0.98 | 4.14 | 2.4 | 0.08 | 763125.31 | 7.69 | skipped_fast |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 0.83 | -0.11 | 627403.38 | 3.35 | skipped_fast |
| WUSDT | IDLE | 0.61 | 2.58 | 0.68 | -0.01 | 543548.62 | 12.69 | skipped_fast |
| ZBCNUSDT | IDLE | 1.29 | 3.49 | 1.51 | -0.04 | 315170.84 | 29.67 | skipped_fast |
| BIOUSDT | IDLE | 0.96 | 6.58 | 3.94 | -0.06 | 219777.63 | 6.56 | skipped_fast |
| KITEUSDT | IDLE | 1.94 | 4.35 | 2.26 | 0.02 | 85129.93 | 14.36 | skipped_fast |
| EDELUSDT | IDLE | 1.41 | 2.52 | 2.01 | -0.03 | 74876.1 | 22.81 | skipped_fast |
| REDUSDT | IDLE | 0.52 | 5.67 | 4.04 | -0.15 | 130178.17 | 21.9 | skipped_fast |
| RIZEUSDT | IDLE | 1.33 | 3.23 | 0.29 | 0.09 | 48837.87 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | -0.01 | 2317.66 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.87 | 2.69 | 2.28 | -0.01 | 182299.72 | 3.16 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.03 | 7676.54 | 69.84 | skipped_fast |
| TELUSDT | IDLE | 0.99 | 2.37 | 2.0 | -0.0 | 136952.93 | 48.24 | skipped_fast |
| RWAUSDT | IDLE | 0.54 | 1.06 | 0.08 | 0.02 | 56517.81 | 24.3 | skipped_fast |
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
