# Hulk DIGEST — 2026-10-25T04:58:31Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 0.94 | 1.87 | 0.11 | 0.02 | 26289246.54 | 1.52 | skipped_fast |
| ETHUSDT | IDLE | 0.62 | 1.23 | 0.13 | -0.01 | 121784597.85 | 0.08 | skipped_fast |
| BTCUSDT | IDLE | 0.3 | 0.58 | 0.09 | 0.0 | 239534387.42 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.27 | 2.44 | 1.05 | -0.06 | 765679.34 | 15.53 | skipped_fast |
| PYTHUSDT | IDLE | 1.41 | 2.71 | 0.68 | 0.01 | 502199.3 | 1.4 | skipped_fast |
| EDELUSDT | IDLE | 0.82 | 2.01 | 0.89 | -0.06 | 595553.67 | 16.58 | skipped_fast |
| QNTUSDT | IDLE | 2.57 | 4.97 | 1.18 | -0.0 | 366746.3 | 2.72 | skipped_fast |
| KITEUSDT | IDLE | 1.84 | 3.23 | 3.03 | -0.06 | 59194.83 | 11.49 | skipped_fast |
| CHIPUSDT | IDLE | 1.52 | 4.52 | 2.23 | 0.05 | 93104.86 | 17.7 | skipped_fast |
| REDUSDT | IDLE | 1.53 | 3.84 | 1.75 | 0.01 | 93080.66 | 16.11 | skipped_fast |
| ZBCNUSDT | IDLE | 0.82 | 1.85 | 1.23 | 0.0 | 225975.9 | 9.76 | skipped_fast |
| LAUSDT | IDLE | 2.01 | 11.5 | 5.82 | -0.07 | 107046.14 | 16.33 | skipped_fast |
| CCUSDT | IDLE | 0.69 | 1.26 | 0.85 | -0.02 | 208565.77 | 7.92 | skipped_fast |
| BIOUSDT | IDLE | 1.05 | 1.89 | 1.38 | -0.02 | 65439.24 | 4.38 | skipped_fast |
| RWAINCUSDT | IDLE | 1.17 | 2.25 | 0.59 | 0.0 | 55536.47 | 10.81 | skipped_fast |
| WAXLUSDT | IDLE | 2.2 | 5.99 | 2.35 | 0.02 | 56135.16 | 34.17 | skipped_fast |
| RIZEUSDT | IDLE | 0.72 | 2.01 | 0.64 | -0.04 | 41584.7 | 48.55 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 1.52 | 0.61 | 0.0 | 203782.85 | 15.36 | skipped_fast |
| IOTAUSDT | IDLE | 1.0 | 1.89 | 0.75 | -0.01 | 67545.96 | 29.59 | skipped_fast |
| FLUIDUSDT | IDLE | 0.94 | 1.83 | 1.39 | -0.04 | 13024.02 | 21.68 | skipped_fast |
| RWAUSDT | IDLE | 0.37 | 0.72 | 0.16 | -0.0 | 53280.57 | 15.85 | skipped_fast |
| MNSRYUSDT | IDLE | 0.4 | 0.74 | 0.39 | -0.01 | 37402.6 | 42.1 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
