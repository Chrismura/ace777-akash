# Hulk DIGEST — 2026-08-22T04:38:30Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.88 | 13.73 | 0.42 | 0.2 | 11505789.03 | 12.78 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.33 | 15.66 | 0.08 | 0.26 | 172873678.33 | 7.29 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.41 | 8.67 | 0.11 | 0.14 | 1041911.16 | 1.17 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.13 | 11.56 | 1.34 | 0.2 | 736577.31 | 9.04 | skipped_fast |
| CHIPUSDT | IDLE | 2.85 | 5.36 | 2.24 | 0.0 | 451431.45 | 12.04 | skipped_fast |
| WUSDT | IDLE | 1.99 | 7.53 | 0.04 | 0.15 | 435280.34 | 13.48 | skipped_fast |
| BIOUSDT | IDLE | 2.96 | 7.36 | 1.52 | 0.07 | 200708.68 | 2.97 | skipped_fast |
| ZBCNUSDT | IDLE | 1.46 | 4.29 | 1.85 | 0.11 | 537341.71 | 51.04 | skipped_fast |
| EDELUSDT | IDLE | 2.04 | 4.07 | 2.93 | -0.03 | 80281.3 | 11.18 | skipped_fast |
| QNTUSDT | IDLE | 2.44 | 8.56 | 4.36 | 0.1 | 181662.61 | 7.37 | skipped_fast |
| RIZEUSDT | IDLE | 1.86 | 7.71 | 5.01 | 0.09 | 58557.78 | 44.52 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.63 | 0.2 | 158327.2 | 18.33 | skipped_fast |
| KITEUSDT | IDLE | 1.59 | 5.55 | 0.31 | 0.13 | 68092.63 | 11.49 | skipped_fast |
| RWAINCUSDT | IDLE | 2.05 | 3.6 | 3.37 | -0.0 | 9357.09 | 70.63 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 1.72 | 4.32 | 0.35 | 0.1 | 177325.45 | 30.05 | skipped_fast |
| RWAUSDT | IDLE | 1.55 | 3.05 | 0.32 | 0.06 | 56543.2 | 16.05 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 22.15 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
