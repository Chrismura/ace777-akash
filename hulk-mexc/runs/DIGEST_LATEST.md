# Hulk DIGEST — 2026-08-19T16:11:33Z

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
| XRPUSDT | IDLE | 3.55 | 6.98 | 0.84 | 0.06 | 21257710.32 | 0.94 | n/a |
| BIOUSDT | IDLE | 3.68 | 19.06 | 2.74 | 0.16 | 114095.99 | 3.47 | n/a |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 19.8 | 9.62 | 0.06 | 143921.64 | 25.96 | no_map |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 4.06 | 12.24 | 5.85 | 0.05 | 19631.14 | 22.57 | no_map |
| QAITUSDT | IDLE | 4.27 | 11.42 | 4.92 | 0.01 | 10937.81 | 51.45 | no_map |
| EDELUSDT | IMPULSE_WAIT — spike en cours, pas chase | 4.04 | 8.27 | 1.38 | 0.05 | 65012.5 | 38.05 | no_map |
| PYTHUSDT | IDLE | 3.12 | 6.05 | 1.21 | 0.04 | 210581.48 | 2.5 | tvl≈86,796,791 |
| CHIPUSDT | IDLE | 2.86 | 9.02 | 4.36 | 0.03 | 172701.07 | 3.62 | no_map |
| ZBCNUSDT | IDLE | 3.04 | 7.07 | 0.76 | 0.08 | 196301.93 | 32.01 | n/a |
| KITEUSDT | IDLE | 3.42 | 6.67 | 1.11 | 0.04 | 56498.87 | 13.61 | no_map |
| WUSDT | IDLE | 2.91 | 5.59 | 1.54 | 0.03 | 146127.79 | 15.41 | tvl≈1,371,613,431 |
| CCUSDT | IDLE | 2.11 | 4.02 | 1.39 | 0.01 | 247404.52 | 9.75 | no_map |
| REDUSDT | IDLE | 2.42 | 6.88 | 0.91 | 0.0 | 113289.91 | 14.05 | tvl≈1,598,608 |
| FLUIDUSDT | IDLE | 3.42 | 7.79 | 1.61 | 0.04 | 1281.01 | 21.69 | tvl≈2,344,087,188 |
| RIZEUSDT | IDLE | 1.88 | 4.12 | 2.71 | -0.06 | 23867.67 | 52.46 | no_map |
| HBARUSDT | IDLE | 1.76 | 3.44 | 0.56 | 0.05 | 197366.26 | 1.44 | empty_tvl |
| QNTUSDT | IDLE | 1.9 | 3.71 | 0.58 | 0.03 | 37816.16 | 8.58 | n/a |
| RWAUSDT | IDLE | 0.82 | 1.58 | 0.35 | 0.0 | 53685.33 | 26.05 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
