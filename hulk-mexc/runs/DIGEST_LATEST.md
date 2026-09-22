# Hulk DIGEST — 2026-09-22T04:08:48Z

> ⚠️ **SCAN DÉGRADÉ (réseau)** — données partielles, veille hors délai.

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
| XRPUSDT | IDLE | 1.72 | 4.36 | 3.0 | 0.08 | 115615394.33 | 2.63 | n/a |
| ETHUSDT | IDLE | 1.25 | 2.25 | 1.69 | 0.03 | 708802071.51 | 0.73 | no_map |
| BTCUSDT | IDLE | 0.9 | 1.63 | 1.16 | 0.05 | 1113605677.26 | 0.0 | no_map |
| HBARUSDT | IDLE | 1.6 | 3.93 | 0.06 | 0.09 | 1172462.04 | 1.06 | empty_tvl |
| PYTHUSDT | IDLE | 1.37 | 3.13 | 0.82 | 0.05 | 789871.12 | 4.66 | tvl≈142,076,380 |
| CCUSDT | IDLE | 1.65 | 3.01 | 1.93 | 0.04 | 665841.7 | 6.8 | no_map |
| RIZEUSDT | WATCH_PULLBACK — tension haute + reflux | 2.9 | 27.81 | 15.77 | -0.19 | 53585.38 | 146.65 | no_map |
| ZBCNUSDT | IDLE | 2.16 | 4.61 | 1.99 | 0.04 | 268152.06 | 9.3 | n/a |
| WUSDT | IDLE | 1.07 | 2.03 | 0.68 | -0.0 | 523678.16 | 2.52 | tvl≈1,803,003,578 |
| REDUSDT | IDLE | 2.16 | 4.16 | 1.04 | 0.03 | 98864.39 | 16.72 | tvl≈2,814,179 |
| CHIPUSDT | IDLE | 1.12 | 5.12 | 2.17 | 0.12 | 170725.84 | 16.97 | no_map |
| BIOUSDT | IDLE | 1.42 | 2.69 | 1.02 | 0.04 | 128946.74 | 10.32 | n/a |
| KITEUSDT | IDLE | 1.49 | 2.95 | 0.21 | 0.05 | 81341.02 | 11.46 | no_map |
| EDELUSDT | IDLE | 0.67 | 4.33 | 1.0 | 0.08 | 233723.04 | 25.96 | no_map |
| RWAINCUSDT | IDLE | 0.8 | 1.94 | 1.2 | 0.07 | 21728.15 | 22.22 | no_map |
| QNTUSDT | IDLE | 1.18 | 2.29 | 0.43 | 0.02 | 121170.57 | 8.95 | n/a |
| TELUSDT | IDLE | 1.15 | 3.3 | 2.23 | 0.06 | 117751.89 | 43.12 | no_map |
| FLUIDUSDT | IDLE | 0.64 | 1.33 | 1.02 | 0.08 | 12008.84 | 21.95 | tvl≈2,657,976,375 |
| RWAUSDT | ERR | — | — | — | — | — | — | scan_deadline |
| MNSRYUSDT | ERR | — | — | — | — | — | — | scan_deadline |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
