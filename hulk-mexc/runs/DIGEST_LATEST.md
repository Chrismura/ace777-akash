# Hulk DIGEST — 2026-10-15T15:13:34Z

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
| PYTHUSDT | IDLE | 3.43 | 16.32 | 2.44 | 0.12 | 3243486.33 | 18.57 | tvl≈191,441,210 |
| WUSDT | IDLE | 1.99 | 6.21 | 0.32 | -0.02 | 2647289.13 | 18.21 | tvl≈1,562,166,478 |
| ETHUSDT | IDLE | 2.24 | 4.45 | 0.22 | -0.0 | 329959369.26 | 0.83 | no_map |
| XRPUSDT | IDLE | 2.05 | 4.09 | 0.1 | 0.01 | 54923760.66 | 0.75 | n/a |
| BTCUSDT | IDLE | 1.57 | 3.14 | 0.04 | 0.01 | 494790297.1 | 0.0 | no_map |
| QNTUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.51 | 9.22 | 0.05 | 0.03 | 1114657.96 | 8.53 | n/a |
| REDUSDT | IDLE | 3.08 | 7.63 | 0.11 | 0.03 | 72811.92 | 7.05 | tvl≈3,780,684 |
| CCUSDT | IDLE | 1.22 | 4.07 | 0.43 | -0.07 | 432374.16 | 10.09 | no_map |
| CHIPUSDT | IDLE | 1.72 | 11.93 | 0.53 | -0.13 | 167566.79 | 8.45 | no_map |
| BIOUSDT | IDLE | 2.1 | 5.8 | 0.47 | -0.03 | 88905.62 | 3.91 | n/a |
| RWAINCUSDT | IDLE | 2.28 | 7.49 | 1.05 | 0.1 | 26808.23 | 9.66 | no_map |
| ZBCNUSDT | IDLE | 1.77 | 3.53 | 0.01 | -0.0 | 199629.06 | 28.36 | n/a |
| KITEUSDT | IDLE | 1.9 | 6.14 | 0.0 | -0.04 | 58615.28 | 11.23 | no_map |
| HBARUSDT | IDLE | 1.83 | 3.65 | 0.01 | -0.01 | 375327.0 | 7.21 | empty_tvl |
| EDELUSDT | IDLE | 1.29 | 4.56 | 0.74 | -0.08 | 239731.26 | 67.53 | no_map |
| RIZEUSDT | IDLE | 1.44 | 5.51 | 2.95 | 0.01 | 77288.91 | 48.52 | no_map |
| TELUSDT | IDLE | 2.34 | 5.77 | 0.0 | 0.01 | 96812.96 | 34.11 | no_map |
| MNSRYUSDT | IDLE | 1.46 | 2.77 | 1.03 | -0.01 | 31221.69 | 43.66 | no_map |
| FLUIDUSDT | IDLE | 1.12 | 4.38 | 0.18 | -0.0 | 17219.27 | 21.49 | tvl≈2,235,312,081 |
| RWAUSDT | IDLE | 0.91 | 1.78 | 0.32 | -0.0 | 55254.92 | 7.97 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
