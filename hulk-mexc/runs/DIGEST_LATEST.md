# Hulk DIGEST — 2026-09-19T22:59:41Z

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
| XRPUSDT | IDLE | 1.84 | 3.38 | 1.94 | 0.01 | 58576349.03 | 0.71 | skipped_fast |
| ETHUSDT | IDLE | 1.08 | 1.94 | 1.43 | 0.0 | 247342361.98 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.64 | 1.16 | 0.74 | 0.0 | 446866575.52 | 0.0 | skipped_fast |
| WUSDT | IDLE | 1.98 | 3.73 | 1.51 | 0.01 | 542796.44 | 8.16 | skipped_fast |
| PYTHUSDT | IDLE | 1.39 | 2.57 | 1.37 | 0.01 | 639555.1 | 1.65 | skipped_fast |
| CCUSDT | IDLE | 2.39 | 4.22 | 3.67 | -0.03 | 334619.01 | 6.41 | skipped_fast |
| HBARUSDT | IDLE | 1.53 | 2.88 | 1.25 | 0.03 | 632087.84 | 1.23 | skipped_fast |
| EDELUSDT | IDLE | 2.11 | 6.6 | 3.1 | -0.08 | 137652.74 | 19.37 | skipped_fast |
| BIOUSDT | IDLE | 1.82 | 3.36 | 1.85 | 0.03 | 88347.43 | 3.56 | skipped_fast |
| ZBCNUSDT | IDLE | 1.23 | 4.9 | 1.66 | 0.11 | 221527.9 | 31.72 | skipped_fast |
| RWAINCUSDT | IDLE | 2.32 | 5.19 | 3.62 | -0.04 | 6959.75 | 77.04 | skipped_fast |
| KITEUSDT | IDLE | 1.44 | 2.68 | 1.33 | 0.03 | 77010.87 | 12.22 | skipped_fast |
| CHIPUSDT | IDLE | 1.16 | 3.49 | 0.36 | -0.03 | 130793.71 | 16.01 | skipped_fast |
| REDUSDT | IDLE | 0.44 | 2.06 | 0.1 | 0.03 | 136662.94 | 14.01 | skipped_fast |
| TELUSDT | IDLE | 1.48 | 3.5 | 3.12 | -0.08 | 104695.31 | 26.83 | skipped_fast |
| FLUIDUSDT | IDLE | 1.72 | 3.09 | 2.3 | 0.04 | 9383.62 | 21.12 | skipped_fast |
| QNTUSDT | IDLE | 1.36 | 2.53 | 1.32 | 0.04 | 59212.03 | 6.1 | skipped_fast |
| RWAUSDT | IDLE | 0.83 | 1.48 | 1.24 | 0.01 | 53172.93 | 14.73 | skipped_fast |
| RIZEUSDT | IDLE | 0.85 | 3.49 | 1.94 | 0.02 | 38201.72 | 264.16 | skipped_fast |
| MNSRYUSDT | IDLE | 0.34 | 0.63 | 0.38 | -0.01 | 34564.96 | 49.02 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
