# Hulk DIGEST — 2026-08-22T00:33:39Z

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
| PYTHUSDT | IDLE | 1.73 | 6.39 | 0.6 | 0.11 | 6396118.55 | 2.03 | skipped_fast |
| XRPUSDT | IDLE | 1.98 | 8.23 | 0.35 | 0.16 | 144874361.37 | 4.08 | skipped_fast |
| HBARUSDT | IDLE | 2.8 | 6.36 | 1.67 | 0.07 | 937879.09 | 2.52 | skipped_fast |
| ZBCNUSDT | IDLE | 2.87 | 11.25 | 2.36 | 0.12 | 538830.41 | 29.39 | skipped_fast |
| CCUSDT | IDLE | 1.92 | 7.42 | 0.42 | 0.14 | 638904.11 | 7.06 | skipped_fast |
| WUSDT | IDLE | 2.75 | 6.91 | 1.22 | 0.08 | 387379.57 | 12.27 | skipped_fast |
| CHIPUSDT | IDLE | 1.63 | 3.56 | 1.4 | 0.02 | 557344.64 | 6.16 | skipped_fast |
| BIOUSDT | IDLE | 2.25 | 5.04 | 0.46 | 0.02 | 185990.63 | 6.18 | skipped_fast |
| EDELUSDT | IDLE | 2.61 | 5.5 | 1.85 | -0.02 | 79696.1 | 11.06 | skipped_fast |
| RIZEUSDT | IDLE | 2.21 | 9.82 | 2.55 | 0.13 | 59861.41 | 45.1 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 19.88 | skipped_fast |
| TELUSDT | IDLE | 2.84 | 6.89 | 0.66 | 0.05 | 186262.27 | 36.04 | skipped_fast |
| QNTUSDT | IDLE | 2.55 | 5.42 | 1.3 | 0.06 | 170451.23 | 7.56 | skipped_fast |
| REDUSDT | IDLE | 0.62 | 5.68 | 0.0 | 0.23 | 157816.7 | 18.73 | skipped_fast |
| KITEUSDT | IDLE | 1.06 | 3.12 | 0.27 | 0.1 | 60962.33 | 10.11 | skipped_fast |
| RWAINCUSDT | IDLE | 1.69 | 2.99 | 2.54 | 0.04 | 9704.24 | 59.19 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.49 | 0.03 | 54670.54 | 16.42 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 21.04 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
