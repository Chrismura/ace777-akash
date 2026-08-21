# Hulk DIGEST — 2026-08-21T23:37:56Z

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
| PYTHUSDT | IDLE | 1.76 | 6.39 | 1.31 | 0.11 | 6125335.55 | 4.09 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 1.94 | 8.23 | 0.7 | 0.16 | 140999352.06 | 3.41 | n/a |
| HBARUSDT | IDLE | 2.58 | 6.36 | 0.51 | 0.1 | 906893.53 | 1.24 | empty_tvl |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.85 | 11.25 | 1.67 | 0.13 | 513163.8 | 26.79 | n/a |
| CCUSDT | IDLE | 1.91 | 7.42 | 1.07 | 0.13 | 645435.51 | 6.23 | no_map |
| WUSDT | IDLE | 2.76 | 6.91 | 1.64 | 0.08 | 379560.39 | 19.51 | tvl≈1,628,401,619 |
| CHIPUSDT | IDLE | 1.18 | 3.56 | 1.46 | 0.03 | 548095.38 | 3.08 | no_map |
| BIOUSDT | IDLE | 2.28 | 5.04 | 0.95 | 0.02 | 186352.68 | 3.11 | n/a |
| EDELUSDT | IDLE | 2.52 | 5.5 | 0.43 | -0.03 | 82417.09 | 21.81 | no_map |
| RIZEUSDT | IDLE | 2.19 | 9.82 | 4.23 | 0.13 | 58907.11 | 45.81 | no_map |
| TELUSDT | IDLE | 2.83 | 6.89 | 0.41 | 0.07 | 188310.38 | 30.77 | no_map |
| REDUSDT | IDLE | 0.87 | 7.3 | 4.68 | 0.19 | 157760.54 | 18.57 | tvl≈2,226,572 |
| RWAINCUSDT | IDLE | 2.13 | 4.07 | 1.32 | 0.02 | 10340.11 | 32.1 | no_map |
| QNTUSDT | IDLE | 2.59 | 5.68 | 0.06 | 0.08 | 139540.81 | 1.49 | n/a |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 67.45 | no_map |
| KITEUSDT | IDLE | 1.1 | 3.12 | 0.94 | 0.09 | 61387.49 | 9.25 | no_map |
| RWAUSDT | IDLE | 1.07 | 2.08 | 0.41 | 0.03 | 54536.14 | 8.19 | no_map |
| FLUIDUSDT | IDLE | 1.06 | 2.87 | 0.0 | 0.11 | 4903.8 | 20.5 | tvl≈2,594,160,978 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
