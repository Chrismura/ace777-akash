# Hulk DIGEST — 2026-08-22T05:06:05Z

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
| PYTHUSDT | IDLE | 3.23 | 15.45 | 3.67 | 0.16 | 13970429.82 | 16.73 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.51 | 19.3 | 0.97 | 0.28 | 183519170.44 | 6.54 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.59 | 10.33 | 0.84 | 0.15 | 1127399.91 | 4.64 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.15 | 11.56 | 1.34 | 0.2 | 747594.86 | 2.46 | skipped_fast |
| CHIPUSDT | IDLE | 2.81 | 5.36 | 1.68 | 0.01 | 446750.42 | 2.99 | skipped_fast |
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.13 | 8.22 | 0.84 | 0.15 | 450487.41 | 10.57 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.03 | 9.0 | 0.12 | 0.1 | 203417.77 | 5.79 | skipped_fast |
| ZBCNUSDT | IDLE | 1.61 | 4.29 | 2.72 | 0.09 | 538381.26 | 127.51 | skipped_fast |
| QNTUSDT | IDLE | 2.73 | 9.16 | 3.98 | 0.1 | 187032.79 | 8.82 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.01 | 10345.47 | 21.57 | skipped_fast |
| REDUSDT | IDLE | 1.01 | 7.96 | 6.29 | 0.19 | 158250.93 | 9.74 | skipped_fast |
| KITEUSDT | IDLE | 1.82 | 6.62 | 0.38 | 0.15 | 68352.47 | 13.13 | skipped_fast |
| EDELUSDT | IDLE | 1.57 | 3.28 | 1.31 | -0.02 | 80959.23 | 33.2 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| TELUSDT | IDLE | 1.95 | 5.52 | 0.39 | 0.1 | 184065.63 | 24.81 | skipped_fast |
| RIZEUSDT | IDLE | 1.09 | 4.41 | 3.8 | 0.09 | 58673.8 | 46.13 | skipped_fast |
| RWAUSDT | IDLE | 1.7 | 3.38 | 0.08 | 0.07 | 56838.7 | 7.97 | skipped_fast |
| FLUIDUSDT | IDLE | 0.88 | 2.07 | 2.03 | 0.08 | 3692.42 | 22.08 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
