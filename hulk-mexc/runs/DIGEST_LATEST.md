# Hulk DIGEST — 2026-10-17T11:17:04Z

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
| WUSDT | IDLE | 2.72 | 5.53 | 4.63 | -0.02 | 1355961.05 | 13.05 | skipped_fast |
| XRPUSDT | IDLE | 0.36 | 0.67 | 0.33 | -0.03 | 21875399.61 | 1.53 | skipped_fast |
| ETHUSDT | IDLE | 0.29 | 0.57 | 0.08 | -0.02 | 141235466.31 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.13 | 0.25 | 0.13 | -0.01 | 278367202.7 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 0.72 | 1.71 | 0.67 | -0.08 | 1503083.95 | 1.18 | skipped_fast |
| ZBCNUSDT | IDLE | 2.36 | 5.26 | 1.08 | -0.05 | 222002.66 | 12.49 | skipped_fast |
| KITEUSDT | IDLE | 2.41 | 4.26 | 3.79 | -0.01 | 56415.59 | 9.04 | skipped_fast |
| CCUSDT | IDLE | 0.87 | 1.57 | 1.16 | -0.01 | 301239.95 | 8.7 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 1.57 | 0.97 | -0.03 | 585162.11 | 2.95 | skipped_fast |
| EDELUSDT | IDLE | 1.37 | 2.42 | 2.19 | -0.05 | 156222.16 | 17.23 | skipped_fast |
| CHIPUSDT | IDLE | 1.29 | 2.82 | 2.74 | -0.08 | 101404.4 | 11.0 | skipped_fast |
| RWAINCUSDT | IDLE | 1.23 | 4.84 | 2.2 | -0.07 | 22974.21 | 10.72 | skipped_fast |
| BIOUSDT | IDLE | 0.78 | 1.37 | 1.27 | -0.05 | 66272.27 | 4.03 | skipped_fast |
| REDUSDT | IDLE | 0.64 | 1.24 | 1.03 | -0.07 | 73693.75 | 17.63 | skipped_fast |
| RIZEUSDT | IDLE | 0.78 | 1.54 | 0.34 | 0.01 | 44544.32 | 38.11 | skipped_fast |
| HBARUSDT | IDLE | 0.55 | 0.96 | 0.88 | -0.04 | 202882.51 | 4.8 | skipped_fast |
| RWAUSDT | IDLE | 1.22 | 2.35 | 0.63 | -0.01 | 52397.53 | 15.96 | skipped_fast |
| FLUIDUSDT | IDLE | 1.34 | 2.7 | 0.0 | 0.07 | 3793.93 | 21.62 | skipped_fast |
| TELUSDT | IDLE | 0.8 | 1.42 | 1.17 | -0.06 | 85135.18 | 29.54 | skipped_fast |
| MNSRYUSDT | IDLE | 0.12 | 0.23 | 0.13 | -0.0 | 28351.91 | 8.5 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
