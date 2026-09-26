# Hulk DIGEST — 2026-09-26T06:52:43Z

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
| XRPUSDT | IDLE | 1.29 | 2.29 | 1.97 | 0.01 | 109804446.07 | 1.94 | n/a |
| ETHUSDT | IDLE | 0.26 | 0.46 | 0.34 | 0.0 | 294835178.54 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.18 | 0.32 | 0.23 | -0.0 | 640354752.07 | 0.0 | no_map |
| PYTHUSDT | IDLE | 1.31 | 3.33 | 1.87 | 0.08 | 1189282.06 | 5.43 | tvl≈165,199,262 |
| CCUSDT | IDLE | 1.27 | 5.69 | 0.03 | 0.18 | 973338.55 | 5.1 | no_map |
| HBARUSDT | IDLE | 1.2 | 2.15 | 1.61 | 0.02 | 863449.68 | 1.07 | empty_tvl |
| QNTUSDT | IDLE | 2.15 | 6.76 | 2.76 | 0.01 | 513504.93 | 12.74 | n/a |
| WUSDT | IDLE | 1.01 | 2.01 | 0.39 | 0.07 | 475691.8 | 5.65 | tvl≈1,838,875,078 |
| ZBCNUSDT | IDLE | 1.44 | 3.27 | 2.27 | 0.03 | 230592.25 | 5.69 | n/a |
| REDUSDT | IDLE | 1.83 | 3.35 | 2.13 | 0.06 | 59525.15 | 14.57 | tvl≈3,162,950 |
| KITEUSDT | IDLE | 1.58 | 4.12 | 2.99 | 0.08 | 76286.82 | 8.11 | no_map |
| CHIPUSDT | IDLE | 1.19 | 2.91 | 2.14 | 0.06 | 147820.44 | 16.5 | no_map |
| EDELUSDT | IDLE | 0.98 | 1.81 | 0.94 | 0.0 | 173404.25 | 44.02 | no_map |
| RWAINCUSDT | IDLE | 1.84 | 4.42 | 0.54 | -0.04 | 11007.79 | 73.37 | no_map |
| BIOUSDT | IDLE | 0.65 | 1.76 | 1.0 | 0.06 | 110622.76 | 3.07 | n/a |
| RIZEUSDT | IDLE | 0.18 | 2.42 | 0.41 | -0.16 | 75314.69 | 51.53 | no_map |
| TELUSDT | IDLE | 0.87 | 1.54 | 1.39 | 0.01 | 118756.97 | 55.33 | no_map |
| FLUIDUSDT | IDLE | 0.96 | 1.83 | 0.62 | 0.01 | 3441.0 | 21.65 | tvl≈2,581,647,948 |
| MNSRYUSDT | IDLE | 0.45 | 0.89 | 0.13 | 0.01 | 40889.09 | 8.92 | no_map |
| RWAUSDT | IDLE | 0.58 | 1.04 | 0.74 | -0.02 | 53416.78 | 36.97 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
