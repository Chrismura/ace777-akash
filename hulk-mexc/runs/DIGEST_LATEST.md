# Hulk DIGEST — 2026-08-30T16:34:22Z

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
| ETHUSDT | IDLE | 1.24 | 2.48 | 0.03 | 0.03 | 182941479.78 | 0.04 | no_map |
| XRPUSDT | IDLE | 0.8 | 1.57 | 0.14 | 0.01 | 18676669.15 | 2.13 | n/a |
| BTCUSDT | IDLE | 0.73 | 1.44 | 0.12 | 0.01 | 265556887.39 | 0.0 | no_map |
| CHIPUSDT | WATCH_PULLBACK — tension haute + reflux | 4.21 | 8.01 | 5.86 | -0.04 | 565706.77 | 2.5 | no_map |
| PYTHUSDT | IDLE | 3.14 | 5.93 | 2.33 | 0.02 | 404150.04 | 2.04 | tvl≈107,930,951 |
| ZBCNUSDT | WATCH_PULLBACK — tension haute + reflux | 4.09 | 7.84 | 6.59 | -0.07 | 177975.55 | 23.88 | n/a |
| EDELUSDT | IDLE | 2.09 | 5.99 | 3.88 | 0.07 | 72369.11 | 16.79 | no_map |
| WUSDT | IDLE | 1.33 | 2.63 | 0.15 | 0.04 | 216646.43 | 12.56 | tvl≈1,543,338,227 |
| CCUSDT | IDLE | 0.9 | 1.62 | 1.18 | 0.02 | 260604.97 | 6.76 | no_map |
| REDUSDT | IDLE | 1.07 | 2.14 | 0.01 | 0.03 | 60429.65 | 9.89 | tvl≈2,031,180 |
| BIOUSDT | IDLE | 0.8 | 1.58 | 0.18 | -0.0 | 75581.32 | 3.62 | n/a |
| KITEUSDT | IDLE | 0.83 | 1.67 | 0.0 | -0.03 | 61578.13 | 22.36 | no_map |
| TELUSDT | IDLE | 1.96 | 3.85 | 0.41 | -0.01 | 82800.53 | 23.23 | no_map |
| RIZEUSDT | IDLE | 0.7 | 2.45 | 0.83 | -0.05 | 45984.25 | 58.56 | no_map |
| RWAINCUSDT | IDLE | 1.5 | 3.01 | 0.0 | 0.01 | 1670.4 | 127.74 | no_map |
| HBARUSDT | IDLE | 0.61 | 1.13 | 0.57 | -0.0 | 126713.4 | 1.33 | empty_tvl |
| MNSRYUSDT | IDLE | 0.75 | 1.41 | 0.54 | 0.01 | 33152.13 | 4.0 | no_map |
| RWAUSDT | IDLE | 0.58 | 1.15 | 0.08 | 0.02 | 53004.3 | 8.1 | no_map |
| QNTUSDT | IDLE | 0.59 | 1.14 | 0.27 | 0.01 | 38353.25 | 3.22 | n/a |
| FLUIDUSDT | IDLE | 0.86 | 1.73 | 0.0 | 0.03 | 3182.59 | 22.17 | tvl≈2,625,311,109 |

## Consignes Qwen (manuel — ne pilote pas le paper)
1. Résumer en 5 lignes : qui spike, qui dump, illiquide (spread/vol).
2. Noter 1–3 paires à surveiller dans `runs/VEILLE_QWEN_NOTES.md`.
3. Signaler murs ask/bid ou spread dangereux.
4. **Ne pas** envoyer d’ordres ; confrontation avec Hulk paper en fin de tests.

## Séparation des pistes
- **PISTE A — Hulk paper** : `python3 scripts/paper_diprip.py` (autonome)
- **PISTE B — Veille/Qwen** : ce digest (+ notes Qwen)
- Fin de campagne : `docs/CONFRONTATION.md`
