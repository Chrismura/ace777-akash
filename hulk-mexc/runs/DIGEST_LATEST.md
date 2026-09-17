# Hulk DIGEST — 2026-09-17T13:15:45Z

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
| ETHUSDT | IDLE | 1.12 | 2.1 | 0.89 | 0.02 | 378187948.24 | 0.94 | no_map |
| XRPUSDT | IDLE | 0.97 | 1.8 | 0.9 | 0.02 | 57265772.99 | 2.3 | n/a |
| BTCUSDT | IDLE | 0.68 | 1.27 | 0.64 | 0.01 | 489495932.88 | 0.13 | no_map |
| CCUSDT | IDLE | 1.04 | 3.81 | 1.98 | 0.11 | 662458.54 | 6.94 | no_map |
| PYTHUSDT | IDLE | 1.0 | 1.98 | 0.07 | 0.03 | 551580.14 | 3.66 | tvl≈120,961,665 |
| CHIPUSDT | IDLE | 2.47 | 7.36 | 4.86 | 0.01 | 139575.69 | 15.89 | no_map |
| EDELUSDT | IDLE | 2.36 | 7.02 | 1.64 | -0.06 | 187821.82 | 15.84 | no_map |
| REDUSDT | IDLE | 2.02 | 3.82 | 3.67 | 0.02 | 63842.5 | 17.59 | tvl≈2,384,561 |
| HBARUSDT | IDLE | 1.11 | 2.11 | 0.77 | 0.01 | 534165.33 | 1.34 | empty_tvl |
| RIZEUSDT | IDLE | 1.32 | 14.59 | 11.29 | -0.31 | 53646.81 | 125.93 | no_map |
| WUSDT | IDLE | 0.9 | 1.77 | 0.69 | 0.06 | 207873.09 | 13.97 | tvl≈1,454,985,536 |
| ZBCNUSDT | IDLE | 1.04 | 1.96 | 0.8 | 0.01 | 175224.95 | 18.99 | n/a |
| RWAINCUSDT | IDLE | 1.64 | 2.93 | 2.33 | 0.0 | 17654.81 | 23.31 | no_map |
| KITEUSDT | IDLE | 1.05 | 3.47 | 3.15 | 0.05 | 68004.16 | 15.29 | no_map |
| BIOUSDT | IDLE | 1.0 | 1.85 | 0.99 | 0.02 | 68636.75 | 11.94 | n/a |
| RWAUSDT | IDLE | 1.66 | 3.31 | 0.07 | 0.02 | 58825.67 | 22.4 | no_map |
| TELUSDT | IDLE | 1.12 | 2.17 | 0.48 | 0.02 | 97507.04 | 27.55 | no_map |
| QNTUSDT | IDLE | 1.17 | 2.24 | 0.73 | 0.04 | 34506.88 | 4.87 | n/a |
| MNSRYUSDT | IDLE | 0.7 | 1.33 | 0.46 | 0.01 | 39183.21 | 9.81 | no_map |
| FLUIDUSDT | IDLE | 0.36 | 0.66 | 0.36 | 0.02 | 844.09 | 21.78 | tvl≈2,636,607,975 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
