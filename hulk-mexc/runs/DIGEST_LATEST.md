# Hulk DIGEST — 2026-09-02T17:52:14Z

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
| XRPUSDT | IDLE | 1.14 | 2.19 | 0.65 | -0.02 | 39274329.82 | 2.24 | skipped_fast |
| ETHUSDT | IDLE | 1.05 | 1.93 | 1.07 | -0.01 | 414043816.09 | 1.0 | skipped_fast |
| PYTHUSDT | IDLE | 2.17 | 10.66 | 2.73 | 0.14 | 1329711.72 | 1.73 | skipped_fast |
| BTCUSDT | IDLE | 0.65 | 1.26 | 0.24 | -0.0 | 542796576.87 | 0.2 | skipped_fast |
| CHIPUSDT | IDLE | 2.49 | 9.13 | 6.66 | -0.03 | 1035072.46 | 2.44 | skipped_fast |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.55 | 11.33 | 0.61 | 0.0 | 38169.38 | 71.45 | skipped_fast |
| WUSDT | IDLE | 1.88 | 3.6 | 1.13 | -0.02 | 355782.93 | 13.61 | skipped_fast |
| CCUSDT | IDLE | 1.45 | 2.56 | 2.26 | -0.05 | 354173.4 | 8.21 | skipped_fast |
| ZBCNUSDT | IDLE | 2.38 | 4.3 | 3.03 | -0.06 | 176783.98 | 32.59 | skipped_fast |
| KITEUSDT | IDLE | 1.8 | 9.31 | 0.0 | 0.19 | 98574.6 | 8.93 | skipped_fast |
| RWAINCUSDT | IDLE | 1.97 | 5.69 | 2.96 | 0.07 | 9967.31 | 27.17 | skipped_fast |
| REDUSDT | IDLE | 1.26 | 2.43 | 0.59 | 0.03 | 151688.82 | 11.25 | skipped_fast |
| EDELUSDT | IDLE | 0.66 | 3.52 | 2.35 | 0.07 | 169721.61 | 41.51 | skipped_fast |
| BIOUSDT | IDLE | 0.85 | 1.67 | 0.24 | -0.01 | 68639.37 | 3.93 | skipped_fast |
| FLUIDUSDT | IDLE | 1.96 | 3.74 | 1.74 | -0.06 | 1875.95 | 22.37 | skipped_fast |
| TELUSDT | IDLE | 1.95 | 3.77 | 0.87 | 0.01 | 77656.23 | 63.97 | skipped_fast |
| HBARUSDT | IDLE | 0.77 | 1.46 | 0.57 | -0.01 | 208640.42 | 1.36 | skipped_fast |
| QNTUSDT | IDLE | 1.35 | 2.69 | 0.08 | 0.02 | 64093.78 | 7.63 | skipped_fast |
| RWAUSDT | IDLE | 1.27 | 2.47 | 0.45 | 0.02 | 51699.68 | 7.56 | skipped_fast |
| MNSRYUSDT | IDLE | 0.26 | 0.51 | 0.12 | -0.01 | 32216.76 | 23.39 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
