# Hulk DIGEST — 2026-08-22T01:18:08Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.72 | 9.41 | 0.08 | 0.15 | 6651740.61 | 3.92 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.18 | 8.4 | 0.51 | 0.16 | 150003296.13 | 3.39 | skipped_fast |
| HBARUSDT | IDLE | 3.01 | 6.36 | 0.78 | 0.09 | 955194.62 | 1.25 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.92 | 0.11 | 547067.18 | 44.59 | skipped_fast |
| CCUSDT | IDLE | 1.76 | 7.18 | 0.12 | 0.16 | 659954.45 | 11.37 | skipped_fast |
| WUSDT | IDLE | 2.71 | 6.65 | 0.89 | 0.09 | 392586.32 | 12.22 | skipped_fast |
| CHIPUSDT | IDLE | 1.66 | 3.56 | 1.76 | -0.01 | 522932.49 | 3.09 | skipped_fast |
| BIOUSDT | IDLE | 2.47 | 5.57 | 0.3 | 0.04 | 186517.26 | 6.12 | skipped_fast |
| EDELUSDT | IDLE | 2.61 | 5.5 | 1.85 | -0.02 | 79585.35 | 22.15 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.03 | 0.11 | 60514.79 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 0.97 | 8.27 | 4.36 | 0.19 | 159675.0 | 15.09 | skipped_fast |
| QNTUSDT | IDLE | 2.42 | 5.18 | 0.91 | 0.07 | 170459.8 | 4.52 | skipped_fast |
| TELUSDT | IDLE | 2.56 | 6.19 | 0.72 | 0.05 | 181113.08 | 41.22 | skipped_fast |
| KITEUSDT | IDLE | 1.47 | 4.48 | 0.23 | 0.11 | 60916.32 | 10.84 | skipped_fast |
| QAITUSDT | IDLE | 2.06 | 4.02 | 0.7 | 0.01 | 3856.35 | 67.05 | skipped_fast |
| RWAINCUSDT | IDLE | 1.33 | 2.45 | 1.43 | 0.03 | 9620.22 | 16.16 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 21.69 | skipped_fast |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.33 | 0.04 | 55237.29 | 32.81 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
