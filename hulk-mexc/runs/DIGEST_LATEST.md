# Hulk DIGEST — 2026-10-27T14:24:59Z

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
| XRPUSDT | IDLE | 1.25 | 2.38 | 0.76 | 0.01 | 21166611.67 | 0.76 | skipped_fast |
| ETHUSDT | IDLE | 1.01 | 1.88 | 0.93 | -0.0 | 151861144.15 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.65 | 1.21 | 0.57 | -0.0 | 322923894.23 | 0.0 | skipped_fast |
| WUSDT | IDLE | 3.45 | 6.82 | 1.97 | 0.07 | 622162.49 | 26.41 | skipped_fast |
| QNTUSDT | IDLE | 2.86 | 5.67 | 4.89 | -0.09 | 885855.0 | 1.52 | skipped_fast |
| CHIPUSDT | IDLE | 2.43 | 8.15 | 3.06 | 0.07 | 286576.88 | 13.37 | skipped_fast |
| REDUSDT | IDLE | 3.51 | 6.97 | 0.4 | 0.05 | 60743.1 | 14.35 | skipped_fast |
| KITEUSDT | IDLE | 3.26 | 6.39 | 0.85 | 0.04 | 56854.89 | 12.68 | skipped_fast |
| PYTHUSDT | IDLE | 0.98 | 1.8 | 1.02 | -0.04 | 457719.11 | 5.51 | skipped_fast |
| EDELUSDT | IDLE | 1.29 | 2.41 | 1.19 | 0.01 | 398562.26 | 24.7 | skipped_fast |
| CCUSDT | IDLE | 1.79 | 3.57 | 0.09 | -0.01 | 226201.48 | 6.05 | skipped_fast |
| RWAINCUSDT | IDLE | 1.67 | 6.75 | 5.94 | -0.15 | 57222.02 | 6.79 | skipped_fast |
| ZBCNUSDT | IDLE | 1.18 | 3.23 | 2.37 | 0.02 | 249714.49 | 50.22 | skipped_fast |
| BIOUSDT | IDLE | 1.4 | 2.62 | 1.21 | -0.01 | 55892.15 | 9.07 | skipped_fast |
| WAXLUSDT | IDLE | 2.12 | 4.04 | 1.35 | 0.02 | 54711.13 | 53.08 | skipped_fast |
| LAUSDT | IDLE | 1.8 | 3.52 | 0.59 | 0.01 | 60595.43 | 22.2 | skipped_fast |
| HBARUSDT | IDLE | 0.83 | 1.5 | 1.08 | -0.02 | 192107.77 | 7.92 | skipped_fast |
| RIZEUSDT | IDLE | 0.59 | 1.1 | 0.49 | -0.0 | 41337.93 | 65.33 | skipped_fast |
| IOTAUSDT | IDLE | 1.05 | 2.0 | 0.66 | -0.02 | 95369.68 | 11.9 | skipped_fast |
| RWAUSDT | IDLE | 1.21 | 2.29 | 0.8 | -0.01 | 56945.5 | 40.31 | skipped_fast |
| FLUIDUSDT | IDLE | 1.24 | 2.23 | 1.65 | 0.03 | 3345.88 | 21.3 | skipped_fast |
| MNSRYUSDT | IDLE | 0.42 | 0.77 | 0.51 | 0.0 | 37141.41 | 79.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
