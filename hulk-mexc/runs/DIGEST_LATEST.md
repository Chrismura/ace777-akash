# Hulk DIGEST — 2026-09-06T14:46:36Z

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
| XRPUSDT | IDLE | 1.08 | 2.0 | 1.05 | -0.0 | 26143954.04 | 1.42 | n/a |
| ETHUSDT | IDLE | 0.92 | 1.72 | 0.85 | 0.01 | 253480528.38 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.55 | 1.03 | 0.42 | -0.0 | 407828958.3 | 0.53 | no_map |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.24 | 8.0 | 6.37 | -0.02 | 398585.24 | 1.74 | no_map |
| PYTHUSDT | IDLE | 2.59 | 4.73 | 2.99 | -0.0 | 486450.15 | 1.83 | tvl≈125,095,039 |
| WUSDT | IDLE | 2.44 | 4.42 | 3.03 | 0.02 | 248591.69 | 13.76 | tvl≈1,682,875,562 |
| ZBCNUSDT | IDLE | 1.84 | 3.32 | 2.37 | -0.02 | 199764.85 | 5.34 | n/a |
| EDELUSDT | IDLE | 2.63 | 4.6 | 4.4 | -0.01 | 68864.23 | 38.28 | no_map |
| RIZEUSDT | IDLE | 2.01 | 11.61 | 9.55 | -0.01 | 80778.06 | 66.95 | no_map |
| REDUSDT | IDLE | 2.31 | 4.14 | 3.21 | 0.02 | 64169.83 | 11.84 | tvl≈2,387,078 |
| BIOUSDT | IDLE | 2.09 | 3.74 | 2.97 | -0.02 | 91791.94 | 3.68 | n/a |
| CCUSDT | IDLE | 1.11 | 1.99 | 1.49 | 0.0 | 319977.12 | 6.38 | no_map |
| RWAINCUSDT | IDLE | 2.09 | 4.5 | 2.45 | 0.06 | 5902.17 | 5.15 | no_map |
| HBARUSDT | IDLE | 0.92 | 1.66 | 1.19 | 0.0 | 406565.32 | 1.24 | empty_tvl |
| KITEUSDT | IDLE | 1.11 | 2.05 | 1.15 | 0.01 | 61066.54 | 7.88 | no_map |
| TELUSDT | IDLE | 0.94 | 1.65 | 1.56 | -0.0 | 65548.22 | 11.76 | no_map |
| QNTUSDT | IDLE | 0.82 | 1.52 | 0.79 | 0.03 | 38563.89 | 4.59 | n/a |
| RWAUSDT | IDLE | 0.76 | 1.37 | 0.99 | -0.02 | 52921.53 | 28.72 | no_map |
| MNSRYUSDT | IDLE | 0.48 | 0.89 | 0.53 | 0.02 | 41511.13 | 25.53 | no_map |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | 0.02 | 353.17 | 19.81 | tvl≈2,659,762,913 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
