# Hulk DIGEST — 2026-09-17T03:14:45Z

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
| XRPUSDT | IDLE | 1.23 | 2.36 | 0.69 | 0.01 | 56764776.04 | 2.3 | n/a |
| ETHUSDT | IDLE | 1.21 | 2.35 | 0.49 | 0.01 | 381151143.0 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.78 | 1.49 | 0.45 | 0.01 | 516174324.52 | 0.0 | no_map |
| CCUSDT | IDLE | 2.16 | 7.73 | 5.33 | 0.06 | 562976.35 | 6.16 | no_map |
| PYTHUSDT | IDLE | 2.87 | 5.71 | 0.15 | 0.03 | 427320.66 | 1.83 | tvl≈117,612,446 |
| WUSDT | IDLE | 2.75 | 5.27 | 1.72 | 0.01 | 225767.25 | 15.24 | tvl≈1,449,243,001 |
| CHIPUSDT | IDLE | 3.16 | 7.1 | 3.67 | -0.04 | 81812.67 | 16.55 | no_map |
| RWAINCUSDT | IDLE | 3.15 | 5.77 | 3.54 | -0.02 | 20839.24 | 5.83 | no_map |
| REDUSDT | IDLE | 2.15 | 4.49 | 1.04 | 0.01 | 64001.94 | 18.21 | tvl≈2,354,127 |
| BIOUSDT | IDLE | 1.92 | 3.74 | 0.71 | 0.02 | 77857.48 | 7.9 | n/a |
| EDELUSDT | IDLE | 0.88 | 3.78 | 2.75 | 0.03 | 267260.76 | 22.99 | no_map |
| ZBCNUSDT | IDLE | 1.27 | 2.54 | 0.0 | 0.03 | 162667.21 | 15.92 | n/a |
| KITEUSDT | IDLE | 1.17 | 4.0 | 2.61 | 0.05 | 66841.11 | 13.29 | no_map |
| HBARUSDT | IDLE | 1.16 | 2.27 | 0.38 | -0.01 | 301822.07 | 1.35 | empty_tvl |
| RIZEUSDT | IDLE | 0.82 | 10.2 | 7.77 | 0.2 | 62865.64 | 97.93 | no_map |
| TELUSDT | IDLE | 1.03 | 1.88 | 1.23 | -0.02 | 115385.43 | 41.61 | no_map |
| QNTUSDT | IDLE | 0.74 | 1.32 | 1.08 | -0.0 | 37486.9 | 8.24 | n/a |
| RWAUSDT | IDLE | 0.55 | 0.98 | 0.75 | 0.01 | 55248.54 | 15.03 | no_map |
| MNSRYUSDT | IDLE | 0.51 | 0.97 | 0.31 | -0.0 | 33681.82 | 41.04 | no_map |
| FLUIDUSDT | IDLE | 0.0 | 0.0 | 0.0 | -0.02 | 1573.23 | 22.01 | tvl≈2,641,825,025 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
