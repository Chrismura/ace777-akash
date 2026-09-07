# Hulk DIGEST — 2026-09-07T22:37:46Z

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
| XRPUSDT | IDLE | 0.63 | 1.1 | 1.07 | -0.02 | 36263302.18 | 2.16 | n/a |
| ETHUSDT | IDLE | 0.4 | 0.69 | 0.67 | -0.01 | 336504437.93 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.29 | 0.5 | 0.48 | -0.01 | 448047398.99 | 0.0 | no_map |
| CCUSDT | IDLE | 1.59 | 2.99 | 1.93 | -0.04 | 466071.6 | 9.55 | no_map |
| PYTHUSDT | IDLE | 1.03 | 1.8 | 1.75 | -0.03 | 526059.71 | 1.85 | tvl≈123,277,106 |
| ZBCNUSDT | IDLE | 2.25 | 6.38 | 0.91 | -0.04 | 216448.1 | 14.48 | n/a |
| EDELUSDT | IDLE | 2.36 | 8.84 | 2.77 | -0.03 | 101597.41 | 29.51 | no_map |
| CHIPUSDT | IDLE | 1.67 | 6.69 | 2.1 | -0.07 | 222939.73 | 12.99 | no_map |
| RWAINCUSDT | IDLE | 2.66 | 8.72 | 4.67 | -0.01 | 4779.68 | 91.7 | no_map |
| HBARUSDT | IDLE | 0.95 | 1.67 | 1.47 | 0.01 | 581176.39 | 2.44 | empty_tvl |
| WUSDT | IDLE | 0.87 | 1.52 | 1.5 | -0.02 | 243744.98 | 9.81 | tvl≈1,581,915,630 |
| RIZEUSDT | IDLE | 1.86 | 5.58 | 2.39 | -0.02 | 55523.09 | 71.43 | no_map |
| REDUSDT | IDLE | 1.09 | 1.9 | 1.81 | 0.02 | 58266.15 | 7.64 | tvl≈2,448,916 |
| KITEUSDT | IDLE | 0.94 | 1.66 | 1.5 | -0.06 | 61194.25 | 9.29 | no_map |
| BIOUSDT | IDLE | 0.78 | 1.37 | 1.31 | -0.02 | 65958.96 | 3.69 | n/a |
| QNTUSDT | IDLE | 1.16 | 2.2 | 0.76 | -0.01 | 46234.3 | 7.53 | n/a |
| TELUSDT | IDLE | 0.83 | 1.47 | 1.22 | -0.05 | 95658.6 | 5.87 | no_map |
| FLUIDUSDT | IDLE | 0.7 | 1.41 | 0.0 | 0.0 | 1666.63 | 20.39 | tvl≈2,645,778,443 |
| RWAUSDT | IDLE | 0.34 | 0.66 | 0.15 | -0.01 | 54727.81 | 7.26 | no_map |
| MNSRYUSDT | IDLE | 0.42 | 0.74 | 0.67 | -0.02 | 37601.28 | 9.56 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
