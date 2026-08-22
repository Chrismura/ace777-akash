# Hulk DIGEST — 2026-08-22T00:39:53Z

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
| PYTHUSDT | IDLE | 1.78 | 6.61 | 0.3 | 0.12 | 6436361.87 | 2.02 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.08 | 8.72 | 1.61 | 0.16 | 146498189.14 | 3.43 | skipped_fast |
| ZBCNUSDT | IDLE | 2.89 | 11.25 | 2.76 | 0.12 | 542846.49 | 5.32 | skipped_fast |
| HBARUSDT | IDLE | 2.79 | 6.36 | 1.44 | 0.08 | 939612.98 | 1.26 | skipped_fast |
| CCUSDT | IDLE | 1.94 | 7.42 | 0.92 | 0.14 | 640395.36 | 6.21 | skipped_fast |
| WUSDT | IDLE | 2.72 | 6.91 | 0.64 | 0.09 | 387991.37 | 12.2 | skipped_fast |
| CHIPUSDT | IDLE | 1.59 | 3.56 | 0.73 | 0.03 | 553274.21 | 18.38 | skipped_fast |
| BIOUSDT | IDLE | 2.33 | 5.3 | 0.0 | 0.03 | 186038.18 | 6.13 | skipped_fast |
| EDELUSDT | IDLE | 2.56 | 5.5 | 0.98 | -0.01 | 79867.72 | 21.93 | skipped_fast |
| RIZEUSDT | IDLE | 2.24 | 9.82 | 3.32 | 0.12 | 59975.37 | 45.4 | skipped_fast |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 19.88 | skipped_fast |
| TELUSDT | IDLE | 2.84 | 6.89 | 0.66 | 0.06 | 186256.23 | 41.17 | skipped_fast |
| QNTUSDT | IDLE | 2.55 | 5.42 | 1.33 | 0.06 | 170527.02 | 4.54 | skipped_fast |
| REDUSDT | IDLE | 0.72 | 6.54 | 0.96 | 0.24 | 158096.26 | 13.34 | skipped_fast |
| RWAINCUSDT | IDLE | 1.7 | 2.99 | 2.7 | 0.04 | 9787.93 | 26.95 | skipped_fast |
| KITEUSDT | IDLE | 1.06 | 3.12 | 0.2 | 0.1 | 61134.09 | 11.01 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.57 | 0.04 | 54744.45 | 8.21 | skipped_fast |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 19.61 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
