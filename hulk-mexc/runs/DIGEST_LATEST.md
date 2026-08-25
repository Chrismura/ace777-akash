# Hulk DIGEST — 2026-08-25T21:53:07Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.33 | 8.61 | 6.71 | 0.01 | 2232659.01 | 2.0 | tvl≈116,225,421 |
| XRPUSDT | IDLE | 2.33 | 5.46 | 3.13 | -0.03 | 75323120.65 | 0.7 | n/a |
| CCUSDT | IDLE | 2.2 | 4.28 | 3.5 | -0.04 | 514268.8 | 2.54 | no_map |
| HBARUSDT | IDLE | 2.11 | 4.2 | 3.31 | -0.03 | 795155.45 | 1.28 | empty_tvl |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.5 | 8.72 | 5.58 | 0.01 | 79752.52 | 19.08 | tvl≈2,151,186 |
| CHIPUSDT | IDLE | 1.77 | 4.92 | 2.93 | -0.02 | 489286.8 | 9.54 | no_map |
| WUSDT | IDLE | 2.3 | 4.36 | 2.87 | -0.03 | 357069.93 | 20.43 | tvl≈1,566,850,746 |
| BIOUSDT | IDLE | 3.18 | 5.87 | 3.21 | -0.01 | 114904.13 | 13.81 | n/a |
| ZBCNUSDT | IDLE | 2.92 | 5.37 | 4.28 | 0.01 | 197831.32 | 44.93 | n/a |
| KITEUSDT | IDLE | 3.15 | 5.69 | 4.91 | -0.04 | 61522.62 | 11.83 | no_map |
| EDELUSDT | IDLE | 1.01 | 14.25 | 12.17 | -0.0 | 166667.14 | 34.36 | no_map |
| FLUIDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.18 | 5.57 | 5.27 | -0.04 | 2047.56 | 21.63 | tvl≈2,584,851,401 |
| RIZEUSDT | IDLE | 3.47 | 7.26 | 2.93 | 0.04 | 51273.46 | 237.41 | no_map |
| QAITUSDT | IDLE | 1.63 | 4.3 | 1.69 | 0.0 | 12471.82 | 30.57 | no_map |
| QNTUSDT | IDLE | 2.12 | 3.8 | 2.95 | -0.02 | 95348.68 | 1.58 | n/a |
| RWAUSDT | IDLE | 1.49 | 2.63 | 2.33 | -0.03 | 56037.64 | 24.64 | no_map |
| RWAINCUSDT | IDLE | 1.13 | 2.0 | 1.67 | -0.01 | 2583.13 | 109.89 | no_map |
| TELUSDT | IDLE | 1.53 | 2.74 | 2.18 | -0.05 | 96042.77 | 61.33 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
