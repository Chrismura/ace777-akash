# Hulk DIGEST — 2026-09-10T11:18:21Z

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
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 4.15 | 209.6 | 51.25 | -0.51 | 90252.73 | 114.69 | no_map |
| XRPUSDT | IDLE | 0.83 | 1.52 | 0.98 | -0.03 | 41188051.0 | 1.45 | n/a |
| BTCUSDT | IDLE | 0.58 | 1.06 | 0.68 | -0.01 | 528747693.19 | 0.0 | no_map |
| ETHUSDT | IDLE | 0.57 | 1.04 | 0.72 | -0.01 | 328708543.49 | 0.16 | no_map |
| PYTHUSDT | IDLE | 1.26 | 3.25 | 2.43 | -0.04 | 997326.04 | 1.93 | tvl≈118,577,544 |
| CCUSDT | IDLE | 2.54 | 4.58 | 3.36 | -0.04 | 696767.86 | 5.89 | no_map |
| KITEUSDT | IDLE | 2.99 | 6.55 | 3.24 | -0.03 | 56989.82 | 11.89 | no_map |
| WUSDT | IDLE | 1.46 | 3.44 | 2.83 | -0.06 | 226584.06 | 10.45 | tvl≈1,499,231,640 |
| ZBCNUSDT | IDLE | 1.8 | 3.24 | 2.37 | 0.02 | 149648.47 | 27.39 | n/a |
| EDELUSDT | IDLE | 1.1 | 3.94 | 3.27 | 0.08 | 238543.68 | 17.81 | no_map |
| BIOUSDT | IDLE | 0.9 | 2.11 | 0.27 | -0.05 | 99071.98 | 3.91 | n/a |
| REDUSDT | IDLE | 1.07 | 2.38 | 1.44 | -0.07 | 65853.53 | 19.48 | tvl≈2,276,455 |
| CHIPUSDT | IDLE | 0.69 | 3.96 | 2.6 | -0.17 | 97260.8 | 16.61 | no_map |
| HBARUSDT | IDLE | 0.93 | 1.69 | 1.09 | -0.02 | 348847.62 | 1.31 | empty_tvl |
| RWAINCUSDT | IDLE | 1.3 | 2.27 | 2.16 | -0.01 | 6086.1 | 123.94 | no_map |
| FLUIDUSDT | IDLE | 1.27 | 2.61 | 2.55 | -0.07 | 1382.71 | 17.98 | tvl≈2,653,600,189 |
| TELUSDT | IDLE | 1.07 | 1.96 | 1.21 | 0.01 | 86931.02 | 50.04 | no_map |
| QNTUSDT | IDLE | 0.83 | 1.48 | 1.22 | -0.02 | 38440.52 | 3.02 | n/a |
| RWAUSDT | IDLE | 0.27 | 0.52 | 0.15 | -0.03 | 53658.13 | 14.94 | no_map |
| MNSRYUSDT | IDLE | 0.39 | 0.72 | 0.41 | -0.02 | 24749.67 | 37.34 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
