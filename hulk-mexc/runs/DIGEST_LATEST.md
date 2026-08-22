# Hulk DIGEST — 2026-08-22T11:52:30Z

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
| PYTHUSDT | IDLE | 2.16 | 9.66 | 7.01 | 0.01 | 51613262.34 | 2.05 | skipped_fast |
| XRPUSDT | IDLE | 2.34 | 14.26 | 8.8 | 0.09 | 216304268.06 | 2.02 | skipped_fast |
| CCUSDT | IDLE | 2.02 | 10.24 | 6.7 | 0.13 | 784439.99 | 3.43 | skipped_fast |
| HBARUSDT | IDLE | 1.46 | 5.26 | 3.48 | 0.02 | 1255133.52 | 6.47 | skipped_fast |
| WUSDT | IDLE | 1.56 | 6.27 | 3.81 | 0.02 | 581883.6 | 11.65 | skipped_fast |
| ZBCNUSDT | IDLE | 2.27 | 5.93 | 3.83 | -0.03 | 385033.82 | 21.03 | skipped_fast |
| CHIPUSDT | IDLE | 0.71 | 4.16 | 1.29 | -0.1 | 617371.35 | 3.34 | skipped_fast |
| KITEUSDT | IDLE | 2.59 | 6.24 | 0.18 | 0.05 | 81587.76 | 9.68 | skipped_fast |
| EDELUSDT | IDLE | 2.75 | 4.93 | 3.82 | -0.03 | 79308.71 | 34.15 | skipped_fast |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 2.65 | 6.75 | 5.51 | -0.03 | 167336.57 | 5.35 | skipped_fast |
| BIOUSDT | IDLE | 0.93 | 6.64 | 2.2 | -0.03 | 241509.51 | 6.44 | skipped_fast |
| QAITUSDT | IDLE | 2.2 | 4.16 | 1.63 | 0.01 | 2467.7 | 63.29 | skipped_fast |
| REDUSDT | IDLE | 0.47 | 6.02 | 3.71 | 0.03 | 154581.48 | 22.34 | skipped_fast |
| RWAINCUSDT | IDLE | 1.38 | 2.4 | 2.34 | -0.02 | 10327.23 | 70.63 | skipped_fast |
| QNTUSDT | IDLE | 1.07 | 3.47 | 1.79 | 0.0 | 188330.18 | 6.23 | skipped_fast |
| RIZEUSDT | IDLE | 0.66 | 2.89 | 0.85 | -0.03 | 48651.78 | 46.44 | skipped_fast |
| FLUIDUSDT | IDLE | 1.87 | 3.68 | 1.96 | -0.01 | 5711.25 | 22.31 | skipped_fast |
| RWAUSDT | IDLE | 1.01 | 1.8 | 1.45 | 0.01 | 57825.17 | 16.29 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
