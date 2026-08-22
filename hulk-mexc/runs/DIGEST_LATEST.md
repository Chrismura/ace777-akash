# Hulk DIGEST — 2026-08-22T04:53:33Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.98 | 15.45 | 0.97 | 0.2 | 12507732.33 | 19.89 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.42 | 17.46 | 0.25 | 0.27 | 179158439.81 | 3.0 | skipped_fast |
| HBARUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.5 | 9.6 | 0.05 | 0.15 | 1076108.88 | 1.16 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 11.56 | 1.47 | 0.2 | 739888.86 | 6.57 | skipped_fast |
| CHIPUSDT | IDLE | 2.8 | 5.36 | 1.56 | 0.01 | 454079.61 | 2.99 | skipped_fast |
| WUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.14 | 8.62 | 0.92 | 0.15 | 437623.95 | 12.51 | skipped_fast |
| BIOUSDT | IDLE | 2.92 | 7.36 | 0.73 | 0.07 | 200551.8 | 2.95 | skipped_fast |
| ZBCNUSDT | IDLE | 1.4 | 4.29 | 0.71 | 0.11 | 538062.16 | 21.26 | skipped_fast |
| QNTUSDT | IDLE | 2.42 | 8.56 | 4.02 | 0.1 | 182299.25 | 5.87 | skipped_fast |
| RIZEUSDT | IDLE | 1.84 | 7.71 | 4.55 | 0.09 | 58589.64 | 44.22 | skipped_fast |
| EDELUSDT | IDLE | 2.0 | 4.07 | 2.28 | -0.02 | 80245.03 | 33.31 | skipped_fast |
| REDUSDT | IDLE | 0.93 | 7.96 | 4.33 | 0.21 | 158188.89 | 11.92 | skipped_fast |
| KITEUSDT | IDLE | 1.72 | 6.49 | 0.05 | 0.15 | 68095.35 | 20.11 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | skipped_fast |
| RWAINCUSDT | IDLE | 1.99 | 3.6 | 2.53 | 0.01 | 9540.48 | 103.06 | skipped_fast |
| TELUSDT | IDLE | 1.97 | 5.52 | 0.74 | 0.1 | 183388.43 | 44.68 | skipped_fast |
| RWAUSDT | IDLE | 1.58 | 3.13 | 0.24 | 0.06 | 56535.27 | 15.99 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.08 | 3692.42 | 20.72 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
