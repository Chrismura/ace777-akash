# Hulk DIGEST — 2026-09-25T23:47:46Z

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
| XRPUSDT | IDLE | 1.02 | 1.94 | 0.61 | 0.02 | 115633708.75 | 1.27 | n/a |
| ETHUSDT | IDLE | 0.42 | 0.81 | 0.25 | 0.0 | 321092232.36 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.33 | 0.65 | 0.13 | -0.0 | 689534300.15 | 0.0 | no_map |
| PYTHUSDT | IDLE | 2.09 | 5.67 | 1.53 | 0.09 | 1245318.23 | 2.7 | tvl≈168,536,691 |
| CCUSDT | IDLE | 1.22 | 4.89 | 1.89 | 0.15 | 861886.75 | 8.45 | no_map |
| HBARUSDT | IDLE | 1.71 | 3.33 | 0.57 | 0.03 | 939669.37 | 2.09 | empty_tvl |
| WUSDT | IDLE | 1.99 | 3.88 | 0.7 | 0.05 | 434788.91 | 10.52 | tvl≈1,837,140,994 |
| EDELUSDT | IDLE | 2.64 | 4.72 | 3.76 | 0.0 | 183022.54 | 6.78 | no_map |
| ZBCNUSDT | IDLE | 1.99 | 4.39 | 3.97 | 0.05 | 245179.86 | 26.09 | n/a |
| RIZEUSDT | IDLE | 1.24 | 18.48 | 12.49 | 0.04 | 109107.8 | 64.86 | no_map |
| CHIPUSDT | IDLE | 2.08 | 5.74 | 0.22 | 0.06 | 162053.04 | 21.74 | no_map |
| QNTUSDT | IDLE | 0.74 | 3.19 | 0.97 | 0.1 | 570138.84 | 4.06 | n/a |
| BIOUSDT | IDLE | 1.12 | 3.35 | 0.87 | 0.08 | 115197.52 | 9.08 | n/a |
| REDUSDT | IDLE | 0.78 | 1.87 | 1.08 | 0.08 | 136948.06 | 13.81 | tvl≈3,156,241 |
| KITEUSDT | IDLE | 0.94 | 1.85 | 0.2 | 0.02 | 80041.86 | 11.24 | no_map |
| RWAINCUSDT | IDLE | 0.68 | 2.15 | 0.75 | -0.08 | 13525.58 | 15.09 | no_map |
| TELUSDT | IDLE | 1.2 | 2.15 | 1.68 | -0.01 | 115608.77 | 55.03 | no_map |
| MNSRYUSDT | IDLE | 0.69 | 1.25 | 0.82 | 0.02 | 41246.91 | 5.09 | no_map |
| RWAUSDT | IDLE | 0.59 | 1.04 | 0.95 | -0.01 | 54360.75 | 44.38 | no_map |
| FLUIDUSDT | IDLE | 0.38 | 0.68 | 0.52 | 0.03 | 3316.59 | 21.48 | tvl≈2,577,601,829 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
