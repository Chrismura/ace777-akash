# Hulk DIGEST — 2026-09-10T03:14:25Z

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
| XRPUSDT | IDLE | 0.79 | 1.53 | 0.34 | -0.01 | 43613553.36 | 1.44 | skipped_fast |
| ETHUSDT | IDLE | 0.72 | 1.43 | 0.12 | -0.0 | 390950216.42 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.49 | 0.96 | 0.18 | -0.0 | 542825922.5 | 0.0 | skipped_fast |
| PYTHUSDT | IDLE | 1.2 | 3.27 | 1.16 | -0.02 | 1010166.37 | 1.92 | skipped_fast |
| EDELUSDT | IDLE | 4.12 | 16.05 | 3.95 | 0.06 | 236516.98 | 17.87 | skipped_fast |
| CCUSDT | IDLE | 1.46 | 2.75 | 1.1 | -0.04 | 647728.68 | 7.67 | skipped_fast |
| REDUSDT | IDLE | 2.87 | 5.33 | 2.77 | -0.0 | 64333.32 | 18.84 | skipped_fast |
| WUSDT | IDLE | 1.87 | 3.66 | 1.73 | -0.02 | 207597.62 | 8.09 | skipped_fast |
| BIOUSDT | IDLE | 1.72 | 4.2 | 1.8 | -0.06 | 101986.81 | 3.91 | skipped_fast |
| CHIPUSDT | IDLE | 1.07 | 5.72 | 5.14 | -0.08 | 123279.22 | 14.31 | skipped_fast |
| ZBCNUSDT | IDLE | 1.02 | 1.85 | 1.2 | 0.02 | 185829.97 | 4.93 | skipped_fast |
| KITEUSDT | IDLE | 1.58 | 2.93 | 1.49 | -0.01 | 57104.42 | 20.41 | skipped_fast |
| RWAINCUSDT | IDLE | 1.79 | 3.14 | 2.87 | -0.02 | 5889.78 | 39.63 | skipped_fast |
| HBARUSDT | IDLE | 0.89 | 1.77 | 0.13 | -0.02 | 443887.67 | 1.3 | skipped_fast |
| RIZEUSDT | IDLE | 0.63 | 7.7 | 0.48 | 0.05 | 60118.86 | 86.54 | skipped_fast |
| TELUSDT | IDLE | 1.22 | 2.31 | 0.83 | 0.01 | 97134.37 | 44.47 | skipped_fast |
| QNTUSDT | IDLE | 1.07 | 2.02 | 0.81 | -0.0 | 45742.93 | 4.47 | skipped_fast |
| FLUIDUSDT | IDLE | 1.27 | 2.41 | 2.35 | -0.07 | 1439.18 | 21.94 | skipped_fast |
| RWAUSDT | IDLE | 0.82 | 1.5 | 0.96 | -0.03 | 54591.38 | 14.94 | skipped_fast |
| MNSRYUSDT | IDLE | 1.31 | 2.4 | 1.53 | -0.02 | 28175.67 | 63.54 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
