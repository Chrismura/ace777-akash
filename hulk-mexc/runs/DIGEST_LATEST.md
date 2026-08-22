# Hulk DIGEST — 2026-08-22T05:09:23Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.32 | 15.45 | 6.47 | 0.13 | 14399748.94 | 38.3 | tvl≈112,886,663 |
| XRPUSDT | IDLE | 2.58 | 19.3 | 4.53 | 0.24 | 184698463.08 | 7.41 | n/a |
| HBARUSDT | IDLE | 2.69 | 10.33 | 3.29 | 0.12 | 1152344.81 | 1.19 | empty_tvl |
| CCUSDT | IDLE | 2.19 | 11.56 | 2.92 | 0.18 | 753496.77 | 10.0 | no_map |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.44 | 6.08 | 5.35 | -0.03 | 453925.73 | 21.81 | no_map |
| WUSDT | IDLE | 2.22 | 8.22 | 3.12 | 0.13 | 456671.77 | 18.69 | tvl≈1,672,612,247 |
| BIOUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.12 | 9.0 | 1.96 | 0.08 | 203810.46 | 14.82 | n/a |
| ZBCNUSDT | IDLE | 1.63 | 4.29 | 3.13 | 0.09 | 538519.87 | 44.57 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 2.78 | 9.16 | 5.32 | 0.1 | 187158.68 | 58.21 | n/a |
| REDUSDT | IDLE | 1.04 | 8.04 | 7.44 | 0.17 | 157657.02 | 25.46 | tvl≈2,314,909 |
| KITEUSDT | IDLE | 1.86 | 6.62 | 1.45 | 0.13 | 68421.75 | 28.44 | no_map |
| RWAINCUSDT | IDLE | 2.41 | 4.48 | 2.3 | 0.02 | 10365.52 | 48.04 | no_map |
| EDELUSDT | IDLE | 1.57 | 3.28 | 1.2 | -0.03 | 81164.71 | 44.4 | no_map |
| QAITUSDT | IDLE | 1.76 | 3.24 | 1.8 | -0.02 | 3417.27 | 35.86 | no_map |
| RIZEUSDT | IDLE | 1.09 | 4.41 | 3.88 | 0.09 | 58685.68 | 44.52 | no_map |
| TELUSDT | IDLE | 1.98 | 5.52 | 0.89 | 0.1 | 184151.14 | 44.79 | no_map |
| RWAUSDT | IDLE | 1.71 | 3.38 | 0.24 | 0.07 | 56918.8 | 7.98 | no_map |
| FLUIDUSDT | IDLE | 0.88 | 2.07 | 2.03 | 0.08 | 3692.42 | 26.67 | tvl≈2,594,231,317 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
