# Hulk DIGEST — 2026-08-21T21:16:10Z

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
| PYTHUSDT | IDLE | 1.19 | 4.51 | 0.99 | 0.09 | 5608995.68 | 8.3 | skipped_fast |
| XRPUSDT | IDLE | 1.15 | 3.73 | 1.95 | 0.1 | 128191244.21 | 2.17 | skipped_fast |
| ZBCNUSDT | IDLE | 2.0 | 8.19 | 5.04 | 0.08 | 482943.86 | 22.41 | skipped_fast |
| CHIPUSDT | IDLE | 1.91 | 5.61 | 4.38 | 0.06 | 515487.76 | 9.36 | skipped_fast |
| CCUSDT | IDLE | 1.15 | 3.14 | 0.51 | 0.1 | 642662.22 | 6.46 | skipped_fast |
| HBARUSDT | IDLE | 1.6 | 3.04 | 1.05 | 0.06 | 810458.22 | 1.29 | skipped_fast |
| WUSDT | IDLE | 1.96 | 3.83 | 0.64 | 0.06 | 367039.47 | 11.52 | skipped_fast |
| BIOUSDT | IDLE | 2.46 | 5.2 | 2.61 | 0.01 | 187629.94 | 3.15 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 11.01 | 9.15 | 0.16 | 153556.41 | 15.53 | skipped_fast |
| RIZEUSDT | IDLE | 1.88 | 9.54 | 1.56 | 0.01 | 56207.43 | 33.43 | skipped_fast |
| RWAINCUSDT | IDLE | 2.27 | 4.3 | 1.64 | 0.02 | 10271.93 | 10.76 | skipped_fast |
| EDELUSDT | IDLE | 2.06 | 4.12 | 2.86 | -0.06 | 82446.49 | 34.03 | skipped_fast |
| KITEUSDT | IDLE | 1.31 | 4.0 | 2.16 | 0.11 | 61012.39 | 12.98 | skipped_fast |
| QAITUSDT | IDLE | 2.5 | 4.38 | 4.2 | -0.04 | 3753.25 | 147.5 | skipped_fast |
| TELUSDT | IDLE | 1.38 | 3.39 | 1.32 | 0.01 | 179335.8 | 37.52 | skipped_fast |
| QNTUSDT | IDLE | 1.45 | 2.65 | 1.66 | 0.04 | 61188.27 | 1.56 | skipped_fast |
| RWAUSDT | IDLE | 0.65 | 1.17 | 0.91 | 0.03 | 53718.81 | 24.91 | skipped_fast |
| FLUIDUSDT | IDLE | 0.58 | 1.15 | 1.1 | 0.08 | 4161.15 | 22.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
