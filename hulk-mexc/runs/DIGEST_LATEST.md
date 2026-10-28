# Hulk DIGEST — 2026-10-28T00:19:51Z

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
| XRPUSDT | IDLE | 0.67 | 1.27 | 0.46 | 0.01 | 19283623.02 | 0.75 | skipped_fast |
| ETHUSDT | IDLE | 0.57 | 1.03 | 0.75 | 0.01 | 237919630.4 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.46 | 0.82 | 0.63 | 0.01 | 323134014.45 | 0.0 | skipped_fast |
| EDELUSDT | IDLE | 2.06 | 3.95 | 1.2 | 0.02 | 460164.62 | 24.22 | skipped_fast |
| WUSDT | IDLE | 0.93 | 2.09 | 1.2 | 0.03 | 689535.07 | 17.96 | skipped_fast |
| ZBCNUSDT | IDLE | 2.12 | 7.31 | 5.72 | -0.02 | 242086.25 | 38.94 | skipped_fast |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 4.03 | 11.59 | 9.97 | -0.01 | 7615.83 | 20.41 | skipped_fast |
| QNTUSDT | IDLE | 1.22 | 2.18 | 1.71 | -0.01 | 677952.84 | 0.5 | skipped_fast |
| PYTHUSDT | IDLE | 1.08 | 2.03 | 0.92 | -0.02 | 395118.02 | 5.45 | skipped_fast |
| RWAINCUSDT | IDLE | 1.68 | 3.57 | 2.93 | -0.04 | 58544.48 | 13.37 | skipped_fast |
| CHIPUSDT | IDLE | 1.27 | 3.09 | 1.45 | 0.06 | 131997.09 | 20.22 | skipped_fast |
| CCUSDT | IDLE | 0.78 | 1.5 | 0.44 | -0.01 | 225974.57 | 8.08 | skipped_fast |
| REDUSDT | IDLE | 0.99 | 1.98 | 1.57 | 0.04 | 59891.89 | 7.12 | skipped_fast |
| KITEUSDT | IDLE | 1.02 | 1.83 | 1.71 | 0.03 | 58217.94 | 11.91 | skipped_fast |
| BIOUSDT | IDLE | 0.86 | 1.6 | 0.83 | 0.02 | 58871.94 | 8.84 | skipped_fast |
| HBARUSDT | IDLE | 0.74 | 1.31 | 1.07 | -0.02 | 310086.84 | 14.5 | skipped_fast |
| RIZEUSDT | IDLE | 0.64 | 1.24 | 0.32 | 0.0 | 33573.75 | 64.68 | skipped_fast |
| LAUSDT | IDLE | 1.22 | 2.33 | 2.09 | 0.02 | 60021.87 | 25.06 | skipped_fast |
| IOTAUSDT | IDLE | 0.96 | 1.89 | 0.23 | -0.01 | 79227.83 | 25.91 | skipped_fast |
| WAXLUSDT | IDLE | 0.78 | 1.46 | 0.65 | 0.03 | 57159.82 | 36.7 | skipped_fast |
| RWAUSDT | IDLE | 0.41 | 0.72 | 0.72 | -0.0 | 57431.11 | 32.08 | skipped_fast |
| MNSRYUSDT | IDLE | 0.43 | 0.8 | 0.44 | -0.0 | 37105.53 | 79.41 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
