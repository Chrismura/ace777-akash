# Hulk DIGEST — 2026-10-21T03:06:07Z

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
| XRPUSDT | IDLE | 0.54 | 0.96 | 0.78 | 0.02 | 24217032.88 | 0.75 | skipped_fast |
| ETHUSDT | IDLE | 0.51 | 0.91 | 0.67 | 0.02 | 171421079.06 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.33 | 0.59 | 0.46 | 0.01 | 326518289.13 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 0.91 | 2.73 | 2.16 | 0.09 | 957079.57 | 2.51 | skipped_fast |
| WUSDT | IDLE | 1.35 | 2.58 | 0.82 | 0.03 | 645074.9 | 16.3 | skipped_fast |
| QNTUSDT | IDLE | 1.27 | 2.46 | 0.56 | 0.01 | 811671.93 | 1.52 | skipped_fast |
| RWAINCUSDT | IDLE | 2.37 | 10.7 | 9.67 | -0.1 | 80616.33 | 5.73 | skipped_fast |
| ZBCNUSDT | IDLE | 2.43 | 4.82 | 0.27 | 0.05 | 193644.24 | 23.5 | skipped_fast |
| CHIPUSDT | IDLE | 1.04 | 2.54 | 2.35 | 0.04 | 446262.26 | 6.81 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.37 | 12.41 | 10.79 | 0.04 | 17676.55 | 21.49 | skipped_fast |
| CCUSDT | IDLE | 0.94 | 1.76 | 0.78 | -0.01 | 366507.78 | 8.52 | skipped_fast |
| EDELUSDT | IDLE | 0.4 | 2.82 | 0.33 | 0.29 | 367804.97 | 19.22 | skipped_fast |
| REDUSDT | IDLE | 1.16 | 2.31 | 0.11 | 0.04 | 57900.86 | 12.58 | skipped_fast |
| HBARUSDT | IDLE | 0.78 | 1.37 | 1.2 | 0.0 | 343876.86 | 4.79 | skipped_fast |
| BIOUSDT | IDLE | 0.7 | 1.31 | 0.65 | 0.04 | 61042.73 | 8.12 | skipped_fast |
| KITEUSDT | IDLE | 0.57 | 1.07 | 0.46 | -0.01 | 73808.98 | 12.31 | skipped_fast |
| LAUSDT | IDLE | 1.93 | 4.92 | 0.14 | 0.07 | 55497.1 | 24.71 | skipped_fast |
| RIZEUSDT | IDLE | 0.76 | 3.01 | 2.22 | 0.05 | 61140.57 | 62.42 | skipped_fast |
| WAXLUSDT | IDLE | 1.75 | 3.28 | 1.48 | -0.03 | 57611.33 | 31.83 | skipped_fast |
| IOTAUSDT | IDLE | 0.73 | 1.3 | 1.02 | 0.02 | 75193.7 | 32.36 | skipped_fast |
| RWAUSDT | IDLE | 0.35 | 0.63 | 0.47 | 0.0 | 53331.12 | 23.52 | skipped_fast |
| MNSRYUSDT | IDLE | 0.19 | 0.37 | 0.04 | -0.0 | 40223.96 | 11.4 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
