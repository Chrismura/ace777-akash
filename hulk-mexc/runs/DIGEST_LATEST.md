# Hulk DIGEST — 2026-08-25T23:09:52Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.57 | 6.92 | 5.05 | 0.01 | 2215941.29 | 2.0 | tvl≈116,225,421 |
| XRPUSDT | IDLE | 2.25 | 5.37 | 2.37 | -0.02 | 75149733.28 | 2.07 | n/a |
| HBARUSDT | IDLE | 2.06 | 4.2 | 2.62 | -0.01 | 803097.46 | 1.27 | empty_tvl |
| CCUSDT | IDLE | 1.75 | 3.74 | 0.55 | -0.01 | 536463.2 | 8.26 | no_map |
| CHIPUSDT | IDLE | 1.74 | 5.18 | 0.68 | -0.01 | 474421.54 | 3.1 | no_map |
| RIZEUSDT | IDLE | 3.53 | 7.26 | 3.89 | 0.02 | 50462.81 | 19.26 | no_map |
| WUSDT | IDLE | 2.26 | 4.36 | 2.32 | -0.01 | 344331.42 | 13.9 | tvl≈1,545,603,246 |
| BIOUSDT | IDLE | 3.08 | 5.87 | 1.94 | 0.01 | 114680.89 | 3.41 | n/a |
| REDUSDT | IDLE | 2.96 | 7.38 | 4.74 | 0.0 | 80617.25 | 12.22 | tvl≈2,151,186 |
| ZBCNUSDT | IDLE | 2.14 | 3.85 | 2.87 | 0.01 | 192353.01 | 11.63 | n/a |
| EDELUSDT | IDLE | 0.97 | 13.82 | 11.23 | -0.01 | 163723.43 | 34.31 | no_map |
| KITEUSDT | IDLE | 2.37 | 4.57 | 1.79 | -0.02 | 61705.83 | 14.25 | no_map |
| QAITUSDT | IDLE | 1.58 | 4.3 | 0.79 | 0.03 | 12489.87 | 26.42 | no_map |
| FLUIDUSDT | IDLE | 2.13 | 3.96 | 2.03 | -0.02 | 2037.2 | 21.4 | tvl≈2,573,786,962 |
| QNTUSDT | IDLE | 1.17 | 2.13 | 1.37 | -0.01 | 125931.55 | 1.58 | n/a |
| TELUSDT | IDLE | 1.27 | 2.46 | 0.6 | -0.04 | 93974.16 | 60.56 | no_map |
| RWAINCUSDT | IDLE | 0.34 | 0.6 | 0.6 | -0.01 | 2546.77 | 70.07 | no_map |
| RWAUSDT | IDLE | 0.93 | 1.65 | 1.46 | -0.03 | 56913.17 | 32.84 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
