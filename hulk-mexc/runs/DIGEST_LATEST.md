# Hulk DIGEST — 2026-08-21T21:31:46Z

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
| PYTHUSDT | IDLE | 1.18 | 4.51 | 0.88 | 0.1 | 5635847.17 | 2.07 | skipped_fast |
| XRPUSDT | IDLE | 1.12 | 3.73 | 1.31 | 0.11 | 129125939.77 | 2.15 | skipped_fast |
| CHIPUSDT | IDLE | 1.89 | 5.61 | 3.97 | 0.05 | 517463.38 | 6.21 | skipped_fast |
| ZBCNUSDT | IDLE | 1.97 | 8.19 | 4.28 | 0.1 | 486472.97 | 35.38 | skipped_fast |
| CCUSDT | IDLE | 1.13 | 3.17 | 0.04 | 0.1 | 644869.4 | 7.34 | skipped_fast |
| HBARUSDT | IDLE | 1.54 | 3.04 | 0.28 | 0.07 | 815015.38 | 1.28 | skipped_fast |
| WUSDT | IDLE | 1.93 | 3.83 | 0.25 | 0.07 | 367589.18 | 14.61 | skipped_fast |
| BIOUSDT | IDLE | 2.42 | 5.2 | 2.03 | 0.02 | 186914.66 | 3.14 | skipped_fast |
| REDUSDT | IDLE | 1.34 | 11.01 | 9.23 | 0.17 | 154003.75 | 10.64 | skipped_fast |
| EDELUSDT | IDLE | 2.0 | 4.12 | 1.98 | -0.05 | 83420.25 | 22.42 | skipped_fast |
| RIZEUSDT | IDLE | 1.87 | 9.54 | 1.47 | 0.02 | 56018.01 | 45.77 | skipped_fast |
| RWAINCUSDT | IDLE | 2.29 | 4.3 | 1.85 | 0.03 | 10171.16 | 59.35 | skipped_fast |
| KITEUSDT | IDLE | 1.29 | 4.0 | 1.54 | 0.12 | 61055.18 | 9.22 | skipped_fast |
| QAITUSDT | IDLE | 2.33 | 4.38 | 1.83 | -0.01 | 3809.29 | 135.62 | skipped_fast |
| TELUSDT | IDLE | 1.9 | 4.81 | 0.83 | 0.03 | 182654.76 | 89.31 | skipped_fast |
| QNTUSDT | IDLE | 1.41 | 2.65 | 1.12 | 0.04 | 63258.89 | 10.87 | skipped_fast |
| RWAUSDT | IDLE | 0.62 | 1.17 | 0.49 | 0.03 | 53872.92 | 8.27 | skipped_fast |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.09 | 0.09 | 4171.26 | 20.58 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
