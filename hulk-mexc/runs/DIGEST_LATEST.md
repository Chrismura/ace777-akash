# Hulk DIGEST — 2026-08-21T06:29:23Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.76 | 9.1 | 0.89 | 0.12 | 2327629.22 | 10.47 | skipped_fast |
| XRPUSDT | IDLE | 0.88 | 4.54 | 1.17 | 0.18 | 119646303.91 | 1.53 | skipped_fast |
| CCUSDT | IDLE | 2.15 | 4.27 | 0.2 | 0.01 | 490223.51 | 7.82 | skipped_fast |
| CHIPUSDT | IDLE | 1.56 | 9.09 | 4.76 | 0.12 | 463851.58 | 6.06 | skipped_fast |
| ZBCNUSDT | IDLE | 1.87 | 7.31 | 0.26 | 0.11 | 294124.53 | 19.89 | skipped_fast |
| BIOUSDT | IDLE | 1.65 | 5.07 | 1.44 | 0.05 | 227506.81 | 3.18 | skipped_fast |
| EDELUSDT | IDLE | 2.02 | 3.61 | 2.85 | 0.01 | 75657.11 | 21.76 | skipped_fast |
| WUSDT | IDLE | 1.02 | 1.96 | 0.51 | 0.06 | 270529.9 | 15.39 | skipped_fast |
| HBARUSDT | IDLE | 1.21 | 2.36 | 0.45 | 0.05 | 493155.76 | 2.66 | skipped_fast |
| REDUSDT | IDLE | 1.27 | 4.77 | 2.39 | -0.12 | 135447.33 | 26.58 | skipped_fast |
| RWAINCUSDT | IDLE | 1.4 | 2.67 | 0.87 | 0.03 | 8575.28 | 21.83 | skipped_fast |
| KITEUSDT | IDLE | 0.84 | 1.67 | 0.12 | 0.05 | 60970.81 | 15.96 | skipped_fast |
| QAITUSDT | IDLE | 0.9 | 2.36 | 0.04 | -0.03 | 5673.22 | 67.05 | skipped_fast |
| TELUSDT | IDLE | 0.53 | 2.7 | 1.23 | 0.14 | 202404.52 | 27.15 | skipped_fast |
| RIZEUSDT | IDLE | 0.64 | 3.01 | 1.55 | -0.09 | 38578.36 | 120.03 | skipped_fast |
| QNTUSDT | IDLE | 0.69 | 1.38 | 0.05 | 0.06 | 67939.93 | 4.81 | skipped_fast |
| FLUIDUSDT | IDLE | 0.77 | 1.6 | 1.11 | 0.08 | 2710.67 | 21.65 | skipped_fast |
| RWAUSDT | IDLE | 0.49 | 0.94 | 0.25 | 0.02 | 54678.13 | 33.9 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
