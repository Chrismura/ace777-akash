# Hulk DIGEST — 2026-10-16T01:06:02Z

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
| WUSDT | IDLE | 1.36 | 3.61 | 0.97 | -0.05 | 2820615.77 | 11.51 | skipped_fast |
| PYTHUSDT | IDLE | 0.7 | 3.98 | 2.97 | 0.12 | 4452808.49 | 4.28 | skipped_fast |
| ETHUSDT | IDLE | 0.67 | 1.19 | 1.02 | 0.01 | 300832258.58 | 0.04 | skipped_fast |
| XRPUSDT | IDLE | 0.56 | 1.02 | 0.65 | 0.01 | 47332401.72 | 0.75 | skipped_fast |
| BTCUSDT | IDLE | 0.42 | 0.79 | 0.29 | 0.01 | 500006738.04 | 0.0 | skipped_fast |
| QNTUSDT | IDLE | 0.95 | 2.98 | 1.13 | 0.01 | 1345215.24 | 2.42 | skipped_fast |
| CCUSDT | IDLE | 1.41 | 2.93 | 0.39 | -0.07 | 481852.91 | 8.38 | skipped_fast |
| ZBCNUSDT | IDLE | 1.61 | 3.29 | 1.72 | 0.04 | 216277.24 | 19.23 | skipped_fast |
| EDELUSDT | IDLE | 1.3 | 4.37 | 2.49 | -0.1 | 230407.22 | 17.03 | skipped_fast |
| CHIPUSDT | IDLE | 1.36 | 5.48 | 0.31 | -0.04 | 150101.31 | 10.33 | skipped_fast |
| REDUSDT | IDLE | 1.18 | 3.43 | 3.11 | -0.03 | 72982.44 | 16.28 | skipped_fast |
| KITEUSDT | IDLE | 1.22 | 2.27 | 1.19 | -0.01 | 69592.51 | 10.49 | skipped_fast |
| BIOUSDT | IDLE | 0.53 | 1.01 | 0.39 | -0.02 | 83773.05 | 3.87 | skipped_fast |
| RIZEUSDT | IDLE | 0.81 | 2.9 | 2.34 | 0.06 | 77689.75 | 59.36 | skipped_fast |
| HBARUSDT | IDLE | 0.79 | 1.54 | 0.27 | 0.02 | 304360.1 | 8.17 | skipped_fast |
| RWAINCUSDT | IDLE | 0.71 | 1.55 | 0.49 | 0.02 | 29703.77 | 19.86 | skipped_fast |
| TELUSDT | IDLE | 1.13 | 2.11 | 1.0 | 0.02 | 93355.07 | 39.43 | skipped_fast |
| FLUIDUSDT | IDLE | 0.64 | 1.27 | 0.84 | -0.04 | 10195.01 | 21.2 | skipped_fast |
| RWAUSDT | IDLE | 0.4 | 0.72 | 0.55 | 0.01 | 53955.88 | 23.84 | skipped_fast |
| MNSRYUSDT | IDLE | 0.19 | 0.35 | 0.24 | -0.0 | 36513.42 | 9.87 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
