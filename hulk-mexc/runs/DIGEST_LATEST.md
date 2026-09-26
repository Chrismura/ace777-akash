# Hulk DIGEST — 2026-09-26T07:56:53Z

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
| XRPUSDT | IDLE | 1.12 | 2.01 | 1.54 | 0.01 | 109748147.79 | 1.93 | skipped_fast |
| ETHUSDT | IDLE | 0.24 | 0.46 | 0.18 | 0.01 | 285648982.37 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.16 | 0.32 | 0.06 | 0.0 | 610935303.67 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.47 | 3.39 | 0.01 | 0.09 | 1202290.56 | 2.66 | skipped_fast |
| CCUSDT | IDLE | 1.53 | 7.25 | 1.32 | 0.17 | 1028105.67 | 10.18 | skipped_fast |
| WUSDT | IDLE | 1.78 | 3.64 | 0.35 | 0.08 | 476378.21 | 3.18 | skipped_fast |
| HBARUSDT | IDLE | 1.05 | 1.97 | 0.92 | 0.03 | 856482.96 | 1.06 | skipped_fast |
| QNTUSDT | IDLE | 2.11 | 6.54 | 3.48 | -0.0 | 526672.85 | 10.88 | skipped_fast |
| ZBCNUSDT | IDLE | 1.4 | 3.27 | 1.39 | 0.04 | 244552.34 | 12.69 | skipped_fast |
| EDELUSDT | IDLE | 1.63 | 3.04 | 1.49 | 0.01 | 176030.09 | 3.37 | skipped_fast |
| KITEUSDT | IDLE | 1.67 | 4.02 | 3.69 | 0.07 | 78198.35 | 8.91 | skipped_fast |
| RWAINCUSDT | IDLE | 1.87 | 4.42 | 1.12 | -0.03 | 10456.2 | 4.93 | skipped_fast |
| CHIPUSDT | IDLE | 1.05 | 2.53 | 0.3 | 0.06 | 149235.14 | 16.27 | skipped_fast |
| BIOUSDT | IDLE | 0.74 | 1.76 | 0.97 | 0.06 | 111483.21 | 6.13 | skipped_fast |
| REDUSDT | IDLE | 0.96 | 1.8 | 0.78 | 0.05 | 59435.53 | 6.42 | skipped_fast |
| RIZEUSDT | IDLE | 0.26 | 3.43 | 1.16 | -0.18 | 70005.95 | 28.14 | skipped_fast |
| TELUSDT | IDLE | 0.89 | 1.61 | 1.1 | 0.01 | 118284.04 | 49.29 | skipped_fast |
| FLUIDUSDT | IDLE | 0.96 | 1.83 | 0.62 | 0.01 | 3431.02 | 21.55 | skipped_fast |
| RWAUSDT | IDLE | 0.56 | 1.04 | 0.51 | -0.01 | 53162.66 | 7.39 | skipped_fast |
| MNSRYUSDT | IDLE | 0.45 | 0.89 | 0.11 | 0.01 | 40770.58 | 8.92 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
