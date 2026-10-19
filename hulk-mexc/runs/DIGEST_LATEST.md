# Hulk DIGEST — 2026-10-19T17:01:53Z

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
| ETHUSDT | IDLE | 1.0 | 1.83 | 1.1 | 0.01 | 158215105.57 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.91 | 1.67 | 0.99 | 0.02 | 27998455.88 | 0.77 | skipped_fast |
| BTCUSDT | IDLE | 0.67 | 1.2 | 0.88 | 0.01 | 358371220.86 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.17 | 4.17 | 1.08 | -0.02 | 944548.89 | 2.7 | skipped_fast |
| WUSDT | IDLE | 2.83 | 5.38 | 1.84 | 0.01 | 552680.35 | 14.51 | skipped_fast |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.16 | 10.75 | 5.0 | -0.08 | 53950.45 | 27.76 | skipped_fast |
| QNTUSDT | IDLE | 1.05 | 3.0 | 1.98 | 0.03 | 840493.02 | 1.53 | skipped_fast |
| RWAINCUSDT | IDLE | 2.88 | 6.71 | 2.15 | 0.04 | 82048.15 | 5.1 | skipped_fast |
| CCUSDT | IDLE | 1.45 | 3.34 | 1.82 | 0.05 | 399304.8 | 7.67 | skipped_fast |
| HBARUSDT | IDLE | 1.49 | 2.72 | 1.68 | -0.04 | 557696.82 | 3.63 | skipped_fast |
| KITEUSDT | IDLE | 2.16 | 6.16 | 2.07 | 0.07 | 64122.89 | 7.4 | skipped_fast |
| EDELUSDT | IDLE | 1.36 | 2.86 | 1.13 | 0.03 | 227366.66 | 22.25 | skipped_fast |
| CHIPUSDT | IDLE | 1.55 | 4.38 | 0.73 | 0.04 | 77895.5 | 9.55 | skipped_fast |
| ZBCNUSDT | IDLE | 0.66 | 2.26 | 1.62 | 0.04 | 261569.32 | 16.11 | skipped_fast |
| REDUSDT | IDLE | 1.48 | 2.81 | 1.0 | 0.02 | 58947.91 | 15.95 | skipped_fast |
| BIOUSDT | IDLE | 1.09 | 2.07 | 0.76 | 0.01 | 70439.49 | 4.25 | skipped_fast |
| WAXLUSDT | IDLE | 1.26 | 3.69 | 3.49 | 0.03 | 78333.04 | 23.08 | skipped_fast |
| LAUSDT | IDLE | 1.48 | 2.71 | 1.67 | 0.02 | 56106.46 | 20.97 | skipped_fast |
| IOTAUSDT | IDLE | 1.02 | 1.95 | 0.56 | 0.01 | 75645.11 | 24.59 | skipped_fast |
| FLUIDUSDT | IDLE | 0.83 | 2.04 | 2.0 | 0.01 | 5787.49 | 17.91 | skipped_fast |
| RWAUSDT | IDLE | 0.59 | 1.11 | 0.47 | 0.01 | 55007.65 | 15.77 | skipped_fast |
| MNSRYUSDT | IDLE | 0.27 | 0.5 | 0.26 | -0.0 | 40269.51 | 31.36 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
