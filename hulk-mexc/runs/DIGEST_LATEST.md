# Hulk DIGEST — 2026-09-20T04:01:18Z

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
| XRPUSDT | IDLE | 1.97 | 3.58 | 2.44 | -0.03 | 58270827.65 | 2.89 | skipped_fast |
| ETHUSDT | IDLE | 1.57 | 2.85 | 1.94 | -0.01 | 241338166.96 | 1.24 | skipped_fast |
| BTCUSDT | IDLE | 0.84 | 1.52 | 1.05 | -0.01 | 474109084.61 | 0.0 | skipped_fast |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.74 | 6.71 | 5.1 | -0.04 | 755827.26 | 5.09 | skipped_fast |
| WUSDT | IDLE | 2.66 | 4.91 | 2.79 | 0.01 | 517325.76 | 6.32 | skipped_fast |
| HBARUSDT | IDLE | 3.01 | 5.43 | 3.92 | 0.01 | 679534.94 | 2.48 | skipped_fast |
| CCUSDT | IDLE | 2.54 | 5.25 | 3.47 | -0.06 | 326297.79 | 10.39 | skipped_fast |
| ZBCNUSDT | IDLE | 1.97 | 7.36 | 5.66 | 0.05 | 216376.84 | 18.36 | skipped_fast |
| BIOUSDT | IDLE | 2.73 | 4.94 | 3.43 | -0.0 | 88910.03 | 7.33 | skipped_fast |
| CHIPUSDT | IDLE | 2.24 | 6.39 | 3.97 | -0.1 | 112687.88 | 21.26 | skipped_fast |
| EDELUSDT | IDLE | 2.04 | 8.65 | 6.42 | -0.14 | 105267.74 | 72.02 | skipped_fast |
| REDUSDT | IDLE | 1.99 | 3.81 | 1.19 | 0.03 | 99955.33 | 21.98 | skipped_fast |
| RIZEUSDT | IDLE | 1.93 | 10.64 | 5.55 | -0.03 | 40533.08 | 82.1 | skipped_fast |
| KITEUSDT | IDLE | 1.54 | 2.87 | 1.34 | -0.0 | 77199.46 | 11.43 | skipped_fast |
| FLUIDUSDT | IDLE | 1.97 | 3.45 | 3.2 | -0.0 | 6703.96 | 21.65 | skipped_fast |
| QNTUSDT | IDLE | 1.5 | 2.64 | 2.41 | 0.01 | 55905.24 | 1.55 | skipped_fast |
| TELUSDT | IDLE | 1.29 | 2.47 | 2.28 | -0.07 | 104196.65 | 34.19 | skipped_fast |
| RWAINCUSDT | IDLE | 0.13 | 0.3 | 0.12 | -0.03 | 7006.77 | 17.8 | skipped_fast |
| RWAUSDT | IDLE | 0.71 | 1.26 | 1.03 | 0.0 | 52563.43 | 22.25 | skipped_fast |
| MNSRYUSDT | IDLE | 0.4 | 0.72 | 0.56 | -0.01 | 34966.53 | 46.5 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
