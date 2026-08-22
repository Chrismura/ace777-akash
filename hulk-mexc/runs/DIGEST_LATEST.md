# Hulk DIGEST — 2026-08-22T00:17:21Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : XRPUSDT, HBARUSDT, QAITUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, TELUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT
- Watch only : QNTUSDT, FLUIDUSDT, RWAUSDT

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| PYTHUSDT | IDLE | 1.77 | 6.39 | 1.63 | 0.1 | 6318923.06 | 4.1 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 2.07 | 8.23 | 2.78 | 0.13 | 143739659.91 | 3.49 | n/a |
| HBARUSDT | IDLE | 2.84 | 6.36 | 2.33 | 0.07 | 929816.43 | 1.27 | empty_tvl |
| ZBCNUSDT | IDLE | 2.91 | 11.25 | 3.43 | 0.11 | 516376.71 | 31.65 | n/a |
| CCUSDT | IDLE | 1.98 | 7.42 | 2.11 | 0.12 | 644393.87 | 9.89 | no_map |
| WUSDT | IDLE | 2.73 | 6.91 | 0.87 | 0.08 | 381536.6 | 17.32 | tvl≈1,628,401,619 |
| CHIPUSDT | IDLE | 1.56 | 3.56 | 0.27 | 0.05 | 545199.88 | 3.06 | no_map |
| BIOUSDT | IDLE | 2.3 | 5.04 | 1.17 | 0.02 | 186644.64 | 3.1 | n/a |
| EDELUSDT | IDLE | 2.6 | 5.5 | 1.63 | -0.01 | 79841.46 | 11.03 | no_map |
| RIZEUSDT | IDLE | 2.24 | 9.82 | 3.37 | 0.14 | 59441.4 | 45.4 | no_map |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.01 | 3715.41 | 19.88 | no_map |
| TELUSDT | IDLE | 2.84 | 6.89 | 0.66 | 0.05 | 189999.92 | 51.49 | no_map |
| QNTUSDT | IDLE | 2.58 | 5.42 | 1.7 | 0.06 | 169893.99 | 10.64 | n/a |
| KITEUSDT | IDLE | 1.08 | 3.12 | 0.68 | 0.09 | 61427.85 | 11.05 | no_map |
| RWAINCUSDT | IDLE | 1.69 | 2.99 | 2.54 | 0.02 | 10272.52 | 59.19 | no_map |
| REDUSDT | IDLE | 0.57 | 4.91 | 2.3 | 0.2 | 157687.59 | 52.96 | tvl≈2,226,572 |
| RWAUSDT | IDLE | 1.08 | 2.08 | 0.49 | 0.03 | 54599.85 | 24.64 | no_map |
| FLUIDUSDT | IDLE | 1.17 | 2.87 | 0.66 | 0.09 | 4845.77 | 21.84 | tvl≈2,594,160,978 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
