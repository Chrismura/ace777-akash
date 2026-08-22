# Hulk DIGEST — 2026-08-22T02:06:21Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.42 | 8.42 | 1.1 | 0.14 | 6891397.93 | 1.95 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.31 | 10.03 | 1.01 | 0.15 | 154057119.47 | 1.34 | skipped_fast |
| HBARUSDT | IDLE | 2.32 | 4.9 | 0.52 | 0.07 | 952570.56 | 1.24 | skipped_fast |
| ZBCNUSDT | IDLE | 2.5 | 9.63 | 3.24 | 0.08 | 547631.46 | 49.13 | skipped_fast |
| CCUSDT | IDLE | 1.67 | 6.1 | 0.17 | 0.15 | 655051.13 | 3.49 | skipped_fast |
| CHIPUSDT | IDLE | 1.6 | 3.69 | 0.03 | 0.02 | 516569.17 | 6.07 | skipped_fast |
| BIOUSDT | IDLE | 2.93 | 6.4 | 0.33 | 0.08 | 185305.84 | 5.98 | skipped_fast |
| WUSDT | IDLE | 1.73 | 4.41 | 0.39 | 0.08 | 400331.57 | 20.22 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.0 | 0.11 | 61097.85 | 45.71 | skipped_fast |
| EDELUSDT | IDLE | 2.35 | 5.02 | 1.19 | -0.02 | 79596.15 | 54.98 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 8.27 | 6.24 | 0.17 | 156731.8 | 19.45 | skipped_fast |
| QNTUSDT | IDLE | 2.32 | 4.89 | 1.36 | 0.06 | 171287.12 | 24.18 | skipped_fast |
| KITEUSDT | IDLE | 1.35 | 4.09 | 0.81 | 0.12 | 61333.91 | 23.41 | skipped_fast |
| QAITUSDT | IDLE | 1.78 | 3.57 | 0.0 | 0.01 | 3870.41 | 31.31 | skipped_fast |
| RWAINCUSDT | IDLE | 1.75 | 3.27 | 1.58 | 0.03 | 9241.73 | 69.8 | skipped_fast |
| TELUSDT | IDLE | 2.18 | 5.11 | 1.64 | 0.04 | 178977.55 | 67.44 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 21.2 | skipped_fast |
| RWAUSDT | IDLE | 1.09 | 2.08 | 0.65 | 0.03 | 54613.8 | 8.21 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
