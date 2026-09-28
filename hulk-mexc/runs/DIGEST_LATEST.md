# Hulk DIGEST — 2026-09-28T07:18:55Z

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
| WUSDT | IDLE | 2.09 | 6.69 | 6.07 | -0.04 | 4768552.7 | 9.12 | tvl≈1,869,780,636 |
| PYTHUSDT | IDLE | 2.48 | 6.54 | 3.22 | -0.05 | 1883004.42 | 3.65 | tvl≈186,631,590 |
| XRPUSDT | IDLE | 1.71 | 3.07 | 2.39 | -0.03 | 51486413.45 | 0.68 | n/a |
| QNTUSDT | IDLE | 0.53 | 17.68 | 3.45 | 0.59 | 16753335.48 | 11.42 | n/a |
| BTCUSDT | IDLE | 0.72 | 1.33 | 0.76 | -0.02 | 575424702.45 | 0.0 | no_map |
| ETHUSDT | IDLE | 0.53 | 0.99 | 0.47 | -0.02 | 281970389.55 | 0.04 | no_map |
| CCUSDT | IDLE | 3.86 | 9.05 | 4.48 | 0.04 | 876940.77 | 10.08 | no_map |
| HBARUSDT | IDLE | 2.84 | 5.6 | 0.52 | 0.05 | 1378283.39 | 11.13 | empty_tvl |
| BIOUSDT | IDLE | 2.71 | 5.02 | 4.71 | -0.06 | 99560.06 | 6.69 | n/a |
| KITEUSDT | IDLE | 2.01 | 4.28 | 3.96 | -0.08 | 106764.72 | 11.28 | no_map |
| EDELUSDT | IDLE | 1.24 | 6.77 | 3.09 | -0.13 | 187541.55 | 19.97 | no_map |
| REDUSDT | IDLE | 1.87 | 4.12 | 3.95 | -0.06 | 65202.26 | 13.6 | tvl≈2,995,392 |
| RIZEUSDT | IDLE | 1.56 | 9.18 | 6.25 | -0.14 | 59196.78 | 54.55 | no_map |
| CHIPUSDT | IDLE | 1.24 | 3.38 | 2.85 | -0.08 | 87091.74 | 15.7 | no_map |
| ZBCNUSDT | IDLE | 0.63 | 1.11 | 1.02 | -0.03 | 244268.29 | 18.28 | n/a |
| FLUIDUSDT | IDLE | 2.73 | 4.78 | 4.57 | -0.03 | 3554.0 | 21.98 | tvl≈2,581,066,825 |
| TELUSDT | IDLE | 1.51 | 3.16 | 2.31 | 0.04 | 172307.08 | 38.41 | no_map |
| RWAINCUSDT | IDLE | 0.6 | 5.57 | 5.27 | 0.17 | 31979.38 | 61.24 | no_map |
| MNSRYUSDT | IDLE | 1.04 | 1.88 | 1.32 | -0.0 | 38213.35 | 24.37 | no_map |
| RWAUSDT | IDLE | 0.67 | 1.22 | 0.78 | -0.01 | 59506.78 | 21.5 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
