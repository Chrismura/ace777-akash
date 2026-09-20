# Hulk DIGEST — 2026-09-20T12:02:13Z

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
| XRPUSDT | IDLE | 0.65 | 1.18 | 0.84 | -0.04 | 50402039.12 | 0.73 | skipped_fast |
| ETHUSDT | IDLE | 0.4 | 0.75 | 0.39 | -0.02 | 242700086.62 | 0.43 | skipped_fast |
| BTCUSDT | IDLE | 0.27 | 0.51 | 0.15 | -0.01 | 486910600.71 | 0.0 | skipped_fast |
| WUSDT | IDLE | 3.11 | 5.63 | 3.99 | -0.02 | 469565.35 | 6.46 | skipped_fast |
| PYTHUSDT | IDLE | 1.23 | 2.3 | 1.53 | -0.05 | 662170.35 | 1.73 | skipped_fast |
| HBARUSDT | IDLE | 1.61 | 3.05 | 1.09 | 0.01 | 772505.42 | 2.45 | skipped_fast |
| EDELUSDT | IDLE | 3.5 | 11.09 | 3.56 | -0.03 | 68541.7 | 92.17 | skipped_fast |
| REDUSDT | IDLE | 2.61 | 5.03 | 1.25 | 0.02 | 74286.54 | 2.63 | skipped_fast |
| CCUSDT | IDLE | 0.75 | 1.88 | 0.49 | -0.06 | 362736.49 | 4.79 | skipped_fast |
| ZBCNUSDT | IDLE | 0.95 | 2.87 | 2.5 | 0.03 | 230838.89 | 20.65 | skipped_fast |
| CHIPUSDT | IDLE | 1.41 | 2.64 | 2.36 | -0.09 | 97027.85 | 12.21 | skipped_fast |
| KITEUSDT | IDLE | 1.36 | 2.37 | 2.32 | -0.02 | 72620.68 | 24.14 | skipped_fast |
| BIOUSDT | IDLE | 1.12 | 2.03 | 1.36 | -0.05 | 83047.33 | 7.47 | skipped_fast |
| RWAINCUSDT | IDLE | 1.27 | 2.34 | 2.0 | -0.05 | 11238.36 | 35.95 | skipped_fast |
| RIZEUSDT | IDLE | 0.75 | 2.7 | 2.09 | -0.07 | 37566.35 | 68.98 | skipped_fast |
| QNTUSDT | IDLE | 0.86 | 1.58 | 0.87 | -0.02 | 55112.86 | 9.42 | skipped_fast |
| TELUSDT | IDLE | 1.04 | 2.0 | 0.54 | -0.05 | 101873.9 | 61.29 | skipped_fast |
| FLUIDUSDT | IDLE | 0.64 | 1.14 | 0.96 | -0.04 | 2114.93 | 21.98 | skipped_fast |
| MNSRYUSDT | IDLE | 0.49 | 0.85 | 0.83 | -0.02 | 34140.89 | 20.0 | skipped_fast |
| RWAUSDT | IDLE | 0.36 | 0.67 | 0.3 | -0.01 | 51773.18 | 37.19 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
