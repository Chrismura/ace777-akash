# Hulk DIGEST — 2026-08-22T05:00:08Z

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
| PYTHUSDT | IDLE | 3.01 | 15.45 | 2.2 | 0.19 | 13250370.44 | 12.82 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.43 | 17.46 | 0.66 | 0.26 | 180643678.57 | 3.01 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.54 | 9.87 | 0.36 | 0.15 | 1107467.72 | 1.16 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.13 | 11.56 | 1.13 | 0.2 | 742654.97 | 13.11 | skipped_fast |
| CHIPUSDT | IDLE | 2.8 | 5.36 | 1.59 | 0.01 | 446616.99 | 5.99 | skipped_fast |
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.15 | 8.62 | 1.11 | 0.15 | 449067.89 | 10.61 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.02 | 8.75 | 0.52 | 0.08 | 203472.46 | 11.64 | skipped_fast |
| ZBCNUSDT | IDLE | 1.43 | 4.29 | 1.33 | 0.11 | 537277.57 | 23.3 | skipped_fast |
| QNTUSDT | IDLE | 2.72 | 9.16 | 3.81 | 0.11 | 187032.27 | 7.33 | skipped_fast |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.01 | 10345.47 | 21.57 | skipped_fast |
| KITEUSDT | IDLE | 1.77 | 6.71 | 0.53 | 0.15 | 68376.82 | 8.77 | skipped_fast |
| RIZEUSDT | IDLE | 1.84 | 7.71 | 4.52 | 0.1 | 58612.5 | 46.02 | skipped_fast |
| REDUSDT | IDLE | 0.94 | 7.96 | 4.93 | 0.2 | 157893.3 | 30.51 | skipped_fast |
| EDELUSDT | IDLE | 1.58 | 3.28 | 1.42 | -0.02 | 80245.07 | 22.2 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| TELUSDT | IDLE | 1.96 | 5.52 | 0.54 | 0.1 | 183501.37 | 14.88 | skipped_fast |
| RWAUSDT | IDLE | 1.57 | 3.13 | 0.08 | 0.07 | 56550.98 | 15.97 | skipped_fast |
| FLUIDUSDT | IDLE | 0.88 | 2.07 | 2.03 | 0.08 | 3692.42 | 22.81 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
