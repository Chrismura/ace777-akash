# Hulk DIGEST — 2026-09-12T21:32:53Z

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
| XRPUSDT | IDLE | 0.48 | 0.88 | 0.6 | 0.0 | 16389564.61 | 2.2 | skipped_fast |
| ETHUSDT | IDLE | 0.45 | 0.84 | 0.45 | -0.0 | 231822643.99 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.24 | 0.45 | 0.25 | -0.0 | 370340266.4 | 0.0 | skipped_fast |
| RIZEUSDT | IDLE | 2.09 | 37.35 | 13.38 | 0.45 | 91319.55 | 50.89 | skipped_fast |
| ZBCNUSDT | IDLE | 2.06 | 5.09 | 2.52 | -0.0 | 220635.56 | 17.76 | skipped_fast |
| PYTHUSDT | IDLE | 1.12 | 3.0 | 1.22 | 0.08 | 398410.33 | 1.81 | skipped_fast |
| CHIPUSDT | IDLE | 2.41 | 5.89 | 4.33 | 0.03 | 74936.8 | 16.61 | skipped_fast |
| WUSDT | IDLE | 2.04 | 3.72 | 2.41 | 0.03 | 170921.66 | 12.03 | skipped_fast |
| EDELUSDT | IDLE | 1.88 | 4.23 | 1.32 | 0.05 | 165286.49 | 25.2 | skipped_fast |
| RWAINCUSDT | IDLE | 2.1 | 4.25 | 1.18 | -0.02 | 10649.09 | 16.35 | skipped_fast |
| CCUSDT | IDLE | 1.06 | 1.89 | 1.56 | -0.01 | 213897.63 | 6.19 | skipped_fast |
| REDUSDT | IDLE | 1.19 | 2.18 | 1.36 | 0.02 | 58227.22 | 16.94 | skipped_fast |
| BIOUSDT | IDLE | 0.85 | 1.53 | 1.16 | 0.02 | 70785.16 | 3.92 | skipped_fast |
| KITEUSDT | IDLE | 0.88 | 1.72 | 0.21 | -0.01 | 62646.09 | 13.04 | skipped_fast |
| HBARUSDT | IDLE | 0.73 | 1.36 | 0.64 | 0.0 | 161146.95 | 1.34 | skipped_fast |
| TELUSDT | IDLE | 0.94 | 1.7 | 1.19 | -0.06 | 89238.86 | 36.25 | skipped_fast |
| QNTUSDT | IDLE | 0.53 | 0.92 | 0.9 | -0.0 | 40830.65 | 1.57 | skipped_fast |
| RWAUSDT | IDLE | 0.47 | 0.82 | 0.74 | -0.0 | 53457.8 | 7.44 | skipped_fast |
| MNSRYUSDT | IDLE | 0.21 | 0.39 | 0.15 | -0.0 | 25893.26 | 11.12 | skipped_fast |
| FLUIDUSDT | IDLE | 0.27 | 0.54 | 0.0 | 0.03 | 1375.44 | 19.63 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
