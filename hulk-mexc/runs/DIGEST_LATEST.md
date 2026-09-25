# Hulk DIGEST — 2026-09-25T03:41:18Z

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
| XRPUSDT | IDLE | 1.36 | 2.45 | 1.82 | 0.03 | 73801620.76 | 1.96 | skipped_fast |
| BTCUSDT | IDLE | 0.58 | 1.07 | 0.59 | 0.0 | 730550128.38 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.56 | 1.01 | 0.69 | 0.0 | 358907805.59 | 0.04 | skipped_fast |
| PYTHUSDT | IDLE | 1.1 | 3.94 | 1.07 | 0.08 | 987252.7 | 2.91 | skipped_fast |
| RIZEUSDT | IDLE | 1.88 | 34.66 | 11.68 | 0.55 | 94346.13 | 11.98 | skipped_fast |
| HBARUSDT | IDLE | 1.34 | 2.4 | 1.93 | 0.02 | 913386.81 | 2.17 | skipped_fast |
| CCUSDT | IDLE | 1.56 | 3.24 | 0.35 | 0.05 | 510253.17 | 7.81 | skipped_fast |
| KITEUSDT | IDLE | 3.0 | 5.34 | 4.45 | -0.03 | 64771.13 | 10.29 | skipped_fast |
| WUSDT | IDLE | 1.6 | 2.87 | 2.22 | 0.03 | 265370.75 | 11.17 | skipped_fast |
| REDUSDT | IDLE | 1.65 | 4.17 | 0.85 | 0.08 | 108168.27 | 7.93 | skipped_fast |
| CHIPUSDT | IDLE | 1.12 | 5.81 | 4.24 | 0.1 | 106817.14 | 15.05 | skipped_fast |
| ZBCNUSDT | IDLE | 0.83 | 1.55 | 0.73 | 0.01 | 236639.62 | 11.72 | skipped_fast |
| EDELUSDT | IDLE | 0.6 | 6.72 | 2.64 | 0.08 | 184274.91 | 26.8 | skipped_fast |
| TELUSDT | IDLE | 2.31 | 4.86 | 4.21 | -0.07 | 109898.57 | 37.69 | skipped_fast |
| QNTUSDT | IDLE | 0.89 | 7.31 | 3.12 | 0.3 | 313835.46 | 18.48 | skipped_fast |
| BIOUSDT | IDLE | 0.81 | 2.18 | 1.16 | 0.07 | 90660.67 | 6.54 | skipped_fast |
| RWAINCUSDT | IDLE | 1.02 | 5.12 | 2.59 | 0.18 | 13552.09 | 59.62 | skipped_fast |
| MNSRYUSDT | IDLE | 0.73 | 1.41 | 0.35 | 0.01 | 39652.71 | 5.16 | skipped_fast |
| RWAUSDT | IDLE | 0.38 | 0.73 | 0.22 | 0.01 | 58947.97 | 14.62 | skipped_fast |
| FLUIDUSDT | IDLE | 0.59 | 1.13 | 0.27 | 0.04 | 1081.64 | 22.13 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
