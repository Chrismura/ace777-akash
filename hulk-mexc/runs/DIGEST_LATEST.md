# Hulk DIGEST — 2026-10-10T08:45:09Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| WUSDT | IDLE | 1.35 | 3.63 | 3.31 | -0.05 | 1769557.73 | 13.74 | skipped_fast |
| XRPUSDT | IDLE | 0.48 | 0.89 | 0.43 | 0.0 | 23504014.11 | 2.13 | skipped_fast |
| ETHUSDT | IDLE | 0.2 | 0.37 | 0.21 | -0.0 | 118579153.02 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.2 | 0.39 | 0.09 | 0.0 | 237396371.59 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.09 | 2.9 | 1.6 | -0.06 | 1440282.27 | 1.26 | skipped_fast |
| QNTUSDT | IDLE | 1.56 | 3.1 | 0.07 | 0.03 | 1141283.03 | 8.35 | skipped_fast |
| CCUSDT | IDLE | 0.8 | 1.7 | 0.77 | 0.03 | 575663.96 | 10.68 | skipped_fast |
| KITEUSDT | IDLE | 2.09 | 4.12 | 0.43 | 0.0 | 76525.41 | 10.37 | skipped_fast |
| CHIPUSDT | IDLE | 1.24 | 4.04 | 2.72 | 0.06 | 99971.92 | 13.29 | skipped_fast |
| RWAINCUSDT | IDLE | 2.03 | 3.65 | 2.67 | 0.02 | 10142.12 | 44.35 | skipped_fast |
| ZBCNUSDT | IDLE | 0.67 | 1.75 | 0.62 | -0.07 | 263615.98 | 11.4 | skipped_fast |
| BIOUSDT | IDLE | 1.14 | 2.06 | 1.47 | 0.01 | 72093.21 | 3.46 | skipped_fast |
| EDELUSDT | IDLE | 0.62 | 2.32 | 1.3 | 0.12 | 209173.29 | 22.42 | skipped_fast |
| REDUSDT | IDLE | 1.31 | 2.56 | 0.39 | 0.02 | 56975.42 | 13.23 | skipped_fast |
| HBARUSDT | IDLE | 1.0 | 1.9 | 0.63 | 0.01 | 300059.35 | 5.39 | skipped_fast |
| TELUSDT | IDLE | 1.63 | 2.95 | 2.02 | -0.01 | 119968.98 | 32.49 | skipped_fast |
| RWAUSDT | IDLE | 1.65 | 2.92 | 2.53 | -0.01 | 52225.49 | 15.72 | skipped_fast |
| RIZEUSDT | IDLE | 0.4 | 2.28 | 1.11 | 0.07 | 64822.91 | 49.56 | skipped_fast |
| MNSRYUSDT | IDLE | 0.4 | 0.77 | 0.22 | 0.01 | 41115.83 | 29.73 | skipped_fast |
| FLUIDUSDT | IDLE | 0.25 | 1.47 | 1.13 | -0.0 | 17293.45 | 20.91 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
