# Hulk DIGEST — 2026-10-13T06:55:46Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 3.09 | 12.26 | 2.33 | 0.07 | 3797164.58 | 3.48 | skipped_fast |
| WUSDT | IDLE | 0.68 | 11.65 | 4.86 | -0.34 | 10540960.6 | 16.42 | skipped_fast |
| ETHUSDT | IDLE | 2.42 | 4.82 | 0.07 | -0.01 | 264987590.14 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 2.16 | 4.38 | 0.01 | -0.02 | 35456215.69 | 0.73 | skipped_fast |
| BTCUSDT | IDLE | 1.52 | 3.02 | 0.15 | -0.0 | 375132681.96 | 0.0 | skipped_fast |
| CCUSDT | IDLE | 2.93 | 6.66 | 0.34 | -0.02 | 406188.81 | 10.43 | skipped_fast |
| QNTUSDT | IDLE | 1.7 | 4.41 | 1.15 | -0.05 | 920386.61 | 7.86 | skipped_fast |
| ZBCNUSDT | IDLE | 2.11 | 4.15 | 0.45 | -0.02 | 220950.65 | 9.82 | skipped_fast |
| KITEUSDT | IDLE | 2.56 | 7.42 | 0.18 | 0.01 | 66184.94 | 8.54 | skipped_fast |
| BIOUSDT | IDLE | 2.22 | 7.89 | 0.88 | -0.05 | 75136.22 | 3.55 | skipped_fast |
| REDUSDT | IDLE | 1.03 | 7.52 | 0.88 | -0.01 | 312613.84 | 14.53 | skipped_fast |
| HBARUSDT | IDLE | 1.41 | 4.24 | 0.57 | -0.07 | 550626.8 | 2.27 | skipped_fast |
| CHIPUSDT | IDLE | 1.71 | 7.75 | 0.1 | -0.05 | 146570.3 | 14.9 | skipped_fast |
| FLUIDUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.8 | 8.59 | 0.0 | 0.07 | 13936.54 | 19.47 | skipped_fast |
| EDELUSDT | IDLE | 0.91 | 3.88 | 1.14 | -0.12 | 279492.14 | 24.15 | skipped_fast |
| RWAINCUSDT | IDLE | 1.76 | 5.01 | 0.43 | 0.04 | 40718.49 | 9.71 | skipped_fast |
| TELUSDT | IDLE | 2.47 | 4.81 | 0.84 | 0.03 | 112361.26 | 28.21 | skipped_fast |
| RIZEUSDT | IDLE | 0.47 | 3.02 | 0.44 | -0.12 | 67278.76 | 35.5 | skipped_fast |
| RWAUSDT | IDLE | 0.87 | 1.72 | 0.15 | 0.0 | 53468.14 | 15.42 | skipped_fast |
| MNSRYUSDT | IDLE | 1.01 | 1.97 | 0.39 | -0.01 | 39996.16 | 55.29 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
