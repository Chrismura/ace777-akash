# Hulk DIGEST — 2026-08-22T03:53:42Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.48 | 11.77 | 1.15 | 0.18 | 8823685.21 | 1.87 | skipped_fast |
| XRPUSDT | IDLE | 2.49 | 14.16 | 2.01 | 0.19 | 166005410.26 | 5.11 | skipped_fast |
| HBARUSDT | IDLE | 2.39 | 6.93 | 0.16 | 0.11 | 1034119.56 | 1.2 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.07 | 10.39 | 0.43 | 0.19 | 700879.79 | 10.78 | skipped_fast |
| CHIPUSDT | IDLE | 2.47 | 5.36 | 1.12 | -0.03 | 460108.96 | 5.95 | skipped_fast |
| BIOUSDT | IDLE | 3.01 | 7.36 | 2.34 | 0.07 | 199306.08 | 3.0 | skipped_fast |
| WUSDT | IDLE | 1.83 | 6.04 | 0.03 | 0.13 | 424578.57 | 7.84 | skipped_fast |
| ZBCNUSDT | IDLE | 1.44 | 5.37 | 1.12 | 0.13 | 537737.02 | 26.09 | skipped_fast |
| RIZEUSDT | IDLE | 1.81 | 7.71 | 4.18 | 0.11 | 59519.99 | 44.22 | skipped_fast |
| EDELUSDT | IDLE | 2.01 | 3.95 | 3.26 | -0.04 | 80684.79 | 44.99 | skipped_fast |
| REDUSDT | IDLE | 0.91 | 7.96 | 2.71 | 0.23 | 157551.96 | 11.68 | skipped_fast |
| KITEUSDT | IDLE | 1.55 | 5.3 | 0.21 | 0.13 | 67691.56 | 11.51 | skipped_fast |
| RWAINCUSDT | IDLE | 2.02 | 3.6 | 2.95 | 0.01 | 9351.15 | 54.47 | skipped_fast |
| QNTUSDT | IDLE | 1.87 | 4.68 | 0.47 | 0.09 | 178457.64 | 10.37 | skipped_fast |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3389.73 | 63.67 | skipped_fast |
| RWAUSDT | IDLE | 1.61 | 3.22 | 0.0 | 0.06 | 56274.01 | 8.01 | skipped_fast |
| TELUSDT | IDLE | 1.01 | 2.45 | 0.25 | 0.07 | 173914.33 | 56.14 | skipped_fast |
| FLUIDUSDT | IDLE | 1.06 | 2.64 | 2.03 | 0.07 | 4710.05 | 14.6 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
