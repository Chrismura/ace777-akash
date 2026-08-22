# Hulk DIGEST — 2026-08-22T03:03:23Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.28 | 9.55 | 0.72 | 0.15 | 7433718.02 | 1.9 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.25 | 11.15 | 0.42 | 0.2 | 159751080.65 | 5.81 | skipped_fast |
| HBARUSDT | IDLE | 2.15 | 5.29 | 0.32 | 0.1 | 993469.26 | 1.22 | skipped_fast |
| CCUSDT | IDLE | 1.92 | 8.83 | 0.02 | 0.19 | 665984.82 | 6.7 | skipped_fast |
| BIOUSDT | IDLE | 3.01 | 7.36 | 2.26 | 0.08 | 194659.35 | 3.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.92 | 4.28 | 0.21 | -0.0 | 449198.46 | 5.97 | skipped_fast |
| ZBCNUSDT | IDLE | 1.43 | 5.16 | 1.94 | 0.12 | 539709.27 | 25.45 | skipped_fast |
| WUSDT | IDLE | 1.72 | 5.34 | 0.04 | 0.12 | 417457.33 | 7.89 | skipped_fast |
| EDELUSDT | IDLE | 1.9 | 3.83 | 2.39 | -0.03 | 79918.6 | 22.22 | skipped_fast |
| RIZEUSDT | IDLE | 1.82 | 7.71 | 4.26 | 0.09 | 61368.42 | 44.22 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 4.16 | 0.2 | 157810.28 | 10.31 | skipped_fast |
| RWAINCUSDT | IDLE | 1.97 | 3.44 | 3.32 | -0.0 | 9418.45 | 43.45 | skipped_fast |
| KITEUSDT | IDLE | 1.31 | 4.03 | 0.23 | 0.12 | 62503.83 | 11.66 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.01 | 3934.37 | 63.67 | skipped_fast |
| QNTUSDT | IDLE | 1.71 | 3.97 | 0.49 | 0.08 | 172751.2 | 10.44 | skipped_fast |
| RWAUSDT | IDLE | 1.17 | 2.31 | 0.24 | 0.05 | 56116.32 | 32.34 | skipped_fast |
| TELUSDT | IDLE | 0.81 | 1.88 | 0.82 | 0.06 | 173054.98 | 61.98 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 22.38 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
