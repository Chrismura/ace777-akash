# Hulk DIGEST — 2026-09-26T20:03:36Z

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
| XRPUSDT | IDLE | 1.33 | 2.35 | 2.03 | -0.03 | 39659458.83 | 0.66 | skipped_fast |
| ETHUSDT | IDLE | 0.29 | 0.51 | 0.43 | -0.0 | 110853348.63 | 0.22 | skipped_fast |
| QNTUSDT | IDLE | 1.95 | 13.91 | 2.0 | 0.26 | 1437579.44 | 10.59 | skipped_fast |
| BTCUSDT | IDLE | 0.13 | 0.24 | 0.19 | 0.0 | 333811992.07 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.28 | 6.03 | 1.01 | 0.1 | 1047400.35 | 2.51 | skipped_fast |
| CCUSDT | IDLE | 2.11 | 5.3 | 4.18 | 0.03 | 864353.17 | 11.16 | skipped_fast |
| WUSDT | IDLE | 1.77 | 3.9 | 1.77 | 0.08 | 561908.36 | 17.69 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.38 | 6.42 | 5.38 | 0.01 | 113588.29 | 18.21 | skipped_fast |
| RWAINCUSDT | IDLE | 3.77 | 13.77 | 3.46 | 0.05 | 9773.82 | 77.18 | skipped_fast |
| KITEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.7 | 9.74 | 0.83 | 0.12 | 110435.26 | 8.69 | skipped_fast |
| ZBCNUSDT | IDLE | 2.23 | 3.93 | 3.51 | -0.04 | 200714.75 | 23.75 | skipped_fast |
| EDELUSDT | IDLE | 2.36 | 4.21 | 3.43 | 0.02 | 169150.22 | 39.8 | skipped_fast |
| HBARUSDT | IDLE | 1.28 | 2.24 | 2.18 | -0.01 | 551142.83 | 1.07 | skipped_fast |
| BIOUSDT | IDLE | 1.64 | 2.87 | 2.67 | -0.03 | 108733.73 | 6.21 | skipped_fast |
| REDUSDT | IDLE | 0.9 | 1.58 | 1.4 | -0.03 | 57973.38 | 7.71 | skipped_fast |
| RIZEUSDT | IDLE | 1.19 | 2.9 | 1.45 | 0.06 | 48546.71 | 47.19 | skipped_fast |
| TELUSDT | IDLE | 1.76 | 3.41 | 0.79 | -0.02 | 127063.8 | 49.2 | skipped_fast |
| RWAUSDT | IDLE | 0.67 | 1.23 | 0.71 | 0.03 | 56526.79 | 7.17 | skipped_fast |
| MNSRYUSDT | IDLE | 0.26 | 0.51 | 0.1 | -0.01 | 38980.91 | 16.57 | skipped_fast |
| FLUIDUSDT | IDLE | 0.27 | 0.49 | 0.28 | 0.01 | 539.62 | 19.5 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
