# Hulk DIGEST — 2026-09-13T15:34:09Z

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
| XRPUSDT | IDLE | 0.88 | 1.65 | 0.72 | -0.02 | 15066912.25 | 2.23 | n/a |
| ETHUSDT | IDLE | 0.69 | 1.35 | 0.24 | -0.02 | 240998125.32 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.51 | 0.98 | 0.21 | -0.0 | 293656564.87 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.29 | 4.38 | 1.27 | 0.0 | 433528.11 | 1.82 | tvl≈121,266,979 |
| CHIPUSDT | IDLE | 2.33 | 8.2 | 7.3 | -0.13 | 89479.33 | 18.34 | no_map |
| WUSDT | IDLE | 1.65 | 3.13 | 1.1 | 0.01 | 259539.69 | 10.0 | tvl≈1,471,657,497 |
| EDELUSDT | IDLE | 1.59 | 7.01 | 1.56 | 0.08 | 203061.63 | 15.81 | no_map |
| ZBCNUSDT | IDLE | 1.58 | 2.96 | 1.3 | -0.03 | 204420.28 | 13.49 | n/a |
| CCUSDT | IDLE | 0.84 | 1.6 | 0.57 | -0.03 | 287583.59 | 10.51 | no_map |
| REDUSDT | IDLE | 1.65 | 2.93 | 2.44 | 0.01 | 60911.4 | 18.37 | tvl≈2,363,783 |
| RIZEUSDT | IDLE | 0.76 | 12.36 | 3.28 | -0.04 | 93266.6 | 38.27 | no_map |
| BIOUSDT | IDLE | 1.11 | 2.03 | 1.25 | -0.01 | 69798.9 | 7.88 | n/a |
| KITEUSDT | IDLE | 1.08 | 1.89 | 1.74 | 0.01 | 63051.69 | 10.22 | no_map |
| RWAINCUSDT | IDLE | 0.86 | 1.65 | 0.45 | -0.01 | 6692.72 | 5.61 | no_map |
| HBARUSDT | IDLE | 1.15 | 2.12 | 1.14 | 0.01 | 192998.91 | 1.32 | empty_tvl |
| TELUSDT | IDLE | 0.9 | 1.65 | 0.94 | -0.05 | 88995.43 | 18.9 | no_map |
| RWAUSDT | IDLE | 1.02 | 1.96 | 0.59 | -0.01 | 53533.93 | 14.89 | no_map |
| QNTUSDT | IDLE | 0.81 | 1.49 | 0.87 | -0.01 | 36998.87 | 4.69 | n/a |
| FLUIDUSDT | IDLE | 0.63 | 1.11 | 1.05 | -0.0 | 1582.44 | 22.11 | tvl≈2,651,589,241 |
| MNSRYUSDT | IDLE | 0.15 | 0.29 | 0.04 | -0.0 | 32414.65 | 13.9 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
