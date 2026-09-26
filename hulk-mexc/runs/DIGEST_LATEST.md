# Hulk DIGEST — 2026-09-26T20:31:21Z

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
| XRPUSDT | IDLE | 1.49 | 2.67 | 2.06 | -0.03 | 39886105.02 | 1.31 | n/a |
| ETHUSDT | IDLE | 0.3 | 0.54 | 0.43 | -0.0 | 110549647.37 | 0.04 | no_map |
| QNTUSDT | IDLE | 1.97 | 13.91 | 2.98 | 0.24 | 1459409.88 | 11.58 | n/a |
| BTCUSDT | IDLE | 0.13 | 0.24 | 0.12 | 0.0 | 330100060.56 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.32 | 6.03 | 1.78 | 0.08 | 1053183.63 | 6.32 | tvl≈174,537,837 |
| CCUSDT | IDLE | 2.09 | 5.3 | 3.73 | 0.04 | 855789.72 | 8.14 | no_map |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.95 | 7.42 | 6.91 | -0.01 | 112307.88 | 16.45 | no_map |
| WUSDT | IDLE | 1.81 | 3.9 | 2.52 | 0.05 | 559418.94 | 9.31 | tvl≈1,878,149,959 |
| RWAINCUSDT | IDLE | 3.77 | 13.77 | 3.46 | 0.05 | 9773.82 | 82.07 | no_map |
| KITEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.73 | 9.74 | 1.59 | 0.12 | 110273.51 | 13.48 | no_map |
| EDELUSDT | IDLE | 2.34 | 4.21 | 3.08 | 0.02 | 167366.36 | 6.62 | no_map |
| ZBCNUSDT | IDLE | 2.38 | 4.24 | 3.42 | -0.03 | 195323.37 | 27.96 | n/a |
| HBARUSDT | IDLE | 1.55 | 2.74 | 2.43 | -0.02 | 546368.49 | 1.07 | empty_tvl |
| BIOUSDT | IDLE | 1.91 | 3.35 | 3.09 | -0.03 | 109423.97 | 6.25 | n/a |
| REDUSDT | IDLE | 1.05 | 1.86 | 1.64 | -0.04 | 58507.87 | 12.49 | tvl≈3,072,611 |
| RIZEUSDT | IDLE | 1.17 | 2.9 | 1.23 | 0.06 | 48040.81 | 59.6 | no_map |
| TELUSDT | IDLE | 1.77 | 3.41 | 0.85 | -0.02 | 125223.54 | 36.97 | no_map |
| FLUIDUSDT | IDLE | 1.16 | 2.02 | 1.98 | -0.01 | 549.6 | 21.62 | tvl≈2,583,652,623 |
| RWAUSDT | IDLE | 0.67 | 1.23 | 0.78 | 0.02 | 56659.25 | 14.35 | no_map |
| MNSRYUSDT | IDLE | 0.26 | 0.51 | 0.06 | -0.0 | 38650.3 | 16.57 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
