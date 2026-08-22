# Hulk DIGEST — 2026-08-22T02:16:30Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.43 | 8.42 | 1.26 | 0.13 | 6930030.88 | 1.96 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.3 | 10.08 | 0.54 | 0.16 | 153983345.42 | 0.67 | skipped_fast |
| HBARUSDT | IDLE | 2.31 | 4.9 | 0.48 | 0.08 | 960850.36 | 1.24 | skipped_fast |
| ZBCNUSDT | IDLE | 2.5 | 9.63 | 3.15 | 0.08 | 545451.52 | 26.71 | skipped_fast |
| CCUSDT | IDLE | 1.67 | 6.14 | 0.0 | 0.15 | 653561.26 | 9.58 | skipped_fast |
| CHIPUSDT | IDLE | 2.13 | 4.91 | 0.0 | -0.01 | 515039.78 | 3.0 | skipped_fast |
| BIOUSDT | IDLE | 2.98 | 6.98 | 0.0 | 0.09 | 192557.94 | 14.8 | skipped_fast |
| WUSDT | IDLE | 1.79 | 4.81 | 0.0 | 0.09 | 401701.94 | 4.02 | skipped_fast |
| EDELUSDT | IDLE | 2.36 | 5.02 | 1.3 | -0.01 | 79536.3 | 21.98 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 3.9 | 0.11 | 61228.98 | 45.71 | skipped_fast |
| REDUSDT | IDLE | 0.99 | 8.27 | 5.95 | 0.18 | 156916.28 | 10.51 | skipped_fast |
| RWAINCUSDT | IDLE | 1.82 | 3.27 | 2.48 | 0.01 | 9604.71 | 27.14 | skipped_fast |
| QNTUSDT | IDLE | 2.28 | 4.89 | 0.79 | 0.07 | 171146.9 | 7.53 | skipped_fast |
| KITEUSDT | IDLE | 1.34 | 4.09 | 0.53 | 0.12 | 61506.63 | 9.89 | skipped_fast |
| QAITUSDT | IDLE | 1.86 | 3.57 | 0.94 | 0.0 | 3916.13 | 39.49 | skipped_fast |
| TELUSDT | IDLE | 2.16 | 5.11 | 1.43 | 0.04 | 179466.09 | 57.07 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 20.43 | skipped_fast |
| RWAUSDT | IDLE | 1.05 | 2.08 | 0.16 | 0.04 | 54815.96 | 8.17 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
