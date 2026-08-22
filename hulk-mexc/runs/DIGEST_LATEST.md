# Hulk DIGEST — 2026-08-22T16:58:58Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.07 | 10.19 | 0.44 | 0.09 | 49200386.32 | 1.9 | skipped_fast |
| XRPUSDT | IDLE | 1.32 | 7.64 | 3.08 | 0.06 | 214649061.61 | 2.7 | skipped_fast |
| HBARUSDT | IDLE | 0.8 | 3.03 | 0.92 | -0.0 | 1131645.59 | 6.45 | skipped_fast |
| CCUSDT | IDLE | 0.94 | 4.14 | 1.23 | 0.1 | 769329.46 | 9.3 | skipped_fast |
| CHIPUSDT | IDLE | 0.56 | 3.36 | 0.7 | -0.1 | 629747.57 | 3.34 | skipped_fast |
| WUSDT | IDLE | 0.61 | 2.58 | 0.54 | -0.01 | 544991.83 | 9.5 | skipped_fast |
| BIOUSDT | IDLE | 1.03 | 6.91 | 5.67 | -0.07 | 225786.57 | 3.34 | skipped_fast |
| ZBCNUSDT | IDLE | 1.29 | 3.49 | 1.36 | -0.02 | 312614.41 | 30.21 | skipped_fast |
| KITEUSDT | IDLE | 1.88 | 4.35 | 1.4 | 0.03 | 87699.72 | 10.67 | skipped_fast |
| EDELUSDT | IDLE | 1.66 | 3.0 | 2.13 | -0.02 | 74940.32 | 34.27 | skipped_fast |
| REDUSDT | IDLE | 0.51 | 5.67 | 3.64 | -0.13 | 126295.28 | 10.0 | skipped_fast |
| RIZEUSDT | IDLE | 1.44 | 3.47 | 0.44 | 0.06 | 46207.9 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | -0.01 | 2322.14 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.85 | 2.69 | 1.77 | -0.01 | 181162.79 | 4.71 | skipped_fast |
| RWAINCUSDT | IDLE | 0.8 | 1.53 | 0.43 | 0.01 | 7571.75 | 102.34 | skipped_fast |
| TELUSDT | IDLE | 1.0 | 2.37 | 2.21 | -0.0 | 136242.54 | 64.34 | skipped_fast |
| RWAUSDT | IDLE | 0.62 | 1.23 | 0.08 | 0.02 | 56354.71 | 16.17 | skipped_fast |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 21.53 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
