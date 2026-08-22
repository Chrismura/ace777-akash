# Hulk DIGEST — 2026-08-22T16:51:20Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.1 | 10.19 | 1.29 | 0.07 | 49951783.86 | 3.84 | skipped_fast |
| XRPUSDT | IDLE | 1.31 | 7.64 | 2.95 | 0.07 | 214898661.4 | 3.37 | skipped_fast |
| HBARUSDT | IDLE | 0.8 | 3.03 | 0.83 | -0.01 | 1130747.39 | 7.74 | skipped_fast |
| CCUSDT | IDLE | 0.98 | 4.14 | 2.36 | 0.09 | 760551.2 | 10.24 | skipped_fast |
| CHIPUSDT | IDLE | 0.56 | 3.36 | 0.7 | -0.1 | 629336.0 | 6.69 | skipped_fast |
| WUSDT | IDLE | 0.61 | 2.58 | 0.63 | -0.01 | 544865.78 | 11.62 | skipped_fast |
| ZBCNUSDT | IDLE | 1.29 | 3.49 | 1.45 | -0.04 | 314505.8 | 23.01 | skipped_fast |
| BIOUSDT | IDLE | 1.04 | 6.91 | 5.77 | -0.08 | 226123.55 | 10.01 | skipped_fast |
| KITEUSDT | IDLE | 1.85 | 4.35 | 0.8 | 0.03 | 86547.75 | 11.49 | skipped_fast |
| EDELUSDT | IDLE | 1.39 | 2.52 | 1.79 | -0.01 | 74719.0 | 22.75 | skipped_fast |
| REDUSDT | IDLE | 0.52 | 5.67 | 3.72 | -0.14 | 128061.12 | 11.83 | skipped_fast |
| RIZEUSDT | IDLE | 1.44 | 3.47 | 0.52 | 0.05 | 46608.01 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | -0.01 | 2322.14 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.85 | 2.69 | 1.84 | -0.01 | 181211.85 | 3.14 | skipped_fast |
| TELUSDT | IDLE | 0.99 | 2.37 | 1.94 | -0.0 | 136484.96 | 58.93 | skipped_fast |
| RWAINCUSDT | IDLE | 0.8 | 1.53 | 0.43 | 0.01 | 7704.25 | 113.06 | skipped_fast |
| RWAUSDT | IDLE | 0.61 | 1.23 | 0.0 | 0.03 | 56493.4 | 32.36 | skipped_fast |
| FLUIDUSDT | IDLE | 0.1 | 0.19 | 0.19 | -0.03 | 4628.58 | 22.29 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
