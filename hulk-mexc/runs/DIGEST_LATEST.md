# Hulk DIGEST — 2026-08-22T01:56:13Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.89 | 10.86 | 1.31 | 0.14 | 6857473.62 | 5.87 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.41 | 10.52 | 1.46 | 0.15 | 153721859.02 | 5.38 | skipped_fast |
| HBARUSDT | IDLE | 3.04 | 6.36 | 1.11 | 0.07 | 948636.44 | 2.5 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.75 | 0.08 | 551070.05 | 3.39 | skipped_fast |
| CCUSDT | IDLE | 1.8 | 7.36 | 0.71 | 0.16 | 662404.72 | 7.02 | skipped_fast |
| WUSDT | IDLE | 2.68 | 6.65 | 0.39 | 0.08 | 398428.23 | 15.2 | skipped_fast |
| CHIPUSDT | IDLE | 1.61 | 3.56 | 1.13 | 0.01 | 510589.73 | 6.15 | skipped_fast |
| BIOUSDT | IDLE | 2.62 | 5.86 | 0.52 | 0.05 | 185152.68 | 6.11 | skipped_fast |
| EDELUSDT | IDLE | 2.62 | 5.5 | 1.95 | -0.02 | 79521.1 | 22.15 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.02 | 0.11 | 61049.58 | 45.71 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 8.27 | 6.43 | 0.15 | 157242.69 | 18.69 | skipped_fast |
| KITEUSDT | IDLE | 1.61 | 5.17 | 0.33 | 0.12 | 61333.16 | 10.78 | skipped_fast |
| QNTUSDT | IDLE | 2.43 | 5.18 | 1.09 | 0.07 | 171362.1 | 7.56 | skipped_fast |
| QAITUSDT | IDLE | 2.04 | 4.02 | 0.43 | 0.01 | 3870.41 | 31.31 | skipped_fast |
| TELUSDT | IDLE | 2.58 | 6.19 | 1.07 | 0.05 | 181491.53 | 56.98 | skipped_fast |
| RWAINCUSDT | IDLE | 1.77 | 3.27 | 1.79 | 0.03 | 9181.85 | 80.36 | skipped_fast |
| FLUIDUSDT | IDLE | 1.46 | 3.74 | 2.03 | 0.08 | 4799.07 | 21.96 | skipped_fast |
| RWAUSDT | IDLE | 1.07 | 2.08 | 0.41 | 0.03 | 54652.85 | 8.19 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
