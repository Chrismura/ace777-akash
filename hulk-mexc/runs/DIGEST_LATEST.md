# Hulk DIGEST — 2026-08-22T02:53:44Z

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
| PYTHUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.62 | 11.02 | 0.66 | 0.16 | 7314032.07 | 1.9 | tvl≈112,886,663 |
| XRPUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.49 | 12.69 | 0.16 | 0.19 | 158212609.48 | 3.88 | n/a |
| HBARUSDT | IDLE | 2.53 | 6.43 | 0.0 | 0.1 | 989365.14 | 1.22 | empty_tvl |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.07 | 9.46 | 0.09 | 0.18 | 660484.99 | 6.75 | no_map |
| ZBCNUSDT | IDLE | 2.49 | 9.63 | 2.83 | 0.1 | 541565.59 | 48.92 | n/a |
| CHIPUSDT | IDLE | 2.53 | 5.8 | 0.24 | -0.01 | 451767.12 | 5.97 | no_map |
| BIOUSDT | IDLE | 3.2 | 8.18 | 2.08 | 0.09 | 194238.43 | 3.0 | n/a |
| WUSDT | IDLE | 2.04 | 6.23 | 0.02 | 0.11 | 415126.49 | 12.88 | tvl≈1,646,654,250 |
| EDELUSDT | IDLE | 2.44 | 5.02 | 2.5 | -0.03 | 79854.01 | 22.27 | no_map |
| RIZEUSDT | IDLE | 1.99 | 8.52 | 4.34 | 0.1 | 61374.48 | 44.22 | no_map |
| REDUSDT | IDLE | 0.98 | 8.27 | 4.94 | 0.19 | 157794.18 | 17.59 | tvl≈2,314,909 |
| RWAINCUSDT | IDLE | 1.83 | 3.27 | 2.58 | 0.0 | 9385.21 | 10.86 | no_map |
| QNTUSDT | IDLE | 2.34 | 5.48 | 0.24 | 0.09 | 172619.22 | 5.95 | n/a |
| KITEUSDT | IDLE | 1.32 | 4.09 | 0.13 | 0.12 | 62474.81 | 8.96 | no_map |
| TELUSDT | IDLE | 2.15 | 5.11 | 1.13 | 0.06 | 174007.66 | 30.93 | no_map |
| QAITUSDT | IDLE | 1.88 | 3.57 | 1.22 | 0.0 | 3930.15 | 63.67 | no_map |
| RWAUSDT | IDLE | 1.56 | 3.08 | 0.32 | 0.05 | 55901.13 | 16.22 | no_map |
| FLUIDUSDT | IDLE | 1.44 | 3.69 | 2.03 | 0.07 | 4710.05 | 21.03 | tvl≈2,599,456,799 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
