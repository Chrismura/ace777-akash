# Hulk DIGEST — 2026-08-22T11:53:41Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 2.17 | 9.66 | 7.07 | 0.01 | 51611931.63 | 2.06 | skipped_fast |
| XRPUSDT | IDLE | 2.34 | 14.26 | 8.84 | 0.09 | 216293282.96 | 2.7 | skipped_fast |
| CCUSDT | IDLE | 2.02 | 10.24 | 6.66 | 0.13 | 784674.49 | 9.42 | skipped_fast |
| HBARUSDT | IDLE | 1.46 | 5.26 | 3.42 | 0.02 | 1255238.82 | 5.18 | skipped_fast |
| WUSDT | IDLE | 1.56 | 6.27 | 3.82 | 0.02 | 581824.05 | 11.66 | skipped_fast |
| ZBCNUSDT | IDLE | 2.28 | 5.93 | 4.05 | -0.03 | 385048.33 | 17.47 | skipped_fast |
| CHIPUSDT | IDLE | 0.71 | 4.16 | 1.22 | -0.1 | 618173.94 | 3.34 | skipped_fast |
| EDELUSDT | IDLE | 2.78 | 4.93 | 4.15 | -0.04 | 79308.74 | 11.38 | skipped_fast |
| KITEUSDT | IDLE | 2.59 | 6.24 | 0.18 | 0.05 | 81584.83 | 13.22 | skipped_fast |
| BIOUSDT | IDLE | 0.93 | 6.64 | 2.42 | -0.04 | 241325.8 | 3.22 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.65 | 6.75 | 5.51 | -0.03 | 167320.73 | 5.35 | skipped_fast |
| QAITUSDT | IDLE | 2.2 | 4.16 | 1.63 | 0.0 | 2458.72 | 63.29 | skipped_fast |
| REDUSDT | IDLE | 0.47 | 6.02 | 3.81 | 0.03 | 154659.78 | 12.51 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.02 | 10327.23 | 70.63 | skipped_fast |
| QNTUSDT | IDLE | 1.07 | 3.47 | 1.74 | 0.0 | 188348.19 | 6.23 | skipped_fast |
| RIZEUSDT | IDLE | 0.66 | 2.89 | 0.82 | -0.03 | 48642.73 | 46.44 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 22.31 | skipped_fast |
| RWAUSDT | IDLE | 1.01 | 1.8 | 1.45 | 0.01 | 57816.83 | 16.3 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
