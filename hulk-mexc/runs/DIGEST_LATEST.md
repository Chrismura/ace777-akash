# Hulk DIGEST — 2026-08-16T22:07:26Z

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
| XRPUSDT | IDLE | 0.69 | 1.26 | 0.75 | -0.01 | 6391928.0 | 1.0 | n/a |
| RIZEUSDT | IDLE | 3.68 | 7.8 | 2.28 | 0.02 | 38057.14 | 59.77 | no_map |
| PYTHUSDT | IDLE | 2.12 | 3.77 | 3.15 | -0.03 | 146403.25 | 5.21 | tvl≈88,764,315 |
| WUSDT | IDLE | 1.75 | 3.24 | 1.7 | 0.01 | 181978.14 | 11.73 | tvl≈1,360,457,371 |
| CHIPUSDT | IDLE | 1.05 | 4.9 | 2.47 | 0.05 | 295555.82 | 17.34 | no_map |
| ZBCNUSDT | IDLE | 1.57 | 2.83 | 2.03 | -0.02 | 193526.03 | 22.98 | n/a |
| BIOUSDT | IDLE | 1.81 | 3.21 | 2.79 | -0.03 | 67300.54 | 8.32 | n/a |
| CCUSDT | IDLE | 0.62 | 1.17 | 1.09 | -0.04 | 332405.07 | 8.43 | no_map |
| EDELUSDT | IDLE | 1.33 | 2.67 | 0.0 | 0.04 | 60305.48 | 26.04 | no_map |
| KITEUSDT | IDLE | 0.81 | 1.42 | 1.38 | -0.03 | 56409.15 | 17.12 | no_map |
| REDUSDT | IDLE | 0.66 | 1.37 | 0.7 | -0.15 | 68517.68 | 12.66 | tvl≈1,586,703 |
| QAITUSDT | IDLE | 1.25 | 3.83 | 0.0 | -0.01 | 2289.9 | 61.3 | no_map |
| RWAINCUSDT | IDLE | 1.21 | 3.01 | 0.0 | 0.09 | 9973.17 | 73.38 | no_map |
| TELUSDT | IDLE | 1.18 | 2.09 | 1.85 | -0.03 | 94896.8 | 27.84 | no_map |
| HBARUSDT | IDLE | 0.63 | 1.24 | 0.18 | -0.01 | 104412.39 | 1.53 | empty_tvl |
| QNTUSDT | IDLE | 0.93 | 1.63 | 1.48 | -0.02 | 33668.12 | 7.08 | n/a |
| RWAUSDT | IDLE | 0.33 | 0.61 | 0.35 | -0.0 | 51075.32 | 17.45 | no_map |
| FLUIDUSDT | IDLE | 0.32 | 0.62 | 0.11 | 0.02 | 219.43 | 21.13 | tvl≈2,307,813,096 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
