# Hulk DIGEST — 2026-08-22T08:11:58Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.14 | 19.14 | 8.99 | 0.01 | 26143823.06 | 1.97 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.75 | 23.87 | 8.82 | 0.16 | 224988691.49 | 4.52 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 15.8 | 9.37 | 0.04 | 1357397.36 | 7.62 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 24.54 | 11.38 | -0.09 | 683169.31 | 6.64 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.27 | 17.58 | 7.65 | 0.05 | 609684.83 | 13.41 | tvl≈1,610,281,058 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.17 | 29.98 | 8.49 | -0.04 | 247370.42 | 12.6 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 42.01 | 11.21 | 0.06 | 154749.77 | 9.61 | tvl≈2,081,438 |
| CCUSDT | IMPULSE_WAIT — spike en cours, pas chase | 2.04 | 11.25 | 1.93 | 0.2 | 818890.74 | 9.78 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.25 | 8.47 | 5.73 | 0.03 | 537311.68 | 37.39 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.36 | 13.91 | 8.36 | 0.03 | 194132.96 | 6.15 | n/a |
| KITEUSDT | IDLE | 3.81 | 9.68 | 3.96 | 0.07 | 72938.4 | 12.69 | no_map |
| FLUIDUSDT | IDLE | 3.75 | 7.38 | 4.01 | 0.04 | 6888.1 | 18.84 | tvl≈2,556,699,557 |
| EDELUSDT | IDLE | 2.22 | 4.52 | 2.59 | -0.03 | 86948.87 | 89.09 | no_map |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.01 | 11250.14 | 112.81 | no_map |
| TELUSDT | IDLE | 1.85 | 4.7 | 4.0 | -0.01 | 173753.19 | 51.36 | no_map |
| RIZEUSDT | IDLE | 0.85 | 3.73 | 0.85 | 0.0 | 52293.21 | 44.42 | no_map |
| RWAUSDT | IDLE | 1.71 | 3.29 | 0.8 | 0.05 | 58228.52 | 24.13 | no_map |
| QAITUSDT | IDLE | 0.99 | 1.92 | 0.35 | 0.01 | 3170.95 | 67.05 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
