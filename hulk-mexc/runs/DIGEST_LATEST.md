# Hulk DIGEST — 2026-08-21T21:51:14Z

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
| PYTHUSDT | IDLE | 1.17 | 4.51 | 0.53 | 0.09 | 5668888.75 | 2.06 | skipped_fast |
| XRPUSDT | IDLE | 1.09 | 3.73 | 0.62 | 0.11 | 129946195.98 | 1.42 | skipped_fast |
| CHIPUSDT | IDLE | 1.88 | 5.61 | 3.64 | 0.05 | 527074.63 | 3.09 | skipped_fast |
| HBARUSDT | IDLE | 2.05 | 4.49 | 0.38 | 0.08 | 826192.29 | 1.27 | skipped_fast |
| ZBCNUSDT | IDLE | 1.92 | 8.19 | 2.81 | 0.1 | 491149.57 | 33.89 | skipped_fast |
| CCUSDT | IDLE | 1.29 | 3.86 | 0.04 | 0.11 | 638797.88 | 8.2 | skipped_fast |
| WUSDT | IDLE | 1.96 | 3.91 | 0.03 | 0.07 | 368715.58 | 10.4 | skipped_fast |
| BIOUSDT | IDLE | 2.39 | 5.2 | 1.5 | 0.03 | 187305.55 | 3.12 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 11.01 | 9.25 | 0.17 | 154085.97 | 12.27 | skipped_fast |
| RIZEUSDT | IDLE | 1.86 | 9.54 | 1.08 | 0.04 | 55827.59 | 31.52 | skipped_fast |
| EDELUSDT | IDLE | 1.9 | 4.12 | 0.55 | -0.04 | 83634.09 | 22.15 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 59.7 | skipped_fast |
| RWAINCUSDT | IDLE | 2.22 | 4.3 | 0.95 | 0.02 | 10222.59 | 42.69 | skipped_fast |
| KITEUSDT | IDLE | 1.27 | 4.0 | 1.2 | 0.12 | 61257.26 | 11.96 | skipped_fast |
| TELUSDT | IDLE | 1.91 | 4.81 | 1.04 | 0.03 | 185321.59 | 42.19 | skipped_fast |
| QNTUSDT | IDLE | 1.36 | 2.65 | 0.52 | 0.04 | 62608.63 | 7.72 | skipped_fast |
| RWAUSDT | IDLE | 0.6 | 1.17 | 0.25 | 0.03 | 54020.48 | 24.78 | skipped_fast |
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
