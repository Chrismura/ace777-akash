# Hulk DIGEST — 2026-10-16T11:59:50Z

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
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 2.81 | 6.77 | 5.92 | 0.02 | 1822252.44 | 4.8 | tvl≈1,652,485,183 |
| PYTHUSDT | IDLE | 1.35 | 7.67 | 5.54 | 0.04 | 3892536.89 | 3.33 | tvl≈206,072,259 |
| ETHUSDT | IDLE | 1.1 | 2.12 | 0.6 | 0.05 | 241951374.11 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.83 | 1.58 | 0.51 | 0.03 | 31270614.87 | 2.23 | n/a |
| BTCUSDT | IDLE | 0.69 | 1.33 | 0.31 | 0.02 | 413870088.88 | 0.0 | no_map |
| QNTUSDT | IDLE | 1.37 | 3.89 | 1.19 | 0.06 | 1244552.1 | 0.48 | n/a |
| CCUSDT | IDLE | 2.97 | 5.23 | 4.79 | -0.04 | 419295.52 | 10.61 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 3.29 | 9.55 | 5.9 | -0.02 | 68279.25 | 59.57 | no_map |
| RWAINCUSDT | IDLE | 2.97 | 5.35 | 3.98 | -0.01 | 24590.69 | 14.94 | no_map |
| EDELUSDT | IDLE | 2.08 | 5.56 | 0.49 | -0.0 | 214894.06 | 22.96 | no_map |
| ZBCNUSDT | IDLE | 1.45 | 2.98 | 1.17 | 0.04 | 216094.58 | 34.41 | n/a |
| REDUSDT | IDLE | 1.28 | 4.07 | 1.15 | -0.01 | 87480.43 | 7.27 | tvl≈3,681,377 |
| CHIPUSDT | IDLE | 0.75 | 3.82 | 3.13 | 0.12 | 181549.77 | 14.15 | no_map |
| KITEUSDT | IDLE | 1.39 | 2.74 | 0.31 | 0.03 | 70072.04 | 10.49 | no_map |
| BIOUSDT | IDLE | 0.94 | 1.79 | 0.61 | 0.05 | 69339.11 | 3.84 | n/a |
| HBARUSDT | IDLE | 0.87 | 1.83 | 0.08 | 0.07 | 268317.55 | 8.04 | empty_tvl |
| FLUIDUSDT | IDLE | 1.97 | 3.64 | 1.96 | -0.01 | 8041.97 | 21.05 | tvl≈2,265,195,612 |
| TELUSDT | IDLE | 0.94 | 2.15 | 0.55 | 0.06 | 93161.67 | 33.46 | no_map |
| RWAUSDT | IDLE | 0.45 | 0.87 | 0.16 | 0.02 | 51038.66 | 15.76 | no_map |
| MNSRYUSDT | IDLE | 0.11 | 0.21 | 0.1 | 0.01 | 39012.77 | 9.89 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
