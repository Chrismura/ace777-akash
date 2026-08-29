# Hulk DIGEST — 2026-08-29T03:09:32Z

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
| XRPUSDT | IDLE | 0.71 | 1.35 | 0.45 | -0.03 | 45663134.5 | 2.89 | skipped_fast |
| CHIPUSDT | IDLE | 1.1 | 6.52 | 1.64 | 0.11 | 1165342.84 | 2.38 | skipped_fast |
| QAITUSDT | IDLE | 2.09 | 27.75 | 19.59 | -0.01 | 97605.85 | 35.61 | skipped_fast |
| PYTHUSDT | IDLE | 1.52 | 3.01 | 0.23 | -0.02 | 559697.29 | 6.27 | skipped_fast |
| RIZEUSDT | IDLE | 2.49 | 6.36 | 3.01 | -0.06 | 35209.06 | 41.15 | skipped_fast |
| CCUSDT | IDLE | 1.03 | 1.88 | 1.17 | -0.01 | 258716.45 | 7.22 | skipped_fast |
| EDELUSDT | IDLE | 1.46 | 5.81 | 2.14 | -0.11 | 92602.25 | 37.99 | skipped_fast |
| WUSDT | IDLE | 0.78 | 1.52 | 0.26 | -0.03 | 210963.68 | 9.82 | skipped_fast |
| KITEUSDT | IDLE | 1.35 | 2.64 | 0.42 | 0.01 | 77890.74 | 11.66 | skipped_fast |
| HBARUSDT | IDLE | 0.67 | 1.23 | 0.79 | -0.03 | 465929.9 | 1.32 | skipped_fast |
| ZBCNUSDT | IDLE | 0.64 | 1.76 | 0.3 | -0.06 | 173463.49 | 10.19 | skipped_fast |
| BIOUSDT | IDLE | 0.68 | 1.3 | 0.43 | -0.02 | 83411.64 | 3.59 | skipped_fast |
| REDUSDT | IDLE | 0.76 | 1.81 | 0.57 | -0.03 | 61051.49 | 12.04 | skipped_fast |
| RWAINCUSDT | IDLE | 1.14 | 2.28 | 0.0 | -0.02 | 3438.94 | 54.82 | skipped_fast |
| TELUSDT | IDLE | 1.51 | 3.12 | 1.07 | -0.07 | 98969.9 | 45.38 | skipped_fast |
| FLUIDUSDT | IDLE | 0.92 | 1.61 | 1.58 | -0.04 | 3732.19 | 21.64 | skipped_fast |
| QNTUSDT | IDLE | 0.65 | 1.28 | 0.19 | -0.01 | 41931.93 | 6.51 | skipped_fast |
| RWAUSDT | IDLE | 0.47 | 0.92 | 0.16 | -0.0 | 53921.07 | 16.52 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
