# Hulk DIGEST — 2026-09-15T16:46:01Z

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
| XRPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.3 | 6.39 | 5.18 | -0.02 | 82189319.82 | 2.89 | n/a |
| ETHUSDT | IDLE | 1.92 | 4.09 | 2.67 | -0.04 | 501513730.74 | 0.33 | no_map |
| BTCUSDT | IDLE | 1.16 | 2.15 | 1.12 | -0.03 | 578791110.06 | 0.0 | no_map |
| EDELUSDT | IDLE | 1.77 | 22.79 | 17.71 | 0.24 | 461565.38 | 48.79 | no_map |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 4.16 | 8.41 | 5.48 | -0.02 | 209348.73 | 22.79 | n/a |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 3.56 | 11.92 | 9.4 | -0.1 | 94470.36 | 13.33 | no_map |
| CCUSDT | IDLE | 1.91 | 3.41 | 2.74 | -0.04 | 338460.65 | 6.45 | no_map |
| HBARUSDT | IDLE | 2.25 | 4.08 | 2.78 | 0.0 | 469180.02 | 1.29 | empty_tvl |
| PYTHUSDT | IDLE | 1.68 | 3.47 | 0.2 | -0.02 | 298384.87 | 1.83 | tvl≈120,975,427 |
| KITEUSDT | IDLE | 2.41 | 4.4 | 2.81 | -0.01 | 62658.0 | 13.43 | no_map |
| WUSDT | IDLE | 1.63 | 3.44 | 2.04 | -0.05 | 182707.69 | 8.41 | tvl≈1,433,457,709 |
| RWAINCUSDT | IDLE | 2.42 | 4.35 | 3.33 | -0.05 | 8125.88 | 22.95 | no_map |
| REDUSDT | IDLE | 1.06 | 5.38 | 4.82 | -0.05 | 104244.01 | 18.13 | tvl≈2,494,935 |
| BIOUSDT | IDLE | 1.49 | 2.84 | 0.87 | -0.02 | 82920.93 | 11.96 | n/a |
| RIZEUSDT | IDLE | 1.21 | 10.95 | 7.53 | 0.04 | 54731.79 | 83.09 | no_map |
| FLUIDUSDT | IDLE | 1.57 | 2.82 | 2.2 | -0.04 | 2071.8 | 22.0 | tvl≈2,641,869,823 |
| TELUSDT | IDLE | 1.34 | 4.37 | 2.92 | -0.04 | 100047.12 | 71.78 | no_map |
| QNTUSDT | IDLE | 1.17 | 2.22 | 0.78 | -0.03 | 50444.95 | 6.38 | n/a |
| RWAUSDT | IDLE | 0.36 | 0.68 | 0.22 | -0.01 | 51918.34 | 14.98 | no_map |
| MNSRYUSDT | IDLE | 0.57 | 1.04 | 0.62 | -0.0 | 32628.79 | 55.8 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
