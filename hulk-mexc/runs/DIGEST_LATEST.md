# Hulk DIGEST — 2026-08-22T16:46:39Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.07 | 10.19 | 0.45 | 0.09 | 50169662.56 | 1.9 | skipped_fast |
| XRPUSDT | IDLE | 1.31 | 7.64 | 2.9 | 0.07 | 214888324.16 | 4.71 | skipped_fast |
| HBARUSDT | IDLE | 0.79 | 3.03 | 0.64 | 0.0 | 1127701.48 | 1.29 | skipped_fast |
| CCUSDT | IDLE | 0.96 | 4.14 | 1.99 | 0.09 | 762205.89 | 8.51 | skipped_fast |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 0.73 | -0.1 | 626825.75 | 6.7 | skipped_fast |
| WUSDT | IDLE | 0.6 | 2.58 | 0.4 | -0.01 | 544583.07 | 10.54 | skipped_fast |
| ZBCNUSDT | IDLE | 1.28 | 3.49 | 1.22 | -0.03 | 314765.59 | 13.27 | skipped_fast |
| BIOUSDT | IDLE | 0.95 | 6.58 | 3.62 | -0.06 | 219557.22 | 3.27 | skipped_fast |
| KITEUSDT | IDLE | 1.86 | 4.35 | 0.93 | 0.03 | 86643.07 | 13.27 | skipped_fast |
| EDELUSDT | IDLE | 1.38 | 2.52 | 1.57 | -0.02 | 74728.36 | 11.37 | skipped_fast |
| REDUSDT | IDLE | 0.51 | 5.67 | 3.59 | -0.15 | 128258.46 | 13.6 | skipped_fast |
| RIZEUSDT | IDLE | 1.43 | 3.47 | 0.34 | 0.05 | 46731.96 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | -0.01 | 2322.14 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.85 | 2.69 | 1.74 | -0.01 | 181119.0 | 3.14 | skipped_fast |
| RWAINCUSDT | IDLE | 0.8 | 1.53 | 0.43 | 0.01 | 7704.25 | 113.06 | skipped_fast |
| TELUSDT | IDLE | 0.98 | 2.37 | 1.84 | -0.0 | 136579.2 | 64.27 | skipped_fast |
| RWAUSDT | IDLE | 0.59 | 1.14 | 0.24 | 0.02 | 56511.5 | 16.21 | skipped_fast |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 21.5 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
