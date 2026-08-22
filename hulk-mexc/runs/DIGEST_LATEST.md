# Hulk DIGEST — 2026-08-22T02:25:39Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.51 | 9.45 | 0.96 | 0.15 | 6984547.6 | 1.93 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.34 | 10.44 | 0.64 | 0.17 | 154909823.64 | 4.65 | skipped_fast |
| HBARUSDT | IDLE | 2.31 | 5.05 | 0.07 | 0.08 | 962546.3 | 2.47 | skipped_fast |
| ZBCNUSDT | IDLE | 2.49 | 9.63 | 2.8 | 0.09 | 542739.45 | 16.94 | skipped_fast |
| CCUSDT | IDLE | 1.7 | 6.33 | 0.02 | 0.15 | 656560.09 | 6.1 | skipped_fast |
| CHIPUSDT | IDLE | 2.23 | 5.07 | 0.57 | -0.01 | 474376.56 | 3.02 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.1 | 8.18 | 0.21 | 0.1 | 193244.2 | 11.76 | skipped_fast |
| WUSDT | IDLE | 1.85 | 5.09 | 0.03 | 0.1 | 402094.97 | 4.0 | skipped_fast |
| EDELUSDT | IDLE | 2.48 | 5.02 | 3.04 | -0.03 | 79688.21 | 44.74 | skipped_fast |
| RIZEUSDT | IDLE | 1.97 | 8.52 | 3.82 | 0.11 | 61300.83 | 45.71 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 8.27 | 6.46 | 0.17 | 157181.24 | 18.69 | skipped_fast |
| KITEUSDT | IDLE | 1.36 | 4.09 | 0.84 | 0.12 | 61833.04 | 9.92 | skipped_fast |
| QNTUSDT | IDLE | 2.23 | 4.89 | 0.1 | 0.07 | 171103.79 | 8.96 | skipped_fast |
| RWAINCUSDT | IDLE | 1.82 | 3.27 | 2.48 | 0.0 | 9345.09 | 37.95 | skipped_fast |
| QAITUSDT | IDLE | 1.88 | 3.57 | 1.22 | 0.0 | 3930.15 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 2.16 | 5.11 | 1.38 | 0.04 | 178515.31 | 62.21 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 20.38 | skipped_fast |
| RWAUSDT | IDLE | 1.05 | 2.08 | 0.16 | 0.04 | 54981.74 | 8.18 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
