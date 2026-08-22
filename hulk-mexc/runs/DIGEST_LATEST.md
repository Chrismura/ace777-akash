# Hulk DIGEST — 2026-08-22T03:09:39Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.36 | 10.61 | 0.28 | 0.17 | 7544366.99 | 15.0 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.27 | 11.43 | 0.37 | 0.2 | 160445460.65 | 3.22 | skipped_fast |
| HBARUSDT | IDLE | 2.14 | 5.29 | 0.17 | 0.1 | 996858.95 | 1.22 | skipped_fast |
| CCUSDT | IDLE | 1.94 | 8.96 | 0.53 | 0.19 | 668600.55 | 12.6 | skipped_fast |
| BIOUSDT | IDLE | 3.02 | 7.36 | 2.46 | 0.07 | 195610.46 | 6.01 | skipped_fast |
| CHIPUSDT | IDLE | 1.94 | 4.28 | 0.45 | -0.0 | 448890.5 | 2.98 | skipped_fast |
| ZBCNUSDT | IDLE | 1.46 | 5.16 | 2.62 | 0.12 | 541254.13 | 38.63 | skipped_fast |
| WUSDT | IDLE | 1.78 | 5.61 | 0.3 | 0.12 | 417330.42 | 11.84 | skipped_fast |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.39 | 0.1 | 59498.02 | 44.22 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 3.99 | 0.21 | 157940.38 | 12.67 | skipped_fast |
| EDELUSDT | IDLE | 1.95 | 3.83 | 3.26 | -0.04 | 80003.08 | 44.84 | skipped_fast |
| RWAINCUSDT | IDLE | 1.94 | 3.44 | 3.0 | -0.0 | 9452.18 | 48.71 | skipped_fast |
| KITEUSDT | IDLE | 1.32 | 4.17 | 0.0 | 0.12 | 63818.78 | 13.41 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.01 | 3824.31 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.69 | 3.97 | 0.1 | 0.09 | 172829.55 | 4.46 | skipped_fast |
| RWAUSDT | IDLE | 1.16 | 2.31 | 0.08 | 0.05 | 56145.08 | 16.17 | skipped_fast |
| TELUSDT | IDLE | 0.91 | 2.19 | 0.31 | 0.07 | 173226.46 | 61.38 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 22.33 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
