# Hulk DIGEST — 2026-10-26T18:26:52Z

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
| ETHUSDT | IDLE | 1.12 | 2.11 | 0.85 | -0.01 | 141540227.58 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 1.05 | 2.01 | 0.58 | -0.0 | 24376242.4 | 1.54 | skipped_fast |
| BTCUSDT | IDLE | 0.9 | 1.69 | 0.73 | -0.01 | 346820871.6 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.85 | 7.77 | 6.53 | 0.06 | 1432260.93 | 5.86 | skipped_fast |
| PYTHUSDT | IDLE | 2.1 | 3.76 | 2.92 | 0.01 | 928192.94 | 2.68 | skipped_fast |
| WUSDT | IDLE | 3.22 | 6.6 | 1.7 | 0.02 | 595650.0 | 74.19 | skipped_fast |
| CHIPUSDT | IDLE | 2.27 | 18.78 | 2.21 | 0.23 | 303476.03 | 23.38 | skipped_fast |
| RWAINCUSDT | IDLE | 3.0 | 13.37 | 3.28 | -0.07 | 61133.91 | 5.95 | skipped_fast |
| EDELUSDT | IDLE | 2.4 | 4.44 | 2.38 | 0.03 | 104648.34 | 43.3 | skipped_fast |
| RIZEUSDT | IDLE | 2.31 | 4.4 | 1.44 | 0.0 | 28859.36 | 50.86 | skipped_fast |
| BIOUSDT | IDLE | 1.78 | 3.28 | 1.85 | -0.01 | 59780.84 | 8.99 | skipped_fast |
| CCUSDT | IDLE | 1.18 | 2.11 | 1.72 | -0.03 | 195646.13 | 8.02 | skipped_fast |
| ZBCNUSDT | IDLE | 1.26 | 2.46 | 2.14 | -0.06 | 197092.69 | 22.28 | skipped_fast |
| REDUSDT | IDLE | 1.64 | 2.98 | 1.96 | 0.0 | 63162.11 | 16.41 | skipped_fast |
| KITEUSDT | IDLE | 1.21 | 2.22 | 1.37 | 0.01 | 53879.98 | 11.47 | skipped_fast |
| HBARUSDT | IDLE | 1.09 | 1.97 | 1.42 | -0.01 | 249686.2 | 9.1 | skipped_fast |
| WAXLUSDT | IDLE | 2.16 | 4.01 | 2.01 | -0.01 | 53850.12 | 41.42 | skipped_fast |
| LAUSDT | IDLE | 1.73 | 3.41 | 2.44 | 0.0 | 65624.32 | 18.95 | skipped_fast |
| IOTAUSDT | IDLE | 1.39 | 2.44 | 2.22 | -0.02 | 84482.5 | 26.0 | skipped_fast |
| FLUIDUSDT | IDLE | 1.31 | 2.35 | 2.0 | -0.05 | 1378.64 | 21.28 | skipped_fast |
| RWAUSDT | IDLE | 0.75 | 1.44 | 0.4 | 0.0 | 54146.38 | 15.89 | skipped_fast |
| MNSRYUSDT | IDLE | 0.41 | 0.74 | 0.59 | -0.01 | 42409.06 | 76.46 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
