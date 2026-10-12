# Hulk DIGEST — 2026-10-12T20:49:38Z

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
| WUSDT | IDLE | 1.49 | 20.1 | 16.51 | -0.06 | 15823023.91 | 5.38 | tvl≈1,678,403,409 |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 2.56 | 10.59 | 5.46 | 0.08 | 3323738.14 | 2.36 | tvl≈187,390,750 |
| XRPUSDT | IDLE | 1.13 | 2.11 | 0.95 | -0.03 | 28958544.4 | 2.19 | n/a |
| ETHUSDT | IDLE | 0.63 | 1.19 | 0.42 | -0.01 | 229635556.33 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.48 | 0.96 | 0.03 | -0.01 | 286245328.15 | 0.0 | no_map |
| QNTUSDT | IDLE | 1.3 | 2.53 | 0.43 | -0.05 | 804488.39 | 0.43 | n/a |
| REDUSDT | IDLE | 1.63 | 10.37 | 6.45 | 0.04 | 262350.98 | 19.6 | tvl≈3,906,190 |
| EDELUSDT | IDLE | 1.54 | 6.93 | 1.85 | -0.1 | 270995.47 | 11.78 | no_map |
| CCUSDT | IDLE | 0.99 | 1.83 | 1.0 | -0.02 | 394230.01 | 5.73 | no_map |
| HBARUSDT | IDLE | 1.3 | 2.44 | 1.12 | -0.05 | 577984.26 | 1.11 | empty_tvl |
| KITEUSDT | IDLE | 2.09 | 4.06 | 0.77 | 0.0 | 66262.62 | 10.92 | no_map |
| ZBCNUSDT | IDLE | 1.16 | 2.17 | 1.02 | 0.0 | 281885.92 | 14.64 | n/a |
| BIOUSDT | IDLE | 1.16 | 2.17 | 1.01 | -0.05 | 82226.39 | 3.51 | n/a |
| RIZEUSDT | IDLE | 1.47 | 6.17 | 4.8 | -0.03 | 62456.23 | 87.25 | no_map |
| CHIPUSDT | IDLE | 0.63 | 3.01 | 0.7 | -0.14 | 164980.98 | 11.76 | no_map |
| TELUSDT | IDLE | 2.08 | 3.89 | 1.79 | 0.02 | 118992.85 | 39.81 | no_map |
| RWAINCUSDT | IDLE | 1.32 | 3.45 | 2.32 | -0.0 | 30471.5 | 123.73 | no_map |
| FLUIDUSDT | IDLE | 1.1 | 2.2 | 0.04 | -0.01 | 14800.22 | 18.11 | tvl≈2,391,422,533 |
| RWAUSDT | IDLE | 0.33 | 0.62 | 0.31 | 0.0 | 52444.93 | 15.43 | no_map |
| MNSRYUSDT | IDLE | 0.41 | 0.76 | 0.34 | -0.0 | 41532.49 | 49.38 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
