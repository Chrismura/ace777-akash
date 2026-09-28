# Hulk DIGEST — 2026-09-28T02:37:13Z

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
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 2.75 | 90.56 | 27.1 | 0.55 | 14826581.04 | 9.17 | skipped_fast |
| WUSDT | IDLE | 2.16 | 9.22 | 6.49 | 0.12 | 5293688.68 | 9.32 | skipped_fast |
| PYTHUSDT | IDLE | 1.46 | 3.33 | 1.4 | 0.01 | 2013923.82 | 8.36 | skipped_fast |
| XRPUSDT | IDLE | 1.49 | 2.64 | 2.24 | -0.02 | 47320156.96 | 4.67 | skipped_fast |
| ETHUSDT | IDLE | 1.12 | 1.96 | 1.83 | -0.02 | 243895225.92 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 1.02 | 1.79 | 1.66 | -0.01 | 470787012.97 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 2.46 | 4.83 | 0.66 | 0.03 | 684980.18 | 9.25 | skipped_fast |
| HBARUSDT | IDLE | 2.34 | 4.38 | 2.01 | 0.03 | 943414.79 | 6.27 | skipped_fast |
| KITEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.44 | 6.04 | 5.6 | -0.06 | 100171.36 | 8.92 | skipped_fast |
| EDELUSDT | IDLE | 2.07 | 10.77 | 8.79 | -0.15 | 154009.29 | 32.6 | skipped_fast |
| BIOUSDT | IDLE | 2.68 | 4.72 | 4.23 | -0.03 | 85742.5 | 3.22 | skipped_fast |
| ZBCNUSDT | IDLE | 2.19 | 3.83 | 3.65 | -0.03 | 247444.32 | 30.99 | skipped_fast |
| RIZEUSDT | IDLE | 1.41 | 13.55 | 7.05 | -0.22 | 65237.44 | 36.62 | skipped_fast |
| CHIPUSDT | IDLE | 1.86 | 4.01 | 3.47 | -0.07 | 94884.85 | 15.35 | skipped_fast |
| REDUSDT | IDLE | 1.58 | 2.78 | 2.48 | -0.01 | 66647.02 | 14.35 | skipped_fast |
| RWAINCUSDT | IDLE | 0.69 | 6.69 | 4.19 | 0.21 | 31089.26 | 52.14 | skipped_fast |
| TELUSDT | IDLE | 1.18 | 2.8 | 0.96 | 0.04 | 174030.0 | 32.36 | skipped_fast |
| FLUIDUSDT | IDLE | 1.89 | 3.39 | 2.65 | 0.03 | 3556.81 | 48.91 | skipped_fast |
| RWAUSDT | IDLE | 0.68 | 1.22 | 0.92 | 0.0 | 59732.55 | 42.8 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.69 | 0.42 | 0.01 | 39733.81 | 45.66 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
