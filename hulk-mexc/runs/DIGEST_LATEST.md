# Hulk DIGEST — 2026-10-19T22:06:44Z

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
| ETHUSDT | IDLE | 0.4 | 0.78 | 0.15 | 0.01 | 135963871.3 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.39 | 0.76 | 0.07 | 0.01 | 22588248.92 | 1.53 | skipped_fast |
| BTCUSDT | IDLE | 0.26 | 0.49 | 0.15 | 0.01 | 336429035.91 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.89 | 3.58 | 1.35 | -0.0 | 820527.5 | 4.09 | skipped_fast |
| WUSDT | IDLE | 2.47 | 4.69 | 1.72 | 0.03 | 696519.77 | 15.81 | skipped_fast |
| QNTUSDT | IDLE | 1.13 | 2.32 | 0.55 | 0.04 | 742617.1 | 4.59 | skipped_fast |
| EDELUSDT | IDLE | 2.12 | 3.95 | 1.94 | 0.02 | 202865.65 | 18.63 | skipped_fast |
| CCUSDT | IDLE | 0.79 | 1.57 | 0.11 | 0.06 | 410187.95 | 9.56 | skipped_fast |
| ZBCNUSDT | IDLE | 1.01 | 2.64 | 1.46 | 0.03 | 243307.26 | 7.68 | skipped_fast |
| KITEUSDT | IDLE | 1.62 | 3.71 | 0.04 | 0.09 | 71199.88 | 0.81 | skipped_fast |
| HBARUSDT | IDLE | 0.7 | 1.35 | 0.36 | -0.02 | 479185.32 | 3.63 | skipped_fast |
| CHIPUSDT | IDLE | 1.19 | 2.25 | 0.85 | 0.04 | 78818.38 | 14.31 | skipped_fast |
| RWAINCUSDT | IDLE | 0.98 | 2.01 | 1.37 | 0.05 | 72062.76 | 5.11 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 1.94 | 0.13 | 0.01 | 56751.63 | 16.7 | skipped_fast |
| BIOUSDT | IDLE | 0.78 | 1.55 | 0.08 | 0.01 | 69062.55 | 8.49 | skipped_fast |
| RIZEUSDT | IDLE | 0.39 | 1.3 | 0.69 | -0.04 | 53238.15 | 46.09 | skipped_fast |
| IOTAUSDT | IDLE | 0.93 | 1.85 | 0.07 | 0.02 | 90602.23 | 28.86 | skipped_fast |
| WAXLUSDT | IDLE | 1.12 | 2.91 | 1.82 | -0.03 | 62522.84 | 55.73 | skipped_fast |
| LAUSDT | IDLE | 0.78 | 1.54 | 0.13 | 0.01 | 56113.51 | 24.74 | skipped_fast |
| RWAUSDT | IDLE | 0.48 | 0.95 | 0.08 | 0.02 | 55943.49 | 7.85 | skipped_fast |
| MNSRYUSDT | IDLE | 0.16 | 0.29 | 0.21 | 0.0 | 40786.84 | 12.83 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.05 | 4749.48 | 21.23 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
