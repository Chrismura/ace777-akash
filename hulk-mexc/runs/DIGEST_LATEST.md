# Hulk DIGEST — 2026-08-22T04:13:25Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.85 | 13.11 | 0.48 | 0.2 | 10283010.01 | 5.51 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 12.22 | 1.2 | 0.2 | 167025122.48 | 2.53 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.1 | 11.56 | 0.23 | 0.22 | 723181.29 | 17.82 | skipped_fast |
| HBARUSDT | IDLE | 2.11 | 6.2 | 0.01 | 0.11 | 1009091.85 | 2.4 | skipped_fast |
| CHIPUSDT | IDLE | 2.86 | 5.36 | 2.44 | 0.0 | 451678.02 | 3.02 | skipped_fast |
| BIOUSDT | IDLE | 3.03 | 7.36 | 2.64 | 0.06 | 199761.21 | 3.01 | skipped_fast |
| WUSDT | IDLE | 1.96 | 7.18 | 0.57 | 0.14 | 429227.07 | 12.63 | skipped_fast |
| ZBCNUSDT | IDLE | 1.44 | 4.29 | 1.4 | 0.12 | 535389.45 | 17.13 | skipped_fast |
| EDELUSDT | IDLE | 2.08 | 4.07 | 3.58 | -0.04 | 80357.19 | 33.73 | skipped_fast |
| RIZEUSDT | IDLE | 1.86 | 7.71 | 5.01 | 0.1 | 59143.7 | 44.52 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 3.85 | 0.21 | 158287.28 | 23.72 | skipped_fast |
| KITEUSDT | IDLE | 1.59 | 5.55 | 0.36 | 0.13 | 67521.39 | 12.38 | skipped_fast |
| RWAINCUSDT | IDLE | 2.04 | 3.6 | 3.22 | 0.01 | 9433.64 | 64.83 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.53 | 3.8 | 0.44 | 0.09 | 178574.52 | 5.93 | skipped_fast |
| RWAUSDT | IDLE | 1.55 | 3.05 | 0.4 | 0.06 | 56288.4 | 24.05 | skipped_fast |
| TELUSDT | IDLE | 1.02 | 2.4 | 0.56 | 0.07 | 173856.9 | 40.94 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 19.53 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
