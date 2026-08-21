# Hulk DIGEST — 2026-08-21T22:18:15Z

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
| PYTHUSDT | IDLE | 1.36 | 5.17 | 0.2 | 0.11 | 5736366.02 | 2.04 | skipped_fast |
| XRPUSDT | IDLE | 1.52 | 5.44 | 0.4 | 0.14 | 131826361.1 | 3.49 | skipped_fast |
| CCUSDT | IDLE | 1.76 | 6.45 | 0.23 | 0.13 | 645198.29 | 6.23 | skipped_fast |
| HBARUSDT | IDLE | 2.2 | 4.71 | 0.6 | 0.09 | 852427.48 | 1.27 | skipped_fast |
| WUSDT | IDLE | 2.46 | 5.3 | 0.22 | 0.08 | 369707.67 | 12.33 | skipped_fast |
| CHIPUSDT | IDLE | 1.49 | 4.54 | 1.33 | 0.06 | 534235.54 | 3.05 | skipped_fast |
| ZBCNUSDT | IDLE | 1.52 | 6.5 | 0.26 | 0.11 | 499584.64 | 11.82 | skipped_fast |
| BIOUSDT | IDLE | 2.27 | 5.04 | 0.77 | 0.03 | 187820.49 | 6.19 | skipped_fast |
| REDUSDT | IDLE | 1.32 | 11.01 | 8.04 | 0.18 | 156307.71 | 12.11 | skipped_fast |
| EDELUSDT | IDLE | 1.94 | 4.24 | 0.33 | -0.04 | 82362.14 | 33.06 | skipped_fast |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 2.51 | 6.45 | 0.56 | 0.06 | 186785.81 | 30.98 | skipped_fast |
| RWAINCUSDT | IDLE | 2.13 | 4.07 | 1.27 | 0.03 | 10238.87 | 70.14 | skipped_fast |
| KITEUSDT | IDLE | 1.2 | 3.58 | 0.74 | 0.11 | 61393.84 | 10.11 | skipped_fast |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.83 | 0.06 | 56363.79 | 29.49 | skipped_fast |
| QNTUSDT | IDLE | 1.66 | 3.3 | 0.2 | 0.05 | 65431.23 | 7.65 | skipped_fast |
| RWAUSDT | IDLE | 0.9 | 1.75 | 0.33 | 0.04 | 54168.39 | 24.68 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 21.78 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
