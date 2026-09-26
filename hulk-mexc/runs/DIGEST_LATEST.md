# Hulk DIGEST — 2026-09-26T11:55:34Z

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
| XRPUSDT | IDLE | 0.69 | 1.3 | 0.57 | -0.03 | 93406468.61 | 1.94 | skipped_fast |
| ETHUSDT | IDLE | 0.35 | 0.66 | 0.3 | -0.01 | 227935419.03 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.27 | 0.51 | 0.17 | -0.01 | 502361796.38 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.27 | 6.5 | 0.17 | 0.09 | 1152594.31 | 1.28 | skipped_fast |
| CCUSDT | IDLE | 1.49 | 5.09 | 3.72 | 0.09 | 989322.19 | 9.68 | skipped_fast |
| QNTUSDT | IDLE | 2.41 | 10.52 | 4.75 | 0.07 | 773347.93 | 5.73 | skipped_fast |
| WUSDT | IDLE | 2.17 | 5.85 | 0.86 | 0.07 | 487043.21 | 8.53 | skipped_fast |
| EDELUSDT | IDLE | 2.66 | 5.11 | 1.39 | 0.03 | 177690.43 | 9.86 | skipped_fast |
| HBARUSDT | IDLE | 0.79 | 1.5 | 0.54 | -0.01 | 722126.2 | 1.06 | skipped_fast |
| RWAINCUSDT | IDLE | 2.59 | 4.93 | 3.75 | 0.03 | 5741.99 | 19.86 | skipped_fast |
| ZBCNUSDT | IDLE | 1.26 | 2.52 | 0.02 | -0.02 | 227587.66 | 14.47 | skipped_fast |
| CHIPUSDT | IDLE | 1.57 | 2.89 | 1.64 | 0.0 | 138318.56 | 18.48 | skipped_fast |
| BIOUSDT | IDLE | 1.43 | 3.25 | 1.68 | 0.04 | 125477.81 | 6.09 | skipped_fast |
| RIZEUSDT | IDLE | 1.28 | 9.26 | 3.84 | -0.17 | 49717.59 | 77.12 | skipped_fast |
| KITEUSDT | IDLE | 1.01 | 2.24 | 1.15 | 0.04 | 74471.32 | 9.59 | skipped_fast |
| REDUSDT | IDLE | 1.07 | 1.87 | 1.76 | -0.01 | 58948.31 | 14.19 | skipped_fast |
| RWAUSDT | IDLE | 2.34 | 4.31 | 2.42 | 0.0 | 55632.19 | 21.91 | skipped_fast |
| TELUSDT | IDLE | 1.32 | 2.32 | 2.08 | -0.05 | 120817.53 | 50.06 | skipped_fast |
| FLUIDUSDT | IDLE | 1.53 | 3.07 | 0.0 | 0.0 | 3424.92 | 20.61 | skipped_fast |
| MNSRYUSDT | IDLE | 0.04 | 0.08 | 0.01 | 0.0 | 38901.67 | 8.92 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
