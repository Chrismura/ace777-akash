# Hulk DIGEST — 2026-08-21T19:45:53Z

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
| PYTHUSDT | IDLE | 1.37 | 4.99 | 4.2 | 0.06 | 5423945.84 | 4.26 | tvl≈109,691,978 |
| XRPUSDT | IDLE | 1.16 | 4.21 | 3.23 | 0.11 | 129042178.72 | 1.46 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.14 | 26.97 | 13.46 | 0.16 | 154033.53 | 18.02 | tvl≈2,358,074 |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 2.56 | 11.37 | 9.43 | 0.05 | 481615.63 | 16.6 | n/a |
| CCUSDT | IDLE | 2.05 | 5.44 | 2.04 | 0.06 | 631115.49 | 8.42 | no_map |
| CHIPUSDT | IDLE | 1.24 | 4.81 | 4.03 | 0.09 | 513440.37 | 3.11 | no_map |
| WUSDT | IDLE | 2.15 | 3.92 | 2.83 | 0.04 | 361097.24 | 10.7 | tvl≈1,603,481,943 |
| BIOUSDT | IDLE | 2.67 | 5.33 | 4.82 | -0.0 | 190638.17 | 3.22 | n/a |
| HBARUSDT | IDLE | 1.49 | 2.85 | 2.76 | 0.05 | 764734.65 | 1.31 | empty_tvl |
| EDELUSDT | IDLE | 2.43 | 4.29 | 3.79 | -0.05 | 79613.32 | 22.52 | no_map |
| RIZEUSDT | IDLE | 2.25 | 11.27 | 3.09 | 0.01 | 56486.65 | 45.77 | no_map |
| KITEUSDT | IDLE | 1.29 | 4.0 | 3.41 | 0.09 | 60941.15 | 11.29 | no_map |
| RWAINCUSDT | IDLE | 2.23 | 4.3 | 1.11 | 0.04 | 11032.33 | 85.88 | no_map |
| QAITUSDT | IDLE | 1.65 | 3.0 | 1.98 | -0.01 | 2930.33 | 63.29 | no_map |
| TELUSDT | IDLE | 1.83 | 4.46 | 2.05 | 0.02 | 184017.98 | 37.66 | no_map |
| QNTUSDT | IDLE | 1.66 | 3.01 | 2.11 | 0.04 | 59828.9 | 4.71 | n/a |
| RWAUSDT | IDLE | 0.65 | 1.16 | 0.99 | 0.04 | 54322.3 | 16.6 | no_map |
| FLUIDUSDT | IDLE | 0.73 | 1.48 | 1.14 | 0.07 | 4331.26 | 21.02 | tvl≈2,554,565,268 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
