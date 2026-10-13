# Hulk DIGEST — 2026-10-13T13:01:36Z

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
| WUSDT | IDLE | 1.1 | 10.93 | 7.7 | -0.27 | 6459031.69 | 5.37 | skipped_fast |
| PYTHUSDT | IDLE | 1.33 | 4.44 | 3.38 | -0.07 | 2605834.5 | 4.83 | skipped_fast |
| XRPUSDT | IDLE | 1.32 | 2.44 | 1.31 | -0.02 | 38794142.96 | 1.47 | skipped_fast |
| ETHUSDT | IDLE | 1.07 | 1.94 | 1.3 | -0.01 | 239688368.68 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.69 | 1.23 | 1.0 | 0.01 | 388569631.05 | 0.0 | skipped_fast |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 3.85 | 13.38 | 9.92 | -0.11 | 1075082.85 | 2.92 | skipped_fast |
| CCUSDT | IDLE | 2.91 | 8.95 | 4.06 | 0.01 | 532512.78 | 8.73 | skipped_fast |
| EDELUSDT | IDLE | 2.15 | 6.69 | 0.86 | -0.06 | 311280.52 | 20.28 | skipped_fast |
| RWAINCUSDT | IDLE | 3.02 | 5.4 | 4.32 | -0.02 | 32286.97 | 19.86 | skipped_fast |
| ZBCNUSDT | IDLE | 2.29 | 4.13 | 3.04 | -0.04 | 233796.31 | 42.13 | skipped_fast |
| REDUSDT | IDLE | 1.72 | 6.14 | 3.67 | -0.06 | 207251.36 | 10.42 | skipped_fast |
| HBARUSDT | IDLE | 1.61 | 3.54 | 1.73 | -0.05 | 548904.48 | 10.32 | skipped_fast |
| CHIPUSDT | IDLE | 1.85 | 5.0 | 2.75 | -0.06 | 130662.9 | 11.94 | skipped_fast |
| RIZEUSDT | IDLE | 1.99 | 10.38 | 3.21 | -0.09 | 65083.39 | 64.03 | skipped_fast |
| BIOUSDT | IDLE | 1.46 | 4.03 | 2.1 | -0.06 | 73764.21 | 7.27 | skipped_fast |
| KITEUSDT | IDLE | 1.49 | 3.07 | 1.62 | -0.01 | 64937.13 | 10.26 | skipped_fast |
| FLUIDUSDT | IDLE | 1.82 | 3.6 | 3.44 | 0.02 | 14619.35 | 21.08 | skipped_fast |
| TELUSDT | IDLE | 1.15 | 2.08 | 1.42 | -0.02 | 105549.5 | 23.01 | skipped_fast |
| RWAUSDT | IDLE | 0.22 | 0.39 | 0.31 | 0.0 | 53557.02 | 15.44 | skipped_fast |
| MNSRYUSDT | IDLE | 0.29 | 0.53 | 0.39 | -0.02 | 38284.07 | 26.37 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
