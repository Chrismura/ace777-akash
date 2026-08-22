# Hulk DIGEST — 2026-08-22T16:17:42Z

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
| PYTHUSDT | IDLE | 1.5 | 7.24 | 1.17 | 0.05 | 51445805.87 | 1.97 | skipped_fast |
| XRPUSDT | IDLE | 1.37 | 7.64 | 5.16 | 0.04 | 215397259.36 | 4.13 | skipped_fast |
| HBARUSDT | IDLE | 0.84 | 3.03 | 1.81 | -0.01 | 1139799.33 | 5.2 | skipped_fast |
| CCUSDT | IDLE | 0.99 | 4.14 | 2.68 | 0.09 | 768995.19 | 9.42 | skipped_fast |
| CHIPUSDT | IDLE | 0.58 | 3.36 | 1.16 | -0.1 | 623715.23 | 6.72 | skipped_fast |
| WUSDT | IDLE | 0.65 | 2.58 | 1.69 | -0.02 | 545653.03 | 10.68 | skipped_fast |
| ZBCNUSDT | IDLE | 1.35 | 3.49 | 2.48 | -0.05 | 316053.56 | 19.65 | skipped_fast |
| BIOUSDT | IDLE | 0.97 | 6.58 | 4.7 | -0.07 | 219759.75 | 3.31 | skipped_fast |
| KITEUSDT | IDLE | 1.87 | 4.35 | 1.24 | 0.04 | 85484.43 | 12.43 | skipped_fast |
| EDELUSDT | IDLE | 1.44 | 2.52 | 2.35 | -0.03 | 74740.56 | 22.88 | skipped_fast |
| REDUSDT | IDLE | 0.52 | 5.67 | 4.28 | -0.12 | 133983.35 | 20.05 | skipped_fast |
| RIZEUSDT | IDLE | 1.33 | 3.23 | 0.27 | 0.03 | 56555.05 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.88 | 2.69 | 2.38 | -0.02 | 183839.84 | 1.58 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.01 | 8654.22 | 86.02 | skipped_fast |
| TELUSDT | IDLE | 0.96 | 2.37 | 1.47 | 0.0 | 137396.69 | 53.36 | skipped_fast |
| RWAUSDT | IDLE | 0.55 | 1.06 | 0.32 | 0.02 | 56298.36 | 8.11 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.03 | 4618.58 | 22.43 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
