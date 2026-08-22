# Hulk DIGEST — 2026-08-22T08:42:38Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.18 | 19.14 | 10.42 | 0.03 | 31616038.21 | 21.99 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.81 | 23.87 | 11.75 | 0.1 | 224468728.1 | 6.01 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 15.8 | 10.18 | 0.02 | 1330075.37 | 3.84 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 24.54 | 12.32 | -0.09 | 688566.86 | 6.71 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.32 | 17.58 | 9.21 | 0.02 | 601589.83 | 9.44 | tvl≈1,600,543,155 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.2 | 29.98 | 10.31 | -0.05 | 257158.09 | 3.22 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.16 | 42.01 | 12.36 | 0.05 | 155482.46 | 12.42 | tvl≈2,081,438 |
| CCUSDT | IDLE | 2.09 | 11.25 | 3.81 | 0.16 | 805612.93 | 9.12 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.3 | 8.47 | 6.65 | -0.01 | 518410.58 | 25.09 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.4 | 13.91 | 9.43 | 0.02 | 192858.29 | 7.79 | n/a |
| KITEUSDT | IDLE | 3.81 | 9.68 | 4.13 | 0.06 | 73689.66 | 11.83 | no_map |
| EDELUSDT | IDLE | 2.28 | 4.52 | 3.46 | -0.04 | 86818.53 | 33.61 | no_map |
| FLUIDUSDT | IDLE | 3.79 | 7.38 | 4.56 | 0.03 | 6885.76 | 54.23 | tvl≈2,562,763,298 |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.01 | 11076.52 | 112.63 | no_map |
| TELUSDT | IDLE | 2.34 | 5.85 | 5.53 | -0.02 | 174663.48 | 57.46 | no_map |
| QAITUSDT | IDLE | 1.49 | 2.91 | 0.43 | 0.01 | 3202.55 | 66.45 | no_map |
| RIZEUSDT | IDLE | 0.88 | 3.73 | 1.78 | 0.0 | 52283.67 | 44.83 | no_map |
| RWAUSDT | IDLE | 1.75 | 3.29 | 1.43 | 0.04 | 58339.31 | 8.08 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
