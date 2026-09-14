# Hulk DIGEST — 2026-09-14T09:42:19Z

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
| XRPUSDT | IDLE | 0.84 | 1.65 | 0.19 | 0.04 | 30385606.19 | 1.44 | skipped_fast |
| ETHUSDT | IDLE | 0.51 | 0.96 | 0.45 | 0.02 | 322823411.11 | 0.44 | skipped_fast |
| BTCUSDT | IDLE | 0.41 | 0.8 | 0.15 | 0.01 | 384306397.51 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.67 | 5.67 | 4.87 | 0.03 | 516765.61 | 1.8 | skipped_fast |
| CHIPUSDT | IDLE | 2.44 | 8.31 | 7.28 | -0.13 | 104921.89 | 22.03 | skipped_fast |
| REDUSDT | IDLE | 2.38 | 5.95 | 0.03 | 0.06 | 139000.56 | 15.23 | skipped_fast |
| RIZEUSDT | IDLE | 1.69 | 19.88 | 6.79 | 0.18 | 72890.3 | 88.95 | skipped_fast |
| EDELUSDT | IDLE | 1.39 | 6.62 | 4.28 | 0.14 | 219099.89 | 28.88 | skipped_fast |
| WUSDT | IDLE | 1.26 | 2.25 | 1.78 | 0.01 | 210099.96 | 3.97 | skipped_fast |
| CCUSDT | IDLE | 1.18 | 2.12 | 1.55 | -0.0 | 242964.82 | 10.5 | skipped_fast |
| KITEUSDT | IDLE | 1.69 | 2.96 | 2.79 | -0.02 | 60968.36 | 10.33 | skipped_fast |
| RWAINCUSDT | IDLE | 1.78 | 3.35 | 1.4 | 0.02 | 9387.11 | 5.47 | skipped_fast |
| ZBCNUSDT | IDLE | 1.02 | 1.85 | 1.25 | -0.01 | 196299.54 | 19.85 | skipped_fast |
| BIOUSDT | IDLE | 0.9 | 1.65 | 1.05 | 0.01 | 73565.82 | 3.92 | skipped_fast |
| HBARUSDT | IDLE | 0.55 | 1.01 | 0.64 | 0.02 | 270186.96 | 1.31 | skipped_fast |
| FLUIDUSDT | IDLE | 1.12 | 2.06 | 1.16 | 0.01 | 783.0 | 21.7 | skipped_fast |
| QNTUSDT | IDLE | 0.6 | 1.1 | 0.72 | 0.0 | 38164.56 | 10.97 | skipped_fast |
| TELUSDT | IDLE | 0.8 | 1.59 | 0.06 | 0.0 | 87598.99 | 62.81 | skipped_fast |
| MNSRYUSDT | IDLE | 0.26 | 0.49 | 0.17 | -0.0 | 29763.49 | 6.97 | skipped_fast |
| RWAUSDT | IDLE | 0.25 | 0.45 | 0.3 | 0.01 | 53156.53 | 22.21 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
