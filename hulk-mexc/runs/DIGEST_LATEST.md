# Hulk DIGEST — 2026-09-15T13:45:51Z

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
| XRPUSDT | IDLE | 2.93 | 5.35 | 3.34 | 0.01 | 79185141.64 | 2.13 | skipped_fast |
| ETHUSDT | IDLE | 1.2 | 2.2 | 1.38 | -0.02 | 470743957.57 | 0.86 | skipped_fast |
| BTCUSDT | IDLE | 0.79 | 1.44 | 0.94 | -0.02 | 557708564.83 | 0.0 | skipped_fast |
| EDELUSDT | IDLE | 1.45 | 19.89 | 6.44 | 0.41 | 447956.31 | 9.91 | skipped_fast |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.44 | 7.71 | 6.55 | -0.06 | 87316.15 | 10.28 | skipped_fast |
| ZBCNUSDT | IDLE | 2.54 | 4.56 | 3.5 | 0.01 | 211725.17 | 3.89 | skipped_fast |
| HBARUSDT | IDLE | 2.5 | 4.71 | 1.94 | 0.02 | 400547.08 | 2.55 | skipped_fast |
| RIZEUSDT | IDLE | 2.18 | 21.18 | 4.35 | 0.02 | 53924.81 | 95.47 | skipped_fast |
| CCUSDT | IDLE | 0.96 | 1.67 | 1.64 | -0.02 | 356898.57 | 8.48 | skipped_fast |
| PYTHUSDT | IDLE | 1.09 | 2.0 | 1.23 | -0.02 | 272286.81 | 3.71 | skipped_fast |
| RWAINCUSDT | IDLE | 1.67 | 2.91 | 2.82 | -0.01 | 8084.06 | 5.61 | skipped_fast |
| REDUSDT | IDLE | 1.03 | 5.46 | 2.01 | -0.03 | 112693.43 | 16.67 | skipped_fast |
| WUSDT | IDLE | 1.03 | 1.87 | 1.29 | -0.03 | 142999.22 | 7.31 | skipped_fast |
| BIOUSDT | IDLE | 0.91 | 1.69 | 0.83 | -0.01 | 86748.72 | 11.95 | skipped_fast |
| KITEUSDT | IDLE | 0.9 | 1.65 | 1.04 | 0.0 | 61200.15 | 12.25 | skipped_fast |
| TELUSDT | IDLE | 1.34 | 3.78 | 3.46 | -0.04 | 93350.71 | 39.06 | skipped_fast |
| FLUIDUSDT | IDLE | 1.5 | 2.64 | 2.37 | -0.04 | 2129.45 | 19.34 | skipped_fast |
| QNTUSDT | IDLE | 0.87 | 1.55 | 1.31 | -0.03 | 43700.22 | 11.2 | skipped_fast |
| RWAUSDT | IDLE | 0.52 | 0.98 | 0.45 | -0.01 | 52389.24 | 14.97 | skipped_fast |
| MNSRYUSDT | IDLE | 0.28 | 0.53 | 0.14 | 0.01 | 32718.67 | 24.98 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
