# Hulk DIGEST — 2026-08-22T16:44:58Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.06 | 10.19 | 0.21 | 0.09 | 50708865.53 | 7.6 | skipped_fast |
| XRPUSDT | IDLE | 1.32 | 7.64 | 3.18 | 0.07 | 214918949.89 | 2.7 | skipped_fast |
| HBARUSDT | IDLE | 0.79 | 3.03 | 0.69 | 0.0 | 1126535.1 | 1.29 | skipped_fast |
| CCUSDT | IDLE | 0.97 | 4.14 | 2.13 | 0.08 | 760602.09 | 4.25 | skipped_fast |
| CHIPUSDT | IDLE | 0.56 | 3.36 | 0.56 | -0.1 | 626976.53 | 6.68 | skipped_fast |
| WUSDT | IDLE | 0.61 | 2.58 | 0.62 | -0.01 | 543873.87 | 11.61 | skipped_fast |
| ZBCNUSDT | IDLE | 1.29 | 3.49 | 1.35 | -0.03 | 314785.35 | 15.85 | skipped_fast |
| BIOUSDT | IDLE | 0.95 | 6.58 | 3.56 | -0.06 | 219670.47 | 3.27 | skipped_fast |
| KITEUSDT | IDLE | 1.89 | 4.35 | 1.46 | 0.02 | 86742.36 | 9.78 | skipped_fast |
| EDELUSDT | IDLE | 1.39 | 2.52 | 1.79 | -0.02 | 74851.07 | 22.75 | skipped_fast |
| REDUSDT | IDLE | 0.51 | 5.67 | 3.37 | -0.13 | 128487.5 | 12.69 | skipped_fast |
| RIZEUSDT | IDLE | 1.44 | 3.47 | 0.45 | 0.06 | 46795.25 | 45.4 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | -0.01 | 2322.14 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.85 | 2.69 | 1.82 | -0.01 | 181108.57 | 14.13 | skipped_fast |
| TELUSDT | IDLE | 0.99 | 2.37 | 1.89 | -0.0 | 136676.81 | 58.87 | skipped_fast |
| RWAINCUSDT | IDLE | 0.8 | 1.53 | 0.43 | 0.01 | 7704.25 | 113.06 | skipped_fast |
| RWAUSDT | IDLE | 0.57 | 1.14 | 0.0 | 0.03 | 56505.34 | 24.3 | skipped_fast |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 21.54 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
