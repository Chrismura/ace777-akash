# Hulk DIGEST — 2026-08-22T17:04:58Z

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
| PYTHUSDT | IDLE | 1.7 | 8.33 | 0.53 | 0.09 | 49193699.26 | 3.81 | skipped_fast |
| XRPUSDT | IDLE | 1.32 | 7.64 | 3.2 | 0.06 | 214382550.85 | 2.7 | skipped_fast |
| HBARUSDT | IDLE | 0.8 | 3.03 | 0.92 | -0.0 | 1123678.39 | 3.87 | skipped_fast |
| CCUSDT | IDLE | 0.92 | 4.14 | 0.42 | 0.09 | 771596.81 | 8.37 | skipped_fast |
| CHIPUSDT | IDLE | 0.56 | 3.36 | 0.7 | -0.09 | 631088.01 | 3.35 | skipped_fast |
| WUSDT | IDLE | 0.61 | 2.58 | 0.57 | -0.01 | 543249.27 | 12.67 | skipped_fast |
| ZBCNUSDT | IDLE | 1.27 | 3.45 | 1.28 | -0.02 | 312681.91 | 15.83 | skipped_fast |
| BIOUSDT | IDLE | 1.03 | 6.91 | 5.64 | -0.07 | 226151.73 | 3.34 | skipped_fast |
| EDELUSDT | IDLE | 1.64 | 3.0 | 1.9 | -0.02 | 74769.32 | 22.83 | skipped_fast |
| KITEUSDT | IDLE | 1.4 | 3.22 | 1.04 | 0.03 | 87651.62 | 9.75 | skipped_fast |
| REDUSDT | IDLE | 0.55 | 5.67 | 3.84 | -0.14 | 123838.39 | 14.57 | skipped_fast |
| RIZEUSDT | IDLE | 1.1 | 2.63 | 0.5 | 0.05 | 46190.87 | 28.63 | skipped_fast |
| QAITUSDT | IDLE | 1.39 | 2.71 | 0.47 | -0.01 | 2322.14 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 1.97 | -0.01 | 181192.53 | 6.29 | skipped_fast |
| TELUSDT | IDLE | 0.99 | 2.37 | 1.94 | -0.0 | 136264.71 | 21.4 | skipped_fast |
| RWAINCUSDT | IDLE | 0.8 | 1.53 | 0.43 | 0.01 | 7571.75 | 91.62 | skipped_fast |
| RWAUSDT | IDLE | 0.57 | 1.14 | 0.0 | 0.02 | 56355.51 | 16.17 | skipped_fast |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 22.35 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
