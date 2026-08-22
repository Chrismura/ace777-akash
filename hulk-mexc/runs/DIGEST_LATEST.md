# Hulk DIGEST — 2026-08-22T17:08:28Z

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
| PYTHUSDT | IDLE | 1.72 | 8.45 | 0.3 | 0.1 | 49191160.75 | 5.7 | skipped_fast |
| XRPUSDT | IDLE | 1.33 | 7.64 | 3.64 | 0.05 | 214114120.87 | 1.36 | skipped_fast |
| HBARUSDT | IDLE | 0.8 | 3.03 | 0.96 | -0.0 | 1123766.52 | 5.16 | skipped_fast |
| CCUSDT | IDLE | 0.93 | 4.25 | 0.22 | 0.1 | 770352.97 | 8.36 | skipped_fast |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 1.1 | -0.1 | 631145.89 | 3.36 | skipped_fast |
| WUSDT | IDLE | 0.61 | 2.58 | 0.52 | -0.01 | 535578.96 | 8.45 | skipped_fast |
| ZBCNUSDT | IDLE | 1.27 | 3.45 | 1.34 | -0.02 | 312686.86 | 15.34 | skipped_fast |
| BIOUSDT | IDLE | 1.03 | 6.91 | 5.64 | -0.08 | 226510.53 | 3.34 | skipped_fast |
| EDELUSDT | IDLE | 1.72 | 3.0 | 2.91 | -0.01 | 74886.94 | 45.92 | skipped_fast |
| KITEUSDT | IDLE | 1.38 | 3.22 | 0.77 | 0.03 | 87550.49 | 9.71 | skipped_fast |
| REDUSDT | IDLE | 0.55 | 5.67 | 3.69 | -0.14 | 123103.5 | 18.19 | skipped_fast |
| RIZEUSDT | IDLE | 1.1 | 2.63 | 0.49 | 0.05 | 46185.22 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.39 | 2.71 | 0.47 | -0.01 | 2322.14 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 1.93 | -0.01 | 181193.31 | 4.72 | skipped_fast |
| RWAINCUSDT | IDLE | 0.8 | 1.53 | 0.43 | 0.01 | 7571.75 | 86.25 | skipped_fast |
| TELUSDT | IDLE | 1.0 | 2.37 | 2.05 | -0.0 | 136243.81 | 37.54 | skipped_fast |
| RWAUSDT | IDLE | 0.58 | 1.14 | 0.08 | 0.02 | 56186.72 | 16.17 | skipped_fast |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 21.6 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
