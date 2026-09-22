# Hulk DIGEST — 2026-09-22T05:08:43Z

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
| XRPUSDT | IDLE | 1.04 | 2.45 | 1.84 | 0.07 | 118643871.28 | 1.98 | n/a |
| ETHUSDT | IDLE | 1.06 | 1.87 | 1.67 | 0.03 | 712482751.98 | 0.22 | no_map |
| BTCUSDT | IDLE | 0.87 | 1.55 | 1.33 | 0.05 | 1122812841.68 | 0.0 | no_map |
| HBARUSDT | IDLE | 1.91 | 4.44 | 3.0 | 0.07 | 1216818.7 | 1.08 | empty_tvl |
| PYTHUSDT | IDLE | 1.46 | 3.13 | 2.25 | 0.04 | 792197.37 | 6.3 | tvl≈142,076,380 |
| CCUSDT | IDLE | 1.63 | 3.01 | 1.72 | 0.06 | 647737.9 | 6.78 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.85 | 27.81 | 12.06 | -0.16 | 53176.21 | 88.24 | no_map |
| WUSDT | IDLE | 1.32 | 2.37 | 1.74 | -0.02 | 481233.31 | 5.95 | tvl≈1,803,003,578 |
| ZBCNUSDT | IDLE | 1.74 | 3.76 | 1.23 | 0.03 | 269742.79 | 35.29 | n/a |
| KITEUSDT | IDLE | 2.08 | 4.02 | 0.95 | 0.06 | 83374.36 | 10.68 | no_map |
| EDELUSDT | IDLE | 1.29 | 8.45 | 0.46 | 0.12 | 236205.22 | 43.4 | no_map |
| CHIPUSDT | IDLE | 1.36 | 5.12 | 3.21 | 0.1 | 171208.3 | 17.13 | no_map |
| REDUSDT | IDLE | 1.84 | 3.48 | 1.35 | 0.03 | 98580.87 | 16.09 | tvl≈2,814,179 |
| BIOUSDT | IDLE | 1.45 | 2.69 | 1.43 | 0.03 | 127989.67 | 6.9 | n/a |
| RWAINCUSDT | IDLE | 1.03 | 2.4 | 2.34 | 0.05 | 22764.52 | 66.74 | no_map |
| QNTUSDT | IDLE | 1.21 | 2.29 | 0.83 | 0.02 | 121610.2 | 4.49 | n/a |
| TELUSDT | IDLE | 0.98 | 2.86 | 1.69 | 0.07 | 118364.5 | 43.17 | no_map |
| MNSRYUSDT | IDLE | 0.75 | 1.37 | 0.82 | 0.02 | 41139.34 | 9.02 | no_map |
| RWAUSDT | IDLE | 0.66 | 1.17 | 1.01 | 0.0 | 57903.22 | 14.56 | no_map |
| FLUIDUSDT | IDLE | 0.68 | 1.33 | 0.18 | 0.09 | 13282.37 | 19.8 | tvl≈2,659,381,808 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
