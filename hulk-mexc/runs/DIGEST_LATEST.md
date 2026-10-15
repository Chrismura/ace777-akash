# Hulk DIGEST — 2026-10-15T15:14:19Z

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
| PYTHUSDT | IDLE | 3.45 | 16.32 | 2.89 | 0.11 | 3243327.04 | 7.68 | skipped_fast |
| WUSDT | IDLE | 2.12 | 6.64 | 0.19 | -0.02 | 2650449.81 | 16.11 | skipped_fast |
| ETHUSDT | IDLE | 2.25 | 4.45 | 0.3 | -0.0 | 330112137.01 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 2.06 | 4.09 | 0.17 | 0.0 | 54910031.85 | 1.5 | skipped_fast |
| BTCUSDT | IDLE | 1.58 | 3.14 | 0.12 | 0.01 | 494220937.27 | 0.03 | skipped_fast |
| QNTUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.54 | 9.55 | 0.05 | 0.04 | 1116115.16 | 9.03 | skipped_fast |
| REDUSDT | IDLE | 3.09 | 7.63 | 0.25 | 0.03 | 72793.22 | 14.09 | skipped_fast |
| CCUSDT | IDLE | 1.23 | 4.07 | 0.57 | -0.07 | 432361.97 | 10.09 | skipped_fast |
| CHIPUSDT | IDLE | 1.72 | 11.93 | 0.74 | -0.14 | 167425.12 | 10.58 | skipped_fast |
| BIOUSDT | IDLE | 2.1 | 5.8 | 0.47 | -0.03 | 88939.68 | 7.81 | skipped_fast |
| ZBCNUSDT | IDLE | 1.77 | 3.53 | 0.02 | -0.0 | 199656.27 | 12.36 | skipped_fast |
| RWAINCUSDT | IDLE | 2.28 | 7.49 | 1.05 | 0.1 | 26823.03 | 33.76 | skipped_fast |
| KITEUSDT | IDLE | 1.91 | 6.14 | 0.11 | -0.04 | 58621.17 | 12.07 | skipped_fast |
| HBARUSDT | IDLE | 1.83 | 3.65 | 0.05 | -0.01 | 375253.39 | 3.6 | skipped_fast |
| EDELUSDT | IDLE | 1.28 | 4.62 | 0.0 | -0.07 | 239781.42 | 41.85 | skipped_fast |
| RIZEUSDT | IDLE | 1.45 | 5.51 | 2.97 | 0.01 | 73994.71 | 56.93 | skipped_fast |
| TELUSDT | IDLE | 2.34 | 5.77 | 0.0 | 0.01 | 96812.96 | 34.11 | skipped_fast |
| MNSRYUSDT | IDLE | 1.46 | 2.77 | 1.03 | -0.0 | 31214.55 | 46.46 | skipped_fast |
| FLUIDUSDT | IDLE | 1.12 | 4.38 | 0.18 | -0.0 | 17219.27 | 21.04 | skipped_fast |
| RWAUSDT | IDLE | 0.91 | 1.78 | 0.32 | -0.01 | 55269.65 | 7.97 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
