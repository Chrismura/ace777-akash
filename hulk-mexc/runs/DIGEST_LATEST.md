# Hulk DIGEST — 2026-08-21T23:33:57Z

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
| PYTHUSDT | IDLE | 1.73 | 6.39 | 0.75 | 0.11 | 6104145.08 | 2.03 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 1.94 | 8.23 | 0.53 | 0.15 | 140764448.65 | 3.41 | n/a |
| HBARUSDT | IDLE | 2.58 | 6.29 | 0.48 | 0.09 | 904603.8 | 1.24 | empty_tvl |
| CCUSDT | IDLE | 1.91 | 7.42 | 1.14 | 0.13 | 645415.79 | 8.01 | no_map |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.8 | 11.25 | 0.39 | 0.14 | 513238.19 | 70.32 | n/a |
| WUSDT | IDLE | 2.73 | 6.91 | 1.06 | 0.08 | 379636.19 | 14.31 | tvl≈1,628,401,619 |
| CHIPUSDT | IDLE | 1.18 | 3.56 | 1.46 | 0.03 | 549131.61 | 3.09 | no_map |
| BIOUSDT | IDLE | 2.25 | 5.04 | 0.49 | 0.02 | 186466.16 | 6.18 | n/a |
| EDELUSDT | IDLE | 2.53 | 5.5 | 0.65 | -0.03 | 82459.4 | 21.83 | no_map |
| RIZEUSDT | IDLE | 2.2 | 9.82 | 4.39 | 0.13 | 58908.2 | 88.03 | no_map |
| RWAINCUSDT | IDLE | 2.2 | 4.07 | 2.22 | 0.01 | 10135.01 | 21.65 | no_map |
| TELUSDT | IDLE | 2.7 | 6.62 | 0.1 | 0.07 | 186967.37 | 20.53 | no_map |
| REDUSDT | IDLE | 0.87 | 7.3 | 4.66 | 0.19 | 157762.01 | 19.36 | tvl≈2,226,572 |
| QNTUSDT | IDLE | 2.58 | 5.68 | 0.01 | 0.07 | 124613.03 | 1.49 | n/a |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 67.45 | no_map |
| KITEUSDT | IDLE | 1.1 | 3.12 | 0.94 | 0.09 | 61400.67 | 11.1 | no_map |
| RWAUSDT | IDLE | 1.05 | 2.08 | 0.16 | 0.04 | 54601.1 | 24.56 | no_map |
| FLUIDUSDT | IDLE | 1.06 | 2.87 | 0.0 | 0.11 | 4903.8 | 21.21 | tvl≈2,594,160,978 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
