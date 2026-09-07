# Hulk DIGEST — 2026-09-07T23:38:04Z

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
| XRPUSDT | IDLE | 0.77 | 1.45 | 0.63 | -0.02 | 36487681.51 | 2.15 | skipped_fast |
| ETHUSDT | IDLE | 0.47 | 0.87 | 0.46 | -0.01 | 331485312.95 | 0.68 | skipped_fast |
| BTCUSDT | IDLE | 0.43 | 0.79 | 0.53 | -0.02 | 440194498.57 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.39 | 2.5 | 1.84 | -0.04 | 510089.35 | 1.85 | skipped_fast |
| CCUSDT | IDLE | 1.58 | 2.99 | 1.76 | -0.05 | 438259.02 | 8.58 | skipped_fast |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.56 | 9.07 | 7.65 | -0.08 | 105715.99 | 51.68 | skipped_fast |
| CHIPUSDT | IDLE | 1.61 | 6.28 | 3.23 | -0.09 | 220822.69 | 13.12 | skipped_fast |
| HBARUSDT | IDLE | 1.03 | 1.83 | 1.48 | 0.01 | 573484.44 | 1.22 | skipped_fast |
| WUSDT | IDLE | 0.98 | 1.83 | 0.93 | -0.01 | 241300.36 | 11.7 | skipped_fast |
| RWAINCUSDT | IDLE | 2.28 | 6.87 | 5.29 | -0.08 | 4654.4 | 83.16 | skipped_fast |
| ZBCNUSDT | IDLE | 0.95 | 2.52 | 1.54 | -0.04 | 218108.05 | 12.88 | skipped_fast |
| REDUSDT | IDLE | 1.29 | 2.37 | 1.37 | 0.03 | 58066.82 | 10.65 | skipped_fast |
| BIOUSDT | IDLE | 1.05 | 1.97 | 0.84 | -0.02 | 66455.24 | 7.35 | skipped_fast |
| KITEUSDT | IDLE | 1.02 | 2.03 | 0.68 | -0.06 | 61841.85 | 9.22 | skipped_fast |
| RIZEUSDT | IDLE | 1.85 | 5.58 | 2.29 | -0.02 | 55026.79 | 131.78 | skipped_fast |
| QNTUSDT | IDLE | 1.23 | 2.32 | 0.88 | -0.01 | 60257.47 | 1.51 | skipped_fast |
| TELUSDT | IDLE | 1.1 | 2.01 | 1.28 | -0.03 | 83104.9 | 47.09 | skipped_fast |
| FLUIDUSDT | IDLE | 0.7 | 1.41 | 0.0 | 0.0 | 1666.63 | 21.77 | skipped_fast |
| RWAUSDT | IDLE | 0.33 | 0.66 | 0.0 | -0.01 | 53636.53 | 14.51 | skipped_fast |
| MNSRYUSDT | IDLE | 0.41 | 0.74 | 0.52 | -0.02 | 37661.27 | 23.22 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
