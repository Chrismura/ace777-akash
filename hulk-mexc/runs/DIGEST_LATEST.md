# Hulk DIGEST — 2026-08-22T01:31:06Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.84 | 10.86 | 0.19 | 0.16 | 6748202.27 | 1.94 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.19 | 8.56 | 0.24 | 0.15 | 150163302.07 | 2.03 | skipped_fast |
| HBARUSDT | IDLE | 2.99 | 6.36 | 0.5 | 0.08 | 952033.36 | 1.25 | skipped_fast |
| ZBCNUSDT | IDLE | 2.6 | 10.08 | 2.77 | 0.1 | 546940.5 | 18.88 | skipped_fast |
| CCUSDT | IDLE | 1.77 | 7.28 | 0.06 | 0.16 | 660429.97 | 9.59 | skipped_fast |
| WUSDT | IDLE | 2.72 | 6.65 | 1.03 | 0.08 | 392054.32 | 9.19 | skipped_fast |
| CHIPUSDT | IDLE | 1.64 | 3.56 | 1.55 | -0.01 | 513357.71 | 6.18 | skipped_fast |
| BIOUSDT | IDLE | 2.53 | 5.57 | 1.13 | 0.04 | 186053.67 | 3.08 | skipped_fast |
| EDELUSDT | IDLE | 2.62 | 5.5 | 1.95 | -0.03 | 79566.25 | 22.15 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.15 | 0.11 | 60697.0 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 0.97 | 8.27 | 4.64 | 0.18 | 158571.66 | 17.53 | skipped_fast |
| TELUSDT | IDLE | 2.6 | 6.19 | 1.38 | 0.05 | 181595.68 | 20.74 | skipped_fast |
| QNTUSDT | IDLE | 2.42 | 5.18 | 0.94 | 0.07 | 170117.57 | 6.03 | skipped_fast |
| KITEUSDT | IDLE | 1.5 | 4.63 | 0.18 | 0.12 | 60961.02 | 10.8 | skipped_fast |
| QAITUSDT | IDLE | 2.06 | 4.02 | 0.7 | 0.01 | 3856.35 | 67.05 | skipped_fast |
| RWAINCUSDT | IDLE | 1.3 | 2.45 | 1.01 | 0.04 | 9587.29 | 42.83 | skipped_fast |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.49 | 0.04 | 54942.81 | 8.21 | skipped_fast |
| FLUIDUSDT | IDLE | 1.35 | 3.74 | 0.0 | 0.1 | 4798.05 | 49.24 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
