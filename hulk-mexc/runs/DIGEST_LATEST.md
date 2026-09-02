# Hulk DIGEST — 2026-09-02T12:42:06Z

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
| XRPUSDT | IDLE | 1.78 | 3.25 | 2.07 | -0.03 | 40463047.12 | 1.51 | skipped_fast |
| ETHUSDT | IDLE | 1.66 | 3.04 | 1.89 | -0.02 | 410553457.65 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.06 | 1.94 | 1.16 | -0.01 | 534206791.18 | 0.0 | skipped_fast |
| CHIPUSDT | IDLE | 2.25 | 8.48 | 6.96 | 0.11 | 997693.23 | 2.3 | skipped_fast |
| PYTHUSDT | IDLE | 1.38 | 4.53 | 2.56 | 0.08 | 884981.9 | 1.84 | skipped_fast |
| WUSDT | IDLE | 1.96 | 3.48 | 2.97 | 0.0 | 411986.23 | 13.75 | skipped_fast |
| CCUSDT | IDLE | 1.27 | 2.23 | 2.06 | -0.05 | 346622.94 | 8.06 | skipped_fast |
| QNTUSDT | IDLE | 3.45 | 6.19 | 4.71 | 0.03 | 71174.87 | 3.13 | skipped_fast |
| REDUSDT | IDLE | 1.88 | 4.29 | 0.3 | 0.06 | 151991.97 | 11.31 | skipped_fast |
| EDELUSDT | IDLE | 1.39 | 7.39 | 5.24 | 0.05 | 171198.72 | 33.06 | skipped_fast |
| ZBCNUSDT | IDLE | 1.21 | 2.41 | 2.18 | -0.02 | 222229.58 | 18.29 | skipped_fast |
| KITEUSDT | IDLE | 1.51 | 6.19 | 1.15 | 0.15 | 87111.66 | 9.42 | skipped_fast |
| BIOUSDT | IDLE | 1.53 | 2.8 | 1.75 | -0.03 | 76026.84 | 3.97 | skipped_fast |
| RIZEUSDT | IDLE | 1.86 | 7.09 | 5.37 | -0.1 | 40178.76 | 81.84 | skipped_fast |
| RWAINCUSDT | IDLE | 1.12 | 3.27 | 1.8 | 0.09 | 10944.89 | 21.53 | skipped_fast |
| HBARUSDT | IDLE | 1.09 | 1.99 | 1.31 | -0.03 | 232274.07 | 1.36 | skipped_fast |
| TELUSDT | IDLE | 1.65 | 3.02 | 1.93 | -0.02 | 83325.01 | 59.74 | skipped_fast |
| FLUIDUSDT | IDLE | 0.87 | 1.52 | 1.49 | -0.04 | 328.21 | 21.95 | skipped_fast |
| RWAUSDT | IDLE | 0.43 | 0.77 | 0.61 | -0.01 | 51131.38 | 15.41 | skipped_fast |
| MNSRYUSDT | IDLE | 0.42 | 0.75 | 0.58 | -0.02 | 35466.06 | 39.95 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
