# Hulk DIGEST — 2026-09-17T22:17:29Z

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
| XRPUSDT | IDLE | 0.87 | 1.55 | 1.28 | 0.0 | 38418028.84 | 2.32 | n/a |
| ETHUSDT | IDLE | 0.84 | 1.46 | 1.44 | 0.02 | 299561659.51 | 0.04 | no_map |
| BTCUSDT | IDLE | 0.48 | 0.83 | 0.82 | 0.01 | 430744409.99 | 0.0 | no_map |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.44 | 40.44 | 12.97 | -0.18 | 278245.83 | 27.24 | no_map |
| PYTHUSDT | IDLE | 1.5 | 3.72 | 3.11 | 0.07 | 549401.72 | 1.8 | tvl≈125,357,356 |
| CCUSDT | IDLE | 1.21 | 2.28 | 0.93 | 0.04 | 559887.93 | 7.98 | no_map |
| WUSDT | IDLE | 1.55 | 4.65 | 2.13 | 0.11 | 326166.18 | 12.08 | tvl≈1,479,999,506 |
| HBARUSDT | IDLE | 1.49 | 2.61 | 2.51 | 0.02 | 547028.35 | 1.34 | empty_tvl |
| CHIPUSDT | IDLE | 1.46 | 4.49 | 4.27 | 0.04 | 143984.91 | 18.8 | no_map |
| ZBCNUSDT | IDLE | 1.3 | 2.38 | 1.49 | 0.02 | 199369.04 | 34.16 | n/a |
| BIOUSDT | IDLE | 1.24 | 2.17 | 2.12 | 0.01 | 67776.62 | 8.02 | n/a |
| TELUSDT | IDLE | 2.76 | 4.88 | 4.25 | -0.02 | 75295.16 | 63.27 | no_map |
| KITEUSDT | IDLE | 1.07 | 2.02 | 0.82 | 0.01 | 60656.69 | 10.41 | no_map |
| RIZEUSDT | IDLE | 1.03 | 7.03 | 3.7 | -0.07 | 43463.65 | 122.23 | no_map |
| RWAINCUSDT | IDLE | 0.72 | 1.25 | 1.23 | 0.0 | 14461.96 | 23.81 | no_map |
| REDUSDT | IDLE | 0.5 | 0.9 | 0.72 | 0.01 | 65604.66 | 23.93 | tvl≈2,360,052 |
| QNTUSDT | IDLE | 0.81 | 1.43 | 1.33 | 0.0 | 40005.46 | 4.93 | n/a |
| FLUIDUSDT | IDLE | 1.1 | 2.2 | 0.0 | 0.03 | 146.13 | 21.85 | tvl≈2,611,209,983 |
| RWAUSDT | IDLE | 0.31 | 0.6 | 0.07 | 0.0 | 57522.1 | 22.38 | no_map |
| MNSRYUSDT | IDLE | 0.03 | 0.06 | 0.03 | 0.02 | 43046.92 | 4.19 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
