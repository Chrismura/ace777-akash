# Hulk DIGEST — 2026-08-22T02:30:58Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.59 | 10.52 | 0.89 | 0.16 | 7048223.99 | 22.99 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.34 | 10.72 | 0.09 | 0.17 | 155074386.91 | 3.95 | skipped_fast |
| HBARUSDT | IDLE | 2.37 | 5.4 | 0.06 | 0.09 | 968132.65 | 1.23 | skipped_fast |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.44 | 9.63 | 1.62 | 0.11 | 545261.53 | 31.09 | skipped_fast |
| CCUSDT | IDLE | 1.72 | 6.45 | 0.07 | 0.15 | 652251.86 | 2.6 | skipped_fast |
| CHIPUSDT | IDLE | 2.21 | 5.07 | 0.27 | -0.02 | 469706.35 | 3.01 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.12 | 8.18 | 0.67 | 0.1 | 193216.04 | 5.9 | skipped_fast |
| WUSDT | IDLE | 1.91 | 5.4 | 0.1 | 0.1 | 405847.27 | 5.99 | skipped_fast |
| EDELUSDT | IDLE | 2.49 | 5.02 | 3.15 | -0.04 | 79698.01 | 22.37 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.07 | 0.1 | 61379.83 | 45.71 | skipped_fast |
| REDUSDT | IDLE | 1.0 | 8.27 | 6.29 | 0.17 | 157908.47 | 9.74 | skipped_fast |
| QNTUSDT | IDLE | 2.25 | 5.06 | 0.0 | 0.08 | 171079.71 | 1.49 | skipped_fast |
| KITEUSDT | IDLE | 1.33 | 4.09 | 0.36 | 0.12 | 61899.64 | 8.96 | skipped_fast |
| RWAINCUSDT | IDLE | 1.83 | 3.27 | 2.58 | 0.01 | 9358.7 | 37.95 | skipped_fast |
| QAITUSDT | IDLE | 1.88 | 3.57 | 1.22 | 0.0 | 3930.15 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 2.14 | 5.11 | 0.97 | 0.05 | 178679.7 | 56.92 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 21.73 | skipped_fast |
| RWAUSDT | IDLE | 1.1 | 2.17 | 0.24 | 0.04 | 55009.38 | 32.68 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
