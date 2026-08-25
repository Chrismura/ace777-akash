# Hulk DIGEST — 2026-08-25T22:09:36Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.85 | 7.78 | 5.11 | 0.01 | 2237766.42 | 1.99 | tvl≈116,225,421 |
| XRPUSDT | IDLE | 2.24 | 5.37 | 2.2 | -0.02 | 75221432.26 | 3.45 | n/a |
| CCUSDT | IDLE | 2.14 | 4.28 | 2.55 | -0.03 | 520384.06 | 5.87 | no_map |
| HBARUSDT | IDLE | 2.07 | 4.2 | 2.81 | -0.02 | 795716.31 | 1.28 | empty_tvl |
| CHIPUSDT | IDLE | 1.71 | 4.92 | 1.79 | -0.01 | 486838.69 | 21.96 | no_map |
| WUSDT | IDLE | 2.25 | 4.36 | 2.19 | -0.03 | 355690.65 | 11.75 | tvl≈1,566,850,746 |
| BIOUSDT | IDLE | 3.13 | 5.87 | 2.54 | -0.01 | 115727.04 | 3.43 | n/a |
| RIZEUSDT | IDLE | 3.44 | 7.26 | 2.56 | 0.05 | 51655.11 | 22.44 | no_map |
| REDUSDT | IDLE | 2.91 | 7.38 | 3.71 | 0.01 | 79739.13 | 18.98 | tvl≈2,151,186 |
| KITEUSDT | IDLE | 2.66 | 4.98 | 2.99 | -0.03 | 61643.09 | 9.85 | no_map |
| ZBCNUSDT | IDLE | 2.1 | 3.85 | 2.89 | 0.01 | 198644.57 | 24.84 | n/a |
| EDELUSDT | IDLE | 0.96 | 13.82 | 10.55 | 0.01 | 166711.46 | 50.72 | no_map |
| QAITUSDT | IDLE | 1.63 | 4.3 | 1.69 | 0.01 | 12416.87 | 30.57 | no_map |
| FLUIDUSDT | IDLE | 2.37 | 4.14 | 3.98 | -0.04 | 2047.56 | 16.94 | tvl≈2,584,851,401 |
| QNTUSDT | IDLE | 1.45 | 2.62 | 1.83 | -0.02 | 101004.55 | 1.58 | n/a |
| RWAINCUSDT | IDLE | 0.98 | 1.7 | 1.67 | -0.01 | 2583.13 | 65.08 | no_map |
| RWAUSDT | IDLE | 1.48 | 2.63 | 2.25 | -0.03 | 56327.35 | 32.84 | no_map |
| TELUSDT | IDLE | 1.41 | 2.52 | 1.97 | -0.05 | 93749.2 | 55.68 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
