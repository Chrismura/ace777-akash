# Hulk DIGEST — 2026-08-22T16:45:46Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.07 | 10.19 | 0.34 | 0.09 | 50296115.66 | 1.9 | skipped_fast |
| XRPUSDT | IDLE | 1.31 | 7.64 | 2.99 | 0.07 | 214868131.63 | 3.37 | skipped_fast |
| HBARUSDT | IDLE | 0.79 | 3.03 | 0.69 | 0.0 | 1127130.19 | 2.57 | skipped_fast |
| CCUSDT | IDLE | 0.96 | 4.14 | 1.98 | 0.08 | 761566.0 | 10.22 | skipped_fast |
| CHIPUSDT | IDLE | 0.56 | 3.36 | 0.66 | -0.1 | 627007.26 | 3.34 | skipped_fast |
| WUSDT | IDLE | 0.6 | 2.58 | 0.44 | -0.01 | 544691.9 | 9.49 | skipped_fast |
| ZBCNUSDT | IDLE | 1.28 | 3.49 | 1.26 | -0.03 | 314786.12 | 14.3 | skipped_fast |
| BIOUSDT | IDLE | 0.95 | 6.58 | 3.56 | -0.06 | 219603.28 | 3.27 | skipped_fast |
| KITEUSDT | IDLE | 1.86 | 4.35 | 0.96 | 0.03 | 86687.14 | 11.51 | skipped_fast |
| EDELUSDT | IDLE | 1.39 | 2.52 | 1.79 | -0.03 | 74826.1 | 22.75 | skipped_fast |
| REDUSDT | IDLE | 0.51 | 5.67 | 3.58 | -0.14 | 128247.58 | 12.71 | skipped_fast |
| RIZEUSDT | IDLE | 1.44 | 3.47 | 0.42 | 0.06 | 46780.36 | 42.14 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | -0.01 | 2322.14 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.85 | 2.69 | 1.82 | -0.01 | 181098.02 | 7.85 | skipped_fast |
| RWAINCUSDT | IDLE | 0.8 | 1.53 | 0.43 | 0.01 | 7704.25 | 113.06 | skipped_fast |
| TELUSDT | IDLE | 0.97 | 2.37 | 1.68 | 0.0 | 136610.13 | 58.87 | skipped_fast |
| RWAUSDT | IDLE | 0.59 | 1.14 | 0.32 | 0.02 | 56513.84 | 16.21 | skipped_fast |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 21.52 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
