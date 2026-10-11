# Hulk DIGEST — 2026-10-11T22:26:06Z

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
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 3.05 | 27.54 | 6.37 | 0.24 | 4322886.2 | 8.24 | skipped_fast |
| XRPUSDT | IDLE | 1.0 | 1.84 | 1.05 | 0.0 | 15840252.0 | 1.42 | skipped_fast |
| ETHUSDT | IDLE | 0.79 | 1.47 | 0.72 | 0.01 | 214484500.14 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.58 | 1.07 | 0.63 | 0.01 | 156471393.44 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.35 | 4.34 | 2.37 | -0.01 | 912710.82 | 2.56 | skipped_fast |
| QNTUSDT | IDLE | 2.16 | 3.86 | 3.05 | -0.0 | 774347.05 | 5.88 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.01 | 18.15 | 12.66 | 0.01 | 39877.0 | 55.84 | skipped_fast |
| ZBCNUSDT | IDLE | 2.7 | 4.73 | 4.42 | -0.01 | 209652.0 | 8.76 | skipped_fast |
| EDELUSDT | IDLE | 1.6 | 2.88 | 2.13 | -0.02 | 384382.66 | 13.24 | skipped_fast |
| CCUSDT | IDLE | 1.66 | 3.32 | 2.06 | 0.05 | 353196.13 | 7.98 | skipped_fast |
| CHIPUSDT | IDLE | 1.07 | 4.13 | 3.12 | 0.0 | 285282.42 | 13.3 | skipped_fast |
| BIOUSDT | IDLE | 1.37 | 2.54 | 1.32 | 0.02 | 96183.59 | 3.35 | skipped_fast |
| TELUSDT | IDLE | 2.47 | 4.51 | 2.84 | -0.04 | 175823.9 | 40.92 | skipped_fast |
| RWAINCUSDT | IDLE | 1.23 | 3.21 | 3.01 | -0.01 | 28720.92 | 19.69 | skipped_fast |
| KITEUSDT | IDLE | 0.97 | 1.83 | 0.69 | -0.0 | 75925.39 | 10.95 | skipped_fast |
| HBARUSDT | IDLE | 1.15 | 2.13 | 1.11 | 0.01 | 302582.8 | 5.34 | skipped_fast |
| REDUSDT | IDLE | 0.92 | 1.63 | 1.4 | 0.0 | 57294.22 | 15.87 | skipped_fast |
| RWAUSDT | IDLE | 1.43 | 2.57 | 1.97 | 0.02 | 53086.24 | 15.49 | skipped_fast |
| MNSRYUSDT | IDLE | 0.69 | 1.24 | 0.92 | -0.0 | 33519.19 | 12.31 | skipped_fast |
| FLUIDUSDT | IDLE | 0.34 | 2.51 | 1.35 | 0.06 | 61764.44 | 20.38 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
