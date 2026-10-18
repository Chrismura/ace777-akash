# Hulk DIGEST — 2026-10-18T14:02:27Z

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
| PYTHUSDT | IDLE | 2.33 | 6.87 | 6.43 | -0.12 | 1482997.33 | 2.67 | skipped_fast |
| XRPUSDT | IDLE | 1.19 | 2.12 | 1.68 | -0.01 | 21027892.79 | 1.56 | skipped_fast |
| ETHUSDT | IDLE | 1.05 | 1.89 | 1.36 | -0.01 | 89849740.87 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.65 | 1.17 | 0.92 | 0.0 | 209237455.51 | 0.0 | skipped_fast |
| WUSDT | IDLE | 2.05 | 4.09 | 3.93 | -0.07 | 969484.69 | 13.02 | skipped_fast |
| WAXLUSDT | WATCH_PULLBACK — tension haute + reflux | 4.52 | 15.8 | 13.64 | -0.01 | 72505.48 | 20.02 | skipped_fast |
| RWAINCUSDT | IDLE | 3.09 | 6.37 | 4.55 | 0.03 | 21018.43 | 5.19 | skipped_fast |
| HBARUSDT | IDLE | 1.68 | 3.54 | 2.43 | 0.06 | 593370.5 | 10.28 | skipped_fast |
| QNTUSDT | IDLE | 1.84 | 3.29 | 2.58 | -0.04 | 495252.12 | 6.18 | skipped_fast |
| RIZEUSDT | IDLE | 2.81 | 5.3 | 2.15 | 0.03 | 47605.37 | 57.65 | skipped_fast |
| CHIPUSDT | IDLE | 2.04 | 3.81 | 3.62 | -0.08 | 69707.31 | 12.13 | skipped_fast |
| EDELUSDT | IDLE | 1.26 | 3.33 | 1.33 | -0.08 | 228125.57 | 15.02 | skipped_fast |
| REDUSDT | IDLE | 1.83 | 3.19 | 3.09 | -0.03 | 77611.29 | 8.08 | skipped_fast |
| CCUSDT | IDLE | 0.96 | 1.73 | 1.29 | -0.03 | 253002.53 | 7.98 | skipped_fast |
| BIOUSDT | IDLE | 1.57 | 2.78 | 2.45 | -0.04 | 82362.69 | 4.27 | skipped_fast |
| KITEUSDT | IDLE | 1.34 | 2.33 | 2.28 | -0.05 | 68071.89 | 11.49 | skipped_fast |
| ZBCNUSDT | IDLE | 0.62 | 1.15 | 0.58 | -0.02 | 176244.18 | 17.64 | skipped_fast |
| LAUSDT | IDLE | 2.02 | 3.54 | 3.31 | -0.07 | 54598.29 | 19.06 | skipped_fast |
| IOTAUSDT | IDLE | 2.08 | 3.64 | 3.4 | -0.05 | 68707.03 | 47.42 | skipped_fast |
| FLUIDUSDT | IDLE | 1.97 | 3.44 | 3.33 | -0.02 | 2526.38 | 21.21 | skipped_fast |
| MNSRYUSDT | IDLE | 0.35 | 0.69 | 0.13 | -0.0 | 34335.65 | 12.78 | skipped_fast |
| RWAUSDT | IDLE | 0.25 | 0.48 | 0.16 | 0.0 | 50310.42 | 15.9 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
