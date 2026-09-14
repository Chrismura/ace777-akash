# Hulk DIGEST — 2026-09-14T14:42:55Z

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
| XRPUSDT | IDLE | 1.1 | 2.06 | 0.91 | 0.03 | 40502171.61 | 2.15 | skipped_fast |
| ETHUSDT | IDLE | 1.05 | 1.89 | 1.41 | 0.0 | 349287497.24 | 0.04 | skipped_fast |
| BTCUSDT | IDLE | 0.8 | 1.55 | 0.33 | 0.02 | 435382932.62 | 0.54 | skipped_fast |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.22 | 7.52 | 6.12 | -0.01 | 500269.9 | 3.64 | skipped_fast |
| REDUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.76 | 10.34 | 1.43 | 0.1 | 175481.4 | 9.59 | skipped_fast |
| WUSDT | IDLE | 2.2 | 3.93 | 3.12 | -0.01 | 227469.46 | 12.13 | skipped_fast |
| CHIPUSDT | IDLE | 2.75 | 5.43 | 3.54 | -0.07 | 88733.94 | 14.49 | skipped_fast |
| EDELUSDT | IDLE | 1.92 | 8.21 | 3.42 | 0.14 | 248812.52 | 55.44 | skipped_fast |
| CCUSDT | IDLE | 1.12 | 2.13 | 0.8 | 0.01 | 264800.98 | 10.42 | skipped_fast |
| ZBCNUSDT | IDLE | 1.51 | 2.94 | 0.48 | -0.0 | 199085.11 | 28.39 | skipped_fast |
| RIZEUSDT | IDLE | 1.09 | 12.23 | 8.64 | 0.08 | 66830.59 | 38.88 | skipped_fast |
| BIOUSDT | IDLE | 1.35 | 2.5 | 1.35 | -0.0 | 79974.01 | 7.85 | skipped_fast |
| KITEUSDT | IDLE | 1.0 | 1.75 | 1.72 | -0.03 | 61491.28 | 13.29 | skipped_fast |
| HBARUSDT | IDLE | 1.03 | 1.87 | 1.21 | 0.0 | 284652.18 | 1.31 | skipped_fast |
| RWAINCUSDT | IDLE | 0.94 | 1.83 | 0.38 | 0.03 | 8736.61 | 27.42 | skipped_fast |
| TELUSDT | IDLE | 1.6 | 3.05 | 1.05 | 0.01 | 89076.68 | 12.47 | skipped_fast |
| QNTUSDT | IDLE | 0.89 | 1.69 | 0.56 | -0.0 | 40314.37 | 6.23 | skipped_fast |
| FLUIDUSDT | IDLE | 1.08 | 1.89 | 1.75 | -0.0 | 910.72 | 21.93 | skipped_fast |
| RWAUSDT | IDLE | 0.28 | 0.52 | 0.3 | 0.01 | 54827.52 | 29.63 | skipped_fast |
| MNSRYUSDT | IDLE | 0.21 | 0.38 | 0.21 | -0.0 | 28525.48 | 18.15 | skipped_fast |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
