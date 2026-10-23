# Hulk DIGEST — 2026-10-23T13:19:46Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| XRPUSDT | IDLE | 0.68 | 1.2 | 1.13 | -0.01 | 25885858.34 | 0.76 | n/a |
| ETHUSDT | IDLE | 0.49 | 0.89 | 0.64 | -0.0 | 222567825.88 | 0.08 | no_map |
| BTCUSDT | IDLE | 0.3 | 0.55 | 0.3 | -0.0 | 321587471.94 | 0.04 | no_map |
| QNTUSDT | IDLE | 2.63 | 5.73 | 4.51 | -0.07 | 1112002.36 | 8.84 | n/a |
| PYTHUSDT | IDLE | 1.98 | 3.46 | 3.34 | -0.04 | 691360.16 | 1.4 | tvl≈162,477,830 |
| WUSDT | IDLE | 2.08 | 3.68 | 3.24 | -0.0 | 613398.59 | 16.56 | tvl≈1,541,605,918 |
| ZBCNUSDT | IDLE | 2.88 | 6.14 | 0.47 | -0.01 | 163625.37 | 11.06 | n/a |
| EDELUSDT | IDLE | 1.62 | 3.03 | 1.46 | -0.03 | 421587.41 | 9.43 | no_map |
| CHIPUSDT | IDLE | 2.79 | 5.18 | 4.88 | 0.02 | 121093.11 | 15.9 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.5 | 10.85 | 6.72 | -0.09 | 48726.61 | 63.43 | no_map |
| CCUSDT | IDLE | 0.99 | 1.92 | 0.43 | 0.01 | 189419.58 | 8.68 | no_map |
| RWAINCUSDT | IDLE | 1.21 | 2.24 | 1.15 | 0.02 | 50421.97 | 5.55 | no_map |
| REDUSDT | IDLE | 0.93 | 1.62 | 1.6 | -0.02 | 77090.42 | 17.24 | tvl≈3,495,614 |
| HBARUSDT | IDLE | 1.01 | 1.89 | 0.85 | -0.01 | 331495.83 | 6.28 | empty_tvl |
| BIOUSDT | IDLE | 0.82 | 1.43 | 1.37 | -0.0 | 60360.04 | 8.4 | n/a |
| KITEUSDT | IDLE | 0.87 | 1.62 | 0.84 | 0.01 | 57505.58 | 13.26 | no_map |
| LAUSDT | IDLE | 2.08 | 3.83 | 2.14 | 0.01 | 56099.49 | 25.11 | no_map |
| FLUIDUSDT | IDLE | 1.97 | 3.44 | 3.33 | -0.04 | 9524.6 | 18.33 | tvl≈2,206,192,085 |
| WAXLUSDT | IDLE | 1.0 | 1.84 | 1.04 | -0.02 | 57023.79 | 37.77 | no_map |
| IOTAUSDT | IDLE | 0.59 | 1.07 | 0.73 | -0.0 | 65872.72 | 13.38 | no_map |
| RWAUSDT | IDLE | 0.36 | 0.71 | 0.08 | 0.01 | 51190.9 | 15.71 | no_map |
| MNSRYUSDT | IDLE | 0.7 | 1.25 | 0.96 | -0.0 | 36461.72 | 74.39 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
