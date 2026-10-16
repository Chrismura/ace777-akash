# Hulk DIGEST — 2026-10-16T02:22:05Z

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
| WUSDT | IDLE | 1.76 | 4.31 | 0.9 | -0.03 | 2595454.46 | 18.12 | skipped_fast |
| PYTHUSDT | IDLE | 0.72 | 4.3 | 1.62 | 0.1 | 4402593.03 | 5.28 | skipped_fast |
| ETHUSDT | IDLE | 0.81 | 1.46 | 1.03 | 0.01 | 296727125.34 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.57 | 1.04 | 0.69 | 0.01 | 46946300.9 | 0.75 | skipped_fast |
| BTCUSDT | IDLE | 0.37 | 0.67 | 0.48 | 0.01 | 494333257.49 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 1.07 | 3.28 | 0.22 | 0.04 | 1312086.1 | 1.44 | skipped_fast |
| CCUSDT | IDLE | 1.79 | 3.28 | 1.95 | -0.05 | 461610.69 | 10.36 | skipped_fast |
| CHIPUSDT | IDLE | 1.81 | 8.4 | 1.29 | 0.02 | 150830.52 | 10.01 | skipped_fast |
| REDUSDT | IDLE | 1.79 | 5.22 | 4.76 | -0.04 | 74296.49 | 9.93 | skipped_fast |
| EDELUSDT | IDLE | 1.32 | 4.23 | 2.8 | -0.11 | 230268.29 | 23.92 | skipped_fast |
| ZBCNUSDT | IDLE | 1.46 | 2.89 | 1.5 | 0.05 | 209241.16 | 14.78 | skipped_fast |
| KITEUSDT | IDLE | 1.01 | 1.94 | 0.57 | 0.0 | 69453.67 | 12.07 | skipped_fast |
| BIOUSDT | IDLE | 0.84 | 1.57 | 0.77 | -0.0 | 80713.5 | 7.77 | skipped_fast |
| HBARUSDT | IDLE | 0.95 | 1.77 | 0.86 | 0.02 | 294815.27 | 8.19 | skipped_fast |
| RWAINCUSDT | IDLE | 0.73 | 1.55 | 0.79 | 0.01 | 29531.8 | 4.98 | skipped_fast |
| RIZEUSDT | IDLE | 0.78 | 2.9 | 1.58 | 0.08 | 74174.74 | 56.82 | skipped_fast |
| TELUSDT | IDLE | 0.83 | 1.53 | 0.84 | 0.03 | 91775.0 | 28.13 | skipped_fast |
| FLUIDUSDT | IDLE | 0.84 | 1.54 | 1.52 | -0.05 | 10196.21 | 21.14 | skipped_fast |
| RWAUSDT | IDLE | 0.31 | 0.56 | 0.4 | 0.01 | 54014.98 | 23.84 | skipped_fast |
| MNSRYUSDT | IDLE | 0.18 | 0.35 | 0.11 | 0.0 | 37299.9 | 26.81 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
