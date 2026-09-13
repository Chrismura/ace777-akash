# Hulk DIGEST — 2026-09-13T21:40:56Z

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
| XRPUSDT | IDLE | 0.74 | 1.42 | 0.35 | -0.01 | 15202432.14 | 2.21 | skipped_fast |
| ETHUSDT | IDLE | 0.52 | 1.02 | 0.18 | -0.01 | 252027859.92 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.2 | 0.38 | 0.07 | 0.0 | 253744905.31 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.75 | 5.64 | 1.02 | 0.04 | 447694.02 | 5.24 | skipped_fast |
| RIZEUSDT | IDLE | 2.27 | 32.72 | 21.16 | -0.11 | 67751.01 | 78.04 | skipped_fast |
| RWAINCUSDT | IDLE | 4.18 | 7.78 | 3.9 | -0.0 | 9897.08 | 21.99 | skipped_fast |
| EDELUSDT | IDLE | 2.09 | 7.43 | 1.47 | 0.13 | 202353.1 | 14.96 | skipped_fast |
| WUSDT | IDLE | 1.46 | 2.67 | 1.66 | 0.02 | 218525.67 | 10.86 | skipped_fast |
| CCUSDT | IDLE | 0.75 | 1.47 | 0.23 | -0.01 | 297992.11 | 9.37 | skipped_fast |
| ZBCNUSDT | IDLE | 1.01 | 1.91 | 0.67 | -0.0 | 197697.48 | 24.48 | skipped_fast |
| CHIPUSDT | IDLE | 0.92 | 2.46 | 2.02 | -0.1 | 82918.86 | 13.87 | skipped_fast |
| BIOUSDT | IDLE | 0.89 | 1.7 | 0.58 | 0.01 | 67607.52 | 11.71 | skipped_fast |
| HBARUSDT | IDLE | 1.36 | 2.58 | 0.97 | 0.03 | 228040.41 | 1.3 | skipped_fast |
| REDUSDT | IDLE | 0.74 | 1.39 | 0.6 | 0.01 | 63998.9 | 11.45 | skipped_fast |
| KITEUSDT | IDLE | 0.56 | 1.11 | 0.1 | 0.0 | 60245.34 | 12.99 | skipped_fast |
| QNTUSDT | IDLE | 1.73 | 3.05 | 2.71 | -0.0 | 36040.71 | 1.57 | skipped_fast |
| TELUSDT | IDLE | 0.93 | 1.65 | 1.37 | -0.05 | 81033.34 | 44.23 | skipped_fast |
| RWAUSDT | IDLE | 0.38 | 0.75 | 0.0 | 0.01 | 53891.92 | 22.21 | skipped_fast |
| FLUIDUSDT | IDLE | 0.53 | 1.04 | 0.17 | 0.0 | 1525.44 | 21.92 | skipped_fast |
| MNSRYUSDT | IDLE | 0.25 | 0.46 | 0.31 | -0.0 | 30534.35 | 12.51 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
