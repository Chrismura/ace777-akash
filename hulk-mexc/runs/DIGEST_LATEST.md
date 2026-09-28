# Hulk DIGEST — 2026-09-28T22:32:02Z

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
| HBARUSDT | IDLE | 1.62 | 14.78 | 6.34 | 0.3 | 11717881.93 | 0.82 | empty_tvl |
| WUSDT | IDLE | 0.94 | 4.31 | 2.48 | -0.13 | 1890876.08 | 10.34 | tvl≈1,804,294,669 |
| QNTUSDT | IDLE | 0.69 | 12.53 | 9.6 | -0.04 | 20150188.4 | 8.13 | n/a |
| XRPUSDT | IDLE | 1.64 | 2.93 | 2.32 | -0.02 | 67686924.91 | 2.02 | n/a |
| ETHUSDT | IDLE | 1.15 | 2.05 | 1.61 | -0.0 | 401432234.47 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.85 | 1.51 | 1.31 | -0.02 | 839736657.89 | 0.0 | no_map |
| CCUSDT | IDLE | 1.46 | 5.38 | 3.83 | -0.06 | 1351361.89 | 4.67 | no_map |
| PYTHUSDT | IDLE | 1.66 | 3.6 | 0.9 | -0.04 | 1194649.28 | 2.49 | tvl≈177,971,605 |
| TELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.33 | 33.58 | 5.27 | 0.27 | 353128.15 | 54.98 | no_map |
| EDELUSDT | IDLE | 1.96 | 11.97 | 9.5 | 0.03 | 164203.54 | 22.51 | no_map |
| ZBCNUSDT | IDLE | 1.59 | 3.05 | 0.92 | -0.02 | 217896.37 | 13.33 | n/a |
| CHIPUSDT | IDLE | 1.72 | 3.87 | 3.59 | -0.07 | 75388.29 | 16.31 | no_map |
| KITEUSDT | IDLE | 1.37 | 4.87 | 4.54 | -0.12 | 101401.6 | 11.11 | no_map |
| RWAINCUSDT | IDLE | 2.53 | 6.31 | 0.27 | -0.01 | 16331.79 | 78.62 | no_map |
| BIOUSDT | IDLE | 0.98 | 2.76 | 2.45 | -0.08 | 115447.8 | 6.88 | n/a |
| REDUSDT | IDLE | 1.29 | 2.42 | 2.01 | -0.06 | 60533.05 | 8.18 | tvl≈2,919,893 |
| RIZEUSDT | IDLE | 1.54 | 5.77 | 0.64 | 0.12 | 45893.38 | 56.29 | no_map |
| FLUIDUSDT | IDLE | 0.98 | 2.23 | 2.11 | -0.05 | 4440.5 | 21.6 | tvl≈2,601,244,143 |
| RWAUSDT | IDLE | 0.61 | 1.08 | 1.0 | -0.02 | 58962.69 | 7.2 | no_map |
| MNSRYUSDT | IDLE | 0.42 | 0.75 | 0.56 | -0.02 | 34365.83 | 19.35 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
