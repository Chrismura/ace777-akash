# Hulk DIGEST — 2026-10-10T16:59:50Z

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
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 3.83 | 12.38 | 6.53 | -0.0 | 1226749.36 | 9.04 | tvl≈1,647,106,296 |
| ETHUSDT | IDLE | 0.48 | 0.89 | 0.46 | 0.01 | 86089938.08 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.39 | 0.7 | 0.55 | 0.01 | 15481449.62 | 1.42 | n/a |
| QNTUSDT | IDLE | 3.63 | 6.57 | 4.59 | -0.01 | 1215938.92 | 0.41 | n/a |
| BTCUSDT | IDLE | 0.19 | 0.36 | 0.08 | 0.0 | 183380553.9 | 0.0 | no_map |
| PYTHUSDT | IDLE | 1.21 | 2.34 | 0.53 | -0.05 | 947947.42 | 3.79 | tvl≈175,240,177 |
| EDELUSDT | IDLE | 2.81 | 5.64 | 4.61 | -0.04 | 219673.93 | 10.45 | no_map |
| CHIPUSDT | IDLE | 2.63 | 8.93 | 3.95 | 0.08 | 100865.61 | 11.12 | no_map |
| KITEUSDT | IDLE | 2.18 | 5.87 | 2.79 | 0.06 | 72007.04 | 17.17 | no_map |
| CCUSDT | IDLE | 0.96 | 1.69 | 1.59 | -0.03 | 360853.16 | 6.71 | no_map |
| ZBCNUSDT | IDLE | 1.05 | 1.96 | 0.99 | -0.01 | 202232.75 | 10.48 | n/a |
| TELUSDT | IDLE | 2.89 | 5.22 | 3.72 | -0.05 | 123064.99 | 44.79 | no_map |
| BIOUSDT | IDLE | 1.26 | 2.45 | 0.41 | 0.04 | 85496.41 | 6.87 | n/a |
| HBARUSDT | IDLE | 0.91 | 1.69 | 0.9 | 0.02 | 354519.22 | 1.08 | empty_tvl |
| REDUSDT | IDLE | 0.99 | 1.87 | 0.7 | 0.02 | 54461.6 | 10.62 | tvl≈3,785,310 |
| RWAINCUSDT | IDLE | 0.89 | 1.73 | 0.29 | -0.04 | 8638.04 | 38.99 | no_map |
| RIZEUSDT | IDLE | 0.55 | 1.26 | 0.77 | -0.0 | 43430.39 | 31.78 | no_map |
| FLUIDUSDT | IDLE | 0.66 | 1.94 | 1.28 | 0.0 | 15311.85 | 21.18 | tvl≈2,429,079,103 |
| RWAUSDT | IDLE | 0.4 | 0.71 | 0.55 | -0.0 | 54439.19 | 7.86 | no_map |
| MNSRYUSDT | IDLE | 0.23 | 0.43 | 0.19 | 0.0 | 38811.27 | 23.01 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
