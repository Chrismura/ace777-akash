# Hulk DIGEST — 2026-09-01T15:25:03Z

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
| XRPUSDT | IDLE | 1.14 | 2.1 | 1.17 | 0.0 | 30129146.71 | 2.19 | n/a |
| ETHUSDT | IDLE | 0.84 | 1.54 | 1.0 | -0.01 | 291229885.19 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.63 | 1.15 | 0.73 | -0.01 | 528531029.03 | 0.0 | no_map |
| CHIPUSDT | IDLE | 3.57 | 14.71 | 2.74 | 0.1 | 465912.73 | 18.57 | no_map |
| PYTHUSDT | IDLE | 1.55 | 3.4 | 1.96 | 0.06 | 598662.97 | 2.0 | tvl≈112,789,076 |
| CCUSDT | IDLE | 2.45 | 4.32 | 3.86 | -0.01 | 388322.22 | 8.59 | no_map |
| ZBCNUSDT | IDLE | 2.59 | 4.82 | 2.34 | 0.03 | 225142.34 | 17.15 | n/a |
| WUSDT | IDLE | 2.25 | 4.35 | 0.94 | 0.06 | 256789.03 | 12.4 | tvl≈1,536,961,838 |
| KITEUSDT | IDLE | 2.91 | 5.66 | 1.0 | 0.04 | 60957.95 | 21.19 | no_map |
| RIZEUSDT | IDLE | 1.85 | 4.79 | 2.96 | -0.07 | 43718.38 | 20.14 | no_map |
| REDUSDT | IDLE | 1.9 | 3.77 | 0.2 | 0.05 | 65549.92 | 22.28 | tvl≈2,031,843 |
| EDELUSDT | IDLE | 0.93 | 6.17 | 4.04 | -0.08 | 175451.98 | 35.06 | no_map |
| BIOUSDT | IDLE | 1.22 | 2.26 | 1.18 | -0.01 | 66802.26 | 3.85 | n/a |
| HBARUSDT | IDLE | 1.04 | 1.83 | 1.64 | 0.01 | 231833.14 | 1.35 | empty_tvl |
| RWAINCUSDT | IDLE | 1.09 | 1.95 | 1.56 | -0.01 | 5633.26 | 52.96 | no_map |
| QNTUSDT | IDLE | 1.82 | 3.58 | 0.46 | 0.03 | 36654.53 | 1.58 | n/a |
| TELUSDT | IDLE | 1.25 | 2.18 | 2.08 | 0.01 | 97142.79 | 23.54 | no_map |
| RWAUSDT | IDLE | 1.09 | 2.57 | 1.37 | -0.0 | 62560.87 | 23.12 | no_map |
| MNSRYUSDT | IDLE | 0.64 | 1.13 | 0.95 | -0.0 | 32699.05 | 27.24 | no_map |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.01 | 396.53 | 21.91 | tvl≈2,602,518,957 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
