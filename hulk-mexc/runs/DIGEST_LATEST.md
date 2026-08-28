# Hulk DIGEST — 2026-08-28T07:07:24Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 1.37 | 2.57 | 1.11 | 0.04 | 15739063.92 | 2.04 | skipped_fast |
| XRPUSDT | IDLE | 1.28 | 2.26 | 2.06 | 0.01 | 56304334.75 | 1.41 | skipped_fast |
| QAITUSDT | IDLE | 1.07 | 55.46 | 31.55 | -0.2 | 72761.94 | 44.94 | skipped_fast |
| CHIPUSDT | IDLE | 1.96 | 9.97 | 2.63 | 0.07 | 686808.47 | 2.5 | skipped_fast |
| CCUSDT | IDLE | 1.38 | 2.69 | 0.44 | -0.02 | 470344.7 | 5.29 | skipped_fast |
| WUSDT | IDLE | 2.03 | 3.69 | 2.47 | -0.0 | 204369.54 | 8.46 | skipped_fast |
| ZBCNUSDT | IDLE | 1.18 | 2.97 | 2.0 | 0.05 | 258667.05 | 10.54 | skipped_fast |
| KITEUSDT | IDLE | 1.91 | 3.8 | 0.13 | -0.0 | 70380.38 | 9.91 | skipped_fast |
| BIOUSDT | IDLE | 1.68 | 3.07 | 1.92 | 0.01 | 93720.92 | 3.49 | skipped_fast |
| REDUSDT | IDLE | 1.63 | 2.84 | 2.76 | 0.0 | 81537.38 | 21.98 | skipped_fast |
| RIZEUSDT | IDLE | 0.86 | 10.92 | 1.41 | -0.16 | 120033.38 | 42.89 | skipped_fast |
| TELUSDT | IDLE | 2.31 | 4.15 | 3.09 | 0.01 | 127614.17 | 48.79 | skipped_fast |
| HBARUSDT | IDLE | 1.05 | 1.99 | 0.76 | 0.01 | 310379.16 | 1.28 | skipped_fast |
| EDELUSDT | IDLE | 0.61 | 4.17 | 3.26 | 0.09 | 43585.04 | 17.26 | skipped_fast |
| RWAINCUSDT | IDLE | 1.39 | 4.28 | 4.1 | -0.03 | 20682.7 | 137.78 | skipped_fast |
| QNTUSDT | IDLE | 0.89 | 1.65 | 0.87 | -0.01 | 43022.3 | 4.81 | skipped_fast |
| FLUIDUSDT | IDLE | 1.01 | 3.22 | 1.71 | 0.01 | 7985.78 | 21.93 | skipped_fast |
| RWAUSDT | IDLE | 0.21 | 0.41 | 0.08 | 0.01 | 54563.71 | 16.52 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
