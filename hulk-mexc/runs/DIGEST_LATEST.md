# Hulk DIGEST — 2026-08-22T04:37:50Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.86 | 13.61 | 0.05 | 0.2 | 11433522.97 | 14.57 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.3 | 15.2 | 0.09 | 0.26 | 172483373.5 | 6.11 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.39 | 8.43 | 0.16 | 0.14 | 1042564.24 | 4.68 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 11.56 | 1.53 | 0.2 | 736529.3 | 7.4 | skipped_fast |
| CHIPUSDT | IDLE | 2.85 | 5.36 | 2.24 | 0.0 | 451392.04 | 15.01 | skipped_fast |
| WUSDT | IDLE | 1.99 | 7.53 | 0.04 | 0.15 | 435309.87 | 14.44 | skipped_fast |
| BIOUSDT | IDLE | 2.96 | 7.36 | 1.47 | 0.07 | 200935.13 | 2.98 | skipped_fast |
| ZBCNUSDT | IDLE | 1.48 | 4.29 | 2.31 | 0.11 | 537562.3 | 82.08 | skipped_fast |
| EDELUSDT | IDLE | 2.04 | 4.07 | 2.93 | -0.04 | 80286.62 | 11.18 | skipped_fast |
| QNTUSDT | IDLE | 2.44 | 8.56 | 4.36 | 0.1 | 181682.1 | 7.37 | skipped_fast |
| RIZEUSDT | IDLE | 1.86 | 7.71 | 5.01 | 0.09 | 58555.82 | 44.52 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.48 | 0.2 | 158363.13 | 8.75 | skipped_fast |
| KITEUSDT | IDLE | 1.59 | 5.55 | 0.28 | 0.13 | 68032.51 | 10.61 | skipped_fast |
| RWAINCUSDT | IDLE | 2.04 | 3.6 | 3.16 | -0.0 | 9331.56 | 48.95 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 1.72 | 4.32 | 0.25 | 0.1 | 177208.84 | 15.03 | skipped_fast |
| RWAUSDT | IDLE | 1.55 | 3.05 | 0.32 | 0.06 | 56525.62 | 8.02 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3702.43 | 21.51 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
