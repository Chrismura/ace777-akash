# Hulk DIGEST — 2026-10-10T09:52:41Z

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
| WUSDT | IDLE | 1.82 | 3.79 | 1.52 | -0.04 | 1420330.66 | 8.24 | skipped_fast |
| XRPUSDT | IDLE | 0.36 | 0.66 | 0.42 | 0.0 | 23111562.47 | 0.71 | skipped_fast |
| BTCUSDT | IDLE | 0.22 | 0.43 | 0.11 | 0.0 | 237139511.75 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.16 | 0.31 | 0.12 | -0.0 | 114089708.73 | 0.04 | skipped_fast |
| PYTHUSDT | IDLE | 1.19 | 3.04 | 2.9 | -0.08 | 1377359.94 | 1.28 | skipped_fast |
| QNTUSDT | IDLE | 1.86 | 3.57 | 1.0 | 0.02 | 1225608.98 | 0.8 | skipped_fast |
| CCUSDT | IDLE | 0.68 | 1.36 | 1.04 | 0.04 | 567350.44 | 8.27 | skipped_fast |
| KITEUSDT | IDLE | 2.5 | 4.72 | 1.89 | 0.0 | 77514.41 | 8.81 | skipped_fast |
| RWAINCUSDT | IDLE | 1.97 | 3.6 | 2.24 | 0.01 | 11020.73 | 14.8 | skipped_fast |
| CHIPUSDT | IDLE | 1.12 | 3.56 | 3.07 | 0.06 | 99722.93 | 5.72 | skipped_fast |
| ZBCNUSDT | IDLE | 0.6 | 1.51 | 0.3 | -0.07 | 262280.92 | 14.84 | skipped_fast |
| EDELUSDT | IDLE | 0.64 | 2.32 | 1.38 | 0.13 | 204847.28 | 4.99 | skipped_fast |
| REDUSDT | IDLE | 1.43 | 2.64 | 1.5 | 0.01 | 56505.36 | 14.72 | skipped_fast |
| BIOUSDT | IDLE | 1.15 | 2.06 | 1.64 | 0.02 | 72508.11 | 6.95 | skipped_fast |
| HBARUSDT | IDLE | 0.99 | 1.9 | 0.5 | 0.01 | 311481.21 | 2.15 | skipped_fast |
| RWAUSDT | IDLE | 1.66 | 2.92 | 2.61 | -0.01 | 52787.43 | 7.86 | skipped_fast |
| TELUSDT | IDLE | 1.63 | 2.95 | 2.02 | -0.01 | 118346.26 | 48.77 | skipped_fast |
| RIZEUSDT | IDLE | 0.4 | 2.28 | 0.86 | 0.07 | 64753.39 | 57.18 | skipped_fast |
| MNSRYUSDT | IDLE | 0.39 | 0.77 | 0.13 | 0.01 | 41147.84 | 8.1 | skipped_fast |
| FLUIDUSDT | IDLE | 0.25 | 1.47 | 1.05 | -0.01 | 17332.36 | 21.36 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
