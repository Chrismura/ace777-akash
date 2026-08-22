# Hulk DIGEST — 2026-08-22T02:51:33Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.61 | 11.02 | 0.38 | 0.17 | 7295860.33 | 1.89 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.49 | 12.56 | 0.27 | 0.19 | 158007162.67 | 1.95 | skipped_fast |
| HBARUSDT | IDLE | 2.53 | 6.38 | 0.15 | 0.09 | 983803.89 | 7.34 | skipped_fast |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.07 | 9.41 | 0.06 | 0.18 | 657221.45 | 0.85 | skipped_fast |
| ZBCNUSDT | IDLE | 2.47 | 9.63 | 2.41 | 0.11 | 540364.99 | 31.82 | skipped_fast |
| CHIPUSDT | IDLE | 2.41 | 5.57 | 0.0 | -0.02 | 452369.96 | 2.98 | skipped_fast |
| BIOUSDT | IDLE | 3.2 | 8.18 | 2.05 | 0.09 | 194145.56 | 5.98 | skipped_fast |
| WUSDT | IDLE | 2.0 | 6.01 | 0.0 | 0.11 | 415109.8 | 10.91 | skipped_fast |
| EDELUSDT | IDLE | 2.45 | 5.02 | 2.61 | -0.03 | 79879.02 | 22.27 | skipped_fast |
| RIZEUSDT | IDLE | 1.99 | 8.52 | 4.44 | 0.1 | 61365.66 | 44.22 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 8.27 | 4.88 | 0.19 | 157814.28 | 10.39 | skipped_fast |
| RWAINCUSDT | IDLE | 1.83 | 3.27 | 2.58 | 0.0 | 9400.35 | 5.43 | skipped_fast |
| QNTUSDT | IDLE | 2.34 | 5.48 | 0.22 | 0.09 | 172529.35 | 2.98 | skipped_fast |
| KITEUSDT | IDLE | 1.33 | 4.09 | 0.34 | 0.12 | 62446.28 | 13.46 | skipped_fast |
| TELUSDT | IDLE | 2.14 | 5.11 | 1.02 | 0.06 | 174237.7 | 31.01 | skipped_fast |
| QAITUSDT | IDLE | 1.88 | 3.57 | 1.22 | 0.0 | 3930.15 | 63.67 | skipped_fast |
| RWAUSDT | IDLE | 1.51 | 3.0 | 0.16 | 0.05 | 55925.56 | 24.32 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 21.04 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
