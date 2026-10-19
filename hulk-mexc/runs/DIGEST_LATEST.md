# Hulk DIGEST — 2026-10-19T07:54:59Z

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
| ETHUSDT | IDLE | 0.63 | 1.18 | 0.55 | 0.01 | 137876898.88 | 0.45 | skipped_fast |
| XRPUSDT | IDLE | 0.62 | 1.16 | 0.51 | 0.02 | 31453550.83 | 1.52 | skipped_fast |
| BTCUSDT | IDLE | 0.52 | 0.96 | 0.49 | 0.01 | 312995980.93 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.09 | 3.02 | 1.66 | -0.03 | 1015961.88 | 3.99 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.19 | 11.35 | 5.26 | 0.02 | 312939.82 | 16.39 | skipped_fast |
| WUSDT | IDLE | 1.57 | 2.83 | 2.64 | -0.04 | 520764.13 | 17.11 | skipped_fast |
| QNTUSDT | IDLE | 1.99 | 5.46 | 0.7 | 0.03 | 676334.34 | 2.99 | skipped_fast |
| EDELUSDT | IDLE | 2.56 | 5.3 | 2.52 | 0.02 | 236136.63 | 7.31 | skipped_fast |
| HBARUSDT | IDLE | 0.71 | 1.69 | 0.76 | -0.03 | 833729.69 | 5.91 | skipped_fast |
| RWAINCUSDT | IDLE | 1.69 | 5.06 | 2.49 | -0.02 | 76998.8 | 5.31 | skipped_fast |
| CCUSDT | IDLE | 0.82 | 1.61 | 0.2 | 0.01 | 300291.84 | 5.82 | skipped_fast |
| CHIPUSDT | IDLE | 1.12 | 3.04 | 1.25 | 0.0 | 78471.86 | 9.34 | skipped_fast |
| BIOUSDT | IDLE | 1.03 | 1.92 | 0.88 | -0.0 | 85366.93 | 4.21 | skipped_fast |
| REDUSDT | IDLE | 1.07 | 1.93 | 1.4 | -0.0 | 94178.91 | 17.49 | skipped_fast |
| KITEUSDT | IDLE | 1.03 | 1.83 | 1.54 | 0.01 | 65513.15 | 9.58 | skipped_fast |
| FLUIDUSDT | IDLE | 2.24 | 6.06 | 1.9 | 0.01 | 7630.81 | 21.21 | skipped_fast |
| RIZEUSDT | IDLE | 0.33 | 1.74 | 0.8 | -0.03 | 58670.08 | 45.78 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 1.91 | 1.64 | 0.0 | 54276.04 | 7.95 | skipped_fast |
| LAUSDT | IDLE | 0.93 | 1.79 | 0.43 | -0.02 | 57704.67 | 20.66 | skipped_fast |
| IOTAUSDT | IDLE | 0.96 | 1.84 | 0.53 | -0.01 | 65208.77 | 31.07 | skipped_fast |
| WAXLUSDT | IDLE | 0.65 | 3.02 | 1.19 | -0.01 | 85671.35 | 69.01 | skipped_fast |
| MNSRYUSDT | IDLE | 0.27 | 0.53 | 0.11 | -0.0 | 38848.86 | 15.66 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
