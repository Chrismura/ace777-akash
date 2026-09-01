# Hulk DIGEST — 2026-09-01T08:23:32Z

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
| XRPUSDT | IDLE | 1.1 | 1.94 | 1.78 | 0.0 | 28815049.89 | 2.19 | n/a |
| BTCUSDT | IDLE | 0.78 | 1.37 | 1.2 | 0.0 | 553396366.11 | 0.0 | no_map |
| ETHUSDT | IDLE | 0.63 | 1.13 | 0.92 | 0.01 | 287237959.47 | 0.04 | no_map |
| EDELUSDT | WATCH_PULLBACK — tension haute + reflux | 4.37 | 29.11 | 18.26 | -0.02 | 173514.4 | 59.0 | no_map |
| CHIPUSDT | IDLE | 2.76 | 6.71 | 2.02 | -0.0 | 334145.0 | 12.61 | no_map |
| PYTHUSDT | IDLE | 1.69 | 3.98 | 3.5 | 0.04 | 523842.18 | 2.02 | tvl≈113,741,883 |
| REDUSDT | IDLE | 3.16 | 6.21 | 0.68 | 0.02 | 59446.94 | 9.85 | tvl≈1,986,510 |
| CCUSDT | IDLE | 1.47 | 2.66 | 1.85 | 0.01 | 388516.59 | 4.11 | no_map |
| WUSDT | IDLE | 2.25 | 4.22 | 1.92 | 0.02 | 223663.89 | 13.69 | tvl≈1,542,460,139 |
| ZBCNUSDT | IDLE | 1.42 | 2.49 | 2.35 | 0.04 | 192308.92 | 7.05 | n/a |
| RWAUSDT | WATCH_PULLBACK — tension haute + reflux | 2.58 | 8.02 | 7.21 | 0.06 | 64804.42 | 22.87 | no_map |
| RIZEUSDT | IDLE | 1.52 | 5.19 | 1.67 | -0.06 | 37434.81 | 68.9 | no_map |
| BIOUSDT | IDLE | 0.97 | 1.71 | 1.54 | -0.01 | 62496.08 | 3.8 | n/a |
| KITEUSDT | IDLE | 0.98 | 1.81 | 0.97 | -0.02 | 60888.0 | 10.11 | no_map |
| RWAINCUSDT | IDLE | 1.75 | 3.21 | 1.96 | -0.04 | 4866.11 | 105.26 | no_map |
| HBARUSDT | IDLE | 1.04 | 1.88 | 1.39 | 0.0 | 228567.75 | 1.35 | empty_tvl |
| TELUSDT | IDLE | 1.61 | 3.01 | 1.37 | 0.0 | 84167.96 | 40.66 | no_map |
| QNTUSDT | IDLE | 0.49 | 0.9 | 0.6 | 0.0 | 49873.79 | 1.63 | n/a |
| MNSRYUSDT | IDLE | 0.41 | 0.72 | 0.61 | -0.0 | 28719.64 | 33.85 | no_map |
| FLUIDUSDT | IDLE | 0.15 | 0.31 | 0.0 | -0.01 | 1146.31 | 21.45 | tvl≈2,609,010,605 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
