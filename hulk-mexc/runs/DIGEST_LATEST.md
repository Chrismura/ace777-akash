# Hulk DIGEST — 2026-10-26T01:12:01Z

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
| ETHUSDT | IDLE | 1.0 | 1.81 | 1.24 | -0.01 | 91341017.79 | 1.03 | skipped_fast |
| XRPUSDT | IDLE | 0.72 | 1.32 | 0.84 | -0.01 | 14997954.52 | 0.77 | skipped_fast |
| BTCUSDT | IDLE | 0.6 | 1.09 | 0.79 | -0.01 | 163002035.54 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.78 | 3.28 | 1.91 | -0.03 | 604739.99 | 17.74 | skipped_fast |
| PYTHUSDT | IDLE | 1.22 | 2.64 | 1.58 | 0.06 | 674809.32 | 1.34 | skipped_fast |
| QNTUSDT | IDLE | 1.49 | 4.02 | 3.68 | 0.04 | 671062.64 | 7.42 | skipped_fast |
| ZBCNUSDT | IDLE | 2.19 | 3.89 | 3.69 | 0.02 | 184386.01 | 24.64 | skipped_fast |
| CHIPUSDT | IDLE | 2.49 | 4.35 | 4.17 | -0.03 | 87338.4 | 13.8 | skipped_fast |
| EDELUSDT | IDLE | 1.14 | 2.75 | 1.93 | 0.04 | 278681.01 | 22.16 | skipped_fast |
| RWAINCUSDT | IDLE | 1.91 | 3.49 | 2.16 | -0.04 | 62716.08 | 5.66 | skipped_fast |
| CCUSDT | IDLE | 1.27 | 2.33 | 1.46 | -0.0 | 188136.86 | 9.91 | skipped_fast |
| REDUSDT | IDLE | 1.23 | 2.25 | 1.39 | -0.03 | 59671.54 | 7.61 | skipped_fast |
| KITEUSDT | IDLE | 1.12 | 2.1 | 0.87 | -0.03 | 54010.01 | 11.51 | skipped_fast |
| BIOUSDT | IDLE | 1.02 | 1.91 | 0.89 | -0.03 | 59525.19 | 4.5 | skipped_fast |
| RIZEUSDT | IDLE | 1.35 | 2.71 | 0.0 | 0.01 | 33092.23 | 59.87 | skipped_fast |
| LAUSDT | IDLE | 1.33 | 3.15 | 1.09 | -0.04 | 65966.98 | 21.15 | skipped_fast |
| HBARUSDT | IDLE | 0.87 | 1.63 | 0.73 | -0.01 | 151444.85 | 6.46 | skipped_fast |
| FLUIDUSDT | IDLE | 1.13 | 5.2 | 4.94 | -0.02 | 19001.78 | 21.09 | skipped_fast |
| IOTAUSDT | IDLE | 1.16 | 2.12 | 1.39 | -0.02 | 60088.86 | 32.82 | skipped_fast |
| WAXLUSDT | IDLE | 1.09 | 2.09 | 0.55 | 0.02 | 53738.1 | 42.73 | skipped_fast |
| RWAUSDT | IDLE | 0.13 | 0.24 | 0.08 | 0.0 | 52483.22 | 7.96 | skipped_fast |
| MNSRYUSDT | IDLE | 0.33 | 0.59 | 0.53 | -0.01 | 38335.25 | 60.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
