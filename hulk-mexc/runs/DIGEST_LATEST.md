# Hulk DIGEST — 2026-09-02T14:46:37Z

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
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.47 | 14.29 | 11.2 | -0.04 | 945300.11 | 4.82 | skipped_fast |
| XRPUSDT | IDLE | 1.43 | 2.79 | 0.46 | -0.03 | 39410885.63 | 0.75 | skipped_fast |
| ETHUSDT | IDLE | 1.37 | 2.63 | 0.67 | -0.02 | 407965721.78 | 0.42 | skipped_fast |
| BTCUSDT | IDLE | 0.82 | 1.59 | 0.27 | -0.01 | 518351966.14 | 0.04 | skipped_fast |
| PYTHUSDT | IDLE | 1.89 | 7.8 | 1.15 | 0.14 | 1089023.5 | 14.05 | skipped_fast |
| CCUSDT | IDLE | 2.1 | 3.69 | 3.35 | -0.07 | 357835.31 | 6.36 | skipped_fast |
| WUSDT | IDLE | 1.58 | 2.91 | 1.71 | -0.02 | 396941.58 | 7.38 | skipped_fast |
| REDUSDT | IDLE | 2.76 | 5.41 | 0.68 | 0.03 | 160639.18 | 20.84 | skipped_fast |
| KITEUSDT | IDLE | 1.63 | 6.19 | 1.46 | 0.11 | 89123.22 | 9.45 | skipped_fast |
| RIZEUSDT | IDLE | 2.28 | 7.8 | 3.12 | -0.07 | 37020.52 | 76.23 | skipped_fast |
| RWAINCUSDT | IDLE | 1.93 | 5.69 | 2.85 | 0.07 | 10922.84 | 32.68 | skipped_fast |
| FLUIDUSDT | IDLE | 2.78 | 4.96 | 4.7 | -0.08 | 1777.37 | 21.95 | skipped_fast |
| ZBCNUSDT | IDLE | 1.02 | 2.07 | 1.52 | -0.03 | 195806.42 | 59.85 | skipped_fast |
| BIOUSDT | IDLE | 1.12 | 2.2 | 0.31 | -0.02 | 72696.85 | 3.94 | skipped_fast |
| EDELUSDT | IDLE | 0.65 | 3.7 | 1.05 | 0.09 | 171440.48 | 32.79 | skipped_fast |
| TELUSDT | IDLE | 1.77 | 3.44 | 0.64 | -0.0 | 74564.61 | 11.74 | skipped_fast |
| HBARUSDT | IDLE | 0.95 | 1.84 | 0.38 | -0.01 | 203381.09 | 1.35 | skipped_fast |
| QNTUSDT | IDLE | 1.26 | 2.48 | 0.31 | 0.02 | 69488.07 | 4.65 | skipped_fast |
| RWAUSDT | IDLE | 0.73 | 1.39 | 0.53 | 0.01 | 51441.31 | 7.65 | skipped_fast |
| MNSRYUSDT | IDLE | 0.38 | 0.72 | 0.23 | -0.01 | 34725.87 | 39.89 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
