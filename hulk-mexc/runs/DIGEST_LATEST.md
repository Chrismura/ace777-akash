# Hulk DIGEST — 2026-08-17T00:09:35Z

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
| XRPUSDT | IDLE | 0.68 | 1.2 | 1.05 | -0.01 | 6710540.11 | 2.02 | n/a |
| CHIPUSDT | IDLE | 1.59 | 7.25 | 5.21 | 0.02 | 294756.03 | 3.56 | no_map |
| RIZEUSDT | IDLE | 3.24 | 6.82 | 2.26 | 0.02 | 37331.21 | 59.77 | no_map |
| PYTHUSDT | IDLE | 1.89 | 3.35 | 2.81 | -0.03 | 148742.99 | 2.61 | tvl≈88,764,315 |
| CCUSDT | IDLE | 0.82 | 1.79 | 0.03 | -0.03 | 336947.87 | 7.27 | no_map |
| WUSDT | IDLE | 1.08 | 2.14 | 0.14 | 0.01 | 180877.85 | 11.67 | tvl≈1,348,995,891 |
| EDELUSDT | IDLE | 1.61 | 3.05 | 1.16 | 0.01 | 56240.54 | 26.08 | no_map |
| BIOUSDT | IDLE | 1.32 | 2.38 | 1.67 | -0.02 | 64363.12 | 8.29 | n/a |
| ZBCNUSDT | IDLE | 0.61 | 1.13 | 0.58 | -0.01 | 192047.14 | 16.56 | n/a |
| REDUSDT | IDLE | 0.67 | 1.25 | 0.57 | -0.04 | 63042.21 | 12.66 | tvl≈1,573,315 |
| KITEUSDT | IDLE | 0.67 | 1.2 | 0.93 | -0.03 | 55117.28 | 17.12 | no_map |
| TELUSDT | IDLE | 1.49 | 2.94 | 0.27 | 0.0 | 102133.6 | 20.42 | no_map |
| QAITUSDT | IDLE | 0.85 | 2.41 | 0.0 | -0.01 | 2289.9 | 61.3 | no_map |
| RWAINCUSDT | IDLE | 0.68 | 1.31 | 0.34 | 0.04 | 5943.17 | 96.45 | no_map |
| HBARUSDT | IDLE | 0.68 | 1.21 | 1.06 | -0.01 | 99510.58 | 1.55 | empty_tvl |
| QNTUSDT | IDLE | 0.86 | 1.61 | 0.72 | -0.02 | 33659.64 | 7.03 | n/a |
| RWAUSDT | IDLE | 0.4 | 0.7 | 0.61 | -0.0 | 50421.19 | 8.75 | no_map |
| FLUIDUSDT | IDLE | 0.58 | 1.16 | 0.03 | 0.02 | 240.62 | 22.65 | tvl≈2,305,164,738 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
