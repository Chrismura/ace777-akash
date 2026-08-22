# Hulk DIGEST — 2026-08-22T02:42:37Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.59 | 10.52 | 0.76 | 0.16 | 7177509.32 | 1.91 | skipped_fast |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.45 | 12.02 | 0.25 | 0.18 | 156783664.93 | 3.91 | skipped_fast |
| HBARUSDT | IDLE | 2.43 | 5.79 | 0.0 | 0.09 | 979276.26 | 1.23 | skipped_fast |
| ZBCNUSDT | IDLE | 2.46 | 9.63 | 2.07 | 0.1 | 541123.61 | 31.74 | skipped_fast |
| CCUSDT | IDLE | 1.84 | 7.35 | 0.0 | 0.15 | 656186.87 | 5.16 | skipped_fast |
| CHIPUSDT | IDLE | 2.29 | 5.26 | 0.27 | -0.02 | 458928.29 | 3.0 | skipped_fast |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.15 | 8.18 | 1.14 | 0.1 | 193237.58 | 14.82 | skipped_fast |
| WUSDT | IDLE | 1.96 | 5.73 | 0.05 | 0.1 | 411758.97 | 10.95 | skipped_fast |
| EDELUSDT | IDLE | 2.47 | 5.02 | 2.93 | -0.04 | 79818.34 | 56.15 | skipped_fast |
| RIZEUSDT | IDLE | 1.98 | 8.52 | 4.15 | 0.1 | 61302.78 | 45.81 | skipped_fast |
| REDUSDT | IDLE | 0.98 | 8.27 | 4.9 | 0.19 | 158146.12 | 11.19 | skipped_fast |
| QNTUSDT | IDLE | 2.34 | 5.48 | 0.3 | 0.08 | 172678.28 | 8.94 | skipped_fast |
| RWAINCUSDT | IDLE | 1.83 | 3.27 | 2.58 | 0.02 | 9400.35 | 21.69 | skipped_fast |
| KITEUSDT | IDLE | 1.33 | 4.09 | 0.28 | 0.12 | 62448.95 | 11.66 | skipped_fast |
| QAITUSDT | IDLE | 1.88 | 3.57 | 1.22 | 0.0 | 3930.15 | 63.67 | skipped_fast |
| TELUSDT | IDLE | 2.14 | 5.11 | 1.02 | 0.06 | 174197.06 | 56.95 | skipped_fast |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 22.43 | skipped_fast |
| RWAUSDT | IDLE | 1.15 | 2.25 | 0.33 | 0.04 | 55582.75 | 16.35 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
