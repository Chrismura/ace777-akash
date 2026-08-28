# Hulk DIGEST — 2026-08-28T14:08:37Z

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
| XRPUSDT | IDLE | 1.56 | 2.77 | 2.34 | -0.03 | 49760717.44 | 4.29 | skipped_fast |
| PYTHUSDT | IDLE | 1.95 | 3.93 | 3.37 | -0.04 | 1210155.22 | 4.25 | skipped_fast |
| CHIPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.37 | 12.74 | 1.83 | 0.13 | 977535.55 | 8.95 | skipped_fast |
| CCUSDT | IDLE | 1.42 | 2.51 | 2.25 | -0.05 | 405360.61 | 9.0 | skipped_fast |
| ZBCNUSDT | IDLE | 2.05 | 4.26 | 2.69 | 0.0 | 242605.58 | 34.83 | skipped_fast |
| WUSDT | IDLE | 1.69 | 2.96 | 2.83 | -0.04 | 198025.76 | 14.02 | skipped_fast |
| QAITUSDT | IDLE | 2.46 | 32.58 | 23.47 | -0.18 | 64699.51 | 396.87 | skipped_fast |
| REDUSDT | IDLE | 1.49 | 2.74 | 1.54 | -0.03 | 73434.72 | 11.2 | skipped_fast |
| RIZEUSDT | IDLE | 1.42 | 7.12 | 1.35 | -0.09 | 102922.1 | 56.88 | skipped_fast |
| KITEUSDT | IDLE | 1.36 | 2.38 | 2.23 | -0.02 | 74556.61 | 11.99 | skipped_fast |
| BIOUSDT | IDLE | 1.06 | 1.85 | 1.75 | -0.04 | 83635.45 | 10.64 | skipped_fast |
| HBARUSDT | IDLE | 1.12 | 1.98 | 1.76 | -0.03 | 308801.35 | 3.91 | skipped_fast |
| FLUIDUSDT | IDLE | 2.13 | 3.73 | 3.59 | -0.05 | 4525.97 | 22.0 | skipped_fast |
| EDELUSDT | IDLE | 0.56 | 2.43 | 2.38 | -0.08 | 56188.13 | 26.05 | skipped_fast |
| TELUSDT | IDLE | 1.28 | 2.91 | 1.9 | -0.01 | 133850.77 | 5.53 | skipped_fast |
| RWAINCUSDT | IDLE | 1.25 | 4.22 | 1.07 | 0.01 | 19055.28 | 102.51 | skipped_fast |
| QNTUSDT | IDLE | 1.61 | 2.82 | 2.7 | -0.01 | 47235.72 | 6.48 | skipped_fast |
| RWAUSDT | IDLE | 1.09 | 2.11 | 0.41 | 0.01 | 53737.74 | 58.12 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
