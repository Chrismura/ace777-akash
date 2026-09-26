# Hulk DIGEST — 2026-09-26T07:53:24Z

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
| XRPUSDT | IDLE | 1.12 | 2.01 | 1.52 | 0.02 | 109644684.21 | 1.93 | n/a |
| ETHUSDT | IDLE | 0.25 | 0.46 | 0.22 | 0.01 | 285998185.64 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.17 | 0.32 | 0.07 | 0.0 | 615473749.36 | 0.0 | no_map |
| PYTHUSDT | IDLE | 1.47 | 3.33 | 0.36 | 0.09 | 1202022.39 | 5.35 | tvl≈165,199,262 |
| CCUSDT | IDLE | 1.52 | 7.25 | 1.18 | 0.17 | 1025827.07 | 9.45 | no_map |
| WUSDT | IDLE | 1.79 | 3.64 | 0.58 | 0.08 | 476046.71 | 6.37 | tvl≈1,826,810,867 |
| HBARUSDT | IDLE | 1.05 | 1.97 | 0.93 | 0.03 | 856138.41 | 1.06 | empty_tvl |
| QNTUSDT | IDLE | 2.11 | 6.54 | 3.31 | 0.02 | 527411.5 | 34.53 | n/a |
| ZBCNUSDT | IDLE | 1.41 | 3.27 | 1.61 | 0.04 | 243898.02 | 15.07 | n/a |
| EDELUSDT | IDLE | 1.65 | 3.04 | 1.72 | 0.01 | 176028.64 | 13.49 | no_map |
| KITEUSDT | IDLE | 1.67 | 4.02 | 3.63 | 0.07 | 78170.1 | 10.4 | no_map |
| RWAINCUSDT | IDLE | 1.87 | 4.42 | 1.12 | -0.03 | 10456.2 | 4.93 | no_map |
| CHIPUSDT | IDLE | 1.04 | 2.53 | 0.16 | 0.07 | 149368.97 | 14.21 | no_map |
| BIOUSDT | IDLE | 0.73 | 1.76 | 0.88 | 0.06 | 111386.36 | 3.07 | n/a |
| REDUSDT | IDLE | 0.96 | 1.8 | 0.8 | 0.05 | 59294.48 | 8.75 | tvl≈3,123,109 |
| RIZEUSDT | IDLE | 0.26 | 3.43 | 1.11 | -0.17 | 70116.68 | 35.81 | no_map |
| TELUSDT | IDLE | 0.88 | 1.61 | 0.98 | 0.0 | 118230.09 | 30.84 | no_map |
| FLUIDUSDT | IDLE | 0.96 | 1.83 | 0.62 | 0.01 | 3431.02 | 21.57 | tvl≈2,580,811,423 |
| RWAUSDT | IDLE | 0.55 | 1.04 | 0.37 | -0.01 | 53205.28 | 7.38 | no_map |
| MNSRYUSDT | IDLE | 0.45 | 0.89 | 0.11 | 0.01 | 40689.8 | 8.92 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
