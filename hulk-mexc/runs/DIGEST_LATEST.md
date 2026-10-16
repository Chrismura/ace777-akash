# Hulk DIGEST — 2026-10-16T14:44:23Z

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
| PYTHUSDT | IDLE | 2.27 | 8.83 | 4.86 | 0.02 | 3572091.64 | 6.72 | tvl≈206,072,259 |
| WUSDT | IDLE | 1.96 | 3.9 | 0.2 | 0.04 | 1746121.23 | 20.75 | tvl≈1,663,326,925 |
| ETHUSDT | IDLE | 1.03 | 1.96 | 0.72 | 0.04 | 222747054.62 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.98 | 1.81 | 1.02 | 0.01 | 23641007.36 | 0.75 | n/a |
| BTCUSDT | IDLE | 0.8 | 1.49 | 0.69 | 0.01 | 371741921.55 | 0.0 | no_map |
| QNTUSDT | IDLE | 2.14 | 3.89 | 2.54 | 0.04 | 1117145.66 | 2.41 | n/a |
| CCUSDT | IDLE | 1.84 | 3.49 | 1.25 | -0.03 | 409529.32 | 10.46 | no_map |
| RWAINCUSDT | WATCH_PULLBACK — tension haute + reflux | 2.86 | 8.9 | 8.02 | -0.08 | 26153.02 | 16.15 | no_map |
| RIZEUSDT | IMPULSE_WAIT — spike en cours, pas chase | 3.09 | 9.55 | 1.66 | 0.04 | 69824.26 | 59.01 | no_map |
| CHIPUSDT | IDLE | 2.04 | 6.21 | 5.09 | 0.05 | 168397.72 | 10.47 | no_map |
| ZBCNUSDT | IDLE | 1.61 | 2.99 | 1.56 | 0.04 | 192960.39 | 19.03 | n/a |
| EDELUSDT | IDLE | 1.2 | 3.22 | 0.23 | 0.0 | 217763.15 | 19.51 | no_map |
| REDUSDT | IDLE | 1.59 | 4.67 | 0.64 | 0.0 | 91273.0 | 14.39 | tvl≈3,681,377 |
| KITEUSDT | IDLE | 1.51 | 2.74 | 1.9 | 0.01 | 68978.29 | 11.45 | no_map |
| BIOUSDT | IDLE | 1.43 | 2.59 | 1.76 | 0.02 | 63167.73 | 3.89 | n/a |
| HBARUSDT | IDLE | 0.93 | 1.76 | 0.69 | 0.05 | 285654.03 | 6.93 | empty_tvl |
| TELUSDT | IDLE | 1.05 | 2.03 | 0.5 | 0.04 | 93805.6 | 33.31 | no_map |
| FLUIDUSDT | IDLE | 1.29 | 2.36 | 1.52 | -0.01 | 6444.09 | 21.32 | tvl≈2,260,925,316 |
| RWAUSDT | IDLE | 0.26 | 0.47 | 0.31 | 0.01 | 51869.41 | 7.89 | no_map |
| MNSRYUSDT | IDLE | 0.11 | 0.21 | 0.13 | 0.01 | 38695.43 | 11.3 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
