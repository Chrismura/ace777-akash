# Hulk DIGEST — 2026-10-20T20:24:08Z

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
| XRPUSDT | IDLE | 1.4 | 2.63 | 1.18 | 0.02 | 23829271.09 | 0.75 | skipped_fast |
| ETHUSDT | IDLE | 1.08 | 1.94 | 1.46 | 0.01 | 148679456.21 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.72 | 1.32 | 0.84 | 0.01 | 318952146.06 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.42 | 6.77 | 1.08 | 0.09 | 1128104.61 | 3.79 | skipped_fast |
| WUSDT | IDLE | 2.32 | 4.43 | 1.43 | 0.01 | 664687.01 | 15.84 | skipped_fast |
| QNTUSDT | IDLE | 2.7 | 4.78 | 4.1 | -0.01 | 781207.73 | 3.1 | skipped_fast |
| EDELUSDT | IDLE | 1.11 | 10.16 | 4.1 | 0.3 | 362204.44 | 19.99 | skipped_fast |
| CHIPUSDT | IDLE | 1.65 | 5.69 | 3.84 | 0.06 | 289191.75 | 24.66 | skipped_fast |
| ZBCNUSDT | IDLE | 2.23 | 4.0 | 3.12 | 0.02 | 189797.98 | 21.28 | skipped_fast |
| CCUSDT | IDLE | 1.19 | 2.1 | 1.82 | 0.01 | 382439.3 | 9.54 | skipped_fast |
| HBARUSDT | IDLE | 1.98 | 3.58 | 2.53 | 0.01 | 370406.31 | 5.99 | skipped_fast |
| REDUSDT | IDLE | 1.79 | 3.3 | 1.86 | 0.02 | 59796.18 | 7.88 | skipped_fast |
| BIOUSDT | IDLE | 1.61 | 2.97 | 1.64 | 0.04 | 62935.15 | 8.14 | skipped_fast |
| KITEUSDT | IDLE | 1.27 | 2.23 | 2.04 | 0.0 | 82554.51 | 10.68 | skipped_fast |
| RWAINCUSDT | IDLE | 1.13 | 3.73 | 0.99 | -0.02 | 67416.56 | 5.26 | skipped_fast |
| IOTAUSDT | IDLE | 2.3 | 4.14 | 3.04 | 0.04 | 72523.33 | 30.01 | skipped_fast |
| RIZEUSDT | IDLE | 1.12 | 4.88 | 0.18 | 0.04 | 69228.18 | 59.43 | skipped_fast |
| WAXLUSDT | IDLE | 2.2 | 3.85 | 3.62 | -0.05 | 56120.79 | 26.29 | skipped_fast |
| LAUSDT | IDLE | 1.38 | 2.57 | 1.25 | 0.02 | 56273.96 | 18.64 | skipped_fast |
| FLUIDUSDT | IDLE | 1.25 | 2.5 | 0.0 | 0.07 | 6257.9 | 21.14 | skipped_fast |
| RWAUSDT | IDLE | 0.42 | 0.79 | 0.31 | 0.0 | 52359.93 | 7.84 | skipped_fast |
| MNSRYUSDT | IDLE | 0.4 | 0.74 | 0.4 | 0.0 | 40133.35 | 22.8 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
