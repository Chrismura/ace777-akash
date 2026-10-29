# Hulk DIGEST — 2026-10-29T12:11:22Z

- **Piste :** VEILLE (séparée du paper Hulk)
- Source trading : **MEXC spot**
- Amont : DefiLlama best-effort (= API DeFi, **pas** Llama LLM)
- Clés MEXC (`~/.mexc.env`) : non (public OK)
- Superviseur : Qwen (lire digest — ne trade pas — piste séparée)
- Trade CORE (réf.) : BTCUSDT, ETHUSDT, XRPUSDT, HBARUSDT, RIZEUSDT, ZBCNUSDT, WUSDT, REDUSDT, CCUSDT, PYTHUSDT, BIOUSDT, KITEUSDT, CHIPUSDT, RWAINCUSDT, EDELUSDT, QNTUSDT, FLUIDUSDT, RWAUSDT, MNSRYUSDT
- Watch only : —

## Priorité (haut → bas)

| pair | hint | tension | move6% | dd6% | chg24% | vol USDT | spread bps | DefiLlama |
|------|------|---------|--------|------|--------|----------|------------|-----------|
| ETHUSDT | IDLE | 0.56 | 1.08 | 0.33 | -0.01 | 236069220.89 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.41 | 0.74 | 0.55 | -0.02 | 23466783.31 | 1.55 | n/a |
| BTCUSDT | IDLE | 0.35 | 0.65 | 0.29 | -0.01 | 343911331.22 | 0.43 | no_map |
| CCUSDT | IDLE | 2.19 | 4.34 | 0.25 | -0.01 | 421315.17 | 8.02 | no_map |
| WUSDT | IDLE | 1.56 | 2.87 | 1.65 | -0.04 | 487457.37 | 17.04 | tvl≈1,488,226,765 |
| PYTHUSDT | IDLE | 1.27 | 2.25 | 1.96 | -0.03 | 451744.1 | 2.87 | tvl≈156,290,508 |
| EDELUSDT | IDLE | 1.53 | 2.73 | 2.15 | -0.05 | 228331.58 | 12.91 | no_map |
| CHIPUSDT | IDLE | 1.29 | 4.1 | 1.17 | -0.06 | 193519.06 | 10.38 | no_map |
| HBARUSDT | IDLE | 0.64 | 1.12 | 1.11 | -0.03 | 561379.77 | 6.82 | empty_tvl |
| BIOUSDT | IDLE | 1.5 | 2.9 | 0.63 | -0.02 | 66869.45 | 8.98 | n/a |
| QNTUSDT | IDLE | 1.08 | 2.02 | 0.87 | -0.04 | 441362.08 | 2.07 | n/a |
| RWAINCUSDT | IDLE | 1.35 | 4.82 | 1.53 | -0.1 | 33750.15 | 7.08 | no_map |
| ZBCNUSDT | IDLE | 0.62 | 1.1 | 1.0 | -0.01 | 250652.59 | 19.61 | n/a |
| REDUSDT | IDLE | 1.16 | 2.26 | 0.44 | -0.02 | 64505.27 | 15.5 | tvl≈3,658,611 |
| KITEUSDT | IDLE | 1.12 | 2.19 | 0.33 | -0.02 | 60114.86 | 13.22 | no_map |
| LAUSDT | IDLE | 2.07 | 3.7 | 2.9 | -0.04 | 57591.4 | 26.48 | no_map |
| RIZEUSDT | IDLE | 0.49 | 0.89 | 0.65 | -0.03 | 39636.81 | 49.3 | no_map |
| IOTAUSDT | IDLE | 1.07 | 2.04 | 1.04 | -0.05 | 95315.75 | 27.39 | no_map |
| FLUIDUSDT | IDLE | 1.39 | 2.79 | 0.99 | -0.06 | 6322.22 | 21.32 | tvl≈2,229,089,584 |
| WAXLUSDT | IDLE | 1.35 | 3.33 | 0.73 | -0.05 | 54065.15 | 45.4 | no_map |
| RWAUSDT | IDLE | 1.14 | 2.01 | 1.74 | -0.01 | 56036.12 | 40.21 | no_map |
| MNSRYUSDT | IDLE | 0.37 | 0.72 | 0.19 | -0.01 | 36461.21 | 4.41 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
