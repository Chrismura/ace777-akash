# Hulk DIGEST — 2026-10-14T09:14:07Z

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
| PYTHUSDT | IDLE | 2.6 | 5.23 | 2.77 | -0.02 | 1818135.63 | 3.69 | tvl≈181,249,525 |
| WUSDT | IDLE | 0.82 | 5.16 | 2.41 | -0.15 | 3725961.83 | 6.12 | tvl≈1,661,900,131 |
| XRPUSDT | IDLE | 0.95 | 1.73 | 1.15 | 0.0 | 29882986.88 | 1.46 | n/a |
| ETHUSDT | IDLE | 0.65 | 1.16 | 0.9 | -0.0 | 119680728.31 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.53 | 0.94 | 0.79 | -0.0 | 314055315.58 | 0.0 | no_map |
| QNTUSDT | IDLE | 1.27 | 3.02 | 2.76 | -0.05 | 1711570.97 | 0.47 | n/a |
| CCUSDT | IDLE | 1.46 | 2.9 | 2.44 | 0.01 | 571652.19 | 8.17 | no_map |
| CHIPUSDT | IDLE | 2.8 | 5.01 | 3.91 | -0.05 | 80226.88 | 8.84 | no_map |
| KITEUSDT | IDLE | 2.25 | 7.12 | 3.55 | 0.08 | 75793.43 | 8.75 | no_map |
| EDELUSDT | IDLE | 1.26 | 2.46 | 0.35 | 0.03 | 216333.34 | 17.38 | no_map |
| REDUSDT | IDLE | 1.54 | 2.7 | 2.55 | -0.01 | 73976.65 | 15.39 | tvl≈3,962,736 |
| RIZEUSDT | IDLE | 1.75 | 5.95 | 1.43 | 0.04 | 53183.89 | 48.98 | no_map |
| BIOUSDT | IDLE | 1.03 | 1.83 | 1.51 | -0.01 | 69272.08 | 3.65 | n/a |
| ZBCNUSDT | IDLE | 0.52 | 0.91 | 0.81 | -0.02 | 200314.7 | 10.12 | n/a |
| RWAINCUSDT | IDLE | 0.98 | 2.01 | 1.11 | -0.07 | 33196.72 | 25.62 | no_map |
| HBARUSDT | IDLE | 0.9 | 1.61 | 1.23 | -0.01 | 307117.98 | 4.62 | empty_tvl |
| FLUIDUSDT | IDLE | 1.63 | 4.76 | 3.34 | 0.07 | 20286.23 | 21.24 | tvl≈2,377,835,295 |
| TELUSDT | IDLE | 1.03 | 1.91 | 0.94 | 0.03 | 116131.64 | 33.43 | no_map |
| RWAUSDT | IDLE | 0.4 | 0.78 | 0.31 | -0.01 | 56295.34 | 7.77 | no_map |
| MNSRYUSDT | IDLE | 0.02 | 0.03 | 0.01 | -0.01 | 38002.95 | 5.58 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
