# Hulk DIGEST — 2026-08-21T22:12:03Z

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
| PYTHUSDT | IDLE | 1.32 | 5.06 | 0.04 | 0.11 | 5707954.23 | 2.04 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 1.54 | 5.44 | 0.9 | 0.13 | 131517194.65 | 2.11 | n/a |
| HBARUSDT | IDLE | 2.2 | 4.71 | 0.54 | 0.08 | 846671.66 | 1.26 | empty_tvl |
| CCUSDT | IDLE | 1.61 | 5.58 | 0.0 | 0.13 | 643874.98 | 8.95 | no_map |
| CHIPUSDT | IDLE | 1.49 | 4.54 | 1.36 | 0.07 | 534539.42 | 3.05 | no_map |
| WUSDT | IDLE | 2.4 | 5.04 | 0.0 | 0.08 | 368138.05 | 20.58 | tvl≈1,602,784,605 |
| ZBCNUSDT | IDLE | 1.52 | 6.5 | 0.23 | 0.12 | 497290.05 | 23.15 | n/a |
| BIOUSDT | IDLE | 2.27 | 5.04 | 0.8 | 0.02 | 187797.59 | 27.9 | n/a |
| REDUSDT | IDLE | 1.33 | 11.01 | 8.5 | 0.18 | 155142.13 | 10.56 | tvl≈2,226,572 |
| EDELUSDT | IDLE | 1.89 | 4.12 | 0.44 | -0.04 | 82388.04 | 11.04 | no_map |
| TELUSDT | IDLE | 2.51 | 6.45 | 0.56 | 0.06 | 186865.54 | 5.17 | no_map |
| QAITUSDT | IDLE | 2.37 | 4.38 | 2.37 | -0.02 | 3827.91 | 63.67 | no_map |
| RWAINCUSDT | IDLE | 2.17 | 4.07 | 1.8 | 0.02 | 10246.19 | 53.48 | no_map |
| KITEUSDT | IDLE | 1.19 | 3.58 | 0.54 | 0.11 | 61309.37 | 11.91 | no_map |
| RIZEUSDT | IDLE | 0.95 | 4.7 | 1.77 | 0.06 | 56397.49 | 45.14 | no_map |
| QNTUSDT | IDLE | 1.51 | 3.0 | 0.09 | 0.05 | 65301.98 | 15.33 | n/a |
| RWAUSDT | IDLE | 0.89 | 1.75 | 0.16 | 0.04 | 54216.24 | 16.43 | no_map |
| FLUIDUSDT | IDLE | 0.51 | 1.15 | 0.08 | 0.09 | 4171.26 | 13.98 | tvl≈2,562,752,708 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
