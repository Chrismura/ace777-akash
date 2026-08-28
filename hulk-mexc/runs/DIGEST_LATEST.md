# Hulk DIGEST — 2026-08-28T16:08:24Z

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
| XRPUSDT | IDLE | 2.02 | 3.74 | 1.95 | -0.04 | 51918223.15 | 2.13 | skipped_fast |
| CHIPUSDT | IDLE | 2.35 | 14.12 | 11.67 | -0.02 | 902635.5 | 19.14 | skipped_fast |
| PYTHUSDT | IDLE | 1.97 | 4.53 | 3.09 | -0.06 | 1037277.6 | 12.76 | skipped_fast |
| QAITUSDT | IDLE | 2.44 | 32.58 | 20.86 | -0.19 | 70014.46 | 71.94 | skipped_fast |
| HBARUSDT | IDLE | 3.01 | 5.38 | 4.22 | -0.06 | 418530.23 | 1.33 | skipped_fast |
| CCUSDT | IDLE | 1.88 | 3.32 | 2.93 | -0.07 | 377246.67 | 10.89 | skipped_fast |
| WUSDT | IDLE | 2.5 | 4.48 | 3.5 | -0.06 | 209039.17 | 11.95 | skipped_fast |
| ZBCNUSDT | IDLE | 2.15 | 4.44 | 3.72 | -0.04 | 225977.9 | 18.82 | skipped_fast |
| REDUSDT | IDLE | 2.69 | 6.25 | 4.52 | -0.06 | 68973.46 | 12.58 | skipped_fast |
| BIOUSDT | IDLE | 2.07 | 3.78 | 2.43 | -0.04 | 94974.42 | 7.12 | skipped_fast |
| RWAUSDT | IDLE | 3.11 | 5.99 | 1.51 | 0.03 | 54791.66 | 24.24 | skipped_fast |
| KITEUSDT | IDLE | 1.54 | 2.81 | 1.81 | -0.04 | 78164.59 | 11.17 | skipped_fast |
| FLUIDUSDT | IDLE | 2.91 | 5.1 | 4.85 | -0.06 | 4740.83 | 22.11 | skipped_fast |
| EDELUSDT | IDLE | 1.45 | 3.97 | 3.82 | -0.16 | 62853.98 | 52.82 | skipped_fast |
| RIZEUSDT | IDLE | 1.27 | 5.64 | 0.21 | -0.04 | 82135.6 | 54.17 | skipped_fast |
| QNTUSDT | IDLE | 2.24 | 4.19 | 3.23 | -0.02 | 50680.44 | 9.79 | skipped_fast |
| RWAINCUSDT | IDLE | 1.17 | 3.82 | 1.92 | -0.01 | 18811.83 | 76.21 | skipped_fast |
| TELUSDT | IDLE | 1.39 | 3.14 | 2.77 | -0.05 | 128367.08 | 22.31 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
