# Hulk DIGEST — 2026-09-06T04:29:18Z

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
| XRPUSDT | IDLE | 1.13 | 2.12 | 0.91 | 0.02 | 24444628.36 | 1.41 | n/a |
| ETHUSDT | IDLE | 0.77 | 1.46 | 0.48 | 0.02 | 202191340.94 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.26 | 0.49 | 0.24 | 0.0 | 375078030.87 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.79 | 5.29 | 1.91 | 0.04 | 441381.53 | 1.78 | tvl≈122,790,024 |
| CHIPUSDT | IDLE | 2.55 | 5.64 | 3.05 | 0.05 | 424831.27 | 1.7 | no_map |
| RWAINCUSDT | IDLE | 2.76 | 5.37 | 0.94 | 0.03 | 8988.84 | 5.25 | no_map |
| CCUSDT | IDLE | 1.38 | 2.52 | 1.66 | 0.01 | 294518.54 | 9.13 | no_map |
| WUSDT | IDLE | 1.77 | 3.22 | 2.16 | 0.03 | 174982.63 | 11.93 | tvl≈1,663,589,288 |
| KITEUSDT | IDLE | 2.12 | 4.06 | 1.15 | -0.04 | 65368.63 | 9.28 | no_map |
| ZBCNUSDT | IDLE | 1.35 | 2.68 | 0.14 | 0.0 | 208073.68 | 16.51 | n/a |
| HBARUSDT | IDLE | 1.5 | 2.85 | 1.0 | 0.03 | 416268.26 | 1.23 | empty_tvl |
| REDUSDT | IDLE | 1.48 | 2.67 | 1.92 | 0.01 | 59275.78 | 8.7 | tvl≈2,345,447 |
| RIZEUSDT | IDLE | 1.26 | 8.56 | 0.75 | 0.07 | 119409.06 | 56.04 | no_map |
| BIOUSDT | IDLE | 0.94 | 1.73 | 1.06 | 0.03 | 95748.79 | 7.15 | n/a |
| EDELUSDT | IDLE | 0.23 | 3.05 | 1.76 | 0.01 | 113507.91 | 18.83 | no_map |
| RWAUSDT | IDLE | 1.53 | 2.7 | 2.35 | 0.03 | 53215.47 | 21.27 | no_map |
| TELUSDT | IDLE | 1.38 | 2.68 | 0.58 | 0.0 | 72725.94 | 11.68 | no_map |
| MNSRYUSDT | IDLE | 1.38 | 2.64 | 0.84 | 0.02 | 39618.8 | 5.37 | no_map |
| QNTUSDT | IDLE | 1.29 | 2.33 | 1.69 | 0.03 | 37322.63 | 4.6 | n/a |
| FLUIDUSDT | IDLE | 0.91 | 1.82 | 0.0 | 0.03 | 390.92 | 22.03 | tvl≈2,661,776,506 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
