# Hulk DIGEST — 2026-10-29T13:26:02Z

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
| ETHUSDT | IDLE | 0.46 | 0.9 | 0.19 | -0.01 | 230851116.35 | 0.43 | no_map |
| XRPUSDT | IDLE | 0.45 | 0.85 | 0.32 | -0.02 | 23485636.59 | 1.55 | n/a |
| BTCUSDT | IDLE | 0.33 | 0.62 | 0.22 | -0.01 | 339479627.77 | 0.0 | no_map |
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 4.1 | 10.02 | 1.8 | 0.05 | 624752.05 | 9.36 | tvl≈156,879,031 |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.99 | 8.59 | 0.52 | 0.08 | 399063.09 | 9.65 | no_map |
| WUSDT | IDLE | 1.71 | 3.31 | 0.79 | -0.01 | 450946.63 | 15.21 | tvl≈1,492,323,596 |
| CHIPUSDT | IDLE | 2.24 | 5.64 | 0.79 | -0.06 | 172381.04 | 8.16 | no_map |
| EDELUSDT | IDLE | 1.42 | 2.6 | 1.55 | -0.04 | 242602.79 | 16.1 | no_map |
| REDUSDT | IDLE | 1.86 | 3.69 | 0.22 | -0.0 | 65080.02 | 15.89 | tvl≈3,673,588 |
| BIOUSDT | IDLE | 1.71 | 3.34 | 0.58 | -0.0 | 65930.86 | 4.46 | n/a |
| HBARUSDT | IDLE | 0.83 | 1.65 | 0.12 | -0.02 | 507410.13 | 4.03 | empty_tvl |
| QNTUSDT | IDLE | 0.9 | 1.75 | 0.31 | -0.02 | 413567.55 | 0.51 | n/a |
| ZBCNUSDT | IDLE | 0.58 | 1.16 | 0.06 | 0.0 | 249865.28 | 31.55 | n/a |
| KITEUSDT | IDLE | 1.17 | 2.3 | 0.31 | -0.01 | 60283.87 | 14.05 | no_map |
| RWAINCUSDT | IDLE | 1.02 | 3.31 | 1.6 | -0.1 | 33803.69 | 7.07 | no_map |
| FLUIDUSDT | IDLE | 1.62 | 3.15 | 3.05 | -0.06 | 7569.14 | 21.37 | tvl≈2,231,292,012 |
| RIZEUSDT | IDLE | 0.5 | 0.89 | 0.68 | -0.03 | 39655.94 | 51.64 | no_map |
| IOTAUSDT | IDLE | 1.01 | 2.01 | 0.42 | -0.03 | 92428.77 | 19.78 | no_map |
| RWAUSDT | IDLE | 1.05 | 1.86 | 1.59 | -0.02 | 55930.67 | 24.26 | no_map |
| WAXLUSDT | IDLE | 1.26 | 3.15 | 0.26 | -0.03 | 53425.75 | 49.19 | no_map |
| LAUSDT | IDLE | 0.97 | 1.85 | 0.66 | -0.02 | 58466.47 | 19.35 | no_map |
| MNSRYUSDT | IDLE | 0.51 | 1.01 | 0.04 | -0.0 | 36241.84 | 8.79 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
