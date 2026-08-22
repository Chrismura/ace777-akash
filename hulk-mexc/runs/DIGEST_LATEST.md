# Hulk DIGEST — 2026-08-22T03:08:48Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.35 | 10.53 | 0.11 | 0.16 | 7516754.67 | 20.59 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.26 | 11.43 | 0.15 | 0.21 | 160265851.22 | 1.93 | skipped_fast |
| HBARUSDT | IDLE | 2.15 | 5.29 | 0.24 | 0.1 | 996818.81 | 1.22 | skipped_fast |
| CCUSDT | IDLE | 1.94 | 8.96 | 0.26 | 0.19 | 667426.63 | 6.71 | skipped_fast |
| BIOUSDT | IDLE | 3.01 | 7.36 | 2.34 | 0.06 | 195574.6 | 3.01 | skipped_fast |
| CHIPUSDT | IDLE | 1.93 | 4.28 | 0.3 | -0.0 | 448840.31 | 2.98 | skipped_fast |
| ZBCNUSDT | IDLE | 1.45 | 5.16 | 2.48 | 0.12 | 541680.54 | 43.47 | skipped_fast |
| WUSDT | IDLE | 1.78 | 5.61 | 0.42 | 0.12 | 417126.2 | 10.86 | skipped_fast |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.46 | 0.09 | 60612.76 | 22.1 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 3.94 | 0.21 | 157944.06 | 18.99 | skipped_fast |
| EDELUSDT | IDLE | 1.92 | 3.83 | 2.82 | -0.03 | 80003.06 | 56.02 | skipped_fast |
| RWAINCUSDT | IDLE | 1.94 | 3.44 | 3.0 | -0.0 | 9452.18 | 43.29 | skipped_fast |
| KITEUSDT | IDLE | 1.33 | 4.16 | 0.02 | 0.12 | 63816.89 | 11.61 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.01 | 3833.07 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.69 | 3.97 | 0.15 | 0.09 | 172838.83 | 2.97 | skipped_fast |
| TELUSDT | IDLE | 0.91 | 2.19 | 0.31 | 0.07 | 173215.12 | 56.25 | skipped_fast |
| RWAUSDT | IDLE | 1.16 | 2.31 | 0.08 | 0.05 | 56146.23 | 24.24 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 18.16 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
