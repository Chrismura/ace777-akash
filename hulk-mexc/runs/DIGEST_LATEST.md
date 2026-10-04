# Hulk DIGEST — 2026-10-04T12:01:34Z

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
| QNTUSDT | IDLE | 2.82 | 10.56 | 3.22 | -0.0 | 3166919.87 | 2.72 | skipped_fast |
| XRPUSDT | IDLE | 0.39 | 0.74 | 0.33 | 0.01 | 16935109.32 | 0.67 | skipped_fast |
| ETHUSDT | IDLE | 0.31 | 0.57 | 0.28 | 0.01 | 96472117.0 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.3 | 0.58 | 0.13 | 0.01 | 310757858.52 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.85 | 5.31 | 2.87 | 0.08 | 888346.26 | 9.55 | skipped_fast |
| EDELUSDT | IDLE | 1.65 | 8.11 | 1.77 | 0.19 | 499185.52 | 22.46 | skipped_fast |
| PYTHUSDT | IDLE | 2.17 | 3.8 | 3.66 | -0.02 | 305005.84 | 2.58 | skipped_fast |
| KITEUSDT | IDLE | 2.29 | 4.03 | 3.7 | -0.01 | 78060.77 | 8.0 | skipped_fast |
| ZBCNUSDT | IDLE | 1.63 | 2.92 | 2.25 | -0.03 | 239419.81 | 24.29 | skipped_fast |
| MNSRYUSDT | IDLE | 3.55 | 6.42 | 4.6 | 0.0 | 47195.91 | 20.73 | skipped_fast |
| CCUSDT | IDLE | 0.92 | 1.62 | 1.45 | -0.0 | 317697.13 | 10.61 | skipped_fast |
| RWAINCUSDT | IDLE | 2.39 | 4.75 | 0.16 | 0.04 | 5380.78 | 39.18 | skipped_fast |
| CHIPUSDT | IDLE | 1.32 | 2.33 | 2.02 | 0.02 | 61851.01 | 15.66 | skipped_fast |
| BIOUSDT | IDLE | 1.16 | 2.03 | 1.93 | -0.01 | 70709.15 | 3.27 | skipped_fast |
| REDUSDT | IDLE | 1.25 | 2.2 | 2.02 | 0.04 | 65507.4 | 12.61 | skipped_fast |
| RIZEUSDT | IDLE | 1.3 | 8.37 | 2.57 | -0.15 | 54769.58 | 87.08 | skipped_fast |
| HBARUSDT | IDLE | 0.75 | 1.3 | 1.27 | -0.0 | 413855.89 | 8.87 | skipped_fast |
| TELUSDT | IDLE | 1.44 | 2.58 | 2.51 | -0.02 | 132430.22 | 31.5 | skipped_fast |
| FLUIDUSDT | IDLE | 0.69 | 1.44 | 1.28 | 0.04 | 1736.4 | 21.52 | skipped_fast |
| RWAUSDT | IDLE | 0.12 | 0.22 | 0.07 | -0.0 | 55867.87 | 14.59 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
