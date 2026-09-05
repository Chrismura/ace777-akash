# Hulk DIGEST — 2026-09-05T13:28:25Z

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
| XRPUSDT | IDLE | 0.67 | 1.32 | 0.1 | 0.0 | 27714264.71 | 2.12 | skipped_fast |
| ETHUSDT | IDLE | 0.19 | 0.37 | 0.08 | 0.0 | 230864938.43 | 0.08 | skipped_fast |
| BTCUSDT | IDLE | 0.14 | 0.27 | 0.02 | 0.0 | 431177168.49 | 0.0 | skipped_fast |
| CHIPUSDT | IDLE | 1.89 | 6.78 | 5.48 | 0.03 | 443393.64 | 1.79 | skipped_fast |
| PYTHUSDT | IDLE | 2.06 | 3.95 | 1.15 | 0.03 | 369843.89 | 1.82 | skipped_fast |
| KITEUSDT | IDLE | 2.41 | 4.53 | 4.33 | -0.05 | 64749.39 | 8.67 | skipped_fast |
| RIZEUSDT | IDLE | 1.19 | 11.89 | 1.35 | -0.05 | 159639.34 | 40.57 | skipped_fast |
| ZBCNUSDT | IDLE | 1.42 | 2.66 | 1.17 | -0.02 | 193615.41 | 23.15 | skipped_fast |
| CCUSDT | IDLE | 0.91 | 1.82 | 0.04 | 0.0 | 281645.02 | 9.11 | skipped_fast |
| REDUSDT | IDLE | 1.57 | 2.75 | 2.66 | 0.03 | 65511.56 | 19.17 | skipped_fast |
| BIOUSDT | IDLE | 0.97 | 1.94 | 0.04 | 0.03 | 81329.87 | 3.6 | skipped_fast |
| WUSDT | IDLE | 0.55 | 1.03 | 0.49 | 0.05 | 176859.09 | 14.08 | skipped_fast |
| HBARUSDT | IDLE | 1.33 | 2.66 | 0.05 | 0.05 | 271573.04 | 1.23 | skipped_fast |
| EDELUSDT | IDLE | 0.13 | 2.29 | 0.93 | -0.04 | 200258.81 | 18.81 | skipped_fast |
| RWAUSDT | IDLE | 1.45 | 2.83 | 0.49 | 0.02 | 53624.69 | 7.09 | skipped_fast |
| RWAINCUSDT | IDLE | 0.82 | 1.52 | 0.75 | 0.0 | 7089.23 | 69.61 | skipped_fast |
| TELUSDT | IDLE | 0.84 | 1.6 | 0.58 | -0.01 | 74986.24 | 23.52 | skipped_fast |
| QNTUSDT | IDLE | 0.59 | 1.11 | 0.42 | -0.02 | 40832.09 | 4.68 | skipped_fast |
| FLUIDUSDT | IDLE | 0.45 | 0.9 | 0.0 | 0.02 | 820.75 | 21.67 | skipped_fast |
| MNSRYUSDT | IDLE | 0.16 | 0.3 | 0.14 | -0.0 | 37572.57 | 17.74 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
