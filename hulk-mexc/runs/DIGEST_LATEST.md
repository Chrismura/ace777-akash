# Hulk DIGEST — 2026-08-31T11:09:18Z

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
| XRPUSDT | IDLE | 0.9 | 1.76 | 0.25 | -0.01 | 39573465.63 | 2.9 | n/a |
| BTCUSDT | IDLE | 0.62 | 1.2 | 0.22 | 0.01 | 524054931.54 | 0.26 | no_map |
| ETHUSDT | IDLE | 0.54 | 1.06 | 0.13 | -0.0 | 441083603.38 | 0.04 | no_map |
| CHIPUSDT | IDLE | 2.21 | 7.0 | 2.46 | 0.03 | 599906.23 | 4.89 | no_map |
| PYTHUSDT | IDLE | 0.94 | 2.26 | 1.1 | -0.0 | 520417.37 | 2.11 | tvl≈106,330,077 |
| CCUSDT | IDLE | 1.3 | 2.46 | 0.88 | 0.01 | 242830.38 | 7.51 | no_map |
| REDUSDT | IDLE | 1.91 | 3.44 | 2.58 | -0.0 | 70094.77 | 11.93 | tvl≈2,057,865 |
| WUSDT | IDLE | 1.12 | 2.11 | 1.2 | -0.01 | 235030.58 | 13.96 | tvl≈1,509,534,477 |
| ZBCNUSDT | IDLE | 0.82 | 2.68 | 0.55 | -0.08 | 235474.37 | 12.81 | n/a |
| KITEUSDT | IDLE | 0.98 | 2.51 | 1.96 | -0.06 | 97088.21 | 9.1 | no_map |
| BIOUSDT | IDLE | 0.85 | 1.51 | 1.34 | -0.03 | 85885.77 | 3.78 | n/a |
| EDELUSDT | IDLE | 0.46 | 3.03 | 0.57 | 0.03 | 120530.84 | 16.45 | no_map |
| RIZEUSDT | IDLE | 1.22 | 2.42 | 0.14 | -0.0 | 33456.41 | 61.55 | no_map |
| TELUSDT | IDLE | 1.99 | 3.87 | 0.69 | 0.03 | 94981.7 | 40.4 | no_map |
| RWAUSDT | IDLE | 1.71 | 3.41 | 0.0 | 0.04 | 54296.26 | 23.59 | no_map |
| QNTUSDT | IDLE | 1.58 | 2.93 | 1.49 | -0.0 | 38469.53 | 8.11 | n/a |
| RWAINCUSDT | IDLE | 1.35 | 2.35 | 2.29 | -0.01 | 2998.57 | 125.14 | no_map |
| HBARUSDT | IDLE | 0.38 | 0.73 | 0.19 | -0.01 | 241532.13 | 1.34 | empty_tvl |
| FLUIDUSDT | IDLE | 1.09 | 2.15 | 0.16 | 0.01 | 1733.99 | 20.83 | tvl≈2,614,953,113 |
| MNSRYUSDT | IDLE | 0.32 | 0.59 | 0.3 | -0.01 | 28870.14 | 31.22 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
