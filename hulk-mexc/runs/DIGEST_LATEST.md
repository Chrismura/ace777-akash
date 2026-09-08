# Hulk DIGEST — 2026-09-08T08:39:24Z

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
| XRPUSDT | IDLE | 0.64 | 1.2 | 0.49 | -0.01 | 31080467.64 | 2.88 | skipped_fast |
| BTCUSDT | IDLE | 0.57 | 1.04 | 0.6 | -0.01 | 600201095.39 | 0.0 | skipped_fast |
| ETHUSDT | IDLE | 0.52 | 1.0 | 0.3 | -0.0 | 290521638.33 | 0.04 | skipped_fast |
| CCUSDT | IDLE | 1.85 | 3.28 | 2.76 | -0.04 | 435228.39 | 4.78 | skipped_fast |
| CHIPUSDT | IDLE | 2.22 | 5.06 | 4.42 | -0.06 | 117559.88 | 13.83 | skipped_fast |
| HBARUSDT | IDLE | 1.58 | 2.84 | 2.07 | -0.01 | 554196.1 | 1.25 | skipped_fast |
| PYTHUSDT | IDLE | 1.0 | 1.84 | 1.01 | -0.03 | 382289.27 | 1.86 | skipped_fast |
| RIZEUSDT | IDLE | 2.4 | 6.43 | 5.66 | -0.08 | 49270.98 | 67.24 | skipped_fast |
| ZBCNUSDT | IDLE | 1.22 | 3.17 | 2.37 | -0.05 | 212081.95 | 25.62 | skipped_fast |
| REDUSDT | IDLE | 1.58 | 3.12 | 0.21 | 0.04 | 57186.67 | 12.03 | skipped_fast |
| WUSDT | IDLE | 0.87 | 1.68 | 0.43 | -0.0 | 195550.51 | 12.6 | skipped_fast |
| RWAINCUSDT | IDLE | 1.96 | 7.39 | 5.79 | -0.1 | 5168.41 | 104.89 | skipped_fast |
| KITEUSDT | IDLE | 0.98 | 1.8 | 1.1 | -0.04 | 64248.04 | 13.44 | skipped_fast |
| EDELUSDT | IDLE | 1.1 | 2.39 | 0.97 | -0.02 | 87652.16 | 48.8 | skipped_fast |
| BIOUSDT | IDLE | 0.76 | 1.48 | 0.29 | 0.01 | 66708.43 | 7.32 | skipped_fast |
| TELUSDT | IDLE | 1.08 | 2.09 | 0.53 | -0.01 | 79417.97 | 47.09 | skipped_fast |
| RWAUSDT | IDLE | 0.91 | 1.75 | 0.5 | 0.01 | 54238.59 | 21.57 | skipped_fast |
| QNTUSDT | IDLE | 0.72 | 1.43 | 0.06 | 0.01 | 57947.93 | 9.03 | skipped_fast |
| MNSRYUSDT | IDLE | 0.27 | 0.53 | 0.05 | -0.01 | 35484.86 | 36.73 | skipped_fast |
| FLUIDUSDT | IDLE | 0.17 | 0.3 | 0.29 | 0.01 | 733.81 | 21.82 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
