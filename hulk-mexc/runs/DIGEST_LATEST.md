# Hulk DIGEST — 2026-08-22T12:18:59Z

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
| PYTHUSDT | IDLE | 1.68 | 7.83 | 3.13 | 0.04 | 51610640.15 | 2.01 | skipped_fast |
| XRPUSDT | IDLE | 2.47 | 14.26 | 6.44 | 0.12 | 215374042.92 | 4.6 | skipped_fast |
| HBARUSDT | IDLE | 1.24 | 4.63 | 1.83 | 0.03 | 1259912.33 | 3.84 | skipped_fast |
| CCUSDT | IDLE | 1.62 | 8.38 | 4.03 | 0.13 | 774443.32 | 5.93 | skipped_fast |
| WUSDT | IDLE | 1.54 | 6.27 | 3.18 | 0.02 | 577513.06 | 14.74 | skipped_fast |
| ZBCNUSDT | IDLE | 2.22 | 5.77 | 3.92 | -0.03 | 370925.42 | 14.9 | skipped_fast |
| CHIPUSDT | IDLE | 0.69 | 4.16 | 0.69 | -0.1 | 612287.72 | 3.32 | skipped_fast |
| KITEUSDT | IDLE | 2.59 | 6.24 | 0.23 | 0.04 | 83277.56 | 10.57 | skipped_fast |
| EDELUSDT | IDLE | 2.17 | 3.89 | 2.98 | -0.03 | 78084.06 | 45.1 | skipped_fast |
| BIOUSDT | IDLE | 0.76 | 5.65 | 0.47 | -0.02 | 240832.07 | 6.32 | skipped_fast |
| QAITUSDT | IDLE | 2.2 | 4.16 | 1.63 | -0.0 | 2384.15 | 63.29 | skipped_fast |
| REDUSDT | IDLE | 0.46 | 6.02 | 2.73 | 0.03 | 153517.98 | 14.15 | skipped_fast |
| TELUSDT | IDLE | 2.18 | 5.61 | 4.09 | -0.03 | 164248.24 | 53.25 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.0 | 10250.54 | 70.63 | skipped_fast |
| QNTUSDT | IDLE | 1.04 | 3.47 | 0.98 | 0.01 | 187924.6 | 6.18 | skipped_fast |
| RIZEUSDT | IDLE | 0.46 | 1.91 | 0.34 | -0.05 | 48098.19 | 22.24 | skipped_fast |
| RWAUSDT | IDLE | 1.0 | 1.8 | 1.37 | 0.02 | 57687.66 | 24.4 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 1.93 | 1.38 | -0.01 | 5711.25 | 45.22 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
