# Hulk DIGEST — 2026-08-28T17:06:39Z

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
| XRPUSDT | IDLE | 2.6 | 4.69 | 3.38 | -0.05 | 53386187.9 | 2.88 | n/a |
| CHIPUSDT | IDLE | 2.32 | 14.34 | 8.91 | 0.04 | 955399.93 | 11.58 | no_map |
| PYTHUSDT | IDLE | 2.32 | 5.81 | 3.24 | -0.06 | 955082.95 | 2.13 | tvl≈107,720,136 |
| QAITUSDT | IDLE | 2.44 | 32.58 | 21.02 | -0.19 | 70698.45 | 67.41 | no_map |
| CCUSDT | IDLE | 2.55 | 4.64 | 3.13 | -0.06 | 383068.85 | 9.1 | no_map |
| WUSDT | IDLE | 2.93 | 6.36 | 4.31 | -0.07 | 218868.48 | 12.05 | tvl≈1,539,835,919 |
| ZBCNUSDT | IDLE | 2.97 | 5.24 | 4.71 | -0.07 | 213068.3 | 10.72 | n/a |
| HBARUSDT | IDLE | 3.11 | 5.77 | 2.97 | -0.04 | 435484.41 | 1.32 | empty_tvl |
| BIOUSDT | IDLE | 2.67 | 5.99 | 3.54 | -0.05 | 95681.54 | 3.6 | n/a |
| REDUSDT | IDLE | 2.62 | 6.25 | 3.34 | -0.04 | 68445.7 | 12.43 | tvl≈1,966,229 |
| KITEUSDT | IDLE | 2.25 | 4.27 | 1.52 | -0.04 | 80749.79 | 10.36 | no_map |
| RWAUSDT | IDLE | 3.31 | 5.99 | 4.14 | 0.0 | 55371.88 | 16.63 | no_map |
| EDELUSDT | IDLE | 1.57 | 4.25 | 4.07 | -0.11 | 65324.6 | 17.68 | no_map |
| QNTUSDT | IDLE | 2.64 | 4.72 | 3.7 | -0.04 | 49814.31 | 6.55 | n/a |
| RIZEUSDT | IDLE | 1.15 | 4.58 | 3.59 | -0.05 | 76742.27 | 28.06 | no_map |
| FLUIDUSDT | IDLE | 2.4 | 4.19 | 4.02 | -0.07 | 4792.01 | 22.28 | tvl≈2,620,934,893 |
| RWAINCUSDT | IDLE | 1.12 | 3.82 | 0.69 | 0.0 | 18818.36 | 64.27 | no_map |
| TELUSDT | IDLE | 1.63 | 4.07 | 3.37 | -0.06 | 126021.88 | 39.36 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
