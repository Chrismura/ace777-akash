# Hulk DIGEST — 2026-09-07T18:36:51Z

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
| XRPUSDT | IDLE | 1.37 | 2.55 | 1.32 | -0.01 | 36031287.81 | 1.43 | skipped_fast |
| ETHUSDT | IDLE | 0.96 | 1.79 | 0.89 | -0.0 | 344984421.56 | 0.6 | skipped_fast |
| BTCUSDT | IDLE | 0.64 | 1.18 | 0.63 | -0.01 | 457364923.87 | 0.02 | skipped_fast |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 4.12 | 11.12 | 5.55 | -0.04 | 215057.55 | 0.56 | skipped_fast |
| PYTHUSDT | IDLE | 2.81 | 5.01 | 4.03 | -0.01 | 562494.95 | 1.84 | skipped_fast |
| CCUSDT | IDLE | 2.06 | 3.69 | 2.87 | -0.03 | 439826.81 | 9.45 | skipped_fast |
| CHIPUSDT | IDLE | 2.16 | 8.22 | 5.41 | -0.09 | 237147.15 | 13.39 | skipped_fast |
| WUSDT | IDLE | 1.82 | 3.36 | 1.85 | -0.03 | 311406.1 | 19.55 | skipped_fast |
| HBARUSDT | IDLE | 1.75 | 3.34 | 1.13 | 0.02 | 583288.36 | 1.22 | skipped_fast |
| RIZEUSDT | IDLE | 2.18 | 9.74 | 8.59 | -0.09 | 69015.34 | 66.79 | skipped_fast |
| KITEUSDT | IDLE | 2.22 | 3.91 | 3.58 | -0.06 | 60276.38 | 13.49 | skipped_fast |
| REDUSDT | IDLE | 2.16 | 4.06 | 1.69 | 0.04 | 61175.33 | 10.53 | skipped_fast |
| EDELUSDT | IDLE | 1.97 | 6.26 | 4.73 | -0.06 | 91164.11 | 40.57 | skipped_fast |
| BIOUSDT | IDLE | 1.83 | 3.39 | 1.8 | -0.01 | 69102.43 | 7.34 | skipped_fast |
| RWAINCUSDT | IDLE | 1.36 | 4.06 | 3.85 | 0.04 | 4993.37 | 44.46 | skipped_fast |
| MNSRYUSDT | IDLE | 2.73 | 5.29 | 1.16 | -0.02 | 37281.53 | 61.29 | skipped_fast |
| TELUSDT | IDLE | 1.02 | 1.89 | 1.04 | -0.01 | 114586.91 | 41.04 | skipped_fast |
| QNTUSDT | IDLE | 0.9 | 1.6 | 1.29 | -0.0 | 46623.56 | 6.09 | skipped_fast |
| RWAUSDT | IDLE | 0.53 | 0.95 | 0.72 | -0.01 | 52956.94 | 21.79 | skipped_fast |
| FLUIDUSDT | IDLE | 0.07 | 0.14 | 0.0 | 0.0 | 1172.4 | 21.86 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
