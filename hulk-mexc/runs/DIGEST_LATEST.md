# Hulk DIGEST — 2026-08-21T23:26:06Z

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
| PYTHUSDT | IDLE | 1.72 | 6.39 | 0.38 | 0.12 | 6065633.36 | 2.02 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 1.93 | 8.23 | 0.43 | 0.16 | 140295152.39 | 2.72 | n/a |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.83 | 11.25 | 1.15 | 0.14 | 512873.76 | 22.84 | n/a |
| HBARUSDT | IDLE | 2.57 | 6.29 | 0.37 | 0.1 | 900449.54 | 1.24 | empty_tvl |
| CCUSDT | IDLE | 1.91 | 7.42 | 1.01 | 0.13 | 645474.38 | 5.34 | no_map |
| WUSDT | IDLE | 2.75 | 6.91 | 1.38 | 0.08 | 377991.61 | 9.22 | tvl≈1,628,401,619 |
| CHIPUSDT | IDLE | 1.16 | 3.56 | 1.0 | 0.05 | 547980.08 | 3.07 | no_map |
| BIOUSDT | IDLE | 2.27 | 5.04 | 0.74 | 0.02 | 187682.93 | 3.1 | n/a |
| EDELUSDT | IDLE | 2.52 | 5.5 | 0.43 | -0.03 | 82503.56 | 21.83 | no_map |
| RIZEUSDT | IDLE | 2.16 | 9.82 | 3.3 | 0.13 | 59029.37 | 45.4 | no_map |
| TELUSDT | IDLE | 2.69 | 6.62 | 0.05 | 0.07 | 184982.37 | 20.53 | no_map |
| RWAINCUSDT | IDLE | 2.2 | 4.07 | 2.22 | 0.02 | 10178.81 | 32.38 | no_map |
| REDUSDT | IDLE | 0.87 | 7.3 | 4.73 | 0.19 | 157525.54 | 11.31 | tvl≈2,226,572 |
| QNTUSDT | IDLE | 2.56 | 5.52 | 0.0 | 0.07 | 119328.63 | 1.5 | n/a |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 67.45 | no_map |
| KITEUSDT | IDLE | 1.1 | 3.12 | 1.05 | 0.09 | 61377.94 | 9.25 | no_map |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.33 | 0.04 | 54513.42 | 32.73 | no_map |
| FLUIDUSDT | IDLE | 1.06 | 2.87 | 0.0 | 0.11 | 4903.8 | 40.82 | tvl≈2,594,160,978 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
