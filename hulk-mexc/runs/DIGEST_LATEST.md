# Hulk DIGEST — 2026-08-22T07:59:55Z

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
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 4.12 | 19.14 | 8.49 | 0.01 | 24460915.0 | 5.87 | tvl≈113,478,518 |
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.41 | 23.87 | 7.87 | 0.19 | 224146827.3 | 3.84 | n/a |
| HBARUSDT | WATCH_PULLBACK — tension haute + reflux | 4.3 | 15.8 | 9.67 | 0.04 | 1349911.4 | 5.09 | empty_tvl |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 24.54 | 11.91 | -0.09 | 686807.28 | 3.34 | no_map |
| WUSDT | WATCH_PULLBACK — tension haute + reflux | 4.29 | 17.58 | 8.26 | 0.04 | 615195.15 | 15.58 | tvl≈1,610,281,058 |
| BIOUSDT | WATCH_PULLBACK — tension haute + reflux | 4.19 | 29.98 | 9.64 | -0.04 | 247493.4 | 3.19 | n/a |
| REDUSDT | WATCH_PULLBACK — tension haute + reflux | 3.15 | 42.01 | 11.44 | 0.06 | 158019.88 | 9.64 | tvl≈2,081,438 |
| CCUSDT | IDLE | 2.03 | 11.25 | 2.52 | 0.2 | 811602.25 | 7.36 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 3.27 | 8.47 | 6.16 | 0.03 | 537698.47 | 15.51 | n/a |
| QNTUSDT | WATCH_PULLBACK — tension haute + reflux | 4.37 | 13.91 | 8.67 | 0.04 | 194446.67 | 6.18 | n/a |
| KITEUSDT | IDLE | 3.45 | 9.68 | 3.95 | 0.08 | 74120.34 | 9.09 | no_map |
| EDELUSDT | IDLE | 2.23 | 4.52 | 2.7 | -0.03 | 87059.38 | 44.4 | no_map |
| FLUIDUSDT | IDLE | 3.33 | 7.38 | 4.01 | 0.04 | 6888.1 | 21.19 | tvl≈2,556,699,557 |
| RWAINCUSDT | IDLE | 2.48 | 4.48 | 3.24 | 0.02 | 11276.39 | 112.81 | no_map |
| TELUSDT | IDLE | 2.09 | 5.36 | 4.15 | -0.01 | 174945.4 | 36.05 | no_map |
| QAITUSDT | IDLE | 1.69 | 3.32 | 0.35 | 0.01 | 3170.95 | 67.05 | no_map |
| RIZEUSDT | IDLE | 0.91 | 3.99 | 0.98 | 0.01 | 52392.53 | 41.01 | no_map |
| RWAUSDT | IDLE | 1.72 | 3.29 | 0.96 | 0.05 | 58427.5 | 16.1 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
