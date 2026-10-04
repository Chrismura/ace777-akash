# Hulk DIGEST — 2026-10-04T09:01:15Z

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
| QNTUSDT | IDLE | 1.78 | 5.19 | 4.04 | -0.02 | 3135392.46 | 14.23 | skipped_fast |
| XRPUSDT | IDLE | 0.43 | 0.81 | 0.38 | 0.01 | 16211700.5 | 0.67 | skipped_fast |
| ETHUSDT | IDLE | 0.31 | 0.59 | 0.26 | 0.01 | 96340407.04 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.23 | 0.44 | 0.1 | 0.01 | 300806506.64 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.54 | 5.07 | 2.02 | 0.12 | 791737.58 | 15.55 | skipped_fast |
| EDELUSDT | IDLE | 1.31 | 7.23 | 3.98 | 0.18 | 465178.79 | 31.23 | skipped_fast |
| PYTHUSDT | IDLE | 1.73 | 3.2 | 1.68 | 0.01 | 291551.88 | 1.26 | skipped_fast |
| CCUSDT | IDLE | 1.46 | 2.56 | 2.43 | 0.02 | 340637.53 | 10.58 | skipped_fast |
| RWAINCUSDT | IDLE | 2.65 | 5.2 | 0.62 | 0.04 | 5445.02 | 39.23 | skipped_fast |
| KITEUSDT | IDLE | 1.73 | 3.28 | 1.24 | 0.02 | 79250.37 | 8.46 | skipped_fast |
| ZBCNUSDT | IDLE | 1.3 | 2.5 | 0.72 | 0.01 | 219014.32 | 33.46 | skipped_fast |
| RIZEUSDT | IDLE | 1.39 | 8.76 | 4.14 | -0.16 | 53490.88 | 59.35 | skipped_fast |
| HBARUSDT | IDLE | 1.03 | 1.95 | 0.69 | 0.02 | 408498.65 | 1.96 | skipped_fast |
| CHIPUSDT | IDLE | 1.26 | 2.26 | 1.75 | 0.04 | 60745.4 | 13.37 | skipped_fast |
| BIOUSDT | IDLE | 0.85 | 1.49 | 1.4 | 0.01 | 69602.73 | 3.24 | skipped_fast |
| REDUSDT | IDLE | 0.89 | 2.12 | 1.66 | 0.05 | 65543.43 | 12.41 | skipped_fast |
| TELUSDT | IDLE | 1.65 | 3.03 | 2.48 | -0.01 | 135222.75 | 36.37 | skipped_fast |
| FLUIDUSDT | IDLE | 0.66 | 1.44 | 1.42 | 0.04 | 1970.3 | 21.47 | skipped_fast |
| RWAUSDT | IDLE | 0.34 | 0.66 | 0.15 | -0.0 | 54833.79 | 7.3 | skipped_fast |
| MNSRYUSDT | IDLE | 0.26 | 0.51 | 0.1 | 0.0 | 38658.45 | 3.88 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
