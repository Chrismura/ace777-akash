# Hulk DIGEST — 2026-08-21T23:29:41Z

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
| PYTHUSDT | IDLE | 1.73 | 6.39 | 0.69 | 0.11 | 6081270.92 | 2.03 | tvl≈107,253,350 |
| XRPUSDT | IDLE | 1.95 | 8.23 | 0.77 | 0.15 | 140288443.93 | 2.05 | n/a |
| HBARUSDT | IDLE | 2.6 | 6.29 | 0.94 | 0.09 | 902536.22 | 1.25 | empty_tvl |
| ZBCNUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.84 | 11.25 | 1.5 | 0.13 | 512893.14 | 23.87 | n/a |
| CCUSDT | IDLE | 1.91 | 7.42 | 1.1 | 0.13 | 645432.67 | 6.22 | no_map |
| WUSDT | IDLE | 2.76 | 6.91 | 1.56 | 0.08 | 378706.21 | 13.34 | tvl≈1,628,401,619 |
| CHIPUSDT | IDLE | 1.18 | 3.56 | 1.4 | 0.04 | 550249.15 | 3.08 | no_map |
| BIOUSDT | IDLE | 2.27 | 5.04 | 0.74 | 0.02 | 187615.36 | 3.1 | n/a |
| EDELUSDT | IDLE | 2.54 | 5.5 | 0.76 | -0.03 | 82490.47 | 21.83 | no_map |
| RIZEUSDT | IDLE | 2.17 | 9.82 | 3.53 | 0.15 | 58940.82 | 43.92 | no_map |
| TELUSDT | IDLE | 2.7 | 6.62 | 0.15 | 0.07 | 186165.58 | 20.53 | no_map |
| RWAINCUSDT | IDLE | 2.2 | 4.07 | 2.22 | 0.01 | 10152.37 | 26.99 | no_map |
| REDUSDT | IDLE | 0.88 | 7.3 | 5.21 | 0.18 | 157817.48 | 12.17 | tvl≈2,226,572 |
| QNTUSDT | IDLE | 2.57 | 5.63 | 0.03 | 0.07 | 120034.05 | 1.49 | n/a |
| QAITUSDT | IDLE | 2.27 | 4.22 | 2.14 | -0.02 | 3921.68 | 67.45 | no_map |
| KITEUSDT | IDLE | 1.11 | 3.12 | 1.25 | 0.08 | 61408.14 | 11.12 | no_map |
| RWAUSDT | IDLE | 1.06 | 2.08 | 0.24 | 0.04 | 54480.16 | 32.76 | no_map |
| FLUIDUSDT | IDLE | 1.06 | 2.87 | 0.0 | 0.11 | 4903.8 | 21.87 | tvl≈2,594,160,978 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
