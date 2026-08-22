# Hulk DIGEST — 2026-08-22T16:26:53Z

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
| PYTHUSDT | IDLE | 1.47 | 7.24 | 0.12 | 0.07 | 51438825.72 | 1.95 | skipped_fast |
| XRPUSDT | IDLE | 1.33 | 7.64 | 3.81 | 0.05 | 215667184.05 | 3.4 | skipped_fast |
| HBARUSDT | IDLE | 0.81 | 3.03 | 1.18 | -0.0 | 1130684.71 | 5.17 | skipped_fast |
| CCUSDT | IDLE | 0.99 | 4.14 | 2.64 | 0.08 | 762619.58 | 5.14 | skipped_fast |
| CHIPUSDT | IDLE | 0.57 | 3.36 | 0.86 | -0.1 | 627550.31 | 3.35 | skipped_fast |
| WUSDT | IDLE | 0.62 | 2.58 | 0.94 | -0.01 | 544229.47 | 12.72 | skipped_fast |
| ZBCNUSDT | IDLE | 1.28 | 3.49 | 1.28 | -0.03 | 316185.27 | 14.3 | skipped_fast |
| BIOUSDT | IDLE | 0.96 | 6.58 | 4.25 | -0.06 | 219727.23 | 3.29 | skipped_fast |
| KITEUSDT | IDLE | 1.88 | 4.35 | 1.36 | 0.03 | 85361.58 | 13.36 | skipped_fast |
| EDELUSDT | IDLE | 1.42 | 2.52 | 2.13 | -0.03 | 74831.17 | 22.86 | skipped_fast |
| REDUSDT | IDLE | 0.52 | 5.67 | 4.08 | -0.13 | 133003.47 | 14.62 | skipped_fast |
| RIZEUSDT | IDLE | 1.32 | 3.23 | 0.15 | 0.03 | 56582.58 | 45.5 | skipped_fast |
| QAITUSDT | IDLE | 1.67 | 3.19 | 0.94 | 0.01 | 2320.37 | 67.45 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 2.69 | 2.08 | -0.02 | 183928.43 | 7.88 | skipped_fast |
| RWAINCUSDT | IDLE | 0.77 | 1.53 | 0.0 | 0.02 | 8619.61 | 64.45 | skipped_fast |
| TELUSDT | IDLE | 0.95 | 2.37 | 1.16 | 0.01 | 137778.43 | 42.55 | skipped_fast |
| RWAUSDT | IDLE | 0.54 | 1.06 | 0.16 | 0.02 | 56366.85 | 8.1 | skipped_fast |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.03 | 4618.58 | 21.64 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
