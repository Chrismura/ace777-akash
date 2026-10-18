# Hulk DIGEST — 2026-10-18T01:25:24Z

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
| ETHUSDT | IDLE | 1.45 | 2.79 | 0.69 | -0.01 | 89999172.69 | 0.17 | no_map |
| XRPUSDT | IDLE | 1.42 | 2.74 | 0.65 | -0.01 | 17331765.94 | 0.77 | n/a |
| PYTHUSDT | WATCH_PULLBACK — tension haute + reflux | 3.21 | 9.68 | 6.54 | -0.09 | 1047242.53 | 1.27 | tvl≈185,824,620 |
| BTCUSDT | IDLE | 0.54 | 1.06 | 0.1 | 0.0 | 170583818.17 | 0.0 | no_map |
| WUSDT | IDLE | 1.58 | 4.69 | 2.7 | -0.04 | 1048282.48 | 15.28 | tvl≈1,583,341,296 |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 3.21 | 10.34 | 8.01 | -0.1 | 156619.76 | 15.14 | no_map |
| QNTUSDT | IDLE | 2.7 | 5.15 | 1.73 | -0.01 | 580856.26 | 1.01 | n/a |
| ZBCNUSDT | IDLE | 1.98 | 3.48 | 3.25 | -0.04 | 180458.03 | 12.79 | n/a |
| BIOUSDT | IDLE | 2.31 | 4.41 | 1.34 | -0.03 | 71673.62 | 4.11 | n/a |
| CCUSDT | IDLE | 1.5 | 2.74 | 1.72 | 0.0 | 248484.8 | 7.74 | no_map |
| CHIPUSDT | IDLE | 1.92 | 5.54 | 1.54 | -0.07 | 83846.03 | 11.48 | no_map |
| HBARUSDT | IDLE | 2.54 | 5.01 | 0.5 | 0.03 | 270330.52 | 8.1 | empty_tvl |
| REDUSDT | IDLE | 1.81 | 3.41 | 1.36 | -0.04 | 60612.11 | 15.77 | tvl≈3,523,275 |
| KITEUSDT | IDLE | 1.49 | 3.79 | 1.84 | -0.05 | 68807.33 | 10.33 | no_map |
| RWAINCUSDT | IDLE | 1.13 | 3.53 | 1.91 | 0.06 | 20763.57 | 5.27 | no_map |
| TELUSDT | IDLE | 2.05 | 3.59 | 3.41 | -0.06 | 102696.1 | 24.74 | no_map |
| RIZEUSDT | IDLE | 0.95 | 1.81 | 0.54 | 0.0 | 45812.33 | 58.86 | no_map |
| RWAUSDT | IDLE | 1.24 | 2.35 | 0.87 | -0.01 | 51591.61 | 16.01 | no_map |
| FLUIDUSDT | IDLE | 1.42 | 2.69 | 0.97 | -0.02 | 1730.78 | 21.57 | tvl≈2,230,755,732 |
| MNSRYUSDT | IDLE | 0.33 | 0.58 | 0.55 | -0.0 | 30679.11 | 5.66 | no_map |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
