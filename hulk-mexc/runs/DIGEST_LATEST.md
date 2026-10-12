# Hulk DIGEST — 2026-10-12T04:32:46Z

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
| WUSDT | IDLE | 2.13 | 39.33 | 3.68 | 0.69 | 8999332.42 | 16.88 | tvl≈1,690,698,708 |
| ETHUSDT | IDLE | 0.62 | 1.18 | 0.39 | 0.02 | 197629338.32 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.5 | 0.96 | 0.21 | 0.01 | 17929950.51 | 1.42 | n/a |
| BTCUSDT | IDLE | 0.36 | 0.67 | 0.34 | 0.01 | 172446111.07 | 0.0 | no_map |
| PYTHUSDT | IDLE | 3.31 | 7.16 | 3.86 | 0.03 | 951995.64 | 6.25 | tvl≈175,590,654 |
| ZBCNUSDT | IDLE | 3.42 | 6.9 | 2.09 | 0.05 | 266223.55 | 4.61 | n/a |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.22 | 9.64 | 7.13 | 0.04 | 212307.6 | 13.87 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.6 | 16.5 | 9.14 | 0.1 | 44413.34 | 80.0 | no_map |
| EDELUSDT | IDLE | 1.83 | 3.56 | 0.7 | -0.01 | 321336.55 | 10.49 | no_map |
| QNTUSDT | IDLE | 1.09 | 2.1 | 0.53 | 0.01 | 695777.81 | 3.33 | n/a |
| CCUSDT | IDLE | 1.1 | 2.18 | 0.24 | 0.07 | 388875.1 | 6.32 | no_map |
| REDUSDT | IDLE | 1.55 | 3.0 | 0.61 | 0.03 | 54459.57 | 10.48 | tvl≈3,781,849 |
| BIOUSDT | IDLE | 1.04 | 1.96 | 0.8 | 0.04 | 96781.82 | 6.7 | n/a |
| KITEUSDT | IDLE | 0.82 | 1.62 | 0.09 | 0.03 | 63656.33 | 10.1 | no_map |
| RWAINCUSDT | IDLE | 1.04 | 2.95 | 1.73 | -0.0 | 22579.74 | 40.16 | no_map |
| HBARUSDT | IDLE | 0.73 | 1.44 | 0.17 | 0.03 | 347035.06 | 6.35 | empty_tvl |
| TELUSDT | IDLE | 1.21 | 2.3 | 0.86 | -0.01 | 174227.34 | 29.04 | no_map |
| FLUIDUSDT | IDLE | 0.54 | 3.78 | 3.38 | 0.07 | 66009.2 | 14.69 | tvl≈2,431,251,819 |
| MNSRYUSDT | IDLE | 0.41 | 0.78 | 0.23 | -0.0 | 35395.13 | 9.56 | no_map |
| RWAUSDT | IDLE | 0.21 | 0.39 | 0.15 | 0.02 | 52988.77 | 7.73 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
