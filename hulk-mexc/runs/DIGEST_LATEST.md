# Hulk DIGEST — 2026-08-20T07:13:19Z

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
| XRPUSDT | IDLE | 0.75 | 2.43 | 0.41 | 0.11 | 47142070.59 | 1.8 | n/a |
| REDUSDT | IDLE | 2.57 | 24.94 | 3.79 | 0.32 | 164414.2 | 11.11 | tvl≈1,819,284 |
| CHIPUSDT | IDLE | 1.76 | 7.39 | 4.09 | 0.12 | 226781.6 | 13.88 | no_map |
| CCUSDT | IDLE | 0.94 | 3.18 | 0.66 | 0.12 | 388617.75 | 8.91 | no_map |
| EDELUSDT | IDLE | 1.44 | 11.01 | 8.1 | 0.23 | 101660.0 | 32.99 | no_map |
| BIOUSDT | IDLE | 1.25 | 6.6 | 0.83 | 0.2 | 179595.52 | 6.68 | n/a |
| ZBCNUSDT | IDLE | 0.96 | 3.83 | 1.02 | 0.14 | 233051.92 | 12.8 | n/a |
| WUSDT | IDLE | 0.79 | 1.63 | 0.88 | 0.06 | 283233.07 | 12.83 | tvl≈1,455,042,970 |
| RIZEUSDT | IDLE | 2.07 | 13.97 | 7.09 | 0.15 | 62702.45 | 155.68 | no_map |
| PYTHUSDT | IDLE | 0.48 | 1.47 | 0.3 | 0.1 | 305796.62 | 2.34 | tvl≈95,798,707 |
| HBARUSDT | IDLE | 1.23 | 2.35 | 0.68 | 0.06 | 368866.16 | 1.4 | empty_tvl |
| KITEUSDT | IDLE | 0.86 | 1.51 | 1.35 | 0.06 | 59605.36 | 16.76 | no_map |
| RWAINCUSDT | IDLE | 0.71 | 1.88 | 1.85 | 0.03 | 17232.3 | 22.62 | no_map |
| QAITUSDT | IDLE | 1.29 | 3.52 | 2.02 | 0.03 | 11161.39 | 185.22 | no_map |
| TELUSDT | IDLE | 0.51 | 2.31 | 1.28 | 0.11 | 192420.21 | 55.71 | no_map |
| QNTUSDT | IDLE | 0.66 | 1.31 | 0.05 | 0.04 | 37042.86 | 5.06 | n/a |
| FLUIDUSDT | IDLE | 0.74 | 2.01 | 0.12 | 0.08 | 3551.44 | 21.38 | tvl≈2,485,178,808 |
| RWAUSDT | IDLE | 0.43 | 0.78 | 0.6 | 0.02 | 53628.28 | 8.65 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
